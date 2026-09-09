import fs from "node:fs/promises";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const dir = "D:/OneDrive/Desktop/组/marker提取/review_md/gemini-repair-review-2026-09-06/execution/luna-existing-marker-correctness";
const main = await SpreadsheetFile.importXlsx(await FileBlob.load(`${dir}/staged/our_markers.xlsx`));
const byCell = await SpreadsheetFile.importXlsx(await FileBlob.load(`${dir}/staged/our_markers_by_cell.xlsx`));
const views = [
  [main, "markers", "A40:AE75", "target-markers-early.png"],
  [main, "markers", "A470:AE525", "target-markers-remediation.png"],
  [main, "markers", "A440:AE470", "target-markers-qualifier.png"],
  [main, "markers", "A545:AE555", "target-markers-pln.png"],
  [main, "markers", "A570:AE635", "target-markers-task13-early.png"],
  [main, "markers", "A2265:AE2290", "target-markers-task13-bcell.png"],
  [main, "markers", "A2498:AE2505", "target-markers-tail.png"],
  [main, "audit_archive_20260907", "A3158:AM3165", "target-audit-archive-tail.png"],
  [byCell, "Marker表", "A1:I40", "target-by-cell-early.png"],
  [byCell, "Marker表", "A240:I280", "target-by-cell-task13-early.png"],
  [byCell, "Marker表", "A940:I952", "target-by-cell-task13-bcell.png"],
  [byCell, "Marker表", "A200:I237", "target-by-cell-remediation.png"],
];
for (const [workbook, sheetName, range, filename] of views) {
  const preview = await workbook.render({ sheetName, range, scale: 1, format: "png" });
  await fs.writeFile(`${dir}/staged/${filename}`, new Uint8Array(await preview.arrayBuffer()));
}
