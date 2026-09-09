from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / "execution" / "luna-existing-marker-correctness"
REVIEW_MD = ROOT.parent
OUTPUT = Path(__file__).with_name("triage.json")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize(text: Any) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(text or "").lower())


def stable_rank(record: dict[str, Any]) -> str:
    return hashlib.sha256(record["review_id"].encode("utf-8")).hexdigest()


def source_path_for(record: dict[str, Any]) -> Path | None:
    paper_id = record.get("paper_id") or ""
    direct = REVIEW_MD / f"{paper_id}.md"
    if direct.exists():
        return direct
    source_file = str(record.get("original_values", {}).get("source_file") or "")
    candidates = [
        REVIEW_MD / Path(source_file).name,
        Path.cwd() / source_file,
    ]
    for candidate in candidates:
        if candidate.exists() and candidate.suffix.lower() == ".md":
            return candidate
    return None


def text_checks(record: dict[str, Any], source_cache: dict[Path, tuple[str, str]]) -> dict[str, Any]:
    source_path = source_path_for(record)
    original = record.get("original_values", {})
    context = str(original.get("source_context") or "")
    gene = str(original.get("gene_symbol") or original.get("original_symbol") or "")
    cell = str(original.get("subtype") or original.get("cell_type") or "")
    if source_path is None:
        return {
            "source_path": None,
            "source_exists": False,
            "context_exact": False,
            "context_normalized": False,
            "gene_present": False,
            "cell_token_present": False,
        }
    if source_path not in source_cache:
        text = source_path.read_text(encoding="utf-8", errors="replace")
        source_cache[source_path] = (text, normalize(text))
    text, norm_text = source_cache[source_path]
    cell_tokens = [token for token in re.findall(r"[A-Za-z0-9]+", cell) if len(token) >= 4]
    return {
        "source_path": str(source_path),
        "source_exists": True,
        "context_exact": bool(context and context in text),
        "context_normalized": bool(context and normalize(context) in norm_text),
        "gene_present": bool(gene and normalize(gene) in norm_text),
        "cell_token_present": any(normalize(token) in norm_text for token in cell_tokens),
    }


def stratified_inherited_sample(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    selected: dict[str, dict[str, Any]] = {}
    by_paper: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_paper[record.get("paper_id") or ""].append(record)
        polarity = record.get("original_values", {}).get("marker_polarity")
        species = record.get("original_values", {}).get("species")
        if polarity != "positive" or species != "human":
            selected[record["review_id"]] = record

    for paper_records in by_paper.values():
        quota = len(paper_records) if len(paper_records) <= 5 else 5
        if len(paper_records) >= 100:
            quota = 25
        elif len(paper_records) >= 20:
            quota = 12
        strata: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for record in paper_records:
            evidence_type = str(record.get("original_values", {}).get("evidence_type") or "unknown")
            strata[evidence_type].append(record)
        for values in strata.values():
            values.sort(key=stable_rank)
            selected[values[0]["review_id"]] = values[0]
        for record in sorted(paper_records, key=stable_rank):
            if sum(1 for item in selected.values() if item.get("paper_id") == record.get("paper_id")) >= quota:
                break
            selected[record["review_id"]] = record
    return sorted(selected.values(), key=lambda item: (item.get("paper_id") or "", item["review_id"]))


def stratified_target_bound_sample(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_paper: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        if record.get("action") == "no_change" and record.get("evidence_binding_status") not in {
            None,
            "",
            "prior_quick_consistency_inherited_with_documented_limit",
        }:
            by_paper[record.get("paper_id") or ""].append(record)
    selected: list[dict[str, Any]] = []
    for paper_records in by_paper.values():
        ranked = sorted(
            paper_records,
            key=lambda item: (
                item.get("original_values", {}).get("marker_polarity") == "positive",
                stable_rank(item),
            ),
        )
        selected.extend(ranked[: min(2, len(ranked))])
    return sorted(selected, key=lambda item: (item.get("paper_id") or "", item["review_id"]))


def best_source_window(record: dict[str, Any], source_cache: dict[Path, tuple[str, str]]) -> dict[str, Any] | None:
    source_path = source_path_for(record)
    if source_path is None:
        return None
    if source_path not in source_cache:
        text = source_path.read_text(encoding="utf-8", errors="replace")
        source_cache[source_path] = (text, normalize(text))
    text = source_cache[source_path][0]
    lines = text.splitlines()
    original = record.get("original_values", {})
    gene_tokens = {
        normalize(original.get("gene_symbol")),
        normalize(original.get("original_symbol")),
    } - {""}
    context_tokens = {
        normalize(token)
        for token in re.findall(r"[A-Za-z0-9]+", str(original.get("source_context") or ""))
        if len(token) >= 4
    }
    cell_tokens = {
        normalize(token)
        for token in re.findall(
            r"[A-Za-z0-9]+",
            f"{original.get('cell_type') or ''} {original.get('subtype') or ''}",
        )
        if len(token) >= 4
    }
    best: tuple[float, int, int] | None = None
    radius = 3
    for index in range(len(lines)):
        start = max(0, index - radius)
        end = min(len(lines), index + radius + 1)
        window_norm = normalize(" ".join(lines[start:end]))
        gene_hits = sum(token in window_norm for token in gene_tokens)
        context_hits = sum(token in window_norm for token in context_tokens)
        cell_hits = sum(token in window_norm for token in cell_tokens)
        score = gene_hits * 20 + cell_hits * 3 + context_hits
        if best is None or score > best[0]:
            best = (score, start, end)
    if best is None:
        return None
    score, start, end = best
    return {
        "score": score,
        "line_start": start + 1,
        "line_end": end,
        "text": "\n".join(f"{line_no + 1}: {lines[line_no]}" for line_no in range(start, end)),
    }


def compact_record(
    record: dict[str, Any],
    checks: dict[str, Any],
    source_cache: dict[Path, tuple[str, str]],
) -> dict[str, Any]:
    original = record.get("original_values", {})
    return {
        "review_id": record.get("review_id"),
        "marker_id": record.get("marker_id"),
        "paper_id": record.get("paper_id"),
        "action": record.get("action"),
        "result": record.get("result"),
        "evidence_binding_status": record.get("evidence_binding_status"),
        "cell_type": original.get("cell_type"),
        "subtype": original.get("subtype"),
        "species": original.get("species"),
        "gene_symbol": original.get("gene_symbol"),
        "original_symbol": original.get("original_symbol"),
        "evidence_type": original.get("evidence_type"),
        "marker_polarity": original.get("marker_polarity"),
        "source_locator": original.get("source_locator"),
        "source_context": original.get("source_context"),
        "luna_evidence_excerpt": record.get("evidence_excerpt"),
        "luna_evidence_locator": record.get("evidence_locator"),
        "checks": checks,
        "best_source_window": best_source_window(record, source_cache),
    }


def main() -> None:
    payload = load_json(RUN / "review-records.json")
    records: list[dict[str, Any]] = payload["records"]
    inherited = [
        record
        for record in records
        if record.get("evidence_binding_status")
        == "prior_quick_consistency_inherited_with_documented_limit"
    ]
    blank_binding = [record for record in records if not record.get("evidence_binding_status")]
    inherited_sample = stratified_inherited_sample(inherited)
    bound_sample = stratified_target_bound_sample(records)
    source_cache: dict[Path, tuple[str, str]] = {}
    all_checks = {record["review_id"]: text_checks(record, source_cache) for record in records}

    output = {
        "run_id": "20260908-astra-audit-after-luna-existing-marker-correctness",
        "population": {
            "all_records": len(records),
            "inherited_quick_consistency": len(inherited),
            "blank_evidence_binding": len(blank_binding),
            "non_no_change_actions": sum(record.get("action") != "no_change" for record in records),
            "binding_status_counts": dict(Counter(str(record.get("evidence_binding_status") or "") for record in records)),
        },
        "mechanical_source_checks": {
            "source_missing": sum(not checks["source_exists"] for checks in all_checks.values()),
            "source_context_exact": sum(checks["context_exact"] for checks in all_checks.values()),
            "source_context_normalized": sum(checks["context_normalized"] for checks in all_checks.values()),
            "gene_present": sum(checks["gene_present"] for checks in all_checks.values()),
            "cell_token_present": sum(checks["cell_token_present"] for checks in all_checks.values()),
        },
        "audit_sets": {
            "all_blank_binding": [
                compact_record(record, all_checks[record["review_id"]], source_cache)
                for record in blank_binding
            ],
            "inherited_stratified_sample": [
                compact_record(record, all_checks[record["review_id"]], source_cache)
                for record in inherited_sample
            ],
            "target_bound_cross_paper_sample": [
                compact_record(record, all_checks[record["review_id"]], source_cache)
                for record in bound_sample
            ],
        },
        "sample_counts": {
            "blank_binding": len(blank_binding),
            "inherited": len(inherited_sample),
            "target_bound": len(bound_sample),
            "total_unique": len(
                {
                    record["review_id"]
                    for record in blank_binding + inherited_sample + bound_sample
                }
            ),
        },
    }
    OUTPUT.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"population": output["population"], "mechanical_source_checks": output["mechanical_source_checks"], "sample_counts": output["sample_counts"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
