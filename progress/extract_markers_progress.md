# Marker 基因提取管线 — 完整操作步骤

## 阶段 0：论文发现与 PDF 归集（手动前置）

| 来源 | 方法 | 产出 |
|---|---|---|
| CellxGene 自动抓取 | 查询 CellxGene API，筛选外周神经相关数据集 | `db/cellxgene/cellxgene_filtered/downloads/` 下 PDF（89 篇候选） |
| PubMed / GEO 检索 | 关键词检索 + GEO 逆向搜索 | `文献_细胞类型_工具一览表.xlsx` 登记（88 篇记录） |
| 核心 9 篇文献 | 本组选定标志性论文 | PDF 以 `JOURNAL.VOL.PAGE.YEAR/JOURNAL.VOL.PAGE.YEAR.full.pdf` 结构放入 `papers/` |

---

## 阶段 1：数据库初始化（一次性）

```bash
# 在 pns-scrna.xlsx 中创建 markers sheet + cell_types.mark_status 列
python scripts/extract_markers/add_markers_sheet.py

# 迁移旧 cell_types.markers 数据到新 markers sheet
python scripts/extract_markers/migrate_old_markers.py
```

---

## 阶段 2：LLM 提取（核心）

```bash
# 设置 LLM API（从 .env 读取或环境变量）
set MARKER_LLM_API_KEY=sk-your-key-here
set MARKER_LLM_MODEL=deepseek-v4-flash

# 模式 A：处理 papers/ 下的单篇论文
python scripts/extract_markers/run_extraction.py --paper-id NATURE.587.619.2020

# 模式 B：批量处理 downloads/ 下的扁平 PDF（需要 paper_map.json 映射表）
python scripts/extract_markers/run_extraction.py --flat-pdf-dir "db/cellxgene/cellxgene_filtered/downloads" --paper-map paper_id_mapping.json

# 模式 C：干跑预览（不调用 LLM）
python scripts/extract_markers/run_extraction.py --dry-run

# 模式 D：跳过已有输出
python scripts/extract_markers/run_extraction.py --skip-existing
```

### 内部处理流程（每篇 PDF）

```
PDF 文件
   │
   ▼
① 转文本（markitdown → 回退 PyPDF2 → 回退 pdfminer）
   │
   ▼
② 按章节分块（Abstract / Results / Methods / Figure Legends...）
   过滤 References / Acknowledgments 等无用页
   单块 > 80K chars 按段落硬切
   │
   ▼
③ 每块调用 LLM（temperature=0.1, response_format=json_object）
   提示词模板: scripts/extract_markers/prompts/extract_markers.txt
   │
   ▼
④ 合并各块结果
   去重规则：同 gene + cell_type + subtype → 保留最高 evidence_level
   explicit(4) > implied(3) > inferred(2) > imported(1)
   │
   ▼
⑤ 输出 → scripts/extract_markers/markers_output/{paper_id}_raw.json
```

### evidence_level 四级标准

| 等级 | 含义 | 判断标准 |
|---|---|---|
| **explicit** | 论文明确声明 | "X is a marker for Y" / 专门的 marker 基因表 / Methods 注明 |
| **implied** | 论文隐含 | "X is specifically expressed in Y" / 热图标志基因 |
| **inferred** | 从结果推断 | DotPlot 中明显区分细胞类型的基因，但论文未明确描述 |
| **imported** | 外部导入 | 旧数据迁移 / CellMarker 等数据库导入 |

---

## 阶段 3：生成复核表

```bash
# 单篇
python scripts/extract_markers/gen_review_sheet.py --paper-id NATURE.587.619.2020

# 全部
python scripts/extract_markers/gen_review_sheet.py --all
```

输出：`markers_output/{paper_id}_review.csv`

列顺序：`cell_type | subtype | gene_symbol | evidence_level | source_section | source_context | review_status | notes`

---

## 阶段 4：人工复核

用 Excel 打开 review CSV，逐条检查：

- [ ] 基因符号正确（对照 PDF 原文/Figure 确认）
- [ ] evidence_level 判断合理
- [ ] cell_type 名称与论文一致
- [ ] 无遗漏 marker（检查 Supplementary tables、Figure legends）
- [ ] 无伪 marker（差异表达基因 ≠ marker 基因）
- [ ] source_section 可追溯回原文位置

修改 `review_status` 列：`pending` → `approved` / `modified` / `rejected`

---

## 阶段 5：入库

```bash
# 只导入 approved / modified 的行
python scripts/extract_markers/import_markers.py markers_output/{paper_id}_review.csv
```

入库逻辑：
1. 读取 review CSV（过滤 review_status=approved/modified）
2. 分配 `marker_id`（M00001 → M00002 → ...）
3. 按 `paper_id + cell_type` 匹配 `ct_id`
4. 追加写入 `pns-scrna.xlsx` → `markers` sheet
5. 更新 `cell_types.mark_status = "updated"`

---

## 阶段 6：基因名标准化（可选后处理）

```bash
python scripts/extract_markers/convert_gene_symbols.py [--dry-run]
```

功能：调用 mygene API 批量将 `original_symbol` 转为 HGNC 官方符号
- 人源：全大写（SOX10）
- 鼠源：首字母大写（Sox10）
- 无法匹配的标记为 `unverified`

本步骤可多次重复运行，只处理未标准化的记录。

---

## 数据库结构

```
papers ──→ datasets ──→ cell_types ──→ markers
  │                       │
  └──→ cell_subtypes ──→ markers (可选)
```

### markers 表核心字段

| 字段 | 说明 |
|---|---|
| marker_id | 主键 M00001 |
| ct_id | 关联 cell_types |
| subtype_id | 可选，关联 cell_subtypes |
| gene_symbol | HGNC 标准化后的符号 |
| original_symbol | 论文原文写法 |
| evidence_level | explicit / implied / inferred / imported |
| source_section | 论文中的位置（Table S2 / Fig.3A） |
| source_context | 原文上下文片段 |
| review_status | pending / approved / modified / rejected |

---

## 关键原则

1. **来源可追溯** — 每个 marker 标注 `source_section` + `source_context`
2. **原文优先** — LLM 保留原始基因名，HGNC 标准化是独立后处理步骤
3. **人工兜底** — LLM 输出必须经过逐条复核才能入库
4. **去重策略** — 同 gene + cell_type + subtype 只保留证据等级最高的记录
