from __future__ import annotations

import hashlib
import json
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
AUDIT_DIR = RUN_DIR.parent / "astra-audit-after-luna-existing-marker-correctness"
LUNA_DIR = RUN_DIR.parent / "execution" / "luna-existing-marker-correctness"
TRIAGE_PATH = AUDIT_DIR / "triage.json"
REVIEWS_PATH = LUNA_DIR / "review-records.json"

ACCEPTED_IDS = {
    "M00036", "M00038", "M00039", "M00044", "M00047", "M00048", "M00050",
    "M00071", "M00398", "M00403", "M00415", "M00416", "M00417", "M00418",
    "M00455", "M00456", "M00460", "M00462", "M00466", "M00467", "M00491",
    "M00494", "M00530", "M00531", "M00553", "M00554", "M00585", "M00592",
    "M00594", "M00597", "M01510", "M02590", "M02591", "M02592",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    triage = json.loads(TRIAGE_PATH.read_text(encoding="utf-8"))
    review_doc = json.loads(REVIEWS_PATH.read_text(encoding="utf-8"))
    reviews = {item["marker_id"]: item for item in review_doc["records"]}
    triage_rows = {
        item["marker_id"]: item
        for item in triage["audit_sets"]["all_blank_binding"]
    }

    if set(triage_rows) != ACCEPTED_IDS:
        raise ValueError(
            "Blank-binding population changed: "
            f"missing={sorted(ACCEPTED_IDS - set(triage_rows))}, "
            f"unexpected={sorted(set(triage_rows) - ACCEPTED_IDS)}"
        )

    decisions = []
    for marker_id in sorted(ACCEPTED_IDS):
        triage_row = triage_rows[marker_id]
        source_path = Path(triage_row["checks"]["source_path"])
        review = reviews[marker_id]
        after_values = review.get("after_values") or review["original_values"]
        decisions.append(
            {
                "decision_id": f"ASTRA-FINAL-BLANK-{marker_id}",
                "marker_id": marker_id,
                "paper_id": review["paper_id"],
                "decision": "accept_current_after_values",
                "publication_eligible": True,
                "after_values": after_values,
                "source_file": str(source_path),
                "source_sha256": sha256(source_path),
                "source_locator": after_values.get("source_locator"),
                "independent_window": triage_row["best_source_window"],
                "astra_reason": (
                    "Astra 对照本地来源正文或图注复核了目标细胞、目标基因及表达方向；"
                    "接受 Luna 当前 after_values。"
                ),
                "reviewed_by": "GPT-6 Astra",
                "reviewed_at": "2026-09-08",
            }
        )

    output = {
        "run_id": "20260908-astra-final-marker-finalization",
        "batch_id": "ASTRA-BLANK-BINDING-01",
        "population_definition": "Luna review records with blank evidence_binding_status",
        "record_count": len(decisions),
        "result_counts": {"accept_current_after_values": len(decisions)},
        "source_registry": str(REVIEWS_PATH),
        "source_registry_sha256": sha256(REVIEWS_PATH),
        "decisions": decisions,
    }
    (RUN_DIR / "decisions-blank-binding.json").write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output["result_counts"], ensure_ascii=False))


if __name__ == "__main__":
    main()
