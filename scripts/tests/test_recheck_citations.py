from __future__ import annotations

import sys
import unittest
from pathlib import Path
from typing import Any

MODULE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_DIR))

from recheck_citations import recheck_paper  # noqa: E402

CONCATENATED_MARKDOWN = """\
( 2024)1 5:8585 10 Article https://doi.org/10.1038/s41467-024-52052-8
wasaccompaniedby wayforthisFactor, anincreasednuclearexpressionofthesenescencemarkerp21starting
painprogression(Fig.2j).Notably, thedistributionofthep53,p21,and p16tumor
"""
CONCATENATED_CONTEXT = (
    "the injury was accompanied by an increased nuclear expression of the "
    "senescence marker p21 starting from day 7 post-injury"
)


def downgraded_marker(**overrides: Any) -> dict:
    base = {
        "cell_type": "senescent nociceptors",
        "subtype": None,
        "species": "human",
        "in_project_scope": True,
        "original_symbol": "p21",
        "normalized_symbol": "CDKN1A",
        "normalization_status": "alias_resolved",
        "evidence_type": "author_declared",
        "marker_polarity": "positive",
        "source_locator": "Results; Fig.2j",
        "source_context": CONCATENATED_CONTEXT,
        "decision": "unresolved",
        "reason": (
            "作者将 p21 作为 senescence marker 并在损伤后 DRG 中验证"
            "; 自动校验：source_context 与 Markdown 词元覆盖率 0.71 低于 0.72"
        ),
        "citation_match_score": 0.71,
        "citation_verified": False,
    }
    base.update(overrides)
    return base


def audit_payload(markers: list[dict], paper_status: str = "corrected") -> dict:
    issues: list[dict] = []
    if any(m["decision"] == "unresolved" for m in markers):
        issues.append(
            {
                "severity": "error",
                "issue_type": "citation",
                "description": "1 条拟纳入 Marker 未通过 Markdown 原文回溯校验，已降级为 unresolved",
            }
        )
    return {
        "audit_version": 1,
        "paper_id": "P_TEST",
        "paper_status": paper_status,
        "summary": "测试",
        "markers": markers,
        "issues": issues,
    }


class RecheckPaperTests(unittest.TestCase):
    def test_citation_downgraded_marker_is_restored(self) -> None:
        data = audit_payload([downgraded_marker()])
        restored, failed, n_restored, n_remaining = recheck_paper(data, CONCATENATED_MARKDOWN)
        marker = data["markers"][0]
        self.assertEqual(n_restored, 1)
        self.assertEqual(n_remaining, 0)
        self.assertEqual(restored, ["CDKN1A"])
        self.assertEqual(failed, [])
        self.assertEqual(marker["decision"], "include")
        self.assertTrue(marker["citation_verified"])
        self.assertEqual(marker["citation_recheck"], "despaced_window")
        self.assertNotIn("自动校验", marker["reason"])
        self.assertIn("自动复核", marker["reason"])
        self.assertEqual(data["issues"], [])

    def test_marker_without_textual_match_stays_unresolved(self) -> None:
        marker = downgraded_marker(
            source_context="quantitative volumetric fractal immunomorphometric paracrine cascades",
            reason="证据存疑; 自动校验：source_context 与 Markdown 词元覆盖率 0.10 低于 0.72",
        )
        data = audit_payload([marker])
        _, failed, n_restored, n_remaining = recheck_paper(data, CONCATENATED_MARKDOWN)
        self.assertEqual(n_restored, 0)
        self.assertEqual(n_remaining, 1)
        self.assertEqual(failed, [marker["normalized_symbol"]])
        self.assertEqual(marker["decision"], "unresolved")
        self.assertFalse(marker["citation_verified"])
        self.assertTrue(any(i["issue_type"] == "citation" for i in data["issues"]))
        self.assertIn("维持 unresolved", data["issues"][0]["description"])

    def test_out_of_catalog_marker_is_restored_when_evidence_passes(self) -> None:
        marker = downgraded_marker(in_project_scope=False)
        data = audit_payload([marker])
        _, _, n_restored, _ = recheck_paper(data, CONCATENATED_MARKDOWN)
        self.assertEqual(n_restored, 1)
        self.assertEqual(marker["decision"], "include")
        self.assertTrue(marker["citation_verified"])

    def test_semantic_unresolved_is_untouched(self) -> None:
        marker = downgraded_marker(
            decision="unresolved",
            reason="NRXN 是家族名，无法唯一解析",
            citation_verified=True,
        )
        data = audit_payload([marker])
        recheck_paper(data, CONCATENATED_MARKDOWN)
        self.assertEqual(marker["decision"], "unresolved")
        self.assertNotIn("citation_recheck", marker)

    def test_no_formal_paper_is_promoted_after_restore(self) -> None:
        data = audit_payload([downgraded_marker()], paper_status="no_formal_marker")
        recheck_paper(data, CONCATENATED_MARKDOWN)
        self.assertEqual(data["paper_status"], "corrected")
        self.assertIn("恢复正式 Marker", data["summary"])


if __name__ == "__main__":
    unittest.main()
