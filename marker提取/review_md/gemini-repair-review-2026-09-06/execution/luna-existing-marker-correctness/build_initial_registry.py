from __future__ import annotations

import copy
import hashlib
import json
from datetime import date
from pathlib import Path
from typing import Any

import openpyxl


ROOT = Path(r"D:/OneDrive/Desktop/组")
RUN_DIR = ROOT / "marker提取/review_md/gemini-repair-review-2026-09-06/execution/luna-existing-marker-correctness"
FORMAL = ROOT / "marker提取/表单/our_markers.xlsx"
BY_CELL = ROOT / "marker提取/表单/our_markers_by_cell.xlsx"
SOURCE_ARCHIVE = ROOT / "marker提取/review_md/gemini-repair-review-2026-09-06/execution/luna-single-model/registry/audit_append.json"
SOURCE_MD = ROOT / "marker提取/review_md"
IMAGE_ROOT = ROOT / "marker_Gemini_evidence_v3/evidence"

EXECUTOR = "GPT-5.6 Luna"
REVIEW_DATE = "2026-09-07"
MARKER_HEADERS = [
    "marker_id", "task_no", "dataset_id", "paper_id", "document_id", "document_role",
    "ct_id", "subtype_id", "cell_type", "subtype", "species", "is_pns_cell",
    "gene_symbol", "original_symbol", "evidence_type", "marker_polarity", "candidate_class",
    "source_locator", "source_context", "review_status", "review_method", "notes",
    "source_file", "imported_at", "audit_status", "normalization_status", "citation_verified",
    "audit_model", "audit_notes", "four_layer_category", "recovery_source",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, default=lambda obj: obj.isoformat() if hasattr(obj, "isoformat") else str(obj)) + "\n", encoding="utf-8")


def workbook_records(path: Path) -> list[dict[str, Any]]:
    wb = openpyxl.load_workbook(path, read_only=True, data_only=False)
    ws = wb["markers"]
    rows = ws.iter_rows(values_only=True)
    headers = list(next(rows))
    records = []
    for row in rows:
        if not row or not row[0]:
            continue
        record = {headers[i]: row[i] if i < len(row) else None for i in range(len(headers))}
        records.append({key: record.get(key) for key in MARKER_HEADERS})
    wb.close()
    return records


def source_hash(rel_path: str) -> str | None:
    path = ROOT / rel_path
    return sha256(path) if path.exists() else None


def evidence(
    evidence_id: str,
    paper_id: str,
    source_file: str,
    locator: str,
    quote: str,
    interpretation: str,
    supports: list[str],
    *,
    image_path: str | None = None,
    image_scope: str | None = None,
    image_observation: str | None = None,
    historical: bool = False,
) -> dict[str, Any]:
    item: dict[str, Any] = {
        "evidence_id": evidence_id,
        "paper_id": paper_id,
        "source_file": source_file,
        "source_sha256": source_hash(source_file),
        "locator": locator,
        "verbatim_quote": quote,
        "interpretation": interpretation,
        "supports_review_ids": supports,
        "actual_checked_by": EXECUTOR,
        "checked_at": REVIEW_DATE,
        "verification_status": "historical_evidence_reused_with_current_scope_check" if historical else "current_source_checked",
    }
    if image_path:
        image = ROOT / image_path
        item["image"] = {
            "path": image_path,
            "sha256": sha256(image) if image.exists() else None,
            "viewed": True,
            "view_scope": image_scope,
            "visual_observation": image_observation,
        }
    return item


def review_record(
    record: dict[str, Any],
    scope: str,
    outcome: str = "pending",
    action: str = "pending",
    evidence_ids: list[str] | None = None,
    reason: str = "尚未完成本轮实际核验。",
    related_ids: list[str] | None = None,
    after_values: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "review_id": f"LUNA-20260907-{record['marker_id']}",
        "marker_id": record["marker_id"],
        "scope": scope,
        "paper_id": record.get("paper_id"),
        "original_values": copy.deepcopy(record),
        "processing_status": "pending" if outcome == "pending" else "completed",
        "result": outcome,
        "action": action,
        "after_values": after_values,
        "evidence_ids": evidence_ids or [],
        "checked_scope": [],
        "issues_found": [],
        "remaining_gaps": [] if outcome != "pending" else ["尚未完成关系、方向、条件和用途的逐项核验"],
        "reason": reason,
        "related_marker_ids": related_ids or [],
        "executed_by": EXECUTOR,
        "reviewed_at": REVIEW_DATE if outcome != "pending" else None,
        "historical_reviewers": [record.get("audit_model")] if record.get("audit_model") else [],
    }


def main() -> None:
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    (RUN_DIR / "baseline").mkdir(exist_ok=True)
    (RUN_DIR / "staged").mkdir(exist_ok=True)

    active = workbook_records(FORMAL)
    active_by_id = {r["marker_id"]: r for r in active}
    archive = load_json(SOURCE_ARCHIVE)
    merge_sources = [r for r in archive if r.get("decision") == "merge_duplicate"]
    side_records = {
        r["marker_id"]: {
            **{k: r.get(k) for k in MARKER_HEADERS},
            "superseded_marker_id": r.get("superseded_marker_id"),
            "decision": r.get("decision"),
            "archive_reason": r.get("reason"),
        }
        for r in merge_sources
    }
    m01510 = next(r for r in archive if r.get("marker_id") == "M01510")
    side_records["M01510"] = {
        **{k: m01510.get(k) for k in MARKER_HEADERS},
        "superseded_marker_id": m01510.get("superseded_marker_id"),
        "decision": m01510.get("decision"),
        "archive_reason": m01510.get("reason"),
    }

    baseline_manifest = {
        "run_id": "20260907-luna-existing-marker-correctness",
        "started_at": REVIEW_DATE,
        "executor": EXECUTOR,
        "formal_workbook": {
            "path": "marker提取/表单/our_markers.xlsx",
            "sha256": sha256(FORMAL),
            "active_record_count": len(active),
            "paper_count": len({r.get("paper_id") for r in active}),
        },
        "by_cell_workbook": {
            "path": "marker提取/表单/our_markers_by_cell.xlsx",
            "sha256": sha256(BY_CELL),
        },
        "side_review": {
            "count": len(side_records),
            "marker_ids": sorted(side_records),
            "source": "execution/luna-single-model/registry/audit_append.json",
        },
        "denominator_rule": "active marker IDs from the current formal workbook; side IDs are counted separately",
    }
    write_json(RUN_DIR / "baseline-manifest.json", baseline_manifest)

    for filename in ["our_markers.xlsx", "our_markers_by_cell.xlsx"]:
        source = FORMAL if filename == "our_markers.xlsx" else BY_CELL
        destination = RUN_DIR / "baseline" / filename
        if not destination.exists():
            destination.write_bytes(source.read_bytes())

    all_records: list[dict[str, Any]] = []
    review_by_id: dict[str, dict[str, Any]] = {}
    for record in active:
        item = review_record(record, "active_baseline")
        review_by_id[record["marker_id"]] = item
        all_records.append(item)
    for record in side_records.values():
        item = review_record(record, "previously_removed")
        review_by_id[record["marker_id"]] = item
        all_records.append(item)

    evidence_items = [
        evidence(
            "EVID_EXIST_CELL_S8C_NEUROD1_LOW",
            "DOI_10.1016_j.cell.2022.11.005",
            "marker提取/review_md/DOI_10.1016_j.cell.2022.11.005.md",
            "Figure S8C legend, lines 1686-1688",
            "#1 labeled GRP+NEUROD1lowGHRL- cells, which have just started the transition from GRP+ pulmonary NE/precursor cells.",
            "NEUROD1 is low, not an unqualified negative; the relationship is limited to the GRP+ pulmonary NE/precursor transition #1.",
            ["LUNA-20260907-M00044"],
        ),
        evidence(
            "EVID_EXIST_CELL_TRANSIT_EPI_FOXJ1_LOW",
            "DOI_10.1038_s41586-021-04345-x",
            "marker提取/review_md/DOI_10.1038_s41586-021-04345-x.md",
            "Results, lines 1972-1975; Detailed Cell Type Annotation, lines 3533-3539",
            "They co-express ciliated cell markers (PIFO) and secretory genes (MUC2), but are FOXJ1 low.",
            "The same sentence covers Transit epi 1 and 2; both records must retain low rather than negative.",
            ["LUNA-20260907-M00398", "LUNA-20260907-M00403"],
        ),
        evidence(
            "EVID_EXIST_IPAIN_NEUN_FIG3I",
            "DOI_10.1038_s41467-024-52052-8",
            "marker提取/review_md/DOI_10.1038_s41467-024-52052-8.md",
            "Results lines 185-191; Fig. 3 caption lines 303-305; PDF p.7 Fig. 3i",
            "We identified a senescent phenotype in a subset of nociceptors, which were characterized by high expression of the neuronal nuclei marker (NeuN) and their smaller size.",
            "NeuN/RBFOX3 is a neuronal nuclear marker observed in a CCI injury senescent nociceptor subset; it is not itself senescence-specific and must not be generalized to all neurons.",
            ["LUNA-20260907-M00071"],
            image_path="marker提取/review_md/gemini-repair-review-2026-09-06/astra-audit-after-luna/ipain-page7.png",
            image_scope="Fig. 3i panel and caption",
            image_observation="SA-β-Gal and NeuN co-staining is shown in panel i; the caption identifies the panel as CCI-related injured DRG staining.",
        ),
        evidence(
            "EVID_EXIST_IPAIN_SST_USAGE",
            "DOI_10.1038_s41467-024-52052-8",
            "marker提取/review_md/DOI_10.1038_s41467-024-52052-8.md",
            "Introduction line 39; Fig. 2a,f,g and Fig. 3e, PDF pp.2-5",
            "Those neurons are of different subtypes that are classified as peptidergic (PEPs), non-peptidergic (NPs), C-LowThreshold mechanoreceptor (C-LTMRs), and a subtype of somatostatin positive neurons (SST).",
            "SST is used as a named nociceptor subtype in the atlas and appears in the actual subtype/driver/chromatin/comparison panels; it is not merely an unused background citation.",
            ["LUNA-20260907-M01510"],
            image_path="marker提取/review_md/gemini-repair-review-2026-09-06/astra-audit-after-luna/ipain-page5.png",
            image_scope="Fig. 2a,f,g panels",
            image_observation="SST is a labeled nociceptor subtype in Fig. 2a and has dedicated driver-gene and chromatin-accessibility panels in Fig. 2f,g.",
        ),
        evidence(
            "EVID_EXIST_CELL_CA4_TEXT_LOW",
            "DOI_10.1016_j.cell.2022.11.005",
            "marker提取/review_md/DOI_10.1016_j.cell.2022.11.005.md",
            "Results line 296",
            "Aerocytes (CA4LO, S100A3+)",
            "The text source records CA4 low expression in aerocytes; it must not be silently represented as the same positive measurement as the HCR image.",
            ["LUNA-20260907-M00415"],
        ),
        evidence(
            "EVID_EXIST_CELL_CA4_HCR_POSITIVE",
            "DOI_10.1016_j.cell.2022.11.005",
            "marker提取/review_md/DOI_10.1016_j.cell.2022.11.005.md",
            "Figure S7B legend, lines 1656-1659; PDF p.44 Fig. S7B",
            "Aerocytes (S100A3+ red/CA4+ white), capillary endothelium (CA4+ white)",
            "The HCR imaging source is a separate positive detection for CA4 in aerocytes/capillary endothelium and should be restored under its original ID.",
            ["LUNA-20260907-M00417"],
            image_path="marker提取/review_md/gemini-repair-review-2026-09-06/astra-audit-after-luna/updated-row.png",
            image_scope="Historical audit image only; current decision is based on the cited S7B legend and source image group.",
            image_observation="The source group is recorded as HCR-based S7B localization; the current action preserves it as a separate positive relation rather than collapsing it into the text low relation.",
            historical=True,
        ),
        evidence(
            "EVID_EXIST_ELIFE_FIG1D_RIMS2_LAMC3",
            "DOI_10.7554_elife.62522",
            "marker提取/review_md/DOI_10.7554_elife.62522.md",
            "Fig. 1D, PDF p.4; marker-annotation figure",
            "Fig. 1D panel contains the RIMS2 column aligned with the PNEC row and the LAMC3 column aligned with the Pericytes row.",
            "RIMS2-PNEC and LAMC3-Pericytes are confirmed figure-labeled relations; the LAMC3 label must not retain the historical repair-claim wording.",
            ["LUNA-20260907-M02590", "LUNA-20260907-M02592"],
            image_path="marker_Gemini_evidence_v3/evidence/DOI_10.7554_elife.62522_p4_Fig1D_dotplot_detail.png",
            image_scope="Fig. 1D dot plot; PNEC and Pericytes rows against gene columns",
            image_observation="RIMS2 is legible at the PNEC row; LAMC3 is legible at the Pericytes row in the reopened dot plot.",
        ),
        evidence(
            "EVID_EXIST_SMG_FIG10G_FULL",
            "DOI_10.1038_s41588-022-01243-4",
            "marker提取/review_md/DOI_10.1038_s41588-022-01243-4.md",
            "Extended Data Fig. 10g full page and p.35 caption",
            "(g) IHC from the HPA showing HLA-DR, MUC5B and PRR4 staining with HLA-DR+ regions corresponding with non-mucous areas",
            "The complete Fig. 10 page visibly contains panel g with PRR4 (SMG-serous); the evidence retains protein_IHC as the measurement modality and uses the full-page asset.",
            ["LUNA-20260907-M02591"],
            image_path="marker_Gemini_evidence_v3/evidence/DOI_10.1038_s41588-022-01243-4_p34_ExtDataFig10_full.png",
            image_scope="Extended Data Fig. 10a-k full page, panel g and legend",
            image_observation="Panel g visibly labels PRR4 (SMG-serous) alongside MUC5B (SMG-mucous) in the HPA protein atlas section.",
        ),
    ]

    merge_quotes = {
        "M00047": ("Results lines 165-166; Figure S3C legend", "GHRL+ neuroendocrine cells", "GHRL marks the stated neuroendocrine subtype."),
        "M00048": ("Figure S8C legend", "#3 labeled GRP-NEUROD1+GHRL+, GHRL+ NE cells", "NEUROD1 is tied to the #3 GHRL+ NE subtype, not all transitional NE cells."),
        "M00050": ("Results lines 491-492; Figure S8E legend", "GHRL+ NE-specific RFX6", "RFX6 is retained with the GHRL+ NE condition."),
        "M00418": ("Figure S7B legend", "Aerocytes (S100A3+ red/CA4+ white)", "S100A3 is positive in the aerocyte HCR relation."),
        "M00456": ("Results line 168; Figure S3H legend", "ciliated FOXJ1+", "FOXJ1 is a ciliated-cell marker in the cited text/figure group."),
        "M00466": ("Results lines 188-192; Figure S3B legend", "club ... SCGB1A1", "SCGB1A1 is used to identify club cells."),
        "M00467": ("Figure S3D legend", "SCGB3A2+/SCGB1A1+", "SCGB3A2 is retained with the combined club-cell gate."),
        "M00494": ("Results lines 313-315; Figure S7E legend", "lymphatic endothelial cells (PROX1+)", "PROX1 is a lymphatic endothelial marker without an added SCG3 subtype."),
        "M00531": ("Results lines 378-379; Figure S7I legend", "FAM162B+ pericytes", "FAM162B is retained for the pericyte relation."),
        "M00554": ("Results line 181; Figure S4E legend", "putative ionocytes (FOXI1)", "FOXI1 is retained with the putative ionocyte qualifier."),
        "M00592": ("Results lines 367-371; Figure S7F legend", "NTN4+/PLN-/low (vSMC1)", "NTN4 is retained with the PLN and vSMC1 condition."),
        "M00597": ("Results lines 309-310; Figure S7D legend", "venous endothelial cells (ACKR3+)", "ACKR3 is retained for venous endothelial cells."),
    }
    for source_id, (locator, quote, interpretation) in merge_quotes.items():
        source = side_records[source_id]
        evidence_items.append(evidence(
            f"EVID_EXIST_MERGE_{source_id}",
            source["paper_id"],
            "marker提取/review_md/DOI_10.1016_j.cell.2022.11.005.md",
            locator,
            quote,
            interpretation,
            [f"LUNA-20260907-{source_id}", f"LUNA-20260907-{source['superseded_marker_id']}"],
            historical=True,
        ))

    evidence_by_id = {e["evidence_id"]: e for e in evidence_items}

    def complete(marker_id: str, result: str, action: str, evidence_ids: list[str], reason: str, after: dict[str, Any] | None = None, related: list[str] | None = None, issues: list[str] | None = None) -> None:
        item = review_by_id[marker_id]
        item.update({
            "processing_status": "completed",
            "result": result,
            "action": action,
            "after_values": after,
            "evidence_ids": evidence_ids,
            "checked_scope": [evidence_by_id[e]["locator"] for e in evidence_ids],
            "issues_found": issues or [],
            "remaining_gaps": [],
            "reason": reason,
            "related_marker_ids": related or [],
            "reviewed_at": REVIEW_DATE,
        })

    def after_for(marker_id: str, **changes: Any) -> dict[str, Any]:
        after = copy.deepcopy(review_by_id[marker_id]["original_values"])
        after.update(changes)
        return after

    complete("M00044", "verified_correct", "update", ["EVID_EXIST_CELL_S8C_NEUROD1_LOW"], "S8C明确写作NEUROD1low；修正为low并保留GRP+肺NE/前体转变#1条件。", after_for("M00044", marker_polarity="low", subtype="GRP+ pulmonary NE/precursor cells (transition #1)", source_context="#1 labeled GRP+NEUROD1lowGHRL- cells, which have just started the transition from GRP+ pulmonary NE/precursor cells."), issues=["原记录把low写为negative且亚群条件不足"])
    for marker_id in ["M00398", "M00403"]:
        complete(marker_id, "verified_correct", "update", ["EVID_EXIST_CELL_TRANSIT_EPI_FOXJ1_LOW"], "同一补充注释句同时覆盖Transit epi 1/2，FOXJ1为low而非negative。", after_for(marker_id, marker_polarity="low", source_context="They co-express ciliated cell markers (PIFO) and secretory genes (MUC2), but are FOXJ1 low."), issues=["原记录把low写为negative"])
    complete("M00071", "verified_correct", "update", ["EVID_EXIST_IPAIN_NEUN_FIG3I"], "保留CCI损伤DRG中SA-β-Gal与NeuN共染对应的衰老nociceptor子集，去掉笼统neurons表述和未经本轮确认的Astra署名。", after_for("M00071", cell_type="nociceptors", subtype="CCI-injured senescent nociceptor subset", source_locator="Results lines 185-191; Fig. 3i caption lines 303-305", notes="NeuN/RBFOX3 is a pan-neuronal nuclear marker; retain the CCI injury senescent-nociceptor experimental context without treating NeuN as senescence-specific."), issues=["原cell_type过泛；原引用指向Fig.1而非Fig.3i"])
    complete("M00415", "verified_correct", "update", ["EVID_EXIST_CELL_CA4_TEXT_LOW"], "正文为CA4LO；改为low并保留正文来源，不与HCR正信号合并。", after_for("M00415", marker_polarity="low", source_context="Aerocytes (CA4LO, S100A3+)"), related=["M00417"], issues=["原极性positive与CA4LO文字不一致"])
    complete("M00417", "verified_correct", "restore", ["EVID_EXIST_CELL_CA4_HCR_POSITIVE"], "恢复原ID，保留S7B HCR中的CA4+ aerocyte/毛细血管内皮正信号；不再压入M00415的正文low关系。", after_for("M00417", marker_polarity="positive", cell_type="aerocytes", source_locator="Figure S7B legend", source_context="Aerocytes (S100A3+ red/CA4+ white)"), related=["M00415"], issues=["上轮把不同来源与不同测量语境直接合并"])
    complete("M01510", "verified_correct", "restore", ["EVID_EXIST_IPAIN_SST_USAGE"], "SST在Fig.2a/f/g和Fig.3e中实际作为命名亚型和分析分组使用，恢复原ID为正式marker；不声称其为衰老特异基因。", after_for("M01510", source_locator="Fig. 2a,f,g; Fig. 3e; Introduction", source_context="SST is a named nociceptor subtype shown in the atlas subtype, driver-gene, chromatin-accessibility and subtype-comparison panels."), issues=["上轮仅保留引言背景而误转context_only"])
    complete("M02590", "verified_correct", "update", ["EVID_EXIST_ELIFE_FIG1D_RIMS2_LAMC3"], "关系成立；本轮只修正决策/证据链指向，避免引用不存在的DEC-M02590-v1。", after_for("M02590"), issues=["旧change_set decision_id未在decisions.json中存在"])
    complete("M02591", "verified_correct", "update", ["EVID_EXIST_SMG_FIG10G_FULL"], "关系和protein_IHC模态成立；证据改指完整Fig.10页面和正确g面板。", after_for("M02591"), issues=["旧证据指向不含决定性g面板的局部图"])
    complete("M02592", "verified_correct", "update", ["EVID_EXIST_ELIFE_FIG1D_RIMS2_LAMC3"], "LAMC3-Pericytes关系成立；清除Pericyte (claimed in repair)及历史申报措辞。", after_for("M02592", cell_type="Pericytes", source_locator="Fig. 1D, PDF p.4", source_context="Fig. 1D dot plot shows LAMC3 aligned with the Pericytes row; the panel is used for cluster annotation.", notes="LAMC3 is a figure-labeled Pericytes relation. measurement_type=RNA."), issues=["历史cell_type和notes带有repair claimed措辞"])

    for source_id, (locator, _, _) in merge_quotes.items():
        source = side_records[source_id]
        target_id = source["superseded_marker_id"]
        evidence_id = f"EVID_EXIST_MERGE_{source_id}"
        if source_id == "M00417":
            continue
        complete(source_id, "verified_keep", "no_change", [evidence_id], f"复核源关系与目标关系的基因、细胞、物种、方向和条件后，保留目标{target_id}；本轮补齐源ID及完整原值归档。", related=[target_id])
        if target_id in review_by_id:
            complete(target_id, "verified_keep", "no_change", [evidence_id], f"与{source_id}共享同一决定性证据组，目标关系保留；不因同一关系重复添加记录。", related=[source_id])

    changes: list[dict[str, Any]] = []

    def change(change_id: str, marker_id: str, operation: str, before: dict[str, Any] | None, after: dict[str, Any] | None, evidence_ids: list[str], reason: str, target: str | None = None, archive_destination: str | None = None) -> None:
        changes.append({
            "change_id": change_id,
            "review_id": f"LUNA-20260907-{marker_id}",
            "marker_id": marker_id,
            "operation": operation,
            "before_values": before,
            "after_values": after,
            "evidence_ids": evidence_ids,
            "reason": reason,
            "target_marker_id": target,
            "archive_destination": archive_destination,
            "executor": EXECUTOR,
            "decided_at": REVIEW_DATE,
            "expected_start_sha256": baseline_manifest["formal_workbook"]["sha256"],
        })

    change("UPDATE:M00044", "M00044", "update", review_by_id["M00044"]["original_values"], review_by_id["M00044"]["after_values"], ["EVID_EXIST_CELL_S8C_NEUROD1_LOW"], "NEUROD1low不能写为negative；保留转变#1亚群条件。")
    for marker_id in ["M00398", "M00403"]:
        change(f"UPDATE:{marker_id}", marker_id, "update", review_by_id[marker_id]["original_values"], review_by_id[marker_id]["after_values"], ["EVID_EXIST_CELL_TRANSIT_EPI_FOXJ1_LOW"], "FOXJ1 low被错误写成negative。")
    change("UPDATE:M00071", "M00071", "update", review_by_id["M00071"]["original_values"], review_by_id["M00071"]["after_values"], ["EVID_EXIST_IPAIN_NEUN_FIG3I"], "修正为CCI损伤DRG的衰老nociceptor子集，纠正Fig.3i定位。")
    change("UPDATE:M00415", "M00415", "update", review_by_id["M00415"]["original_values"], review_by_id["M00415"]["after_values"], ["EVID_EXIST_CELL_CA4_TEXT_LOW"], "正文CA4LO保留为low。", target="M00417")
    change("RESTORE:M00417", "M00417", "restore", review_by_id["M00417"]["original_values"], review_by_id["M00417"]["after_values"], ["EVID_EXIST_CELL_CA4_HCR_POSITIVE"], "恢复原ID并保留独立HCR positive来源。", target="M00417", archive_destination="our_markers.xlsx#audit_exclusions (restore provenance retained)")
    change("RESTORE:M01510", "M01510", "restore", review_by_id["M01510"]["original_values"], review_by_id["M01510"]["after_values"], ["EVID_EXIST_IPAIN_SST_USAGE"], "恢复实际用于命名和分析SST亚型的原ID。", target="M01510", archive_destination="our_markers.xlsx#audit_exclusions (restore provenance retained)")
    change("UPDATE:M02592", "M02592", "update", review_by_id["M02592"]["original_values"], review_by_id["M02592"]["after_values"], ["EVID_EXIST_ELIFE_FIG1D_RIMS2_LAMC3"], "清除历史repair claim措辞，保留图中LAMC3-Pericytes关系。")
    change("LINK:M02590", "M02590", "evidence_link_fix", review_by_id["M02590"]["original_values"], review_by_id["M02590"]["after_values"], ["EVID_EXIST_ELIFE_FIG1D_RIMS2_LAMC3"], "将旧不存在的DEC-M02590-v1改为本轮有效review/evidence链。")
    change("LINK:M02591", "M02591", "evidence_link_fix", review_by_id["M02591"]["original_values"], review_by_id["M02591"]["after_values"], ["EVID_EXIST_SMG_FIG10G_FULL"], "改指完整Fig.10页面/正确g面板。")
    for source_id in merge_quotes:
        if source_id == "M00417":
            continue
        source = side_records[source_id]
        change(f"ARCHIVE_REVIEW:{source_id}", source_id, "verify_existing_merge_archive", source, None, [f"EVID_EXIST_MERGE_{source_id}"], f"复核后维持目标{source['superseded_marker_id']}，并在独立本轮归档保留源ID和31字段原值。", target=source["superseded_marker_id"], archive_destination="new execution change-set and staged audit archive")

    review_summary = {
        "run_id": baseline_manifest["run_id"],
        "active_baseline_count": len(active),
        "side_count": len(side_records),
        "review_record_count": len(all_records),
        "processing_status_counts": {
            "completed": sum(r["processing_status"] == "completed" for r in all_records),
            "pending": sum(r["processing_status"] == "pending" for r in all_records),
        },
        "result_counts": {},
        "known_batch_scope": sorted([r["marker_id"] for r in all_records if r["processing_status"] == "completed"]),
    }
    for r in all_records:
        review_summary["result_counts"][r["result"]] = review_summary["result_counts"].get(r["result"], 0) + 1

    write_json(RUN_DIR / "review-records.json", {"run_id": baseline_manifest["run_id"], "records": all_records, "summary": review_summary})
    write_json(RUN_DIR / "evidence.json", {"run_id": baseline_manifest["run_id"], "evidence": evidence_items})
    write_json(RUN_DIR / "change-set.json", {"run_id": baseline_manifest["run_id"], "changes": changes, "change_count": len(changes), "scope_note": "Only explicit, evidence-linked corrections and archive reviews are included; unrelated active records remain pending."})


if __name__ == "__main__":
    main()
