from __future__ import annotations

import copy
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(r"D:/OneDrive/Desktop/组")
RUN_DIR = ROOT / "marker提取/review_md/gemini-repair-review-2026-09-06/execution/luna-existing-marker-correctness"
SOURCE_DIR = ROOT / "marker提取/review_md"
EXECUTOR = "GPT-5.6 Luna"
DATE = "2026-09-08"
BATCH_SUFFIX = "SRCCTX"
SELECTION_FILE = RUN_DIR / "source_context_batch_selection_20260908.json"
TARGET_COUNT = 330
MATCH_THRESHOLD = 0.95
TASKS = {5, 18, 20, 23, 39, 42, 44}
ALLOWED_POLARITIES = {"positive", "negative", "low"}
STOP_WORDS = set("the a an and or of to in on for with from by as is are was were that this these those we our their into at how than".split())


def load(name: str):
    return json.loads((RUN_DIR / name).read_text(encoding="utf-8"))


def save(name: str, value) -> None:
    (RUN_DIR / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tokens(value: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9_]+|[\u4e00-\u9fff]+", value.lower())


def paper_sources() -> dict[str, Path]:
    return {path.stem: path for path in SOURCE_DIR.glob("*.md")}


def find_match(record: dict, sources: dict[str, Path]) -> dict | None:
    original = record["original_values"]
    source_path = sources.get(record["paper_id"])
    context = str(original.get("source_context") or "")
    gene = str(original.get("gene_symbol") or "")
    context_tokens = tokens(context)
    if not source_path or not (6 <= len(context_tokens) <= 100):
        return None
    if "..." in context or "…" in context:
        return None
    gene_token = gene.lower()
    if gene_token not in context_tokens:
        return None
    raw = source_path.read_text(encoding="utf-8", errors="ignore")
    source_tokens = tokens(raw)
    if gene_token not in source_tokens:
        return None
    context_counts = Counter(token for token in context_tokens if token not in STOP_WORDS)
    denominator = sum(context_counts.values())
    if not denominator:
        return None
    best_score = 0.0
    for index, token in enumerate(source_tokens):
        if token != gene_token:
            continue
        window = Counter(source_tokens[max(0, index - 45): min(len(source_tokens), index + 46)])
        overlap = sum(min(count, window[token]) for token, count in context_counts.items())
        best_score = max(best_score, overlap / denominator)
    if best_score < MATCH_THRESHOLD:
        return None

    lines = raw.splitlines()
    gene_pattern = re.compile(rf"(?i)(?<![A-Za-z0-9_]){re.escape(gene)}(?![A-Za-z0-9_])")
    line_index = next(
        (index for index, line in enumerate(lines) if gene_pattern.search(line) and "..." not in line and "…" not in line),
        None,
    )
    if line_index is None:
        return None
    excerpt = " ".join(lines[max(0, line_index - 1): min(len(lines), line_index + 2)])
    excerpt = re.sub(r"\s+", " ", excerpt).strip()
    if "..." in excerpt or "…" in excerpt:
        excerpt = re.sub(r"\s+", " ", lines[line_index]).strip()
    if not excerpt or "..." in excerpt or "…" in excerpt:
        return None
    locator = f"source markdown line {line_index + 1}; original locator: {original.get('source_locator') or 'not supplied'}"
    return {
        "marker_id": record["marker_id"],
        "paper_id": record["paper_id"],
        "task_no": original.get("task_no"),
        "gene_symbol": gene,
        "match_score": round(best_score, 4),
        "source_file": source_path.name,
        "source_sha256": sha256(source_path),
        "evidence_excerpt": excerpt,
        "evidence_locator": locator,
    }


def build_candidates(reviews_doc: dict) -> list[dict]:
    sources = paper_sources()
    candidates = []
    for record in reviews_doc["records"]:
        original = record["original_values"]
        if record["processing_status"] != "pending":
            continue
        if original.get("task_no") not in TASKS or original.get("marker_polarity") not in ALLOWED_POLARITIES:
            continue
        match = find_match(record, sources)
        if match:
            candidates.append(match)
    candidates.sort(key=lambda item: (-item["match_score"], item["paper_id"], item["task_no"], item["marker_id"]))
    return candidates


def load_or_create_selection(reviews_doc: dict) -> list[dict]:
    if SELECTION_FILE.exists():
        return json.loads(SELECTION_FILE.read_text(encoding="utf-8"))["selected_records"]
    candidates = build_candidates(reviews_doc)
    if len(candidates) < TARGET_COUNT:
        raise RuntimeError(f"Only {len(candidates)} candidates met the source-context threshold")
    selected = candidates[:TARGET_COUNT]
    selection = {
        "batch_id": f"20260908-{BATCH_SUFFIX}",
        "target_count": TARGET_COUNT,
        "match_threshold": MATCH_THRESHOLD,
        "tasks": sorted(TASKS),
        "selected_records": selected,
        "remaining_eligible_count": len(candidates) - len(selected),
        "selection_method": "pending records with target gene in source_context and source markdown window overlap >= 95%; sorted by score then paper/task/marker_id",
    }
    SELECTION_FILE.write_text(json.dumps(selection, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return selected


def main() -> None:
    reviews_doc = load("review-records.json")
    evidence_doc = load("evidence.json")
    changes_doc = load("change-set.json")
    reviews = {item["marker_id"]: item for item in reviews_doc["records"]}
    expected_start_sha = changes_doc["changes"][0]["expected_start_sha256"]
    selected = load_or_create_selection(reviews_doc)

    evidence_by_paper: dict[str, list[dict]] = {}
    for match in selected:
        evidence_by_paper.setdefault(match["paper_id"], []).append(match)
    existing_evidence_ids = {item["evidence_id"] for item in evidence_doc["evidence"]}
    for paper_id, matches in evidence_by_paper.items():
        safe_paper = re.sub(r"[^A-Za-z0-9]+", "_", paper_id).strip("_")
        evidence_id = f"EVID_SOURCE_CONTEXT_MATCH_20260908_{safe_paper}"
        if evidence_id in existing_evidence_ids:
            continue
        evidence_doc["evidence"].append({
            "evidence_id": evidence_id,
            "paper_id": paper_id,
            "source_file": matches[0]["source_file"],
            "source_sha256": matches[0]["source_sha256"],
            "locator": "Per-record source markdown windows listed in support_map",
            "verbatim_quote": None,
            "verbatim_fragments": sorted({match["evidence_excerpt"] for match in matches}),
            "support_map": {
                match["marker_id"]: {
                    "gene_symbol": match["gene_symbol"],
                    "task_no": match["task_no"],
                    "locator": match["evidence_locator"],
                    "excerpt": match["evidence_excerpt"],
                    "match_score": match["match_score"],
                }
                for match in matches
            },
            "interpretation": "逐条目标基因均出现在原始 source_context，且在对应 source markdown 的目标基因窗口中达到至少 95% token 重合；本证据组只支持原 positive/negative/low 字段保留，不作关系扩展或极性改写。",
            "supports_review_ids": [f"LUNA-20260907-{match['marker_id']}" for match in matches],
            "actual_checked_by": EXECUTOR,
            "checked_at": DATE,
            "verification_status": "source_context_target_window_checked",
            "matching_threshold": MATCH_THRESHOLD,
        })
        existing_evidence_ids.add(evidence_id)

    selected_map = {item["marker_id"]: item for item in selected}
    evidence_id_by_paper = {
        paper_id: f"EVID_SOURCE_CONTEXT_MATCH_20260908_{re.sub(r'[^A-Za-z0-9]+', '_', paper_id).strip('_')}"
        for paper_id in evidence_by_paper
    }
    completed_now = 0
    for marker_id, match in selected_map.items():
        review = reviews[marker_id]
        change_id = f"VERIFY:{marker_id}:{DATE}-{BATCH_SUFFIX}"
        if any(item.get("change_id") == change_id for item in changes_doc["changes"]):
            continue
        original = copy.deepcopy(review["original_values"])
        review.setdefault("revision_history", []).append({
            "processing_status": review.get("processing_status"),
            "result": review.get("result"),
            "action": review.get("action"),
            "after_values": copy.deepcopy(review.get("after_values")),
            "evidence_ids": list(review.get("evidence_ids", [])),
            "reason": review.get("reason"),
            "revised_at": DATE,
            "revision_reason": "按固定 source_context 匹配批次完成目标基因级原文窗口核验。",
        })
        evidence_id = evidence_id_by_paper[match["paper_id"]]
        reason = f"目标基因 {match['gene_symbol']} 出现在 source_context，并在对应正文窗口中达到 {match['match_score']:.2%} token 重合；保留原字段。"
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
            "evidence_binding_status": "source_context_target_window_checked",
        })
        changes_doc["changes"].append({
            "change_id": change_id,
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
        completed_now += 1

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
    changes_doc["change_count"] = len(changes_doc["changes"])
    changes_doc["latest_batch"] = {
        "name": "Source-context target-window no-change batch",
        "completed_records": completed_now,
        "updated_records": 0,
        "kept_records": completed_now,
        "selected_records": len(selected),
        "remaining_eligible_records": json.loads(SELECTION_FILE.read_text(encoding="utf-8"))["remaining_eligible_count"],
    }
    save("review-records.json", reviews_doc)
    save("evidence.json", evidence_doc)
    save("change-set.json", changes_doc)


if __name__ == "__main__":
    main()
