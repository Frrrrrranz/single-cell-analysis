# Marker 项目最终整理计划

制定日期：2026-09-09

## 目标

在不处理 `papers_report/` 的前提下，将 Marker 项目整理为可交付、可追溯、可恢复的最终目录：

- 只保留 3 张正式表；
- 每篇 Marker 文章建立独立目录；
- 保留所有论文 PDF、对应转换 Markdown、JSON 和证据文件；
- 保留必要的全局审核裁决和最终验证记录；
- 删除重复、临时、过时和可再生内容；
- 所有删除或移动操作均有 Git 或外部备份作为恢复来源。

## 已确认决定

1. `papers_report/` 完全不处理。
2. 正式表只保留：
   - `表单/our_marker_papers.xlsx`
   - `表单/our_markers.xlsx`
   - `表单/our_markers_by_cell.xlsx`
3. `表单/our_paper_metadata.xlsx` 不进入最终交付目录。
4. PDF 由用户另行备份，不提交 Git。
5. 重要 JSON 在删除或移动前进入 Git 检查点，并生成清单供用户另行备份。
6. 文章范围以 `our_marker_papers.xlsx` 的 44 条任务清单为准，不以当前 Marker 表中的 43 个 `paper_id` 推断。

## 目标目录

```text
marker提取/
├─ README.md
├─ MARKER_POLICY.md
├─ CLEANUP_PLAN.md
├─ 表单/
│  ├─ our_marker_papers.xlsx
│  ├─ our_markers.xlsx
│  └─ our_markers_by_cell.xlsx
├─ articles/
│  └─ <paper_id>/
│     ├─ source/
│     │  ├─ paper.pdf
│     │  ├─ paper.md
│     │  └─ supplement-*.*
│     ├─ extraction/
│     │  └─ *.json
│     └─ evidence/
│        ├─ *.json
│        ├─ *.png
│        └─ 其他不可再生证据文件
├─ audit/
│  ├─ final-decisions/
│  ├─ evidence-binding/
│  ├─ validation/
│  └─ IMPORTANT_JSON_MANIFEST.md
└─ reference/
```

目录中的 `<paper_id>` 优先使用 DOI 规范化名称；无 DOI 时使用 PMID。原始文件名和来源路径记录在清单中，避免重命名后失去对应关系。

## 重要 JSON 备份范围

以下内容必须保留，并同时写入 `audit/IMPORTANT_JSON_MANIFEST.md`：

1. 每篇文章最终或最新的提取 JSON：
   - `marker_Gemini_repair/*.json`
   - 若 repair 版本不存在，则保留 `marker_Gemini/*.json` 的最新版本。
2. 每篇文章的目标级证据 JSON：
   - `marker_Gemini_evidence_v2/`
   - `marker_Gemini_evidence_v3/`
   - 其他含 source locator、原文片段、图号、页码或 marker_id 绑定的 JSON。
3. Luna 全量正确性审核核心记录：
   - `review-records.json`
   - `evidence.json`
   - `change-set.json`
   - `validation.json`
4. Astra 最终收口核心记录：
   - `final-change-set.json`
   - `final-acceptance-validation.json`
   - `final-workbook-build-validation.json`
   - `decisions-*.json`
   - `deferred-*.json`
   - `review-221-summary.json`
   - `remaining-221-worklist.json`
5. 跨文章映射、合并、排除或恢复关系中仍能解释最终表来源的 JSON。

纯缓存、重复 inspect 输出和可由上述核心记录重新生成的中间 JSON，在完成哈希及内容等价核对后才可删除。

## 执行阶段

### 阶段 1：只读盘点

- 从 `our_marker_papers.xlsx` 读取 44 篇文章的 canonical ID、标题和数据集编号。
- 建立 PDF、Markdown、提取 JSON、证据 JSON、证据图片的对应关系。
- 输出文件清单、孤儿文件清单、重复文件清单和缺配对清单。
- 对同名或疑似重复文件计算 SHA-256；不凭文件名直接删除。

验收条件：44 篇文章都有明确目录归属，无法归属的文件进入人工复核清单。

### 阶段 2：整理前安全检查点

- 检查工作区是否存在未跟踪的重要 MD、JSON 和证据图片。
- 将重要 JSON、证据和转换 Markdown 提交到 `feat/0909`。
- 不提交 `.env`、PDF、临时渲染图、缓存和 Office 临时文件。
- 记录检查点 commit，并在开始移动前确认 `git status`。

验收条件：除有外部备份的 PDF 外，所有待移动或待删除的重要文件都有 Git 恢复路径。

### 阶段 3：建立文章目录并移动资料

- 创建 `articles/<paper_id>/source|extraction|evidence`。
- 将 PDF 和对应 Markdown 移入 `source/`。
- 将单篇文章 JSON 移入 `extraction/` 或 `evidence/`。
- 将证据图片、补充表转换结果及不可再生证据移入 `evidence/`。
- 对跨文章文件不强行拆分，统一移入 `audit/`。

验收条件：每篇文章至少具备 PDF/MD 配对状态说明；所有保留 JSON 和证据均有唯一去向。

### 阶段 4：整理正式表和审核资产

- 将最终发布版本覆盖到 `表单/` 的 3 张正式表中。
- 核对三张表的文件哈希、工作表名称、记录数和 Marker 总数。
- 将最终裁决、证据绑定和验证 JSON 集中到 `audit/`。
- 更新 `marker提取/README.md` 和 `表单/README.md`，只描述最终流程和目录。

验收条件：正式表不存在多个“final/staged/reviewing”副本；README 不再引用旧流水线。

### 阶段 5：删除无用和过时内容

优先删除以下明确可再生或已失效内容：

- 根目录和临时目录中的裁图、页面预览和 PDF 渲染 PNG；
- `*.inspect.ndjson`、`__pycache__/`、`*.pyc`；
- 已被最终表替代的 baseline、staged、reviewing 工作簿副本；
- 一次性批处理脚本、旧模型任务提示、旧计划、旧 handoff 和已被最终裁决覆盖的过程报告；
- 内容哈希完全相同且已有唯一保留副本的重复文件；
- 空目录。

以下内容不得自动删除：

- 无法确认是否重复的 PDF、Markdown、JSON 或证据；
- 仍能解释 Marker 纳入、纠正、剔除或待议原因的唯一记录；
- `reference/` 中导师资料；
- `papers_report/` 中任何内容。

验收条件：删除清单逐项包含原路径、理由和恢复来源。

### 阶段 6：最终验证与提交

- 验证 44 篇文章目录与任务表一一对应。
- 验证所有保留 PDF 与 Markdown 的配对情况。
- 验证所有 JSON 可解析，证据文件可读取。
- 验证 3 张正式表可打开，Marker 总数和按细胞汇总一致。
- 扫描残留的 `final`、`staged`、`reviewing`、`temp`、`old`、`backup` 等歧义副本。
- 提交目录整理结果并推送 `feat/0909`。

## 每阶段输出

- `file-inventory.json`：整理前后文件清单及 SHA-256。
- `IMPORTANT_JSON_MANIFEST.md`：用户应另行备份的重要 JSON。
- `move-map.json`：每个文件的原路径和新路径。
- `deletion-manifest.json`：删除理由及 Git/外部备份恢复方式。
- 最终 `git status`、验证摘要和提交号。

## 当前状态

- [x] 确认最终保留 3 张表。
- [x] 确认 PDF 使用用户外部备份。
- [x] 为未跟踪旧计划建立 Git 安全检查点：`900ab1fb`。
- [x] 建立本整理计划。
- [x] 阶段 1：只读盘点。
- [x] 阶段 2：完整整理前安全检查点。
- [ ] 阶段 3：按文章重组。
- [ ] 阶段 4：正式表和审核资产收口。
- [ ] 阶段 5：删除无用和过时内容。
- [ ] 阶段 6：最终验证、提交和推送。

### 阶段 1 盘点结果（2026-09-14）

- 已生成 `audit/file-inventory.json`。范围包括 `pdf/`、`review_md/`、`marker_Gemini/`、`marker_Gemini_repair/`、`marker_Gemini_evidence_v2/` 和 `marker_Gemini_evidence_v3/`；不包含 `papers_report/`、`reference/` 或正式表以外的工作簿。
- 任务表包含 44 篇论文；盘点了 420 个候选保留资产（44 PDF、79 Markdown、239 JSON、58 图片）。
- 42 篇论文至少有一个已关联资产。`TITLE_single_cell_atlas_of_the_human_optic_nerve` 和 `TITLE_bronchopulmonary_dysplasia` 均在任务表中标记为“缺少有效 PDF”，当前没有可关联资产。
- 42 篇已有资产论文的 PDF 与 Markdown 数量一致。PDF 按任务表的原始 PDF 文件名关联，其他资产按 `paper_id` 路径或文件名关联。
- 发现 10 个内容哈希完全相同的重复组，其中 8 个为 v2/v3 证据图片重复，另 2 个为历史审核截图或 manifest 重复；仅记录，尚未删除。
- 有 201 个未能从路径或文件名直接关联到论文的文件（131 JSON、37 Markdown、31 图片、2 PDF）。它们保留在 `orphan_files`，将在阶段 3 前按内容与审核语义人工归属。

### 阶段 2 安全检查点（2026-09-14）

- `audit/IMPORTANT_JSON_MANIFEST.md` 已记录 239 个候选保留 JSON 的路径、大小和 SHA-256。
- 检查点暂存范围为 270 个 JSON、Markdown、PNG/JPEG 证据文件、盘点报告和本计划更新；不包含 PDF、XLSX、Python/MJS 脚本、缓存或 `.claude/`。
- 提交完成后，提交号即为上述资产的 Git 恢复来源；PDF 仍仅依赖用户约定的外部备份。
