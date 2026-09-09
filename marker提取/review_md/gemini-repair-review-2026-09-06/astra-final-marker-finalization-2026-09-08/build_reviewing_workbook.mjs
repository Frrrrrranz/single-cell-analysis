import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const runDir = path.dirname(fileURLToPath(import.meta.url));
const sourcePath = path.resolve(runDir, "../execution/luna-existing-marker-correctness/staged/our_markers.xlsx");
const outputDir = path.join(runDir, "staged");
const outputPath = path.join(outputDir, "our_markers_reviewing.xlsx");
const decisionsPath = path.join(runDir, "decisions-context-2922.json");

function rowsFromUsed(sheet) {
  const values = sheet.getUsedRange()?.values ?? [];
  return values.map((row) => Array.from(row));
}

function replaceCountText(value) {
  if (typeof value !== "string") return value;
  return value.replaceAll("2490", "2482");
}

async function savePreview(workbook, sheetName, range, fileName) {
  const preview = await workbook.render({ sheetName, range, scale: 1, format: "png" });
  await fs.writeFile(path.join(outputDir, fileName), new Uint8Array(await preview.arrayBuffer()));
}

const decisionData = JSON.parse(await fs.readFile(decisionsPath, "utf8"));
const batchDecisionFiles = (await fs.readdir(runDir))
  .filter((name) => /^decisions-review-batch-\d+\.json$/.test(name))
  .sort();
const batchDecisions = (
  await Promise.all(batchDecisionFiles.map(async (name) => JSON.parse(await fs.readFile(path.join(runDir, name), "utf8"))))
).flatMap((document) => document.decisions);
const deferredDecisionFiles = (await fs.readdir(runDir))
  .filter((name) => /^decisions-deferred-batch-\d+\.json$/.test(name))
  .sort();
const deferredDecisions = (
  await Promise.all(deferredDecisionFiles.map(async (name) => JSON.parse(await fs.readFile(path.join(runDir, name), "utf8"))))
).flatMap((document) => document.decisions);
const allDecisions = [...decisionData.decisions, ...batchDecisions, ...deferredDecisions];
const deferredReviewSummary = JSON.parse(await fs.readFile(path.join(runDir, "deferred-review-summary.json"), "utf8"));
const rejected = allDecisions.filter((item) => item.decision === "exclude_from_final");
const rejectedIds = new Set(rejected.map((item) => item.marker_id));
const corrections = new Map(
  allDecisions
    .filter((item) => item.decision === "correct_and_accept")
    .map((item) => [item.marker_id, item.after_values]),
);
if (rejectedIds.size !== 8) throw new Error(`Expected 8 rejected markers, got ${rejectedIds.size}`);
if (corrections.size !== 5) throw new Error(`Expected 5 corrected markers, got ${corrections.size}`);

const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(sourcePath));
const markers = workbook.worksheets.getItem("markers");
const markerRows = rowsFromUsed(markers);
const headers = markerRows[0];
const markerIdIndex = headers.indexOf("marker_id");
if (markerIdIndex < 0) throw new Error("markers sheet is missing marker_id");

const dataRows = markerRows.slice(1).filter((row) => row?.[markerIdIndex]);
const sourceRowsById = new Map(dataRows.map((row) => [String(row[markerIdIndex]), row]));
const missingRejectedIds = [...rejectedIds].filter((id) => !sourceRowsById.has(id));
if (missingRejectedIds.length) throw new Error(`Rejected IDs missing from source workbook: ${missingRejectedIds.join(", ")}`);

const correctedRows = dataRows.map((row) => {
  const correctedValues = corrections.get(String(row[markerIdIndex]));
  return correctedValues ? headers.map((header) => correctedValues[String(header)] ?? null) : row;
});
const retainedRows = correctedRows.filter((row) => !rejectedIds.has(String(row[markerIdIndex])));
if (dataRows.length !== 2490 || retainedRows.length !== 2482) {
  throw new Error(`Unexpected row counts: source=${dataRows.length}, retained=${retainedRows.length}`);
}

const markerUsed = markers.getUsedRange();
markerUsed.clear({ applyTo: "contents" });
markers.getRangeByIndexes(0, 0, retainedRows.length + 1, headers.length).values = [headers, ...retainedRows];

const notes = workbook.worksheets.getItem("说明与统计");
const noteRows = rowsFromUsed(notes);
for (let rowIndex = 0; rowIndex < noteRows.length; rowIndex += 1) {
  for (let columnIndex = 0; columnIndex < noteRows[rowIndex].length; columnIndex += 1) {
    const oldValue = noteRows[rowIndex][columnIndex];
    const newValue = replaceCountText(oldValue);
    if (newValue !== oldValue) notes.getCell(rowIndex, columnIndex).values = [[newValue]];
  }
}

const archive = workbook.worksheets.getItem("audit_archive_20260907");
const archiveRows = rowsFromUsed(archive);
const archiveHeaders = archiveRows[0];
const archiveHeaderIndex = new Map(archiveHeaders.map((header, index) => [String(header), index]));
const lastArchiveRowIndex = archiveRows.reduce((last, row, index) => (row?.some((value) => value !== null && value !== "") ? index : last), 0);
const newArchiveRows = rejected.map((decision) => {
  const sourceRow = sourceRowsById.get(decision.marker_id);
  const sourceObject = Object.fromEntries(headers.map((header, index) => [String(header), sourceRow[index] ?? null]));
  const extras = {
    review_id: decision.decision_id,
    scope: "astra_final_marker_finalization",
    archive_action: "exclude_from_final",
    target_marker_id: decision.marker_id,
    evidence_ids: null,
    reason: decision.astra_reason,
    executor: decision.reviewed_by,
    reviewed_at: decision.reviewed_at,
    change_status: "active",
    supersedes: null,
    superseded_by: null,
  };
  return archiveHeaders.map((header) => sourceObject[String(header)] ?? extras[String(header)] ?? null);
});

const archiveWriteStart = lastArchiveRowIndex + 1;
if (lastArchiveRowIndex >= 1) {
  const template = archive.getRangeByIndexes(lastArchiveRowIndex, 0, 1, archiveHeaders.length);
  for (let offset = 0; offset < newArchiveRows.length; offset += 1) {
    archive.getRangeByIndexes(archiveWriteStart + offset, 0, 1, archiveHeaders.length).copyFrom(template, "all");
  }
}
archive.getRangeByIndexes(archiveWriteStart, 0, newArchiveRows.length, archiveHeaders.length).values = newArchiveRows;

for (const requiredHeader of ["archive_action", "target_marker_id", "reason"]) {
  if (!archiveHeaderIndex.has(requiredHeader)) throw new Error(`Archive sheet is missing ${requiredHeader}`);
}

workbook.recalculate();
await fs.mkdir(outputDir, { recursive: true });
const xlsx = await SpreadsheetFile.exportXlsx(workbook);
await xlsx.save(outputPath);

const overview = await workbook.inspect({
  kind: "workbook,sheet,table",
  maxChars: 16000,
  tableMaxRows: 5,
  tableMaxCols: 12,
  tableMaxCellChars: 120,
});
const formulaErrors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!",
  options: { useRegex: true, maxResults: 300 },
  summary: "formula error scan after invalid-marker removal",
  maxChars: 12000,
});

await savePreview(workbook, "markers", "A1:AE18", "reviewing-markers-head.png");
await savePreview(workbook, "audit_archive_20260907", `A${Math.max(1, archiveWriteStart - 1)}:AM${archiveWriteStart + newArchiveRows.length}`, "reviewing-invalid-marker-archive.png");

const validation = {
  run_id: "20260909-astra-marker-reviewing",
  source_workbook: sourcePath,
  output_workbook: outputPath,
  source_active_marker_count: dataRows.length,
  active_marker_count: retainedRows.length,
  excluded_marker_ids: [...rejectedIds].sort(),
  corrected_marker_ids: [...corrections.keys()].sort(),
  archive_rows_appended: newArchiveRows.length,
  formal_workbook_overwritten: false,
  carried_forward_evidence_bound_count: 1819,
  deferred_source_count: deferredReviewSummary.source_count,
  deferred_reviewed_count: deferredReviewSummary.reviewed_count,
  deferred_unresolved_count: deferredReviewSummary.remaining_count,
  reviewed_from_remaining_221: 221,
  remaining_review_count: 0,
  workbook_overview: overview.ndjson,
  formula_error_scan: formulaErrors.ndjson,
};
await fs.writeFile(path.join(runDir, "filter-validation.json"), `${JSON.stringify(validation, null, 2)}\n`, "utf8");

console.log(JSON.stringify({
  outputPath,
  sourceActive: dataRows.length,
  activeAfter: retainedRows.length,
  excluded: [...rejectedIds].sort(),
  corrected: [...corrections.keys()].sort(),
  formulaErrors: formulaErrors.ndjson,
}, null, 2));
