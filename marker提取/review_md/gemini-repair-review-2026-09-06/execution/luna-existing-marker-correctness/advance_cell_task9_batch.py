from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(r"D:/OneDrive/Desktop/组")
RUN_DIR = ROOT / "marker提取/review_md/gemini-repair-review-2026-09-06/execution/luna-existing-marker-correctness"
SOURCE = ROOT / "marker提取/review_md/DOI_10.1016_j.cell.2022.11.005.md"
EXECUTOR = "GPT-5.6 Luna"
DATE = "2026-09-07"


def load(name: str):
    return json.loads((RUN_DIR / name).read_text(encoding="utf-8"))


def save(name: str, value) -> None:
    (RUN_DIR / name).write_text(json.dumps(value, ensure_ascii=False, indent=2, default=lambda x: x.isoformat() if hasattr(x, "isoformat") else str(x)) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    reviews_doc = load("review-records.json")
    evidence_doc = load("evidence.json")
    changes_doc = load("change-set.json")
    review_by_id = {item["marker_id"]: item for item in reviews_doc["records"]}

    groups = [
        {
            "evidence_id": "EVID_CELL_S8C_E_NEGATIVE",
            "ids": ["M00045", "M00049", "M00046"],
            "locator": "Figure S8C and S8E legends; lines 1686-1692",
            "quote": "#1 labeled GRP+NEUROD1lowGHRL- cells ... #3 labeled GRP-NEUROD1+GHRL+, GHRL+ NE cells. ... Representative HCR images showing RFX6 expression in GHRL+ NE cells. Dash yellow line labeled GRP+RFX6- pulmonary NE cells.",
            "interpretation": "GHRL-, GRP- and RFX6- are explicit negative components of the named NE transition/subtype conditions; retain negative rather than infer a new positive marker.",
        },
        {
            "evidence_id": "EVID_CELL_S7H_F_NEGATIVE",
            "ids": ["M00413", "M00587", "M00593"],
            "locator": "Results lines 367-370; Figure S7F and S7H legend lines 1662-1665",
            "quote": "vSMC1 (NTRK3+, NTN4+, and PLN-) and vSMC2 (NTRK3+, NTN4+, and PLN+) ... NDUFA4L2+ red/NTRK3+ vSMCs ... surrounded by NDUFA4L2-/NTRK3+ adventitial fibroblasts.",
            "interpretation": "The negative signs are explicit cell-state gates for PLN and NDUFA4L2; they are not merely missing evidence. PLN-/low is recorded as low for M00593 because the figure explicitly includes low expression.",
        },
        {
            "evidence_id": "EVID_CELL_S3_AIRWAY_NEGATIVE",
            "ids": ["M00426", "M00428", "M00457", "M00558", "M00570"],
            "locator": "Figure S3B/B', S3D, S3G and S3H legends lines 1542-1559",
            "quote": "Airway progenitor cells marked by SOX9-/CYTL1+/SCGB3A2+ ... SCGB3A2+/SCGB1A1- ... Submucosal gland cells ... SCGB3A1+/SCGB3A2- ... Ciliated cells ... FOXJ1+/SCGB3A2-; secretory cells ... FOXJ1-/SCGB3A2+.",
            "interpretation": "Each relation is a directly labeled negative gate for the named airway lineage. The signs are retained as negative, including SCGB1A1-, SOX9-, SCGB3A2-, FOXJ1- and SCGB3A2-.",
        },
        {
            "evidence_id": "EVID_CELL_SECRETORY_TEXT_NEGATIVE_LOW",
            "ids": ["M00459", "M00461", "M00463", "M00547", "M00548", "M00550", "M00551"],
            "locator": "Results lines 183-203, 'Multiple secretory cell subtypes in the proximal cartilaginous airways'",
            "quote": "Club cells (SCGB3A2+, SCGB1A1+, SCGB3A1-, SPDEF-, MUC16-) ... proximal secretory 3 (SCGB1A1+, SCGB3A2LO/-, SCGB3A1+) ... was SPDEF- ... proximal secretory progenitors (SCGB3A2+, SCGB1A1-, SCGB3A1-/LO, CYTL1+).",
            "interpretation": "Exact '-' relations remain negative. SCGB3A2LO/- and SCGB3A1-/LO explicitly contain a low-expression condition, so M00547 and M00551 are corrected to low rather than collapsed to negative.",
        },
        {
            "evidence_id": "EVID_CELL_ALVEOLAR_NEGATIVE_LOW",
            "ids": ["M00438", "M00444", "M00482", "M00485", "M00486"],
            "locator": "Results lines 264-266 and 294-310; Figure S6C/H-J legends",
            "quote": "differentiating AT2 cells (SOX9LO/-, TPPP3LO/-, SFTPC+) ... AT2 cells (SOX9-, SFTPC+, NASPA+, ETV5+) ... AT1 cells (SPOCK2+, SFTPC-).",
            "interpretation": "The AT1/AT2 relations distinguish exact negative from low/negative combined wording. This batch keeps the exact negative records unchanged; no low conversion is made where the registered relation is the explicit '-'.",
        },
        {
            "evidence_id": "EVID_CELL_MESENCHYMAL_NEGATIVE_LOW",
            "ids": ["M00514", "M00517", "M00524", "M00566"],
            "locator": "Results lines 136, 378-380; Figure S7K-M legend lines 1669-1671",
            "quote": "adjacent stalk cells (SOX9LO/-, PDPNLO, HOPXLO) ... myofibroblast 3 (CXCL14+, KCNK17+, CT45A3-, and THBD-) ... PDGFRA+ Myofibroblast-3 at 21 pcw does not express ACTA2.",
            "interpretation": "CT45A3-, THBD- and ACTA2 non-expression are explicit negative gates. SOX9LO/- includes low expression and is corrected to low for the stalk-cell relation M00566.",
        },
    ]

    source_hash = sha256(SOURCE)
    new_evidence = []
    for group in groups:
        new_evidence.append({
            "evidence_id": group["evidence_id"],
            "paper_id": "DOI_10.1016_j.cell.2022.11.005",
            "source_file": "marker提取/review_md/DOI_10.1016_j.cell.2022.11.005.md",
            "source_sha256": source_hash,
            "locator": group["locator"],
            "verbatim_quote": group["quote"],
            "interpretation": group["interpretation"],
            "supports_review_ids": [f"LUNA-20260907-{marker_id}" for marker_id in group["ids"]],
            "actual_checked_by": EXECUTOR,
            "checked_at": DATE,
            "verification_status": "current_source_checked",
        })

    existing_evidence_ids = {item["evidence_id"] for item in evidence_doc["evidence"]}
    evidence_doc["evidence"].extend(item for item in new_evidence if item["evidence_id"] not in existing_evidence_ids)
    evidence_map = {item["evidence_id"]: item for item in new_evidence}
    low_ids = {"M00547", "M00551", "M00566", "M00593"}

    for group in groups:
        for marker_id in group["ids"]:
            review = review_by_id[marker_id]
            original = review["original_values"]
            after = copy.deepcopy(original)
            if marker_id in low_ids:
                after["marker_polarity"] = "low"
                after["notes"] = f"{original.get('notes') or ''} 本轮复核：原文明确含 LO/low，按原文保留为 low。".strip()
                result = "verified_correct"
                action = "update"
                reason = "原文把该基因写作 LO/low；修正极性为 low，避免将低表达条件折叠为 negative。"
                issues = ["原记录将LO/low表示为negative"]
            else:
                result = "verified_keep"
                action = "no_change"
                reason = "图注/正文明确给出该基因在命名细胞条件中的负向门控；本轮保留原字段。"
                issues = []
            review.update({
                "processing_status": "completed",
                "result": result,
                "action": action,
                "after_values": after,
                "evidence_ids": [group["evidence_id"]],
                "checked_scope": [group["locator"]],
                "issues_found": issues,
                "remaining_gaps": [],
                "reason": reason,
                "related_marker_ids": [other for other in group["ids"] if other != marker_id],
                "executed_by": EXECUTOR,
                "reviewed_at": DATE,
            })
            changes_doc["changes"].append({
                "change_id": f"{'UPDATE' if action == 'update' else 'VERIFY'}:{marker_id}",
                "review_id": review["review_id"],
                "marker_id": marker_id,
                "operation": action,
                "before_values": original,
                "after_values": after,
                "evidence_ids": [group["evidence_id"]],
                "reason": reason,
                "target_marker_id": None,
                "archive_destination": None,
                "executor": EXECUTOR,
                "decided_at": DATE,
                "expected_start_sha256": changes_doc["changes"][0]["expected_start_sha256"],
            })

    summary = reviews_doc["summary"]
    summary["processing_status_counts"] = {
        "completed": sum(item["processing_status"] == "completed" for item in reviews_doc["records"]),
        "pending": sum(item["processing_status"] == "pending" for item in reviews_doc["records"]),
    }
    summary["result_counts"] = {}
    summary["known_batch_scope"] = []
    for item in reviews_doc["records"]:
        summary["result_counts"][item["result"]] = summary["result_counts"].get(item["result"], 0) + 1
        if item["processing_status"] == "completed": summary["known_batch_scope"].append(item["marker_id"])
    summary["known_batch_scope"].sort()
    changes_doc["change_count"] = len(changes_doc["changes"])
    changes_doc["latest_batch"] = {
        "name": "CELL task 9 shared S3/S6/S7/S8 evidence group",
        "completed_records": 27,
        "updated_records": len(low_ids),
        "kept_records": 27 - len(low_ids),
    }
    save("review-records.json", reviews_doc)
    save("evidence.json", evidence_doc)
    save("change-set.json", changes_doc)


if __name__ == "__main__":
    main()
