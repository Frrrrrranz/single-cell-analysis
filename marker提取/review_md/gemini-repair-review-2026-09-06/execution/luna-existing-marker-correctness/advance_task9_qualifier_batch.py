from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(r"D:/OneDrive/Desktop/组")
RUN_DIR = ROOT / "marker提取/review_md/gemini-repair-review-2026-09-06/execution/luna-existing-marker-correctness"
SOURCE = ROOT / "marker提取/review_md/DOI_10.1016_j.cell.2022.11.005.md"
EXECUTOR = "GPT-5.6 Luna"
DATE = "2026-09-07"

TARGETS = {
    "M00493": ("UCP2LO", "Results, lines 313-315", "淋巴内皮细胞条件明确为 UCP2LO；兼容编码改为 low。"),
    "M00495": ("FGFR4LO", "Results, lines 382-385", "中期成纤维细胞条件明确为 FGFR4LO；兼容编码改为 low。"),
    "M00498": ("MUC16LO", "Results, lines 171-173", "MUC16+纤毛细胞条件明确为 MUC16LO；兼容编码改为 low。"),
    "M00508": ("THBDLO", "Results, lines 377-380", "肌成纤维细胞1条件明确为 THBDLO；兼容编码改为 low。"),
    "M00534": ("SCGB1A1LO", "Results, lines 196-198", "proximal secretory 1 条件明确为 SCGB1A1LO；兼容编码改为 low。"),
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
    evidence_id = "EVID_CELL_TASK9_TARGET_LOW_QUALIFIERS"
    source_hash = sha256(SOURCE)
    support_map = {marker_id: {"locator": locator, "excerpt": excerpt} for marker_id, (excerpt, locator, _) in TARGETS.items()}
    if not any(item["evidence_id"] == evidence_id for item in evidence_doc["evidence"]):
        evidence_doc["evidence"].append({
            "evidence_id": evidence_id,
            "paper_id": "DOI_10.1016_j.cell.2022.11.005",
            "source_file": "marker提取/review_md/DOI_10.1016_j.cell.2022.11.005.md",
            "source_sha256": source_hash,
            "locator": "Results lines 171-173, 196-198, 313-315, 377-380, 382-385",
            "verbatim_quote": None,
            "verbatim_fragments": [item[0] for item in TARGETS.values()],
            "support_map": support_map,
            "interpretation": "目标基因分别带有 LO 限定；不能用同一细胞定义中的其他阳性基因覆盖该表达强度。",
            "supports_review_ids": [f"LUNA-20260907-{marker_id}" for marker_id in TARGETS],
            "actual_checked_by": EXECUTOR,
            "checked_at": DATE,
            "verification_status": "current_source_checked_per_record",
        })

    for marker_id, (excerpt, locator, reason) in TARGETS.items():
        review = reviews[marker_id]
        previous = {
            "processing_status": review.get("processing_status"),
            "result": review.get("result"),
            "action": review.get("action"),
            "after_values": copy.deepcopy(review.get("after_values")),
            "evidence_ids": list(review.get("evidence_ids", [])),
            "reason": review.get("reason"),
            "revised_at": DATE,
            "revision_reason": "继续筛查 task 9 时发现目标基因本身带有 LO 限定，按 Astra 规范逐条修正。",
        }
        history = review.setdefault("revision_history", [])
        if not any(item.get("revision_reason") == previous["revision_reason"] and item.get("revised_at") == DATE for item in history):
            history.append(previous)
        original = review["original_values"]
        after = copy.deepcopy(original)
        after["marker_polarity"] = "low"
        after["notes"] = f"{original.get('notes') or ''} {reason}".strip()
        review.update({
            "processing_status": "completed",
            "result": "verified_correct",
            "action": "update",
            "after_values": after,
            "evidence_ids": [evidence_id],
            "checked_scope": [locator],
            "issues_found": ["原始上下文中目标基因含 LO 限定，不能无条件记为 positive"],
            "remaining_gaps": [],
            "reason": reason,
            "related_marker_ids": [],
            "executed_by": EXECUTOR,
            "reviewed_at": DATE,
            "evidence_excerpt": excerpt,
            "evidence_locator": locator,
            "evidence_binding_status": "per_record_source_fragment_checked",
        })
        prior = next((item for item in reversed(changes_doc["changes"]) if item.get("marker_id") == marker_id and not item.get("superseded_by")), None)
        reopen_id = f"REOPEN:{marker_id}:20260907"
        update_id = f"UPDATE:{marker_id}:20260907-R1"
        if prior:
            prior["superseded_by"] = update_id
            prior["status"] = "superseded_by_revision"
        if not any(item.get("change_id") == reopen_id for item in changes_doc["changes"]):
            changes_doc["changes"].append({
                "change_id": reopen_id,
                "review_id": review["review_id"],
                "marker_id": marker_id,
                "operation": "reopen_pending",
                "before_values": previous["after_values"],
                "after_values": original,
                "evidence_ids": [],
                "reason": "目标基因级表达限定补核。",
                "target_marker_id": None,
                "archive_destination": None,
                "executor": EXECUTOR,
                "decided_at": DATE,
                "expected_start_sha256": expected_start_sha,
                "supersedes": prior["change_id"] if prior else None,
            })
        if not any(item.get("change_id") == update_id for item in changes_doc["changes"]):
            changes_doc["changes"].append({
                "change_id": update_id,
                "review_id": review["review_id"],
                "marker_id": marker_id,
                "operation": "update",
                "before_values": original,
                "after_values": after,
                "evidence_ids": [evidence_id],
                "reason": reason,
                "target_marker_id": None,
                "archive_destination": None,
                "executor": EXECUTOR,
                "decided_at": DATE,
                "expected_start_sha256": expected_start_sha,
                "supersedes": reopen_id,
            })

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
        "name": "CELL task 9 target-level LO qualifier batch",
        "completed_records": len(TARGETS),
        "updated_records": len(TARGETS),
        "kept_records": 0,
    }
    save("review-records.json", reviews_doc)
    save("evidence.json", evidence_doc)
    save("change-set.json", changes_doc)


if __name__ == "__main__":
    main()
