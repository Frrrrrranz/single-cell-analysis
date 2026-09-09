from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
SOURCE_PATH = RUN_DIR / "deferred-all-current.json"
REMAINING_PATH = RUN_DIR / "deferred-remaining-current.json"
SUMMARY_PATH = RUN_DIR / "deferred-review-summary.json"


def main() -> None:
    source = json.loads(SOURCE_PATH.read_text(encoding="utf-8"))
    source_records = source["records"]
    source_ids = {record["marker_id"] for record in source_records}
    if len(source_records) != 399 or len(source_ids) != 399:
        raise ValueError("Deferred source must contain 399 unique records")

    decisions = []
    for path in sorted(RUN_DIR.glob("decisions-deferred-batch-*.json")):
        decisions.extend(json.loads(path.read_text(encoding="utf-8"))["decisions"])
    decision_ids = [decision["marker_id"] for decision in decisions]
    duplicates = sorted(marker_id for marker_id, count in Counter(decision_ids).items() if count > 1)
    unknown = sorted(set(decision_ids) - source_ids)
    if duplicates or unknown:
        raise ValueError(f"Invalid deferred decisions: duplicates={duplicates}, unknown={unknown}")

    reviewed_ids = set(decision_ids)
    remaining = [record for record in source_records if record["marker_id"] not in reviewed_ids]
    decision_counts = Counter(decision["decision"] for decision in decisions)
    paper_counts = Counter(record["paper_id"] for record in remaining)
    remaining_document = {
        "run_id": "20260909-astra-deferred-remaining",
        "record_count": len(remaining),
        "marker_ids": [record["marker_id"] for record in remaining],
        "records": remaining,
    }
    summary = {
        "run_id": "20260909-astra-deferred-review",
        "source_count": len(source_records),
        "reviewed_count": len(decisions),
        "remaining_count": len(remaining),
        "reviewed_unique_count": len(reviewed_ids),
        "coverage_valid": len(source_records) == len(decisions) + len(remaining),
        "duplicate_decision_marker_ids": duplicates,
        "unknown_decision_marker_ids": unknown,
        "decision_counts": dict(sorted(decision_counts.items())),
        "remaining_by_paper": dict(sorted(paper_counts.items())),
    }
    REMAINING_PATH.write_text(json.dumps(remaining_document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    SUMMARY_PATH.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
