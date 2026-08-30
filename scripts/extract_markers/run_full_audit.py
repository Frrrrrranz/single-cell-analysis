"""使用已有 Markdown 对 40 篇 Marker 提取结果做逐篇终审。

本脚本不转换 PDF、不修改 markers_output_v2，也不修改现有 Excel。
每篇只调用一次 OpenAI 兼容 API，并将可恢复的逐篇审核 JSON 写入 markers_audited/。
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import logging
import os
import re
import time
from pathlib import Path
from typing import Any

from dotenv import load_dotenv


LOGGER = logging.getLogger(__name__)
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
DEFAULT_MD_DIR = SCRIPT_DIR / "review_md"
DEFAULT_RAW_DIR = SCRIPT_DIR / "markers_output_v2"
DEFAULT_OUTPUT_DIR = SCRIPT_DIR / "markers_audited"
DEFAULT_SCOPE_FILE = SCRIPT_DIR / "audits" / "task-scope-2026-08-14.md"
DEFAULT_PROMPT_FILE = SCRIPT_DIR / "prompts" / "audit_markers_v1.md"

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
NEURAL_TERMS = re.compile(
    r"schwann|neuro|neural|neuron|glia|gangli|sensory|sympathetic|parasympathetic|"
    r"autonomic|enteric|nocicept|pnec|enteroendocrine|satellite",
    re.IGNORECASE,
)
HIGH_RISK_TERMS = re.compile(
    r"marker|marked by|marks\b|defined by|characteri[sz]ed by|annotat|identif|classif|"
    r"gated|sorted|\bhigh\b|\blow\b|minimal|negative|positive|\+|−",
    re.IGNORECASE,
)

PAPER_ID_FIELD = re.compile(r"^(?:DOI|PMID|TITLE)_[^\s|]+$")
L_LEVEL_FIELD = re.compile(r"^L\d+:")
TECH_FIELD = re.compile(
    r"10x|smart-?seq|drop-?seq|seq-?well|cite-?seq|snrna|scrna|multiome|\|",
    re.IGNORECASE,
)
PDF_STATUS_FIELD = re.compile(r"核验|PDF|求助")
NO_SCOPE = {"—", "-", "NaN", ""}

CITATION_SCORE_THRESHOLD = 0.72
TOKEN_PATTERN = re.compile(r"[a-z0-9][a-z0-9\-']+")
STOPWORDS = frozenset(
    """
    a an the and or but if then than so such both each other more most some any all
    also very into over under between during after before above below up down out off
    again further once here there when where why how which who whom whose what am is
    are was were be been being as it its itself this that these those i me my we our
    us you your he him his she her they them their not no nor do does did done can
    could may might will would shall should have has had of at by for with about to
    from in on upon within without across through against per via due based
    """.split()
)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def parse_scope_table(path: Path) -> dict[str, dict[str, Any]]:
    """任务范围表的“PNS层级”列数不稳定（1-3 列），固定列号会错位。

    因此用 paper_id 模式动态定位行内字段，再向前收集 L 层级和组织。
    """
    task_map: dict[str, dict[str, Any]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not re.match(r"^\|\s*\d+\s*\|", line):
            continue
        fields = [field.strip().replace("\\_", "_") for field in line.strip().strip("|").split("|")]
        if len(fields) < 21:
            continue
        paper_index = next(
            (index for index, field in enumerate(fields) if PAPER_ID_FIELD.match(field)),
            None,
        )
        if paper_index is None:
            continue
        paper_id = fields[paper_index]
        if paper_id == "NaN":
            continue
        scope_fields = fields[12:paper_index]
        l_levels = [field for field in scope_fields if L_LEVEL_FIELD.match(field)]
        if l_levels:
            target_cell_scope = " / ".join(l_levels)
        else:
            target_cell_scope = next(
                (field for field in scope_fields if field in NO_SCOPE), "—"
            )
        tissue = ""
        for field in scope_fields:
            if L_LEVEL_FIELD.match(field) or field in NO_SCOPE:
                continue
            if TECH_FIELD.search(field) or PDF_STATUS_FIELD.search(field):
                continue
            tissue = field
            break
        task_map[paper_id] = {
            "task_no": int(fields[0]),
            "dataset_id": fields[4],
            "paper_title": fields[6],
            "task_species": fields[11],
            "target_cell_scope": target_cell_scope,
            "tissue": tissue,
            "paper_id": paper_id,
        }
    return task_map


def compact_existing_candidates(payload: dict[str, Any]) -> list[dict[str, Any]]:
    candidates: list[dict[str, Any]] = []
    for cell in payload.get("cell_types", []):
        cell_label = " ".join(
            str(value or "") for value in (cell.get("cell_type"), cell.get("subtype"))
        )
        neural_cell = bool(NEURAL_TERMS.search(cell_label)) or cell.get("is_pns_cell") in {"true", "NA"}
        for marker in cell.get("markers", []):
            source_context = str(marker.get("source_context", ""))
            formal_or_risky = (
                marker.get("candidate_class") == "formal_candidate"
                or marker.get("evidence_type") in FORMAL_EVIDENCE_TYPES
                or marker.get("model_evidence_type") in FORMAL_EVIDENCE_TYPES
                or bool(HIGH_RISK_TERMS.search(source_context))
            )
            if not neural_cell and not formal_or_risky:
                continue
            candidates.append(
                {
                    "cell_type": cell.get("cell_type"),
                    "subtype": cell.get("subtype"),
                    "species": cell.get("species"),
                    "is_pns_cell": cell.get("is_pns_cell"),
                    "gene": marker.get("gene"),
                    "evidence_type": marker.get("evidence_type"),
                    "model_evidence_type": marker.get("model_evidence_type"),
                    "marker_polarity": marker.get("marker_polarity"),
                    "candidate_class": marker.get("candidate_class"),
                    "source_locator": marker.get("source_locator"),
                    "source_context": source_context,
                    "guardrail_reason": marker.get("guardrail_reason"),
                }
            )
    return candidates


def strip_json_fence(content: str) -> str:
    cleaned = content.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r"\s*```$", "", cleaned)
    return cleaned.strip()


def tokenize(text: str) -> list[str]:
    return TOKEN_PATTERN.findall(text.lower())


def symbol_in_markdown(symbol: str, markdown: str) -> bool:
    if not symbol.strip():
        return False
    pattern = rf"(?<![A-Za-z0-9]){re.escape(symbol.strip())}(?![A-Za-z0-9])"
    return bool(re.search(pattern, markdown, re.IGNORECASE))


def context_match_score(context: str, markdown: str, symbol: str) -> float:
    """source_context 信息词元在 Markdown 全文中的覆盖率。

    双栏 PDF 转 Markdown 后句子常被另一栏文字打断，连续子串匹配会把真实
    引文误判为幻觉；词元覆盖率只要求证据词在全文出现。基因符号不在原文
    时直接 0 分。
    """
    if not context.strip():
        return 0.0
    if symbol and not symbol_in_markdown(symbol, markdown):
        return 0.0
    context_tokens = {token for token in tokenize(context) if token not in STOPWORDS}
    if not context_tokens:
        return 0.0
    markdown_tokens = set(tokenize(markdown))
    hits = len(context_tokens & markdown_tokens)
    return hits / len(context_tokens)


def _despace(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def _symbol_tokens(*symbols: str) -> list[str]:
    """取符号的字母数字词元（≥3 字符），长词元优先。"""
    tokens: set[str] = set()
    for symbol in symbols:
        if not symbol:
            continue
        for token in tokenize(symbol):
            if len(token) >= 3:
                tokens.add(token)
    return sorted(tokens, key=len, reverse=True)


def despaced_window_hit(
    context: str,
    markdown: str,
    symbols: tuple[str, ...] = (),
    window: int = 6,
    min_chunk_len: int = 18,
) -> bool:
    """粘连 PDF 文本兜底校验。

    部分 PDF 抽取会把整句抽成无空格长词（如 "thesenescencemarkerp21"），
    词元化后一个词都对不上，但把 source_context 连续若干词元拼接后仍是
    原文（去空格、去标点）的连续子串。18 字符以上的字母数字连续段等价
    于原文逐字引用，可视为回溯通过。图注类短引文不足 6 个词元时窗口
    自适应收缩到 4。

    提供符号时，命中的连续段必须实际包含该基因符号（原文写法或标准
    符号任一）：否则 "Dotplot showing the mean expression of..." 这类
    通用图例前缀会误判为可回溯，而它证明不了具体 gene–cell 对应。
    """
    tokens = tokenize(context)
    if len(tokens) < 4:
        return False
    markdown_ns = _despace(markdown)
    symbol_tokens = _symbol_tokens(*symbols)
    for size in range(min(window, len(tokens)), 3, -1):
        for start in range(len(tokens) - size + 1):
            chunk = _despace("".join(tokens[start : start + size]))
            if len(chunk) < min_chunk_len or chunk not in markdown_ns:
                continue
            if symbol_tokens and not any(token in chunk for token in symbol_tokens):
                continue
            return True
    return False


def validate_audit_result(data: dict[str, Any], paper_id: str, markdown: str) -> dict[str, Any]:
    if data.get("audit_version") != 1:
        raise ValueError("audit_version 必须为 1")
    if data.get("paper_id") != paper_id:
        raise ValueError(f"paper_id 不一致: {data.get('paper_id')!r}")
    if data.get("paper_status") not in {"pass", "corrected", "no_formal_target_marker", "unresolved"}:
        raise ValueError(f"无效 paper_status: {data.get('paper_status')!r}")
    if not isinstance(data.get("markers"), list) or not isinstance(data.get("issues"), list):
        raise ValueError("markers/issues 必须为数组")

    citation_failures = 0
    for index, marker in enumerate(data["markers"]):
        prefix = f"markers[{index}]"
        if marker.get("species") not in SPECIES:
            raise ValueError(f"{prefix}.species 无效")
        if marker.get("evidence_type") not in ALL_EVIDENCE_TYPES:
            raise ValueError(f"{prefix}.evidence_type 无效")
        if marker.get("marker_polarity") not in POLARITIES:
            raise ValueError(f"{prefix}.marker_polarity 无效")
        if marker.get("decision") not in DECISIONS:
            raise ValueError(f"{prefix}.decision 无效")
        if marker.get("normalization_status") not in NORMALIZATION_STATUSES:
            raise ValueError(f"{prefix}.normalization_status 无效")
        for key in ("cell_type", "original_symbol", "normalized_symbol", "source_locator", "source_context"):
            if not isinstance(marker.get(key), str) or not marker[key].strip():
                raise ValueError(f"{prefix}.{key} 必须为非空字符串")

        score = context_match_score(
            marker["source_context"], markdown, marker["original_symbol"]
        )
        verified = score >= CITATION_SCORE_THRESHOLD
        if not verified and despaced_window_hit(
            marker["source_context"],
            markdown,
            (marker["original_symbol"], marker["normalized_symbol"]),
        ):
            marker["citation_recheck"] = "despaced_window"
            verified = True
        marker["citation_match_score"] = round(score, 4)
        marker["citation_verified"] = verified
        if marker["decision"] == "include":
            if marker.get("in_project_scope") is not True:
                marker["decision"] = "exclude"
                marker["reason"] = f"{marker.get('reason', '')}; 自动校验：不在项目目标范围"
            elif marker["evidence_type"] not in FORMAL_EVIDENCE_TYPES:
                marker["decision"] = "context_only"
                marker["reason"] = f"{marker.get('reason', '')}; 自动校验：非正式证据"
            elif marker["normalization_status"] not in {"exact", "alias_resolved"}:
                marker["decision"] = "unresolved"
                marker["reason"] = f"{marker.get('reason', '')}; 自动校验：基因符号未唯一解析"
            elif marker["species"] == "unknown":
                marker["decision"] = "unresolved"
                marker["reason"] = f"{marker.get('reason', '')}; 自动校验：物种无法确定"
            elif not marker["citation_verified"]:
                marker["decision"] = "unresolved"
                marker["reason"] = (
                    f"{marker.get('reason', '')}; 自动校验：source_context 与 Markdown "
                    f"词元覆盖率 {score:.2f} 低于 {CITATION_SCORE_THRESHOLD}"
                )
                citation_failures += 1

    if citation_failures:
        data["issues"].append(
            {
                "severity": "error",
                "issue_type": "citation",
                "description": f"{citation_failures} 条拟纳入 Marker 未通过 Markdown 原文回溯校验，已降级为 unresolved",
            }
        )
    return data


def call_api(system_prompt: str, user_content: str, model: str, api_key: str, api_base: str) -> str:
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RuntimeError("缺少 openai 依赖") from exc

    client_args: dict[str, Any] = {"api_key": api_key, "timeout": 300.0}
    if api_base:
        client_args["base_url"] = api_base
    client = OpenAI(**client_args)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
        temperature=0.0,
        response_format={"type": "json_object"},
    )
    return response.choices[0].message.content or ""


def audit_one(
    md_path: Path,
    raw_dir: Path,
    output_dir: Path,
    task_map: dict[str, dict[str, Any]],
    prompt: str,
    model: str,
    api_key: str,
    api_base: str,
    overwrite: bool,
) -> tuple[str, str]:
    paper_id = md_path.stem
    output_path = output_dir / f"{paper_id}_audit.json"
    if output_path.exists() and not overwrite:
        return paper_id, "skipped"

    raw_path = raw_dir / f"{paper_id}_raw.json"
    if not raw_path.exists():
        raise FileNotFoundError(f"缺少 raw JSON: {raw_path}")
    task = task_map.get(paper_id)
    if task is None:
        raise KeyError(f"任务范围表缺少 paper_id: {paper_id}")

    markdown = md_path.read_text(encoding="utf-8")
    raw_text = raw_path.read_text(encoding="utf-8")
    raw_payload = json.loads(raw_text)
    existing_candidates = compact_existing_candidates(raw_payload)
    user_content = (
        "请审核以下单篇论文。任务范围是唯一的项目范围依据，但 Marker 必须来自 Markdown 原文。\n\n"
        f"任务元数据:\n{json.dumps(task, ensure_ascii=False, indent=2)}\n\n"
        "现有提取中的正式、神经相关或高风险候选（可能有误，也可能漏提）:\n"
        f"{json.dumps(existing_candidates, ensure_ascii=False, indent=2)}\n\n"
        f"论文 Markdown（文件 {md_path.name}）:\n{markdown}"
    )

    last_error: Exception | None = None
    for attempt in range(1, 4):
        try:
            content = call_api(prompt, user_content, model, api_key, api_base)
            result = json.loads(strip_json_fence(content))
            result = validate_audit_result(result, paper_id, markdown)
            result["task"] = task
            result["audit_model"] = model
            result["source_markdown"] = md_path.name
            result["source_raw_json"] = raw_path.name
            result["source_markdown_sha256"] = sha256_text(markdown)
            result["source_raw_sha256"] = sha256_text(raw_text)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
            return paper_id, "completed"
        except Exception as exc:  # noqa: BLE001 - API/JSON 错误统一重试并保留最后异常
            last_error = exc
            LOGGER.warning("%s 审核失败（%d/3）：%s", paper_id, attempt, exc)
            if attempt < 3:
                time.sleep(2**attempt)
    raise RuntimeError(f"{paper_id} 审核失败") from last_error


def main() -> None:
    parser = argparse.ArgumentParser(description="审核 40 篇现有 Markdown 的 Marker 提取结果")
    parser.add_argument("--md-dir", type=Path, default=DEFAULT_MD_DIR)
    parser.add_argument("--raw-dir", type=Path, default=DEFAULT_RAW_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--scope-file", type=Path, default=DEFAULT_SCOPE_FILE)
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

    task_map = parse_scope_table(args.scope_file)
    prompt = args.prompt_file.read_text(encoding="utf-8")
    md_paths = sorted(args.md_dir.glob("*.md"))
    if args.paper_id:
        selected = set(args.paper_id)
        md_paths = [path for path in md_paths if path.stem in selected]
    if not md_paths:
        raise SystemExit("没有待审核 Markdown")

    missing_raw = [path.stem for path in md_paths if not (args.raw_dir / f"{path.stem}_raw.json").exists()]
    missing_scope = [path.stem for path in md_paths if path.stem not in task_map]
    if missing_raw or missing_scope:
        raise SystemExit(f"输入映射不完整：missing_raw={missing_raw}, missing_scope={missing_scope}")

    LOGGER.info("开始审核 %d 篇，model=%s，workers=%d", len(md_paths), model, args.workers)
    failures: list[str] = []
    counts = {"completed": 0, "skipped": 0}
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        future_map = {
            executor.submit(
                audit_one,
                md_path,
                args.raw_dir,
                args.output_dir,
                task_map,
                prompt,
                model,
                api_key,
                api_base,
                args.overwrite,
            ): md_path.stem
            for md_path in md_paths
        }
        for future in concurrent.futures.as_completed(future_map):
            paper_id = future_map[future]
            try:
                _, status = future.result()
                counts[status] += 1
                LOGGER.info("%s：%s", paper_id, status)
            except Exception:  # noqa: BLE001 - 汇总失败后继续其余论文
                failures.append(paper_id)
                LOGGER.exception("%s：failed", paper_id)

    LOGGER.info("审核结束：%s，failed=%d", counts, len(failures))
    if failures:
        LOGGER.error("失败论文：%s", ", ".join(sorted(failures)))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
