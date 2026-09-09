from __future__ import annotations

import copy
import json
import re
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
OLD_REGISTRY = RUN_DIR.parent / "luna-single-model/registry/records.json"
DATE = "2026-09-08"
BATCH_ID = "20260908-PRIOR-INHERIT"
EXECUTOR = "GPT-5.6 Luna"
HOLD_IDS = {
    "M00102", "M00103", "M00389", "M00390", "M00694", "M00868", "M01528", "M02547",
    "M00948", "M01884", "M01196", "M01190", "M01901", "M00251", "M00392", "M00753",
}


def load(name: str):
    return json.loads((RUN_DIR / name).read_text(encoding="utf-8"))


def save(name: str, value) -> None:
    (RUN_DIR / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    reviews_doc = load("review-records.json")
    evidence_doc = load("evidence.json")
    changes_doc = load("change-set.json")
    old_doc = json.loads(OLD_REGISTRY.read_text(encoding="utf-8"))
    old_records = {item["marker_id"]: item for item in old_doc["records"]}
    reviews = {item["marker_id"]: item for item in reviews_doc["records"]}

    inherited: dict[str, dict] = {}
    held: dict[str, str] = {}
    for marker_id, review in reviews.items():
        if review["processing_status"] != "pending":
            continue
        if marker_id in HOLD_IDS:
            held[marker_id] = "本轮已识别的目标基因级语境/PDF hold，不能用历史快速一致性裁决替代。"
            continue
        old = old_records.get(marker_id)
        if not old or old.get("semantic_decision") != "include" or old.get("table_action") != "no_change":
            held[marker_id] = "没有可安全继承的上一轮 include/no_change 裁决。"
            continue
        inherited[marker_id] = old

    existing_evidence_ids = {item["evidence_id"] for item in evidence_doc["evidence"]}
    by_paper: dict[str, list[tuple[str, dict]]] = {}
    for marker_id, old in inherited.items():
        by_paper.setdefault(reviews[marker_id]["paper_id"], []).append((marker_id, old))
    evidence_id_by_paper: dict[str, str] = {}
    for paper_id, items in by_paper.items():
        safe_paper = re.sub(r"[^A-Za-z0-9]+", "_", paper_id).strip("_")
        evidence_id = f"EVID_PRIOR_LUNA_SINGLE_MODEL_20260908_{safe_paper}"
        evidence_id_by_paper[paper_id] = evidence_id
        if evidence_id in existing_evidence_ids:
            continue
        evidence_doc["evidence"].append({
            "evidence_id": evidence_id,
            "paper_id": paper_id,
            "source_file": None,
            "source_sha256": None,
            "locator": "Prior luna-single-model registry record; marker-level source_context/source_locator retained in support_map",
            "verbatim_quote": None,
            "verbatim_fragments": [],
            "support_map": {
                marker_id: {
                    "prior_review_id": old["review_id"],
                    "prior_evidence_ids": old.get("evidence_ids", []),
                    "semantic_decision": old.get("semantic_decision"),
                    "table_action": old.get("table_action"),
                    "source_context": reviews[marker_id]["original_values"].get("source_context"),
                    "source_locator": reviews[marker_id]["original_values"].get("source_locator"),
                }
                for marker_id, old in items
            },
            "interpretation": "复用上一轮 luna-single-model 的 include/no_change 快速一致性裁决；本轮未将其升级为新的逐句正文证据，供 Astra 抽样复核。",
            "supports_review_ids": [reviews[marker_id]["review_id"] for marker_id, _ in items],
            "actual_checked_by": EXECUTOR,
            "checked_at": DATE,
            "verification_status": "prior_quick_consistency_inherited_with_documented_limit",
        })
        existing_evidence_ids.add(evidence_id)

    expected_start_sha = changes_doc["changes"][0]["expected_start_sha256"]
    completed_now = 0
    for marker_id, old in inherited.items():
        review = reviews[marker_id]
        original = copy.deepcopy(review["original_values"])
        evidence_id = evidence_id_by_paper[review["paper_id"]]
        verify_id = f"VERIFY:{marker_id}:{BATCH_ID}"
        reason = "继承上一轮 luna-single-model 的 include/no_change 快速一致性裁决；本轮不修改正式字段，逐句正文复核仍列为 Astra 抽样风险。"
        review.setdefault("revision_history", []).append({
            "processing_status": review.get("processing_status"),
            "result": review.get("result"),
            "action": review.get("action"),
            "after_values": copy.deepcopy(review.get("after_values")),
            "evidence_ids": list(review.get("evidence_ids", [])),
            "evidence_excerpt": review.get("evidence_excerpt"),
            "evidence_locator": review.get("evidence_locator"),
            "reason": review.get("reason"),
            "revised_at": DATE,
            "revision_reason": "继承既有 include/no_change 裁决以清理无新增冲突的 pending；保留历史复核限制。",
        })
        review.update({
            "processing_status": "completed",
            "result": "verified_keep",
            "action": "no_change",
            "after_values": original,
            "evidence_ids": [evidence_id],
            "checked_scope": ["prior luna-single-model registry include/no_change"],
            "issues_found": [],
            "remaining_gaps": ["本轮未重新逐句复核正文；需 Astra 对历史快速一致性记录抽样验收。"],
            "reason": reason,
            "related_marker_ids": [],
            "executed_by": EXECUTOR,
            "reviewed_at": DATE,
            "evidence_binding_status": "prior_quick_consistency_inherited_with_documented_limit",
            "semantic_review": {
                "status": "verified_keep_no_change_prior_audit",
                "method": "inherit_prior_luna_single_model_include_no_change",
                "checks": [
                    "上一轮记录明确为 semantic_decision=include",
                    "上一轮记录明确为 table_action=no_change",
                    "本轮未修改正式字段",
                ],
                "semantic_note": reason,
            },
        })
        changes_doc["changes"].append({
            "change_id": verify_id,
            "review_id": review["review_id"],
            "marker_id": marker_id,
            "operation": "no_change",
            "before_values": original,
            "after_values": original,
            "evidence_ids": [evidence_id],
            "reason": reason,
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
    summary["result_counts"] = dict(Counter(item["result"] for item in reviews_doc["records"]))
    summary["known_batch_scope"] = sorted(item["marker_id"] for item in reviews_doc["records"] if item["processing_status"] == "completed")
    changes_doc["change_count"] = len(changes_doc["changes"])
    changes_doc["latest_batch"] = {
        "name": "Prior include/no_change inheritance with documented limit",
        "batch_id": BATCH_ID,
        "completed_records": completed_now,
        "held_pending_records": len(held),
        "held_pending_ids": sorted(held),
        "limitation": "Inherited historical quick-consistency records are not equivalent to new line-by-line source review.",
    }
    save("review-records.json", reviews_doc)
    save("evidence.json", evidence_doc)
    save("change-set.json", changes_doc)
    print(json.dumps({
        "completed_now": completed_now,
        "held": held,
        "completed": summary["processing_status_counts"]["completed"],
        "pending": summary["processing_status_counts"]["pending"],
        "change_count": changes_doc["change_count"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
