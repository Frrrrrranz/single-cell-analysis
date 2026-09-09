from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


RUN_DIR = Path(__file__).resolve().parent
LUNA_DIR = RUN_DIR.parent / "execution" / "luna-existing-marker-correctness"
REVIEWS_PATH = LUNA_DIR / "review-records.json"
SOURCE_PATH = RUN_DIR.parents[1] / "DOI_10.1126_sciimmunol.adf9988.md"
PAPER_ID = "DOI_10.1126_sciimmunol.adf9988"

EXPECTED_IDS = {
    "M00658", "M00659", "M00663", "M00664", "M00668", "M00675", "M00682", "M00683",
    "M02348", "M02350", "M02377", "M02378", "M02379", "M02380", "M02381", "M02382",
    "M02383", "M02384", "M02385", "M02386", "M02387", "M02388", "M02389", "M02390",
    "M02394", "M02395",
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
rows = [record for record in review_doc["records"] if record["marker_id"] in EXPECTED_IDS]
actual_ids = {record["marker_id"] for record in rows}
if actual_ids != EXPECTED_IDS:
    raise RuntimeError(f"Batch ID mismatch: missing={sorted(EXPECTED_IDS - actual_ids)}, extra={sorted(actual_ids - EXPECTED_IDS)}")
if {record["paper_id"] for record in rows} != {PAPER_ID}:
    raise RuntimeError("Batch contains an unexpected paper")

source_hash = sha256(SOURCE_PATH)
decisions = []
for record in sorted(rows, key=lambda item: item["marker_id"]):
    marker_id = record["marker_id"]
    values = current_values(record)
    if marker_id == "M02348":
        values["cell_type"] = "pre-pro-B cell"
        values["source_locator"] = "Main text, B cell developmental niche; Fig. 3C"
        values["source_context"] = "pre-pro-B cells are defined as EBF1+SPINK2+VPREB1+; Fig. 3C shows B-cell marker-gene expression."
        values["notes"] = (
            "Astra 复核纠正：原 LMPP/ELP–SPINK2 关系与正文不符；正文将 SPINK2 阳性明确归于 "
            "pre-pro-B（EBF1+SPINK2+VPREB1+）。"
        )
        values["audit_status"] = "astra_corrected_include"
        values["review_method"] = "astra_source_review_2026-09-09"
        decision = "correct_and_accept"
        reason = "正文明确把 SPINK2 置于 pre-pro-B 定义中；原 LMPP/ELP 标签需纠正后保留。"
    else:
        decision = "accept_current_after_values"
        reason = (
            "Astra 对照正文、方法中的明确阳/阴性 gate、图注或目标细胞级 marker 图复核；"
            "目标细胞—marker—极性关系可由当前来源支持。"
        )
    decisions.append(
        {
            "decision_id": f"ASTRA-221-B001-{marker_id}",
            "marker_id": marker_id,
            "paper_id": PAPER_ID,
            "decision": decision,
            "publication_eligible": True,
            "after_values": values,
            "source_file": str(SOURCE_PATH),
            "source_sha256": source_hash,
            "source_locator": values.get("source_locator"),
            "source_excerpt": values.get("source_context"),
            "astra_reason": reason,
            "reviewed_by": "GPT-6 Astra",
            "reviewed_at": "2026-09-09",
        }
    )

result_counts = Counter(item["decision"] for item in decisions)
result = {
    "run_id": "20260909-astra-remaining-221",
    "batch_id": "ASTRA-221-B001",
    "paper_id": PAPER_ID,
    "record_count": len(decisions),
    "result_counts": dict(result_counts),
    "remaining_after_batch": 221 - len(decisions),
    "decisions": decisions,
}
(RUN_DIR / "decisions-review-batch-001.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)
print(json.dumps({"record_count": len(decisions), "result_counts": result["result_counts"], "remaining": result["remaining_after_batch"]}, ensure_ascii=False))
