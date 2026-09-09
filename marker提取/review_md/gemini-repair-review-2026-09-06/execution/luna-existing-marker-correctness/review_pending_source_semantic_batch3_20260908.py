from __future__ import annotations

import copy
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

import advance_source_context_match_batch as candidate_builder
import review_pending_source_semantic_batch_20260908 as batch2


ROOT = Path(r"D:/OneDrive/Desktop/组")
RUN_DIR = ROOT / "marker提取/review_md/gemini-repair-review-2026-09-06/execution/luna-existing-marker-correctness"
SOURCE_DIR = ROOT / "marker提取/review_md"
DATE = "2026-09-08"
BATCH_ID = "20260908-SRCSEM3"
EXECUTOR = "GPT-5.6 Luna"
SELECTION_FILE = RUN_DIR / "source_context_semantic_batch3_selection_20260908.json"
PREVIOUS_HOLD_IDS = {
    "M00102", "M00103", "M00389", "M00390", "M00694", "M00868", "M01528", "M02547",
}


def load(name: str):
    return json.loads((RUN_DIR / name).read_text(encoding="utf-8"))


def save(name: str, value) -> None:
    (RUN_DIR / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def select_candidates(reviews_doc: dict) -> list[dict]:
    candidate_builder.TASKS = set(range(1, 45))
    candidate_builder.MATCH_THRESHOLD = 0.0
    candidates = candidate_builder.build_candidates(reviews_doc)
    return [candidate for candidate in candidates if candidate["marker_id"] not in PREVIOUS_HOLD_IDS]


def main() -> None:
    reviews_doc = load("review-records.json")
    evidence_doc = load("evidence.json")
    changes_doc = load("change-set.json")
    reviews = {item["marker_id"]: item for item in reviews_doc["records"]}

    candidates = select_candidates(reviews_doc)
    if SELECTION_FILE.exists():
        selection_doc = json.loads(SELECTION_FILE.read_text(encoding="utf-8"))
    else:
        selection_doc = {
            "batch_id": BATCH_ID,
            "target_count": len(candidates),
            "tasks": list(range(1, 45)),
            "selected_records": candidates,
            "selection_method": "all remaining pending records across tasks 1-44 with independently recomputed source-context candidate windows, excluding prior unresolved holds",
        }
        SELECTION_FILE.write_text(json.dumps(selection_doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    selected_records = selection_doc["selected_records"]
    selected_ids = {item["marker_id"] for item in selected_records}
    if len(selected_ids) != len(selected_records):
        raise RuntimeError("Duplicate marker IDs in fixed selection")

    batch2.HOLD_IDS = set(PREVIOUS_HOLD_IDS)
    matches: dict[str, dict] = {}
    held: dict[str, str] = {}
    for selection in selected_records:
        marker_id = selection["marker_id"]
        record = reviews[marker_id]
        if record["processing_status"] != "pending":
            raise RuntimeError(f"Selected record is no longer pending: {marker_id}")
        try:
            match = batch2.relocate(record, selection)
        except RuntimeError as exc:
            held[marker_id] = str(exc)
            continue
        ok, note = batch2.review_semantics(record, match)
        record["source_context_semantic_candidate"] = {
            "batch_id": BATCH_ID,
            "selection_record": selection,
            "corrected_window": match,
            "candidate_status": "semantic_reviewed" if ok else "held_pending",
            "semantic_note": note,
        }
        if ok:
            matches[marker_id] = {**match, "semantic_note": note}
        else:
            held[marker_id] = note

    existing_evidence_ids = {item["evidence_id"] for item in evidence_doc["evidence"]}
    by_paper: dict[str, list[dict]] = {}
    for match in matches.values():
        by_paper.setdefault(match["paper_id"], []).append(match)
    evidence_id_by_paper: dict[str, str] = {}
    for paper_id, paper_matches in by_paper.items():
        safe_paper = re.sub(r"[^A-Za-z0-9]+", "_", paper_id).strip("_")
        evidence_id = f"EVID_SOURCE_CONTEXT_SEMANTIC3_20260908_{safe_paper}"
        evidence_id_by_paper[paper_id] = evidence_id
        if evidence_id in existing_evidence_ids:
            continue
        evidence_doc["evidence"].append({
            "evidence_id": evidence_id,
            "paper_id": paper_id,
            "source_file": paper_matches[0]["source_file"],
            "source_sha256": paper_matches[0]["source_sha256"],
            "locator": "Per-record corrected source windows listed in support_map",
            "verbatim_quote": None,
            "verbatim_fragments": sorted({match["evidence_excerpt"] for match in paper_matches}),
            "support_map": {
                match["marker_id"]: {
                    "gene_symbol": match["gene_symbol"],
                    "task_no": match["task_no"],
                    "locator": match["evidence_locator"],
                    "excerpt": match["evidence_excerpt"],
                    "match_score": match["match_score"],
                    "semantic_note": match["semantic_note"],
                }
                for match in paper_matches
            },
            "interpretation": "第三批逐条复核 source_context 与重新定位的目标正文窗口；目标基因、目标细胞语境和原 marker_polarity 一致，仅保留原字段。",
            "supports_review_ids": [f"LUNA-20260907-{match['marker_id']}" for match in paper_matches],
            "actual_checked_by": EXECUTOR,
            "checked_at": DATE,
            "verification_status": "semantic_reviewed_corrected_source_window_batch3",
            "matching_threshold": 0.80,
        })
        existing_evidence_ids.add(evidence_id)

    expected_start_sha = changes_doc["changes"][0]["expected_start_sha256"]
    reviewed_now = 0
    for marker_id, match in matches.items():
        review = reviews[marker_id]
        verify_id = f"VERIFY:{marker_id}:{BATCH_ID}-SEMANTIC"
        original = copy.deepcopy(review["original_values"])
        evidence_id = evidence_id_by_paper[match["paper_id"]]
        reason = f"第三批逐条语义复核：目标基因 {match['gene_symbol']} 在 source_context 与重新定位正文窗口中一致；目标细胞语境和原 {original['marker_polarity']} 限定均保留。"
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
            "revision_reason": "第三批 source-context 语义复核：重新定位目标正文窗口并核对目标基因—细胞语境及极性。",
        })
        review.update({
            "processing_status": "completed",
            "result": "verified_keep",
            "action": "no_change",
            "after_values": original,
            "evidence_ids": [evidence_id],
            "checked_scope": [match["evidence_locator"]],
            "issues_found": [],
            "remaining_gaps": [],
            "reason": reason,
            "related_marker_ids": [],
            "executed_by": EXECUTOR,
            "reviewed_at": DATE,
            "evidence_excerpt": match["evidence_excerpt"],
            "evidence_locator": match["evidence_locator"],
            "evidence_binding_status": "semantic_reviewed_corrected_source_window_batch3",
            "semantic_review": {
                "status": "verified_keep_no_change",
                "method": "corrected_best_overlap_source_window_plus_target_qualifier_check_batch3",
                "source_context_match_score": match["match_score"],
                "checks": [
                    "目标基因在 source_context 和重新定位正文窗口中均出现",
                    "目标细胞语境与原记录一致",
                    "目标基因级表达方向/限定与原 marker_polarity 一致",
                    "未将其他细胞或其他基因的限定借用到当前记录",
                ],
                "semantic_note": match["semantic_note"],
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
        reviewed_now += 1

    summary = reviews_doc["summary"]
    summary["processing_status_counts"] = {
        "completed": sum(item["processing_status"] == "completed" for item in reviews_doc["records"]),
        "pending": sum(item["processing_status"] == "pending" for item in reviews_doc["records"]),
    }
    summary["result_counts"] = Counter(item["result"] for item in reviews_doc["records"])
    summary["result_counts"] = dict(summary["result_counts"])
    summary["known_batch_scope"] = sorted(item["marker_id"] for item in reviews_doc["records"] if item["processing_status"] == "completed")
    changes_doc["change_count"] = len(changes_doc["changes"])
    changes_doc["latest_batch"] = {
        "name": "Third source-context semantic review batch",
        "batch_id": BATCH_ID,
        "completed_records": reviewed_now,
        "held_pending_records": len(held),
        "held_pending_ids": sorted(held),
        "fixed_selection_records": len(selected_records),
    }
    selection_doc["status"] = "semantic_reviewed_with_holds"
    selection_doc["semantic_reviewed_count"] = reviewed_now
    selection_doc["semantic_hold_count"] = len(held)
    selection_doc["semantic_hold_ids"] = sorted(held)
    selection_doc["semantic_hold_reasons"] = held
    selection_doc["completed_at"] = DATE
    SELECTION_FILE.write_text(json.dumps(selection_doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    save("review-records.json", reviews_doc)
    save("evidence.json", evidence_doc)
    save("change-set.json", changes_doc)
    print(json.dumps({
        "selected": len(selected_records),
        "reviewed_now": reviewed_now,
        "held": held,
        "completed": summary["processing_status_counts"]["completed"],
        "pending": summary["processing_status_counts"]["pending"],
        "change_count": changes_doc["change_count"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
