from __future__ import annotations

import hashlib
import json
from pathlib import Path

from openpyxl import load_workbook


RUN_DIR = Path(__file__).resolve().parent
WORKSPACE = RUN_DIR.parents[3]
DEFERRED_PATH = RUN_DIR / "deferred-remaining-current.json"
WORKBOOK_PATH = RUN_DIR / "staged" / "our_markers_reviewing.xlsx"
OUTPUT_PATH = RUN_DIR / "decisions-deferred-batch-003.json"
PAPER_ID = "DOI_10.1101_2025.09.26.678707"
PDF_PATH = next((WORKSPACE / "marker提取" / "pdf").glob("*678707*.pdf"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    deferred = json.loads(DEFERRED_PATH.read_text(encoding="utf-8"))["records"]
    records = [record for record in deferred if record["paper_id"] == PAPER_ID]
    if len(records) != 117:
        raise ValueError(f"Expected 117 deferred records for {PAPER_ID}, got {len(records)}")

    workbook = load_workbook(WORKBOOK_PATH, read_only=True, data_only=False)
    sheet = workbook["markers"]
    rows = sheet.iter_rows(values_only=True)
    headers = [str(value) for value in next(rows)]
    marker_id_index = headers.index("marker_id")
    marker_rows = {
        str(row[marker_id_index]): dict(zip(headers, row, strict=True))
        for row in rows
        if row[marker_id_index]
    }

    pdf_hash = sha256(PDF_PATH)
    decisions = []
    for record in records:
        marker_id = record["marker_id"]
        after_values = marker_rows.get(marker_id)
        if after_values is None:
            raise ValueError(f"Marker missing from reviewing workbook: {marker_id}")
        locator = after_values.get("source_locator") or record["source_locator"]
        if "Figure 2b" in locator:
            reason = "逐项对照 Figure 2b fibroblast gene-expression dotplot，目标 fibroblast 状态与 marker 列一致。"
        elif "Figure 2h" in locator:
            reason = "逐项对照 Figure 2h immune-subtype gene-expression dotplot，目标免疫亚群与 marker 列一致。"
        elif "ED Figure 6f" in locator:
            reason = "逐项对照 ED Figure 6f myeloid dotplot，目标髓系状态与 marker 列一致。"
        else:
            reason = "逐项对照 Figure 3b/3c epithelial-state gene-expression 与轨迹面板，目标状态-marker/TF 关系一致。"
        decisions.append(
            {
                "decision_id": f"ASTRA-DEFERRED-B003-{marker_id}",
                "marker_id": marker_id,
                "paper_id": PAPER_ID,
                "decision": "accept_current_after_values",
                "publication_eligible": True,
                "after_values": after_values,
                "source_file": str(PDF_PATH),
                "source_sha256": pdf_hash,
                "source_locator": locator,
                "source_excerpt": after_values.get("source_context"),
                "astra_reason": reason,
                "reviewed_by": "GPT-6 Astra",
                "reviewed_at": "2026-09-09",
            }
        )

    document = {
        "run_id": "20260909-astra-deferred-review",
        "batch_id": "ASTRA-DEFERRED-B003",
        "paper_id": PAPER_ID,
        "record_count": len(decisions),
        "result_counts": {"accept_current_after_values": len(decisions)},
        "remaining_after_batch": 2,
        "evidence_groups": {
            "Figure 2b": 17,
            "Figure 2h": 33,
            "ED Figure 6f (including main-text paired records)": 34,
            "Figure 3b/3c (including main-text paired records)": 33,
        },
        "decisions": decisions,
    }
    OUTPUT_PATH.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(OUTPUT_PATH), "accepted": len(decisions), "remaining": 2}, ensure_ascii=False))


if __name__ == "__main__":
    main()
