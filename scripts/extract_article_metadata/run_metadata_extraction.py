"""从论文 Markdown 提取文章级元数据、神经相关细胞和单细胞统计方法。"""

from __future__ import annotations

import argparse
import json
import logging
import os
import re
import time
from pathlib import Path
from typing import Any, Iterable

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - 运行环境缺少可选依赖时由 API 调用阶段报告
    load_dotenv = None


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SCOPE_MAPPING = PROJECT_ROOT / "scripts" / "extract_article_metadata" / "output" / "scope_mapping.json"
REVIEW_MD_DIR = PROJECT_ROOT / "scripts" / "extract_markers" / "review_md"
OUTPUT_DIR = PROJECT_ROOT / "scripts" / "extract_article_metadata" / "output"
DEFAULT_PROMPT = PROJECT_ROOT / "scripts" / "extract_article_metadata" / "article_metadata_prompt.md"
MAX_CHARS = 100_000
SCHEMA_VERSION = 1

LOGGER = logging.getLogger(__name__)

ARTICLE_METADATA_PROMPT = """你是一位单细胞组学文献整理专家。请从给定论文 Markdown 中提取文章元数据，不要补写原文没有报告的信息。

核心边界：
1. 只记录论文正文、Methods、Figure legend、Supplementary 中能够定位的内容；引言、讨论、参考文献中仅提到的细胞必须标记为 discussion_only，不能当作本研究检测结果。
2. 组织来源记录实际取样组织/器官；不要把疾病名称、讨论中提到的器官或数据集标签误当作取样组织。
3. 神经相关细胞包括神经元、外周神经胶质和神经内分泌细胞，但必须保留 cell_category、pns_level 和 evidence_context 的区分。
4. 统计方法只记录与单细胞分析直接相关且原文明确报告的内容。未报告的参数留空，必要时通过 issues 标记 not_reported，不根据软件默认行为推断。
5. source_locator 必须具体到章节、Figure、Table 或页码；evidence_snippet 使用短原文片段，便于回查，不要大段复制。
6. 同一条证据在不同分块重复出现时，合并时保留信息更完整的一条。
7. 不重新判断 Marker，不列出新的 marker 基因；marker_linkage 只填写输入中给出的现有结果文件信息。

字段约束：
- cell_category: neuron / peripheral_glia / neuroendocrine / other_neural
- pns_level: L1 / L2 / L4 / NA
- evidence_context: detected / cluster / annotation / discussion_only
- analysis_stage: quality_control / normalization_integration / dimension_reduction_clustering / differential_expression / enrichment / abundance_proportion / multiple_testing / software / other
- review_status: supported / pending / discussion_only / not_reported

只输出 JSON 对象，不要代码围栏或解释：
{
  "schema_version": 1,
  "paper_id": "输入提供的 paper_id",
  "document_id": "输入提供的 document_id",
  "task_no": 0,
  "source_markdown": "输入提供的 Markdown 文件名",
  "article_identity": {"title_original": "", "doi": "", "pmid": "", "species": []},
  "tissue_sources": [{
    "tissue_source_original": "",
    "tissue_source_normalized": "",
    "sample_context": "",
    "species": "",
    "single_cell_type": "",
    "source_locator": "",
    "evidence_snippet": ""
  }],
  "neural_cells": [{
    "cell_name_original": "",
    "cell_name_normalized": "",
    "cell_category": "neuron",
    "pns_level": "NA",
    "tissue": "",
    "evidence_context": "detected",
    "source_locator": "",
    "evidence_snippet": "",
    "review_status": "supported"
  }],
  "statistics_methods": [{
    "analysis_stage": "quality_control",
    "method_original": "",
    "method_normalized": "",
    "software": "",
    "software_version": "",
    "threshold": "",
    "multiple_testing": "",
    "source_locator": "",
    "evidence_snippet": "",
    "review_status": "supported"
  }],
  "marker_linkage": {
    "marker_status": "",
    "formal_candidate_count": null,
    "context_only_count": null,
    "raw_json_file": "",
    "review_csv_file": "",
    "master_table_present": true
  },
  "issues": [{
    "issue_type": "",
    "severity": "info",
    "field": "",
    "description": "",
    "source_locator": "",
    "evidence_snippet": ""
  }]
}
"""


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as stream:
        value = json.load(stream)
    if not isinstance(value, dict):
        raise ValueError(f"JSON 顶层必须是对象: {path}")
    return value


def clean_json_text(text: str) -> str:
    stripped = text.strip()
    fenced = re.match(r"^```(?:json)?\s*(.*?)\s*```$", stripped, re.IGNORECASE | re.DOTALL)
    return fenced.group(1).strip() if fenced else stripped


def first_value(row: dict[str, Any], names: Iterable[str]) -> object:
    for name in names:
        value = row.get(name)
        if value not in (None, ""):
            return value
    return ""


def normalize_rows(rows: object, aliases: dict[str, tuple[str, ...]]) -> list[dict[str, Any]]:
    if isinstance(rows, dict):
        rows = [rows]
    if not isinstance(rows, list):
        return []
    normalized: list[dict[str, Any]] = []
    for raw_row in rows:
        if isinstance(raw_row, str):
            raw_row = {"name": raw_row, "label": raw_row, "original": raw_row}
        if not isinstance(raw_row, dict):
            continue
        normalized.append({field: first_value(raw_row, names) for field, names in aliases.items()})
    return normalized


def infer_cell_category(name: str) -> str:
    lowered = name.casefold()
    if any(term in lowered for term in ("neuroendocrine", "enteroendocrine", "pnec", "ne cells")):
        return "neuroendocrine"
    if any(term in lowered for term in ("schwann", "satellite glia", "glial", "glia")):
        return "peripheral_glia"
    if any(term in lowered for term in ("neuron", "nociceptor", "sensory", "sympathetic", "parasympathetic", "enteric")):
        return "neuron"
    return "other_neural"


def infer_analysis_stage(method: str) -> str:
    lowered = method.casefold()
    if any(term in lowered for term in ("quality", "qc", "mitochond", "doublet", "low-quality")):
        return "quality_control"
    if any(term in lowered for term in ("normaliz", "integration", "batch", "harmony", "sctransform")):
        return "normalization_integration"
    if any(term in lowered for term in ("umap", "pca", "cluster", "clustering", "dimensionality", "paga")):
        return "dimension_reduction_clustering"
    if any(term in lowered for term in ("differential", "deg", "gene expression")):
        return "differential_expression"
    if any(term in lowered for term in ("enrichment", "scenic", "cellphonedb", "gene signature", "trajectory")):
        return "enrichment"
    if any(term in lowered for term in ("proportion", "abundance", "composition", "chi-square", "chi square")):
        return "abundance_proportion"
    if any(term in lowered for term in ("software", "package", "version")):
        return "software"
    return "other"


def normalize_semantics(payload: dict[str, Any]) -> dict[str, Any]:
    for row in payload.get("neural_cells", []):
        name = nonempty(row.get("cell_name_original"))
        if not nonempty(row.get("cell_category")):
            row["cell_category"] = infer_cell_category(name)
        if not nonempty(row.get("pns_level")):
            row["pns_level"] = (
                "L4" if row["cell_category"] == "neuroendocrine"
                else "L1" if row["cell_category"] == "neuron"
                else "L2" if row["cell_category"] == "peripheral_glia"
                else "NA"
            )
        if not nonempty(row.get("evidence_context")):
            row["evidence_context"] = "discussion_only" if "discussion" in nonempty(row.get("source_locator")).casefold() else "detected"
        if not nonempty(row.get("review_status")):
            row["review_status"] = "discussion_only" if row["evidence_context"] == "discussion_only" else "supported"
    for row in payload.get("statistics_methods", []):
        if not nonempty(row.get("analysis_stage")):
            row["analysis_stage"] = infer_analysis_stage(nonempty(row.get("method_original")))
        if not nonempty(row.get("review_status")):
            row["review_status"] = "supported"
    return payload


def normalize_model_payload(payload: dict[str, Any]) -> dict[str, Any]:
    """兼容模型使用的同义字段名，保持内容不变后再进入本地 schema 校验。"""
    tissue_aliases = {
        "tissue_source_original": ("tissue_source_original", "tissue_original", "tissue", "organ", "tissue_name", "name", "label", "original"),
        "tissue_source_normalized": ("tissue_source_normalized", "tissue_normalized", "normalized_tissue", "normalized_name", "normalized"),
        "sample_context": ("sample_context", "context", "sample_type", "condition"),
        "species": ("species", "organism"),
        "single_cell_type": ("single_cell_type", "technology", "assay", "sequencing_type"),
        "source_locator": ("source_locator", "locator", "evidence_locator", "source"),
        "evidence_snippet": ("evidence_snippet", "snippet", "evidence", "evidence_context"),
    }
    cell_aliases = {
        "cell_name_original": ("cell_name_original", "cell_original", "cell_name", "original_name", "cell_type", "name", "label"),
        "cell_name_normalized": ("cell_name_normalized", "cell_normalized", "normalized_name", "normalized_cell_type"),
        "cell_category": ("cell_category", "category", "type"),
        "pns_level": ("pns_level", "PNS_level", "level"),
        "tissue": ("tissue", "organ", "tissue_source"),
        "evidence_context": ("evidence_context", "evidence_type", "context"),
        "source_locator": ("source_locator", "locator", "evidence_locator", "source"),
        "evidence_snippet": ("evidence_snippet", "snippet", "evidence", "evidence_text"),
        "review_status": ("review_status", "status"),
    }
    statistic_aliases = {
        "analysis_stage": ("analysis_stage", "stage", "analysis_step"),
        "method_original": ("method_original", "method", "method_description", "description", "name", "label"),
        "method_normalized": ("method_normalized", "normalized_method", "method_standardized"),
        "software": ("software", "tool", "package"),
        "software_version": ("software_version", "version"),
        "threshold": ("threshold", "cutoff", "parameters"),
        "multiple_testing": ("multiple_testing", "multiple_testing_correction", "adjustment"),
        "source_locator": ("source_locator", "locator", "evidence_locator", "source"),
        "evidence_snippet": ("evidence_snippet", "snippet", "evidence", "evidence_text"),
        "review_status": ("review_status", "status"),
    }
    normalized = dict(payload)
    normalized["schema_version"] = SCHEMA_VERSION
    normalized["article_identity"] = payload.get("article_identity", {}) if isinstance(payload.get("article_identity", {}), dict) else {}
    normalized["tissue_sources"] = normalize_rows(
        payload.get("tissue_sources", payload.get("tissue_origin", [])), tissue_aliases
    )
    normalized["neural_cells"] = normalize_rows(
        payload.get("neural_cells", payload.get("neural_related_cells", payload.get("neural_associated_cells", []))),
        cell_aliases,
    )
    normalized["statistics_methods"] = normalize_rows(
        payload.get(
            "statistics_methods",
            payload.get("single_cell_analysis_statistics", payload.get("single_cell_analysis_statistical_methods", [])),
        ),
        statistic_aliases,
    )
    normalized["issues"] = payload.get("issues", []) if isinstance(payload.get("issues", []), list) else []
    normalized["marker_linkage"] = payload.get("marker_linkage", {}) if isinstance(payload.get("marker_linkage", {}), dict) else {}
    return normalize_semantics(normalized)


def split_markdown(text: str, max_chars: int = MAX_CHARS) -> list[tuple[str, str]]:
    """按 Markdown 章节切分，避免把一个完整段落硬切开。"""
    sections: list[tuple[str, str]] = []
    current_name = "preamble"
    current_lines: list[str] = []
    for line in text.splitlines():
        heading = re.match(r"^#{1,4}\s+(.+?)\s*$", line)
        if heading:
            content = "\n".join(current_lines).strip()
            if content:
                sections.append((current_name, content))
            current_name = heading.group(1).strip()
            current_lines = []
        else:
            current_lines.append(line)
    content = "\n".join(current_lines).strip()
    if content:
        sections.append((current_name, content))

    chunks: list[tuple[str, str]] = []
    for section_name, section_content in sections:
        if len(section_content) <= max_chars:
            chunks.append((section_name, section_content))
            continue
        paragraphs = re.split(r"\n\s*\n", section_content)
        current: list[str] = []
        current_size = 0
        part = 1
        for paragraph in paragraphs:
            if current and current_size + len(paragraph) + 2 > max_chars:
                chunks.append((f"{section_name}_part{part}", "\n\n".join(current)))
                part += 1
                current = []
                current_size = 0
            current.append(paragraph)
            current_size += len(paragraph) + 2
        if current:
            chunks.append((f"{section_name}_part{part}", "\n\n".join(current)))
    return chunks


def nonempty(value: object) -> str:
    return str(value).strip() if value is not None else ""


def validate_payload(payload: dict[str, Any], expected: dict[str, Any]) -> None:
    if payload.get("schema_version") != SCHEMA_VERSION:
        raise ValueError("schema_version 无效")
    for key in ("tissue_sources", "neural_cells", "statistics_methods", "issues"):
        if not isinstance(payload.get(key), list):
            raise ValueError(f"{key} 必须是数组")
    if not isinstance(payload.get("article_identity"), dict):
        raise ValueError("article_identity 必须是对象")
    for key in ("paper_id", "document_id"):
        expected_value = expected.get(key) if key in expected else expected.get("paper_id")
        if nonempty(payload.get(key)) != nonempty(expected_value):
            raise ValueError(f"{key} 与输入映射不一致")


def row_key(row: dict[str, Any], fields: Iterable[str]) -> str:
    return "|".join(nonempty(row.get(field)).casefold() for field in fields)


def merge_rows(existing: list[dict[str, Any]], incoming: list[dict[str, Any]], fields: Iterable[str]) -> list[dict[str, Any]]:
    merged: list[dict[str, Any]] = [dict(row) for row in existing if isinstance(row, dict)]
    positions = {row_key(row, fields): index for index, row in enumerate(merged)}
    for raw_row in incoming:
        if not isinstance(raw_row, dict):
            continue
        row = dict(raw_row)
        key = row_key(row, fields)
        if not key.strip("|"):
            continue
        if key not in positions:
            positions[key] = len(merged)
            merged.append(row)
            continue
        target = merged[positions[key]]
        for field, value in row.items():
            if not nonempty(target.get(field)) and nonempty(value):
                target[field] = value
    return merged


def merge_payloads(payloads: list[dict[str, Any]], expected: dict[str, Any]) -> dict[str, Any]:
    if not payloads:
        raise ValueError("没有可合并的提取结果")
    merged: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "paper_id": expected["paper_id"],
        "document_id": expected["paper_id"],
        "task_no": expected["序号"],
        "source_markdown": expected["markdown_file"],
        "article_identity": {
            "title_original": nonempty(expected.get("论文标题")),
            "doi": nonempty(expected.get("DOI")),
            "pmid": nonempty(expected.get("PMID")),
            "species": [nonempty(expected.get("物种"))] if nonempty(expected.get("物种")) else [],
        },
        "tissue_sources": [],
        "neural_cells": [],
        "statistics_methods": [],
        "marker_linkage": {},
        "issues": [],
    }
    for payload in payloads:
        identity = payload.get("article_identity")
        if isinstance(identity, dict):
            for field, value in identity.items():
                if not nonempty(merged["article_identity"].get(field)) and nonempty(value):
                    merged["article_identity"][field] = value
        merged["tissue_sources"] = merge_rows(
            merged["tissue_sources"], payload.get("tissue_sources", []),
            ("tissue_source_original", "sample_context", "species", "single_cell_type", "source_locator"),
        )
        merged["neural_cells"] = merge_rows(
            merged["neural_cells"], payload.get("neural_cells", []),
            ("cell_name_original", "tissue", "evidence_context", "source_locator"),
        )
        merged["statistics_methods"] = merge_rows(
            merged["statistics_methods"], payload.get("statistics_methods", []),
            ("analysis_stage", "method_original", "software", "threshold", "source_locator"),
        )
        merged["issues"] = merge_rows(
            merged["issues"], payload.get("issues", []),
            ("issue_type", "field", "description", "source_locator"),
        )
        linkage = payload.get("marker_linkage")
        if isinstance(linkage, dict):
            for field, value in linkage.items():
                if not nonempty(merged["marker_linkage"].get(field)) and value not in (None, ""):
                    merged["marker_linkage"][field] = value
    return merged


def call_llm(system_prompt: str, user_content: str, model: str, api_key: str, api_base: str) -> dict[str, Any]:
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RuntimeError("未安装 openai，无法执行文章元数据提取") from exc
    client_kwargs: dict[str, str] = {"api_key": api_key}
    if api_base:
        client_kwargs["base_url"] = api_base
    client = OpenAI(**client_kwargs, timeout=120.0, max_retries=1)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_content}],
        temperature=0.1,
        response_format={"type": "json_object"},
    )
    content = response.choices[0].message.content or ""
    value = json.loads(clean_json_text(content))
    if not isinstance(value, dict):
        raise ValueError("LLM 返回的 JSON 顶层不是对象")
    return normalize_model_payload(value)


def load_scope() -> list[dict[str, Any]]:
    payload = load_json(SCOPE_MAPPING)
    return [row for row in payload.get("records", []) if isinstance(row, dict) and row.get("processing_status") == "matched"]


def build_marker_linkage(paper_id: str, marker_status: str) -> dict[str, Any]:
    raw_path = PROJECT_ROOT / "scripts" / "extract_markers" / "markers_output_v2" / f"{paper_id}_raw.json"
    review_path = PROJECT_ROOT / "scripts" / "extract_markers" / "markers_output_v2" / f"{paper_id}_review.csv"
    formal_count: int | None = None
    context_count: int | None = None
    if raw_path.exists():
        try:
            raw = load_json(raw_path)
            markers = [marker for cell_type in raw.get("cell_types", []) if isinstance(cell_type, dict) for marker in cell_type.get("markers", []) if isinstance(marker, dict)]
            formal_count = sum(marker.get("evidence_type") in {"author_declared", "annotation_marker", "figure_labeled", "supplementary_marker"} for marker in markers)
            context_count = len(markers) - formal_count
        except (OSError, ValueError, TypeError):
            LOGGER.warning("读取 Marker 结果失败: %s", raw_path)
    return {
        "marker_status": marker_status,
        "formal_candidate_count": formal_count,
        "context_only_count": context_count,
        "raw_json_file": str(raw_path.relative_to(PROJECT_ROOT)).replace("\\", "/") if raw_path.exists() else "",
        "review_csv_file": str(review_path.relative_to(PROJECT_ROOT)).replace("\\", "/") if review_path.exists() else "",
        "master_table_present": (PROJECT_ROOT / "db" / "cellxgene" / "our_markers.xlsx").exists(),
    }


def extract_document(row: dict[str, Any], model: str, api_key: str, api_base: str, prompt: str, skip_existing: bool) -> Path | None:
    paper_id = nonempty(row.get("paper_id"))
    markdown_file = nonempty(row.get("markdown_file"))
    markdown_path = REVIEW_MD_DIR / markdown_file
    output_path = OUTPUT_DIR / f"{paper_id}_metadata.json"
    if skip_existing and output_path.exists():
        LOGGER.info("跳过已有结果: %s", output_path.name)
        return output_path
    text = markdown_path.read_text(encoding="utf-8")
    chunks = split_markdown(text)
    LOGGER.info("处理 %s: %d 个文本块", paper_id, len(chunks))
    payloads: list[dict[str, Any]] = []
    for index, (section_name, section_text) in enumerate(chunks, start=1):
        user_content = (
            f"输入任务元数据：paper_id={paper_id}; document_id={paper_id}; task_no={row.get('序号')}; "
            f"source_markdown={markdown_file}; 表中论文标题={row.get('论文标题')}; 表中物种={row.get('物种')}; "
            f"表中组织={row.get('组织')}; 表中技术={row.get('技术')}。\n"
            f"当前文本块：{section_name}（{index}/{len(chunks)}）\n\n论文 Markdown：\n{section_text}"
        )
        result: dict[str, Any] | None = None
        try:
            result = call_llm(prompt, user_content, model=model, api_key=api_key, api_base=api_base)
            result["paper_id"] = paper_id
            result["document_id"] = paper_id
            result["task_no"] = row.get("序号")
            result["source_markdown"] = markdown_file
            validate_payload(result, row)
            payloads.append(result)
        except Exception as exc:  # 单块失败后整篇不落盘，避免生成不完整结果
            if isinstance(result, dict):
                LOGGER.exception(
                    "%s 文本块 %d/%d 提取失败: %s；返回 schema_version=%r，keys=%s",
                    paper_id,
                    index,
                    len(chunks),
                    exc,
                    result.get("schema_version"),
                    sorted(result.keys()),
                )
            else:
                LOGGER.exception("%s 文本块 %d/%d 提取失败: %s", paper_id, index, len(chunks), exc)
            return None
        if index < len(chunks):
            time.sleep(1)
    merged = merge_payloads(payloads, row)
    merged["marker_linkage"] = build_marker_linkage(paper_id, nonempty(row.get("Marker状态")))
    merged["source_markdown"] = markdown_file
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LOGGER.info("完成 %s: tissue=%d, neural=%d, stats=%d", paper_id, len(merged["tissue_sources"]), len(merged["neural_cells"]), len(merged["statistics_methods"]))
    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Markdown → LLM → 文章元数据 JSON")
    parser.add_argument("--pilot", action="store_true", help="运行预设 5 篇试跑文章")
    parser.add_argument("--all", action="store_true", help="处理所有存在 Markdown 的负责文章")
    parser.add_argument("--paper-id", action="append", help="指定一个或多个 paper_id")
    parser.add_argument("--skip-existing", action="store_true", help="跳过已有 JSON")
    parser.add_argument("--model", default=None, help="覆盖 MARKER_LLM_MODEL")
    parser.add_argument("--api-key", default=None, help="覆盖 MARKER_LLM_API_KEY")
    parser.add_argument("--api-base", default=None, help="覆盖 MARKER_LLM_API_BASE")
    parser.add_argument("--prompt-file", type=Path, default=DEFAULT_PROMPT)
    return parser.parse_args()


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    if load_dotenv is not None:
        load_dotenv(PROJECT_ROOT / ".env")
    args = parse_args()
    rows = load_scope()
    pilot_ids = {
        "DOI_10.1016_j.cell.2022.11.005",
        "DOI_10.1038_s41467-024-52052-8",
        "DOI_10.1038_s41586-024-07069-w",
        "DOI_10.1016_j.cell.2017.09.004",
        "DOI_10.1101_2024.10.23.619925",
    }
    if args.pilot:
        rows = [row for row in rows if row.get("paper_id") in pilot_ids]
    elif args.paper_id:
        wanted = set(args.paper_id)
        rows = [row for row in rows if row.get("paper_id") in wanted]
    elif not args.all:
        raise SystemExit("请指定 --pilot、--all 或 --paper-id")
    api_key = args.api_key or os.environ.get("MARKER_LLM_API_KEY", "")
    api_base = args.api_base or os.environ.get("MARKER_LLM_API_BASE", "")
    model = args.model or os.environ.get("MARKER_LLM_MODEL", "")
    if not api_key or not model:
        raise SystemExit("缺少 MARKER_LLM_API_KEY 或 MARKER_LLM_MODEL")
    prompt = args.prompt_file.read_text(encoding="utf-8")
    successes = 0
    for row in rows:
        if extract_document(row, model, api_key, api_base, prompt, args.skip_existing) is not None:
            successes += 1
    LOGGER.info("批处理完成: %d/%d", successes, len(rows))
    if successes != len(rows):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
