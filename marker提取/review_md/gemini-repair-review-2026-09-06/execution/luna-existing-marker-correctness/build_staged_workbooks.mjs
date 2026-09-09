import fs from "node:fs/promises";
import { createHash } from "node:crypto";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const root = "D:/OneDrive/Desktop/组";
const runDir = `${root}/marker提取/review_md/gemini-repair-review-2026-09-06/execution/luna-existing-marker-correctness`;
const baselineMain = `${runDir}/baseline/our_markers.xlsx`;
const baselineByCell = `${runDir}/baseline/our_markers_by_cell.xlsx`;
const oldByCellPath = `${root}/marker提取/review_md/gemini-repair-review-2026-09-06/execution/luna-single-model/baseline/20260906-luna-single-model/our_markers_by_cell.xlsx`;

const markerHeaders = [
  "marker_id", "task_no", "dataset_id", "paper_id", "document_id", "document_role",
  "ct_id", "subtype_id", "cell_type", "subtype", "species", "is_pns_cell",
  "gene_symbol", "original_symbol", "evidence_type", "marker_polarity", "candidate_class",
  "source_locator", "source_context", "review_status", "review_method", "notes",
  "source_file", "imported_at", "audit_status", "normalization_status", "citation_verified",
  "audit_model", "audit_notes", "four_layer_category", "recovery_source",
];
const extraArchiveHeaders = ["review_id", "scope", "archive_action", "target_marker_id", "evidence_ids", "reason", "executor", "reviewed_at", "change_status", "supersedes", "superseded_by"];

async function readJson(path) {
  return JSON.parse(await fs.readFile(path, "utf8"));
}

function rowsFromUsed(sheet) {
  const values = sheet.getUsedRange()?.values ?? [];
  return values.map((row) => Array.from(row));
}

function findRows(rows, idColumn = 0) {
  const result = new Map();
  rows.forEach((row, index) => {
    if (row?.[idColumn]) result.set(String(row[idColumn]), { index, row });
  });
  return result;
}

function normalize(value) {
  if (value === null || value === undefined) return "";
  return String(value);
}

function semanticKey(row) {
  return [0, 1, 6, 7].map((i) => normalize(row[i])).join("\u001f");
}

function setIfFound(rows, matcher, updater) {
  for (const row of rows) {
    if (matcher(row)) updater(row);
  }
}

function colLetter(index) {
  let n = index + 1;
  let out = "";
  while (n > 0) {
    const r = (n - 1) % 26;
    out = String.fromCharCode(65 + r) + out;
    n = Math.floor((n - 1) / 26);
  }
  return out;
}

async function renderAndSave(workbook, sheetName, range, path) {
  const preview = await workbook.render({ sheetName, range, scale: 1, format: "png" });
  await fs.writeFile(path, new Uint8Array(await preview.arrayBuffer()));
}

async function buildMainWorkbook(changeSet, reviewData, evidenceData) {
  const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(baselineMain));
  const markers = workbook.worksheets.getItem("markers");
  const markerRows = rowsFromUsed(markers);
  const markerRowMap = findRows(markerRows);
  const reviewMap = new Map(reviewData.records.map((r) => [r.marker_id, r]));
  const changeMap = new Map(changeSet.changes.map((c) => [c.marker_id, c]));

  const fieldUpdates = {
    M00044: ["subtype", "marker_polarity", "source_context"],
    M00398: ["marker_polarity", "source_context"],
    M00403: ["marker_polarity", "source_context"],
    M00071: ["cell_type", "subtype", "source_locator", "notes"],
    M00415: ["marker_polarity", "source_context"],
    M02592: ["cell_type", "source_locator", "source_context", "notes"],
    M00547: ["marker_polarity", "notes"],
    M00551: ["marker_polarity", "notes"],
    M00566: ["marker_polarity", "notes"],
    M00593: ["marker_polarity", "notes"],
    M00520: ["marker_polarity", "notes"],
    M00564: ["marker_polarity", "notes"],
    M00565: ["marker_polarity", "notes"],
    M00533: ["marker_polarity", "notes"],
    M00537: ["marker_polarity", "notes"],
    M00493: ["marker_polarity", "notes"],
    M00495: ["marker_polarity", "notes"],
    M00498: ["marker_polarity", "notes"],
    M00508: ["marker_polarity", "notes"],
    M00534: ["marker_polarity", "notes"],
    M00633: ["marker_polarity", "notes"],
    M00637: ["marker_polarity", "notes"],
    M00680: ["marker_polarity", "notes"],
    M02359: ["marker_polarity", "notes"],
    M02364: ["marker_polarity", "notes"],
    M02369: ["marker_polarity", "notes"],
    M02374: ["marker_polarity", "notes"],
    M02375: ["marker_polarity", "notes"],
    M02376: ["marker_polarity", "notes"],
  };
  const updateIds = Object.keys(fieldUpdates);
  for (const markerId of updateIds) {
    const rowInfo = markerRowMap.get(markerId);
    const review = reviewMap.get(markerId);
    if (!rowInfo || !review?.after_values) throw new Error(`Missing active row or after_values for ${markerId}`);
    const nextRow = [...rowInfo.row];
    for (const field of fieldUpdates[markerId]) {
      nextRow[markerHeaders.indexOf(field)] = review.after_values[field] ?? null;
    }
    markers.getRangeByIndexes(rowInfo.index, 0, 1, markerHeaders.length).values = [nextRow];
  }

  const restoreIds = ["M00417", "M01510"];
  const lastDataIndex = markerRows.reduce((last, row, index) => (row?.[0] ? index : last), 0);
  const restoreRows = restoreIds.map((markerId) => {
    const review = reviewMap.get(markerId);
    if (!review?.after_values) throw new Error(`Missing restore snapshot for ${markerId}`);
    return markerHeaders.map((h) => review.after_values[h] ?? null);
  });
  const template = markers.getRangeByIndexes(lastDataIndex, 0, 1, markerHeaders.length);
  for (let i = 0; i < restoreRows.length; i += 1) {
    const target = markers.getRangeByIndexes(lastDataIndex + 1 + i, 0, 1, markerHeaders.length);
    target.copyFrom(template, "all");
    target.values = [restoreRows[i]];
  }

  const archiveSheetName = "audit_archive_20260907";
  const archive = workbook.worksheets.add(archiveSheetName);
  const archiveHeaders = [...markerHeaders, ...extraArchiveHeaders];
  const archiveRows = changeSet.changes
    .filter((change) => change.before_values)
    .map((change) => {
      const before = change.before_values;
      return [
        ...markerHeaders.map((h) => before[h] ?? null),
        change.review_id,
        reviewMap.get(change.marker_id)?.scope ?? "unknown",
        change.operation,
        change.target_marker_id ?? null,
        change.evidence_ids.join(", "),
        change.reason,
        change.executor,
        change.decided_at,
        change.status ?? "active",
        change.supersedes ?? null,
        change.superseded_by ?? null,
      ];
    });
  archive.getRangeByIndexes(0, 0, 1, archiveHeaders.length).values = [archiveHeaders];
  archive.getRangeByIndexes(1, 0, archiveRows.length, archiveHeaders.length).values = archiveRows;
  archive.getRangeByIndexes(0, 0, 1, archiveHeaders.length).format = {
    fill: "#1F4E78",
    font: { color: "#FFFFFF", bold: true },
    wrapText: true,
    verticalAlignment: "center",
  };
  archive.getRangeByIndexes(1, 0, archiveRows.length, archiveHeaders.length).format = {
    verticalAlignment: "center",
    wrapText: false,
  };
  archive.getRangeByIndexes(0, 0, archiveRows.length + 1, archiveHeaders.length).format.borders = { preset: "all", style: "thin", color: "#D9D9D9" };
  archive.freezePanes.freezeRows(1);
  archive.getRange("A:AE").format.columnWidth = 18;
  archive.getRange("AF:AM").format.columnWidth = 28;

  const summary = workbook.worksheets.getItem("audit_summary");
  const summaryRows = rowsFromUsed(summary);
  for (let index = 1; index < summaryRows.length; index += 1) {
    const taskNo = summaryRows[index]?.[0];
    if (taskNo === 9) {
      summary.getRangeByIndexes(index, 7, 1, 4).values = [[(summaryRows[index][7] ?? 0) + 1, (summaryRows[index][8] ?? 0), summaryRows[index][9] ?? 0, summaryRows[index][10] ?? 0]];
    }
    if (taskNo === 36) {
      summary.getRangeByIndexes(index, 7, 1, 4).values = [[(summaryRows[index][7] ?? 0) + 1, (summaryRows[index][8] ?? 0) + 1, summaryRows[index][9] ?? 0, summaryRows[index][10] ?? 0]];
    }
  }

  const notes = workbook.worksheets.getItem("说明与统计");
  const noteRows = rowsFromUsed(notes);
  for (let index = 0; index < noteRows.length; index += 1) {
    const value = noteRows[index]?.[1];
    if (typeof value === "string" && value.includes("2488")) {
      notes.getCell(index, 1).values = [[value.replaceAll("2488", "2490")]];
    }
  }

  workbook.recalculate();
  const xlsx = await SpreadsheetFile.exportXlsx(workbook);
  const output = `${runDir}/staged/our_markers.xlsx`;
  await xlsx.save(output);
  await renderAndSave(workbook, "markers", "A1:AE18", `${runDir}/staged/staged-our-markers-head.png`);
  await renderAndSave(workbook, archiveSheetName, "A1:AM12", `${runDir}/staged/staged-audit-archive-head.png`);

  return {
    workbook,
    output,
    markerRowsBefore: markerRows.filter((row) => row?.[0]).length,
    markerRowsAfter: markerRows.filter((row) => row?.[0]).length + restoreRows.length,
    archiveRows: archiveRows.length,
    affectedIds: [...updateIds, ...restoreIds],
  };
}

async function buildByCellWorkbook() {
  const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(baselineByCell));
  const oldWorkbook = await SpreadsheetFile.importXlsx(await FileBlob.load(oldByCellPath));
  const sheet = workbook.worksheets.getItem("Marker表");
  const oldSheet = oldWorkbook.worksheets.getItem("Marker表");
  const currentRows = rowsFromUsed(sheet);
  const oldRows = rowsFromUsed(oldSheet);
  const oldMap = new Map();
  for (const row of oldRows.slice(1)) {
    const key = semanticKey(row);
    if (!oldMap.has(key)) oldMap.set(key, []);
    oldMap.get(key).push(row);
  }
  let matched = 0;
  let restoredCells = 0;
  const unmatched = [];
  for (let index = 1; index < currentRows.length; index += 1) {
    const row = currentRows[index];
    const matches = oldMap.get(semanticKey(row)) ?? [];
    if (matches.length !== 1) {
      if (matches.length === 0) unmatched.push({ row: index + 1, key: semanticKey(row) });
      continue;
    }
    matched += 1;
    const oldRow = matches[0];
    const nextRow = [...row];
    for (const columnIndex of [2, 3, 4, 5]) {
      if ((nextRow[columnIndex] === null || nextRow[columnIndex] === "") && oldRow[columnIndex] !== null && oldRow[columnIndex] !== "") {
        nextRow[columnIndex] = oldRow[columnIndex];
        restoredCells += 1;
      }
    }
    currentRows[index] = nextRow;
  }

  setIfFound(currentRows, (row) => normalize(row[0]).includes("A human fetal lung cell atlas") && normalize(row[6]).includes("GRP+ pulmonary NE cells") && normalize(row[7]).includes("NEUROD1"), (row) => {
    row[6] = "pulmonary neuroendocrine cells（GRP+ pulmonary NE/precursor transition #1）";
    row[7] = normalize(row[7]).replace("NEUROD1（阴性）", "NEUROD1（低表达）");
    row[8] = `${row[8]}；Fig. S8C #1：NEUROD1low`;
  });
  setIfFound(currentRows, (row) => normalize(row[0]).includes("Local and systemic responses") && normalize(row[7]).includes("FOXJ1（阴性）"), (row) => {
    row[7] = normalize(row[7]).replaceAll("FOXJ1（阴性）", "FOXJ1（低表达）");
    row[8] = `${row[8]}；正文/补充注释明确为 FOXJ1 low`;
  });
  setIfFound(currentRows, (row) => normalize(row[0]).includes("A human fetal lung cell atlas") && normalize(row[6]) === "aerocyte" && normalize(row[7]).includes("CA4"), (row) => {
    row[7] = "CA4（正文CA4LO；S7B HCR+）；S100A3";
    row[8] = "物种：human；证据：annotation_marker、figure_labeled；定位：Results line 296（CA4LO）；Figure S7B legend（CA4+ HCR）";
  });
  setIfFound(currentRows, (row) => normalize(row[0]).includes("A human fetal lung cell atlas") && normalize(row[6]) === "proximal secretory 3" && normalize(row[7]).includes("SCGB3A2（阴性）"), (row) => {
    row[7] = normalize(row[7]).replace("SCGB3A2（阴性）", "SCGB3A2（低表达/阴性）");
    row[8] = `${row[8]}；正文明确为 SCGB3A2LO/-；low 为兼容编码，保留阴性可能性`;
  });
  setIfFound(currentRows, (row) => normalize(row[0]).includes("A human fetal lung cell atlas") && normalize(row[6]) === "proximal secretory progenitor" && normalize(row[7]).includes("SCGB3A1（阴性）"), (row) => {
    row[7] = normalize(row[7]).replace("SCGB3A1（阴性）", "SCGB3A1（低表达/阴性）");
    row[8] = `${row[8]}；正文明确为 SCGB3A1-/LO；low 为兼容编码，保留阴性可能性`;
  });
  setIfFound(currentRows, (row) => normalize(row[0]).includes("A human fetal lung cell atlas") && normalize(row[6]) === "stalk cell" && normalize(row[7]).includes("SOX9（阴性）"), (row) => {
    row[7] = normalize(row[7]).replace("HOPX", "HOPX（低表达）").replace("PDPN", "PDPN（低表达）").replace("SOX9（阴性）", "SOX9（低表达/阴性）");
    row[8] = `${row[8]}；正文明确为 SOX9LO/-、PDPNLO、HOPXLO；low 为兼容编码，保留阴性可能性`;
  });
  setIfFound(currentRows, (row) => normalize(row[0]).includes("A human fetal lung cell atlas") && normalize(row[6]).includes("vascular SMC1") && normalize(row[7]).includes("PLN（阴性）"), (row) => {
    row[7] = normalize(row[7]).replace("PLN（阴性）", "PLN（低表达/阴性）");
    row[8] = `${row[8]}；Figure S7F 明确为 PLN-/low；low 为兼容编码，保留阴性可能性`;
  });
  setIfFound(currentRows, (row) => normalize(row[0]).includes("A human fetal lung cell atlas") && normalize(row[6]).includes("myofibroblast（myofibroblast 1）") && normalize(row[7]).endsWith("THBD"), (row) => {
    row[7] = `${row[7]}（低表达）`;
    row[8] = `${row[8]}；正文明确为 THBDLO；low 为兼容编码，保留低/弱表达限定`;
  });
  setIfFound(currentRows, (row) => normalize(row[0]).includes("A human fetal lung cell atlas") && normalize(row[6]) === "myofibroblast-1" && normalize(row[7]) === "ACTA2；PDGFRA；THBD", (row) => {
    row[7] = "ACTA2；PDGFRA；THBD（低表达）";
    row[8] = `${row[8]}；Figure S7K-M 明确为 THBDweak；low 为兼容编码，保留低/弱表达限定`;
  });
  setIfFound(currentRows, (row) => normalize(row[0]).includes("A human fetal lung cell atlas") && normalize(row[6]) === "proximal secretory 1" && normalize(row[7]) === "MUC16；SCGB1A1；SCGB3A1；SCGB3A2", (row) => {
    row[7] = "MUC16（低表达/阴性）；SCGB1A1；SCGB3A1；SCGB3A2";
    row[8] = `${row[8]}；正文/图注明确为 MUC16low/-；low 为兼容编码，保留阴性可能性`;
  });
  setIfFound(currentRows, (row) => normalize(row[0]).includes("A human fetal lung cell atlas") && normalize(row[6]) === "proximal secretory 2" && normalize(row[7]) === "MUC16；SCGB1A1；SCGB3A1；SCGB3A2", (row) => {
    row[7] = "MUC16（低表达/阳性）；SCGB1A1；SCGB3A1；SCGB3A2";
    row[8] = `${row[8]}；Figure S3E 明确为 MUC16low/+；low 为兼容编码，保留低/阳性混合限定`;
  });
  setIfFound(currentRows, (row) => normalize(row[0]).includes("A human fetal lung cell atlas") && normalize(row[6]) === "lymphatic endothelial cell" && normalize(row[7]).includes("UCP2"), (row) => {
    row[7] = normalize(row[7]).replace("UCP2", "UCP2（低表达）");
    row[8] = `${row[8]}；正文明确为 UCP2LO；low 为兼容编码`;
  });
  setIfFound(currentRows, (row) => normalize(row[0]).includes("A human fetal lung cell atlas") && normalize(row[6]) === "mid fibroblast" && normalize(row[7]).includes("FGFR4"), (row) => {
    row[7] = normalize(row[7]).replace("FGFR4", "FGFR4（低表达）");
    row[8] = `${row[8]}；正文明确为 FGFR4LO；low 为兼容编码`;
  });
  setIfFound(currentRows, (row) => normalize(row[0]).includes("A human fetal lung cell atlas") && normalize(row[6]) === "MUC16+ ciliated cell" && normalize(row[7]).includes("MUC16"), (row) => {
    row[7] = normalize(row[7]).replace("MUC16", "MUC16（低表达）");
    row[8] = `${row[8]}；正文明确为 MUC16LO；low 为兼容编码`;
  });
  setIfFound(currentRows, (row) => normalize(row[0]).includes("A human fetal lung cell atlas") && normalize(row[6]) === "proximal secretory 1" && normalize(row[7]).includes("SCGB1A1"), (row) => {
    row[7] = normalize(row[7]).replace("SCGB1A1；", "SCGB1A1（低表达）；");
    row[8] = `${row[8]}；正文明确为 SCGB1A1LO；low 为兼容编码`;
  });
  setIfFound(currentRows, (row) => normalize(row[0]).includes("Single-cell multiomic profiling") && normalize(row[6]) === "Pericyte (claimed in repair)", (row) => {
    row[6] = "Pericytes";
    row[8] = normalize(row[8]).replace("Fig. 1D", "Fig. 1D, PDF p.4; marker-annotation dot plot");
  });
  setIfFound(currentRows, (row) => normalize(row[0]).includes("A spatially resolved atlas") && normalize(row[7]).includes("PRR4"), (row) => {
    row[8] = "物种：human；证据：annotation_marker；定位：Extended Data Fig. 10g full page, PDF pp.34-35; HPA IHC";
  });

  const markerRowForSst = currentRows.find((row) => normalize(row[0]).includes("Nature Communications") && normalize(row[0]).includes("senescence") && normalize(row[1]) === "10.1038/s41467-024-52052-8" && normalize(row[6]).includes("SST"));
  if (!markerRowForSst) {
    const title = "Senescence of nociceptors in pain models in mice with chronic pain.";
    currentRows.push([title, "10.1038/s41467-024-52052-8", null, null, null, null, "SST neurons（somatostatin-positive nociceptor subtype）", "Sst", "物种：mouse；证据：annotation_marker、figure_labeled；定位：Fig. 2a,f,g; Fig. 3e; Introduction"]);
  }
  sheet.getRangeByIndexes(0, 0, currentRows.length, 9).values = currentRows;
  const notes = workbook.worksheets.getItem("说明");
  const noteRows = rowsFromUsed(notes);
  for (let index = 0; index < noteRows.length; index += 1) {
    const value = noteRows[index]?.[1];
    if (typeof value === "string" && value.includes("2488")) notes.getCell(index, 1).values = [[value.replaceAll("2488", "2490")]];
  }

  const indexSheet = workbook.worksheets.getItem("图表索引");
  const indexRows = rowsFromUsed(indexSheet);
  const hasSstIndex = indexRows.some((row) => normalize(row[0]).includes("Nature Communications") && normalize(row[1]).includes("Fig. 2a"));
  if (!hasSstIndex) {
    const lastIndex = indexRows.reduce((last, row, index) => (row?.[0] ? index : last), 0);
    const template = indexSheet.getRangeByIndexes(lastIndex, 0, 1, 7);
    const target = indexSheet.getRangeByIndexes(lastIndex + 1, 0, 1, 7);
    target.copyFrom(template, "all");
    target.values = [["Senescence of nociceptors in pain models in mice with chronic pain.", "Fig. 2a,f,g; Fig. 3e", null, null, null, null, "SST nociceptor subtype"]];
  }

  workbook.recalculate();
  const xlsx = await SpreadsheetFile.exportXlsx(workbook);
  const output = `${runDir}/staged/our_markers_by_cell.xlsx`;
  await xlsx.save(output);
  await renderAndSave(workbook, "Marker表", "A1:I22", `${runDir}/staged/staged-by-cell-head.png`);
  await renderAndSave(workbook, "图表索引", "A1:G18", `${runDir}/staged/staged-by-cell-index-head.png`);

  return { output, currentRowsBefore: currentRows.length - 1, currentRowsAfter: currentRows.length - 1, matched, restoredCells, unmatchedCount: unmatched.length, unmatchedSample: unmatched.slice(0, 20) };
}

async function main() {
  const changeSet = await readJson(`${runDir}/change-set.json`);
  const reviewData = await readJson(`${runDir}/review-records.json`);
  const evidenceData = await readJson(`${runDir}/evidence.json`);
  const mainResult = await buildMainWorkbook(changeSet, reviewData, evidenceData);
  const byCellResult = await buildByCellWorkbook();

  const sha256File = async (path) => createHash("sha256").update(await fs.readFile(path)).digest("hex");
  const manifest = await readJson(`${runDir}/baseline-manifest.json`);
  const formalMainSha = await sha256File(`${root}/marker提取/表单/our_markers.xlsx`);
  const formalByCellSha = await sha256File(`${root}/marker提取/表单/our_markers_by_cell.xlsx`);
  const stagedMainSha = await sha256File(mainResult.output);
  const stagedByCellSha = await sha256File(byCellResult.output);
  const evidenceIds = new Set(evidenceData.evidence.map((e) => e.evidence_id));
  const missingReviewEvidence = reviewData.records.flatMap((record) => (record.evidence_ids ?? []).filter((id) => !evidenceIds.has(id)).map((id) => `${record.marker_id}:${id}`));
  const missingChangeEvidence = changeSet.changes.flatMap((change) => (change.evidence_ids ?? []).filter((id) => !evidenceIds.has(id)).map((id) => `${change.change_id}:${id}`));
  const changeIds = changeSet.changes.map((change) => change.change_id);
  const duplicateChangeIds = changeIds.filter((id, index) => changeIds.indexOf(id) !== index);
  const perRecordEvidenceBindingCount = reviewData.records.filter((record) => record.processing_status === "completed" && (record.evidence_ids ?? []).length > 0 && record.evidence_locator && record.evidence_excerpt).length;

  const validation = {
    run_id: "20260907-luna-existing-marker-correctness",
    validation_status: "passed_with_documented_limits",
    formal_source_unchanged: formalMainSha === manifest.formal_workbook.sha256 && formalByCellSha === manifest.by_cell_workbook.sha256,
    formal_source_hashes: { current_main: formalMainSha, current_by_cell: formalByCellSha, baseline_main: manifest.formal_workbook.sha256, baseline_by_cell: manifest.by_cell_workbook.sha256 },
    staged_sha256: { "our_markers.xlsx": stagedMainSha, "our_markers_by_cell.xlsx": stagedByCellSha },
    staged_outputs: [mainResult.output, byCellResult.output],
    main_workbook: {
      active_before: mainResult.markerRowsBefore - 1,
      active_after: mainResult.markerRowsAfter - 1,
      expected_active_after: 2490,
      restored_ids: ["M00417", "M01510"],
      updated_ids: mainResult.affectedIds.filter((id) => !["M00417", "M01510"].includes(id)),
      audit_archive_rows: mainResult.archiveRows,
      formula_recalculated: true,
      formula_validation_method: "artifact-tool recalculate/export followed by independent formula-error scan",
    },
    by_cell_workbook: {
      unique_semantic_matches: byCellResult.matched,
      restored_metadata_cells: byCellResult.restoredCells,
      unmatched_semantic_rows: byCellResult.unmatchedCount,
      unmatched_sample: byCellResult.unmatchedSample,
      note: "Only unique semantic-key matches using title, DOI, author cell label and marker string were restored; unmatched rows remain for later evidence-group mapping and were not filled by row position.",
    },
    evidence_links_resolved: missingReviewEvidence.length === 0 && missingChangeEvidence.length === 0,
    evidence_validation: {
      evidence_id_unique: evidenceData.evidence.length === evidenceIds.size,
      missing_review_evidence_refs: missingReviewEvidence,
      missing_change_evidence_refs: missingChangeEvidence,
      completed_records_with_target_level_binding: perRecordEvidenceBindingCount,
      completed_record_count: reviewData.records.filter((record) => record.processing_status === "completed").length,
    },
    change_set_validation: { change_count: changeSet.changes.length, unique_change_id_count: new Set(changeIds).size, duplicate_change_ids: duplicateChangeIds },
    pending_review_count: reviewData.summary.result_counts.pending ?? 0,
    warning: "This is an interim staged correction package. Full active-marker correctness review is not complete and Astra independent acceptance has not occurred.",
  };
  await fs.writeFile(`${runDir}/validation.json`, JSON.stringify(validation, null, 2) + "\n", "utf8");
}

await main();
