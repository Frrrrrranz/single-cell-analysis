from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


RUN_DIR = Path(__file__).resolve().parent
WORKLIST_PATH = RUN_DIR / "worklist.json"
DECISION_PATHS = (
    RUN_DIR / "decisions-blank-binding.json",
    RUN_DIR / "decisions-context-2922.json",
    RUN_DIR / "decisions-context-695268.json",
)
OUTPUT_JSON = RUN_DIR / "remaining-221-worklist.json"
OUTPUT_MD = RUN_DIR / "remaining-221-worklist.md"


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


worklist = read_json(WORKLIST_PATH)
decided_ids = {
    decision["marker_id"]
    for path in DECISION_PATHS
    for decision in read_json(path)["decisions"]
}
deferred_ids = {
    record["marker_id"]
    for record in read_json(RUN_DIR / "deferred-unresolved.json")["records"]
}

context_records = worklist["buckets"]["context_backed_reopen"]["records"]
inherited_records = worklist["buckets"]["inherited_local_recheck"]["records"]

remaining_context = [
    record
    for record in context_records
    if record["marker_id"] not in decided_ids and record["marker_id"] not in deferred_ids
]
remaining_inherited = [
    record
    for record in inherited_records
    if record["marker_id"] not in decided_ids and record["marker_id"] not in deferred_ids
]
remaining = remaining_context + remaining_inherited

if len(remaining_context) != 129 or len(remaining_inherited) != 92 or len(remaining) != 221:
    raise RuntimeError(
        "Unexpected remaining counts: "
        f"context={len(remaining_context)}, inherited={len(remaining_inherited)}, total={len(remaining)}"
    )

records_by_paper: dict[str, list[dict[str, Any]]] = defaultdict(list)
for record in remaining:
    records_by_paper[record["paper_id"]].append(record)

paper_counts = Counter(record["paper_id"] for record in remaining)
payload = {
    "run_id": "20260909-astra-remaining-221",
    "status": "in_review",
    "counts": {
        "context_backed": len(remaining_context),
        "inherited_local": len(remaining_inherited),
        "total": len(remaining),
    },
    "paper_counts": dict(sorted(paper_counts.items(), key=lambda item: (-item[1], item[0]))),
    "records": remaining,
}
OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

lines = [
    "# Astra 剩余 221 条复核工作单",
    "",
    "状态：复核中",
    "",
    f"- context-backed：{len(remaining_context)}",
    f"- inherited local：{len(remaining_inherited)}",
    f"- 合计：{len(remaining)}",
    "",
]
for paper_id, records in sorted(records_by_paper.items(), key=lambda item: (-len(item[1]), item[0])):
    lines.extend([f"## {paper_id}（{len(records)}）", ""])
    for record in records:
        lines.append(
            "- {marker_id} | {cell_type} | {gene_symbol} | {marker_polarity} | "
            "{evidence_type} | {source_locator} | {source_context}".format(**record)
        )
    lines.append("")
OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")

print(json.dumps(payload["counts"], ensure_ascii=False))
print(json.dumps(payload["paper_counts"], ensure_ascii=False, indent=2))
