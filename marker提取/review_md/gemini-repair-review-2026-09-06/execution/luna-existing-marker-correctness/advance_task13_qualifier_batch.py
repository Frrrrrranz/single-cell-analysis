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
EVIDENCE_ID = "EVID_SCIIMMUNOLOGY_TASK13_TARGET_NEGATIVE_LOW"

TARGETS = {
    "M00633": {
        "excerpt": "SOX9-/SOX2+ airway progenitors",
        "locator": "Results, lines 1197-1200",
        "polarity": "negative",
        "reason": "原文将 airway progenitors 定义为 SOX9-/SOX2+，因此 SOX9 为目标级阴性。",
    },
    "M00637": {
        "excerpt": "NEIL1+MKI67- late pro-B cells",
        "locator": "Results, lines 716-724",
        "polarity": "negative",
        "reason": "原文将 late pro-B 细胞写为 NEIL1+MKI67-，因此 MKI67 为目标级阴性。",
    },
    "M00680": {
        "excerpt": "LMPP/ELP (CD34+EBF1-)",
        "locator": "Results, lines 716-724",
        "polarity": "negative",
        "reason": "原文将 LMPP/ELP 写为 CD34+EBF1-，因此 EBF1 为目标级阴性。",
    },
    "M02359": {
        "excerpt": "small pre-B (IL7R+SPIB+MKI67-)",
        "locator": "Results, lines 716-724",
        "polarity": "negative",
        "reason": "原文将 small pre-B 细胞写为 IL7R+SPIB+MKI67-，因此 MKI67 为目标级阴性。",
    },
    "M02364": {
        "excerpt": "small pre-B (IL7R+SPIB+MKI67-)",
        "locator": "Results, lines 716-724",
        "polarity": "negative",
        "reason": "原文将 small pre-B 细胞写为 IL7R+SPIB+MKI67-，因此 MKI67 为目标级阴性。",
    },
    "M02369": {
        "excerpt": "immature B (MS4A1+IGHDloIGHMhiVPREB3hi)",
        "locator": "Results, lines 716-724",
        "polarity": "low",
        "reason": "原文将 immature B 细胞写为 MS4A1+IGHDloIGHMhiVPREB3hi，IGHD 为目标级低表达。",
    },
    "M02374": {
        "excerpt": "mature B (MS4A1+IGHDhiIGHMhiVPREB3lo)",
        "locator": "Results, lines 716-724",
        "polarity": "low",
        "reason": "原文将 mature B 细胞写为 MS4A1+IGHDhiIGHMhiVPREB3lo，VPREB3 为目标级低表达。",
    },
    "M02375": {
        "excerpt": "CD5- versus CD5+ mature B cells",
        "locator": "Results, lines 724-725",
        "polarity": "negative",
        "reason": "原文明确区分 CD5- 与 CD5+ mature B cells，因此 CD5- 记录为目标级阴性。",
    },
    "M02376": {
        "excerpt": "Absence of the expression of the transcription factor PRDM1 (Fig 3C) confirmed that our dataset",
        "locator": "Results, lines 838-840",
        "polarity": "negative",
        "reason": "原文明确指出缺少转录因子 PRDM1，因此 PRDM1 为目标级阴性。",
    },
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
        marker_id: {"locator": spec["locator"], "excerpt": spec["excerpt"]}
        for marker_id, spec in TARGETS.items()
    }
    if not any(item["evidence_id"] == EVIDENCE_ID for item in evidence_doc["evidence"]):
        evidence_doc["evidence"].append({
            "evidence_id": EVIDENCE_ID,
            "paper_id": "DOI_10.1126_sciimmunol.adf9988",
            "source_file": "marker提取/review_md/DOI_10.1126_sciimmunol.adf9988.md",
            "source_sha256": sha256(SOURCE),
            "locator": "Results lines 716-725, 838-840, 1197-1200",
            "verbatim_quote": None,
            "verbatim_fragments": [spec["excerpt"] for spec in TARGETS.values()],
            "support_map": support_map,
            "interpretation": "目标基因级的负向、低表达和同一细胞定义中的限定必须逐条保留，不能被其他阳性标记覆盖。",
            "supports_review_ids": [f"LUNA-20260907-{marker_id}" for marker_id in TARGETS],
            "actual_checked_by": EXECUTOR,
            "checked_at": DATE,
            "verification_status": "current_source_checked_per_record",
        })

    updated = 0
    for marker_id, spec in TARGETS.items():
        review = reviews[marker_id]
        update_id = f"UPDATE:{marker_id}:{DATE}"
        if any(item.get("change_id") == update_id for item in changes_doc["changes"]):
            continue

        original = copy.deepcopy(review["original_values"])
        previous = {
            "processing_status": review.get("processing_status"),
            "result": review.get("result"),
            "action": review.get("action"),
            "after_values": copy.deepcopy(review.get("after_values")),
            "evidence_ids": list(review.get("evidence_ids", [])),
            "reason": review.get("reason"),
            "revised_at": DATE,
            "revision_reason": "完成 task 13 原文核验并补充目标基因级负向/低表达限定。",
        }
        review.setdefault("revision_history", []).append(previous)
        after = copy.deepcopy(original)
        after["marker_polarity"] = spec["polarity"]
        after["notes"] = f"{original.get('notes') or ''} {spec['reason']}".strip()
        review.update({
            "processing_status": "completed",
            "result": "verified_correct",
            "action": "update",
            "after_values": after,
            "evidence_ids": [EVIDENCE_ID],
            "checked_scope": [spec["locator"]],
            "issues_found": ["原始记录尚未完成本轮核验；原文现已确认目标基因级负向或低表达限定。"],
            "remaining_gaps": [],
            "reason": spec["reason"],
            "related_marker_ids": [],
            "executed_by": EXECUTOR,
            "reviewed_at": DATE,
            "evidence_excerpt": spec["excerpt"],
            "evidence_locator": spec["locator"],
            "evidence_binding_status": "per_record_source_fragment_checked",
        })
        changes_doc["changes"].append({
            "change_id": update_id,
            "review_id": review["review_id"],
            "marker_id": marker_id,
            "operation": "update",
            "before_values": original,
            "after_values": after,
            "evidence_ids": [EVIDENCE_ID],
            "reason": spec["reason"],
            "target_marker_id": None,
            "archive_destination": None,
            "executor": EXECUTOR,
            "decided_at": DATE,
            "expected_start_sha256": expected_start_sha,
        })
        updated += 1

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
        "name": "Sci Immunology task 13 target-level negative/low qualifier batch",
        "completed_records": updated,
        "updated_records": updated,
        "kept_records": 0,
    }
    save("review-records.json", reviews_doc)
    save("evidence.json", evidence_doc)
    save("change-set.json", changes_doc)


if __name__ == "__main__":
    main()
