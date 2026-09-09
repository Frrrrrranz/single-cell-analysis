from __future__ import annotations

import copy
import json
from pathlib import Path


RUN_DIR = Path(r"D:/OneDrive/Desktop/组/marker提取/review_md/gemini-repair-review-2026-09-06/execution/luna-existing-marker-correctness")
DATE = "2026-09-08"
BATCH_ID = "20260908-SRCCTX"
REVISION_SUFFIX = "ASTRA_CORRECTION"
SELECTION_FILE = RUN_DIR / "source_context_batch_selection_20260908.json"


def load(name: str):
    return json.loads((RUN_DIR / name).read_text(encoding="utf-8"))


def save(name: str, value) -> None:
    (RUN_DIR / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    reviews_doc = load("review-records.json")
    evidence_doc = load("evidence.json")
    changes_doc = load("change-set.json")
    selection_doc = json.loads(SELECTION_FILE.read_text(encoding="utf-8"))
    selected = selection_doc["selected_records"]
    selected_ids = [item["marker_id"] for item in selected]
    reviews = {item["marker_id"]: item for item in reviews_doc["records"]}
    changes_by_id = {item["change_id"]: item for item in changes_doc["changes"]}
    reopened = 0
    candidate_evidence_ids: set[str] = set()

    for selection in selected:
        marker_id = selection["marker_id"]
        review = reviews[marker_id]
        old_change_id = f"VERIFY:{marker_id}:2026-09-08-SRCCTX"
        reopen_id = f"REOPEN:{marker_id}:{DATE}-{REVISION_SUFFIX}"
        old_change = changes_by_id.get(old_change_id)
        if old_change is None:
            raise RuntimeError(f"Missing source-context change for {marker_id}")
        evidence_ids = list(old_change.get("evidence_ids", []))
        candidate_evidence_ids.update(evidence_ids)

        revision_reason = "Astra 2026-09-08：自动 source-context 匹配仅作为候选，回退到 pending。"
        if not any(item.get("revision_reason") == revision_reason for item in review.get("revision_history", [])):
            review.setdefault("revision_history", []).append({
                "processing_status": review.get("processing_status"),
                "result": review.get("result"),
                "action": review.get("action"),
                "after_values": copy.deepcopy(review.get("after_values")),
                "evidence_ids": list(review.get("evidence_ids", [])),
                "evidence_excerpt": review.get("evidence_excerpt"),
                "evidence_locator": review.get("evidence_locator"),
                "reason": review.get("reason"),
                "automated_candidate": {
                    "batch_id": BATCH_ID,
                    "evidence_ids": evidence_ids,
                    "selection_record": selection,
                },
                "revised_at": DATE,
                "revision_reason": revision_reason,
            })

        review["automated_source_context_candidate"] = {
            "batch_id": BATCH_ID,
            "selection_record": selection,
            "candidate_evidence_ids": evidence_ids,
            "candidate_status": "reverted_to_pending_for_semantic_review",
        }
        review.update({
            "processing_status": "pending",
            "result": "pending",
            "action": "pending",
            "after_values": None,
            "evidence_ids": [],
            "checked_scope": [],
            "issues_found": [],
            "remaining_gaps": ["自动 source-context 匹配只能定位候选证据，尚未完成目标基因—细胞关系、方向和条件的逐条语义核验。"],
            "reason": "Astra 2026-09-08：source-context 批次回退；保留候选匹配和旧版本链，等待逐条语义审核。",
            "related_marker_ids": [],
            "evidence_excerpt": None,
            "evidence_locator": None,
            "evidence_binding_status": "candidate_only_reverted_to_pending",
            "reviewed_at": None,
        })

        old_change["status"] = "superseded_by_revision"
        old_change["superseded_by"] = reopen_id
        old_change["revision_reason"] = "Astra 2026-09-08：自动 source-context 匹配不足以完成语义裁决。"
        if reopen_id not in changes_by_id:
            reopen_change = {
                "change_id": reopen_id,
                "review_id": review["review_id"],
                "marker_id": marker_id,
                "operation": "reopen_pending",
                "before_values": copy.deepcopy(old_change.get("after_values")),
                "after_values": None,
                "evidence_ids": [],
                "reason": "Astra 2026-09-08：自动 source-context 匹配只能作为候选，回退到 pending，待逐条核对目标基因—细胞关系、方向和条件。",
                "target_marker_id": None,
                "archive_destination": None,
                "executor": "GPT-5.6 Luna",
                "decided_at": DATE,
                "expected_start_sha256": old_change["expected_start_sha256"],
                "supersedes": old_change_id,
            }
            changes_doc["changes"].append(reopen_change)
            changes_by_id[reopen_id] = reopen_change
            reopened += 1
        else:
            reopened += 1

    for evidence in evidence_doc["evidence"]:
        if evidence["evidence_id"] in candidate_evidence_ids:
            evidence["candidate_only"] = True
            evidence["verification_status"] = "candidate_only_not_semantic_reviewed"
            evidence["reverted_at"] = DATE
            evidence["reverted_reason"] = "Astra 2026-09-08 source-window correction plan"
            evidence["retracted_from_completed_records"] = selected_ids

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

    selection_doc["status"] = "reverted_to_pending_for_semantic_review"
    selection_doc["reverted_at"] = DATE
    selection_doc["reverted_count"] = reopened
    SELECTION_FILE.write_text(json.dumps(selection_doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    changes_doc["change_count"] = len(changes_doc["changes"])
    changes_doc["latest_batch"] = {
        "name": "Astra source-window correction rollback",
        "completed_records": 0,
        "updated_records": 0,
        "kept_records": 0,
        "reopened_records": reopened,
        "candidate_records_preserved": len(selected),
        "remaining_eligible_records": selection_doc["remaining_eligible_count"],
    }
    save("review-records.json", reviews_doc)
    save("evidence.json", evidence_doc)
    save("change-set.json", changes_doc)


if __name__ == "__main__":
    main()
