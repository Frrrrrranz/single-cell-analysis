"""Codex 抽查续检发现问题的确定性修复（2026-08-30）。

修复三项：
1. DOI_10.1038_s41588-025-02158-6 PLP1：figure_labeled 唯一依据是通用 dotplot 图注
   （"Dotplot showing the mean expression of marker genes..."，Fig. 1d legend L147）+
   基因轴 OCR（L112）与细胞轴 OCR（L113）同图共现；行列对应关系在 OCR 中丢失，
   无法读出 PLP1↔Schwann cells 具体映射，不满足计划 5.1 figure_labeled 标准。
   include → unresolved，paper_status corrected → unresolved。
   同篇 CDH19（"CD H19"，L112 OCR 带空格形式）维持 unresolved，reason 更准确化。
2. DOI_10.1016_j.cell.2022.11.005 NEUROD1（figure_labeled, pulmonary neuroendocrine cells）：
   Figure S8C 图注 "#1 labeled GRP+NEUROD1lowGHRL- cells"，NEUROD1low 用于区分
   #1/#2/#3 亚群，按计划 5.4（low 不得因缺少 negative 单词降为 unknown）→ negative。
3. DOI_10.1016_j.stem.2022.11.013：Figure S3G 图注明确声称 "showing transcript
   expression of marker genes specific to ... neuroendocrine lineages"（L1453），
   即 NE marker 证据存在但基因名在 Markdown 不可读。按计划第 6 节定义
   （关键证据只在不可读图表）paper_status 应为 unresolved 而非 no_formal_target_marker。
"""

from __future__ import annotations

import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
LOGGER = logging.getLogger(__name__)

SCRIPT_DIR = Path(__file__).resolve().parent
MARKER_DIR = SCRIPT_DIR.parent / "marker提取"
AUDIT_DIR = MARKER_DIR / "audited-extraction" / "markers"

FIX_TAG = "; Codex 抽查续检 2026-08-30"


def load(pid: str) -> tuple[Path, dict]:
    path = AUDIT_DIR / f"{pid}_audit.json"
    return path, json.loads(path.read_text(encoding="utf-8"))


def save(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    LOGGER.info("写回 %s", path.name)


def add_issue(data: dict, issue_type: str, description: str) -> None:
    data.setdefault("issues", []).append({"issue_type": issue_type, "description": description})


def fix_plp1() -> None:
    pid = "DOI_10.1038_s41588-025-02158-6"
    path, data = load(pid)
    changed = False
    for marker in data["markers"]:
        if marker.get("normalized_symbol") == "PLP1" and marker.get("decision") == "include":
            marker["decision"] = "unresolved"
            marker["reason"] = (
                "figure_labeled 证据不足：唯一依据为 Fig. 1d 通用图注"
                "（Dotplot showing the mean expression of marker genes...）与基因轴 OCR（PLP1）/"
                "细胞轴 OCR（Schwann cells）同图共现；OCR 无法读出 PLP1 与 Schwann cells 的"
                "具体对应关系，不满足 figure_labeled 标准（计划 5.1）" + FIX_TAG
            )
            changed = True
        if marker.get("normalized_symbol") == "CDH19" and marker.get("decision") == "unresolved":
            marker["reason"] = (
                "Fig.1d dotplot 图轴 OCR 以带空格形式（CD H19，原文 L112）出现，"
                "但无法读出 CDH19 与 Schwann cells 的具体对应关系；"
                "不得用领域常识补证据，维持 unresolved 待查原图" + FIX_TAG
            )
    for marker in data["markers"]:
        if marker.get("normalized_symbol") == "CDH19" and marker.get("decision") == "unresolved":
            marker["reason"] = (
                "Fig.1d dotplot 基因轴 OCR 以带空格形式（CD H19，原文 L112）出现，"
                "但行列对应关系在 OCR 中丢失，无法读出 CDH19 与 Schwann cells 的具体映射；"
                "不得用领域常识补证据，维持 unresolved 待查原图" + FIX_TAG
            )
    if data.get("paper_status") == "corrected":
        data["paper_status"] = "unresolved"
        changed = True
    if changed:
        data["summary"] = (
            "原审核仅 PLP1 一条 include，Codex 抽查续检认定其 figure_labeled 证据不足"
            "（通用 dotplot 图例 + 轴共现，无具体 gene–cell 映射），降级 unresolved；"
            "目标细胞 Schwann 的正式 Marker 证据均在不可读图表中，paper_status 改为 unresolved。"
        )
        add_issue(
            data,
            "evidence",
            "PLP1 figure_labeled include 证据不足：通用 dotplot 图注 + 基因轴/细胞轴 OCR 共现"
            "不构成具体 gene–cell 映射（计划 5.1），已降级 unresolved" + FIX_TAG,
        )
        add_issue(
            data,
            "citation",
            "CDH19 在原文以 OCR 带空格形式（CD H19，L112）存在；词元覆盖失败的原因是 OCR 拆词，"
            "但图表映射同样不可读，维持 unresolved" + FIX_TAG,
        )
        save(path, data)


def fix_neurod1_polarity() -> None:
    pid = "DOI_10.1016_j.cell.2022.11.005"
    path, data = load(pid)
    changed = False
    for marker in data["markers"]:
        if (
            marker.get("normalized_symbol") == "NEUROD1"
            and marker.get("evidence_type") == "figure_labeled"
            and marker.get("marker_polarity") == "unknown"
            and marker.get("decision") == "include"
        ):
            marker["marker_polarity"] = "negative"
            marker["reason"] = (
                (marker.get("reason") or "").rstrip("; ")
                + "; 极性修正：Figure S8C 图注 #1 labeled GRP+NEUROD1lowGHRL-，"
                "NEUROD1low 用于区分 #1/#2/#3 亚群，按计划 5.4（low 用于区分时为 negative）"
                "由 unknown 改为 negative" + FIX_TAG
            )
            changed = True
    if changed:
        add_issue(
            data,
            "polarity",
            "NEUROD1（figure_labeled, pulmonary neuroendocrine cells）极性 unknown→negative："
            "S8C 图注 NEUROD1low 用于亚群区分（计划 5.4）" + FIX_TAG,
        )
        save(path, data)


def fix_stem_status() -> None:
    pid = "DOI_10.1016_j.stem.2022.11.013"
    path, data = load(pid)
    if data.get("paper_status") != "no_formal_target_marker":
        return
    data["paper_status"] = "unresolved"
    data["summary"] = (
        "主动扫描全文确认论文未在正文给出 pulmonary neuroendocrine cell 的具体 marker 基因"
        "（ASCL1/CHGA/SYP/GRP/CGRP 均 0 次出现）；但 Figure S3G 图注明确写 "
        "「UMAP plots showing transcript expression of marker genes specific to ... neuroendocrine "
        "lineages」（L1453），即 NE marker 证据存在、仅基因名在 Markdown 中不可读。"
        "按计划第 6 节定义（关键证据只在不可读图表），状态由 no_formal_target_marker 改为 unresolved。"
    )
    add_issue(
        data,
        "other",
        "paper_status 修正：S3G 图注声称展示 neuroendocrine lineage 的 marker genes，"
        "但具体基因不可读；属「证据在不可读图表」而非「无 marker」，应为 unresolved" + FIX_TAG,
    )
    save(path, data)


def main() -> None:
    fix_plp1()
    fix_neurod1_polarity()
    fix_stem_status()


if __name__ == "__main__":
    main()
