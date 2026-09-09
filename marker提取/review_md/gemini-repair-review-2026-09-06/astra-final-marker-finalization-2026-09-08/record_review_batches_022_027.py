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
    "022": ("DOI_10.1038_s41586-020-2922-4", {"M00177", "M00179", "M00189", "M00222"}),
    "023": ("DOI_10.1038_s42255-023-00876-x", {"M01622", "M01635", "M01645", "M01649"}),
    "024": ("DOI_10.1126_science.aat5031", {"M01094", "M01099", "M01104", "M02580"}),
    "025": ("DOI_10.1038_s41591-024-03215-z", {"M01308", "M01312", "M01316"}),
    "026": ("DOI_10.7554_elife.62522", {"M00051", "M02586", "M02587"}),
    "027": ("DOI_10.1038_s41586-021-03569-1", {"M00815", "M00816", "M00817"}),
}
EXCLUDE_REASONS = {
    "M00189": "CD31/CD45 磁珠共同定义的是 immune and endothelial enriched 混合富集组；PTPRC/CD45 不能作为其中 endothelial 部分的阳性 marker。",
    "M00222": "CD45RA/PTPRC 仅出现在通用 T-cell 抗体 panel，极性未知，未给出目标细胞级阳性定义，不能形成正式 marker 关系。",
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
completed_before = 170
outputs = []
for batch_no, (paper_id, expected_ids) in BATCHES.items():
    rows = [record for record in review_doc["records"] if record["marker_id"] in expected_ids]
    if {record["marker_id"] for record in rows} != expected_ids or {record["paper_id"] for record in rows} != {paper_id}:
        raise RuntimeError(f"Batch {batch_no} source/ID mismatch")
    source_path = SOURCE_DIR / f"{paper_id}.md"
    source_hash = sha256(source_path)
    decisions = []
    for record in sorted(rows, key=lambda item: item["marker_id"]):
        marker_id = record["marker_id"]
        values = current_values(record)
        if marker_id in EXCLUDE_REASONS:
            decision = "exclude_from_final"
            eligible = False
            after_values = None
            reason = EXCLUDE_REASONS[marker_id]
        elif marker_id == "M01645":
            values["cell_type"] = "postnatal δ-cell"
            values["subtype"] = "postnatal only"
            values["source_context"] = "Cer1 is a potential δ-cell marker in postnatal samples, but not in embryonic samples."
            values["notes"] = "Astra 复核收窄：Cer1 的 δ-cell marker 关系仅适用于 postnatal 样本。"
            values["audit_status"] = "astra_corrected_include"
            values["review_method"] = "astra_source_review_2026-09-09"
            decision = "correct_and_accept"
            eligible = True
            after_values = values
            reason = "来源明确限定 Cer1 只在 postnatal δ-cells 中成立，补足阶段限定后保留。"
        else:
            decision = "accept_current_after_values"
            eligible = True
            after_values = values
            reason = "Astra 对照正文、图注或明确阳/阴性 gate 复核，当前目标细胞—marker 关系成立。"
        decisions.append(
            {
                "decision_id": f"ASTRA-221-B{batch_no}-{marker_id}",
                "marker_id": marker_id,
                "paper_id": paper_id,
                "decision": decision,
                "publication_eligible": eligible,
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
