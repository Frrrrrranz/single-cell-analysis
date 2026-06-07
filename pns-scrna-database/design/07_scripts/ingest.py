#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ingest.py · 入库器（确定性任务，不调用 LLM）

用途
----
把一份「校验通过」的 per-dataset 提取 JSON（结构见 05_extraction.md §2）写入
D:/database/db/ 下的 4 张 CSV，并从 4 张 CSV 重建 database.sqlite。

输入 JSON 结构（per-dataset，与 05_extraction.md / validate.py 严格一致）
-------------------------------------------------------------------------
{
  "dataset_id": "GSE190000",
  "dataset":    { ...datasets 表字段(不含 paper_ids)... },
  "cell_types": [ { ...cell_types 行(不含 ct_id/dataset_id)... }, ... ],
  "processing": { ...processing 方法列(不含 proc_id/dataset_id/paper_id)... },
  "_self_check":{ "qualified": "true/false", ... }
}

关键约定
--------
  - 文章在预筛阶段已写入 papers.csv，故提取 JSON **不含 paper**；本脚本通过
    命令行 **--paper-id P0001** 关联该已存在文章，回填镜像并把其 status 推进到
    `extracted`。
  - 若该 paper_id 尚不在 papers.csv（如黄金标准首测），可用 --paper-meta meta.json
    提供其题录字段以新建该 paper 行（meta.json 字段同 papers 表）。
  - 内部 ID（ct_id/proc_id）由本脚本以 "__AUTO__" 占位统一赋号（C00001/X00001）。
  - 去重核心 = dataset_id：已存在 → 仅追加 paper_ids（不重复 cell_types；processing
    可因不同文章的再分析而新增一行）。

幂等
----
  - datasets 以 dataset_id 去重；cell_types 仅在「数据集首次入库」时写入，并以内容
    指纹双保险；processing 以 (dataset_id, paper_id, 方法指纹) 去重。
  - 重复运行同一 JSON 不产生重复行。

用法示例
--------
  # 把一份提取 JSON 入库（关联已预筛登记的 P0001）
  python ingest.py --db D:/database/db --json extracted/GSE190000.json --paper-id P0001

  # 黄金标准首测：paper 尚未登记，用 meta 新建
  python ingest.py --db D:/database/db --json extracted/GSE190000.json \
                   --paper-id P0001 --paper-meta meta/P0001.json

  # 仅由现有 4 张 CSV 重建 sqlite
  python ingest.py --db D:/database/db --rebuild-only

退出码：0 = 成功；1 = 业务冲突（外键缺失/未登记/自检不合格等）；2 = IO/解析错误。
"""

from __future__ import annotations

import argparse
import csv
import json
import sqlite3
import sys
from pathlib import Path
from typing import Any

NA: str = "NA"
AUTO: str = "__AUTO__"

# 4 张 CSV 表头（逐字与 01_schema.md 一致）
HEADERS: dict[str, list[str]] = {
    "papers": ["paper_id", "title", "first_author", "corresponding", "year",
               "journal", "doi", "pmid", "url", "species", "has_scrna",
               "dataset_ids", "status", "source", "suppl_path", "notes"],
    "datasets": ["dataset_id", "repository", "accession_url", "platform",
                 "vendor", "species", "tissue", "condition", "n_cells",
                 "n_samples", "data_availability", "paper_ids"],
    "cell_types": ["ct_id", "dataset_id", "paper_id", "cell_type", "is_pns_cell",
                   "subtype", "markers", "species", "n_cells_or_pct",
                   "annotation_method", "provenance"],
    "cell_subtypes": ["subtype_id", "dataset_id", "paper_id", "parent_cell_type", "subtype",
                      "is_pns_cell", "species", "condition_specificity", "markers",
                      "functional_signature", "n_cells_or_pct", "lineage", "provenance"],
    "processing": ["proc_id", "dataset_id", "paper_id", "qc", "normalization",
                   "batch_correction", "dim_reduction", "clustering",
                   "annotation", "diff_expr", "trajectory", "cell_comm",
                   "enrichment", "software", "provenance"],
}

CSV_NAMES: dict[str, str] = {k: f"{k}.csv" for k in HEADERS}

# SQLite 建表 DDL（与 schema §SQLite CREATE TABLE DDL 完全一致）
DDL: str = """
PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS processing;
DROP TABLE IF EXISTS cell_subtypes;
DROP TABLE IF EXISTS cell_types;
DROP TABLE IF EXISTS datasets;
DROP TABLE IF EXISTS papers;

CREATE TABLE papers (
    paper_id      TEXT PRIMARY KEY,
    title         TEXT NOT NULL,
    first_author  TEXT NOT NULL,
    corresponding TEXT,
    year          TEXT,
    journal       TEXT NOT NULL,
    doi           TEXT,
    pmid          TEXT,
    url           TEXT,
    species       TEXT NOT NULL,
    has_scrna     TEXT NOT NULL CHECK (has_scrna IN ('true','false','NA')),
    dataset_ids   TEXT,
    status        TEXT NOT NULL CHECK (status IN ('pending','qualified','rejected','extracted')),
    source        TEXT NOT NULL CHECK (source IN ('PubMed','GEO','OpenAlex','SemanticScholar','EuropePMC','bioRxiv','other')),
    suppl_path    TEXT,
    notes         TEXT
);

CREATE TABLE datasets (
    dataset_id        TEXT PRIMARY KEY,
    repository        TEXT NOT NULL CHECK (repository IN ('GEO','SRA','ArrayExpress','Zenodo','EGA','other')),
    accession_url     TEXT,
    platform          TEXT NOT NULL,
    vendor            TEXT,
    species           TEXT NOT NULL,
    tissue            TEXT NOT NULL,
    condition         TEXT,
    n_cells           TEXT,
    n_samples         TEXT,
    data_availability TEXT NOT NULL CHECK (data_availability IN ('raw','processed','both','restricted')),
    paper_ids         TEXT NOT NULL
);

CREATE TABLE cell_types (
    ct_id             TEXT PRIMARY KEY,
    dataset_id        TEXT NOT NULL,
    paper_id          TEXT NOT NULL,
    cell_type         TEXT NOT NULL,
    is_pns_cell       TEXT NOT NULL CHECK (is_pns_cell IN ('true','false','NA')),
    subtype           TEXT,
    markers           TEXT,
    species           TEXT NOT NULL CHECK (species IN ('human','mouse','rat')),
    n_cells_or_pct    TEXT,
    annotation_method TEXT,
    provenance        TEXT NOT NULL,
    FOREIGN KEY (dataset_id) REFERENCES datasets(dataset_id),
    FOREIGN KEY (paper_id)   REFERENCES papers(paper_id)
);

CREATE TABLE cell_subtypes (
    subtype_id            TEXT PRIMARY KEY,
    dataset_id            TEXT NOT NULL,
    paper_id              TEXT NOT NULL,
    parent_cell_type      TEXT NOT NULL,
    subtype               TEXT NOT NULL,
    is_pns_cell           TEXT NOT NULL CHECK (is_pns_cell IN ('true','false','NA')),
    species               TEXT NOT NULL CHECK (species IN ('human','mouse','rat')),
    condition_specificity TEXT,
    markers               TEXT,
    functional_signature  TEXT,
    n_cells_or_pct        TEXT,
    lineage               TEXT,
    provenance            TEXT NOT NULL,
    FOREIGN KEY (dataset_id) REFERENCES datasets(dataset_id),
    FOREIGN KEY (paper_id)   REFERENCES papers(paper_id)
);

CREATE TABLE processing (
    proc_id          TEXT PRIMARY KEY,
    dataset_id       TEXT NOT NULL,
    paper_id         TEXT NOT NULL,
    qc               TEXT,
    normalization    TEXT,
    batch_correction TEXT,
    dim_reduction    TEXT,
    clustering       TEXT,
    annotation       TEXT,
    diff_expr        TEXT,
    trajectory       TEXT,
    cell_comm        TEXT,
    enrichment       TEXT,
    software         TEXT,
    provenance       TEXT NOT NULL,
    FOREIGN KEY (dataset_id) REFERENCES datasets(dataset_id),
    FOREIGN KEY (paper_id)   REFERENCES papers(paper_id)
);

CREATE INDEX IF NOT EXISTS idx_ct_dataset   ON cell_types(dataset_id);
CREATE INDEX IF NOT EXISTS idx_cst_dataset  ON cell_subtypes(dataset_id);
CREATE INDEX IF NOT EXISTS idx_proc_dataset ON processing(dataset_id);
CREATE INDEX IF NOT EXISTS idx_proc_paper   ON processing(paper_id);
CREATE INDEX IF NOT EXISTS idx_ct_is_pns    ON cell_types(is_pns_cell);
"""


# ----------------------------------------------------------------------------
# CSV 读写
# ----------------------------------------------------------------------------
def read_csv(path: Path) -> list[dict[str, str]]:
    """读取 CSV → list[dict]，不存在返回空列表。"""
    p = Path(path)
    if not p.exists():
        return []
    with p.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, header: list[str], rows: list[dict[str, Any]]) -> None:
    r"""写回 CSV（UTF-8 无 BOM、\n、RFC4180）。缺列补 NA。"""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header,
                                lineterminator="\n",
                                quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: _cell(row.get(k)) for k in header})


def _cell(v: Any) -> str:
    """单元格归一：None/空 → NA；其余转字符串。"""
    if v is None:
        return NA
    s = str(v)
    return s if s != "" else NA


# ----------------------------------------------------------------------------
# 多值字段工具
# ----------------------------------------------------------------------------
def parse_multi(value: Any) -> list[str]:
    if value is None or value == "" or value == NA:
        return []
    return [t for t in str(value).split(";") if t != ""]


def join_multi(tokens: list[str]) -> str:
    seen: set[str] = set()
    ordered: list[str] = []
    for t in tokens:
        if t not in seen:
            seen.add(t)
            ordered.append(t)
    return ";".join(ordered) if ordered else NA


def union_multi(*values: Any) -> str:
    tokens: list[str] = []
    for v in values:
        tokens.extend(parse_multi(v))
    return join_multi(tokens)


# ----------------------------------------------------------------------------
# 内部 ID 赋号
# ----------------------------------------------------------------------------
def next_serial(existing_ids: set[str | None], prefix: str, width: int) -> str:
    """给定现有内部 ID 集合，返回下一个序号字符串（如 C00001）。"""
    max_n = 0
    for x in existing_ids:
        if isinstance(x, str) and x.startswith(prefix):
            num = x[len(prefix):]
            if num.isdigit():
                max_n = max(max_n, int(num))
    return f"{prefix}{max_n + 1:0{width}d}"


class IdAllocator:
    """统一管理内部 ID 的递增赋号，保证一次入库内不冲突。"""

    def __init__(self, papers: list[dict[str, Any]], cell_types: list[dict[str, Any]],
                 cell_subtypes: list[dict[str, Any]],
                 processing: list[dict[str, Any]]) -> None:
        self._paper_ids: set[str | None] = {r.get("paper_id") for r in papers}
        self._ct_ids: set[str | None] = {r.get("ct_id") for r in cell_types}
        self._subtype_ids: set[str | None] = {r.get("subtype_id") for r in cell_subtypes}
        self._proc_ids: set[str | None] = {r.get("proc_id") for r in processing}

    def new_paper(self) -> str:
        nid = next_serial(self._paper_ids, "P", 4)
        self._paper_ids.add(nid)
        return nid

    def new_ct(self) -> str:
        nid = next_serial(self._ct_ids, "C", 5)
        self._ct_ids.add(nid)
        return nid

    def new_subtype(self) -> str:
        nid = next_serial(self._subtype_ids, "S", 5)
        self._subtype_ids.add(nid)
        return nid

    def new_proc(self) -> str:
        nid = next_serial(self._proc_ids, "X", 5)
        self._proc_ids.add(nid)
        return nid


# ----------------------------------------------------------------------------
# 幂等去重指纹
# ----------------------------------------------------------------------------
def ct_fingerprint(row: dict[str, Any]) -> tuple:
    """cell_types 内容指纹（不含 ct_id）。"""
    return (row.get("dataset_id"), row.get("cell_type"), row.get("subtype"),
            row.get("species"), row.get("markers"))


def cst_fingerprint(row: dict[str, Any]) -> tuple:
    """cell_subtypes 内容指纹（不含 subtype_id）。"""
    return (row.get("dataset_id"), row.get("parent_cell_type"), row.get("subtype"),
            row.get("species"), row.get("markers"))


def proc_fingerprint(row: dict[str, Any]) -> tuple:
    """processing 内容指纹（不含 proc_id）：dataset+paper+核心方法。"""
    return (row.get("dataset_id"), row.get("paper_id"), row.get("qc"),
            row.get("normalization"), row.get("clustering"), row.get("software"))


def find_paper_by_id(papers: list[dict[str, Any]], paper_id: str) -> dict[str, Any] | None:
    """按 paper_id 在 papers 列表中定位行。"""
    for r in papers:
        if (r.get("paper_id") or "").strip() == paper_id:
            return r
    return None


# ----------------------------------------------------------------------------
# 主入库流程（per-dataset）
# ----------------------------------------------------------------------------
def ingest_perdataset(db: Path, payload: dict[str, Any], paper_id: str,
                      paper_meta: dict[str, Any] | None,
                      conflicts: list[str], *, force: bool = False
                      ) -> tuple[list, list, list, list, list] | None:
    """
    把一份 per-dataset 提取 JSON 合并进 4 张 CSV（幂等）。
    返回更新后的四表行列表；若致命中断返回 None。
    """
    papers = read_csv(db / CSV_NAMES["papers"])
    datasets = read_csv(db / CSV_NAMES["datasets"])
    cell_types = read_csv(db / CSV_NAMES["cell_types"])
    cell_subtypes = read_csv(db / CSV_NAMES["cell_subtypes"])
    processing = read_csv(db / CSV_NAMES["processing"])

    alloc = IdAllocator(papers, cell_types, cell_subtypes, processing)

    # --- 0) _self_check 门控 ---
    self_check = payload.get("_self_check") or {}
    if str(self_check.get("qualified")) == "false" and not force:
        conflicts.append(
            f"_self_check.qualified=false（{self_check.get('notes', '')}）。"
            f"已拒绝入库，请人工复核；确需入库加 --force。")
        return None

    # --- 1) 定位/创建 paper 行（提取阶段 JSON 不含 paper，用 --paper-id 关联）---
    paper_row = find_paper_by_id(papers, paper_id)
    if paper_row is None:
        if paper_meta is None:
            conflicts.append(
                f"paper_id {paper_id!r} 不在 papers.csv（提取前应已预筛登记）。"
                f"请先预筛登记，或用 --paper-meta 提供题录字段新建。")
            return None
        # 用 meta 新建最小 paper 行
        paper_row = {k: _cell(paper_meta.get(k)) for k in HEADERS["papers"]}
        paper_row["paper_id"] = paper_id
        if paper_row.get("status") in (NA, "", "pending"):
            paper_row["status"] = "qualified"  # 既然在提取，至少 qualified
        papers.append(paper_row)

    # 状态推进：qualified → extracted
    cur_status = (paper_row.get("status") or "").strip()
    if cur_status not in ("qualified", "extracted"):
        conflicts.append(
            f"paper {paper_id} 当前 status={cur_status!r}，正常应为 qualified 才进入提取"
            f"（继续入库，但请核对裁决流程）。")
    paper_row["status"] = "extracted"

    # --- 2) dataset 块：去重 + 镜像 ---
    did = (payload.get("dataset_id") or
           (payload.get("dataset") or {}).get("dataset_id") or "").strip()
    if did in ("", NA):
        conflicts.append("提取 JSON 缺少 dataset_id，无法入库")
        return None

    ds_index = {r.get("dataset_id"): r for r in datasets}
    ds_block = dict(payload.get("dataset") or {})
    is_new_dataset = did not in ds_index

    if is_new_dataset:
        row = {k: _cell(ds_block.get(k)) for k in HEADERS["datasets"]}
        row["dataset_id"] = did
        row["paper_ids"] = union_multi(paper_id)        # 提取阶段由 --paper-id 回填
        datasets.append(row)
        ds_index[did] = row
    else:
        row = ds_index[did]
        row["paper_ids"] = union_multi(row.get("paper_ids"), paper_id)

    # 镜像：paper.dataset_ids 追加 did
    paper_row["dataset_ids"] = union_multi(paper_row.get("dataset_ids"), did)

    # --- 3) cell_types：仅「数据集首次入库」时写入（schema §8 去重规则）---
    if is_new_dataset:
        existing_ct_fps = {ct_fingerprint(r) for r in cell_types}
        for ct in payload.get("cell_types") or []:
            row_ct = {k: _cell(ct.get(k)) for k in HEADERS["cell_types"]}
            row_ct["dataset_id"] = did
            row_ct["paper_id"] = paper_id
            fp = ct_fingerprint(row_ct)
            if fp in existing_ct_fps:
                continue  # 幂等：相同内容不重复
            row_ct["ct_id"] = alloc.new_ct()
            cell_types.append(row_ct)
            existing_ct_fps.add(fp)
    else:
        n_skip = len(payload.get("cell_types") or [])
        if n_skip:
            print(f"[去重] 数据集 {did} 已存在，按 schema §8 跳过本次 {n_skip} "
                  f"条 cell_types（仅追加 paper_ids）。")

    # --- 3b) cell_subtypes：仅「数据集首次入库」时写入（同 cell_types 去重规则）---
    if is_new_dataset:
        existing_cst_fps = {cst_fingerprint(r) for r in cell_subtypes}
        for cst in payload.get("cell_subtypes") or []:
            row_cst = {k: _cell(cst.get(k)) for k in HEADERS["cell_subtypes"]}
            row_cst["dataset_id"] = did
            row_cst["paper_id"] = paper_id
            fp = cst_fingerprint(row_cst)
            if fp in existing_cst_fps:
                continue
            row_cst["subtype_id"] = alloc.new_subtype()
            cell_subtypes.append(row_cst)
            existing_cst_fps.add(fp)

    # --- 4) processing：总是尝试（不同文章可对同数据集再分析）---
    valid_papers = {r.get("paper_id") for r in papers}
    existing_proc_fps = {proc_fingerprint(r) for r in processing}
    proc_block = payload.get("processing")
    if isinstance(proc_block, dict) and proc_block:
        row_pr = {k: _cell(proc_block.get(k)) for k in HEADERS["processing"]}
        row_pr["dataset_id"] = did
        row_pr["paper_id"] = paper_id
        if paper_id not in valid_papers:
            conflicts.append(f"processing 引用的 paper_id {paper_id!r} 不存在，已跳过 processing")
        else:
            fp = proc_fingerprint(row_pr)
            if fp not in existing_proc_fps:
                row_pr["proc_id"] = alloc.new_proc()
                processing.append(row_pr)
                existing_proc_fps.add(fp)

    return papers, datasets, cell_types, cell_subtypes, processing


# ----------------------------------------------------------------------------
# 镜像最终校验（双向一致）
# ----------------------------------------------------------------------------
def verify_mirror(papers: list[dict[str, Any]], datasets: list[dict[str, Any]],
                  conflicts: list[str]) -> None:
    """校验 papers.dataset_ids 与 datasets.paper_ids 双向一致。"""
    ds_to_papers = {d.get("dataset_id"): set(parse_multi(d.get("paper_ids")))
                    for d in datasets}
    pp_to_datasets = {p.get("paper_id"): set(parse_multi(p.get("dataset_ids")))
                      for p in papers}

    for did, pids in ds_to_papers.items():
        for pid in pids:
            if did not in pp_to_datasets.get(pid, set()):
                conflicts.append(
                    f"镜像不一致：datasets[{did}].paper_ids 含 {pid}，"
                    f"但 papers[{pid}].dataset_ids 缺 {did}")
    for pid, dids in pp_to_datasets.items():
        for did in dids:
            if pid not in ds_to_papers.get(did, set()):
                conflicts.append(
                    f"镜像不一致：papers[{pid}].dataset_ids 含 {did}，"
                    f"但 datasets[{did}].paper_ids 缺 {pid}")


# ----------------------------------------------------------------------------
# 从 CSV 重建 SQLite
# ----------------------------------------------------------------------------
def rebuild_sqlite(db: Path, conflicts: list[str]) -> Path:
    """读取 4 张 CSV，DROP→CREATE→INSERT 重建 database.sqlite。"""
    sqlite_path = db / "database.sqlite"
    tables = {name: read_csv(db / CSV_NAMES[name]) for name in HEADERS}

    conn = sqlite3.connect(str(sqlite_path))
    try:
        conn.executescript(DDL)
        # 按外键依赖顺序插入
        for name in ("papers", "datasets", "cell_types", "cell_subtypes", "processing"):
            _insert(conn, name, HEADERS[name], tables[name])
        conn.commit()
        bad = conn.execute("PRAGMA foreign_key_check;").fetchall()
        for b in bad:
            conflicts.append(f"SQLite 外键违例：{b}")
    except sqlite3.Error as e:
        conn.rollback()
        conflicts.append(f"SQLite 重建失败：{e}")
        raise
    finally:
        conn.close()
    return sqlite_path


def _insert(conn: sqlite3.Connection, table: str, header: list[str],
            rows: list[dict[str, Any]]) -> None:
    """批量插入一张表。缺列补 NA。"""
    placeholders = ",".join("?" for _ in header)
    cols = ",".join(header)
    sql = f"INSERT INTO {table} ({cols}) VALUES ({placeholders})"
    data = [tuple(_cell(r.get(c)) for c in header) for r in rows]
    conn.executemany(sql, data)


# ----------------------------------------------------------------------------
# 初始化空 CSV
# ----------------------------------------------------------------------------
def ensure_empty_csvs(db: Path) -> None:
    """若某张 CSV 不存在，则创建只含表头的空文件。"""
    for name, header in HEADERS.items():
        path = db / CSV_NAMES[name]
        if not path.exists():
            write_csv(path, header, [])


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------
def main() -> int:
    parser = argparse.ArgumentParser(
        description="把校验通过的 per-dataset 提取 JSON 入库（4 CSV + 重建 SQLite），幂等。")
    parser.add_argument("--db", required=True,
                        help="数据库 CSV 目录，如 D:/database/db")
    parser.add_argument("--json", metavar="FILE",
                        help="待入库的 per-dataset 提取 JSON 文件")
    parser.add_argument("--paper-id", metavar="P0001",
                        help="该提取所属文章的 paper_id（提取 JSON 不含 paper，靠此关联）")
    parser.add_argument("--paper-meta", metavar="FILE",
                        help="可选：paper 尚未登记时，提供其题录字段(同 papers 表)以新建")
    parser.add_argument("--force", action="store_true",
                        help="忽略 _self_check.qualified=false，强制入库")
    parser.add_argument("--rebuild-only", action="store_true",
                        help="仅由现有 CSV 重建 SQLite，不并入新 JSON")
    parser.add_argument("--no-sqlite", action="store_true",
                        help="只写 CSV，不重建 SQLite")
    args = parser.parse_args()

    db = Path(args.db)
    db.mkdir(parents=True, exist_ok=True)
    ensure_empty_csvs(db)
    conflicts: list[str] = []

    # --- 仅重建 ---
    if args.rebuild_only:
        try:
            path = rebuild_sqlite(db, conflicts)
        except sqlite3.Error:
            for c in conflicts:
                print(f"  [冲突] {c}")
            return 2
        if conflicts:
            print(f"[重建] 完成但有 {len(conflicts)} 处外键违例：")
            for c in conflicts:
                print(f"  - {c}")
            return 1
        print(f"[重建] SQLite 已从 CSV 重建：{path}")
        return 0

    if not args.json:
        parser.error("需提供 --json 或 --rebuild-only")
        return 2
    if not args.paper_id:
        parser.error("入库 per-dataset JSON 必须提供 --paper-id（关联已登记文章）")
        return 2

    # --- 读取 JSON / meta ---
    try:
        payload = json.loads(Path(args.json).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"[ERROR] 读取/解析 JSON 失败：{e}", file=sys.stderr)
        return 2

    paper_meta: dict[str, Any] | None = None
    if args.paper_meta:
        try:
            paper_meta = json.loads(Path(args.paper_meta).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            print(f"[ERROR] 读取/解析 paper-meta 失败：{e}", file=sys.stderr)
            return 2

    result = ingest_perdataset(db, payload, args.paper_id.strip(), paper_meta,
                               conflicts, force=args.force)
    if result is None:
        print(f"[中断] 未入库，共 {len(conflicts)} 处问题：")
        for c in conflicts:
            print(f"  - {c}")
        return 1

    papers, datasets, cell_types, cell_subtypes, processing = result
    verify_mirror(papers, datasets, conflicts)

    # 写回 5 张 CSV
    write_csv(db / CSV_NAMES["papers"], HEADERS["papers"], papers)
    write_csv(db / CSV_NAMES["datasets"], HEADERS["datasets"], datasets)
    write_csv(db / CSV_NAMES["cell_types"], HEADERS["cell_types"], cell_types)
    write_csv(db / CSV_NAMES["cell_subtypes"], HEADERS["cell_subtypes"], cell_subtypes)
    write_csv(db / CSV_NAMES["processing"], HEADERS["processing"], processing)
    print(f"[入库] papers={len(papers)} datasets={len(datasets)} "
          f"cell_types={len(cell_types)} cell_subtypes={len(cell_subtypes)} "
          f"processing={len(processing)} → CSV 已写回。")

    if not args.no_sqlite:
        try:
            path = rebuild_sqlite(db, conflicts)
            print(f"[重建] SQLite 已重建：{path}")
        except sqlite3.Error:
            print("[ERROR] SQLite 重建失败，CSV 已写回，请人工排查。", file=sys.stderr)

    if conflicts:
        print(f"[冲突] 共 {len(conflicts)} 处需人工介入：")
        for c in conflicts:
            print(f"  - {c}")
        return 1

    print("[完成] 入库成功，无冲突。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
