"""Marker 提取 schema v2 的枚举、校验和候选分层规则。"""

from __future__ import annotations

import re
from typing import Any

SCHEMA_VERSION = 2

FORMAL_EVIDENCE_TYPES = {
    "author_declared",
    "annotation_marker",
    "figure_labeled",
    "supplementary_marker",
}

CONTEXT_EVIDENCE_TYPES = {
    "cluster_enriched",
    "model_inferred",
    "reference_imported",
}

EVIDENCE_TYPES = FORMAL_EVIDENCE_TYPES | CONTEXT_EVIDENCE_TYPES
MARKER_POLARITIES = {"positive", "negative", "unknown"}
DOCUMENT_ROLES = {"primary", "supplement", "extended_data", "correction"}
SPECIES_VALUES = {"human", "mouse", "rat", "other", "unknown"}
PNS_VALUES = {"true", "false", "NA"}

EVIDENCE_RANK = {
    "author_declared": 7,
    "annotation_marker": 6,
    "supplementary_marker": 5,
    "figure_labeled": 4,
    "cluster_enriched": 3,
    "model_inferred": 2,
    "reference_imported": 1,
}

FORMAL_EVIDENCE_PATTERNS = {
    "author_declared": re.compile(
        r"\bmarkers?\b|characteri[sz]ed by|defined by|\bsignature\b",
        re.IGNORECASE,
    ),
    "annotation_marker": re.compile(
        r"\bmarkers?\b|annotat|identif|classif|defined by|used .{0,60}(?:identify|annotat|label)",
        re.IGNORECASE,
    ),
    "figure_labeled": re.compile(r"\bmarkers?\b", re.IGNORECASE),
    "supplementary_marker": re.compile(r"\bmarkers?\b|annotat", re.IGNORECASE),
}

NEGATIVE_POLARITY_PATTERN = re.compile(
    r"\bnegative\b|\babsence\b|\babsent\b|\blacks?\b|\blow(?:er)?\b|"
    r"not express|without expression|depleted",
    re.IGNORECASE,
)


class MarkerSchemaError(ValueError):
    """提取 JSON 不符合 marker schema。"""


def candidate_class_for(evidence_type: str) -> str:
    if evidence_type in FORMAL_EVIDENCE_TYPES:
        return "formal_candidate"
    if evidence_type in CONTEXT_EVIDENCE_TYPES:
        return "context_only"
    raise MarkerSchemaError(f"未知 evidence_type: {evidence_type!r}")


def apply_evidence_guardrail(marker: dict[str, Any]) -> dict[str, Any]:
    """把缺少作者措辞支持的“正式 marker”降级为上下文候选。"""
    normalized = dict(marker)
    evidence_type = str(normalized["evidence_type"])
    source_text = f"{normalized.get('source_locator', '')} {normalized.get('source_context', '')}"
    pattern = FORMAL_EVIDENCE_PATTERNS.get(evidence_type)
    if pattern is not None and not pattern.search(source_text):
        normalized["model_evidence_type"] = evidence_type
        normalized["evidence_type"] = "cluster_enriched"
        normalized["guardrail_reason"] = "缺少作者 marker/注释措辞，降级为表达或富集上下文"
    if (
        normalized.get("marker_polarity") == "negative"
        and not NEGATIVE_POLARITY_PATTERN.search(source_text)
    ):
        normalized["model_marker_polarity"] = "negative"
        normalized["marker_polarity"] = "unknown"
        previous_reason = normalized.get("guardrail_reason", "")
        polarity_reason = "缺少阴性/缺失表达措辞，极性降为 unknown"
        normalized["guardrail_reason"] = "; ".join(filter(None, (previous_reason, polarity_reason)))
    normalized["candidate_class"] = candidate_class_for(str(normalized["evidence_type"]))
    return normalized


def apply_payload_guardrails(payload: dict[str, Any]) -> dict[str, int]:
    counts = {"evidence_downgraded": 0, "polarity_downgraded": 0}
    for cell_type in payload.get("cell_types", []):
        normalized_markers: list[dict[str, Any]] = []
        for marker in cell_type.get("markers", []):
            original_evidence = marker.get("evidence_type")
            original_polarity = marker.get("marker_polarity")
            normalized = apply_evidence_guardrail(marker)
            if normalized.get("evidence_type") != original_evidence:
                counts["evidence_downgraded"] += 1
            if normalized.get("marker_polarity") != original_polarity:
                counts["polarity_downgraded"] += 1
            normalized_markers.append(normalized)
        cell_type["markers"] = normalized_markers
    return counts


def validate_marker(marker: dict[str, Any], location: str) -> None:
    gene = marker.get("gene")
    if not isinstance(gene, str) or not gene.strip():
        raise MarkerSchemaError(f"{location}.gene 必须是非空字符串")
    evidence_type = marker.get("evidence_type")
    if evidence_type not in EVIDENCE_TYPES:
        raise MarkerSchemaError(f"{location}.evidence_type 无效: {evidence_type!r}")
    polarity = marker.get("marker_polarity")
    if polarity not in MARKER_POLARITIES:
        raise MarkerSchemaError(f"{location}.marker_polarity 无效: {polarity!r}")
    for key in ("source_locator", "source_context"):
        value = marker.get(key)
        if not isinstance(value, str) or not value.strip():
            raise MarkerSchemaError(f"{location}.{key} 必须是非空字符串")


def validate_payload(payload: dict[str, Any]) -> None:
    if payload.get("schema_version") != SCHEMA_VERSION:
        raise MarkerSchemaError(
            f"schema_version 必须为 {SCHEMA_VERSION}，实际为 {payload.get('schema_version')!r}"
        )
    cell_types = payload.get("cell_types")
    if not isinstance(cell_types, list):
        raise MarkerSchemaError("cell_types 必须是数组")
    for cell_index, cell_type in enumerate(cell_types):
        location = f"cell_types[{cell_index}]"
        if not isinstance(cell_type, dict):
            raise MarkerSchemaError(f"{location} 必须是对象")
        if not isinstance(cell_type.get("cell_type"), str) or not cell_type["cell_type"].strip():
            raise MarkerSchemaError(f"{location}.cell_type 必须是非空字符串")
        if cell_type.get("species") not in SPECIES_VALUES:
            raise MarkerSchemaError(f"{location}.species 无效: {cell_type.get('species')!r}")
        if cell_type.get("is_pns_cell") not in PNS_VALUES:
            raise MarkerSchemaError(f"{location}.is_pns_cell 无效: {cell_type.get('is_pns_cell')!r}")
        markers = cell_type.get("markers")
        if not isinstance(markers, list):
            raise MarkerSchemaError(f"{location}.markers 必须是数组")
        for marker_index, marker in enumerate(markers):
            if not isinstance(marker, dict):
                raise MarkerSchemaError(f"{location}.markers[{marker_index}] 必须是对象")
            validate_marker(marker, f"{location}.markers[{marker_index}]")
