"""门 2：LLM 定向复核 + 全文漏提扫描（B-lite）。

对 40 篇论文各调用一次 LLM：
- 逐条复核恢复池候选（旧判定仅作线索）；
- 全文扫描候选与已入总表之外的正式 Marker（new_finding）。

输出写入 audited-extraction/recovery/<paper_id>_verify.json。
复用 run_full_audit.py 的 API 调用与引用回溯校验函数。
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import logging
import os
import time
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from run_full_audit import (
    CITATION_SCORE_THRESHOLD,
    call_api,
    context_match_score,
    despaced_window_hit,
    strip_json_fence,
)

LOGGER = logging.getLogger(__name__)
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
MARKER_DIR = PROJECT_ROOT / "marker提取"
MD_DIR = MARKER_DIR / "review_md"
AUDIT_DIR = MARKER_DIR / "audited-extraction" / "markers"
RECOVERY_DIR = MARKER_DIR / "audited-extraction" / "recovery"
DEFAULT_PROMPT_FILE = MARKER_DIR / "prompts" / "recovery_verify_v1.md"

FORMAL_EVIDENCE_TYPES = {
    "author_declared",
    "annotation_marker",
    "figure_labeled",
    "supplementary_marker",
}
ALL_EVIDENCE_TYPES = FORMAL_EVIDENCE_TYPES | {
    "cluster_enriched",
    "model_inferred",
    "reference_imported",
}
DECISIONS = {"include", "context_only", "exclude", "unresolved"}
NORMALIZATION_STATUSES = {
    "exact",
    "alias_resolved",
    "ambiguous",
    "non_gene_entity",
    "unresolved",
}
SPECIES = {"human", "mouse", "rat", "other", "unknown"}
POLARITIES = {"positive", "negative", "unknown"}
FOUR_LAYERS = {"L1", "L2", "L3", "L4", "outside", "unknown"}


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_candidates(paper_id: str) -> list[dict[str, Any]]:
    """池候选（排除 duplicate），附加 candidate_index。"""
    pool_path = RECOVERY_DIR / f"{paper_id}_pool.json"
    if not pool_path.exists():
        return []
    records = json.loads(pool_path.read_text(encoding="utf-8"))
    usable = [r for r in records if r.get("gate1_status") not in ("duplicate_pool", "duplicate_existing")]
    for index, record in enumerate(usable):
        record["candidate_index"] = index
    return usable


def compact_candidate(record: dict[str, Any]) -> dict[str, Any]:
    return {
        "candidate_index": record["candidate_index"],
        "pool": record.get("pool"),
        "cell_type": record.get("cell_type"),
        "subtype": record.get("subtype"),
        "species": record.get("species"),
        "gene": record.get("original_symbol"),
        "evidence_type": record.get("evidence_type"),
        "marker_polarity": record.get("marker_polarity"),
        "source_locator": record.get("source_locator"),
        "source_context": record.get("source_context"),
        "old_decision": record.get("old_decision"),
        "old_reason": record.get("old_reason"),
        "gate1_status": record.get("gate1_status"),
    }


def citation_verified(marker: dict[str, Any], markdown: str) -> tuple[bool, float]:
    symbol = marker.get("original_symbol", "")
    context = marker.get("source_context", "")
    score = context_match_score(context, markdown, symbol)
    if score >= CITATION_SCORE_THRESHOLD:
        return True, score
    if despaced_window_hit(
        context,
        markdown,
        (symbol, marker.get("normalized_symbol", "")),
    ):
        return True, max(score, CITATION_SCORE_THRESHOLD)
    return False, score


def validate_record(marker: dict[str, Any], prefix: str) -> None:
    if marker.get("species") not in SPECIES:
        raise ValueError(f"{prefix}.species 无效: {marker.get('species')!r}")
    if marker.get("evidence_type") not in ALL_EVIDENCE_TYPES:
        raise ValueError(f"{prefix}.evidence_type 无效")
    if marker.get("marker_polarity") not in POLARITIES:
        raise ValueError(f"{prefix}.marker_polarity 无效")
    if marker.get("decision") not in DECISIONS:
        raise ValueError(f"{prefix}.decision 无效")
    if marker.get("normalization_status") not in NORMALIZATION_STATUSES:
        raise ValueError(f"{prefix}.normalization_status 无效")
    if marker.get("four_layer_category") not in FOUR_LAYERS:
        raise ValueError(f"{prefix}.four_layer_category 无效")
    for key in (
        "cell_type",
        "original_symbol",
        "normalized_symbol",
        "source_locator",
        "source_context",
    ):
        if not isinstance(marker.get(key), str) or not marker[key].strip():
            raise ValueError(f"{prefix}.{key} 必须为非空字符串")


def enforce_include_rules(marker: dict[str, Any], markdown: str) -> None:
    """include 的机械后校验，失败按原因降级。"""
    if marker["decision"] != "include":
        return
    if marker["evidence_type"] not in FORMAL_EVIDENCE_TYPES:
        marker["decision"] = "context_only"
        marker["reason"] = f"{marker.get('reason', '')}; 自动校验：非正式证据"
        return
    if marker["normalization_status"] not in {"exact", "alias_resolved"}:
        marker["decision"] = "unresolved"
        marker["reason"] = f"{marker.get('reason', '')}; 自动校验：基因符号未唯一解析"
        return
    if marker["species"] == "unknown":
        marker["decision"] = "unresolved"
        marker["reason"] = f"{marker.get('reason', '')}; 自动校验：物种无法确定"
        return
    verified, score = citation_verified(marker, markdown)
    marker["citation_match_score"] = round(score, 4)
    marker["citation_verified"] = verified
    if not verified:
        marker["decision"] = "unresolved"
        marker["reason"] = (
            f"{marker.get('reason', '')}; 自动校验：source_context 回溯覆盖率 "
            f"{score:.2f} 低于 {CITATION_SCORE_THRESHOLD}"
        )


def validate_result(
    data: dict[str, Any],
    paper_id: str,
    markdown: str,
    candidate_indices: set[int],
) -> dict[str, Any]:
    if data.get("verify_version") != 1:
        raise ValueError("verify_version 必须为 1")
    if data.get("paper_id") != paper_id:
        raise ValueError(f"paper_id 不一致: {data.get('paper_id')!r}")
    for key in ("cluster_inventory", "verifications", "new_findings", "issues"):
        if not isinstance(data.get(key), list):
            raise ValueError(f"{key} 必须为数组")

    got_indices = [v.get("candidate_index") for v in data["verifications"]]
    if sorted(got_indices) != sorted(candidate_indices):
        raise ValueError(
            f"candidate_index 不匹配: 期望 {sorted(candidate_indices)}，"
            f"返回 {sorted(i for i in got_indices if i is not None)}"
        )

    for index, marker in enumerate(data["verifications"]):
        validate_record(marker, f"verifications[{index}]")
        enforce_include_rules(marker, markdown)
    for index, marker in enumerate(data["new_findings"]):
        validate_record(marker, f"new_findings[{index}]")
        enforce_include_rules(marker, markdown)
    return data


def verify_one(
    paper_id: str,
    prompt: str,
    model: str,
    api_key: str,
    api_base: str,
    overwrite: bool,
) -> str:
    output_path = RECOVERY_DIR / f"{paper_id}_verify.json"
    if output_path.exists() and not overwrite:
        return "skipped"

    md_path = MD_DIR / f"{paper_id}.md"
    markdown = md_path.read_text(encoding="utf-8")
    audit = json.loads((AUDIT_DIR / f"{paper_id}_audit.json").read_text(encoding="utf-8"))
    task = audit.get("task") or {}

    candidates = load_candidates(paper_id)
    existing_includes = [
        {"cell_type": m.get("cell_type"), "gene": m.get("original_symbol")}
        for m in audit.get("markers", [])
        if m.get("decision") == "include"
    ]

    user_content = (
        "请复核以下单篇论文。所有细胞类型的正式 Marker 都要保留；层级、物种、组织只用于分类。\n\n"
        f"分类元数据:\n{json.dumps(task, ensure_ascii=False, indent=2)}\n\n"
        "已入总表的 include（不需要重新判定，也不要作为新发现重复报告）:\n"
        f"{json.dumps(existing_includes, ensure_ascii=False, indent=2)}\n\n"
        f"待复核候选（共 {len(candidates)} 条，candidate_index 逐条对应输出）:\n"
        f"{json.dumps([compact_candidate(c) for c in candidates], ensure_ascii=False, indent=2)}\n\n"
        f"论文 Markdown（文件 {md_path.name}）:\n{markdown}"
    )

    last_error: Exception | None = None
    for attempt in range(1, 4):
        try:
            content = call_api(prompt, user_content, model, api_key, api_base)
            result = json.loads(strip_json_fence(content))
            result = validate_result(
                result,
                paper_id,
                markdown,
                {c["candidate_index"] for c in candidates},
            )
            result["task"] = task
            result["verify_model"] = model
            result["source_markdown"] = md_path.name
            result["source_markdown_sha256"] = sha256_text(markdown)
            result["pool_records"] = len(candidates)
            output_path.write_text(
                json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
            )
            return "completed"
        except Exception as exc:  # noqa: BLE001 - API/JSON 错误统一重试
            last_error = exc
            LOGGER.warning("%s 复核失败（%d/3）：%s", paper_id, attempt, exc)
            if attempt < 3:
                time.sleep(2**attempt)
    raise RuntimeError(f"{paper_id} 复核失败") from last_error


def main() -> None:
    parser = argparse.ArgumentParser(description="恢复池门 2 LLM 复核 + 全文漏提扫描")
    parser.add_argument("--prompt-file", type=Path, default=DEFAULT_PROMPT_FILE)
    parser.add_argument("--model", default=None)
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--paper-id", action="append", default=[])
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    load_dotenv(PROJECT_ROOT / ".env")
    api_key = os.environ.get("MARKER_LLM_API_KEY", "")
    api_base = os.environ.get("MARKER_LLM_API_BASE", "")
    model = args.model or os.environ.get("MARKER_LLM_MODEL", "deepseek-v4-flash")
    if not api_key:
        raise SystemExit("未设置 MARKER_LLM_API_KEY")
    if args.workers < 1 or args.workers > 6:
        raise SystemExit("--workers 必须为 1..6")

    prompt = args.prompt_file.read_text(encoding="utf-8")
    paper_ids = sorted(p.name[: -len("_audit.json")] for p in AUDIT_DIR.glob("*_audit.json"))
    if args.paper_id:
        selected = set(args.paper_id)
        paper_ids = [p for p in paper_ids if p in selected]
    if not paper_ids:
        raise SystemExit("没有待复核论文")

    LOGGER.info("开始复核 %d 篇，model=%s，workers=%d", len(paper_ids), model, args.workers)
    failures: list[str] = []
    counts: dict[str, int] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        future_map = {
            executor.submit(
                verify_one, pid, prompt, model, api_key, api_base, args.overwrite
            ): pid
            for pid in paper_ids
        }
        for future in concurrent.futures.as_completed(future_map):
            pid = future_map[future]
            try:
                status = future.result()
                counts[status] = counts.get(status, 0) + 1
                LOGGER.info("%s：%s", pid, status)
            except Exception:  # noqa: BLE001 - 汇总失败后继续其余论文
                failures.append(pid)
                LOGGER.exception("%s：failed", pid)

    LOGGER.info("复核结束：%s，failed=%d", counts, len(failures))
    if failures:
        LOGGER.error("失败论文：%s", ", ".join(sorted(failures)))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
