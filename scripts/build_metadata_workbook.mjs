import fs from "node:fs/promises";
import { pathToFileURL } from "node:url";

const { SpreadsheetFile, Workbook } = await import(
  pathToFileURL(
    "C:/Users/35221/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs",
  ).href,
);

const projectRoot = "D:/OneDrive/Desktop/组";
const outputPath = `${projectRoot}/marker提取/表单/our_paper_metadata.xlsx`;
const previewDir = "C:/Users/35221/.codex/visualizations/2026/08/21/01a022ba-d0b4-7d81-b52a-2caf6232833a/article_metadata";

async function readJson(path) {
  return JSON.parse(await fs.readFile(path, "utf8"));
}

const scope = await readJson(`${projectRoot}/marker提取/article_metadata/output/scope_mapping.json`);
const metadataFiles = (await fs.readdir(`${projectRoot}/marker提取/article_metadata/output`))
  .filter((file) => file.endsWith("_metadata.json"));
const metadata = new Map();
for (const file of metadataFiles) {
  const value = await readJson(`${projectRoot}/marker提取/article_metadata/output/${file}`);
  metadata.set(value.paper_id, value);
}

const safe = (value) => value ?? "";
const first = (value) => (Array.isArray(value) ? (value[0] ?? {}) : (value ?? {}));
const relative = (path) => safe(path).replaceAll("\\", "/");

const articleHeaders = [
  "task_no", "paper_id", "document_id", "title_original", "doi", "pmid", "species",
  "tissue_source_original", "tissue_source_normalized", "sample_context", "single_cell_type",
  "neural_cell_count", "statistics_method_count", "marker_status", "formal_candidate_count",
  "context_only_count", "source_markdown", "processing_status", "review_status", "issue_count",
  "marker_raw_json",
];
const neuralHeaders = [
  "task_no", "paper_id", "title_original", "cell_name_original", "cell_name_normalized",
  "cell_category", "pns_level", "tissue", "evidence_context", "source_locator",
  "evidence_snippet", "review_status",
];
const statsHeaders = [
  "task_no", "paper_id", "title_original", "analysis_stage", "method_original", "method_normalized",
  "software", "software_version", "threshold", "multiple_testing", "source_locator",
  "evidence_snippet", "review_status",
];
const issueHeaders = [
  "task_no", "paper_id", "title_original", "issue_type", "severity", "field", "description",
  "source_locator", "evidence_snippet",
];

const articleRows = [];
const neuralRows = [];
const statsRows = [];
const issueRows = [];

for (const row of scope.records) {
  const paperId = safe(row.paper_id);
  const item = metadata.get(paperId);
  const identity = item?.article_identity ?? {};
  const tissue = first(item?.tissue_sources);
  const linkage = item?.marker_linkage ?? {};
  const itemIssues = Array.isArray(item?.issues) ? item.issues : [];
  const processingStatus = safe(row.processing_status);
  const reviewStatus = item ? "pending_light_review" : "skipped_missing_markdown";
  articleRows.push([
    safe(row["序号"]), paperId, paperId, safe(identity.title_original || row["论文标题"]),
    safe(identity.doi || row.DOI), safe(identity.pmid || row.PMID),
    Array.isArray(identity.species) ? identity.species.join("; ") : safe(identity.species || row["物种"]),
    safe(tissue.tissue_source_original || row["组织"]), safe(tissue.tissue_source_normalized),
    safe(tissue.sample_context), safe(tissue.single_cell_type || row["技术"]),
    Array.isArray(item?.neural_cells) ? item.neural_cells.length : 0,
    Array.isArray(item?.statistics_methods) ? item.statistics_methods.length : 0,
    safe(linkage.marker_status || row["Marker状态"]), safe(linkage.formal_candidate_count),
    safe(linkage.context_only_count), safe(item?.source_markdown || row.markdown_file),
    processingStatus, reviewStatus, itemIssues.length + (item ? 0 : 1),
    relative(linkage.raw_json_file),
  ]);

  for (const cell of item?.neural_cells ?? []) {
    neuralRows.push([
      safe(row["序号"]), paperId, safe(identity.title_original || row["论文标题"]),
      safe(cell.cell_name_original), safe(cell.cell_name_normalized), safe(cell.cell_category),
      safe(cell.pns_level), safe(cell.tissue), safe(cell.evidence_context), safe(cell.source_locator),
      safe(cell.evidence_snippet), safe(cell.review_status),
    ]);
  }
  for (const method of item?.statistics_methods ?? []) {
    statsRows.push([
      safe(row["序号"]), paperId, safe(identity.title_original || row["论文标题"]),
      safe(method.analysis_stage), safe(method.method_original), safe(method.method_normalized),
      safe(method.software), safe(method.software_version), safe(method.threshold),
      safe(method.multiple_testing), safe(method.source_locator), safe(method.evidence_snippet),
      safe(method.review_status),
    ]);
  }
  for (const issue of itemIssues) {
    issueRows.push([
      safe(row["序号"]), paperId, safe(identity.title_original || row["论文标题"]),
      safe(issue.issue_type), safe(issue.severity), safe(issue.field), safe(issue.description),
      safe(issue.source_locator), safe(issue.evidence_snippet),
    ]);
  }
  if (!item) {
    issueRows.push([
      safe(row["序号"]), paperId, safe(row["论文标题"]), "missing_markdown_skipped", "blocking",
      "source_markdown", "按用户要求跳过：当前没有可用的 review_md 正文。",
      "scope_mapping.json", `PDF状态=${safe(row["PDF状态"])}；预期文件=${safe(row.markdown_file)}`,
    ]);
  }
}

const wb = Workbook.create();
const summary = wb.worksheets.add("article_summary");
const neural = wb.worksheets.add("neural_cells");
const stats = wb.worksheets.add("statistics_methods");
const issues = wb.worksheets.add("issues");

const headerFormat = {
  fill: "#1F4E78",
  font: { bold: true, color: "#FFFFFF" },
  horizontalAlignment: "center",
  verticalAlignment: "center",
  wrapText: true,
};
const titleFormat = {
  fill: "#D9EAF7",
  font: { bold: true, color: "#17365D", size: 14 },
  verticalAlignment: "center",
};
const dataFormat = { verticalAlignment: "top", wrapText: false };
const evidenceFormat = { verticalAlignment: "top", wrapText: true };

function setupSheet(sheet, headers, rows, tableName, title = "") {
  let startRow = 1;
  if (title) {
    sheet.getRange("A1").values = [[title]];
    sheet.getRange("A1").format = titleFormat;
    startRow = 3;
  }
  const headerAddress = `A${startRow}:${String.fromCharCode(64 + headers.length)}${startRow}`;
  const endRow = startRow + rows.length;
  const dataAddress = `A${startRow}:${String.fromCharCode(64 + headers.length)}${endRow}`;
  sheet.getRange(headerAddress).values = [headers];
  sheet.getRange(headerAddress).format = headerFormat;
  if (rows.length > 0) {
    sheet.getRange(`A${startRow + 1}:${String.fromCharCode(64 + headers.length)}${endRow}`).values = rows;
    sheet.getRange(`A${startRow + 1}:${String.fromCharCode(64 + headers.length)}${endRow}`).format = dataFormat;
    sheet.tables.add(dataAddress, true, tableName);
  }
  sheet.freezePanes.freezeRows(startRow);
  sheet.showGridLines = false;
  return { startRow, endRow, lastColumn: String.fromCharCode(64 + headers.length) };
}

const summaryLayout = setupSheet(summary, articleHeaders, articleRows, "ArticleSummary", "文章元数据整理（Markdown 规则提取）");
const summaryEnd = summaryLayout.endRow;
summary.getRange("A2:J2").values = [["任务总数", null, "已生成元数据", null, "按要求跳过", null, "待轻量复核", null, "Issues总数", null]];
summary.getRange("A2:J2").format = { fill: "#EAF2F8", font: { bold: true, color: "#17365D" } };
summary.getRange("B2").formulas = [[`=COUNTA(A4:A${summaryEnd})`]];
summary.getRange("D2").formulas = [[`=COUNTIF(R4:R${summaryEnd},"matched")`]];
summary.getRange("F2").formulas = [[`=COUNTIF(R4:R${summaryEnd},"skipped_missing_markdown")`]];
summary.getRange("H2").formulas = [[`=COUNTIF(S4:S${summaryEnd},"pending_light_review")`]];
summary.getRange("J2").formulas = [[`=SUM(T4:T${summaryEnd})`]];
summary.getRange("A4:U${summaryEnd}").format = dataFormat;

const neuralLayout = setupSheet(neural, neuralHeaders, neuralRows, "NeuralCells");
const statsLayout = setupSheet(stats, statsHeaders, statsRows, "StatisticsMethods");
const issueLayout = setupSheet(issues, issueHeaders, issueRows, "MetadataIssues");

for (const sheet of [summary, neural, stats, issues]) {
  const usedRange = sheet.getUsedRange();
  if (usedRange) {
    usedRange.format.borders = { preset: "outside", style: "thin", color: "#B7C9D6" };
  }
}

summary.getRange(`D4:K${summaryEnd}`).format = evidenceFormat;
summary.getRange(`Q4:U${summaryEnd}`).format = evidenceFormat;
neural.getRange(`J2:K${neuralLayout.endRow}`).format = evidenceFormat;
stats.getRange(`E2:L${statsLayout.endRow}`).format = evidenceFormat;
issues.getRange(`G2:I${issueLayout.endRow}`).format = evidenceFormat;

const widths = [10, 31, 31, 46, 24, 16, 18, 22, 24, 24, 20, 14, 18, 22, 18, 18, 38, 22, 22, 12, 48];
for (let i = 0; i < widths.length; i += 1) {
  const col = String.fromCharCode(65 + i);
  summary.getRange(`${col}1:${col}${summaryEnd}`).format.columnWidth = widths[i];
}
for (const [sheet, widthsByColumn, endRow] of [
  [neural, [10, 31, 44, 28, 28, 18, 12, 20, 18, 32, 70, 18], neuralLayout.endRow],
  [stats, [10, 31, 44, 28, 60, 28, 20, 16, 28, 28, 32, 70, 18], statsLayout.endRow],
  [issues, [10, 31, 44, 32, 14, 24, 60, 32, 70], issueLayout.endRow],
]) {
  for (let i = 0; i < widthsByColumn.length; i += 1) {
    const col = String.fromCharCode(65 + i);
    sheet.getRange(`${col}1:${col}${endRow}`).format.columnWidth = widthsByColumn[i];
  }
}

await fs.mkdir(previewDir, { recursive: true });
for (const sheet of [summary, neural, stats, issues]) {
  const preview = await wb.render({ sheetName: sheet.name, autoCrop: "all", scale: 1, format: "png" });
  await fs.writeFile(`${previewDir}/${sheet.name}.png`, new Uint8Array(await preview.arrayBuffer()));
}
const output = await SpreadsheetFile.exportXlsx(wb);
await output.save(outputPath);
console.log(JSON.stringify({ output: outputPath, article_rows: articleRows.length, neural_rows: neuralRows.length, statistics_rows: statsRows.length, issue_rows: issueRows.length }, null, 2));
