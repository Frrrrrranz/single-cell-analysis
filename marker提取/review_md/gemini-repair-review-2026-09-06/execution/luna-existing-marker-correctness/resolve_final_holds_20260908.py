from __future__ import annotations

import copy
import json
import re
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
DATE = "2026-09-08"
BATCH_ID = "20260908-FINAL-HOLDS"
EXECUTOR = "GPT-5.6 Luna"
IDS = {
    "M00102", "M00103", "M00251", "M00389", "M00390", "M00392", "M00694", "M00753",
    "M00948", "M01190", "M01196", "M01528", "M01884", "M01901", "M02547",
}
NOTES = {
    "M00102": "source_context 明确要求 MRC1 和 CD247 在纯 microglia 筛选中 normalized expression strictly less than 1；CD247 为目标级 negative。",
    "M00103": "source_context 明确要求 MRC1 和 CD247 在纯 microglia 筛选中 normalized expression strictly less than 1；MRC1 为目标级 negative。",
    "M00251": "source_context 明确将 CCL21、CCL19 作为 IR-Ven-Peri markers，并与 ACKR1 邻近的静脉血管语境区分开；目标 CCL19 为 positive。",
    "M00389": "source_context 将 mono CXCL10+ 作为单核细胞 distinct cluster 的高表达 marker；目标细胞与基因标签直接一致。",
    "M00390": "source_context 将 mono GPBAR1+ 作为单核细胞 distinct cluster 的高表达 marker；目标细胞与基因标签直接一致。",
    "M00392": "source_context 明确写出 Cell type label Mono IL6+ includes IL6；目标关系为 positive。",
    "M00694": "source_context 将 SCGB3A1 与 SCGB3A2、MUC5AC 一并列为 secretory cell markers；目标关系为 positive。",
    "M00753": "source_context 明确区分 lung goblet cells 的 MUC5AC+/MUC5B+ 与 SMG mucous 的 MUC5AC-/MUC5B+；当前目标是 lung goblet cells，按目标细胞语境绑定 positive。",
    "M00948": "source_context 直接写出 MUC5AC-expressing goblet，目标关系为 positive。",
    "M01190": "source_context 同时说明 KRT13+ cells 不与 ACPP 共表达，并在同一段将 ACPP 作为 prostate secretory luminal cell marker；negative 限定属于 KRT13+ 细胞，不否定当前目标。",
    "M01196": "source_context 以 Trop2（TACSTD2）作为 mouse urethral luminal epithelial surface marker；目标关系为 positive。",
    "M01528": "source_context 直接将 Itgb4 与 Slc2a1 列为 perineurial fibroblast markers。",
    "M01884": "source_context 直接将 Slit2 列为 myelinating Schwann cell unique gene，并说明 Slit2-high population。",
    "M01901": "source_context 直接写出 MRGPRX1 selectively localized to H10 neurons；目标 H10 关系为 positive。",
    "M02547": "source_context 明确 H5 cells 为 NTRK1 negative、NTRK2 strongly positive；目标 NTRK2 为 positive。",
}


def load(name: str):
    return json.loads((RUN_DIR / name).read_text(encoding="utf-8"))


def save(name: str, value) -> None:
    (RUN_DIR / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    reviews_doc = load("review-records.json")
    evidence_doc = load("evidence.json")
    changes_doc = load("change-set.json")
    reviews = {item["marker_id"]: item for item in reviews_doc["records"]}
    selected = [reviews[marker_id] for marker_id in sorted(IDS)]
    if any(item["processing_status"] != "pending" for item in selected):
        raise RuntimeError("A final hold record is no longer pending")

    existing_evidence_ids = {item["evidence_id"] for item in evidence_doc["evidence"]}
    by_paper: dict[str, list[dict]] = {}
    for review in selected:
        by_paper.setdefault(review["paper_id"], []).append(review)
    evidence_id_by_paper: dict[str, str] = {}
    for paper_id, items in by_paper.items():
        safe_paper = re.sub(r"[^A-Za-z0-9]+", "_", paper_id).strip("_")
        evidence_id = f"EVID_FINAL_HOLD_RESOLUTION_20260908_{safe_paper}"
        evidence_id_by_paper[paper_id] = evidence_id
        if evidence_id in existing_evidence_ids:
            continue
        evidence_doc["evidence"].append({
            "evidence_id": evidence_id,
            "paper_id": paper_id,
            "source_file": None,
            "source_sha256": None,
            "locator": "Per-record source_context and original source_locator listed in support_map",
            "verbatim_quote": None,
            "verbatim_fragments": sorted({item["original_values"].get("source_context") or "" for item in items}),
            "support_map": {
                item["marker_id"]: {
                    "gene_symbol": item["original_values"].get("gene_symbol"),
                    "task_no": item["original_values"].get("task_no"),
                    "locator": item["original_values"].get("source_locator"),
                    "excerpt": item["original_values"].get("source_context"),
                    "semantic_note": NOTES[item["marker_id"]],
                }
                for item in items
            },
            "interpretation": "对上一批 hold 逐条补充目标基因级语义解释；仅 M00868 仍保留 PDF/SOX2 符号 hold。",
            "supports_review_ids": [item["review_id"] for item in items],
            "actual_checked_by": EXECUTOR,
            "checked_at": DATE,
            "verification_status": "final_hold_target_level_resolution",
        })
        existing_evidence_ids.add(evidence_id)

    expected_start_sha = changes_doc["changes"][0]["expected_start_sha256"]
    for review in selected:
        marker_id = review["marker_id"]
        original = copy.deepcopy(review["original_values"])
        evidence_id = evidence_id_by_paper[review["paper_id"]]
        reason = NOTES[marker_id]
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
            "revision_reason": "逐条补充目标基因级方向、别名或目标细胞语境解释。",
        })
        review.update({
            "processing_status": "completed",
            "result": "verified_keep",
            "action": "no_change",
            "after_values": original,
            "evidence_ids": [evidence_id],
            "checked_scope": [original.get("source_locator") or "recorded source_context"],
            "issues_found": [],
            "remaining_gaps": [],
            "reason": reason,
            "related_marker_ids": [],
            "executed_by": EXECUTOR,
            "reviewed_at": DATE,
            "evidence_excerpt": original.get("source_context"),
            "evidence_locator": original.get("source_locator") or "recorded source_context",
            "evidence_binding_status": "final_hold_target_level_resolution",
            "semantic_review": {
                "status": "verified_keep_no_change",
                "method": "target_level_manual_resolution_of_prior_hold",
                "checks": [
                    "目标基因或规范别名在 source_context 中可定位",
                    "目标细胞语境与目标基因方向已单独解释",
                    "未将相邻细胞的限定借用到当前记录",
                ],
                "semantic_note": reason,
            },
        })
        changes_doc["changes"].append({
            "change_id": f"VERIFY:{marker_id}:{BATCH_ID}",
            "review_id": review["review_id"],
            "marker_id": marker_id,
            "operation": "no_change",
            "before_values": original,
            "after_values": original,
            "evidence_ids": [evidence_id],
            "reason": reason,
            "target_marker_id": None,
            "archive_destination": None,
            "executor": EXECUTOR,
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
    changes_doc["latest_batch"] = {
        "name": "Final target-level resolution of prior holds",
        "batch_id": BATCH_ID,
        "completed_records": len(selected),
        "held_pending_records": 1,
        "held_pending_ids": ["M00868"],
    }
    save("review-records.json", reviews_doc)
    save("evidence.json", evidence_doc)
    save("change-set.json", changes_doc)
    print(json.dumps({
        "resolved": len(selected),
        "remaining_pending": summary["processing_status_counts"]["pending"],
        "remaining_pending_ids": [item["marker_id"] for item in reviews_doc["records"] if item["processing_status"] == "pending"],
        "change_count": changes_doc["change_count"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
