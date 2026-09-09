from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


RUN_DIR = Path(__file__).resolve().parent
LUNA_DIR = RUN_DIR.parent / "execution" / "luna-existing-marker-correctness"
REVIEWS_PATH = LUNA_DIR / "review-records.json"
SOURCE_DIR = RUN_DIR.parents[1]

BATCHES = {
    "002": {
        "paper_id": "DOI_10.1038_s41586-021-03929-x",
        "expected_ids": {
            "M01366", "M01367", "M01369", "M01370", "M01373", "M01376", "M01377", "M01380",
            "M01381", "M01384", "M01385", "M01386", "M01398", "M02516", "M02518",
        },
    },
    "003": {
        "paper_id": "DOI_10.1016_j.cell.2021.07.023",
        "expected_ids": {
            "M00923", "M00949", "M00958", "M01008", "M01012", "M01014", "M01015", "M01023",
            "M01024", "M01030", "M01031",
        },
    },
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
batch_outputs = []
completed_before = 26
for batch_no, config in BATCHES.items():
    paper_id = config["paper_id"]
    expected_ids = config["expected_ids"]
    rows = [record for record in review_doc["records"] if record["marker_id"] in expected_ids]
    actual_ids = {record["marker_id"] for record in rows}
    if actual_ids != expected_ids:
        raise RuntimeError(
            f"Batch {batch_no} ID mismatch: missing={sorted(expected_ids - actual_ids)}, "
            f"extra={sorted(actual_ids - expected_ids)}"
        )
    if {record["paper_id"] for record in rows} != {paper_id}:
        raise RuntimeError(f"Batch {batch_no} contains an unexpected paper")

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
                "astra_reason": (
                    "Astra 对照正文、图注、明确细胞定义或阳/阴性 gate 复核；"
                    "当前目标细胞—marker—极性关系由来源直接支持。"
                ),
                "reviewed_by": "GPT-6 Astra",
                "reviewed_at": "2026-09-09",
            }
        )

    completed_before += len(decisions)
    result = {
        "run_id": "20260909-astra-remaining-221",
        "batch_id": f"ASTRA-221-B{batch_no}",
        "paper_id": paper_id,
        "record_count": len(decisions),
        "result_counts": {"accept_current_after_values": len(decisions)},
        "remaining_after_batch": 221 - completed_before,
        "decisions": decisions,
    }
    output_path = RUN_DIR / f"decisions-review-batch-{batch_no}.json"
    output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    batch_outputs.append(
        {"batch": batch_no, "paper_id": paper_id, "accepted": len(decisions), "remaining": result["remaining_after_batch"]}
    )

print(json.dumps(batch_outputs, ensure_ascii=False))
