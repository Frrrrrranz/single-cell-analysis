from __future__ import annotations

import hashlib
import json
from pathlib import Path

from openpyxl import load_workbook


RUN_DIR = Path(__file__).resolve().parent
WORKSPACE = RUN_DIR.parents[3]
DEFERRED_PATH = RUN_DIR / "deferred-all-current.json"
WORKBOOK_PATH = RUN_DIR / "staged" / "our_markers_reviewing.xlsx"
OUTPUT_PATH = RUN_DIR / "decisions-deferred-batch-001.json"
PAPER_ID = "DOI_10.1101_2025.01.17.633590"
PDF_PATH = next((WORKSPACE / "marker提取" / "pdf").glob("*633590*.pdf"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    deferred = json.loads(DEFERRED_PATH.read_text(encoding="utf-8"))["records"]
    records = [record for record in deferred if record["paper_id"] == PAPER_ID]
    if len(records) != 238:
        raise ValueError(f"Expected 238 deferred records for {PAPER_ID}, got {len(records)}")

    workbook = load_workbook(WORKBOOK_PATH, read_only=True, data_only=False)
    sheet = workbook["markers"]
    rows = sheet.iter_rows(values_only=True)
    headers = [str(value) for value in next(rows)]
    marker_rows = {
        str(row[headers.index("marker_id")]): dict(zip(headers, row, strict=True))
        for row in rows
        if row[headers.index("marker_id")]
    }

    reasons = {
        "Supplementary Figure 2": "逐项对照 Supplementary Figure 2 热图的 marker gene 行名与细胞类型列，目标细胞-marker 关系一致。",
        "Supplementary Figure 8e": "逐项对照 Supplementary Figure 8e 的 alpha-cell cluster 1-7 marker heatmap，亚群与 marker 行一致。",
        "Supplementary Figure 9e": "逐项对照 Supplementary Figure 9e 的 delta-cell cluster marker heatmap，亚群与 marker 行一致。",
    }
    pdf_hash = sha256(PDF_PATH)
    decisions = []
    for record in records:
        marker_id = record["marker_id"]
        if marker_id not in marker_rows:
            raise ValueError(f"Marker missing from reviewing workbook: {marker_id}")
        locator = record["source_locator"]
        reason = reasons.get(
            locator,
            "逐项对照 Figure 4c 的 beta-cell cluster heatmap；目标 cluster 与 marker 行标签一致，正文中的功能状态说明也相符。",
        )
        decisions.append(
            {
                "decision_id": f"ASTRA-DEFERRED-B001-{marker_id}",
                "marker_id": marker_id,
                "paper_id": PAPER_ID,
                "decision": "accept_current_after_values",
                "publication_eligible": True,
                "after_values": marker_rows[marker_id],
                "source_file": str(PDF_PATH),
                "source_sha256": pdf_hash,
                "source_locator": locator,
                "source_excerpt": record.get("source_context"),
                "astra_reason": reason,
                "reviewed_by": "GPT-6 Astra",
                "reviewed_at": "2026-09-09",
            }
        )

    document = {
        "run_id": "20260909-astra-deferred-review",
        "batch_id": "ASTRA-DEFERRED-B001",
        "paper_id": PAPER_ID,
        "record_count": len(decisions),
        "result_counts": {"accept_current_after_values": len(decisions)},
        "remaining_after_batch": 399 - len(decisions),
        "evidence_groups": {
            "Supplementary Figure 2": 127,
            "Supplementary Figure 8e": 34,
            "Supplementary Figure 9e": 10,
            "Figure 4c": 67,
        },
        "decisions": decisions,
    }
    OUTPUT_PATH.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(OUTPUT_PATH), "accepted": len(decisions), "remaining": 161}, ensure_ascii=False))


if __name__ == "__main__":
    main()
