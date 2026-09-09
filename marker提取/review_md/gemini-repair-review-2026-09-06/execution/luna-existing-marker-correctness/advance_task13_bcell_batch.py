from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(r"D:/OneDrive/Desktop/组")
RUN_DIR = ROOT / "marker提取/review_md/gemini-repair-review-2026-09-06/execution/luna-existing-marker-correctness"
SOURCE = ROOT / "marker提取/review_md/DOI_10.1126_sciimmunol.adf9988.md"
EXECUTOR = "GPT-5.6 Luna"
DATE = "2026-09-08"
EVIDENCE_ID = "EVID_SCIIMMUNOLOGY_TASK13_BCELL_POSITIVE_DEFINITIONS"

TARGETS = {
    "M00632": ("SOX2", "to become SOX9-/SOX2+ airway progenitors", "Results, lines 1197-1200"),
    "M00634": ("CD5", "CD5- versus CD5+ mature B cells", "Results, lines 724-725"),
    "M00635": ("IGHM", "immature B (MS4A1+IGHDloIGHMhiVPREB3hi)", "Results, lines 716-724"),
    "M00636": ("IGLL1", "MS4A1+ late pre-B cells that expressed the marker for surrogate light chain, IGLL1", "Results, lines 724-725"),
    "M00638": ("NEIL1", "NEIL1+MKI67- late pro-B cells", "Results, lines 724-725"),
    "M00639": ("EBF1", "pre-pro-B (EBF1+SPINK2+VPREB1+)", "Results, lines 716-724"),
    "M00640": ("IL7R", "acquisition of B cell markers such as IL7R at the pre-pro-B cell stage", "Results, lines 727-731"),
    "M00641": ("SPINK2", "pre-pro-B (EBF1+SPINK2+VPREB1+)", "Results, lines 716-724"),
    "M00642": ("VPREB1", "pre-pro-B (EBF1+SPINK2+VPREB1+)", "Results, lines 716-724"),
    "M00643": ("DNTT", "pro-B (DNTT+)", "Results, lines 716-724"),
    "M00644": ("MS4A1", "RAG1+MS4A1+ pro-B/pre-B transition cells", "Results, lines 724-725"),
    "M00645": ("RAG1", "RAG1+MS4A1+ pro-B/pre-B transition cells", "Results, lines 724-725"),
    "M00646": ("BEST3", "RAG1+BEST3+ small pre-B cells", "Results, lines 748-750"),
    "M00647": ("SPIB", "small pre-B (IL7R+SPIB+MKI67-)", "Results, lines 716-724"),
    "M00648": ("IGKC", "immunoglobulin kappa (IGKC+)", "Results, lines 724-725"),
    "M00649": ("IGLC2", "lambda (IGLC2+IGLC3+) light chain genes", "Results, lines 724-725"),
    "M00650": ("IGLC3", "lambda (IGLC2+IGLC3+) light chain genes", "Results, lines 724-725"),
    "M00651": ("CCL22", "CD5, CD27, SPN (CD43), CCR10 and CCL22", "Results, lines 842-844"),
    "M00652": ("CCR10", "CD5, CD27, SPN (CD43), CCR10 and CCL22", "Results, lines 842-844"),
    "M00653": ("CD27", "CD5, CD27, SPN (CD43), CCR10 and CCL22", "Results, lines 842-844"),
    "M00655": ("SPN", "CD5, CD27, SPN (CD43), CCR10 and CCL22", "Results, lines 842-844"),
}


def load(name: str):
    return json.loads((RUN_DIR / name).read_text(encoding="utf-8"))


def save(name: str, value) -> None:
    (RUN_DIR / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    reviews_doc = load("review-records.json")
    evidence_doc = load("evidence.json")
    changes_doc = load("change-set.json")
    reviews = {item["marker_id"]: item for item in reviews_doc["records"]}
    expected_start_sha = changes_doc["changes"][0]["expected_start_sha256"]
    support_map = {
        marker_id: {"gene_symbol": gene, "locator": locator, "excerpt": excerpt}
        for marker_id, (gene, excerpt, locator) in TARGETS.items()
    }

    if not any(item["evidence_id"] == EVIDENCE_ID for item in evidence_doc["evidence"]):
        evidence_doc["evidence"].append({
            "evidence_id": EVIDENCE_ID,
            "paper_id": "DOI_10.1126_sciimmunol.adf9988",
            "source_file": "marker提取/review_md/DOI_10.1126_sciimmunol.adf9988.md",
            "source_sha256": sha256(SOURCE),
            "locator": "Results lines 716-725, 727-731, 748-750, 842-844, 1197-1200",
            "verbatim_quote": None,
            "verbatim_fragments": sorted({spec[1] for spec in TARGETS.values()}),
            "support_map": support_map,
            "interpretation": "原文直接给出目标基因的正向表达、细胞阶段定义或命名细胞 marker；保留原 positive 极性。",
            "supports_review_ids": [f"LUNA-20260907-{marker_id}" for marker_id in TARGETS],
            "actual_checked_by": EXECUTOR,
            "checked_at": DATE,
            "verification_status": "current_source_checked_per_record",
        })

    completed_now = 0
    for marker_id, (gene, excerpt, locator) in TARGETS.items():
        review = reviews[marker_id]
        change_id = f"VERIFY:{marker_id}:{DATE}"
        if any(item.get("change_id") == change_id for item in changes_doc["changes"]):
            continue
        original = copy.deepcopy(review["original_values"])
        review.setdefault("revision_history", []).append({
            "processing_status": review.get("processing_status"),
            "result": review.get("result"),
            "action": review.get("action"),
            "after_values": copy.deepcopy(review.get("after_values")),
            "evidence_ids": list(review.get("evidence_ids", [])),
            "reason": review.get("reason"),
            "revised_at": DATE,
            "revision_reason": "完成 task 13 B 细胞发育与气道 progenitor 正向定义核验。",
        })
        review.update({
            "processing_status": "completed",
            "result": "verified_keep",
            "action": "no_change",
            "after_values": original,
            "evidence_ids": [EVIDENCE_ID],
            "checked_scope": [locator],
            "issues_found": [],
            "remaining_gaps": [],
            "reason": f"原文片段直接包含目标基因 {gene} 的正向表达或细胞定义，保留原字段。",
            "related_marker_ids": [],
            "executed_by": EXECUTOR,
            "reviewed_at": DATE,
            "evidence_excerpt": excerpt,
            "evidence_locator": locator,
            "evidence_binding_status": "per_record_source_fragment_checked",
        })
        changes_doc["changes"].append({
            "change_id": change_id,
            "review_id": review["review_id"],
            "marker_id": marker_id,
            "operation": "no_change",
            "before_values": original,
            "after_values": original,
            "evidence_ids": [EVIDENCE_ID],
            "reason": f"原文片段直接包含目标基因 {gene} 的正向表达或细胞定义，保留原字段。",
            "target_marker_id": None,
            "archive_destination": None,
            "executor": EXECUTOR,
            "decided_at": DATE,
            "expected_start_sha256": expected_start_sha,
        })
        completed_now += 1

    summary = reviews_doc["summary"]
    summary["processing_status_counts"] = {
        "completed": sum(item["processing_status"] == "completed" for item in reviews_doc["records"]),
        "pending": sum(item["processing_status"] == "pending" for item in reviews_doc["records"]),
    }
    summary["result_counts"] = {}
    summary["known_batch_scope"] = []
    for item in reviews_doc["records"]:
        summary["result_counts"][item["result"]] = summary["result_counts"].get(item["result"], 0) + 1
        if item["processing_status"] == "completed":
            summary["known_batch_scope"].append(item["marker_id"])
    summary["known_batch_scope"].sort()
    changes_doc["change_count"] = len(changes_doc["changes"])
    changes_doc["latest_batch"] = {
        "name": "Sci Immunology task 13 B-cell and airway positive-definition batch",
        "completed_records": completed_now,
        "updated_records": 0,
        "kept_records": completed_now,
    }
    save("review-records.json", reviews_doc)
    save("evidence.json", evidence_doc)
    save("change-set.json", changes_doc)


if __name__ == "__main__":
    main()
