from __future__ import annotations

import hashlib
import json
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
LUNA_DIR = RUN_DIR.parent / "execution" / "luna-existing-marker-correctness"
REVIEWS_PATH = LUNA_DIR / "review-records.json"
SOURCE_PATH = RUN_DIR.parents[1] / "DOI_10.1038_s41586-020-2922-4.md"
PAPER_ID = "DOI_10.1038_s41586-020-2922-4"

EXCLUDE_REASONS = {
    "M00157": "CD123/IL3RA 只出现在 basophils、neutrophils、eosinophils 联合分选抗体 panel，不能外推为该合并类别中每种细胞的正式 marker。",
    "M00188": "CD31/PECAM1 与 CD45 微珠只定义 immune and endothelial enriched 富集组，不是单一细胞类型 marker 关系。",
    "M00209": "CD123/IL3RA 只出现在 pDC、mDC、CD16+ DC 联合分选 panel，未给出目标细胞级阳性定义。",
    "M00210": "CD11c/ITGAX 只出现在 pDC、mDC、CD16+ DC 联合分选 panel，未给出目标细胞级阳性定义。",
    "M00223": "CD62L/SELL 只出现在 T-cell 分选 panel，不能外推为所有 T cells 的正式 marker。",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    review_doc = json.loads(REVIEWS_PATH.read_text(encoding="utf-8"))
    rows = [
        row
        for row in review_doc["records"]
        if row["paper_id"] == PAPER_ID
        and row.get("evidence_binding_status") == "context_backed_target_marker_review"
    ]
    if len(rows) != 32:
        raise ValueError(f"Expected 32 context-backed records, found {len(rows)}")
    if not set(EXCLUDE_REASONS).issubset({row["marker_id"] for row in rows}):
        raise ValueError("Expected exclusion IDs are not all present")

    source_hash = sha256(SOURCE_PATH)
    decisions = []
    for row in sorted(rows, key=lambda item: item["marker_id"]):
        values = row.get("after_values") or row["original_values"]
        marker_id = row["marker_id"]
        if marker_id in EXCLUDE_REASONS:
            decision = "exclude_from_final"
            publication_eligible = False
            reason = EXCLUDE_REASONS[marker_id]
        else:
            decision = "accept_current_after_values"
            publication_eligible = True
            reason = (
                "Astra 对照正文、图注或目标细胞级分群定义复核；来源明确将目标基因作为"
                "该目标细胞的 marker、阳性检测或选择性表达基因。"
            )
        decisions.append(
            {
                "decision_id": f"ASTRA-FINAL-2922-{marker_id}",
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

    result = {
        "run_id": "20260908-astra-final-marker-finalization",
        "batch_id": "ASTRA-CONTEXT-2922-01",
        "paper_id": PAPER_ID,
        "record_count": len(decisions),
        "result_counts": {
            "accept_current_after_values": sum(item["publication_eligible"] for item in decisions),
            "exclude_from_final": sum(not item["publication_eligible"] for item in decisions),
        },
        "decisions": decisions,
    }
    (RUN_DIR / "decisions-context-2922.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result["result_counts"], ensure_ascii=False))


if __name__ == "__main__":
    main()
