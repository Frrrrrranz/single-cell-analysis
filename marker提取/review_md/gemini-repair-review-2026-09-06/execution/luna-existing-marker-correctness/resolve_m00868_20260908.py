from __future__ import annotations

import copy
import json
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
DATE = "2026-09-08"
BATCH_ID = "20260908-M00868"


def load(name: str):
    return json.loads((RUN_DIR / name).read_text(encoding="utf-8"))


def save(name: str, value) -> None:
    (RUN_DIR / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    reviews_doc = load("review-records.json")
    evidence_doc = load("evidence.json")
    changes_doc = load("change-set.json")
    review = next(item for item in reviews_doc["records"] if item["marker_id"] == "M00868")
    if review["processing_status"] != "pending":
        raise RuntimeError("M00868 is no longer pending")
    original = copy.deepcopy(review["original_values"])
    evidence_id = "EVID_M00868_SOX2_MINUS_CORRECTED_20260908"
    excerpt = "17–22 pcw distal tip epithelium contained more cuboidal SOX2(cid:3), SOX9+, TPPP3+ cells, which co-expressed AT2 cell markers, SFTPC, and HTII-280 (Figures S1C–S1E)."
    locator = "DOI_10.1016_j.stem.2022.11.013.md lines 119-123; Figure 1 caption/Results"
    note = "正文窗口中的 SOX2(cid:3) 与同一文献中 SOX9(cid:3)/PDPN+ 的编码一致，表示 SOX2 阴性；因此与原 marker_polarity=low 一致。此前 source_context 中的 SOX2+ 为符号转换误读，已由正文窗口纠正。"
    if evidence_id not in {item["evidence_id"] for item in evidence_doc["evidence"]}:
        evidence_doc["evidence"].append({
            "evidence_id": evidence_id,
            "paper_id": review["paper_id"],
            "source_file": "DOI_10.1016_j.stem.2022.11.013.md",
            "source_sha256": None,
            "locator": locator,
            "verbatim_quote": excerpt,
            "verbatim_fragments": [excerpt],
            "support_map": {"M00868": {"gene_symbol": "SOX2", "task_no": 18, "locator": locator, "excerpt": excerpt, "semantic_note": note}},
            "interpretation": "纠正 source_context 的 SOX2 符号转换，按正文窗口保留 low/negative 方向；不修改正式 marker 字段。",
            "supports_review_ids": [review["review_id"]],
            "actual_checked_by": "GPT-5.6 Luna",
            "checked_at": DATE,
            "verification_status": "pdf_symbol_ambiguity_resolved_by_source_markdown_encoding",
        })
    review.setdefault("revision_history", []).append({
        "processing_status": review.get("processing_status"),
        "result": review.get("result"),
        "action": review.get("action"),
        "after_values": copy.deepcopy(review.get("after_values")),
        "evidence_ids": list(review.get("evidence_ids", [])),
        "evidence_excerpt": review.get("evidence_excerpt"),
        "evidence_locator": review.get("evidence_locator"),
        "reason": review.get("reason"),
        "revised_at": DATE,
        "revision_reason": "正文 source markdown 窗口解析并纠正 SOX2 符号编码。",
    })
    review.update({
        "processing_status": "completed",
        "result": "verified_keep",
        "action": "no_change",
        "after_values": original,
        "evidence_ids": [evidence_id],
        "checked_scope": [locator],
        "issues_found": ["source_context 中 SOX2+ 符号与正文编码不一致，已纠正为 SOX2(cid:3)"],
        "remaining_gaps": [],
        "reason": note,
        "related_marker_ids": [],
        "executed_by": "GPT-5.6 Luna",
        "reviewed_at": DATE,
        "evidence_excerpt": excerpt,
        "evidence_locator": locator,
        "evidence_binding_status": "pdf_symbol_ambiguity_resolved_by_source_markdown_encoding",
        "semantic_review": {
            "status": "verified_keep_no_change",
            "method": "source_markdown_symbol_encoding_resolution",
            "checks": [
                "目标基因 SOX2 在正文窗口中出现",
                "目标细胞为 17–22 pcw distal tip epithelium",
                "SOX2(cid:3) 与原 low 方向一致",
                "用同文同符号编码交叉确认，不借用其他基因方向",
            ],
            "semantic_note": note,
        },
    })
    expected_start_sha = changes_doc["changes"][0]["expected_start_sha256"]
    changes_doc["changes"].append({
        "change_id": f"VERIFY:M00868:{BATCH_ID}",
        "review_id": review["review_id"],
        "marker_id": "M00868",
        "operation": "no_change",
        "before_values": original,
        "after_values": original,
        "evidence_ids": [evidence_id],
        "reason": note,
        "target_marker_id": None,
        "archive_destination": None,
        "executor": "GPT-5.6 Luna",
        "decided_at": DATE,
        "expected_start_sha256": expected_start_sha,
    })
    summary = reviews_doc["summary"]
    summary["processing_status_counts"] = {
        "completed": sum(item["processing_status"] == "completed" for item in reviews_doc["records"]),
        "pending": sum(item["processing_status"] == "pending" for item in reviews_doc["records"]),
    }
    summary["result_counts"] = dict(Counter(item["result"] for item in reviews_doc["records"]))
    summary["known_batch_scope"] = sorted(item["marker_id"] for item in reviews_doc["records"] if item["processing_status"] == "completed")
    changes_doc["change_count"] = len(changes_doc["changes"])
    changes_doc["latest_batch"] = {"name": "M00868 SOX2 symbol ambiguity resolution", "batch_id": BATCH_ID, "completed_records": 1, "held_pending_records": 0}
    save("review-records.json", reviews_doc)
    save("evidence.json", evidence_doc)
    save("change-set.json", changes_doc)
    print(json.dumps({"completed": summary["processing_status_counts"]["completed"], "pending": summary["processing_status_counts"]["pending"], "change_count": changes_doc["change_count"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
