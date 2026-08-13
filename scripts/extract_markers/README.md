# Marker 基因提取管线

从 scRNA-seq 论文中提取细胞类型 marker 基因，经人工复核后结构化入库。

## 架构

```
PDF ─→ 身份审计/文档角色 ─→ MarkItDown ─→ LLM schema v2 ─→ 人工复核
         paper_map.json        转 Markdown       raw JSON       review CSV
                                          ↓                          ↓
                                    import_markers.py ←──── approved/modified
                                        (入库)
                                          ↓
                                    ④ convert_gene_symbols.py
                                        (HGNC 标准化)
```

## 文件说明

| 文件 | 用途 |
|------|------|
| `run_extraction.py` | **主入口**。校验结构化映射和 PDF 哈希，优先用 MarkItDown 解析，再调用 LLM |
| `audit_paper_map.py` | 审计 PDF 的 SHA-256、DOI、PMID、标题及登记路径；仅在零冲突时生成正式映射 |
| `quarantine_pdf_issues.py` | 将损坏/伪 PDF 和字节完全相同的冗余副本移入可恢复隔离区 |
| `marker_schema.py` | marker schema v2 枚举、证据分层和校验规则 |
| `normalize_marker_output.py` | 对既有 schema v2 JSON 应用确定性证据护栏并保留模型原判 |
| `gen_review_sheet.py` | 将 LLM 输出的 JSON 转为复核 CSV（按阅读顺序排列） |
| `import_markers.py` | 将复核通过的 CSV 导入 pns-scrna.xlsx 的 markers sheet |
| `convert_gene_symbols.py` | **可选后处理**。用 mygene 将基因名标准化为 HGNC 符号 |
| `prompts/extract_markers_v4.txt` | 默认提示词，区分作者声明、注释、图表、补充材料与普通 DEG |
| `markers_output_v2/` | schema v2 输出目录（原始 JSON + 复核 CSV） |

## 完整使用流程

### 0. 审计 PDF 与论文映射

`db/cellxgene/paper_registry.json` 是 `pns_papers_summary.xlsx` 的只读 JSON 镜像。运行：

```bash
python audit_paper_map.py
```

审计结果写入 `db/cellxgene/paper_map.audit.json` 和 `paper_map.audit.csv`。修复所有 `blocked` 项后，再执行：

```bash
python audit_paper_map.py --write-map
```

只有全部活动 PDF 通过身份审计、且 `document_id` 唯一时，才会生成正式 `db/cellxgene/paper_map.json`。同一 `paper_id` 可以同时具有 `primary` 和 `supplement` 等不同文档角色；旧映射不得复制回来。

对审计明确识别出的无效文件和完全相同副本，先预览、再执行隔离：

```bash
python quarantine_pdf_issues.py
python quarantine_pdf_issues.py --apply
```

### 1. 提取新论文

```bash
# 设置 LLM API
set MARKER_LLM_API_KEY=sk-your-key-here
set MARKER_LLM_MODEL=gpt-4o

# 处理单篇主文或补充文档（可传 paper_id 或 document_id）
python run_extraction.py \
  --flat-pdf-dir ../../db/cellxgene/cellxgene_filtered/downloads \
  --paper-map ../../db/cellxgene/paper_map.json \
  --paper-id DOI_10.1038_s41586-020-2496-1 \
  --dry-run

# 处理全部活动文档时去掉 --paper-id 和 --dry-run
```

程序会核验 PDF SHA-256；文件在审计后被替换或修改时会拒绝提取。无论 PDF 大小，正文转换均优先使用 MarkItDown。任一分块调用失败时整篇不落盘，避免把残缺结果误当成完整提取。

合并结果还会经过确定性证据护栏：只有原文定位或上下文含作者的 marker/注释措辞，才能保留为正式候选；仅在图中出现表达信号的基因会降为 `cluster_enriched`。模型原判和降级原因会保留，供人工追溯。

### 2. 生成复核表

```bash
python gen_review_sheet.py --input-dir markers_output_v2 --output-dir markers_output_v2 \
  --paper-id DOI_10.1038_s41586-020-2496-1
# 或处理全部
python gen_review_sheet.py --input-dir markers_output_v2 --output-dir markers_output_v2 --all
```

### 3. 人工复核

用 Excel/WPS 打开 `markers_output_v2/{document_id}_review.csv`，逐条检查：

- [ ] 基因符号正确（对照原文/Figure 确认）
- [ ] `evidence_type` 与作者实际措辞一致
- [ ] `marker_polarity` 正/负标记正确
- [ ] `candidate_class=context_only` 的 DEG/推断项没有被误批准
- [ ] cell_type 名称与论文一致
- [ ] 无遗漏 marker（检查 Supplementary tables、Figure legends）
- [ ] 无伪 marker（差异表达基因 ≠ marker 基因）
- [ ] `source_locator` 可追溯回原文位置

将 review_status 改为 `approved` / `modified` / `rejected`。

### 4. 导入数据库

当前旧 `db/pns-scrna.xlsx` 尚未具备 schema v2 所需列，导入器会主动拒绝写入，防止丢失 document/evidence/polarity 信息。完成干净主表重建后再运行：

```bash
python import_markers.py markers_output_v2/{document_id}_review.csv
```

### 5. HGNC 标准化（可选）

```bash
python convert_gene_symbols.py
```

## 环境变量

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `MARKER_LLM_API_KEY` | LLM API Key | - |
| `MARKER_LLM_API_BASE` | API Base URL（兼容 OpenAI 格式） | 空（使用 OpenAI 官方） |
| `MARKER_LLM_MODEL` | 模型名 | `gpt-4o` |

## evidence_type 与入库资格

| evidence_type | 含义 | candidate_class |
|---|---|---|
| `author_declared` | 作者明确称为 marker | `formal_candidate` |
| `annotation_marker` | 作者明确用于识别/注释细胞 | `formal_candidate` |
| `figure_labeled` | 图或图注明确标作 marker | `formal_candidate` |
| `supplementary_marker` | 补充材料明确列为 marker/annotation panel | `formal_candidate` |
| `cluster_enriched` | 仅富集、高表达或 DEG | `context_only` |
| `model_inferred` | 模型仅从表达图推断 | `context_only` |
| `reference_imported` | 作者引用的外部 canonical marker | `context_only` |

## review_status 流转

```
formal_candidate → pending → approved / modified / rejected
context_only     → excluded_by_rule（默认不得导入）
```
