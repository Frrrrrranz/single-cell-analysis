"""审计论文 PDF 身份，并在零冲突时生成确定性的 paper_map.json。"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import logging
import re
import unicodedata
from collections import defaultdict
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path, PureWindowsPath
from typing import Iterable, Sequence

try:
    from pypdf import PdfReader
except ImportError:  # 兼容项目原有依赖
    from PyPDF2 import PdfReader

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PDF_DIR = PROJECT_ROOT / "db" / "cellxgene" / "cellxgene_filtered" / "downloads"
DEFAULT_REGISTRY = PROJECT_ROOT / "db" / "cellxgene" / "paper_registry.json"
DEFAULT_AUDIT_JSON = PROJECT_ROOT / "db" / "cellxgene" / "paper_map.audit.json"
DEFAULT_AUDIT_CSV = PROJECT_ROOT / "db" / "cellxgene" / "paper_map.audit.csv"
DEFAULT_MAP = PROJECT_ROOT / "db" / "cellxgene" / "paper_map.json"
DEFAULT_DOCUMENT_OVERRIDES = PROJECT_ROOT / "db" / "cellxgene" / "document_overrides.json"

DOI_PATTERN = re.compile(r"10\.\d{4,9}/[-._;()/:a-z0-9]+", re.IGNORECASE)
PMID_PATTERN = re.compile(r"\bPMID\s*[:#]?\s*(\d{7,9})\b", re.IGNORECASE)
FILENAME_PMID_PATTERN = re.compile(r"(?:^|[^a-z0-9])PMID[_ -]?(\d{7,9})(?:[^0-9]|$)", re.IGNORECASE)
TRAILING_DOI_PUNCTUATION = ".,;:!?]}>'\""
MIN_TITLE_MATCH = 0.88
MIN_STRONG_TITLE_MATCH = 0.94
MIN_SCORE = 120
MIN_SCORE_MARGIN = 30

BLOCKING_ISSUES = {
    "ambiguous_match",
    "duplicate_content",
    "duplicate_paper_id",
    "document_override_mismatch",
    "no_registry_match",
    "pdf_read_error",
    "primary_doi_mismatch",
    "weak_identity_evidence",
}


def normalize_doi(value: object) -> str:
    """将 DOI、doi.org URL 或带 DOI 前缀的文本归一化。"""
    if value is None:
        return ""
    text = unicodedata.normalize("NFKC", str(value)).strip().lower()
    text = re.sub(r"^(?:https?://)?(?:dx\.)?doi\.org/", "", text)
    text = re.sub(r"^doi\s*:\s*", "", text)
    match = DOI_PATTERN.search(text)
    if not match:
        return ""
    return match.group(0).rstrip(TRAILING_DOI_PUNCTUATION)


def normalize_pmid(value: object) -> str:
    if value is None:
        return ""
    text = unicodedata.normalize("NFKC", str(value)).strip()
    if text.endswith(".0"):
        text = text[:-2]
    match = re.search(r"\b(\d{7,9})\b", text)
    return match.group(1) if match else ""


def normalize_title(value: object) -> str:
    if value is None:
        return ""
    text = unicodedata.normalize("NFKD", str(value)).lower()
    text = "".join(char for char in text if not unicodedata.combining(char))
    return " ".join(re.findall(r"[a-z0-9]+", text))


def canonical_paper_id(doi: str, pmid: str, title: str) -> str:
    if doi:
        safe_doi = re.sub(r"[^a-z0-9._-]+", "_", doi, flags=re.IGNORECASE).strip("_")
        return f"DOI_{safe_doi}"
    if pmid:
        return f"PMID_{pmid}"
    safe_title = re.sub(r"[^a-z0-9]+", "_", normalize_title(title), flags=re.IGNORECASE)
    return f"TITLE_{safe_title[:80].strip('_')}"


def path_basename(value: object) -> str:
    if value is None:
        return ""
    text = str(value).strip()
    if not text:
        return ""
    return PureWindowsPath(text).name.casefold()


def ordered_unique(values: Iterable[str]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        if value and value not in seen:
            seen.add(value)
            result.append(value)
    return result


@dataclass
class RegistryPaper:
    key: str
    doi: str
    pmid: str
    title: str
    dataset_ids: set[str] = field(default_factory=set)
    expected_filenames: set[str] = field(default_factory=set)
    download_expected: bool = False

    @property
    def paper_id(self) -> str:
        return canonical_paper_id(self.doi, self.pmid, self.title)


@dataclass
class PdfEvidence:
    filename: str
    sha256: str
    file_size: int
    page_count: int
    metadata_title: str
    first_pages_text: str
    observed_dois: list[str]
    observed_pmids: list[str]
    filename_pmids: list[str]
    read_error: str = ""


@dataclass
class MatchResult:
    evidence: PdfEvidence
    paper: RegistryPaper | None
    score: int
    title_score: float
    match_basis: list[str]
    issues: list[str]
    document_role: str = "primary"
    document_id: str = ""

    @property
    def status(self) -> str:
        if any(issue in BLOCKING_ISSUES for issue in self.issues):
            return "blocked"
        return "verified"


def load_cached_results(
    audit_path: Path,
    papers: Sequence[RegistryPaper],
) -> dict[str, MatchResult]:
    """复用已验证且登记身份未变化的 PDF 证据，避免反复解析大型旧文件。"""
    if not audit_path.exists():
        return {}

    payload = json.loads(audit_path.read_text(encoding="utf-8"))
    records = payload.get("records", [])
    if not isinstance(records, list):
        raise ValueError("缓存审计 JSON 的 records 必须是数组")

    papers_by_id = {paper.paper_id: paper for paper in papers}
    cached: dict[str, MatchResult] = {}
    cross_file_issues = {"duplicate_content", "duplicate_paper_id"}
    for record in records:
        if not isinstance(record, dict) or record.get("status") != "verified":
            continue
        filename = str(record.get("filename") or "")
        paper = papers_by_id.get(str(record.get("paper_id") or ""))
        if not filename or paper is None:
            continue
        registry_identity = (
            str(record.get("registry_doi") or ""),
            str(record.get("registry_pmid") or ""),
            str(record.get("registry_title") or ""),
        )
        if registry_identity != (paper.doi, paper.pmid, paper.title):
            continue

        evidence = PdfEvidence(
            filename=filename,
            sha256=str(record.get("sha256") or ""),
            file_size=int(record.get("file_size") or 0),
            page_count=int(record.get("page_count") or 0),
            metadata_title=str(record.get("metadata_title") or ""),
            first_pages_text="",
            observed_dois=[str(value) for value in record.get("observed_dois", [])],
            observed_pmids=[str(value) for value in record.get("observed_pmids", [])],
            filename_pmids=ordered_unique(
                match.group(1) for match in FILENAME_PMID_PATTERN.finditer(filename)
            ),
            read_error=str(record.get("read_error") or ""),
        )
        issues = [
            str(issue)
            for issue in record.get("issues", [])
            if str(issue) not in cross_file_issues
        ]
        cached[filename] = MatchResult(
            evidence=evidence,
            paper=paper,
            score=int(record.get("score") or 0),
            title_score=float(record.get("title_score") or 0.0),
            match_basis=[str(value) for value in record.get("match_basis", [])],
            issues=issues,
        )
    return cached


def load_registry(registry_path: Path) -> list[RegistryPaper]:
    payload = json.loads(registry_path.read_text(encoding="utf-8"))
    records = payload.get("records")
    if not isinstance(records, list):
        raise ValueError("registry JSON 缺少 records 数组")

    grouped: dict[str, RegistryPaper] = {}
    for index, row in enumerate(records, start=2):
        if not isinstance(row, dict):
            raise ValueError(f"registry 第 {index} 行不是对象")
        doi = normalize_doi(row.get("doi"))
        pmid = normalize_pmid(row.get("PMID"))
        title = str(row.get("Publication_Title") or row.get("collection_name") or "").strip()
        if not doi and not pmid and not title:
            logger.warning("跳过无论文身份的登记行: %s", index)
            continue
        key = f"doi:{doi}" if doi else f"pmid:{pmid}" if pmid else f"title:{normalize_title(title)}"
        paper = grouped.get(key)
        if paper is None:
            paper = RegistryPaper(key=key, doi=doi, pmid=pmid, title=title)
            grouped[key] = paper
        elif pmid and paper.pmid and pmid != paper.pmid:
            raise ValueError(f"同一 DOI 登记了不同 PMID: {doi} -> {paper.pmid}, {pmid}")
        elif not paper.pmid:
            paper.pmid = pmid

        dataset_id = str(row.get("dataset_id") or "").strip()
        if dataset_id:
            paper.dataset_ids.add(dataset_id)
        basename = path_basename(row.get("本地PDF路径"))
        if basename:
            paper.expected_filenames.add(basename)
        if str(row.get("是否下载成功(Y/N)") or "").strip().upper() == "Y":
            paper.download_expected = True

    return sorted(grouped.values(), key=lambda paper: paper.paper_id)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def extract_pdf_evidence(path: Path, page_limit: int = 3) -> PdfEvidence:
    file_hash = sha256_file(path)
    metadata_title = ""
    text_parts: list[str] = []
    page_count = 0
    read_error = ""
    try:
        reader = PdfReader(str(path), strict=False)
        page_count = len(reader.pages)
        metadata = reader.metadata or {}
        metadata_title = str(metadata.get("/Title") or "").strip()
        for page in reader.pages[:page_limit]:
            try:
                text_parts.append(page.extract_text() or "")
            except Exception as exc:  # 单页损坏不应中断其余证据提取
                logger.warning("PDF 单页文本提取失败 %s: %s", path.name, exc)
    except Exception as exc:
        read_error = f"{type(exc).__name__}: {exc}"

    first_pages_text = "\n".join(text_parts)
    identifier_text = "\n".join((metadata_title, first_pages_text))
    observed_dois = ordered_unique(normalize_doi(match.group(0)) for match in DOI_PATTERN.finditer(identifier_text))
    observed_pmids = ordered_unique(match.group(1) for match in PMID_PATTERN.finditer(identifier_text))
    filename_pmids = ordered_unique(match.group(1) for match in FILENAME_PMID_PATTERN.finditer(path.name))
    return PdfEvidence(
        filename=path.name,
        sha256=file_hash,
        file_size=path.stat().st_size,
        page_count=page_count,
        metadata_title=metadata_title,
        first_pages_text=first_pages_text,
        observed_dois=observed_dois,
        observed_pmids=observed_pmids,
        filename_pmids=filename_pmids,
        read_error=read_error,
    )


def title_similarity(expected_title: str, evidence: PdfEvidence) -> float:
    expected = normalize_title(expected_title)
    if not expected:
        return 0.0
    text = normalize_title(evidence.first_pages_text)
    if expected in text:
        return 1.0

    filename = normalize_title(Path(evidence.filename).stem)
    metadata = normalize_title(evidence.metadata_title)
    candidates = [candidate for candidate in (filename, metadata) if candidate]
    sequence_score = max(
        (SequenceMatcher(None, expected, candidate).ratio() for candidate in candidates),
        default=0.0,
    )
    expected_tokens = set(expected.split())
    text_tokens = set(text.split())
    token_score = len(expected_tokens & text_tokens) / len(expected_tokens) if expected_tokens else 0.0
    return round(max(sequence_score, token_score if token_score >= 0.80 else 0.0), 4)


def encoded_doi_in_filename(doi: str, filename: str) -> bool:
    if not doi:
        return False
    encoded = re.sub(r"[^a-z0-9._-]+", "_", doi, flags=re.IGNORECASE)
    return encoded.casefold() in filename.casefold()


def score_paper(paper: RegistryPaper, evidence: PdfEvidence) -> tuple[int, float, list[str]]:
    score = 0
    basis: list[str] = []
    title_score = title_similarity(paper.title, evidence)

    if paper.doi and evidence.observed_dois:
        if paper.doi == evidence.observed_dois[0]:
            score += 220
            basis.append("primary_pdf_doi")
        elif paper.doi in evidence.observed_dois:
            score += 90
            basis.append("secondary_pdf_doi")
    if paper.pmid and paper.pmid in evidence.observed_pmids:
        score += 190
        basis.append("pdf_pmid")
    if paper.doi and encoded_doi_in_filename(paper.doi, evidence.filename):
        score += 120
        basis.append("filename_doi")
    if paper.pmid and paper.pmid in evidence.filename_pmids:
        score += 120
        basis.append("filename_pmid")
    if evidence.filename.casefold() in paper.expected_filenames:
        score += 40
        basis.append("registry_path")
    if title_score >= MIN_STRONG_TITLE_MATCH:
        score += 100
        basis.append("strong_title")
    elif title_score >= MIN_TITLE_MATCH:
        score += 60
        basis.append("title")
    return score, title_score, basis


def match_pdf(evidence: PdfEvidence, papers: Sequence[RegistryPaper]) -> MatchResult:
    issues: list[str] = []
    if evidence.read_error:
        issues.append("pdf_read_error")

    ranked: list[tuple[int, float, str, RegistryPaper, list[str]]] = []
    for paper in papers:
        score, title_score, basis = score_paper(paper, evidence)
        if score:
            ranked.append((score, title_score, paper.paper_id, paper, basis))
    ranked.sort(key=lambda item: (-item[0], -item[1], item[2]))

    if not ranked or ranked[0][0] < MIN_SCORE:
        issues.append("no_registry_match")
        return MatchResult(evidence, None, 0, 0.0, [], sorted(set(issues)))

    best_score, best_title_score, _, best_paper, basis = ranked[0]
    if len(ranked) > 1 and best_score - ranked[1][0] < MIN_SCORE_MARGIN:
        issues.append("ambiguous_match")

    path_papers = [paper for paper in papers if evidence.filename.casefold() in paper.expected_filenames]
    if path_papers and best_paper not in path_papers:
        issues.append("registry_path_mismatch")
    if len({paper.paper_id for paper in path_papers}) > 1:
        issues.append("registry_path_conflict")

    filename_identifier_papers = [
        paper for paper in papers
        if encoded_doi_in_filename(paper.doi, evidence.filename)
        or (paper.pmid and paper.pmid in evidence.filename_pmids)
    ]
    if filename_identifier_papers and best_paper not in filename_identifier_papers:
        issues.append("filename_identifier_mismatch")

    primary_doi = evidence.observed_dois[0] if evidence.observed_dois else ""
    known_primary_doi = bool(primary_doi) and any(paper.doi == primary_doi for paper in papers)
    if known_primary_doi and best_paper.doi != primary_doi:
        issues.append("primary_doi_mismatch")

    strong_identity = any(item in basis for item in ("primary_pdf_doi", "pdf_pmid", "strong_title"))
    if not strong_identity:
        issues.append("weak_identity_evidence")

    return MatchResult(
        evidence=evidence,
        paper=best_paper,
        score=best_score,
        title_score=best_title_score,
        match_basis=basis,
        issues=sorted(set(issues)),
    )


def add_cross_file_issues(results: list[MatchResult]) -> None:
    by_hash: dict[str, list[MatchResult]] = defaultdict(list)
    by_document_id: dict[str, list[MatchResult]] = defaultdict(list)
    for result in results:
        by_hash[result.evidence.sha256].append(result)
        if result.document_id:
            by_document_id[result.document_id].append(result)

    for group in by_hash.values():
        if len(group) > 1:
            for result in group:
                result.issues = sorted(set(result.issues + ["duplicate_content"]))
    for group in by_document_id.values():
        if len(group) > 1:
            for result in group:
                result.issues = sorted(set(result.issues + ["duplicate_paper_id"]))


def load_document_overrides(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    documents = payload.get("documents", {})
    if not isinstance(documents, dict):
        raise ValueError("document_overrides.json 的 documents 必须是对象")
    return {
        str(filename): {str(key): str(value) for key, value in config.items()}
        for filename, config in documents.items()
        if isinstance(config, dict)
    }


def apply_document_overrides(
    results: Sequence[MatchResult],
    overrides: dict[str, dict[str, str]],
) -> None:
    valid_roles = {"primary", "supplement", "extended_data", "correction"}
    for result in results:
        config = overrides.get(result.evidence.filename, {})
        role = config.get("document_role", "primary")
        if role not in valid_roles:
            raise ValueError(f"无效 document_role: {role}")
        result.document_role = role
        if result.paper is None:
            continue
        expected_paper_id = config.get("paper_id")
        if expected_paper_id and expected_paper_id != result.paper.paper_id:
            result.issues = sorted(set(result.issues + ["document_override_mismatch"]))
        default_document_id = (
            result.paper.paper_id
            if role == "primary"
            else f"{result.paper.paper_id}__{role}_{result.evidence.sha256[:12]}"
        )
        result.document_id = config.get("document_id", default_document_id)


def result_to_dict(result: MatchResult) -> dict[str, object]:
    paper = result.paper
    return {
        "filename": result.evidence.filename,
        "sha256": result.evidence.sha256,
        "file_size": result.evidence.file_size,
        "page_count": result.evidence.page_count,
        "status": result.status,
        "paper_id": paper.paper_id if paper else "",
        "document_id": result.document_id,
        "document_role": result.document_role,
        "registry_doi": paper.doi if paper else "",
        "registry_pmid": paper.pmid if paper else "",
        "registry_title": paper.title if paper else "",
        "observed_dois": result.evidence.observed_dois,
        "observed_pmids": result.evidence.observed_pmids,
        "metadata_title": result.evidence.metadata_title,
        "score": result.score,
        "title_score": result.title_score,
        "match_basis": result.match_basis,
        "issues": result.issues,
        "read_error": result.evidence.read_error,
    }


def write_audit(
    results: Sequence[MatchResult],
    papers: Sequence[RegistryPaper],
    registry_path: Path,
    json_path: Path,
    csv_path: Path,
) -> None:
    records = [result_to_dict(result) for result in results]
    issue_counts: dict[str, int] = defaultdict(int)
    for result in results:
        for issue in result.issues:
            issue_counts[issue] += 1
    expected_ids = {paper.paper_id for paper in papers if paper.download_expected}
    available_ids = {
        result.paper.paper_id
        for result in results
        if result.paper is not None and "pdf_read_error" not in result.issues
    }
    missing_expected = [
        {
            "paper_id": paper.paper_id,
            "doi": paper.doi,
            "pmid": paper.pmid,
            "title": paper.title,
            "expected_filenames": sorted(paper.expected_filenames),
        }
        for paper in papers
        if paper.paper_id in expected_ids - available_ids
    ]
    payload = {
        "registry": str(registry_path),
        "pdf_count": len(results),
        "verified_count": sum(result.status == "verified" for result in results),
        "blocked_count": sum(result.status == "blocked" for result in results),
        "issue_counts": dict(sorted(issue_counts.items())),
        "registry_expected_paper_count": len(expected_ids),
        "content_available_paper_count": len(expected_ids & available_ids),
        "missing_expected_paper_count": len(missing_expected),
        "missing_expected_papers": missing_expected,
        "records": records,
    }
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    columns = [
        "filename", "sha256", "file_size", "page_count", "status", "paper_id", "document_id", "document_role",
        "registry_doi", "registry_pmid", "registry_title", "observed_dois",
        "observed_pmids", "metadata_title", "score", "title_score", "match_basis",
        "issues", "read_error",
    ]
    with csv_path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns)
        writer.writeheader()
        for record in records:
            row = dict(record)
            for key in ("observed_dois", "observed_pmids", "match_basis", "issues"):
                row[key] = ";".join(str(value) for value in record[key])
            writer.writerow(row)


def build_paper_map(results: Sequence[MatchResult]) -> dict[str, dict[str, str]]:
    blocked = [result.evidence.filename for result in results if result.status != "verified"]
    if blocked:
        raise ValueError(f"仍有 {len(blocked)} 个 PDF 未通过身份审计，拒绝生成正式 paper_map.json")
    mapping = {
        result.evidence.filename: {
            "paper_id": result.paper.paper_id,
            "document_id": result.document_id,
            "document_role": result.document_role,
            "sha256": result.evidence.sha256,
        }
        for result in results
        if result.paper is not None
    }
    if len(mapping) != len(results):
        raise ValueError("映射数量与 PDF 数量不一致")
    document_ids = [entry["document_id"] for entry in mapping.values()]
    if len(set(document_ids)) != len(document_ids):
        raise ValueError("document_id 不是一一映射")
    return dict(sorted(mapping.items()))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="审计 PDF 论文身份并生成无冲突 paper_map.json")
    parser.add_argument("--pdf-dir", type=Path, default=DEFAULT_PDF_DIR)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--audit-json", type=Path, default=DEFAULT_AUDIT_JSON)
    parser.add_argument("--audit-csv", type=Path, default=DEFAULT_AUDIT_CSV)
    parser.add_argument("--map-output", type=Path, default=DEFAULT_MAP)
    parser.add_argument("--document-overrides", type=Path, default=DEFAULT_DOCUMENT_OVERRIDES)
    parser.add_argument("--page-limit", type=int, default=3)
    parser.add_argument(
        "--reuse-audit",
        action="store_true",
        help="复用 --audit-json 中 SHA256 和登记身份均未变化的 verified 结果",
    )
    parser.add_argument("--write-map", action="store_true", help="仅在全部 PDF 通过时写出正式映射")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    papers = load_registry(args.registry)
    overrides = load_document_overrides(args.document_overrides)
    cached_results = load_cached_results(args.audit_json, papers) if args.reuse_audit else {}
    pdf_paths = sorted(args.pdf_dir.glob("*.pdf"), key=lambda path: path.name.casefold())
    logger.info(
        "登记论文身份: %d；PDF: %d；可复用审计: %d",
        len(papers),
        len(pdf_paths),
        len(cached_results),
    )

    results: list[MatchResult] = []
    for index, pdf_path in enumerate(pdf_paths, start=1):
        logger.info("[%d/%d] 审计 %s", index, len(pdf_paths), pdf_path.name)
        cached = cached_results.get(pdf_path.name)
        if (
            cached is not None
            and cached.evidence.file_size == pdf_path.stat().st_size
            and cached.evidence.sha256 == sha256_file(pdf_path)
        ):
            logger.info("复用已验证审计证据: %s", pdf_path.name)
            results.append(cached)
            continue
        evidence = extract_pdf_evidence(pdf_path, page_limit=args.page_limit)
        results.append(match_pdf(evidence, papers))
    apply_document_overrides(results, overrides)
    add_cross_file_issues(results)
    write_audit(results, papers, args.registry, args.audit_json, args.audit_csv)

    blocked_count = sum(result.status == "blocked" for result in results)
    logger.info("审计完成：verified=%d, blocked=%d", len(results) - blocked_count, blocked_count)
    logger.info("审计报告：%s；%s", args.audit_json, args.audit_csv)
    if args.write_map:
        try:
            mapping = build_paper_map(results)
        except ValueError as exc:
            logger.error("%s", exc)
            return 2
        args.map_output.write_text(json.dumps(mapping, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        logger.info("正式映射已写出：%s", args.map_output)
    return 0 if blocked_count == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
