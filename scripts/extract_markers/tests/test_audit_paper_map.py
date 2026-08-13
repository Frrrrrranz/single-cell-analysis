from __future__ import annotations

import sys
import json
import tempfile
import unittest
from pathlib import Path

MODULE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_DIR))

from audit_paper_map import (  # noqa: E402
    MatchResult,
    PdfEvidence,
    RegistryPaper,
    add_cross_file_issues,
    apply_document_overrides,
    build_paper_map,
    canonical_paper_id,
    load_cached_results,
    match_pdf,
    normalize_doi,
)
from quarantine_pdf_issues import plan_quarantine  # noqa: E402
from run_extraction import load_paper_map  # noqa: E402


def evidence(
    filename: str,
    *,
    sha256: str = "a" * 64,
    dois: list[str] | None = None,
    pmids: list[str] | None = None,
    filename_pmids: list[str] | None = None,
    text: str = "",
) -> PdfEvidence:
    return PdfEvidence(
        filename=filename,
        sha256=sha256,
        file_size=100,
        page_count=10,
        metadata_title="",
        first_pages_text=text,
        observed_dois=dois or [],
        observed_pmids=pmids or [],
        filename_pmids=filename_pmids or [],
    )


class NormalizeIdentifierTests(unittest.TestCase):
    def test_normalize_doi_url_and_trailing_punctuation(self) -> None:
        self.assertEqual(
            normalize_doi("https://doi.org/10.1038/S41586-020-2496-1."),
            "10.1038/s41586-020-2496-1",
        )

    def test_canonical_paper_id(self) -> None:
        self.assertEqual(
            canonical_paper_id("10.1016/j.cell.2022.11.005", "", ""),
            "DOI_10.1016_j.cell.2022.11.005",
        )


class MappingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.actual = RegistryPaper(
            key="doi:10.1038/s41586-020-2496-1",
            doi="10.1038/s41586-020-2496-1",
            pmid="32669714",
            title="A single-cell transcriptomic atlas characterizes ageing tissues in the mouse",
            expected_filenames={"pmid_32669714_correct.pdf"},
        )
        self.wrong_filename = RegistryPaper(
            key="doi:10.1126/science.abl4896",
            doi="10.1126/science.abl4896",
            pmid="00000000",
            title="A different paper",
            expected_filenames={"doi_10.1126_science.abl4896.pdf"},
        )

    def test_pdf_content_doi_wins_over_wrong_filename(self) -> None:
        result = match_pdf(
            evidence(
                "DOI_10.1126_science.abl4896.pdf",
                dois=[self.actual.doi],
                text=self.actual.title,
            ),
            [self.actual, self.wrong_filename],
        )
        self.assertEqual(result.paper, self.actual)
        self.assertIn("registry_path_mismatch", result.issues)
        self.assertIn("filename_identifier_mismatch", result.issues)
        self.assertEqual(result.status, "verified")

    def test_duplicate_paper_id_blocks_both_files(self) -> None:
        first = match_pdf(
            evidence("first.pdf", sha256="a" * 64, dois=[self.actual.doi], text=self.actual.title),
            [self.actual],
        )
        second = match_pdf(
            evidence("second.pdf", sha256="b" * 64, dois=[self.actual.doi], text=self.actual.title),
            [self.actual],
        )
        apply_document_overrides([first, second], {})
        add_cross_file_issues([first, second])
        self.assertIn("duplicate_paper_id", first.issues)
        self.assertIn("duplicate_paper_id", second.issues)
        with self.assertRaisesRegex(ValueError, "未通过身份审计"):
            build_paper_map([first, second])

    def test_duplicate_content_blocks_different_files(self) -> None:
        first = MatchResult(evidence("first.pdf"), self.actual, 220, 1.0, ["primary_pdf_doi"], [])
        second = MatchResult(evidence("second.pdf"), self.wrong_filename, 220, 1.0, ["primary_pdf_doi"], [])
        add_cross_file_issues([first, second])
        self.assertIn("duplicate_content", first.issues)
        self.assertIn("duplicate_content", second.issues)

    def test_clean_one_to_one_mapping_is_deterministic(self) -> None:
        result = MatchResult(
            evidence("paper.pdf"),
            self.actual,
            220,
            1.0,
            ["primary_pdf_doi"],
            [],
        )
        apply_document_overrides([result], {})
        self.assertEqual(
            build_paper_map([result]),
            {
                "paper.pdf": {
                    "paper_id": self.actual.paper_id,
                    "document_id": self.actual.paper_id,
                    "document_role": "primary",
                    "sha256": "a" * 64,
                }
            },
        )

    def test_primary_and_supplement_may_share_paper_id(self) -> None:
        primary = MatchResult(
            evidence("primary.pdf", sha256="a" * 64), self.actual, 220, 1.0, ["primary_pdf_doi"], []
        )
        supplement = MatchResult(
            evidence("supplement.pdf", sha256="b" * 64), self.actual, 220, 1.0, ["primary_pdf_doi"], []
        )
        apply_document_overrides(
            [primary, supplement],
            {
                "supplement.pdf": {
                    "paper_id": self.actual.paper_id,
                    "document_role": "supplement",
                }
            },
        )
        add_cross_file_issues([primary, supplement])
        self.assertNotIn("duplicate_paper_id", primary.issues)
        self.assertNotIn("duplicate_paper_id", supplement.issues)
        self.assertNotEqual(primary.document_id, supplement.document_id)

    def test_loads_only_verified_cache_with_unchanged_registry_identity(self) -> None:
        temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(temp_dir.cleanup)
        audit_path = Path(temp_dir.name) / "audit.json"
        audit_path.write_text(
            json.dumps({
                "records": [{
                    "filename": "paper.pdf",
                    "sha256": "a" * 64,
                    "file_size": 100,
                    "page_count": 10,
                    "status": "verified",
                    "paper_id": self.actual.paper_id,
                    "registry_doi": self.actual.doi,
                    "registry_pmid": self.actual.pmid,
                    "registry_title": self.actual.title,
                    "observed_dois": [self.actual.doi],
                    "observed_pmids": [],
                    "metadata_title": self.actual.title,
                    "score": 220,
                    "title_score": 1.0,
                    "match_basis": ["primary_pdf_doi", "strong_title"],
                    "issues": ["duplicate_paper_id", "registry_path_mismatch"],
                    "read_error": "",
                }]
            }),
            encoding="utf-8",
        )

        cached = load_cached_results(audit_path, [self.actual])

        self.assertEqual(cached["paper.pdf"].paper, self.actual)
        self.assertNotIn("duplicate_paper_id", cached["paper.pdf"].issues)
        self.assertIn("registry_path_mismatch", cached["paper.pdf"].issues)

        changed = RegistryPaper(
            key=self.actual.key,
            doi=self.actual.doi,
            pmid=self.actual.pmid,
            title=f"{self.actual.title} revised",
        )
        self.assertEqual(load_cached_results(audit_path, [changed]), {})


class QuarantinePlanTests(unittest.TestCase):
    def test_keeps_duplicate_whose_filename_matches_registry_pmid(self) -> None:
        records = [
            {
                "filename": "DOI_10.1038_s41586-020-2496-1_copy.pdf",
                "sha256": "a" * 64,
                "paper_id": "DOI_10.1038_s41586-020-2496-1",
                "registry_doi": "10.1038/s41586-020-2496-1",
                "registry_pmid": "32669714",
                "page_count": 10,
                "file_size": 100,
                "match_basis": ["primary_pdf_doi"],
                "issues": ["duplicate_content"],
            },
            {
                "filename": "PMID_32669714_correct.pdf",
                "sha256": "a" * 64,
                "paper_id": "DOI_10.1038_s41586-020-2496-1",
                "registry_doi": "10.1038/s41586-020-2496-1",
                "registry_pmid": "32669714",
                "page_count": 10,
                "file_size": 100,
                "match_basis": ["primary_pdf_doi", "registry_path"],
                "issues": ["duplicate_content"],
            },
        ]
        actions = plan_quarantine(records)
        self.assertEqual(len(actions), 1)
        self.assertEqual(actions[0]["filename"], "DOI_10.1038_s41586-020-2496-1_copy.pdf")
        self.assertEqual(actions[0]["canonical_filename"], "PMID_32669714_correct.pdf")

    def test_invalid_pdf_is_quarantined_without_duplicate_processing(self) -> None:
        records = [
            {
                "filename": "bad.pdf",
                "sha256": "b" * 64,
                "paper_id": "PMID_12345678",
                "issues": ["pdf_read_error"],
            }
        ]
        actions = plan_quarantine(records)
        self.assertEqual(actions[0]["reason"], "invalid_pdf_content")


class ExtractionMapTests(unittest.TestCase):
    def write_map(self, payload: dict) -> Path:
        temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(temp_dir.cleanup)
        path = Path(temp_dir.name) / "paper_map.json"
        path.write_text(json.dumps(payload), encoding="utf-8")
        return path

    def test_loads_structured_primary_and_supplement(self) -> None:
        path = self.write_map({
            "primary.pdf": {
                "paper_id": "DOI_10.1_a",
                "document_id": "DOI_10.1_a",
                "document_role": "primary",
                "sha256": "a" * 64,
            },
            "supplement.pdf": {
                "paper_id": "DOI_10.1_a",
                "document_id": "DOI_10.1_a__supplement_01",
                "document_role": "supplement",
                "sha256": "b" * 64,
            },
        })
        mapping = load_paper_map(path)
        self.assertEqual(mapping["supplement.pdf"]["document_role"], "supplement")

    def test_rejects_duplicate_document_id(self) -> None:
        path = self.write_map({
            "one.pdf": {"paper_id": "P1", "document_id": "D1", "document_role": "primary"},
            "two.pdf": {"paper_id": "P1", "document_id": "D1", "document_role": "supplement"},
        })
        with self.assertRaisesRegex(ValueError, "重复 document_id"):
            load_paper_map(path)


if __name__ == "__main__":
    unittest.main()
