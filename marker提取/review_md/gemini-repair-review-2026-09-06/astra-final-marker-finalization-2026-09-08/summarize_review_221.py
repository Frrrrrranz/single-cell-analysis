from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any


RUN_DIR = Path(__file__).resolve().parent


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


worklist = read_json(RUN_DIR / "remaining-221-worklist.json")
expected_ids = {record["marker_id"] for record in worklist["records"]}
batch_paths = sorted(RUN_DIR.glob("decisions-review-batch-*.json"))
decisions = [decision for path in batch_paths for decision in read_json(path)["decisions"]]
decision_ids = [decision["marker_id"] for decision in decisions]
decision_id_set = set(decision_ids)
duplicates = sorted(marker_id for marker_id, count in Counter(decision_ids).items() if count > 1)

if len(decisions) != 221 or decision_id_set != expected_ids or duplicates:
    raise RuntimeError(
        f"221 review coverage failed: decisions={len(decisions)}, missing={sorted(expected_ids - decision_id_set)}, "
        f"extra={sorted(decision_id_set - expected_ids)}, duplicates={duplicates}"
    )

counts = Counter(decision["decision"] for decision in decisions)
eligible = [decision for decision in decisions if decision["publication_eligible"]]
excluded = [decision for decision in decisions if decision["decision"] == "exclude_from_final"]
deferred_new = [decision for decision in decisions if decision["decision"] == "defer_unresolved"]
corrected = [decision for decision in decisions if decision["decision"] == "correct_and_accept"]

legacy_deferred = read_json(RUN_DIR / "deferred-unresolved.json")["records"]
context_695268 = read_json(RUN_DIR / "decisions-context-695268.json")["decisions"]
figure_deferred = [decision for decision in context_695268 if decision["decision"] == "defer_unresolved"]
all_deferred = [*legacy_deferred, *figure_deferred, *deferred_new]
all_deferred_ids = [record["marker_id"] for record in all_deferred]
if len(all_deferred) != 399 or len(set(all_deferred_ids)) != 399:
    raise RuntimeError(f"Deferred union is not 399 unique records: total={len(all_deferred)}, unique={len(set(all_deferred_ids))}")

summary = {
    "run_id": "20260909-astra-remaining-221",
    "status": "completed",
    "batch_count": len(batch_paths),
    "reviewed_count": len(decisions),
    "unique_marker_count": len(decision_id_set),
    "coverage_matches_worklist": True,
    "result_counts": dict(counts),
    "publication_eligible_count": len(eligible),
    "excluded_marker_ids": sorted(decision["marker_id"] for decision in excluded),
    "corrected_marker_ids": sorted(decision["marker_id"] for decision in corrected),
    "newly_deferred_marker_ids": sorted(decision["marker_id"] for decision in deferred_new),
    "all_deferred_count": len(all_deferred),
    "full_review_unit_partition": {
        "carried_forward_evidence_bound": 1819,
        "accepted_before_221": 63,
        "publication_eligible_from_221": len(eligible),
        "confirmed_invalid": 8,
        "deferred": len(all_deferred),
        "total": 1819 + 63 + len(eligible) + 8 + len(all_deferred),
    },
}
if summary["full_review_unit_partition"]["total"] != 2502:
    raise RuntimeError("Full review-unit partition does not total 2502")

(RUN_DIR / "review-221-summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(RUN_DIR / "deferred-all-current.json").write_text(
    json.dumps(
        {
            "run_id": "20260909-astra-all-current-deferred",
            "record_count": len(all_deferred),
            "marker_ids": sorted(all_deferred_ids),
            "records": all_deferred,
        },
        ensure_ascii=False,
        indent=2,
    )
    + "\n",
    encoding="utf-8",
)
print(json.dumps(summary, ensure_ascii=False, indent=2))
