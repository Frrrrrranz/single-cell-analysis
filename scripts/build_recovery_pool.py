"""B-lite 恢复池构建 + 门 1 机械校验。

输入：
- audited-extraction/markers/*_audit.json（旧 v1 严格范围口径终审，工作树）
- .archive/marker-extraction-85b4727/.../markers_output_v2/*_raw.json（旧一轮原始提取）
- review_md/*.md（当前论文 Markdown）
- marker提取/表单/our_markers.xlsx（现有正式 Marker，冻结基线）

池定义：
- A_exclude：旧终审 exclude 且排除理由非实质性（范围/物种/PNS/理由模糊）
- A_downgraded：旧终审 context_only / unresolved 且证据类型为正式四类
- B_unaudited：raw 中从未进入终审、证据类型为正式四类的候选

门 1 机械校验（不信任旧判定字段，全部重算）：
1. Markdown SHA256 与旧审计记录比对（防文本漂移）
2. 引用回溯：context_match_score + despaced_window_hit 兜底（复用 run_full_audit）
3. 唯一键 paper_id+cell_type+gene 去重：池内互查 + 与现有 markers sheet 对查
4. 字段合法性：species / polarity / normalization_status

输出：
- audited-extraction/recovery/recovery_pool.csv（全量候选 + 门 1 结果）
- audited-extraction/recovery/<paper_id>_pool.json（逐篇，供门 2 使用）
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

import openpyxl

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
MARKER_DIR = PROJECT_ROOT / "marker提取"
sys.path.insert(0, str(SCRIPT_DIR))

from run_full_audit import (  # noqa: E402
    CITATION_SCORE_THRESHOLD,
    context_match_score,
    despaced_window_hit,
)

ARCHIVE_RAW_DIR = (
    PROJECT_ROOT
    / ".archive"
    / "marker-extraction-85b4727"
    / "scripts"
    / "extract_markers"
    / "markers_output_v2"
)
AUDIT_DIR = MARKER_DIR / "audited-extraction" / "markers"
MD_DIR = MARKER_DIR / "review_md"
RECOVERY_DIR = MARKER_DIR / "audited-extraction" / "recovery"
MASTER_XLSX = MARKER_DIR / "表单" / "our_markers.xlsx"

FORMAL_EVIDENCE_TYPES = {
    "author_declared",
    "annotation_marker",
    "figure_labeled",
    "supplementary_marker",
}

# 大小写敏感：IGNORECASE 会让 "OCR" 误匹配 endocrine/neuroendocrine
SUBSTANTIVE_PATTERNS = re.compile(
    r"非基因|基因实体|对应错误|不存在|重复|污染|OCR|无法唯一|不可读|不可辨认|"
    r"并非\s*[Mm]arker|不是\s*[Mm]arker|非\s*[Mm]arker|不是正式|无法解析|拼写错误|幻觉"
)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def uniq_key(paper_id: str, cell_type: str, gene: str) -> tuple[str, str, str]:
    return (paper_id, (cell_type or "").strip(), (gene or "").strip().upper())


def load_existing_keys() -> set[tuple[str, str, str]]:
    wb = openpyxl.load_workbook(MASTER_XLSX, read_only=True)
    ws = wb["markers"]
    rows = list(ws.iter_rows(values_only=True))
    hdr = list(rows[0])
    i_pid, i_ct, i_g = hdr.index("paper_id"), hdr.index("cell_type"), hdr.index("gene_symbol")
    keys = {uniq_key(r[i_pid], r[i_ct], r[i_g]) for r in rows[1:]}
    wb.close()
    return keys


def gate1_check(
    record: dict,
    markdown: str,
    md_sha_ok: bool,
) -> tuple[str, dict]:
    """返回 (gate1_status, extra_fields)。status 非 pass 者仍留在池中交门 2/人工。"""
    symbol = (record.get("original_symbol") or record.get("gene") or "").strip()
    normalized = (record.get("normalized_symbol") or "").strip()
    context = record.get("source_context") or ""

    score = context_match_score(context, markdown, symbol)
    verified = score >= CITATION_SCORE_THRESHOLD
    if not verified and despaced_window_hit(context, markdown, (symbol, normalized)):
        verified = True
        score = max(score, 0.72)

    extra = {
        "citation_match_score": round(score, 4),
        "citation_verified": verified,
        "markdown_sha256_match": md_sha_ok,
    }

    if not verified:
        return "fail_citation", extra
    if not md_sha_ok:
        return "warn_markdown_changed", extra
    if (record.get("species") or "unknown") == "unknown":
        return "fail_species", extra
    status = record.get("normalization_status")
    if record.get("pool") != "B_unaudited" and status not in ("exact", "alias_resolved"):
        return "fail_symbol", extra
    return "pass", extra


def main() -> None:
    RECOVERY_DIR.mkdir(parents=True, exist_ok=True)
    existing_keys = load_existing_keys()

    audit_files = sorted(AUDIT_DIR.glob("*_audit.json"))
    if len(audit_files) != 40:
        raise SystemExit(f"预期 40 个审计 JSON，实际 {len(audit_files)}")

    pool: list[dict] = []
    md_sha_mismatch: list[str] = []

    for audit_path in audit_files:
        paper_id = audit_path.name[: -len("_audit.json")]
        data = json.loads(audit_path.read_text(encoding="utf-8"))

        md_path = MD_DIR / f"{paper_id}.md"
        if not md_path.exists():
            raise SystemExit(f"缺少 Markdown: {md_path}")
        markdown = md_path.read_text(encoding="utf-8")
        md_sha_ok = data.get("source_markdown_sha256") == sha256_text(markdown)
        if not md_sha_ok:
            md_sha_mismatch.append(paper_id)

        # 池 A：终审记录中非 include 且非实质性排除
        for m in data.get("markers", []):
            decision = m.get("decision")
            if decision == "include":
                continue
            reason = m.get("reason") or ""
            if decision == "exclude":
                if SUBSTANTIVE_PATTERNS.search(reason):
                    continue  # 实质性理由，维持排除，不入池
                pool_tag = "A_exclude"
            elif decision in ("context_only", "unresolved"):
                if m.get("evidence_type") not in FORMAL_EVIDENCE_TYPES:
                    continue
                pool_tag = "A_downgraded"
            else:
                continue
            pool.append(
                {
                    "paper_id": paper_id,
                    "pool": pool_tag,
                    "cell_type": m.get("cell_type"),
                    "subtype": m.get("subtype"),
                    "species": m.get("species"),
                    "original_symbol": m.get("original_symbol"),
                    "normalized_symbol": m.get("normalized_symbol"),
                    "normalization_status": m.get("normalization_status"),
                    "evidence_type": m.get("evidence_type"),
                    "marker_polarity": m.get("marker_polarity"),
                    "source_locator": m.get("source_locator"),
                    "source_context": m.get("source_context"),
                    "old_decision": decision,
                    "old_reason": reason,
                    "old_citation_verified": m.get("citation_verified"),
                    "task_no": (data.get("task") or {}).get("task_no"),
                }
            )

        # 池 B：raw 中从未进入终审的正式证据候选
        raw_path = ARCHIVE_RAW_DIR / f"{paper_id}_raw.json"
        raw_payload = json.loads(raw_path.read_text(encoding="utf-8"))
        audited_keys = {
            uniq_key(paper_id, m.get("cell_type"), m.get("original_symbol") or m.get("gene") or "")
            for m in data.get("markers", [])
        }
        for cell in raw_payload.get("cell_types", []):
            for mk in cell.get("markers", []):
                gene = mk.get("gene") or ""
                if mk.get("evidence_type") not in FORMAL_EVIDENCE_TYPES:
                    continue
                if uniq_key(paper_id, cell.get("cell_type"), gene) in audited_keys:
                    continue
                pool.append(
                    {
                        "paper_id": paper_id,
                        "pool": "B_unaudited",
                        "cell_type": cell.get("cell_type"),
                        "subtype": cell.get("subtype"),
                        "species": cell.get("species"),
                        "original_symbol": gene,
                        "normalized_symbol": gene,
                        "normalization_status": None,
                        "evidence_type": mk.get("evidence_type"),
                        "marker_polarity": mk.get("marker_polarity"),
                        "source_locator": mk.get("source_locator"),
                        "source_context": mk.get("source_context"),
                        "old_decision": "never_audited",
                        "old_reason": "",
                        "old_citation_verified": None,
                        "task_no": (data.get("task") or {}).get("task_no"),
                    }
                )

    # 门 1：逐条机械校验 + 去重
    seen_pool_keys: set[tuple[str, str, str]] = set()
    for record in pool:
        key = uniq_key(record["paper_id"], record["cell_type"], record["original_symbol"])
        markdown = (MD_DIR / f"{record['paper_id']}.md").read_text(encoding="utf-8")

        # 重新读取 md_sha 状态（按论文缓存可优化，规模小不必要）
        audit_sha = json.loads(
            (AUDIT_DIR / f"{record['paper_id']}_audit.json").read_text(encoding="utf-8")
        ).get("source_markdown_sha256")
        md_sha_ok = audit_sha == sha256_text(markdown)

        status, extra = gate1_check(record, markdown, md_sha_ok)
        record.update(extra)

        if key in existing_keys:
            record["gate1_status"] = "duplicate_existing"
        elif key in seen_pool_keys:
            record["gate1_status"] = "duplicate_pool"
        else:
            if status == "pass":
                record["gate1_status"] = "pass"
            else:
                record["gate1_status"] = status
            seen_pool_keys.add(key)

    # 输出 CSV
    import csv

    csv_path = RECOVERY_DIR / "recovery_pool.csv"
    fieldnames = list(pool[0].keys())
    with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(pool)

    # 输出逐篇 pool JSON（供门 2）
    by_paper: dict[str, list[dict]] = {}
    for record in pool:
        by_paper.setdefault(record["paper_id"], []).append(record)
    for paper_id, records in by_paper.items():
        out = RECOVERY_DIR / f"{paper_id}_pool.json"
        out.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")

    # 统计
    from collections import Counter

    pool_counts = Counter(r["pool"] for r in pool)
    gate_counts = Counter(r["gate1_status"] for r in pool)
    paper_counts = Counter(r["paper_id"] for r in pool)
    print(f"pool total: {len(pool)}")
    print(f"by pool: {dict(pool_counts)}")
    print(f"gate1: {dict(gate_counts)}")
    print(f"papers involved: {len(paper_counts)}")
    print(f"markdown sha mismatch: {md_sha_mismatch or 'none'}")
    print(f"CSV: {csv_path}")


if __name__ == "__main__":
    main()
