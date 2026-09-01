"""将确定无效的 PDF 和字节完全相同的冗余副本移入可恢复隔离区。"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from collections import defaultdict
from pathlib import Path
from typing import Any, Sequence

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PDF_DIR = PROJECT_ROOT / "marker提取" / "pdf"
DEFAULT_AUDIT = PROJECT_ROOT / "marker提取" / "paper_map.audit.json"
DEFAULT_QUARANTINE = (
    PROJECT_ROOT / "marker提取" / "pdf-quarantine"
)


def filename_pmid(filename: str) -> str:
    match = re.search(r"(?:^|[^a-z0-9])PMID[_ -]?(\d{7,9})(?:[^0-9]|$)", filename, re.IGNORECASE)
    return match.group(1) if match else ""


def encoded_doi_in_filename(doi: str, filename: str) -> bool:
    if not doi:
        return False
    encoded = re.sub(r"[^a-z0-9._-]+", "_", doi, flags=re.IGNORECASE)
    return encoded.casefold() in filename.casefold()


def canonical_rank(record: dict[str, Any]) -> tuple[int, int, int, str]:
    """优先保留文件名身份、登记身份和正文身份一致的副本。"""
    score = 0
    pmid = filename_pmid(str(record.get("filename", "")))
    registry_pmid = str(record.get("registry_pmid", ""))
    registry_doi = str(record.get("registry_doi", ""))
    match_basis = set(record.get("match_basis") or [])
    if pmid and pmid == registry_pmid:
        score += 100
    if encoded_doi_in_filename(registry_doi, str(record.get("filename", ""))):
        score += 80
    if "registry_path" in match_basis:
        score += 40
    if "primary_pdf_doi" in match_basis or "pdf_pmid" in match_basis:
        score += 20
    # 负号用于 sorted() 升序时把高分放前面。
    return (-score, -int(record.get("page_count") or 0), -int(record.get("file_size") or 0), str(record["filename"]).casefold())


def plan_quarantine(records: Sequence[dict[str, Any]]) -> list[dict[str, str]]:
    actions: list[dict[str, str]] = []
    invalid_names = {
        str(record["filename"])
        for record in records
        if "pdf_read_error" in set(record.get("issues") or [])
    }
    for record in records:
        filename = str(record["filename"])
        if filename in invalid_names:
            actions.append({
                "filename": filename,
                "reason": "invalid_pdf_content",
                "sha256": str(record.get("sha256", "")),
                "paper_id": str(record.get("paper_id", "")),
                "canonical_filename": "",
                "subdirectory": "invalid-content",
            })

    by_hash: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        if str(record["filename"]) not in invalid_names:
            by_hash[str(record.get("sha256", ""))].append(record)
    for group in by_hash.values():
        if len(group) < 2:
            continue
        canonical = sorted(group, key=canonical_rank)[0]
        for record in group:
            if record is canonical:
                continue
            actions.append({
                "filename": str(record["filename"]),
                "reason": "byte_identical_duplicate",
                "sha256": str(record.get("sha256", "")),
                "paper_id": str(record.get("paper_id", "")),
                "canonical_filename": str(canonical["filename"]),
                "subdirectory": "exact-duplicates",
            })
    return sorted(actions, key=lambda action: (action["subdirectory"], action["filename"].casefold()))


def ensure_within(path: Path, root: Path) -> Path:
    resolved = path.resolve()
    resolved.relative_to(root.resolve())
    return resolved


def apply_actions(
    actions: Sequence[dict[str, str]],
    pdf_dir: Path,
    quarantine_dir: Path,
) -> list[dict[str, str]]:
    project_root = PROJECT_ROOT.resolve()
    source_root = ensure_within(pdf_dir, project_root)
    destination_root = ensure_within(quarantine_dir, project_root)
    completed: list[dict[str, str]] = []
    for action in actions:
        source = ensure_within(source_root / action["filename"], source_root)
        destination_dir = ensure_within(destination_root / action["subdirectory"], destination_root)
        destination = ensure_within(destination_dir / action["filename"], destination_root)
        if not source.is_file():
            raise FileNotFoundError(f"待隔离文件不存在: {source}")
        destination_dir.mkdir(parents=True, exist_ok=True)
        if destination.exists():
            raise FileExistsError(f"隔离目标已存在，拒绝覆盖: {destination}")
        shutil.move(str(source), str(destination))
        completed.append({**action, "source": str(source), "destination": str(destination)})
    return completed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="隔离无效 PDF 和字节完全相同的冗余副本")
    parser.add_argument("--audit", type=Path, default=DEFAULT_AUDIT)
    parser.add_argument("--pdf-dir", type=Path, default=DEFAULT_PDF_DIR)
    parser.add_argument("--quarantine-dir", type=Path, default=DEFAULT_QUARANTINE)
    parser.add_argument("--apply", action="store_true", help="实际移动文件；默认只输出计划")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    payload = json.loads(args.audit.read_text(encoding="utf-8"))
    actions = plan_quarantine(payload["records"])
    print(json.dumps({"apply": args.apply, "count": len(actions), "actions": actions}, ensure_ascii=False, indent=2))
    if not args.apply:
        return 0

    completed = apply_actions(actions, args.pdf_dir, args.quarantine_dir)
    manifest = {
        "source_audit": str(args.audit),
        "action_count": len(completed),
        "invalid_content_count": sum(item["reason"] == "invalid_pdf_content" for item in completed),
        "exact_duplicate_count": sum(item["reason"] == "byte_identical_duplicate" for item in completed),
        "actions": completed,
    }
    args.quarantine_dir.mkdir(parents=True, exist_ok=True)
    (args.quarantine_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
