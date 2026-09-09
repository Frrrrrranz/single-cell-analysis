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
    (RUN_DIR / name).write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    reviews_doc = load("review-records.json")
    evidence_doc = load("evidence.json")
    changes_doc = load("change-set.json")
    review_by_id = {item["marker_id"]: item for item in reviews_doc["records"]}

    groups = [
        {
            "evidence_id": "EVID_CELL_TASK9_POSITIVE_NE",
            "ids": ["M00033", "M00035"],
            "locator": "Results lines 492-503 and 506-514",
            "quote": "the pan-NE PROX1 ... ASCL1 was co-expressed with GRP ... these two TFs coincide with the scRNA-seq marker genes",
            "interpretation": "The registered PROX1 and ASCL1 relations are explicitly described as positive neuroendocrine or pulmonary-NE markers; retain positive polarity.",
        },
        {
            "evidence_id": "EVID_CELL_TASK9_POSITIVE_AIRWAY",
            "ids": ["M00414", "M00425", "M00427"],
            "locator": "Figure S3B/B' legend lines 1542-1544; Figure S7H legend lines 1665-1666",
            "quote": "Airway progenitor cells marked by SOX9-/CYTL1+/SCGB3A2+ ... NDUFA4L2-/NTRK3+ adventitial fibroblasts",
            "interpretation": "CYTL1, SCGB3A2 and NTRK3 are explicitly positive components of the named cell definitions; retain positive polarity even when another gate in the same definition is negative.",
        },
        {
            "evidence_id": "EVID_CELL_TASK9_POSITIVE_ALVEOLAR",
            "ids": ["M00437", "M00439", "M00440", "M00441", "M00442", "M00443", "M00483", "M00484", "M00490"],
            "locator": "Results lines 239-266, 294-310; Figure 3F-I and Figure S6C/E-J legends lines 1637-1645",
            "quote": "fetal AT1 SFTPC-/MMP28+/SPOCK2+ ... AT1 cells (SPOCK2+, SFTPC-) ... AT2 cells (SOX9-, SFTPC+, NASPA+, ETV5+) ... SFTPC+ fetal AT2 cell population",
            "interpretation": "MMP28, SPOCK2, ETV5, NAPSA and SFTPC are directly positive markers in the registered AT1/AT2 or late-tip relations; retain positive polarity and preserve the separate negative gates.",
        },
        {
            "evidence_id": "EVID_CELL_TASK9_POSITIVE_EPITHELIAL",
            "ids": ["M00478"],
            "locator": "Figure S3A legend lines 1539-1542",
            "quote": "Tip and stalk epithelial cells ... immunostained using antibodies against CD36 ... PDPN ... and E-cadherin (epithelium, cyan).",
            "interpretation": "E-cadherin is explicitly used as the epithelial signal; retain the positive epithelial marker relation.",
        },
        {
            "evidence_id": "EVID_CELL_TASK9_POSITIVE_MESENCHYMAL",
            "ids": ["M00515", "M00516", "M00518", "M00519", "M00520", "M00521", "M00522", "M00523", "M00525", "M00586"],
            "locator": "Results lines 366-370; Figure S7F/H and S7K-M legends lines 1662-1671",
            "quote": "vSMC1 (NTRK3+, NTN4+, and PLN-) ... ACTA2+/PDGFRA+ Myofibroblast-1 ... Myofibroblast-2 (THBDhigh) ... PDGFRA+ Myofibroblast-3 ... NTRK3+ vSMCs",
            "interpretation": "The registered positive relations are explicitly present in vSMC and myofibroblast definitions. Negative or weak/low qualifiers on other genes do not change these positive relations.",
        },
        {
            "evidence_id": "EVID_CELL_TASK9_POSITIVE_SECRETORY",
            "ids": ["M00533", "M00537", "M00545", "M00546", "M00549", "M00552", "M00559", "M00568", "M00569"],
            "locator": "Results lines 183-203; Figure S3D-G/H legends lines 1547-1559",
            "quote": "proximal secretory progenitors (SCGB3A2+, ... CYTL1+) ... proximal secretory 3 (SCGB1A1+, SCGB3A2LO/-, SCGB3A1+) ... SMG secretory cells (LTF+, SCGB3A1+, SPDEF+) ... secretory cells ... FOXJ1-/SCGB3A2+",
            "interpretation": "The registered MUC16, SCGB1A1, SCGB3A1, CYTL1, SCGB3A2, LTF and SCGB3A1 relations are explicitly positive in their respective cell definitions; retain positive polarity.",
        },
        {
            "evidence_id": "EVID_CELL_TASK9_POSITIVE_STALK_TIP",
            "ids": ["M00563", "M00564", "M00565", "M00571", "M00573", "M00574", "M00575", "M00576", "M00577"],
            "locator": "Results lines 235-248; Figure 3F/G and Figure S6C/D legends lines 1637-1644",
            "quote": "stalk cells ... gain ... PDPN and AGER ... Tip cells express a core set of tip-specific markers (SOX9+, ETV5+, TESC+, TPPP3+, and STC1+) ... late-tip cells (SOX9+, TPPP3+, SFTPC+)",
            "interpretation": "AGER, HOPX, PDPN, ETV5, SOX9, STC1, TESC, TPPP3 and SFTPC are explicitly positive or acquired markers in the registered stalk/tip relations; retain positive polarity.",
        },
    ]

    source_hash = sha256(SOURCE)
    existing_evidence_ids = {item["evidence_id"] for item in evidence_doc["evidence"]}
    for group in groups:
        if group["evidence_id"] not in existing_evidence_ids:
            evidence_doc["evidence"].append(
                {
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
                }
            )

    expected_start_sha = changes_doc["changes"][0]["expected_start_sha256"]
    for group in groups:
        for marker_id in group["ids"]:
            review = review_by_id[marker_id]
            original = review["original_values"]
            after = copy.deepcopy(original)
            review.update(
                {
                    "processing_status": "completed",
                    "result": "verified_keep",
                    "action": "no_change",
                    "after_values": after,
                    "evidence_ids": [group["evidence_id"]],
                    "checked_scope": [group["locator"]],
                    "issues_found": [],
                    "remaining_gaps": [],
                    "reason": "正文或图注明确给出该基因在命名细胞条件中的正向表达；本轮保留原字段。",
                    "related_marker_ids": [other for other in group["ids"] if other != marker_id],
                    "executed_by": EXECUTOR,
                    "reviewed_at": DATE,
                }
            )
            changes_doc["changes"].append(
                {
                    "change_id": f"VERIFY:{marker_id}",
                    "review_id": review["review_id"],
                    "marker_id": marker_id,
                    "operation": "no_change",
                    "before_values": original,
                    "after_values": after,
                    "evidence_ids": [group["evidence_id"]],
                    "reason": "正文或图注明确给出该基因在命名细胞条件中的正向表达；本轮保留原字段。",
                    "target_marker_id": None,
                    "archive_destination": None,
                    "executor": EXECUTOR,
                    "decided_at": DATE,
                    "expected_start_sha256": expected_start_sha,
                }
            )

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
        "name": "CELL task 9 positive marker evidence group",
        "completed_records": 43,
        "updated_records": 0,
        "kept_records": 43,
    }
    save("review-records.json", reviews_doc)
    save("evidence.json", evidence_doc)
    save("change-set.json", changes_doc)


if __name__ == "__main__":
    main()
