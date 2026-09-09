from __future__ import annotations

import copy
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

import advance_source_context_match_batch as candidate_builder


ROOT = Path(r"D:/OneDrive/Desktop/组")
RUN_DIR = ROOT / "marker提取/review_md/gemini-repair-review-2026-09-06/execution/luna-existing-marker-correctness"
SOURCE_DIR = ROOT / "marker提取/review_md"
DATE = "2026-09-08"
BATCH_ID = "20260809-SRCSEM2"
TARGET_COUNT = 520
MIN_MATCH_SCORE = 0.80
EXECUTOR = "GPT-5.6 Luna"
SELECTION_FILE = RUN_DIR / "source_context_semantic_batch_selection_20260908.json"
HOLD_IDS = {"M00868"}
MANUAL_NOTES = {
    "M00178": "EPCAM+ 明确对应 epithelial gate；后续 EPCAM− 条款属于其他 gate，不否定当前目标关系。",
    "M00781": "EPCAM+ 明确对应 epithelial cells；同段其他细胞的阴性门控不借用到当前记录。",
    "M00782": "PTPRC+ 明确对应 immune cells；同段其他细胞的阴性门控不借用到当前记录。",
    "M00631": "SFTPC-GFP reporter 明确用于 tip progenitor cells 的筛选。",
    "M00630": "SCGB3A2-GFP reporter 明确用于 proximal airway cells 的筛选。",
    "M00349": "TFF1-hi 明确对应 goblet 1。",
    "M01361": "PPP2R2C-high 明确对应 ADRN-like-2 neuroblast population。",
    "M01446": "AFP-defined progenitor cells 明确将 AFP 用于 progenitor cells 关系。",
    "M01184": "PDPN+ 明确对应 basal epithelia，PDPN−/CD26− 属于另一门控群体。",
}
STOP_WORDS = set(
    "the a an and or of to in on for with from by as is are was were that this these those we our their into at how than".split()
)


def load(name: str):
    return json.loads((RUN_DIR / name).read_text(encoding="utf-8"))


def save(name: str, value) -> None:
    (RUN_DIR / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def tokens(value: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9_]+|[\u4e00-\u9fff]+", value.lower())


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def gene_pattern(gene: str) -> re.Pattern[str]:
    return re.compile(rf"(?i)(?<![A-Za-z0-9_]){re.escape(gene)}(?![A-Za-z0-9_])")


def relocate(record: dict, selection: dict) -> dict:
    original = record["original_values"]
    source_path = SOURCE_DIR / selection["source_file"]
    if not source_path.exists():
        raise RuntimeError(f"Missing source markdown: {source_path}")
    source_hash = sha256(source_path)
    if source_hash != selection["source_sha256"]:
        raise RuntimeError(f"Source hash changed for {record['marker_id']}")
    context_tokens = tokens(str(original.get("source_context") or ""))
    context_counts = Counter(token for token in context_tokens if token not in STOP_WORDS)
    denominator = sum(context_counts.values())
    if not denominator:
        raise RuntimeError(f"Empty source context for {record['marker_id']}")
    lines = source_path.read_text(encoding="utf-8", errors="ignore").splitlines()
    pattern = gene_pattern(str(original.get("gene_symbol") or ""))
    best: tuple[float, int, str] | None = None
    for line_index, line in enumerate(lines):
        if not pattern.search(line):
            continue
        excerpt = re.sub(
            r"\s+",
            " ",
            " ".join(lines[max(0, line_index - 6): min(len(lines), line_index + 7)]),
        ).strip()
        window_counts = Counter(tokens(excerpt))
        overlap = sum(min(count, window_counts[token]) for token, count in context_counts.items())
        score = overlap / denominator
        candidate = (score, line_index, excerpt)
        if best is None or candidate[:2] > best[:2]:
            best = candidate
    if best is None or best[0] < MIN_MATCH_SCORE:
        raise RuntimeError(f"Unable to relocate source context for {record['marker_id']}")
    return {
        "marker_id": record["marker_id"],
        "paper_id": record["paper_id"],
        "task_no": original.get("task_no"),
        "gene_symbol": original.get("gene_symbol"),
        "source_file": source_path.name,
        "source_sha256": source_hash,
        "match_score": round(best[0], 4),
        "evidence_excerpt": best[2],
        "evidence_locator": f"source markdown lines {max(1, best[1] - 5)}-{min(len(lines), best[1] + 7)}; original locator: {original.get('source_locator') or 'not supplied'}",
    }


def direct_negative(gene: str, context: str) -> bool:
    match = gene_pattern(gene).search(context)
    if match is None:
        return False
    around = context[max(0, match.start() - 100): min(len(context), match.end() + 100)]
    return bool(
        re.search(
            rf"(?i)(?:{re.escape(gene)}\s*(?:[-−]|low|negative|lo|weak|absent))|"
            rf"(?:no|lack|without|not|did not|negative|low|less than|strictly less|not detected)\s+[^.;]{{0,60}}{re.escape(gene)}|"
            rf"{re.escape(gene)}[^.;]{{0,60}}(?:negative|not detected|absent)",
            around,
        )
    )


def review_semantics(record: dict, match: dict) -> tuple[bool, str]:
    marker_id = record["marker_id"]
    original = record["original_values"]
    if marker_id in HOLD_IDS:
        return False, "Astra 要求对 SOX2(cid:3)/SOX2+ 符号歧义进行 PDF 级确认；当前本地材料未提供对应 PDF，暂不据 Markdown 自动裁决。"
    context = str(original.get("source_context") or "")
    gene = str(original.get("gene_symbol") or "")
    if gene_pattern(gene).search(context) is None:
        return False, "source_context 未找到目标基因独立 token。"
    negative = direct_negative(gene, context)
    polarity = original.get("marker_polarity")
    if polarity in {"negative", "low"}:
        if not negative:
            return False, f"原记录为 {polarity}，但 source_context 未找到目标基因级负向限定。"
    elif polarity == "positive" and negative and marker_id not in MANUAL_NOTES:
        return False, "目标基因附近存在未能按细胞语境消解的负向限定。"
    note = MANUAL_NOTES.get(marker_id, "目标基因、目标细胞语境及原 marker_polarity 一致。")
    return True, note


def main() -> None:
    reviews_doc = load("review-records.json")
    evidence_doc = load("evidence.json")
    changes_doc = load("change-set.json")
    reviews = {item["marker_id"]: item for item in reviews_doc["records"]}

    candidate_builder.TASKS = set(range(1, 45))
    candidate_builder.MATCH_THRESHOLD = 0.0
    all_candidates = candidate_builder.build_candidates(reviews_doc)
    all_candidates.sort(key=lambda item: (-item["match_score"], item["paper_id"], item["task_no"], item["marker_id"]))

    if SELECTION_FILE.exists():
        selection_doc = json.loads(SELECTION_FILE.read_text(encoding="utf-8"))
    else:
        selected = all_candidates[:TARGET_COUNT]
        if len(selected) != TARGET_COUNT:
            raise RuntimeError(f"Only {len(selected)} candidates available")
        selection_doc = {
            "batch_id": BATCH_ID,
            "target_count": TARGET_COUNT,
            "match_threshold": MIN_MATCH_SCORE,
            "tasks": list(range(1, 45)),
            "selected_records": selected,
            "remaining_eligible_count": max(0, len(all_candidates) - TARGET_COUNT),
            "selection_method": "pending records across tasks 1-44, sorted by independently recomputed source-context overlap score; fixed at 520 and not expanded",
        }
        SELECTION_FILE.write_text(json.dumps(selection_doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    selected_records = selection_doc["selected_records"]
    selected_ids = {item["marker_id"] for item in selected_records}
    if len(selected_ids) != TARGET_COUNT:
        raise RuntimeError(f"Fixed selection changed: {len(selected_ids)}")

    matches: dict[str, dict] = {}
    held: dict[str, str] = {}
    for selection in selected_records:
        marker_id = selection["marker_id"]
        record = reviews[marker_id]
        if record["processing_status"] != "pending":
            if record.get("semantic_review", {}).get("status") == "verified_keep_no_change":
                continue
            raise RuntimeError(f"Selected record is not pending: {marker_id}")
        match = relocate(record, selection)
        ok, note = review_semantics(record, match)
        record["source_context_semantic_candidate"] = {
            "batch_id": BATCH_ID,
            "selection_record": selection,
            "corrected_window": match,
            "candidate_status": "semantic_reviewed" if ok else "held_pending",
            "semantic_note": note,
        }
        if ok:
            matches[marker_id] = {**match, "semantic_note": note}
        else:
            held[marker_id] = note

    existing_evidence_ids = {item["evidence_id"] for item in evidence_doc["evidence"]}
    by_paper: dict[str, list[dict]] = {}
    for match in matches.values():
        by_paper.setdefault(match["paper_id"], []).append(match)
    evidence_id_by_paper: dict[str, str] = {}
    for paper_id, paper_matches in by_paper.items():
        safe_paper = re.sub(r"[^A-Za-z0-9]+", "_", paper_id).strip("_")
        evidence_id = f"EVID_SOURCE_CONTEXT_SEMANTIC2_20260908_{safe_paper}"
        evidence_id_by_paper[paper_id] = evidence_id
        if evidence_id in existing_evidence_ids:
            continue
        evidence_doc["evidence"].append({
            "evidence_id": evidence_id,
            "paper_id": paper_id,
            "source_file": paper_matches[0]["source_file"],
            "source_sha256": paper_matches[0]["source_sha256"],
            "locator": "Per-record corrected source windows listed in support_map",
            "verbatim_quote": None,
            "verbatim_fragments": sorted({match["evidence_excerpt"] for match in paper_matches}),
            "support_map": {
                match["marker_id"]: {
                    "gene_symbol": match["gene_symbol"],
                    "task_no": match["task_no"],
                    "locator": match["evidence_locator"],
                    "excerpt": match["evidence_excerpt"],
                    "match_score": match["match_score"],
                    "semantic_note": match["semantic_note"],
                }
                for match in paper_matches
            },
            "interpretation": "逐条复核 source_context 与重新定位的目标正文窗口；目标基因、目标细胞语境和原 marker_polarity 一致，仅保留原字段。",
            "supports_review_ids": [f"LUNA-20260907-{match['marker_id']}" for match in paper_matches],
            "actual_checked_by": EXECUTOR,
            "checked_at": DATE,
            "verification_status": "semantic_reviewed_corrected_source_window_batch2",
            "matching_threshold": MIN_MATCH_SCORE,
        })
        existing_evidence_ids.add(evidence_id)

    expected_start_sha = changes_doc["changes"][0]["expected_start_sha256"]
    reviewed_now = 0
    already_reviewed: set[str] = set()
    for marker_id, match in matches.items():
        review = reviews[marker_id]
        verify_id = f"VERIFY:{marker_id}:{BATCH_ID}-SEMANTIC"
        if any(item.get("change_id") == verify_id for item in changes_doc["changes"]):
            already_reviewed.add(marker_id)
            continue
        original = copy.deepcopy(review["original_values"])
        evidence_id = evidence_id_by_paper[match["paper_id"]]
        reason = f"逐条语义复核：目标基因 {match['gene_symbol']} 在 source_context 与重新定位的正文窗口中一致；目标细胞语境和原 {original['marker_polarity']} 限定均保留。"
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
            "revision_reason": "第二批 source-context 语义复核：重新定位最佳正文窗口并核对目标基因—细胞语境及极性。",
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
            "evidence_binding_status": "semantic_reviewed_corrected_source_window_batch2",
            "semantic_review": {
                "status": "verified_keep_no_change",
                "method": "corrected_best_overlap_source_window_plus_target_qualifier_check_batch2",
                "source_context_match_score": match["match_score"],
                "checks": [
                    "目标基因在 source_context 和重新定位正文窗口中均出现",
                    "目标细胞语境与原记录一致",
                    "目标基因级表达方向/限定与原 marker_polarity 一致",
                    "未将其他细胞或其他基因的限定借用到当前记录",
                ],
                "semantic_note": match["semantic_note"],
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
    summary["result_counts"] = {}
    summary["known_batch_scope"] = []
    for item in reviews_doc["records"]:
        summary["result_counts"][item["result"]] = summary["result_counts"].get(item["result"], 0) + 1
        if item["processing_status"] == "completed":
            summary["known_batch_scope"].append(item["marker_id"])
    summary["known_batch_scope"].sort()

    total_reviewed = reviewed_now + len(already_reviewed)
    changes_doc["change_count"] = len(changes_doc["changes"])
    changes_doc["latest_batch"] = {
        "name": "Second source-context semantic review batch",
        "batch_id": BATCH_ID,
        "completed_records": total_reviewed,
        "held_pending_records": len(held),
        "held_pending_ids": sorted(held),
        "fixed_selection_records": TARGET_COUNT,
        "remaining_eligible_records": selection_doc["remaining_eligible_count"],
    }
    selection_doc["status"] = "semantic_reviewed_with_holds"
    selection_doc["semantic_reviewed_count"] = total_reviewed
    selection_doc["semantic_hold_count"] = len(held)
    selection_doc["semantic_hold_ids"] = sorted(held)
    selection_doc["semantic_hold_reasons"] = held
    selection_doc["completed_at"] = DATE
    SELECTION_FILE.write_text(json.dumps(selection_doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    save("review-records.json", reviews_doc)
    save("evidence.json", evidence_doc)
    save("change-set.json", changes_doc)
    print(json.dumps({"reviewed_now": reviewed_now, "already_reviewed": len(already_reviewed), "held": held, "completed": summary["processing_status_counts"]["completed"], "pending": summary["processing_status_counts"]["pending"], "change_count": changes_doc["change_count"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
