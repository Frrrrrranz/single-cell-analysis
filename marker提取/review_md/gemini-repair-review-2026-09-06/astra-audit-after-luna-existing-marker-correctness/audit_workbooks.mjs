import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const auditDir = path.dirname(fileURLToPath(import.meta.url));
const runDir = path.resolve(auditDir, "../execution/luna-existing-marker-correctness");

async function importWorkbook(filePath) {
  return SpreadsheetFile.importXlsx(await FileBlob.load(filePath));
}

async function auditWorkbook(fileName) {
  const filePath = path.join(runDir, "staged", fileName);
  const workbook = await importWorkbook(filePath);
  const overview = await workbook.inspect({
    kind: "workbook,sheet,table",
    maxChars: 12000,
    tableMaxRows: 4,
    tableMaxCols: 12,
    tableMaxCellChars: 100,
  });
  const formulaErrors = await workbook.inspect({
    kind: "match",
    searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!",
    options: { useRegex: true, maxResults: 300 },
    summary: "independent Astra formula-error scan",
    maxChars: 12000,
  });
  return { workbook, filePath, overview: overview.ndjson, formulaErrors: formulaErrors.ndjson };
}

const main = await auditWorkbook("our_markers.xlsx");
const byCell = await auditWorkbook("our_markers_by_cell.xlsx");

const mainPreview = await main.workbook.render({
  sheetName: "markers",
  range: "A1:AE18",
  scale: 1,
  format: "png",
});
await fs.writeFile(path.join(auditDir, "staged-main-preview.png"), new Uint8Array(await mainPreview.arrayBuffer()));

const archivePreview = await main.workbook.render({
  sheetName: "audit_archive_20260907",
  range: "A1:AI16",
  scale: 1,
  format: "png",
});
await fs.writeFile(path.join(auditDir, "staged-archive-preview.png"), new Uint8Array(await archivePreview.arrayBuffer()));

const byCellPreview = await byCell.workbook.render({
  sheetName: "Marker表",
  range: "A1:I22",
  scale: 1,
  format: "png",
});
await fs.writeFile(path.join(auditDir, "staged-by-cell-preview.png"), new Uint8Array(await byCellPreview.arrayBuffer()));

const result = {
  run_id: "20260908-astra-audit-after-luna-existing-marker-correctness",
  files: {
    "our_markers.xlsx": {
      path: main.filePath,
      overview: main.overview,
      formula_errors: main.formulaErrors,
    },
    "our_markers_by_cell.xlsx": {
      path: byCell.filePath,
      overview: byCell.overview,
      formula_errors: byCell.formulaErrors,
    },
  },
  previews: [
    path.join(auditDir, "staged-main-preview.png"),
    path.join(auditDir, "staged-archive-preview.png"),
    path.join(auditDir, "staged-by-cell-preview.png"),
  ],
};

await fs.writeFile(path.join(auditDir, "workbook-audit.json"), JSON.stringify(result, null, 2), "utf8");
console.log(JSON.stringify({
  mainOverview: main.overview.slice(0, 4000),
  mainFormulaErrors: main.formulaErrors,
  byCellOverview: byCell.overview.slice(0, 4000),
  byCellFormulaErrors: byCell.formulaErrors,
}, null, 2));
