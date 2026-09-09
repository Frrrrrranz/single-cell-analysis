from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


RUN_DIR = Path(__file__).resolve().parent
LUNA_DIR = RUN_DIR.parent / "execution" / "luna-existing-marker-correctness"
REVIEWS_PATH = LUNA_DIR / "review-records.json"
SOURCE_DIR = RUN_DIR.parents[1]

BATCHES = {
    "012": {
        "paper_id": "DOI_10.1164_rccm.202207-1384oc",
        "expected_ids": {"M00303", "M00305", "M00308", "M00309", "M00319", "M02531", "M02532"},
    },
    "013": {
        "paper_id": "PMID_35115729",
        "expected_ids": {"M01514", "M01518", "M01523", "M01526", "M01529", "M02589"},
    },
    "014": {
        "paper_id": "DOI_10.1038_s41588-022-01243-4",
        "expected_ids": {"M00246", "M00247", "M00248", "M00249", "M00284", "M00285"},
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
completed_before = 116
for batch_no, config in BATCHES.items():
    paper_id = config["paper_id"]
    expected_ids = config["expected_ids"]
    rows = [record for record in review_doc["records"] if record["marker_id"] in expected_ids]
    actual_ids = {record["marker_id"] for record in rows}
    if actual_ids != expected_ids:
        raise RuntimeError(
            f"Batch {batch_no} mismatch: missing={sorted(expected_ids - actual_ids)}, extra={sorted(actual_ids - expected_ids)}"
        )
    if {record["paper_id"] for record in rows} != {paper_id}:
        raise RuntimeError(f"Batch {batch_no} contains an unexpected paper")

    source_path = SOURCE_DIR / f"{paper_id}.md"
    source_hash = sha256(source_path)
    decisions = []
    for record in sorted(rows, key=lambda item: item["marker_id"]):
        marker_id = record["marker_id"]
        values = current_values(record)
        if marker_id == "M00285":
            values["cell_type"] = "naive B cells"
            values["subtype"] = "IgD+"
            values["source_locator"] = "Main text, GAIN section; Fig. 4g; Extended Data Fig. 10i"
            values["source_context"] = "The human SMG contains IgD+ naive B cells; Fig. 4g labels IgD among B-lineage markers."
            values["notes"] = "Astra 复核纠正：IgD 对应 naive B cells，不是 plasma cells。"
            values["audit_status"] = "astra_corrected_include"
            values["review_method"] = "astra_source_review_2026-09-09"
            decision = "correct_and_accept"
            reason = "正文明确写为 IgD+ naive B cells；纠正原 plasma-cell 映射后关系成立。"
        else:
            decision = "accept_current_after_values"
            reason = (
                "Astra 对照正文、图注、明确细胞定义或 marker 表达结果复核；"
                "当前目标细胞—marker—极性关系由来源直接支持。"
            )
        decisions.append(
            {
                "decision_id": f"ASTRA-221-B{batch_no}-{marker_id}",
                "marker_id": marker_id,
                "paper_id": paper_id,
                "decision": decision,
                "publication_eligible": True,
                "after_values": values,
                "source_file": str(source_path),
                "source_sha256": source_hash,
                "source_locator": values.get("source_locator"),
                "source_excerpt": values.get("source_context"),
                "astra_reason": reason,
                "reviewed_by": "GPT-6 Astra",
                "reviewed_at": "2026-09-09",
            }
        )

    completed_before += len(decisions)
    result_counts = Counter(item["decision"] for item in decisions)
    result = {
        "run_id": "20260909-astra-remaining-221",
        "batch_id": f"ASTRA-221-B{batch_no}",
        "paper_id": paper_id,
        "record_count": len(decisions),
        "result_counts": dict(result_counts),
        "remaining_after_batch": 221 - completed_before,
        "decisions": decisions,
    }
    (RUN_DIR / f"decisions-review-batch-{batch_no}.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    batch_outputs.append({"batch": batch_no, "paper_id": paper_id, "counts": dict(result_counts), "remaining": result["remaining_after_batch"]})

print(json.dumps(batch_outputs, ensure_ascii=False))
