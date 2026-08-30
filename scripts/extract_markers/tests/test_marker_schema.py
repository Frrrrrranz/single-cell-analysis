from __future__ import annotations

import csv
import json
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_DIR))

from gen_review_sheet import generate_review_sheet  # noqa: E402
from marker_schema import (  # noqa: E402
    MarkerSchemaError,
    apply_evidence_guardrail,
    candidate_class_for,
    has_subpopulation_syntax,
    validate_payload,
)
from run_extraction import merge_json_results  # noqa: E402


def payload(markers: list[dict], *, species: str = "rat") -> dict:
    return {
        "schema_version": 2,
        "paper_id": "P1",
        "document_id": "D1",
        "document_role": "primary",
        "cell_types": [
            {
                "cell_type": "Schwann cell",
                "subtype": None,
                "species": species,
                "is_pns_cell": "true",
                "markers": markers,
            }
        ],
    }


def marker(
    evidence_type: str,
    *,
    polarity: str = "positive",
    context: str = "Mpz is an author-declared marker for Schwann cells",
) -> dict:
    return {
        "gene": "Mpz",
        "evidence_type": evidence_type,
        "marker_polarity": polarity,
        "source_locator": "Results p.5",
        "source_context": context,
    }


class MarkerSchemaTests(unittest.TestCase):
    def test_candidate_class_separates_author_marker_from_deg(self) -> None:
        self.assertEqual(candidate_class_for("author_declared"), "formal_candidate")
        self.assertEqual(candidate_class_for("cluster_enriched"), "context_only")

    def test_missing_source_locator_is_rejected(self) -> None:
        invalid = payload([marker("author_declared")])
        invalid["cell_types"][0]["markers"][0]["source_locator"] = ""
        with self.assertRaises(MarkerSchemaError):
            validate_payload(invalid)

    def test_merge_keeps_stronger_evidence_and_both_polarities(self) -> None:
        weak = payload([
            marker("cluster_enriched"),
            marker("annotation_marker", polarity="negative", context="Mpz was used as a negative marker"),
        ])
        strong = payload([marker("author_declared", context="explicit marker statement")])
        merged = merge_json_results([json.dumps(weak), json.dumps(strong)])
        markers = merged["cell_types"][0]["markers"]
        self.assertEqual(len(markers), 2)
        positive = next(item for item in markers if item["marker_polarity"] == "positive")
        self.assertEqual(positive["evidence_type"], "author_declared")
        self.assertEqual(positive["candidate_class"], "formal_candidate")

    def test_figure_expression_without_marker_word_is_downgraded(self) -> None:
        normalized = apply_evidence_guardrail(
            marker("figure_labeled", context="TAC1 was expressed in H1 cells in Fig. 3A")
        )
        self.assertEqual(normalized["evidence_type"], "cluster_enriched")
        self.assertEqual(normalized["model_evidence_type"], "figure_labeled")
        self.assertEqual(normalized["candidate_class"], "context_only")

    def test_unsupported_negative_polarity_is_downgraded(self) -> None:
        normalized = apply_evidence_guardrail(
            marker("author_declared", polarity="negative", context="Mpz is a marker for Schwann cells")
        )
        self.assertEqual(normalized["marker_polarity"], "unknown")
        self.assertEqual(normalized["model_marker_polarity"], "negative")

    def test_marked_by_and_marks_phrases_are_formal(self) -> None:
        for context in (
            "neuroblasts are marked by B2m expression",
            "NEFH marks several classes of cells",
            "Markers highlighting Schwann cell identity",
        ):
            normalized = apply_evidence_guardrail(
                marker("author_declared", context=context)
            )
            self.assertEqual(normalized["evidence_type"], "author_declared", context)
            self.assertNotIn("guardrail_reason", normalized, context)

    def test_gene_plus_annotation_is_not_downgraded(self) -> None:
        normalized = apply_evidence_guardrail(
            marker("figure_labeled", context="Myelinating Schwann cells (Tgfb2+)")
        )
        self.assertEqual(normalized["evidence_type"], "figure_labeled")
        self.assertEqual(normalized["candidate_class"], "formal_candidate")

    def test_gene_high_low_subpopulation_is_not_downgraded(self) -> None:
        for context in (
            "ISL1-high interneurons form a distinct subcluster",
            "PPP2R2C-low subset was separated from the rest",
        ):
            normalized = apply_evidence_guardrail(
                marker("annotation_marker", context=context)
            )
            self.assertEqual(normalized["evidence_type"], "annotation_marker", context)

    def test_gating_syntax_is_formal_annotation(self) -> None:
        normalized = apply_evidence_guardrail(
            marker("annotation_marker", context="stroma gated on CD45−/EPCAM−")
        )
        self.assertEqual(normalized["evidence_type"], "annotation_marker")

    def test_ordinary_hyphenated_words_are_not_subpopulation_syntax(self) -> None:
        self.assertFalse(has_subpopulation_syntax("cell-type specific programs in Fig. 3A"))
        self.assertFalse(has_subpopulation_syntax("well-known genes were expressed"))
        self.assertTrue(has_subpopulation_syntax("Myelinating Schwann cells (Tgfb2+)"))
        self.assertTrue(has_subpopulation_syntax("ISL1-high interneurons"))
        self.assertTrue(has_subpopulation_syntax("gated on CD45−"))

    def test_minimal_polarity_word_keeps_negative_marker(self) -> None:
        normalized = apply_evidence_guardrail(
            marker(
                "annotation_marker",
                polarity="negative",
                context="PHOX2B-minimal population defined by the authors",
            )
        )
        self.assertEqual(normalized["marker_polarity"], "negative")

    def test_plain_expression_with_plus_symbol_stays_downgraded(self) -> None:
        normalized = apply_evidence_guardrail(
            marker("annotation_marker", context="proliferation was increased in the treated group")
        )
        self.assertEqual(normalized["evidence_type"], "cluster_enriched")
        self.assertEqual(normalized["candidate_class"], "context_only")

    def test_review_sheet_excludes_context_only_by_rule(self) -> None:
        data = payload([marker("author_declared"), {**marker("cluster_enriched"), "gene": "Sox10"}])
        with tempfile.TemporaryDirectory() as temp_dir:
            directory = Path(temp_dir)
            source = directory / "D1_raw.json"
            source.write_text(json.dumps(data), encoding="utf-8")
            output = generate_review_sheet(source, directory)
            with output.open("r", encoding="utf-8-sig", newline="") as stream:
                rows = list(csv.DictReader(stream))
        statuses = {row["gene_symbol"]: row["review_status"] for row in rows}
        self.assertEqual(statuses["Mpz"], "pending")
        self.assertEqual(statuses["Sox10"], "excluded_by_rule")


if __name__ == "__main__":
    unittest.main()
