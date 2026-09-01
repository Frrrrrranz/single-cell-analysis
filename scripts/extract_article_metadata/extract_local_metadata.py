"""用确定性规则从现有论文 Markdown 整理文章元数据。"""

from __future__ import annotations

import argparse
import json
import logging
import re
from pathlib import Path
from typing import Any, Iterable

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SCOPE_PATH = PROJECT_ROOT / "scripts" / "extract_article_metadata" / "output" / "scope_mapping.json"
MARKDOWN_DIR = PROJECT_ROOT / "scripts" / "extract_markers" / "review_md"
OUTPUT_DIR = PROJECT_ROOT / "scripts" / "extract_article_metadata" / "output"
LOGGER = logging.getLogger(__name__)

NEURAL_ALIASES = {
    "schwann": ("Schwann cell", "Schwann cells"),
    "satellite glia": ("satellite glia", "satellite glial cell", "satellite glial cells"),
    "pulmonary neuroendocrine": ("pulmonary neuroendocrine", "PNEC", "pulmonary NE"),
    "neuroendocrine": ("neuroendocrine", "neuroendocrine cell", "NE cells"),
    "enteroendocrine": ("enteroendocrine", "enteroendocrine cell"),
    "sensory neuron": ("sensory neuron", "nociceptor", "nociceptors"),
    "enteric neuron": ("enteric neuron", "enteric neurons"),
    "sympathetic neuron": ("sympathetic neuron", "sympathetic neurons"),
    "parasympathetic neuron": ("parasympathetic neuron", "parasympathetic neurons"),
    "efferent neuron": ("efferent neuron", "efferent neurons"),
    "peripheral nervous system neuron": ("peripheral nervous system", "PNS neuron"),
    "neural cells": ("neural cells", "neural cell"),
}

STAT_METHODS = {
    "quality_control": ("quality control", "QC", "mitochondrial", "doublet", "low-quality", "filtering"),
    "normalization_integration": ("normalization", "normalized", "SCTransform", "Harmony", "batch correction", "integration"),
    "dimension_reduction_clustering": ("UMAP", "t-SNE", "PCA", "clustering", "cluster", "principal component", "PAGA"),
    "differential_expression": ("differential expression", "differentially expressed", "DEG", "FindMarkers", "gene expression analysis"),
    "enrichment": ("gene set enrichment", "enrichment analysis", "GSEA", "SCENIC", "CellPhoneDB", "ligand-receptor", "trajectory", "pseudotime", "RNA velocity"),
    "abundance_proportion": ("cell proportion", "cell composition", "differential abundance", "chi-square", "chi square", "abundance"),
    "multiple_testing": ("multiple testing", "Benjamini", "FDR", "false discovery", "Bonferroni", "adjusted p"),
    "software": ("Seurat", "Scanpy", "Cell Ranger", "Monocle", "scVelo", "CellPhoneDB", "Harmony", "SCENIC"),
}

TISSUE_NORMALIZATION = {
    "dorsal root ganglion": "dorsal root ganglion",
    "lumbar dorsal root ganglia": "dorsal root ganglion",
    "sciatic nerve": "sciatic nerve",
    "lung epithelium": "lung epithelium",
    "lung": "lung",
    "bronchus": "bronchus",
    "carina of trachea": "trachea carina",
    "nasopharynx": "nasopharynx",
    "urinary bladder": "urinary bladder",
    "dome of urinary bladder": "urinary bladder",
    "prostate gland": "prostate gland",
    "peripheral zone of prostate": "prostate gland",
    "islet of langerhans": "pancreatic islet",
    "pancreas": "pancreas",
    "kidney": "kidney",
    "mammary gland": "mammary gland",
    "bone marrow": "bone marrow",
    "adipose tissue": "adipose tissue",
    "heart": "heart",
    "blood": "blood",
    "embryo": "embryo",
}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as stream:
        value = json.load(stream)
    if not isinstance(value, dict):
        raise ValueError(f"JSON 顶层必须是对象: {path}")
    return value


def text_value(value: object) -> str:
    return str(value).strip() if value is not None else ""


def split_terms(value: str) -> list[str]:
    return [part.strip() for part in re.split(r"[/|;]+", value) if part.strip() and part.strip() not in {"—", "-", "NA"}]


def locator(line_no: int, heading: str) -> str:
    return f"Markdown line {line_no}" + (f"; section {heading}" if heading else "")


def iter_lines(text: str) -> Iterable[tuple[int, str, str]]:
    heading = ""
    for line_no, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        match = re.match(r"^#{1,4}\s+(.+?)\s*$", line)
        if match:
            heading = match.group(1).strip()
            if re.search(r"references?|bibliography|acknowledg|author contributions|data availability|funding|conflict of interest", heading, re.IGNORECASE):
                break
        if line:
            yield line_no, heading, line


def article_body(text: str) -> str:
    match = re.search(r"(?im)^#{1,4}\s+(?:references?|bibliography|acknowledg|author contributions|data availability|funding|conflict of interest)\b", text)
    return text[:match.start()] if match else text


def nearest_context(heading: str, line: str) -> str:
    lowered = f"{heading} {line}".casefold()
    if any(term in lowered for term in ("introduction", "discussion", "references", "background")):
        return "discussion_only"
    if any(term in lowered for term in ("cluster", "annotat", "identified", "classified", "cell type")):
        return "annotation"
    return "detected"


def cell_category(name: str) -> str:
    lowered = name.casefold()
    if "neuroendocrine" in lowered or "enteroendocrine" in lowered or "pnec" in lowered:
        return "neuroendocrine"
    if any(term in lowered for term in ("schwann", "glia")):
        return "peripheral_glia"
    if any(term in lowered for term in ("neuron", "nociceptor")):
        return "neuron"
    return "other_neural"


def pns_level(name: str, task_levels: str) -> str:
    for level in ("L1", "L2", "L4"):
        if level in task_levels:
            lowered = name.casefold()
            if (level == "L1" and any(term in lowered for term in ("neuron", "nociceptor"))) or (level == "L2" and any(term in lowered for term in ("schwann", "glia"))) or (level == "L4" and "endocrine" in lowered):
                return level
    category = cell_category(name)
    return "L1" if category == "neuron" else "L2" if category == "peripheral_glia" else "L4" if category == "neuroendocrine" else "NA"


def sample_context(title: str, text: str) -> str:
    lowered = f"{title} {text}".casefold()
    contexts: list[str] = []
    if any(term in lowered for term in ("fetal", "embryo", "pcw", "prenatal", "development")):
        contexts.append("fetal/developmental")
    if "organoid" in lowered:
        contexts.append("organoid")
    if any(term in lowered for term in ("cancer", "tumour", "tumor", "neoplasm")):
        contexts.append("tumor")
    if any(term in lowered for term in ("covid", "infection", "disease", "diabetes", "fibrosis", "copd", "rejection")):
        contexts.append("disease")
    if any(term in lowered for term in ("healthy", "normal", "control")):
        contexts.append("normal/control")
    return "; ".join(dict.fromkeys(contexts)) or ""


def find_first_evidence(text: str, patterns: Iterable[str], min_line: int = 1) -> tuple[str, str, str] | None:
    compiled = [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
    for line_no, heading, line in iter_lines(text):
        if line_no < min_line:
            continue
        if any(pattern.search(line) for pattern in compiled):
            return locator(line_no, heading), line[:600], heading
    return None


def extract_tissue(row: dict[str, Any], text: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    original = text_value(row.get("组织"))
    normalized = TISSUE_NORMALIZATION.get(original.casefold(), original)
    evidence = find_first_evidence(text, [re.escape(original), re.escape(normalized)], min_line=10) if original else None
    issues: list[dict[str, Any]] = []
    if evidence:
        source_locator, snippet, _ = evidence
    else:
        source_locator = f"Task table: 我方Marker文章 row {row.get('分工表行号')}"
        snippet = f"表中组织：{original}"
        issues.append({
            "issue_type": "tissue_source_not_located_in_markdown",
            "severity": "warning",
            "field": "tissue_sources",
            "description": "组织来源使用任务表预填值，尚未在 Markdown 中定位到原文证据。",
            "source_locator": source_locator,
            "evidence_snippet": snippet,
        })
    return ([{
        "tissue_source_original": original,
        "tissue_source_normalized": normalized,
        "sample_context": sample_context(text_value(row.get("论文标题")), article_body(text)),
        "species": text_value(row.get("物种")),
        "single_cell_type": text_value(row.get("技术")),
        "source_locator": source_locator,
        "evidence_snippet": snippet,
    }] if original else []), issues


def extract_neural(row: dict[str, Any], text: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    task_levels = text_value(row.get("PNS层级"))
    task_names = [re.sub(r"^L[1-4]:", "", name).strip() for name in split_terms(task_levels.split(":", 1)[-1] if ":" in task_levels else task_levels)]
    candidates: list[tuple[str, tuple[str, ...]]] = []
    for name in task_names:
        matched_alias = next((aliases for key, aliases in NEURAL_ALIASES.items() if key.casefold() in name.casefold()), (name,))
        candidates.append((name, matched_alias))
    for canonical, aliases in NEURAL_ALIASES.items():
        if any(re.search(re.escape(alias), text, re.IGNORECASE) for alias in aliases):
            candidates.append((canonical, aliases))
    seen: set[str] = set()
    cells: list[dict[str, Any]] = []
    issues: list[dict[str, Any]] = []
    for name, aliases in candidates:
        key = name.casefold()
        if key in seen:
            continue
        seen.add(key)
        evidence = find_first_evidence(text, [re.escape(alias) for alias in aliases])
        if not evidence:
            issues.append({
                "issue_type": "task_neural_cell_not_located",
                "severity": "warning",
                "field": "neural_cells",
                "description": f"任务表标注的神经相关细胞未在 Markdown 中直接定位：{name}",
                "source_locator": f"Task table: 我方Marker文章 row {row.get('分工表行号')}",
                "evidence_snippet": name,
            })
            continue
        source_locator, snippet, heading = evidence
        context = nearest_context(heading, snippet)
        cells.append({
            "cell_name_original": name,
            "cell_name_normalized": name,
            "cell_category": cell_category(name),
            "pns_level": pns_level(name, task_levels),
            "tissue": text_value(row.get("组织")),
            "evidence_context": context,
            "source_locator": source_locator,
            "evidence_snippet": snippet,
            "review_status": "discussion_only" if context == "discussion_only" else "pending",
        })
    return cells, issues


def extract_statistics(text: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    methods: list[dict[str, Any]] = []
    issues: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    found_stages: set[str] = set()
    for stage, patterns in STAT_METHODS.items():
        evidence = find_first_evidence(text, [re.escape(pattern) for pattern in patterns])
        if not evidence:
            if stage in {"quality_control", "normalization_integration", "dimension_reduction_clustering", "differential_expression", "multiple_testing"}:
                issues.append({
                    "issue_type": "statistical_method_not_reported_or_not_located",
                    "severity": "info",
                    "field": "statistics_methods",
                    "description": f"未在 Markdown 中定位到单细胞分析阶段：{stage}",
                    "source_locator": "",
                    "evidence_snippet": "",
                })
            continue
        source_locator, snippet, _ = evidence
        method_name = next((pattern for pattern in patterns if re.search(re.escape(pattern), snippet, re.IGNORECASE)), patterns[0])
        key = (stage, method_name.casefold())
        if key in seen:
            continue
        seen.add(key)
        found_stages.add(stage)
        version_match = re.search(r"(?:Seurat|Scanpy|Harmony|Monocle|scVelo|CellPhoneDB|SCENIC|Cell Ranger)\s*(?:v|version\s*)?([0-9]+(?:\.[0-9]+)*)", snippet, re.IGNORECASE)
        threshold_match = re.search(r"(?:FDR|adjusted p|q[- ]value|p[- ]value|cutoff|threshold)[^.;]{0,120}", snippet, re.IGNORECASE)
        methods.append({
            "analysis_stage": stage,
            "method_original": snippet[:300],
            "method_normalized": method_name,
            "software": method_name if stage == "software" else "",
            "software_version": version_match.group(1) if version_match else "",
            "threshold": threshold_match.group(0).strip() if threshold_match else "",
            "multiple_testing": snippet[:300] if stage == "multiple_testing" else "",
            "source_locator": source_locator,
            "evidence_snippet": snippet,
            "review_status": "pending",
        })
    return methods, issues


def marker_linkage(paper_id: str, marker_status: str) -> dict[str, Any]:
    raw_path = PROJECT_ROOT / "scripts" / "extract_markers" / "markers_output_v2" / f"{paper_id}_raw.json"
    review_path = PROJECT_ROOT / "scripts" / "extract_markers" / "markers_output_v2" / f"{paper_id}_review.csv"
    formal_count: int | None = None
    context_count: int | None = None
    if raw_path.exists():
        raw = load_json(raw_path)
        markers = [marker for cell_type in raw.get("cell_types", []) if isinstance(cell_type, dict) for marker in cell_type.get("markers", []) if isinstance(marker, dict)]
        formal_types = {"author_declared", "annotation_marker", "figure_labeled", "supplementary_marker"}
        formal_count = sum(marker.get("evidence_type") in formal_types for marker in markers)
        context_count = len(markers) - formal_count
    return {
        "marker_status": marker_status,
        "formal_candidate_count": formal_count,
        "context_only_count": context_count,
        "raw_json_file": str(raw_path.relative_to(PROJECT_ROOT)).replace("\\", "/") if raw_path.exists() else "",
        "review_csv_file": str(review_path.relative_to(PROJECT_ROOT)).replace("\\", "/") if review_path.exists() else "",
        "master_table_present": (PROJECT_ROOT / "db" / "cellxgene" / "our_markers.xlsx").exists(),
    }


def process_row(row: dict[str, Any]) -> dict[str, Any]:
    paper_id = text_value(row.get("paper_id"))
    markdown_path = MARKDOWN_DIR / text_value(row.get("markdown_file"))
    text = markdown_path.read_text(encoding="utf-8")
    body = article_body(text)
    tissue, tissue_issues = extract_tissue(row, body)
    cells, cell_issues = extract_neural(row, body)
    methods, stat_issues = extract_statistics(body)
    return {
        "schema_version": 1,
        "extraction_method": "deterministic_markdown_rules_v1",
        "paper_id": paper_id,
        "document_id": paper_id,
        "task_no": row.get("序号"),
        "source_markdown": text_value(row.get("markdown_file")),
        "article_identity": {
            "title_original": text_value(row.get("论文标题")),
            "doi": text_value(row.get("DOI")),
            "pmid": text_value(row.get("PMID")),
            "species": [text_value(row.get("物种"))] if text_value(row.get("物种")) else [],
        },
        "tissue_sources": tissue,
        "neural_cells": cells,
        "statistics_methods": methods,
        "marker_linkage": marker_linkage(paper_id, text_value(row.get("Marker状态"))),
        "issues": tissue_issues + cell_issues + stat_issues,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="确定性 Markdown 文章元数据提取")
    parser.add_argument("--pilot", action="store_true", help="只处理 5 篇试跑文章")
    parser.add_argument("--all", action="store_true", help="处理所有有 Markdown 的任务")
    parser.add_argument("--paper-id", action="append", help="指定 paper_id")
    parser.add_argument("--skip-existing", action="store_true", help="跳过已有结果")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    scope = load_json(SCOPE_PATH)
    rows = [row for row in scope.get("records", []) if isinstance(row, dict) and row.get("processing_status") == "matched"]
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
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    success = 0
    for row in rows:
        output_path = OUTPUT_DIR / f"{text_value(row.get('paper_id'))}_metadata.json"
        if args.skip_existing and output_path.exists():
            LOGGER.info("跳过已有结果: %s", output_path.name)
            success += 1
            continue
        output_path.write_text(json.dumps(process_row(row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        LOGGER.info("完成 %s", row.get("paper_id"))
        success += 1
    LOGGER.info("批处理完成: %d/%d", success, len(rows))


if __name__ == "__main__":
    main()
