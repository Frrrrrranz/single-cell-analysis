"""
recheck_citations.py — 粘连 PDF 文本的引用回溯复核（确定性，无 LLM 调用）

背景：run_full_audit.py 的 citation 校验用词元覆盖率。部分论文 Markdown
由 PDF 抽取时整句粘连成无空格长词（如 "thesenescencemarkerp21"），词元化后
全部失配，真实引文被误判为未回溯，include 被降级为 unresolved。

本脚本对 markers_audited/ 现有审计 JSON 复用 run_full_audit.py 的去空格
连续窗口复检逻辑：
- 命中且 decision 为 citation 降级产生的 unresolved → 恢复 include
- 未命中 → 维持 unresolved（随复核 CSV 走人工决策）
- 同步更新 citation_verified / citation_recheck 与 issues 中 citation 计数

用法：
    python recheck_citations.py [--audit-dir markers_audited]
                                [--md-dir review_md] [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from run_full_audit import (
    FORMAL_EVIDENCE_TYPES,
    despaced_window_hit,
)

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_AUDIT_DIR = SCRIPT_DIR / "markers_audited"
DEFAULT_MD_DIR = SCRIPT_DIR / "review_md"

DOWNGRADE_SUFFIX = re.compile(
    r"\s*;?\s*自动校验：source_context 与 Markdown 词元覆盖率 [\d.]+ 低于 [\d.]+\s*$"
)
RECHECK_NOTE = "; 自动复核：去空格连续窗口复检通过（PDF 粘连文本）"


def load_markdown(md_dir: Path, filename: str) -> str:
    return (md_dir / filename).read_text(encoding="utf-8")


def gates_still_pass(marker: dict[str, Any]) -> bool:
    """citation 降级发生前其余门槛已通过；恢复前按同一顺序再确认一次。"""
    return (
        marker.get("in_project_scope") is True
        and marker.get("evidence_type") in FORMAL_EVIDENCE_TYPES
        and marker.get("normalization_status") in {"exact", "alias_resolved"}
        and marker.get("species") != "unknown"
    )


def recheck_paper(
    data: dict[str, Any], markdown: str
) -> tuple[list[str], list[str], int, int]:
    """复核单篇，返回（恢复的符号列表、仍失败的符号列表、恢复数、剩余降级数）。

    两类复核：
    1. 旧版兜底（无符号包含检查）留下的 `citation_recheck=despaced_window`
       标记：用新逻辑复检，不通过则撤销验证标记；此前若据此恢复过
       include，降回 unresolved。
    2. `citation_verified=false` 的 citation 降级条目：命中新逻辑则恢复
       include，未命中维持 unresolved 待人工复核。
    """
    restored: list[str] = []
    still_failed: list[str] = []
    revoked: list[str] = []
    remaining_downgrades = 0
    revoked_include = 0

    for marker in data.get("markers", []):
        symbols = (
            marker.get("original_symbol", ""),
            marker.get("normalized_symbol", ""),
        )
        if marker.get("citation_recheck") == "despaced_window":
            if not despaced_window_hit(marker.get("source_context", ""), markdown, symbols):
                marker["citation_verified"] = False
                marker.pop("citation_recheck", None)
                revoked.append(marker.get("normalized_symbol") or "")
                if marker.get("decision") == "include":
                    marker["decision"] = "unresolved"
                    revoked_include += 1
                    marker["reason"] = (
                        f"{marker.get('reason', '')}; "
                        "自动复核：符号包含复检未通过，降级 unresolved"
                    )
            continue
        if marker.get("citation_verified"):
            continue

        hit = despaced_window_hit(marker.get("source_context", ""), markdown, symbols)
        citation_downgraded = (
            marker.get("decision") == "unresolved"
            and DOWNGRADE_SUFFIX.search(marker.get("reason", ""))
        )
        if hit:
            marker["citation_verified"] = True
            marker["citation_recheck"] = "despaced_window"
        if hit and citation_downgraded and gates_still_pass(marker):
            marker["decision"] = "include"
            marker["reason"] = (
                DOWNGRADE_SUFFIX.sub("", marker.get("reason", "")) + RECHECK_NOTE
            )
            restored.append(marker.get("normalized_symbol") or marker.get("original_symbol", ""))
        elif citation_downgraded:
            remaining_downgrades += 1
            still_failed.append(marker.get("normalized_symbol") or marker.get("original_symbol", ""))

    update_citation_issue(data, remaining_downgrades + revoked_include)
    promote_paper_status(data)
    for symbol in revoked:
        print(f"    撤销旧版兜底验证标记: {symbol}")
    return restored, still_failed, len(restored), remaining_downgrades


def update_citation_issue(data: dict[str, Any], remaining: int) -> None:
    issues = data.get("issues", [])
    citation_issues = [i for i in issues if i.get("issue_type") == "citation"]
    for issue in citation_issues:
        if remaining > 0:
            issue["description"] = (
                f"{remaining} 条拟纳入 Marker 未通过 Markdown 原文回溯校验，"
                "维持 unresolved 待人工复核"
            )
        else:
            issues.remove(issue)


def promote_paper_status(data: dict[str, Any]) -> None:
    if data.get("paper_status") != "no_formal_target_marker":
        return
    has_include = any(m.get("decision") == "include" for m in data.get("markers", []))
    if has_include:
        data["paper_status"] = "corrected"
        data["summary"] = (
            f"{data.get('summary', '')} 引用复核后恢复正式 Marker，状态由 "
            "no_formal_target_marker 改为 corrected。"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="粘连文本 citation 复核")
    parser.add_argument("--audit-dir", type=Path, default=DEFAULT_AUDIT_DIR)
    parser.add_argument("--md-dir", type=Path, default=DEFAULT_MD_DIR)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    audit_paths = sorted(args.audit_dir.glob("*_audit.json"))
    if not audit_paths:
        raise SystemExit(f"未找到审计 JSON: {args.audit_dir}")

    total_restored = 0
    total_remaining = 0
    for path in audit_paths:
        original_text = path.read_text(encoding="utf-8")
        data = json.loads(original_text)
        markdown = load_markdown(args.md_dir, data["source_markdown"])
        restored, failed, n_restored, n_remaining = recheck_paper(data, markdown)
        total_restored += n_restored
        total_remaining += n_remaining
        if n_restored or n_remaining:
            print(
                f"{data['paper_id']}: 恢复 {n_restored} 条"
                + (f"（{', '.join(restored)}）" if restored else "")
                + f"；剩余 unresolved {n_remaining} 条"
                + (f"（{', '.join(failed)}）" if failed else "")
            )
        updated_text = json.dumps(data, ensure_ascii=False, indent=2)
        if not args.dry_run and updated_text != original_text.rstrip("\n"):
            path.write_text(updated_text, encoding="utf-8")

    action = "预览（未写回）" if args.dry_run else "已写回"
    print(f"\n共恢复 include {total_restored} 条；维持 unresolved {total_remaining} 条；{action}")


if __name__ == "__main__":
    main()
