from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
PROJECT_REVIEW_DIR = RUN_DIR.parent
LUNA_DIR = PROJECT_REVIEW_DIR / "execution" / "luna-existing-marker-correctness"
SOURCE_PATH = LUNA_DIR / "review-records.json"

CONTEXT_BACKED_STATUS = "context_backed_target_marker_review"
INHERITED_STATUS = "prior_quick_consistency_inherited_with_documented_limit"
DEFERRED_PAPERS = {
    "DOI_10.1101_2025.01.17.633590",
    "DOI_10.1101_2025.09.26.678707",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def compact_record(record: dict) -> dict:
    values = record.get("after_values") or record.get("original_values") or {}
    return {
        "review_id": record.get("review_id"),
        "marker_id": record.get("marker_id"),
        "paper_id": record.get("paper_id"),
        "task_no": values.get("task_no"),
        "cell_type": values.get("cell_type"),
        "subtype": values.get("subtype"),
        "species": values.get("species"),
        "gene_symbol": values.get("gene_symbol"),
        "original_symbol": values.get("original_symbol"),
        "marker_polarity": values.get("marker_polarity"),
        "evidence_type": values.get("evidence_type"),
        "source_locator": values.get("source_locator"),
        "source_context": values.get("source_context"),
        "prior_evidence_binding_status": record.get("evidence_binding_status"),
    }


def main() -> None:
    document = json.loads(SOURCE_PATH.read_text(encoding="utf-8"))
    records = document["records"]

    deferred = [
        compact_record(record)
        for record in records
        if record.get("paper_id") in DEFERRED_PAPERS
        and record.get("evidence_binding_status") == INHERITED_STATUS
    ]
    context_backed = [
        compact_record(record)
        for record in records
        if record.get("evidence_binding_status") == CONTEXT_BACKED_STATUS
    ]
    blank_binding = [
        compact_record(record)
        for record in records
        if not record.get("evidence_binding_status")
    ]
    inherited_local = [
        compact_record(record)
        for record in records
        if record.get("evidence_binding_status") == INHERITED_STATUS
        and record.get("paper_id") not in DEFERRED_PAPERS
    ]

    source_hash = sha256(SOURCE_PATH)
    deferred_registry = {
        "run_id": "20260908-astra-final-marker-finalization",
        "policy": {
            "status": "unresolved_source_material_deferred",
            "publication_eligible": False,
            "final_table_action": "exclude_until_source_verified",
            "reason": "用户同意暂时跳过缺少决定性原图或补充材料、需要大规模逐图复核的复杂记录。",
        },
        "source_registry": str(SOURCE_PATH),
        "source_sha256": source_hash,
        "record_count": len(deferred),
        "paper_counts": dict(Counter(item["paper_id"] for item in deferred)),
        "records": deferred,
    }
    worklist = {
        "run_id": "20260908-astra-final-marker-finalization",
        "source_registry": str(SOURCE_PATH),
        "source_sha256": source_hash,
        "buckets": {
            "deferred_unresolved": {
                "count": len(deferred),
                "marker_ids": [item["marker_id"] for item in deferred],
            },
            "context_backed_reopen": {
                "count": len(context_backed),
                "paper_counts": dict(Counter(item["paper_id"] for item in context_backed)),
                "records": context_backed,
            },
            "blank_binding_recheck": {
                "count": len(blank_binding),
                "paper_counts": dict(Counter(item["paper_id"] for item in blank_binding)),
                "records": blank_binding,
            },
            "inherited_local_recheck": {
                "count": len(inherited_local),
                "paper_counts": dict(Counter(item["paper_id"] for item in inherited_local)),
                "records": inherited_local,
            },
        },
    }

    (RUN_DIR / "deferred-unresolved.json").write_text(
        json.dumps(deferred_registry, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (RUN_DIR / "worklist.json").write_text(
        json.dumps(worklist, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                "deferred_unresolved": len(deferred),
                "context_backed_reopen": len(context_backed),
                "blank_binding_recheck": len(blank_binding),
                "inherited_local_recheck": len(inherited_local),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
