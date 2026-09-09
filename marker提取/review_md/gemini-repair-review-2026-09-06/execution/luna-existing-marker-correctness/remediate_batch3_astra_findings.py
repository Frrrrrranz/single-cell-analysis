from __future__ import annotations

import copy
import hashlib
import json
from datetime import date
from pathlib import Path


ROOT = Path(r"D:/OneDrive/Desktop/组")
RUN_DIR = ROOT / "marker提取/review_md/gemini-repair-review-2026-09-06/execution/luna-existing-marker-correctness"
SOURCE = ROOT / "marker提取/review_md/DOI_10.1016_j.cell.2022.11.005.md"
EXECUTOR = "GPT-5.6 Luna"
DATE = "2026-09-07"


def load(name: str):
    return json.loads((RUN_DIR / name).read_text(encoding="utf-8"))


def save(name: str, value) -> None:
    (RUN_DIR / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def support(evidence_id: str, locator: str, excerpt: str) -> dict[str, str]:
    return {"evidence_id": evidence_id, "locator": locator, "excerpt": excerpt}


SUPPORT = {
    # Second-batch records: each excerpt is a direct source fragment for the target gene.
    "M00045": support("EVID_CELL_S8C_E_NEGATIVE", "Figure S8C legend, lines 1686-1688", "GRP+NEUROD1lowGHRL- cells"),
    "M00049": support("EVID_CELL_S8C_E_NEGATIVE", "Figure S8C legend, lines 1686-1688", "GRP-NEUROD1+GHRL+"),
    "M00046": support("EVID_CELL_S8C_E_NEGATIVE", "Figure S8E legend, lines 1690-1692", "GRP+RFX6-pulmonaryNEcells"),
    "M00413": support("EVID_CELL_S7H_F_NEGATIVE", "Figure S7H legend, lines 1665-1666", "NDUFA4L2-/NTRK3+adventitialfibroblasts"),
    "M00587": support("EVID_CELL_S7H_F_NEGATIVE", "Results, lines 367-370", "vSMC1(NTRK3+,NTN4+,andPLN-)"),
    "M00593": support("EVID_CELL_S7H_F_NEGATIVE", "Figure S7F legend, lines 1662-1663", "NTN4+/PLN(cid:3)/low(vSMC1,arrows)"),
    "M00426": support("EVID_CELL_S3_AIRWAY_NEGATIVE", "Figure S3D legend, lines 1547-1549", "SCGB3A2+/SCGB1A1-"),
    "M00428": support("EVID_CELL_S3_AIRWAY_NEGATIVE", "Figure S3B/B' legend, lines 1542-1544", "SOX9-/CYTL1+/SCGB3A2+"),
    "M00457": support("EVID_CELL_S3_AIRWAY_NEGATIVE", "Figure S3H legend, lines 1558-1559", "FOXJ1+/SCGB3A2-"),
    "M00558": support("EVID_CELL_S3_AIRWAY_NEGATIVE", "Figure S3H legend, lines 1558-1559", "FOXJ1-/SCGB3A2+"),
    "M00570": support("EVID_CELL_S3_AIRWAY_NEGATIVE", "Figure S3G legend, lines 1556-1557", "SCGB3A1+/SCGB3A2-"),
    "M00459": support("EVID_CELL_SECRETORY_TEXT_NEGATIVE_LOW", "Results, lines 188-189", "Clubcells(SCGB3A2+,SCGB1A1+,SCGB3A1-,SPDEF-,MUC16-)"),
    "M00461": support("EVID_CELL_SECRETORY_TEXT_NEGATIVE_LOW", "Results, lines 188-189", "SCGB3A1-"),
    "M00463": support("EVID_CELL_SECRETORY_TEXT_NEGATIVE_LOW", "Results, lines 188-189", "SPDEF-"),
    "M00547": support("EVID_CELL_SECRETORY_TEXT_NEGATIVE_LOW", "Results, lines 202-203", "SCGB3A2LO/-"),
    "M00548": support("EVID_CELL_SECRETORY_TEXT_NEGATIVE_LOW", "Results, lines 202-203", "SPDEF-"),
    "M00550": support("EVID_CELL_SECRETORY_TEXT_NEGATIVE_LOW", "Results, lines 184-185", "SCGB1A1-"),
    "M00551": support("EVID_CELL_SECRETORY_TEXT_NEGATIVE_LOW", "Results, lines 184-185", "SCGB3A1-/LO"),
    "M00438": support("EVID_CELL_ALVEOLAR_NEGATIVE_LOW", "Results, lines 304-306", "AT1cells(SPOCK2+,SFTPC-)"),
    "M00444": support("EVID_CELL_ALVEOLAR_NEGATIVE_LOW", "Results, lines 291-295", "AT2cells(SOX9-,SFTPC+,NASPA+,ETV5+)"),
    "M00482": support("EVID_CELL_ALVEOLAR_NEGATIVE_LOW", "Figure S6H-J legend, lines 1643-1645", "SFTPC(cid:3)/SPOCK2-stalkcells"),
    "M00485": support("EVID_CELL_ALVEOLAR_NEGATIVE_LOW", "Figure S6C legend, lines 1637-1638", "SOX9(cid:3)TPPP3(cid:3)SFTPC+fetalAT2cellpopulation"),
    "M00486": support("EVID_CELL_ALVEOLAR_NEGATIVE_LOW", "Figure S6C legend, lines 1637-1638", "SOX9(cid:3)TPPP3(cid:3)SFTPC+fetalAT2cellpopulation"),
    "M00514": support("EVID_CELL_MESENCHYMAL_NEGATIVE_LOW", "Results, lines 377-380", "myofibroblast3(CXCL14+,KCNK17+,CT45A3-,andTHBD-)"),
    "M00517": support("EVID_CELL_MESENCHYMAL_NEGATIVE_LOW", "Results, lines 377-380", "myofibroblast3(CXCL14+,KCNK17+,CT45A3-,andTHBD-)"),
    "M00524": support("EVID_CELL_MESENCHYMAL_NEGATIVE_LOW", "Figure S7K-M legend, lines 1669-1671", "doesnotexpressACTA2"),
    "M00566": support("EVID_CELL_MESENCHYMAL_NEGATIVE_LOW", "Results, lines 135-137", "SOX9LO/-,PDPNLO,HOPXLO"),
    # Third-batch records: every completed positive relation gets a target-specific source fragment.
    "M00033": support("EVID_CELL_TASK9_POSITIVE_NE", "Results, lines 492-493", "thepan-NEPROX1"),
    "M00035": support("EVID_CELL_TASK9_POSITIVE_NE", "Results, lines 499-500", "ASCL1wasco-expressedwithGRP"),
    "M00414": support("EVID_CELL_TASK9_POSITIVE_AIRWAY", "Figure S7H legend, lines 1665-1666", "NDUFA4L2+red/NTRK3+vSMCs"),
    "M00425": support("EVID_CELL_TASK9_POSITIVE_AIRWAY", "Figure S3B/B' legend, lines 1542-1544", "SOX9-/CYTL1+/SCGB3A2+"),
    "M00427": support("EVID_CELL_TASK9_POSITIVE_AIRWAY", "Figure S3B/B' legend, lines 1542-1544", "SOX9-/CYTL1+/SCGB3A2+"),
    "M00437": support("EVID_CELL_TASK9_POSITIVE_ALVEOLAR", "Figure 3H-I legend, lines 279-280", "SFTPC(cid:3)/MMP28+/SPOCK2+"),
    "M00439": support("EVID_CELL_TASK9_POSITIVE_ALVEOLAR", "Results, lines 304-306", "SPOCK2+,SFTPC-"),
    "M00440": support("EVID_CELL_TASK9_POSITIVE_ALVEOLAR", "Results, lines 291-295", "ETV5+"),
    "M00441": support("EVID_CELL_TASK9_POSITIVE_ALVEOLAR", "Figure S6E-G legend, lines 1641-1642", "NAPSA(white;F)"),
    "M00442": support("EVID_CELL_TASK9_POSITIVE_ALVEOLAR", "Figure 3A-B legend, lines 267-269", "SFTPA1(red)"),
    "M00443": support("EVID_CELL_TASK9_POSITIVE_ALVEOLAR", "Figure 3A-B legend, lines 267-269", "SFTPC(green)"),
    "M00478": support("EVID_CELL_TASK9_POSITIVE_EPITHELIAL", "Figure S3A legend, lines 1539-1542", "E-cadherin(epithelium,cyan)"),
    "M00483": support("EVID_CELL_TASK9_POSITIVE_ALVEOLAR", "Figure S6H-J legend, lines 1643-1645", "SFTPC(cid:3)/SPOCK2-stalkcells"),
    "M00484": support("EVID_CELL_TASK9_POSITIVE_ALVEOLAR", "Figure S6C legend, lines 1637-1638", "SFTPC+fetalAT2cellpopulation"),
    "M00490": support("EVID_CELL_TASK9_POSITIVE_ALVEOLAR", "Figure S6E-G legend, lines 1641-1642", "SFTPC+fetalAT2cellpopulation"),
    "M00515": support("EVID_CELL_TASK9_POSITIVE_MESENCHYMAL", "Results, lines 377-378", "myofibroblast1(CXCL14+,KCNK17+"),
    "M00516": support("EVID_CELL_TASK9_POSITIVE_MESENCHYMAL", "Results, lines 377-378", "myofibroblast1(CXCL14+,KCNK17+"),
    "M00518": support("EVID_CELL_TASK9_POSITIVE_MESENCHYMAL", "Figure S7K-M legend, lines 1669-1671", "ACTA2+/PDGFRA+Myofibroblast-1"),
    "M00519": support("EVID_CELL_TASK9_POSITIVE_MESENCHYMAL", "Figure S7K-M legend, lines 1669-1671", "ACTA2+/PDGFRA+Myofibroblast-1"),
    "M00520": support("EVID_CELL_TASK9_THBD_LOW", "Figure S7K-M legend, lines 1669-1671", "Myofibroblast-1(THBDweak;K)"),
    "M00521": support("EVID_CELL_TASK9_POSITIVE_MESENCHYMAL", "Figure S7K-M legend, lines 1669-1671", "Myofibroblast-2"),
    "M00522": support("EVID_CELL_TASK9_POSITIVE_MESENCHYMAL", "Figure S7K-M legend, lines 1669-1671", "ACTA2+/PDGFRA+Myofibroblast-1"),
    "M00523": support("EVID_CELL_TASK9_POSITIVE_MESENCHYMAL", "Figure S7K-M legend, lines 1669-1671", "THBDhigh,arrows;L"),
    "M00525": support("EVID_CELL_TASK9_POSITIVE_MESENCHYMAL", "Figure S7K-M legend, lines 1669-1671", "PDGFRA+Myofibroblast-3"),
    "M00533": support("EVID_CELL_TASK9_MUC16_LOW_MIXED", "Results, lines 196-198", "proximal secretory1(SCGB1A1LO,SCGB3A2+,SCGB3A1+)"),
    "M00537": support("EVID_CELL_TASK9_MUC16_LOW_MIXED", "Figure S3E legend, lines 1550-1552", "MUC16low/+"),
    "M00545": support("EVID_CELL_TASK9_POSITIVE_SECRETORY", "Results, lines 202-203", "SCGB1A1+"),
    "M00546": support("EVID_CELL_TASK9_POSITIVE_SECRETORY", "Results, lines 202-203", "SCGB3A1+"),
    "M00549": support("EVID_CELL_TASK9_POSITIVE_SECRETORY", "Results, lines 184-185", "CYTL1+"),
    "M00552": support("EVID_CELL_TASK9_POSITIVE_SECRETORY", "Results, lines 184-185", "SCGB3A2+"),
    "M00559": support("EVID_CELL_TASK9_POSITIVE_SECRETORY", "Figure S3H legend, lines 1558-1559", "FOXJ1-/SCGB3A2+"),
    "M00563": support("EVID_CELL_TASK9_POSITIVE_STALK_TIP", "Results, lines 235-237", "gainasmallnumberofgenes,includingPDPNandAGER"),
    "M00564": support("EVID_CELL_TASK9_STALK_LOW", "Results, lines 135-137", "SOX9LO/-,PDPNLO,HOPXLO"),
    "M00565": support("EVID_CELL_TASK9_STALK_LOW", "Results, lines 135-137", "SOX9LO/-,PDPNLO,HOPXLO"),
    "M00568": support("EVID_CELL_TASK9_POSITIVE_SECRETORY", "Figure S3G legend, lines 1556-1557", "strongLTFexpression"),
    "M00569": support("EVID_CELL_TASK9_POSITIVE_SECRETORY", "Figure S3G legend, lines 1556-1557", "SCGB3A1+"),
    "M00571": support("EVID_CELL_TASK9_POSITIVE_STALK_TIP", "Results, lines 239-240", "ETV5+"),
    "M00573": support("EVID_CELL_TASK9_POSITIVE_STALK_TIP", "Results, lines 239-240", "SOX9+"),
    "M00574": support("EVID_CELL_TASK9_POSITIVE_STALK_TIP", "Results, lines 239-240", "STC1+"),
    "M00575": support("EVID_CELL_TASK9_POSITIVE_STALK_TIP", "Results, lines 239-240", "TESC+"),
    "M00576": support("EVID_CELL_TASK9_POSITIVE_STALK_TIP", "Results, lines 239-240", "TPPP3+"),
    "M00577": support("EVID_CELL_TASK9_POSITIVE_STALK_TIP", "Results, lines 263-266", "SOX9+,TPPP3+,SFTPC+"),
    "M00586": support("EVID_CELL_TASK9_POSITIVE_MESENCHYMAL", "Results, lines 367-370", "vSMC1(NTRK3+,NTN4+,andPLN-)"),
}


LOW_REPAIRS = {
    "M00520": ("EVID_CELL_TASK9_THBD_LOW", "原文将 THBD 标为 weak/LO；兼容编码改为 low，并保留低/弱表达限定。"),
    "M00533": ("EVID_CELL_TASK9_MUC16_LOW_MIXED", "原文为 MUC16low/-；兼容编码改为 low，并保留阴性可能性。"),
    "M00537": ("EVID_CELL_TASK9_MUC16_LOW_MIXED", "原文为 MUC16low/+；兼容编码改为 low，并保留低/阳性混合限定。"),
    "M00564": ("EVID_CELL_TASK9_STALK_LOW", "原文为 HOPXLO；兼容编码改为 low，不能按无条件 positive 记录。"),
    "M00565": ("EVID_CELL_TASK9_STALK_LOW", "原文为 PDPNLO；兼容编码改为 low，不能用另一阶段的 PDPN 获取表达覆盖本行。"),
}


MIXED_NOTES = {
    "M00547": "原文限定为 SCGB3A2LO/-；主表使用 low 作为兼容枚举，但该编码不表示纯低表达，仍保留阴性可能性。",
    "M00551": "原文限定为 SCGB3A1-/LO；主表使用 low 作为兼容枚举，但该编码不表示纯低表达，仍保留阴性可能性。",
    "M00566": "原文限定为 SOX9LO/-；主表使用 low 作为兼容枚举，但该编码不表示纯低表达，仍保留阴性可能性。",
    "M00593": "原文限定为 PLN-/low；主表使用 low 作为兼容枚举，但该编码不表示纯低表达，仍保留阴性可能性。",
}


def old_change(changes: list[dict], marker_id: str) -> dict | None:
    candidates = [item for item in changes if item.get("marker_id") == marker_id and not item.get("superseded_by")]
    return candidates[-1] if candidates else None


def append_once(changes: list[dict], item: dict) -> None:
    if not any(change.get("change_id") == item["change_id"] for change in changes):
        changes.append(item)


def main() -> None:
    reviews_doc = load("review-records.json")
    evidence_doc = load("evidence.json")
    changes_doc = load("change-set.json")
    reviews = {item["marker_id"]: item for item in reviews_doc["records"]}
    evidence = {item["evidence_id"]: item for item in evidence_doc["evidence"]}
    source_hash = sha256(SOURCE)
    expected_start_sha = changes_doc["changes"][0]["expected_start_sha256"]

    new_evidence = {
        "EVID_CELL_TASK9_THBD_LOW": {
            "paper_id": "DOI_10.1016_j.cell.2022.11.005",
            "locator": "Figure S7K-M legend, lines 1669-1671; Results, lines 377-380",
            "verbatim_fragments": ["Myofibroblast-1(THBDweak;K)", "myofibroblast1(CXCL14+,KCNK17+,CT45A3+,andTHBDLO)"],
            "interpretation": "THBD is weak/low in the myofibroblast-1 relation; do not inherit positive polarity from ACTA2 or PDGFRA.",
        },
        "EVID_CELL_TASK9_STALK_LOW": {
            "paper_id": "DOI_10.1016_j.cell.2022.11.005",
            "locator": "Results, lines 135-137",
            "verbatim_fragments": ["SOX9LO/-,PDPNLO,HOPXLO"],
            "interpretation": "The exact stalk-cell context gives low/negative SOX9, low PDPN and low HOPX; this condition governs M00564 and M00565.",
        },
        "EVID_CELL_TASK9_MUC16_LOW_MIXED": {
            "paper_id": "DOI_10.1016_j.cell.2022.11.005",
            "locator": "Results, lines 196-198; Figure S3E legend, lines 1550-1552",
            "verbatim_fragments": ["proximal secretory1(SCGB1A1LO,SCGB3A2+,SCGB3A1+)", "MUC16low/+"],
            "interpretation": "MUC16 is low/negative for proximal secretory 1 and low/positive for proximal secretory 2; use low only as a compatible enum and preserve the mixed qualifier.",
        },
    }
    for evidence_id, payload in new_evidence.items():
        if evidence_id not in evidence:
            evidence_doc["evidence"].append({
                "evidence_id": evidence_id,
                "source_file": "marker提取/review_md/DOI_10.1016_j.cell.2022.11.005.md",
                "source_sha256": source_hash,
                "supports_review_ids": [],
                "actual_checked_by": EXECUTOR,
                "checked_at": DATE,
                "verification_status": "current_source_checked_per_record",
                **payload,
            })
            evidence[evidence_id] = evidence_doc["evidence"][-1]

    # Every second/third-batch evidence group gets a per-record support map.
    group_supports: dict[str, dict[str, dict[str, str]]] = {}
    for marker_id, info in SUPPORT.items():
        group_supports.setdefault(info["evidence_id"], {})[marker_id] = {
            "locator": info["locator"],
            "excerpt": info["excerpt"],
        }
        if marker_id in reviews:
            reviews[marker_id]["evidence_excerpt"] = info["excerpt"]
            reviews[marker_id]["evidence_locator"] = info["locator"]
            reviews[marker_id]["evidence_binding_status"] = "per_record_source_fragment_checked"

    for evidence_id, item in evidence.items():
        if evidence_id in group_supports:
            item["support_map"] = group_supports[evidence_id]
            item["supports_review_ids"] = [f"LUNA-20260907-{marker_id}" for marker_id in group_supports[evidence_id]]
            item["verbatim_quote"] = None
            item["verbatim_fragments"] = [entry["excerpt"] for entry in group_supports[evidence_id].values()]
            item["verification_status"] = "current_source_checked_per_record"

    # Reopen five incorrectly generalized positive decisions, then resolve each to low with a revision trail.
    for marker_id, (evidence_id, reason) in LOW_REPAIRS.items():
        review = reviews[marker_id]
        previous = {
            "processing_status": review.get("processing_status"),
            "result": review.get("result"),
            "action": review.get("action"),
            "after_values": copy.deepcopy(review.get("after_values")),
            "evidence_ids": list(review.get("evidence_ids", [])),
            "reason": review.get("reason"),
            "revised_at": DATE,
            "revision_reason": "Astra抽查发现组级引文漏掉目标基因的LO/weak/low限定，必须按目标基因逐条返修。",
        }
        history = review.setdefault("revision_history", [])
        if not any(item.get("revision_reason") == previous["revision_reason"] and item.get("revised_at") == DATE for item in history):
            history.append(previous)
        original = review["original_values"]
        after = copy.deepcopy(original)
        after["marker_polarity"] = "low"
        after["notes"] = f"{original.get('notes') or ''} {reason}".strip()
        info = SUPPORT[marker_id]
        review.update({
            "processing_status": "completed",
            "result": "verified_correct",
            "action": "update",
            "after_values": after,
            "evidence_ids": [evidence_id],
            "checked_scope": [info["locator"]],
            "issues_found": ["第三批组级证据漏掉目标基因的低/弱/混合表达限定"],
            "remaining_gaps": [],
            "reason": reason,
            "related_marker_ids": [],
            "executed_by": EXECUTOR,
            "reviewed_at": DATE,
        })
        prior = old_change(changes_doc["changes"], marker_id)
        if prior:
            prior["superseded_by"] = f"UPDATE:{marker_id}:20260907-R1"
            prior["status"] = "superseded_by_revision"
        reopen_id = f"REOPEN:{marker_id}:20260907"
        append_once(changes_doc["changes"], {
            "change_id": reopen_id,
            "review_id": review["review_id"],
            "marker_id": marker_id,
            "operation": "reopen_pending",
            "before_values": previous["after_values"],
            "after_values": original,
            "evidence_ids": [],
            "reason": "Astra抽查要求重开并逐条核对目标基因表达限定。",
            "target_marker_id": None,
            "archive_destination": None,
            "executor": EXECUTOR,
            "decided_at": DATE,
            "expected_start_sha256": expected_start_sha,
            "supersedes": prior["change_id"] if prior else None,
        })
        append_once(changes_doc["changes"], {
            "change_id": f"UPDATE:{marker_id}:20260907-R1",
            "review_id": review["review_id"],
            "marker_id": marker_id,
            "operation": "update",
            "before_values": original,
            "after_values": after,
            "evidence_ids": [evidence_id],
            "reason": reason,
            "target_marker_id": None,
            "archive_destination": None,
            "executor": EXECUTOR,
            "decided_at": DATE,
            "expected_start_sha256": expected_start_sha,
            "supersedes": reopen_id,
        })

    # Preserve the compatible low enum while adding the mixed-expression qualifier to notes.
    for marker_id, note in MIXED_NOTES.items():
        review = reviews[marker_id]
        original_after = copy.deepcopy(review["after_values"])
        after = copy.deepcopy(original_after)
        after["notes"] = f"{after.get('notes') or ''} {note}".strip()
        review["after_values"] = after
        review["notes_revision"] = "Astra补充规范：low 为兼容编码，原始混合方向保留在备注与按细胞汇总。"
        prior = old_change(changes_doc["changes"], marker_id)
        revision_id = f"REVISE:{marker_id}:20260907-MIXED"
        if prior:
            prior["superseded_by"] = revision_id
            prior["status"] = "superseded_by_revision"
        info = SUPPORT[marker_id]
        append_once(changes_doc["changes"], {
            "change_id": revision_id,
            "review_id": review["review_id"],
            "marker_id": marker_id,
            "operation": "update",
            "before_values": original_after,
            "after_values": after,
            "evidence_ids": [info["evidence_id"]],
            "reason": note,
            "target_marker_id": None,
            "archive_destination": None,
            "executor": EXECUTOR,
            "decided_at": DATE,
            "expected_start_sha256": expected_start_sha,
            "supersedes": prior["change_id"] if prior else None,
        })

    # The positive group must no longer claim support for the five repaired records.
    removed_from_groups = {
        "EVID_CELL_TASK9_POSITIVE_MESENCHYMAL": {"M00520"},
        "EVID_CELL_TASK9_POSITIVE_STALK_TIP": {"M00564", "M00565"},
        "EVID_CELL_TASK9_POSITIVE_SECRETORY": {"M00533", "M00537"},
    }
    for evidence_id, removed in removed_from_groups.items():
        if evidence_id in evidence:
            support_map = evidence[evidence_id].get("support_map", {})
            for marker_id in removed:
                support_map.pop(marker_id, None)
            evidence[evidence_id]["support_map"] = support_map
            evidence[evidence_id]["supports_review_ids"] = [f"LUNA-20260907-{marker_id}" for marker_id in support_map]
            evidence[evidence_id]["verbatim_fragments"] = [entry["excerpt"] for entry in support_map.values()]

    summary = reviews_doc["summary"]
    summary["processing_status_counts"] = {
        "completed": sum(item["processing_status"] == "completed" for item in reviews_doc["records"]),
        "pending": sum(item["processing_status"] == "pending" for item in reviews_doc["records"]),
    }
    summary["result_counts"] = {}
    summary["known_batch_scope"] = []
    for item in reviews_doc["records"]:
        summary["result_counts"][item["result"]] = summary["result_counts"].get(item["result"], 0) + 1
        if item["processing_status"] == "completed":
            summary["known_batch_scope"].append(item["marker_id"])
    summary["known_batch_scope"].sort()
    changes_doc["change_count"] = len(changes_doc["changes"])
    changes_doc["latest_batch"] = {
        "name": "Astra batch-3 remediation: target-level qualifiers and evidence binding",
        "completed_records": 0,
        "reopened_and_resolved_records": len(LOW_REPAIRS),
        "mixed_encoding_note_revisions": len(MIXED_NOTES),
        "new_evidence_records": len(new_evidence),
    }
    save("review-records.json", reviews_doc)
    save("evidence.json", evidence_doc)
    save("change-set.json", changes_doc)


if __name__ == "__main__":
    main()
