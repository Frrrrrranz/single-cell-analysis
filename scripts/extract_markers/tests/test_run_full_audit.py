from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

MODULE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_DIR))

from run_full_audit import (  # noqa: E402
    CITATION_SCORE_THRESHOLD,
    context_match_score,
    despaced_window_hit,
    parse_scope_table,
    validate_audit_result,
)

MD_DIR = MODULE_DIR / "review_md"
RAW_DIR = MODULE_DIR / "markers_output_v2"
AUDITED_DIR = MODULE_DIR / "audited-extraction" / "markers"
SCOPE_FILE = MODULE_DIR / "audits" / "task-scope-2026-08-14.md"

TWO_COLUMN_MARKDOWN = """\
3 | RESULTS Table S5.
3.1 | Identification of equivalent epithelial cell
types of the prostate and urethra in the mouse vs
human
neuroendocrine epithelia are an extremely rare cell type that do not
independently, but can be identified using known markers such as
CGRP and CHGA (Figure S3A,C).
"""
REAL_CONTEXT = (
    "neuroendocrine epithelia are an extremely rare cell type that do not cluster "
    "independently, but can be identified using known markers such as CGRP and CHGA"
)


def marker_result(**overrides) -> dict:
    base = {
        "cell_type": "neuroendocrine epithelia",
        "subtype": None,
        "species": "human",
        "in_project_scope": True,
        "original_symbol": "CHGA",
        "normalized_symbol": "CHGA",
        "normalization_status": "exact",
        "evidence_type": "annotation_marker",
        "marker_polarity": "positive",
        "source_locator": "Results 3.1; Figure S3A,C",
        "source_context": REAL_CONTEXT,
        "decision": "include",
        "reason": "作者用该基因识别目标细胞",
    }
    base.update(overrides)
    return base


def audit_payload(markers: list[dict]) -> dict:
    return {
        "audit_version": 2,
        "paper_id": "P_TEST",
        "paper_status": "corrected",
        "summary": "测试",
        "markers": markers,
        "issues": [],
    }


class ContextMatchScoreTests(unittest.TestCase):
    def test_two_column_interruption_still_verifies(self) -> None:
        score = context_match_score(REAL_CONTEXT, TWO_COLUMN_MARKDOWN, "CHGA")
        self.assertGreaterEqual(score, CITATION_SCORE_THRESHOLD)

    def test_symbol_missing_from_markdown_scores_zero(self) -> None:
        self.assertEqual(context_match_score(REAL_CONTEXT, TWO_COLUMN_MARKDOWN, "ZZZ9"), 0.0)

    def test_hallucinated_context_scores_below_threshold(self) -> None:
        hallucinated = (
            "the authors performed quantitative volumetric fractal immunomorphometric "
            "reconstruction to validate paracrine signaling cascades across compartments"
        )
        score = context_match_score(hallucinated, TWO_COLUMN_MARKDOWN, "CHGA")
        self.assertLess(score, CITATION_SCORE_THRESHOLD)

    def test_empty_context_scores_zero(self) -> None:
        self.assertEqual(context_match_score("   ", TWO_COLUMN_MARKDOWN, "CHGA"), 0.0)


CONCATENATED_MARKDOWN = """\
( 2024)1 5:8585 10 Article https://doi.org/10.1038/s41467-024-52052-8
wasaccompaniedby wayforthisFactor, anincreasednuclearexpressionofthesenescencemarkerp21starting
painprogression(Fig.2j).Notably, thedistributionofthep53,p21,and p16tumor
"""
CONCATENATED_CONTEXT = (
    "the injury was accompanied by an increased nuclear expression of the "
    "senescence marker p21 starting from day 7 post-injury"
)


class DespacedWindowHitTests(unittest.TestCase):
    def test_concatenated_pdf_text_matches(self) -> None:
        self.assertTrue(despaced_window_hit(CONCATENATED_CONTEXT, CONCATENATED_MARKDOWN))

    def test_absent_text_does_not_match(self) -> None:
        hallucinated = (
            "quantitative volumetric fractal immunomorphometric paracrine cascades"
        )
        self.assertFalse(despaced_window_hit(hallucinated, CONCATENATED_MARKDOWN))

    def test_short_context_skips_fallback(self) -> None:
        self.assertFalse(despaced_window_hit("p21 marker only", CONCATENATED_MARKDOWN))

    def test_generic_legend_prefix_without_symbol_is_rejected(self) -> None:
        context = (
            "Dotplot showing the mean expression of marker genes and the percentage "
            "of cells expressing them for each annotated cell type; figure gene axis "
            "includes CDH19 with Schwann cells row."
        )
        markdown = (
            "Fig. 1d: Dotplot showing the mean expression of marker genes and the "
            "percentage of cells expressing them for each annotated cell type. "
            "Gene axis: PLP1, MPZ, MBP."
        )
        self.assertTrue(despaced_window_hit(context, markdown))
        self.assertFalse(despaced_window_hit(context, markdown, ("CDH19", "CDH19")))

    def test_window_must_contain_symbol(self) -> None:
        context = "we found the senescence marker p21 elevated after injury in DRG"
        self.assertTrue(
            despaced_window_hit(context, CONCATENATED_MARKDOWN, ("p21", "CDKN1A"))
        )
        self.assertFalse(
            despaced_window_hit(context, CONCATENATED_MARKDOWN, ("RBFOX3", "RBFOX3"))
        )

    def test_include_survives_concatenated_markdown(self) -> None:
        data = validate_audit_result(
            audit_payload([marker_result(source_context=CONCATENATED_CONTEXT, original_symbol="p21")]),
            "P_TEST",
            CONCATENATED_MARKDOWN,
        )
        marker = data["markers"][0]
        self.assertEqual(marker["decision"], "include")
        self.assertTrue(marker["citation_verified"])
        self.assertEqual(marker.get("citation_recheck"), "despaced_window")
        self.assertFalse(any(issue["issue_type"] == "citation" for issue in data["issues"]))


class ValidateAuditResultTests(unittest.TestCase):
    def test_valid_include_passes_unchanged(self) -> None:
        data = validate_audit_result(audit_payload([marker_result()]), "P_TEST", TWO_COLUMN_MARKDOWN)
        self.assertEqual(data["markers"][0]["decision"], "include")
        self.assertTrue(data["markers"][0]["citation_verified"])
        self.assertEqual(data["paper_status"], "corrected")

    def test_non_formal_evidence_is_demoted_to_context_only(self) -> None:
        data = validate_audit_result(
            audit_payload([marker_result(evidence_type="cluster_enriched")]),
            "P_TEST",
            TWO_COLUMN_MARKDOWN,
        )
        self.assertEqual(data["markers"][0]["decision"], "context_only")

    def test_ambiguous_symbol_is_demoted_to_unresolved(self) -> None:
        data = validate_audit_result(
            audit_payload([marker_result(original_symbol="CGRP", normalized_symbol="CGRP", normalization_status="ambiguous")]),
            "P_TEST",
            TWO_COLUMN_MARKDOWN,
        )
        self.assertEqual(data["markers"][0]["decision"], "unresolved")

    def test_out_of_catalog_formal_marker_is_retained(self) -> None:
        data = validate_audit_result(
            audit_payload([marker_result(in_project_scope=False)]),
            "P_TEST",
            TWO_COLUMN_MARKDOWN,
        )
        self.assertEqual(data["markers"][0]["decision"], "include")

    def test_unknown_species_is_demoted_to_unresolved(self) -> None:
        data = validate_audit_result(
            audit_payload([marker_result(species="unknown")]),
            "P_TEST",
            TWO_COLUMN_MARKDOWN,
        )
        self.assertEqual(data["markers"][0]["decision"], "unresolved")

    def test_citation_failure_demotes_marker_and_records_issue(self) -> None:
        hallucinated = "quantitative volumetric fractal immunomorphometric paracrine validation cascades"
        data = validate_audit_result(
            audit_payload([marker_result(source_context=hallucinated)]),
            "P_TEST",
            TWO_COLUMN_MARKDOWN,
        )
        self.assertEqual(data["markers"][0]["decision"], "unresolved")
        self.assertFalse(data["markers"][0]["citation_verified"])
        self.assertTrue(any(issue["issue_type"] == "citation" for issue in data["issues"]))

    def test_invalid_enum_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            validate_audit_result(
                audit_payload([marker_result(evidence_type="made_up")]),
                "P_TEST",
                TWO_COLUMN_MARKDOWN,
            )


class ScopeIntegrationTests(unittest.TestCase):
    def test_scope_table_maps_all_markdown_paper_ids(self) -> None:
        task_map = parse_scope_table(SCOPE_FILE)
        md_ids = {path.stem for path in MD_DIR.glob("*.md")}
        self.assertEqual(len(md_ids), 43, "review_md 应包含原 40 篇及新补入的 3 篇")
        missing = md_ids - set(task_map)
        self.assertEqual(missing, set(), f"任务范围表缺少 paper_id: {sorted(missing)}")
        for paper_id, task in task_map.items():
            self.assertTrue(task["catalog_cell_layers"], paper_id)
            self.assertIn(task["task_species"], {"Homo sapiens", "Mus musculus", "Rattus norvegicus", "NaN"}, paper_id)

    def test_audited_json_records_raw_provenance(self) -> None:
        for audit_path in sorted(AUDITED_DIR.glob("*_audit.json")):
            data = json.loads(audit_path.read_text(encoding="utf-8"))
            self.assertTrue(data["source_raw_json"].endswith("_raw.json"), audit_path.name)
            self.assertRegex(data["source_raw_sha256"], r"^[0-9a-f]{64}$", audit_path.name)

    def test_audited_json_source_hashes_match_current_markdown(self) -> None:
        import hashlib

        for audit_path in sorted(AUDITED_DIR.glob("*_audit.json")):
            data = json.loads(audit_path.read_text(encoding="utf-8"))
            md_path = MD_DIR / data["source_markdown"]
            self.assertTrue(md_path.exists(), f"{audit_path.name} 引用的 Markdown 不存在")
            md_hash = hashlib.sha256(md_path.read_text(encoding="utf-8").encode("utf-8")).hexdigest()
            self.assertEqual(data["source_markdown_sha256"], md_hash, f"{audit_path.name} Markdown 哈希变化")


if __name__ == "__main__":
    unittest.main()
