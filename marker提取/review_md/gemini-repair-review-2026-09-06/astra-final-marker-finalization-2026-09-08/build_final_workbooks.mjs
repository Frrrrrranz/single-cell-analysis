import fs from "node:fs/promises";
import path from "node:path";
import { createHash } from "node:crypto";
import { fileURLToPath } from "node:url";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const runDir = path.dirname(fileURLToPath(import.meta.url));
const reviewingPath = path.join(runDir, "staged", "our_markers_reviewing.xlsx");
const byCellTemplatePath = path.resolve(runDir, "../execution/luna-existing-marker-correctness/staged/our_markers_by_cell.xlsx");
const mainOutputPath = path.join(runDir, "staged", "our_markers_final.xlsx");
const byCellOutputPath = path.join(runDir, "staged", "our_markers_by_cell_final.xlsx");
const unresolvedIds = new Set(["M01806", "M01807"]);

function rowsFromUsed(sheet) {
  return (sheet.getUsedRange()?.values ?? []).map((row) => Array.from(row));
}

function markerDisplay(record) {
  const polarity = String(record.marker_polarity ?? "").toLowerCase();
  if (polarity === "negative") return `${record.gene_symbol}（阴性）`;
  if (polarity === "low") return `${record.gene_symbol}（低表达）`;
  if (polarity === "unknown" || polarity === "") return `${record.gene_symbol}（方向未明）`;
  return record.gene_symbol;
}

function normalizedDoi(paperId) {
  return paperId.startsWith("DOI_") ? paperId.slice(4).replaceAll("_", "/") : paperId;
}

function buildByCellRows(records, titleMap, metadataMap) {
  const groups = new Map();
  for (const record of records) {
    const key = [record.paper_id, record.cell_type, record.subtype ?? "", record.species].join("\u001f");
    const group = groups.get(key) ?? {
      paper_id: record.paper_id,
      title: titleMap.get(record.paper_id) ?? record.paper_id,
      cell_type: record.cell_type,
      subtype: record.subtype ?? "",
      species: record.species,
      markers: [],
      evidence: [],
      locators: [],
    };
    const display = markerDisplay(record);
    if (!group.markers.includes(display)) group.markers.push(display);
    if (record.evidence_type && !group.evidence.includes(record.evidence_type)) group.evidence.push(record.evidence_type);
    if (record.source_locator && !group.locators.includes(record.source_locator)) group.locators.push(record.source_locator);
    groups.set(key, group);
  }
  return [...groups.values()].map((group) => {
    const doi = normalizedDoi(group.paper_id);
    const authorLabel = group.subtype ? `${group.cell_type}（${group.subtype}）` : group.cell_type;
    const metadata = metadataMap.get(`${doi}\u001f${authorLabel}`) ?? [null, null, null, null];
    return [
      group.title,
      doi,
      ...metadata,
      authorLabel,
      group.markers.join("；"),
      `物种：${group.species}；证据：${group.evidence.join("、")}；定位：${group.locators.join("；")}`,
    ];
  });
}

function buildPanelRows(records, titleMap, panelMetadataMap) {
  const seen = new Set();
  const rows = [];
  for (const record of records) {
    const title = titleMap.get(record.paper_id) ?? record.paper_id;
    const locator = record.source_locator ?? "";
    const key = `${title}\u001f${locator}`;
    if (seen.has(key)) continue;
    seen.add(key);
    const metadata = panelMetadataMap.get(key) ?? [null, null, null, null, null];
    rows.push([title, locator || null, ...metadata]);
  }
  return rows;
}

async function renderAndSave(workbook, sheetName, range, fileName) {
  const preview = await workbook.render({ sheetName, range, scale: 1, format: "png" });
  await fs.writeFile(path.join(runDir, "staged", fileName), new Uint8Array(await preview.arrayBuffer()));
}

const mainWorkbook = await SpreadsheetFile.importXlsx(await FileBlob.load(reviewingPath));
const markers = mainWorkbook.worksheets.getItem("markers");
const markerRows = rowsFromUsed(markers);
const headers = markerRows[0].map(String);
const markerIdIndex = headers.indexOf("marker_id");
const sourceRows = markerRows.slice(1).filter((row) => row?.[markerIdIndex]);
const unresolvedRows = sourceRows.filter((row) => unresolvedIds.has(String(row[markerIdIndex])));
const retainedRows = sourceRows.filter((row) => !unresolvedIds.has(String(row[markerIdIndex])));
if (sourceRows.length !== 2482 || unresolvedRows.length !== 2 || retainedRows.length !== 2480) {
  throw new Error(`Unexpected final counts: source=${sourceRows.length}, unresolved=${unresolvedRows.length}, retained=${retainedRows.length}`);
}

const markerUsed = markers.getUsedRange();
markerUsed.clear({ applyTo: "contents" });
markers.getRangeByIndexes(0, 0, retainedRows.length + 1, headers.length).values = [headers, ...retainedRows];
const oldTable = markers.tables.getItem("OurMarkersTable");
oldTable.delete();
markers.tables.add(`A1:AE${retainedRows.length + 1}`, true, "OurMarkersTable");

const unresolvedSheetName = "unresolved_hold_20260909";
const existingUnresolved = mainWorkbook.worksheets.items.find((sheet) => sheet.name === unresolvedSheetName);
if (existingUnresolved) mainWorkbook.worksheets.delete(unresolvedSheetName);
const unresolved = mainWorkbook.worksheets.add(unresolvedSheetName);
const unresolvedHeaders = [...headers, "decision_id", "publication_status", "reason", "reviewed_by", "reviewed_at"];
const unresolvedOutputRows = unresolvedRows.map((row) => [
  ...row,
  `ASTRA-221-B006-${row[markerIdIndex]}`,
  "defer_unresolved_not_published",
  "主文仅列出 cardiac macrophage 抗体 panel；缺 Supplementary Information 中的实际 flow gate，不能确认单个阳性关系。",
  "GPT-6 Astra",
  "2026-09-09",
]);
unresolved.getRangeByIndexes(0, 0, 1, unresolvedHeaders.length).values = [unresolvedHeaders];
unresolved.getRangeByIndexes(1, 0, unresolvedOutputRows.length, unresolvedHeaders.length).values = unresolvedOutputRows;
unresolved.getRangeByIndexes(0, 0, 1, unresolvedHeaders.length).format = {
  fill: "#9C6500",
  font: { color: "#FFFFFF", bold: true },
  wrapText: true,
};
unresolved.getRangeByIndexes(0, 0, unresolvedOutputRows.length + 1, unresolvedHeaders.length).format.borders = { preset: "all", style: "thin", color: "#D9D9D9" };
unresolved.getRange("A:AJ").format.columnWidth = 18;
unresolved.getRange("AH:AJ").format.columnWidth = 32;
unresolved.freezePanes.freezeRows(1);

const notes = mainWorkbook.worksheets.getItem("说明与统计");
const noteRows = rowsFromUsed(notes);
for (let rowIndex = 0; rowIndex < noteRows.length; rowIndex += 1) {
  for (let columnIndex = 0; columnIndex < noteRows[rowIndex].length; columnIndex += 1) {
    const value = noteRows[rowIndex][columnIndex];
    if (typeof value === "string" && value.includes("2482")) {
      notes.getCell(rowIndex, columnIndex).values = [[value.replaceAll("2482", "2480")]];
    }
  }
}
notes.getRange("A30:B30").values = [["Astra 最终收口（2026-09-09）", "发布集合 2480 条；8 条不合格已归档；M01806、M01807 转入 unresolved_hold_20260909，不计入发布集合。"]];
mainWorkbook.recalculate();
await (await SpreadsheetFile.exportXlsx(mainWorkbook)).save(mainOutputPath);

const records = retainedRows.map((row) => Object.fromEntries(headers.map((header, index) => [header, row[index] ?? null])));
const byCellWorkbook = await SpreadsheetFile.importXlsx(await FileBlob.load(byCellTemplatePath));
const markerSheet = byCellWorkbook.worksheets.getItem("Marker表");
const currentMarkerRows = rowsFromUsed(markerSheet);
const titleMap = new Map();
const metadataMap = new Map();
for (const row of currentMarkerRows.slice(1)) {
  if (!row?.[0] || !row?.[1]) continue;
  titleMap.set(String(row[1]), row[0]);
  titleMap.set(`DOI_${String(row[1]).replaceAll("/", "_")}`, row[0]);
  metadataMap.set(`${row[1]}\u001f${row[6]}`, [row[2] ?? null, row[3] ?? null, row[4] ?? null, row[5] ?? null]);
}
const indexSheet = byCellWorkbook.worksheets.getItem("图表索引");
const currentPanelRows = rowsFromUsed(indexSheet);
const panelMetadataMap = new Map(
  currentPanelRows.slice(1).filter((row) => row?.[0]).map((row) => [`${row[0]}\u001f${row[1] ?? ""}`, [row[2] ?? null, row[3] ?? null, row[4] ?? null, row[5] ?? null, row[6] ?? null]]),
);
const byCellRows = buildByCellRows(records, titleMap, metadataMap);
const panelRows = buildPanelRows(records, titleMap, panelMetadataMap);
const markerSheetUsed = markerSheet.getUsedRange();
markerSheet.getRangeByIndexes(1, 0, Math.max(markerSheetUsed.values.length - 1, byCellRows.length), 9).clear({ applyTo: "contents" });
markerSheet.getRangeByIndexes(1, 0, byCellRows.length, 9).values = byCellRows;
const indexSheetUsed = indexSheet.getUsedRange();
indexSheet.getRangeByIndexes(1, 0, Math.max(indexSheetUsed.values.length - 1, panelRows.length), 7).clear({ applyTo: "contents" });
indexSheet.getRangeByIndexes(1, 0, panelRows.length, 7).values = panelRows;
const info = byCellWorkbook.worksheets.getItem("说明");
info.getRange("B3").values = [["2026-09-09"]];
info.getRange("B4").values = [[`our_markers_final.xlsx 的已确认发布集合，共 ${records.length} 条。`]];
info.getRange("B13").values = [[records.length]];
info.getRange("B14").values = [[panelRows.length]];
info.getRange("B15").values = [[new Set(records.map((record) => record.paper_id)).size]];
info.getRange("B16").values = [["依据 Astra 终审发布集合同步；8 条明确不合格与 2 条 unresolved 均不进入本汇总。"]];
byCellWorkbook.recalculate();
await (await SpreadsheetFile.exportXlsx(byCellWorkbook)).save(byCellOutputPath);

await renderAndSave(mainWorkbook, "markers", "A1:AE18", "final-markers-head.png");
await renderAndSave(mainWorkbook, unresolvedSheetName, "A1:AJ3", "final-unresolved-hold.png");
await renderAndSave(byCellWorkbook, "Marker表", "A1:I18", "final-by-cell-head.png");
await renderAndSave(byCellWorkbook, "说明", "A1:B16", "final-by-cell-notes.png");

const sha256 = async (filePath) => createHash("sha256").update(await fs.readFile(filePath)).digest("hex");
const validation = {
  run_id: "20260909-astra-final-marker-publication",
  published_marker_count: records.length,
  published_unique_marker_ids: new Set(records.map((record) => record.marker_id)).size,
  unresolved_marker_count: unresolvedOutputRows.length,
  unresolved_marker_ids: [...unresolvedIds].sort(),
  by_cell_group_count: byCellRows.length,
  panel_index_count: panelRows.length,
  paper_count: new Set(records.map((record) => record.paper_id)).size,
  outputs: {
    our_markers_final: { path: mainOutputPath, sha256: await sha256(mainOutputPath) },
    our_markers_by_cell_final: { path: byCellOutputPath, sha256: await sha256(byCellOutputPath) },
  },
};
await fs.writeFile(path.join(runDir, "final-workbook-build-validation.json"), `${JSON.stringify(validation, null, 2)}\n`, "utf8");
console.log(JSON.stringify(validation, null, 2));
