#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate.py · 提取 JSON 校验器（确定性任务，不调用 LLM）

用途
----
校验 DeepSeek 按 05_extraction.md 提取出的一份「单数据集(per-dataset)」JSON
是否符合 01_schema.md 定义的 schema。

输入 JSON 结构（与 05_extraction.md §2 骨架严格一致）
----------------------------------------------------
{
  "dataset_id": "GSE190000",                 # 顶层回显，必须 == dataset.dataset_id
  "dataset":    { ...datasets 表中由 LLM 填的字段(不含 paper_ids)... },
  "cell_types": [ { ...cell_types 行(不含 ct_id/dataset_id)... }, ... ],
  "processing": { ...processing 方法列(不含 proc_id/dataset_id/paper_id)... },
  "_self_check":{ "qualified", "n_pns_cell_types", "uncontrolled_terms", "notes" }
}

说明：
  - 提取阶段 **不含 paper 对象**（文章在预筛阶段已写入 papers.csv）。
  - cell_types 元素不含 ct_id / dataset_id；processing 不含 proc_id / dataset_id /
    paper_id —— 这些都由 ingest.py 在入库时回填/赋号，故本校验器**不**要求它们。
  - paper_id 由 ingest.py 的 --paper-id 命令行参数提供，不在 JSON 内，也不在此校验。

校验项
------
  - 顶层结构完整（dataset_id / dataset / cell_types / processing），dataset_id 一致
  - 物种白名单 {human, mouse, rat}（datasets 多值；cell_types 单值）
  - 必填字段非空、非 NA（按「提取阶段」口径，见 *_REQUIRED）
  - 布尔字段取值 {true, false, NA}（仅 is_pns_cell 允许 NA）
  - 枚举字段合法性（repository/data_availability/normalization/...）
  - marker 命名规范（人类全大写；鼠/大鼠首字母大写其余小写）
  - dataset_id 格式（GSE/SRP/PRJNA/E-XXXX/zenodo/EGA）与 repository 前缀匹配
  - provenance 非空且不是无法定位的占位词
  - 多值字段分隔规范（分号两侧不留空格、无尾随分号）
  - 整数字段不带千分位逗号

用法示例
--------
  python validate.py extracted/GSE190000.json
  python validate.py extracted/GSE190000.json --json      # 机器可读结果
  python validate.py --stdin < extracted/GSE190000.json

退出码：0 = 全部通过；1 = 存在错误；2 = 无法读取/解析输入。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable

# ----------------------------------------------------------------------------
# 常量：白名单与枚举（与 01_schema.md 严格一致）
# ----------------------------------------------------------------------------
SPECIES_WHITELIST: set[str] = {"human", "mouse", "rat"}
BOOL_VALUES: set[str] = {"true", "false"}
BOOL_VALUES_WITH_NA: set[str] = {"true", "false", "NA"}
NA: str = "NA"
AUTO: str = "__AUTO__"

# datasets 枚举
DS_REPOSITORY: set[str] = {"GEO", "SRA", "ArrayExpress", "Zenodo", "EGA", "other"}
DS_VENDOR: set[str] = {"10x Genomics", "BD", "Parse Biosciences", "Illumina",
                       "BGI-MGI", "Fluidigm", "other"}
DS_DATA_AVAIL: set[str] = {"raw", "processed", "both", "restricted"}

# cell_types 枚举
CT_ANNOT_METHOD: set[str] = {"manual-marker", "SingleR", "CellTypist", "Azimuth",
                             "scANVI", "reference-mapping", "other"}

# 各块「契约允许字段」全集（含由 ingest 回填的内部列，避免与 forbidden 检测重复报）。
# 用于「未知字段检测」：出现集合外的键说明字段名笔误，入库时会被静默丢弃。
DS_KNOWN_FIELDS: set[str] = {
    "dataset_id", "repository", "accession_url", "platform", "vendor", "species",
    "tissue", "condition", "n_cells", "n_samples", "data_availability",
    "paper_ids", "provenance",
}
CT_KNOWN_FIELDS: set[str] = {
    "cell_type", "is_pns_cell", "subtype", "markers", "species", "n_cells_or_pct",
    "annotation_method", "provenance", "ct_id", "dataset_id", "paper_id",
}
PROC_KNOWN_FIELDS: set[str] = {
    "qc", "normalization", "batch_correction", "dim_reduction", "clustering",
    "annotation", "diff_expr", "trajectory", "cell_comm", "enrichment", "software",
    "provenance", "proc_id", "dataset_id", "paper_id",
}
CST_KNOWN_FIELDS: set[str] = {
    "parent_cell_type", "subtype", "is_pns_cell", "species",
    "condition_specificity", "markers", "functional_signature",
    "n_cells_or_pct", "lineage", "provenance", "subtype_id", "dataset_id", "paper_id",
}

# 常见「拼错/近义」别名 → 契约正名。命中即静默丢数据，必须明确拦截并指明正名。
CT_FIELD_ALIASES: dict[str, str] = {
    "marker": "markers", "cell_count": "n_cells_or_pct",
    "cell_counts": "n_cells_or_pct", "n_cells": "n_cells_or_pct",
    "celltype": "cell_type", "cell": "cell_type", "ispnscell": "is_pns_cell",
}
DS_FIELD_ALIASES: dict[str, str] = {"n_cell": "n_cells", "nsamples": "n_samples"}
PROC_FIELD_ALIASES: dict[str, str] = {}

# processing 枚举（部分列允许多值；多值时拆分后逐项校验）
PROC_NORMALIZATION: set[str] = {"LogNormalize", "SCTransform", "scran", "TPM", "other"}
PROC_BATCH: set[str] = {"Harmony", "scVI", "Seurat-CCA", "Seurat-RPCA", "fastMNN",
                        "BBKNN", "none"}
PROC_ANNOTATION: set[str] = {"marker-based", "reference-mapping", "mixed"}
PROC_DIFF_EXPR: set[str] = {"Wilcoxon", "MAST", "pseudobulk-DESeq2", "edgeR",
                            "t-test", "none", "other"}
PROC_TRAJECTORY: set[str] = {"Monocle2", "Monocle3", "Slingshot", "PAGA", "scVelo", "none"}
PROC_CELL_COMM: set[str] = {"CellChat", "CellPhoneDB", "NicheNet", "LIANA", "none"}

# 「提取阶段」各块必填字段（不含由脚本回填的 ct_id/dataset_id/proc_id/paper_id/paper_ids）
DS_REQUIRED: list[str] = ["dataset_id", "repository", "accession_url", "platform",
                          "species", "tissue", "data_availability"]
CT_REQUIRED: list[str] = ["cell_type", "is_pns_cell", "species", "provenance"]
CST_REQUIRED: list[str] = ["parent_cell_type", "subtype", "is_pns_cell", "species", "provenance"]
PROC_REQUIRED: list[str] = ["provenance"]

# provenance 禁用的无法定位占位词（小写比对）
PROVENANCE_BANNED: set[str] = {"paper", "原文", "见上", "见前", "na", "n/a", "ref",
                               "reference", "见正文", "上文"}

# dataset_id 格式 → 对应 repository（前缀判定）
DATASET_ID_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"^GSE\d+$"), "GEO"),
    (re.compile(r"^GSM\d+$"), "GEO"),
    (re.compile(r"^SRP\d+$"), "SRA"),
    (re.compile(r"^PRJNA\d+$"), "SRA"),
    (re.compile(r"^SRR\d+$"), "SRA"),
    (re.compile(r"^E-[A-Z]{4}-\d+$"), "ArrayExpress"),
    (re.compile(r"^zenodo\.\d+$"), "Zenodo"),
    (re.compile(r"^EGA[DS]\d+$"), "EGA"),
]

INT_RE: re.Pattern[str] = re.compile(r"^\d+$")
PCT_RE: re.Pattern[str] = re.compile(r"^\d+(\.\d+)?%$")


# ----------------------------------------------------------------------------
# 错误收集器
# ----------------------------------------------------------------------------
class Issues:
    """收集校验错误。每条记录 (定位, 信息)。"""

    def __init__(self) -> None:
        self.errors: list[tuple[str, str]] = []

    def add(self, where: str, msg: str) -> None:
        self.errors.append((where, msg))

    def ok(self) -> bool:
        return len(self.errors) == 0


# ----------------------------------------------------------------------------
# 通用小工具
# ----------------------------------------------------------------------------
def is_missing(value: Any) -> bool:
    """判断字段是否「缺失」：None、空串、或字面 NA。"""
    if value is None:
        return True
    if isinstance(value, str) and (value.strip() == "" or value == NA):
        return True
    return False


def split_multi(value: Any) -> list[str]:
    """拆分分号多值字段，返回 token 列表（不含 NA / 空）。"""
    if is_missing(value):
        return []
    return [t for t in str(value).split(";") if t != ""]


def check_no_nested_delimiter(value: Any, where: str, field: str,
                              issues: Issues) -> None:
    """守卫：分号仅作字段级多值分隔符，不得嵌入括号内部。

    历史 bug：`time_series(0d;1d;3d;7d)`、`doublet_removal(a=1;b=2)` 这类值把 `;`
    塞进括号里，stats.py 按 `;` 拆分时会拆碎成 `time_series(0d` / `7d)` 等无效
    token，污染分面统计。判据：按 `;` 拆分后任一 token 括号不闭合，即说明分号落在
    括号内部。括号内多值请改用 `/` 分隔。
    """
    if is_missing(value):
        return
    for token in str(value).split(";"):
        if token.count("(") != token.count(")"):
            issues.add(where, f"{field} 的分号疑似嵌入括号内部（拆分后 token 括号"
                              f"不闭合）：{token!r}；括号内多值请改用 '/'，"
                              f"';' 仅用于字段级分隔")


def check_multi_format(value: Any, where: str, field: str, issues: Issues) -> None:
    """校验多值字段格式：分号两侧不留空格、无尾随/前置分号、无空 token、无嵌套分号。"""
    if is_missing(value):
        return
    s = str(value)
    if s != s.strip():
        issues.add(where, f"{field} 首尾含空白：{s!r}")
    if s.startswith(";") or s.endswith(";"):
        issues.add(where, f"{field} 含前置/尾随分号（违反多值规范）：{s!r}")
    if ";;" in s:
        issues.add(where, f"{field} 含空 token（连续分号）：{s!r}")
    if "; " in s or " ;" in s:
        issues.add(where, f"{field} 分号两侧不应留空格：{s!r}")
    check_no_nested_delimiter(value, where, field, issues)


def check_required(record: dict[str, Any], required_fields: Iterable[str],
                   where: str, issues: Issues) -> None:
    """校验必填字段存在且非缺失。"""
    for f in required_fields:
        if f not in record or is_missing(record.get(f)):
            issues.add(where, f"必填字段缺失或为 NA：{f}")


def check_species(value: Any, where: str, field: str, issues: Issues,
                  single: bool = False) -> None:
    """校验物种字段在白名单内（小写）。single=True 表示只允许单值。"""
    if is_missing(value):
        issues.add(where, f"{field} 必填，不能为 NA")
        return
    tokens = split_multi(value)
    if single and len(tokens) != 1:
        issues.add(where, f"{field} 必须为单值（cell_types 同物种多类应拆行）：{value!r}")
    for t in tokens:
        if t not in SPECIES_WHITELIST:
            issues.add(where, f"{field} 含非法物种 {t!r}（白名单：human/mouse/rat，须小写）")


def check_bool(value: Any, where: str, field: str, issues: Issues,
               allow_na: bool = False) -> None:
    """校验布尔字段取值。allow_na 仅对 is_pns_cell 为 True。"""
    if value is None:
        issues.add(where, f"{field} 缺失")
        return
    sval = str(value)
    allowed = BOOL_VALUES_WITH_NA if allow_na else BOOL_VALUES
    if sval not in allowed:
        issues.add(where, f"{field} 取值非法 {sval!r}（允许：{sorted(allowed)}）")


def check_enum(value: Any, allowed: set[str], where: str, field: str,
               issues: Issues, multi: bool = False, allow_na: bool = True) -> None:
    """校验枚举字段。multi=True 时按分号拆分逐项校验。"""
    if is_missing(value):
        if allow_na:
            return
        issues.add(where, f"{field} 必填，不能为 NA")
        return
    tokens = split_multi(value) if multi else [str(value)]
    for t in tokens:
        if t not in allowed:
            issues.add(where, f"{field} 取值非法 {t!r}（允许：{sorted(allowed)}）")


def check_provenance(value: Any, where: str, issues: Issues) -> None:
    """校验 provenance 非空且不是无法定位的占位。"""
    if is_missing(value):
        issues.add(where, "provenance 必填，不能为 NA/空")
        return
    for token in split_multi(value):
        if token.strip().lower() in PROVENANCE_BANNED:
            issues.add(where, f"provenance 含无法定位的占位 {token!r}"
                              f"（须写 Fig./Table/Methods/GEO: 等可定位来源）")


def check_marker_case(markers: Any, species: Any, where: str, issues: Issues) -> None:
    """
    校验 marker 命名大小写规范：
      - human：全大写（允许数字、连字符），如 SOX10、HLA-DRA
      - mouse/rat：首字母大写其余小写，如 Sox10、Calca
    species 取该 cell_types 行的单值物种。
    """
    if is_missing(markers) or is_missing(species):
        return
    sp = str(species)
    for gene in split_multi(markers):
        g = gene.strip()
        if g == "" or g == NA:
            continue
        letters = [c for c in g if c.isalpha()]
        if not letters:
            continue
        if sp == "human":
            if any(c.islower() for c in letters):
                issues.add(where, f"marker {g!r} 物种 human 应全大写（如 SOX10）")
        elif sp in ("mouse", "rat"):
            if not letters[0].isupper():
                issues.add(where, f"marker {g!r} 物种 {sp} 首字母应大写（如 Sox10）")
            if any(c.isupper() for c in letters[1:]):
                issues.add(where, f"marker {g!r} 物种 {sp} 仅首字母大写其余应小写（如 Sox10）")


def check_int_field(value: Any, where: str, field: str, issues: Issues,
                    min_value: int = 0) -> None:
    """校验整数字段（允许 NA）：非负整数、不带千分位逗号。"""
    if is_missing(value):
        return
    s = str(value)
    if "," in s:
        issues.add(where, f"{field} 不应含千分位逗号：{s!r}")
        return
    if not INT_RE.match(s):
        issues.add(where, f"{field} 应为非负整数或 NA：{s!r}")
        return
    if int(s) < min_value:
        issues.add(where, f"{field} 应 ≥ {min_value}：{s!r}")


def check_dataset_id(dataset_id: Any, repository: Any, where: str,
                     issues: Issues) -> None:
    """校验 dataset_id 格式合法，且与 repository 前缀一致。"""
    if is_missing(dataset_id):
        issues.add(where, "dataset_id 必填，不能为 NA")
        return
    did = str(dataset_id)
    matched_repo: str | None = None
    for pat, repo in DATASET_ID_PATTERNS:
        if pat.match(did):
            matched_repo = repo
            break
    if matched_repo is None:
        if repository == "other":
            return  # other 仓库放行自定义官方号，交人工
        issues.add(where, f"dataset_id 格式无法识别 {did!r}"
                          f"（期望 GSE/SRP/PRJNA/E-XXXX-/zenodo./EGA 等）")
        return
    if not is_missing(repository) and repository != matched_repo:
        issues.add(where, f"dataset_id {did!r} 前缀对应 {matched_repo}，"
                          f"但 repository 声明为 {repository!r}（不一致）")


def check_unknown_fields(record: dict[str, Any], known: set[str],
                         aliases: dict[str, str], where: str,
                         issues: Issues) -> None:
    """
    未知字段检测：拦截契约外字段，防止字段名笔误导致入库时数据被静默丢弃。
      - 命中已知别名（如 marker→markers、cell_count→n_cells_or_pct）：明确报错并指明正名；
      - 其他未知字段：提示该字段不在 schema 内、入库时会被忽略。
    入库脚本按契约字段名取值，字段名不符即取不到 → NA（历史数据丢失 bug 的根因）。
    """
    for key in record:
        if key in known:
            continue
        if key in aliases:
            issues.add(where, f"字段名 {key!r} 不符契约，应为 {aliases[key]!r}；"
                              f"否则入库时该字段数据会被静默丢弃")
        else:
            issues.add(where, f"未知字段 {key!r}（不在 schema 内，入库时将被忽略）")


# ----------------------------------------------------------------------------
# 各块校验（per-dataset 结构）
# ----------------------------------------------------------------------------
def validate_dataset_block(dataset: Any, top_dataset_id: Any,
                           issues: Issues) -> None:
    """校验 dataset 块（对应 datasets 表，提取阶段不含 paper_ids）。"""
    where = "dataset"
    if not isinstance(dataset, dict):
        issues.add(where, "dataset 必须是 JSON 对象")
        return
    did = dataset.get("dataset_id", "?")
    where = f"dataset[{did}]"

    check_required(dataset, DS_REQUIRED, where, issues)

    # 顶层 dataset_id 必须与块内一致
    if not is_missing(top_dataset_id) and not is_missing(dataset.get("dataset_id")):
        if str(top_dataset_id) != str(dataset.get("dataset_id")):
            issues.add(where, f"顶层 dataset_id {top_dataset_id!r} 与 "
                              f"dataset.dataset_id {dataset.get('dataset_id')!r} 不一致")

    repo = dataset.get("repository")
    check_enum(repo, DS_REPOSITORY, where, "repository", issues, allow_na=False)
    check_dataset_id(dataset.get("dataset_id"), repo, where, issues)

    check_species(dataset.get("species"), where, "species", issues)
    check_enum(dataset.get("data_availability"), DS_DATA_AVAIL, where,
               "data_availability", issues, allow_na=False)
    check_enum(dataset.get("vendor"), DS_VENDOR, where, "vendor", issues,
               multi=True, allow_na=True)

    check_int_field(dataset.get("n_cells"), where, "n_cells", issues)
    check_int_field(dataset.get("n_samples"), where, "n_samples", issues)

    for fld in ("platform", "tissue", "condition", "vendor", "species"):
        check_multi_format(dataset.get(fld), where, fld, issues)

    # 提取阶段不应出现 paper_ids（由 ingest 回填）；若出现给出提示但不算致命
    if "paper_ids" in dataset and not is_missing(dataset.get("paper_ids")):
        issues.add(where, "dataset 不应包含 paper_ids（提取阶段由 ingest.py 用 --paper-id 回填）")

    check_unknown_fields(dataset, DS_KNOWN_FIELDS, DS_FIELD_ALIASES, where, issues)


def validate_cell_type(ct: Any, idx: int, issues: Issues) -> None:
    """校验 cell_types 数组的一个元素（提取阶段不含 ct_id/dataset_id）。"""
    where = f"cell_types[{idx}]"
    if not isinstance(ct, dict):
        issues.add(where, "cell_type 记录必须是 JSON 对象")
        return

    check_required(ct, CT_REQUIRED, where, issues)
    check_bool(ct.get("is_pns_cell"), where, "is_pns_cell", issues, allow_na=True)
    check_species(ct.get("species"), where, "species", issues, single=True)
    check_enum(ct.get("annotation_method"), CT_ANNOT_METHOD, where,
               "annotation_method", issues, allow_na=True)
    check_provenance(ct.get("provenance"), where, issues)
    check_marker_case(ct.get("markers"), ct.get("species"), where, issues)
    check_multi_format(ct.get("markers"), where, "markers", issues)

    # n_cells_or_pct：整数或百分比或 NA
    npc = ct.get("n_cells_or_pct")
    if not is_missing(npc):
        s = str(npc)
        if not (INT_RE.match(s) or PCT_RE.match(s)):
            issues.add(where, f"n_cells_or_pct 应为整数 / 百分比(如 12.4%) / NA：{s!r}")

    # 提取阶段不应自带内部 ID 或 dataset_id（由脚本回填）
    for forbidden in ("ct_id", "dataset_id", "paper_id"):
        if forbidden in ct and not is_missing(ct.get(forbidden)) \
                and str(ct.get(forbidden)) != AUTO:
            issues.add(where, f"cell_types 不应自带 {forbidden}（由 ingest.py 回填/赋号）")

    check_unknown_fields(ct, CT_KNOWN_FIELDS, CT_FIELD_ALIASES, where, issues)


def validate_cell_subtype(cst: Any, idx: int, issues: Issues) -> None:
    """校验 cell_subtypes 数组的一个元素（提取阶段不含 subtype_id/dataset_id）。"""
    where = f"cell_subtypes[{idx}]"
    if not isinstance(cst, dict):
        issues.add(where, "cell_subtype 记录必须是 JSON 对象")
        return

    check_required(cst, CST_REQUIRED, where, issues)
    check_bool(cst.get("is_pns_cell"), where, "is_pns_cell", issues, allow_na=True)
    check_species(cst.get("species"), where, "species", issues, single=True)
    check_provenance(cst.get("provenance"), where, issues)
    check_marker_case(cst.get("markers"), cst.get("species"), where, issues)
    check_multi_format(cst.get("markers"), where, "markers", issues)

    # 自由文本字段（可能含括号子列表）：守分号不得嵌入括号内部
    for fld in ("condition_specificity", "functional_signature", "lineage"):
        check_no_nested_delimiter(cst.get(fld), where, fld, issues)

    npc = cst.get("n_cells_or_pct")
    if not is_missing(npc):
        s = str(npc)
        if not (INT_RE.match(s) or PCT_RE.match(s)):
            issues.add(where, f"n_cells_or_pct 应为整数 / 百分比(如 12.4%) / NA：{s!r}")

    for forbidden in ("subtype_id", "dataset_id", "paper_id"):
        if forbidden in cst and not is_missing(cst.get(forbidden)) \
                and str(cst.get(forbidden)) != AUTO:
            issues.add(where, f"cell_subtypes 不应自带 {forbidden}（由 ingest.py 回填/赋号）")

    check_unknown_fields(cst, CST_KNOWN_FIELDS, {}, where, issues)


def validate_processing_block(proc: Any, issues: Issues) -> None:
    """校验 processing 块（提取阶段不含 proc_id/dataset_id/paper_id）。"""
    where = "processing"
    if not isinstance(proc, dict):
        issues.add(where, "processing 必须是 JSON 对象")
        return

    check_required(proc, PROC_REQUIRED, where, issues)
    check_enum(proc.get("normalization"), PROC_NORMALIZATION, where,
               "normalization", issues, allow_na=True)
    check_enum(proc.get("batch_correction"), PROC_BATCH, where,
               "batch_correction", issues, multi=True, allow_na=True)
    check_enum(proc.get("annotation"), PROC_ANNOTATION, where,
               "annotation", issues, allow_na=True)
    check_enum(proc.get("diff_expr"), PROC_DIFF_EXPR, where,
               "diff_expr", issues, multi=True, allow_na=True)
    check_enum(proc.get("trajectory"), PROC_TRAJECTORY, where,
               "trajectory", issues, multi=True, allow_na=True)
    check_enum(proc.get("cell_comm"), PROC_CELL_COMM, where,
               "cell_comm", issues, multi=True, allow_na=True)
    check_provenance(proc.get("provenance"), where, issues)

    # 自由文本多值字段（用 ; 串多步骤/多工具，可能含括号子列表）：
    # 守卫分号不得嵌入括号内部，否则 stats/下游解析会拆碎（历史 bug：qc 字段）。
    # enrichment 同属此类：记富集分析「类型(工具)」如 GO(Metascape)，括号内多值用 '/'。
    for fld in ("qc", "dim_reduction", "clustering", "software", "enrichment"):
        check_no_nested_delimiter(proc.get(fld), where, fld, issues)

    for forbidden in ("proc_id", "dataset_id", "paper_id"):
        if forbidden in proc and not is_missing(proc.get(forbidden)) \
                and str(proc.get(forbidden)) != AUTO:
            issues.add(where, f"processing 不应自带 {forbidden}（由 ingest.py 回填/赋号）")

    check_unknown_fields(proc, PROC_KNOWN_FIELDS, PROC_FIELD_ALIASES, where, issues)


# ----------------------------------------------------------------------------
# 顶层校验入口（per-dataset 提取 JSON）
# ----------------------------------------------------------------------------
def validate_extraction(payload: Any, issues: Issues) -> None:
    """校验整份 per-dataset 提取 JSON。"""
    if not isinstance(payload, dict):
        issues.add("root", "顶层必须是 JSON 对象（per-dataset：dataset_id/dataset/cell_types/processing）")
        return

    # 兼容性硬护栏：若误用了旧的 paper/datasets(复数) 结构，明确报错指向 05 契约
    if "paper" in payload or "datasets" in payload:
        issues.add("root", "检测到旧结构(paper/datasets[])。本库提取 JSON 为 per-dataset 结构："
                           "顶层用 dataset_id + dataset(单对象) + cell_types[] + processing(单对象)，"
                           "不含 paper（详见 05_extraction.md §2）。")

    if is_missing(payload.get("dataset_id")):
        issues.add("root", "缺少顶层 dataset_id")
    if "dataset" not in payload:
        issues.add("root", "缺少 dataset 块（对应 datasets 表）")
    else:
        validate_dataset_block(payload["dataset"], payload.get("dataset_id"), issues)

    cts = payload.get("cell_types")
    if not isinstance(cts, list):
        issues.add("root", "cell_types 必须是数组（可为空数组，但至少应有 PNS 细胞才算合格）")
    else:
        for i, ct in enumerate(cts):
            validate_cell_type(ct, i, issues)
        # 合格性提示：至少 1 条 is_pns_cell=true
        n_pns = sum(1 for c in cts if isinstance(c, dict)
                    and str(c.get("is_pns_cell")) == "true")
        if n_pns == 0:
            issues.add("cell_types", "无任何 is_pns_cell=true 的细胞类型；"
                                     "该数据集可能不合格，请人工复核（_self_check.qualified 应为 false）")

    # cell_subtypes 为可选数组（无亚群细分的数据集可省略或空数组）
    csts = payload.get("cell_subtypes")
    if csts is not None:
        if not isinstance(csts, list):
            issues.add("root", "cell_subtypes 必须是数组（可省略或为空数组）")
        else:
            for i, cst in enumerate(csts):
                validate_cell_subtype(cst, i, issues)

    if "processing" not in payload:
        issues.add("root", "缺少 processing 块（对应 processing 表）")
    else:
        validate_processing_block(payload["processing"], issues)


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------
def main() -> int:
    parser = argparse.ArgumentParser(
        description="校验一份 per-dataset 提取 JSON 是否符合外周神经 scRNA 数据库 schema。")
    parser.add_argument("path", nargs="?",
                        help="待校验 JSON 文件路径（省略则配合 --stdin）")
    parser.add_argument("--stdin", action="store_true",
                        help="从标准输入读取 JSON")
    parser.add_argument("--json", action="store_true", dest="as_json",
                        help="以 JSON 输出校验结果（机器可读）")
    args = parser.parse_args()

    try:
        if args.stdin:
            raw = sys.stdin.read()
        elif args.path:
            raw = Path(args.path).read_text(encoding="utf-8")
        else:
            parser.error("需提供 JSON 文件路径或使用 --stdin")
            return 2
    except OSError as e:
        print(f"[ERROR] 无法读取输入：{e}", file=sys.stderr)
        return 2

    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"[ERROR] JSON 解析失败：{e}", file=sys.stderr)
        return 2

    issues = Issues()
    validate_extraction(payload, issues)

    if args.as_json:
        result = {
            "passed": issues.ok(),
            "error_count": len(issues.errors),
            "errors": [{"where": w, "message": m} for w, m in issues.errors],
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        if issues.ok():
            print("[PASS] 校验通过：未发现错误。")
        else:
            print(f"[FAIL] 校验未通过，共 {len(issues.errors)} 处错误：")
            for w, m in issues.errors:
                print(f"  - {w}: {m}")

    return 0 if issues.ok() else 1


if __name__ == "__main__":
    sys.exit(main())
