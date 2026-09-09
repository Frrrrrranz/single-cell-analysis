from __future__ import annotations

import json
from pathlib import Path


RUN_DIR = Path(r"D:/OneDrive/Desktop/组/marker提取/review_md/gemini-repair-review-2026-09-06/execution/luna-existing-marker-correctness")
HOLD_ID = "M00868"
REASON = "Astra 要求对 SOX2(cid:3)/SOX2+ 符号歧义进行 PDF 级确认；当前本地材料未提供对应 PDF，暂不据 Markdown 自动裁决。"


def main() -> None:
    path = RUN_DIR / "review-records.json"
    doc = json.loads(path.read_text(encoding="utf-8"))
    record = next(item for item in doc["records"] if item["marker_id"] == HOLD_ID)
    record["remaining_gaps"] = [REASON]
    record["reason"] = REASON
    record["evidence_binding_status"] = "candidate_only_held_for_pdf_semantic_review"
    record["semantic_review"] = {
        "status": "held_pending",
        "method": "manual_hold_due_to_pdf_symbol_ambiguity",
        "reason": REASON,
    }
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
