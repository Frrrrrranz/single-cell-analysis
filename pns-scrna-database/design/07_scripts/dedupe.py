#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dedupe.py · 数据集去重 / 镜像合并器（确定性任务，不调用 LLM）

用途
----
以 datasets.dataset_id（GSE 号优先）为唯一键，做两类事：
  1. 库内自检/修复（--check / --apply）：扫描 db/datasets.csv，发现重复 dataset_id
     行 → 合并它们的 paper_ids（并集），保留首行其余字段，删除重复行；并修复
     papers.dataset_ids 与 datasets.paper_ids 的双向镜像一致性。
  2. 入库前预演（--merge JSON --paper-id P0001）：纯 dry-run，判断该 per-dataset
     提取 JSON 是「新建数据集」还是「仅追加 paper_ids」，给出决策报告。
     **不写任何文件**——真正落库由 ingest.py 负责（避免两脚本都写镜像而冲突）。

输入 JSON 结构（--merge，与 05_extraction.md / ingest.py 一致）
---------------------------------------------------------------
  per-dataset：{ "dataset_id", "dataset":{}, "cell_types":[], "processing":{}, ... }
  提取 JSON 不含 paper，故 --merge 必须配合 --paper-id 指明所属文章。

设计原则
--------
  - 本脚本聚焦「去重决策」与「镜像一致性」；真正写 cell_types/processing + SQLite 的是 ingest.py。
  - --apply 仅安全改写 papers.csv / datasets.csv 的 *_ids 多值列与去重行，
    不触碰 cell_types / processing（避免破坏主键序号）。
  - 幂等：对已去重的库重复运行不产生变化。

用法示例
--------
  python dedupe.py --db D:/database/db --check                         # 库内去重自检（只报告）
  python dedupe.py --db D:/database/db --apply                         # 库内去重 + 镜像修复并写回（先备份 .bak）
  python dedupe.py --db D:/database/db --merge extracted/GSE190000.json --paper-id P0007   # 入库前预演

退出码：0 = 成功（或仅报告）；1 = 发现需人工介入的冲突；2 = IO/解析错误。
"""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import sys
from pathlib import Path
from typing import Any

NA: str = "NA"

# 4 张 CSV 的表头（与 01_schema.md 完全一致）
HEADERS: dict[str, list[str]] = {
    "papers": ["paper_id", "title", "first_author", "corresponding", "year",
               "journal", "doi", "pmid", "url", "species", "has_scrna",
               "dataset_ids", "status", "source", "suppl_path", "notes"],
    "datasets": ["dataset_id", "repository", "accession_url", "platform",
                 "vendor", "species", "tissue", "condition", "n_cells",
                 "n_samples", "data_availability", "paper_ids"],
    "cell_types": ["ct_id", "dataset_id", "cell_type", "is_pns_cell",
                   "subtype", "markers", "species", "n_cells_or_pct",
                   "annotation_method", "provenance"],
    "processing": ["proc_id", "dataset_id", "paper_id", "qc", "normalization",
                   "batch_correction", "dim_reduction", "clustering",
                   "annotation", "diff_expr", "trajectory", "cell_comm",
                   "software", "provenance"],
}


# ----------------------------------------------------------------------------
# CSV 读写（UTF-8 无 BOM，RFC4180）
# ----------------------------------------------------------------------------
def read_csv(path: Path) -> list[dict[str, str]]:
    """读取 CSV → list[dict]。文件不存在返回空列表。"""
    p = Path(path)
    if not p.exists():
        return []
    with p.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, header: list[str], rows: list[dict[str, Any]]) -> None:
    r"""写回 CSV（UTF-8 无 BOM、\n 换行、RFC4180 转义）。"""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header,
                                lineterminator="\n",
                                quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, NA) for k in header})


# ----------------------------------------------------------------------------
# 多值字段工具
# ----------------------------------------------------------------------------
def parse_multi(value: Any) -> list[str]:
    """'P0001;P0007' → ['P0001','P0007']；NA/空 → []。"""
    if value is None or value == "" or value == NA:
        return []
    return [t for t in str(value).split(";") if t != ""]


def join_multi(tokens: list[str]) -> str:
    """token 列表 → 分号字符串；空列表 → NA。保序去重。"""
    seen: set[str] = set()
    ordered: list[str] = []
    for t in tokens:
        if t not in seen:
            seen.add(t)
            ordered.append(t)
    return ";".join(ordered) if ordered else NA


def union_multi(*values: Any) -> str:
    """合并多个多值字段为保序并集字符串。"""
    tokens: list[str] = []
    for v in values:
        tokens.extend(parse_multi(v))
    return join_multi(tokens)


# ----------------------------------------------------------------------------
# 1) 库内 datasets 去重（合并重复 dataset_id 行）
# ----------------------------------------------------------------------------
def dedupe_datasets_rows(datasets: list[dict[str, Any]],
                         conflicts: list[str]) -> list[dict[str, Any]]:
    """
    合并重复 dataset_id 行：保留首次出现的行，把后续同 id 行的 paper_ids 并入。
    关键字段不一致时记录冲突（交人工），保留首行值。返回去重后的行列表。
    """
    merged: dict[str, dict[str, Any]] = {}
    order: list[str] = []
    KEY_FIELDS = ["repository", "species", "tissue", "platform", "data_availability"]

    for row in datasets:
        did = (row.get("dataset_id") or "").strip()
        if did == "" or did == NA:
            conflicts.append(f"datasets 存在空 dataset_id 行，已跳过：{row}")
            continue
        if did not in merged:
            merged[did] = dict(row)
            order.append(did)
        else:
            base = merged[did]
            base["paper_ids"] = union_multi(base.get("paper_ids"), row.get("paper_ids"))
            for kf in KEY_FIELDS:
                a = (base.get(kf) or "").strip()
                b = (row.get(kf) or "").strip()
                if a != b and b not in ("", NA):
                    conflicts.append(
                        f"dataset_id={did} 字段 {kf} 冲突：保留 {a!r}，"
                        f"忽略重复行的 {b!r}（请人工确认）")

    return [merged[d] for d in order]


# ----------------------------------------------------------------------------
# 2) 镜像一致性修复：papers.dataset_ids <-> datasets.paper_ids
# ----------------------------------------------------------------------------
def rebuild_mirror(papers: list[dict[str, Any]], datasets: list[dict[str, Any]],
                   conflicts: list[str]) -> None:
    """以「双向并集」为准重建镜像，使两侧完全对齐。引用不存在主键的情况记入 conflicts。"""
    paper_ids_set = {(p.get("paper_id") or "").strip() for p in papers}
    dataset_ids_set = {(d.get("dataset_id") or "").strip() for d in datasets}

    ds_to_papers: dict[str, set[str]] = {(d.get("dataset_id") or "").strip(): set()
                                         for d in datasets}
    pp_to_datasets: dict[str, set[str]] = {(p.get("paper_id") or "").strip(): set()
                                           for p in papers}

    for d in datasets:
        did = (d.get("dataset_id") or "").strip()
        for pid in parse_multi(d.get("paper_ids")):
            if pid not in paper_ids_set:
                conflicts.append(f"datasets[{did}].paper_ids 引用了不存在的 paper {pid!r}")
                continue
            ds_to_papers[did].add(pid)
            pp_to_datasets[pid].add(did)

    for p in papers:
        pid = (p.get("paper_id") or "").strip()
        for did in parse_multi(p.get("dataset_ids")):
            if did not in dataset_ids_set:
                conflicts.append(f"papers[{pid}].dataset_ids 引用了不存在的 dataset {did!r}")
                continue
            ds_to_papers[did].add(pid)
            pp_to_datasets[pid].add(did)

    for d in datasets:
        did = (d.get("dataset_id") or "").strip()
        d["paper_ids"] = join_multi(sorted(ds_to_papers.get(did, set())))
    for p in papers:
        pid = (p.get("paper_id") or "").strip()
        p["dataset_ids"] = join_multi(sorted(pp_to_datasets.get(pid, set())))


# ----------------------------------------------------------------------------
# 3) 入库前预演（per-dataset，纯 dry-run，不写文件）
# ----------------------------------------------------------------------------
def plan_merge_json(payload: dict[str, Any], paper_id: str,
                    datasets: list[dict[str, Any]]) -> list[str]:
    """
    判断本 per-dataset 提取 JSON 的 dataset 是「新建」还是「仅追加 paper_ids」。
    返回人类可读决策列表。不改任何文件（真正落库交 ingest.py）。
    """
    existing_ds = {(d.get("dataset_id") or "").strip() for d in datasets}
    plan: list[str] = []

    did = (payload.get("dataset_id")
           or (payload.get("dataset") or {}).get("dataset_id") or "").strip()
    if did == "" or did == NA:
        plan.append("[跳过] 提取 JSON 缺少 dataset_id")
        return plan

    if did in existing_ds:
        plan.append(
            f"[已存在] {did}：仅追加 paper_ids+={paper_id}，"
            f"papers[{paper_id}].dataset_ids+={did}；不重复写 cell_types/processing。")
    else:
        n_ct = len(payload.get("cell_types") or [])
        n_proc = 1 if (payload.get("processing") or {}) else 0
        plan.append(
            f"[新建] {did}：新增 datasets 行 + {n_ct} 条 cell_types + "
            f"{n_proc} 条 processing（交 ingest.py 落库赋号）。")
    return plan


# ----------------------------------------------------------------------------
# 备份
# ----------------------------------------------------------------------------
def backup(path: Path) -> None:
    """复制为 .bak（若源文件存在）。"""
    p = Path(path)
    if p.exists():
        shutil.copy2(p, p.with_suffix(p.suffix + ".bak"))


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------
def main() -> int:
    parser = argparse.ArgumentParser(
        description="datasets 去重 + papers/datasets 镜像一致性修复（不用 LLM）。")
    parser.add_argument("--db", required=True, help="数据库 CSV 目录，如 D:/database/db")
    parser.add_argument("--paper-id", metavar="P0001",
                        help="--merge 时该提取所属文章的 paper_id（提取 JSON 不含 paper）")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true",
                       help="只检查并报告库内重复/不一致，不改文件")
    group.add_argument("--apply", action="store_true",
                       help="执行库内去重 + 镜像修复并写回（先备份 .bak）")
    group.add_argument("--merge", metavar="JSON",
                       help="入库前预演：判断该 per-dataset JSON 是新建还是追加（纯 dry-run，不写文件）")
    args = parser.parse_args()

    db = Path(args.db)
    papers_csv = db / "papers.csv"
    datasets_csv = db / "datasets.csv"

    try:
        papers = read_csv(papers_csv)
        datasets = read_csv(datasets_csv)
    except OSError as e:
        print(f"[ERROR] 读取 CSV 失败：{e}", file=sys.stderr)
        return 2

    conflicts: list[str] = []

    # --- 模式 3：并入 JSON 预演（纯 dry-run）---
    if args.merge:
        if not args.paper_id:
            parser.error("--merge 需要配合 --paper-id 指明所属文章")
            return 2
        try:
            payload = json.loads(Path(args.merge).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            print(f"[ERROR] 读取/解析 JSON 失败：{e}", file=sys.stderr)
            return 2

        paper_id = args.paper_id.strip()
        plan = plan_merge_json(payload, paper_id, datasets)
        print(f"[MERGE 预演 · dry-run] 文章 {paper_id}：")
        for line in plan:
            print(f"  {line}")
        print("提示：本命令不写文件。确认后用 ingest.py --json ... --paper-id ... 实际落库。")
        return 0

    # --- 模式 1/2：库内去重 ---
    deduped = dedupe_datasets_rows(datasets, conflicts)
    n_removed = len(datasets) - len(deduped)
    rebuild_mirror(papers, deduped, conflicts)

    print(f"[去重] datasets 原 {len(datasets)} 行 → 去重后 {len(deduped)} 行"
          f"（合并删除 {n_removed} 行重复 dataset_id）。")
    if conflicts:
        print(f"[一致性] 发现 {len(conflicts)} 处需人工确认：")
        for c in conflicts:
            print(f"  - {c}")
    else:
        print("[一致性] 镜像与引用全部一致。")

    if args.apply:
        backup(papers_csv)
        backup(datasets_csv)
        write_csv(datasets_csv, HEADERS["datasets"], deduped)
        write_csv(papers_csv, HEADERS["papers"], papers)
        print("[写回] 已更新 datasets.csv / papers.csv（原文件备份为 .bak）。")
    else:
        print("[check] 仅报告，未改文件。加 --apply 写回。")

    return 1 if conflicts else 0


if __name__ == "__main__":
    sys.exit(main())
