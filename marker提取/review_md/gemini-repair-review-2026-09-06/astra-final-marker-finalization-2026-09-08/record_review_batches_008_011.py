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
    "008": {
        "paper_id": "DOI_10.1016_j.stem.2022.11.013",
        "expected_ids": {"M00829", "M00832", "M00834", "M00873", "M00877", "M00881", "M00888"},
    },
    "009": {
        "paper_id": "DOI_10.1038_s41467-024-52052-8",
        "expected_ids": {"M00072", "M00073", "M00074", "M00075", "M02566", "M02567", "M02568"},
    },
    "010": {
        "paper_id": "DOI_10.1038_s41586-021-04345-x",
        "expected_ids": {"M00029", "M00030", "M00391", "M00399", "M00400", "M00404", "M00405"},
    },
    "011": {
        "paper_id": "DOI_10.1038_s44318-024-00328-6",
        "expected_ids": {"M00053", "M00620", "M00625", "M01959", "M01961", "M01964", "M01965"},
    },
}

EXCLUDE_REASONS = {
    "M00829": (
        "原记录将 THBD/CD141 阴性泛化到全部 alveolar fibroblasts；来源只支持 "
        "PDGFRA−CD141− alveolar fibroblast 亚群，且该精确关系已由 M00832 收录，故本条过宽且重复。"
    )
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
completed_before = 88
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
        if marker_id in EXCLUDE_REASONS:
            decision = "exclude_from_final"
            publication_eligible = False
            after_values = None
            reason = EXCLUDE_REASONS[marker_id]
        else:
            decision = "accept_current_after_values"
            publication_eligible = True
            after_values = values
            reason = (
                "Astra 对照正文、图注、明确亚型命名或目标细胞级 marker 表达复核；"
                "当前目标细胞—marker—极性关系由来源直接支持。"
            )
        decisions.append(
            {
                "decision_id": f"ASTRA-221-B{batch_no}-{marker_id}",
                "marker_id": marker_id,
                "paper_id": paper_id,
                "decision": decision,
                "publication_eligible": publication_eligible,
                "after_values": after_values,
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
