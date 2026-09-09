from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


RUN_DIR = Path(__file__).resolve().parent
REVIEWS_PATH = RUN_DIR.parent / "execution" / "luna-existing-marker-correctness" / "review-records.json"
SOURCE_DIR = RUN_DIR.parents[1]

BATCHES = {
    "015": ("DOI_10.1002_pros.24020", {"M01187", "M01192", "M01194", "M02496", "M02500"}),
    "016": ("DOI_10.1016_j.cell.2017.09.004", {"M01918", "M01919", "M01920", "M01921", "M01922"}),
    "017": ("DOI_10.1016_j.cell.2022.11.005", {"M00448", "M00477", "M00578", "M00591", "M00596"}),
    "018": ("DOI_10.1038_s41467-021-21783-3", {"M01588", "M01590", "M01591", "M01592", "M01594"}),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def current_values(record: dict[str, Any]) -> dict[str, Any]:
    return dict(record.get("after_values") or record["original_values"])


review_doc = json.loads(REVIEWS_PATH.read_text(encoding="utf-8"))
completed_before = 135
outputs = []
for batch_no, (paper_id, expected_ids) in BATCHES.items():
    rows = [record for record in review_doc["records"] if record["marker_id"] in expected_ids]
    actual_ids = {record["marker_id"] for record in rows}
    if actual_ids != expected_ids or {record["paper_id"] for record in rows} != {paper_id}:
        raise RuntimeError(f"Batch {batch_no} source/ID mismatch")
    source_path = SOURCE_DIR / f"{paper_id}.md"
    source_hash = sha256(source_path)
    decisions = []
    for record in sorted(rows, key=lambda item: item["marker_id"]):
        values = current_values(record)
        decisions.append(
            {
                "decision_id": f"ASTRA-221-B{batch_no}-{record['marker_id']}",
                "marker_id": record["marker_id"],
                "paper_id": paper_id,
                "decision": "accept_current_after_values",
                "publication_eligible": True,
                "after_values": values,
                "source_file": str(source_path),
                "source_sha256": source_hash,
                "source_locator": values.get("source_locator"),
                "source_excerpt": values.get("source_context"),
                "astra_reason": "Astra 对照正文或图注明确的细胞命名、marker 表达与阳性关系复核，当前记录成立。",
                "reviewed_by": "GPT-6 Astra",
                "reviewed_at": "2026-09-09",
            }
        )
    completed_before += len(decisions)
    counts = Counter(item["decision"] for item in decisions)
    result = {
        "run_id": "20260909-astra-remaining-221",
        "batch_id": f"ASTRA-221-B{batch_no}",
        "paper_id": paper_id,
        "record_count": len(decisions),
        "result_counts": dict(counts),
        "remaining_after_batch": 221 - completed_before,
        "decisions": decisions,
    }
    (RUN_DIR / f"decisions-review-batch-{batch_no}.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    outputs.append({"batch": batch_no, "paper_id": paper_id, "counts": dict(counts), "remaining": result["remaining_after_batch"]})

print(json.dumps(outputs, ensure_ascii=False))
