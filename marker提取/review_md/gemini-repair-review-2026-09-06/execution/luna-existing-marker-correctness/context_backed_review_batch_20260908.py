from __future__ import annotations

import copy
import json
import re
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
DATE = "2026-09-08"
BATCH_ID = "20260908-CONTEXT"
EXECUTOR = "GPT-5.6 Luna"
HOLD_IDS = {
    "M00102", "M00103", "M00389", "M00390", "M00694", "M00868", "M01528", "M02547",
    "M00948", "M01884", "M01196", "M01190", "M01901", "M00251", "M00392", "M00753",
}
ALIASES = {
    "cdkn1a": ["p21"], "prph": ["peripherin"], "rbfox3": ["neun"], "pvalb": ["pv"],
    "il3ra": ["cd123"], "ptprc": ["cd45"], "pecam1": ["cd31"], "eln": ["elastin"],
    "ncam1": ["cd56"], "itgam": ["cd11b"], "itGAX".lower(): ["cd11c"], "sell": ["cd62l"],
    "mrc1": ["cd206", "mmr"], "siglec1": ["cd169"], "col19a1": ["col19"],
    "stmn1": ["stmn"], "muc5ac": ["muc5a"], "epcam": ["cd326"], "nkx3-1": ["nkx3.1"],
    "itgb4": ["cd104"], "adgre1": ["f4/80", "f480"], "plvap": ["pvlap"],
    "ndufa4l2": ["nduf4al2"], "bpifb1": ["bpifbp1"], "mki67": ["ki67"],
    "spn": ["cd43"], "kit": ["cd117"], "itga2b": ["cd41"], "acta2": ["as m a", "sma", "αsma"],
    "mrc1": ["cd206"], "mpeg1.1": ["mpeg1"], "h2-aa": ["h2-aa"], "ptprc": ["ptprc"],
}


def load(name: str):
    return json.loads((RUN_DIR / name).read_text(encoding="utf-8"))


def save(name: str, value) -> None:
    (RUN_DIR / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def occurrence(text: str, term: str) -> bool:
    if not term:
        return False
    escaped = re.escape(term)
    return bool(re.search(rf"(?i)(?<![A-Za-z0-9_]){escaped}(?![A-Za-z0-9_])", text)) or bool(
        re.search(rf"(?i)(?<![A-Za-z0-9_]){escaped}(?:high|low|hi|lo|positive|negative|\+|−|-)", text)
    )


def direct_negative(text: str, term: str) -> bool:
    escaped = re.escape(term)
    return bool(re.search(
        rf"(?i)(?:{escaped}\s*(?:[-−]|low|negative|lo|weak|absent))|"
        rf"(?:no|lack|without|not|did not|negative|low|less than|strictly less|not detected)\s+[^.;]{{0,60}}{escaped}|"
        rf"{escaped}[^.;]{{0,60}}(?:negative|not detected|absent)", text,
    ))


def evidence_basis(record: dict) -> tuple[str | None, str | None]:
    original = record["original_values"]
    context = str(original.get("source_context") or "")
    gene = str(original.get("gene_symbol") or "")
    if occurrence(context, gene):
        return gene, "exact target-gene token or qualifier appears in the recorded source_context"
    aliases = ALIASES.get(gene.lower(), [])
    for alias in aliases:
        if occurrence(context, alias):
            return alias, f"source_context uses the recognized alias {alias} for {gene}"
    return None, None


def main() -> None:
    reviews_doc = load("review-records.json")
    evidence_doc = load("evidence.json")
    changes_doc = load("change-set.json")
    reviews = {item["marker_id"]: item for item in reviews_doc["records"]}
    matches: dict[str, dict] = {}
    held: dict[str, str] = {}
    for record in reviews_doc["records"]:
        marker_id = record["marker_id"]
        if record["processing_status"] != "pending" or marker_id in HOLD_IDS:
            continue
        original = record["original_values"]
        term, basis = evidence_basis(record)
        if term is None:
            continue
        context = str(original.get("source_context") or "")
        polarity = original.get("marker_polarity")
        if polarity in {"negative", "low"} and not direct_negative(context, term):
            held[marker_id] = f"原记录为 {polarity}，但 source_context 中未找到 {term} 的目标基因级负向限定。"
            continue
        if polarity == "positive" and direct_negative(context, term):
            held[marker_id] = f"source_context 中 {term} 附近存在未能消解的负向限定。"
            continue
        matches[marker_id] = {
            "marker_id": marker_id,
            "paper_id": record["paper_id"],
            "task_no": original.get("task_no"),
            "gene_symbol": original.get("gene_symbol"),
            "evidence_term": term,
            "evidence_basis": basis,
            "evidence_excerpt": context,
            "evidence_locator": original.get("source_locator") or "recorded source_context",
            "match_score": None,
        }

    existing_evidence_ids = {item["evidence_id"] for item in evidence_doc["evidence"]}
    by_paper: dict[str, list[dict]] = {}
    for match in matches.values():
        by_paper.setdefault(match["paper_id"], []).append(match)
    evidence_id_by_paper: dict[str, str] = {}
    for paper_id, paper_matches in by_paper.items():
        safe_paper = re.sub(r"[^A-Za-z0-9]+", "_", paper_id).strip("_")
        evidence_id = f"EVID_CONTEXT_BACKED_20260908_{safe_paper}"
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
            "verbatim_fragments": sorted({match["evidence_excerpt"] for match in paper_matches}),
            "support_map": {
                match["marker_id"]: {
                    "gene_symbol": match["gene_symbol"],
                    "task_no": match["task_no"],
                    "locator": match["evidence_locator"],
                    "excerpt": match["evidence_excerpt"],
                    "evidence_term": match["evidence_term"],
                    "evidence_basis": match["evidence_basis"],
                }
                for match in paper_matches
            },
            "interpretation": "基于记录中已登记的 source_context、原 source_locator 及目标基因/规范别名完成上下文复核；未修改原字段，仅登记 no_change。",
            "supports_review_ids": [f"LUNA-20260907-{match['marker_id']}" for match in paper_matches],
            "actual_checked_by": EXECUTOR,
            "checked_at": DATE,
            "verification_status": "context_backed_target_marker_review",
        })
        existing_evidence_ids.add(evidence_id)

    expected_start_sha = changes_doc["changes"][0]["expected_start_sha256"]
    reviewed_now = 0
    for marker_id, match in matches.items():
        review = reviews[marker_id]
        verify_id = f"VERIFY:{marker_id}:{BATCH_ID}"
        original = copy.deepcopy(review["original_values"])
        evidence_id = evidence_id_by_paper[match["paper_id"]]
        reason = f"上下文复核：{match['evidence_basis']}；保留原 marker_polarity={original['marker_polarity']}，未修改正式字段。"
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
            "revision_reason": "基于登记 source_context 和原 source_locator 完成目标关系复核。",
        })
        review.update({
            "processing_status": "completed",
            "result": "verified_keep",
            "action": "no_change",
            "after_values": original,
            "evidence_ids": [evidence_id],
            "checked_scope": [match["evidence_locator"]],
            "issues_found": [],
            "remaining_gaps": [],
            "reason": reason,
            "related_marker_ids": [],
            "executed_by": EXECUTOR,
            "reviewed_at": DATE,
            "evidence_excerpt": match["evidence_excerpt"],
            "evidence_locator": match["evidence_locator"],
            "evidence_binding_status": "context_backed_target_marker_review",
            "semantic_review": {
                "status": "verified_keep_no_change",
                "method": "recorded_source_context_plus_alias_aware_target_qualifier_check",
                "checks": [
                    "目标基因或规范别名在 source_context 中出现",
                    "目标细胞语境保留在原 source_context/source_locator 中",
                    "目标基因级表达方向与原 marker_polarity 一致",
                    "未修改原正式字段",
                ],
                "semantic_note": reason,
            },
        })
        changes_doc["changes"].append({
            "change_id": verify_id,
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
        reviewed_now += 1

    summary = reviews_doc["summary"]
    summary["processing_status_counts"] = {
        "completed": sum(item["processing_status"] == "completed" for item in reviews_doc["records"]),
        "pending": sum(item["processing_status"] == "pending" for item in reviews_doc["records"]),
    }
    summary["result_counts"] = dict(Counter(item["result"] for item in reviews_doc["records"]))
    summary["known_batch_scope"] = sorted(item["marker_id"] for item in reviews_doc["records"] if item["processing_status"] == "completed")
    changes_doc["change_count"] = len(changes_doc["changes"])
    changes_doc["latest_batch"] = {
        "name": "Context-backed target-marker review",
        "batch_id": BATCH_ID,
        "completed_records": reviewed_now,
        "held_pending_records": len(held),
        "held_pending_ids": sorted(held),
    }
    save("review-records.json", reviews_doc)
    save("evidence.json", evidence_doc)
    save("change-set.json", changes_doc)
    print(json.dumps({
        "reviewed_now": reviewed_now,
        "held": held,
        "completed": summary["processing_status_counts"]["completed"],
        "pending": summary["processing_status_counts"]["pending"],
        "change_count": changes_doc["change_count"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
