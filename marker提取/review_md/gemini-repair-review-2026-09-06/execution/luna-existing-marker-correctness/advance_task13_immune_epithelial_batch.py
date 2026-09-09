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
EVIDENCE_ID = "EVID_SCIIMMUNOLOGY_TASK13_IMMUNE_EPITHELIAL_POSITIVE_DEFINITIONS"

TARGETS = {
    "M00666": ("SOX2", "Distal epithelial tip cells co-express SOX9 and SOX2", "Results, lines 1201-1202"),
    "M00667": ("SOX9", "distal epithelial tips are composed of SOX9+ progenitors", "Results, lines 1197-1198"),
    "M00671": ("SMIM24", "rare SMIM24+SPINK2+ cells, likely HSCs", "Results, lines 1079-1080"),
    "M00672": ("SPINK2", "rare SMIM24+SPINK2+ cells, likely HSCs", "Results, lines 1079-1080"),
    "M00673": ("HPN", "A cluster of ILCPs was identified by expression of marker genes (HPN and SCN1B", "Results, lines 956-957"),
    "M00674": ("SCN1B", "A cluster of ILCPs was identified by expression of marker genes (HPN and SCN1B", "Results, lines 956-957"),
    "M00676": ("CD14", "fetal MΦ populations express markers (CD14+ CD36+ MRC1+)", "Results, lines 1091-1092"),
    "M00677": ("CD36", "fetal MΦ populations express markers (CD14+ CD36+ MRC1+)", "Results, lines 1091-1092"),
    "M00678": ("MRC1", "fetal MΦ populations express markers (CD14+ CD36+ MRC1+)", "Results, lines 1091-1092"),
    "M00679": ("CD34", "LMPP/ELP (CD34+EBF1-)", "Results, lines 716-724"),
    "M00681": ("CD14", "CD14, a marker gene of classical monocytes and macrophages", "Results, lines 1086-1087"),
    "M00684": ("APOE", "CXCL2+ macrophages, APOE+ macrophages, macrophages", "Results, lines 991-993"),
    "M00685": ("CXCL2", "CXCL2+ macrophages, APOE+ macrophages, macrophages", "Results, lines 991-993"),
    "M00686": ("S100A12", "S100A12hi CD14+", "Results, lines 990-992"),
    "M00687": ("S100A12", "S100A12hi CD14+", "Results, lines 990-992"),
    "M00689": ("CD68", "Most myeloid cells, defined by their expression of CD68", "Results, lines 1084-1085"),
    "M00696": ("SOX9", "the SOX9+ tip progenitors", "Results, lines 1197-1198"),
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
            "locator": "Results lines 716-724, 956-957, 990-993, 1079-1087, 1091-1092, 1197-1202",
            "verbatim_quote": None,
            "verbatim_fragments": sorted({spec[1] for spec in TARGETS.values()}),
            "support_map": support_map,
            "interpretation": "原文直接给出目标基因作为免疫、造血或肺上皮细胞的 marker/定义成分；保留原 positive 极性。",
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
            "revision_reason": "完成 task 13 免疫、造血与上皮正向 marker 核验。",
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
        "name": "Sci Immunology task 13 immune/epithelial positive-definition batch",
        "completed_records": completed_now,
        "updated_records": 0,
        "kept_records": completed_now,
    }
    save("review-records.json", reviews_doc)
    save("evidence.json", evidence_doc)
    save("change-set.json", changes_doc)


if __name__ == "__main__":
    main()
