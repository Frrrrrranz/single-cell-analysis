#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
stats.py · 总览统计 / index.md 生成器（确定性任务，不调用 LLM）

用途
----
扫描 D:/database/db/ 下的 4 张 CSV，生成数据库总览 D:/database/index.md：
  - 规模：文章 / 数据集 / 细胞类型 / 处理流程 计数（按 status 分层）
  - 物种 / 组织 / 平台 / 数据可得性 / 实验条件 分布
  - 外周神经细胞类型（is_pns_cell=true）频次 + 亚群 subtype 频次
  - marker 出现频次 Top（跨物种按大写归一合并，如 SOX10/Sox10 合并）
    【已知限制】归一仅按大小写合并，不处理人鼠「拼写差异」同源基因
    （如人 TP53 与鼠 Trp53，大写后 TP53≠TRP53，仍计为两个）。如需严格跨物种
    同源合并，应接入 ortholog 映射表（当前 YAGNI，未实现）。
  - 合格数据集数（含 ≥1 条 is_pns_cell=true）
  - 「怎么查」示例 SQL（呼应数据库的检索价值）

仅用标准库。幂等：重复运行覆盖生成同一份 index.md。

用法示例
--------
  python stats.py --db D:/database/db --out D:/database/index.md
  python stats.py --db D:/database/db                # 默认输出 <db>/../index.md

退出码：0 = 成功；2 = IO 错误。
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

NA: str = "NA"
TRUE: str = "true"
TOP_MARKERS: int = 30  # marker 频次榜展示条数


# ----------------------------------------------------------------------------
# CSV 读取
# ----------------------------------------------------------------------------
def read_csv(path: Path) -> list[dict[str, str]]:
    """读取 CSV → list[dict]。不存在返回空列表。"""
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def parse_multi(value: Any) -> list[str]:
    """分号多值 → token 列表（去 NA/空）。"""
    if value is None or value == "" or value == NA:
        return []
    return [t.strip() for t in str(value).split(";") if t.strip() not in ("", NA)]


def count_multi(rows: list[dict[str, Any]], field: str) -> Counter:
    """统计某多值列各取值出现次数（按行内去重后计数，即「多少行命中该值」）。"""
    counter: Counter = Counter()
    for r in rows:
        for tok in set(parse_multi(r.get(field))):
            counter[tok] += 1
    return counter


def count_single(rows: list[dict[str, Any]], field: str) -> Counter:
    """统计某单值列分布（NA 计入 'NA'）。"""
    counter: Counter = Counter()
    for r in rows:
        v = (r.get(field) or NA).strip() or NA
        counter[v] += 1
    return counter


# ----------------------------------------------------------------------------
# Markdown 渲染
# ----------------------------------------------------------------------------
def md_table(headers: list[str], rows: list[list[Any]]) -> str:
    """渲染 Markdown 表格。"""
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


def counter_table(counter: Counter, col_name: str, value_name: str = "数据集数",
                  top: int | None = None) -> str:
    """把 Counter 渲染成两列频次表（降序）。"""
    items = counter.most_common(top)
    if not items:
        return "_（暂无数据）_"
    return md_table([col_name, value_name], [[k, v] for k, v in items])


# ----------------------------------------------------------------------------
# 统计主流程
# ----------------------------------------------------------------------------
def build_index(db: Path) -> str:
    """读取 4 张 CSV，生成 index.md 文本。"""
    papers = read_csv(db / "papers.csv")
    datasets = read_csv(db / "datasets.csv")
    cell_types = read_csv(db / "cell_types.csv")
    processing = read_csv(db / "processing.csv")

    # --- 规模 ---
    status_dist = count_single(papers, "status")
    pns_cts = [c for c in cell_types if (c.get("is_pns_cell") or "").strip() == TRUE]

    # 合格数据集 = 至少 1 条 is_pns_cell=true 的数据集
    ds_with_pns = {(c.get("dataset_id") or "").strip() for c in pns_cts}
    n_qualified_ds = len([d for d in datasets
                          if (d.get("dataset_id") or "").strip() in ds_with_pns])

    # --- 分布 ---
    species_dist = count_multi(datasets, "species")
    tissue_dist = count_multi(datasets, "tissue")
    platform_dist = count_multi(datasets, "platform")
    avail_dist = count_single(datasets, "data_availability")
    condition_dist = count_multi(datasets, "condition")

    # --- 外周神经细胞类型频次（按命中数据集数计）---
    pns_celltype_counter: Counter = Counter()
    for c in pns_cts:
        ct = (c.get("cell_type") or NA).strip() or NA
        pns_celltype_counter[ct] += 1
    pns_subtype_counter: Counter = Counter()
    for c in pns_cts:
        st = (c.get("subtype") or NA).strip()
        if st and st != NA:
            pns_subtype_counter[st] += 1

    # --- marker 频次（跨物种按大写归一合并）---
    marker_counter: Counter = Counter()
    for c in cell_types:
        for m in parse_multi(c.get("markers")):
            marker_counter[m.upper()] += 1

    # --- 组装 Markdown ---
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    parts: list[str] = []
    parts.append("# 外周神经 scRNA 数据库 · 总览（index）\n")
    parts.append(f"> 自动生成于 {ts} · 由 `stats.py` 扫描 `db/*.csv` 产出，请勿手改。\n")

    # 规模
    parts.append("## 一、规模总览\n")
    parts.append(md_table(
        ["指标", "数量"],
        [
            ["文章 papers（总）", len(papers)],
            ["　├ 已提取 extracted", status_dist.get("extracted", 0)],
            ["　├ 合格待提取 qualified", status_dist.get("qualified", 0)],
            ["　├ 待裁决 pending", status_dist.get("pending", 0)],
            ["　└ 已淘汰 rejected", status_dist.get("rejected", 0)],
            ["数据集 datasets（去重后）", len(datasets)],
            ["　└ 合格（含≥1 外周神经细胞）", n_qualified_ds],
            ["细胞类型记录 cell_types", len(cell_types)],
            ["　└ 外周神经细胞 is_pns_cell=true", len(pns_cts)],
            ["处理流程记录 processing", len(processing)],
        ]))
    parts.append("")

    # 分布
    parts.append("## 二、物种分布（datasets）\n")
    parts.append(counter_table(species_dist, "物种"))
    parts.append("\n## 三、组织分布（datasets）\n")
    parts.append(counter_table(tissue_dist, "组织"))
    parts.append("\n## 四、测序平台分布（datasets）\n")
    parts.append(counter_table(platform_dist, "平台"))
    parts.append("\n## 五、数据可得性分布（datasets）\n")
    parts.append(counter_table(avail_dist, "data_availability"))
    parts.append("\n## 六、实验条件分布（datasets · Top20）\n")
    parts.append(counter_table(condition_dist, "condition", top=20))

    # 细胞类型
    parts.append("\n## 七、外周神经细胞类型频次（is_pns_cell=true）\n")
    parts.append(counter_table(pns_celltype_counter, "cell_type", "记录数"))
    parts.append("\n## 八、外周神经亚群 subtype 频次\n")
    parts.append(counter_table(pns_subtype_counter, "subtype", "记录数"))

    # marker
    parts.append(f"\n## 九、marker 出现频次 Top{TOP_MARKERS}（跨物种按大写归一合并）\n")
    parts.append(counter_table(marker_counter, "marker(大写归一)", "出现次数",
                               top=TOP_MARKERS))

    # 怎么查
    parts.append("\n## 十、怎么查（database.sqlite 示例）\n")
    parts.append(
        "```sql\n"
        "-- 1) 所有测了小鼠 DRG 的数据集及平台\n"
        "SELECT dataset_id, platform, n_cells FROM datasets\n"
        "WHERE species LIKE '%mouse%' AND tissue LIKE '%DRG%';\n\n"
        "-- 2) Schwann cell 在各数据集用过哪些 marker\n"
        "SELECT dataset_id, subtype, markers FROM cell_types\n"
        "WHERE cell_type='Schwann cell' AND is_pns_cell='true';\n\n"
        "-- 3) 某 marker（如 SOX10）出现在哪些外周神经细胞记录\n"
        "SELECT dataset_id, cell_type, species, markers FROM cell_types\n"
        "WHERE is_pns_cell='true' AND UPPER(markers) LIKE '%SOX10%';\n\n"
        "-- 4) 人类坐骨神经损伤的现成数据集\n"
        "SELECT dataset_id, accession_url, condition FROM datasets\n"
        "WHERE species LIKE '%human%' AND tissue LIKE '%sciatic%'\n"
        "  AND condition LIKE '%injury%';\n"
        "```\n")

    return "\n".join(parts) + "\n"


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------
def main() -> int:
    parser = argparse.ArgumentParser(
        description="扫描 4 张 CSV 生成数据库总览 index.md（不用 LLM）。")
    parser.add_argument("--db", required=True, help="数据库 CSV 目录，如 D:/database/db")
    parser.add_argument("--out", help="index.md 输出路径（默认 <db>/../index.md）")
    args = parser.parse_args()

    db = Path(args.db)
    if not db.exists():
        print(f"[ERROR] 数据库目录不存在：{db}", file=sys.stderr)
        return 2

    out = Path(args.out) if args.out else db.parent / "index.md"

    try:
        text = build_index(db)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
    except OSError as e:
        print(f"[ERROR] 生成失败：{e}", file=sys.stderr)
        return 2

    print(f"[stats] 总览已生成：{out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
