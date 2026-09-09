from __future__ import annotations

import hashlib
import json
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
LUNA_DIR = RUN_DIR.parent / "execution" / "luna-existing-marker-correctness"
REVIEWS_PATH = LUNA_DIR / "review-records.json"
SOURCE_PATH = RUN_DIR.parents[1] / "DOI_10.64898_2025.12.18.695268.md"
PAPER_ID = "DOI_10.64898_2025.12.18.695268"
TEXT_SUPPORTED_IDS = {"M01066", "M01082"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    doc = json.loads(REVIEWS_PATH.read_text(encoding="utf-8"))
    rows = [
        row
        for row in doc["records"]
        if row["paper_id"] == PAPER_ID
        and row.get("evidence_binding_status") == "context_backed_target_marker_review"
    ]
    if len(rows) != 43:
        raise ValueError(f"Expected 43 context-backed records, found {len(rows)}")
    source_hash = sha256(SOURCE_PATH)
    decisions = []
    for row in sorted(rows, key=lambda item: item["marker_id"]):
        values = row.get("after_values") or row["original_values"]
        marker_id = row["marker_id"]
        if marker_id in TEXT_SUPPORTED_IDS:
            decision = "accept_current_after_values"
            publication_eligible = True
            reason = (
                "正文直接将该细胞亚群命名为 KI67+，目标 MKI67 与目标细胞范围和阳性方向一致。"
            )
        else:
            decision = "defer_unresolved"
            publication_eligible = False
            reason = (
                "关系仅声称来自 Fig. 1D、Fig. S1/S3 或 table S6；当前本地来源没有决定性图表内容。"
                "按用户同意的跳过策略隔离，待原图或补表复核后再纳入。"
            )
        decisions.append(
            {
                "decision_id": f"ASTRA-FINAL-695268-{marker_id}",
                "marker_id": marker_id,
                "paper_id": PAPER_ID,
                "decision": decision,
                "publication_eligible": publication_eligible,
                "after_values": values if publication_eligible else None,
                "source_file": str(SOURCE_PATH),
                "source_sha256": source_hash,
                "source_locator": values.get("source_locator"),
                "source_excerpt": values.get("source_context"),
                "astra_reason": reason,
                "reviewed_by": "GPT-6 Astra",
                "reviewed_at": "2026-09-08",
            }
        )
    output = {
        "run_id": "20260908-astra-final-marker-finalization",
        "batch_id": "ASTRA-CONTEXT-695268-01",
        "paper_id": PAPER_ID,
        "record_count": len(decisions),
        "result_counts": {
            "accept_current_after_values": sum(item["publication_eligible"] for item in decisions),
            "defer_unresolved": sum(not item["publication_eligible"] for item in decisions),
        },
        "decisions": decisions,
    }
    (RUN_DIR / "decisions-context-695268.json").write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output["result_counts"], ensure_ascii=False))


if __name__ == "__main__":
    main()
