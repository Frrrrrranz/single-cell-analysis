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
    "004": {
        "paper_id": "DOI_10.1126_science.abo0510",
        "expected_ids": {"M01471", "M01472", "M01473", "M01474", "M01475", "M01478", "M01479", "M01495", "M01496", "M01501"},
    },
    "005": {
        "paper_id": "DOI_10.1016_j.celrep.2018.11.086",
        "expected_ids": {"M01197", "M01200", "M01205", "M01207", "M01212", "M01214", "M01221", "M01222", "M01223"},
    },
    "006": {
        "paper_id": "DOI_10.1038_s42003-024-07315-x",
        "expected_ids": {"M01806", "M01807", "M01808", "M01836", "M01854", "M01861", "M01865", "M01876", "M01883"},
    },
    "007": {
        "paper_id": "DOI_10.1126_science.abl4290",
        "expected_ids": {"M01458", "M01461", "M01462", "M01467", "M01468", "M02581", "M02582", "M02584"},
    },
}

DEFER_REASONS = {
    "M01806": "现有来源只列出用于 cardiac macrophages 的抗体 panel，缺失补充材料中的实际 gate，不能据此单独确认 F4/80 阳性关系。",
    "M01807": "现有来源只列出用于 cardiac macrophages 的抗体 panel，缺失补充材料中的实际 gate，不能据此单独确认 CD11b 阳性关系。",
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
completed_before = 52
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
        if marker_id in DEFER_REASONS:
            decision = "defer_unresolved"
            publication_eligible = False
            after_values = None
            reason = DEFER_REASONS[marker_id]
        elif marker_id == "M01808":
            values["cell_type"] = "mouse cardiac macrophages"
            values["subtype"] = "mm4 (CD206+)"
            values["source_locator"] = "Results, Cardiac macrophage response; Fig. 6a-c; Supplementary Fig. 5c-e"
            values["source_context"] = "CD206+ cardiac macrophages were predicted as the mm4 cluster; Mrc1 was most abundant in mm4 cells."
            values["notes"] = "Astra 复核纠正：CD206/Mrc1 不是全部 cardiac macrophages 的阳性 marker，来源支持的是 CD206+ mm4 亚群。"
            values["audit_status"] = "astra_corrected_include"
            values["review_method"] = "astra_source_review_2026-09-09"
            decision = "correct_and_accept"
            publication_eligible = True
            after_values = values
            reason = "正文与 Fig. 6 将 CD206/Mrc1 明确定位到 mouse cardiac macrophage 的 mm4 亚群，纠正粒度后成立。"
        else:
            decision = "accept_current_after_values"
            publication_eligible = True
            after_values = values
            reason = (
                "Astra 对照正文、图注、明确细胞定义或目标细胞级表达结果复核；"
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
