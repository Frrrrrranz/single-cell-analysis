# Marker 基因提取管线

从 scRNA-seq 论文中提取细胞类型 marker 基因，经人工复核后结构化入库。

## 架构

```
PDF 论文 ──→ ① run_extraction.py ──→ ② gen_review_sheet.py ──→ ③ 人工复核
                (LLM 提取)              (生成复核表)              (review CSV)
                                          ↓                          ↓
                                    ③ import_markers.py ←─── approved/modified
                                        (入库)
                                          ↓
                                    ④ convert_gene_symbols.py
                                        (HGNC 标准化)
```

## 文件说明

| 文件 | 用途 |
|------|------|
| `run_extraction.py` | **主入口**。遍历 papers/ 目录下的 PDF，用 LLM 提取 marker，输出 JSON |
| `gen_review_sheet.py` | 将 LLM 输出的 JSON 转为复核 CSV（按阅读顺序排列） |
| `import_markers.py` | 将复核通过的 CSV 导入 pns-scrna.xlsx 的 markers sheet |
| `migrate_old_markers.py` | **一次性迁移**。将 cell_types 和 cell_subtypes 旧 markers 迁移到 markers sheet |
| `convert_gene_symbols.py` | **可选后处理**。用 mygene 将基因名标准化为 HGNC 符号 |
| `add_markers_sheet.py` | **一次性初始化**。创建 markers sheet 和 cell_types.mark_status 列 |
| `prompts/extract_markers.txt` | LLM 提示词模板 |
| `markers_output/` | 输出目录（JSON + 复核 CSV） |

## 完整使用流程

### 0. 初始化数据库

```bash
python add_markers_sheet.py
```

### 1. 迁移旧数据

```bash
python migrate_old_markers.py
```

### 2. 提取新论文

```bash
# 设置 LLM API
set MARKER_LLM_API_KEY=sk-your-key-here
set MARKER_LLM_MODEL=gpt-4o

# 处理单篇论文
python run_extraction.py --paper-id NATURE.587.619.2020

# 处理所有论文
python run_extraction.py --all

# 干跑预览
python run_extraction.py --dry-run
```

### 3. 生成复核表

```bash
python gen_review_sheet.py --paper-id NATURE.587.619.2020
# 或处理全部
python gen_review_sheet.py --all
```

### 4. 人工复核

用 Excel/WPS 打开 `markers_output/{paper_id}_review.csv`，逐条检查：

- [ ] 基因符号正确（对照原文/Figure 确认）
- [ ] evidence_level 判断合理
- [ ] cell_type 名称与论文一致
- [ ] 无遗漏 marker（检查 Supplementary tables、Figure legends）
- [ ] 无伪 marker（差异表达基因 ≠ marker 基因）
- [ ] source_section 可追溯回原文位置

将 review_status 改为 `approved` / `modified` / `rejected`。

### 5. 导入数据库

```bash
python import_markers.py markers_output/{paper_id}_review.csv
```

### 6. HGNC 标准化（可选）

```bash
python convert_gene_symbols.py
```

## 环境变量

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `MARKER_LLM_API_KEY` | LLM API Key | - |
| `MARKER_LLM_API_BASE` | API Base URL（兼容 OpenAI 格式） | 空（使用 OpenAI 官方） |
| `MARKER_LLM_MODEL` | 模型名 | `gpt-4o` |

## evidence_level 定义

| 等级 | 含义 | 示例 |
|------|------|------|
| **explicit** | 论文明确声明的 marker | "X is a marker for Y" |
| **implied** | 论文隐含的 marker | 热图/气泡图上选用的标志基因 |
| **inferred** | 从结果推断 | DotPlot 中明显区分细胞类型的基因 |
| **imported** | 外部导入 | 旧数据迁移 / 数据库导入 |

## review_status 流转

```
LLM 输出 → pending
         ↓ (人工复核)
  approved / modified / rejected
         ↓ (确认后)
  导入数据库 → 标记为 imported
```
