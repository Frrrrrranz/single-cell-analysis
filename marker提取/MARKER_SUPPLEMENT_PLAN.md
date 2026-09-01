# Marker 全量补充方案

## 目标

按 2026-09-01 最终口径重建结果：凡论文把某基因明确作为某细胞类型或亚群的 Marker，均保留。L1-L4、物种、组织和是否属于 PNS 仅作为分类字段，不作为删除条件。

## 输入基线

- 当前 `review_md/` 中已转换的全部文章 Markdown，包括新补入的 3 篇。
- `.archive/marker-extraction-85b4727/` 中旧版逐篇原始提取、逐篇审核和旧总表，仅用于找回历史候选及比较差异。
- 当前 `audited-extraction/markers/` 与 `db/cellxgene/our_markers.xlsx` 作为“旧严格筛选版”基线；87 条不是新口径最终数目。

旧 40 篇终审 JSON 的初步盘点：共有 1848 条审计记录，其中 88 条逐篇 `include`（去重入表后为 87 条），1752 条 `exclude`、5 条 `unresolved`、3 条 `context_only`。在非 `include` 记录中，有 1117 条同时满足“旧 `in_project_scope=false`、正式证据类型、符号 exact/alias_resolved、引用已核验”，分布于 35 篇论文。这 1117 条是高优先级复核池，不等于可无条件写回的最终数量：仍须逐条确认旧排除理由是否只有范围/物种门槛。

## 执行顺序

### 1. 找回被范围规则淘汰的候选

逐篇比较旧原始提取与旧终审 JSON，列出因下列原因被排除或降级的记录：

- 细胞不属于任务目标层级；
- `in_project_scope=false`；
- 物种与任务物种不同；
- 不属于 PNS；
- 普通上皮、免疫、内皮、成纤维等“非目标细胞”。

这一步只建立补充候选池，不凭旧决定直接写入正式总表。

### 2. 自动恢复证据已经充分的 Marker

同时满足以下条件者可自动恢复为 `include`：

- 证据类型是 `author_declared`、`annotation_marker`、`figure_labeled` 或 `supplementary_marker`；
- 原文引用能够核对；
- 基因符号为 `exact` 或 `alias_resolved`；
- 唯一排除原因是旧范围、层级、物种或 PNS 门槛。

恢复时新增 `four_layer_category`、`species`、`tissue` 等分类字段，不再写入控制纳入的范围布尔值。

### 3. 对全部文章重新全量扫描

使用 `prompts/audit_markers_v2.md` 对每篇 Markdown 扫描所有细胞类型，既复核旧候选，也主动寻找旧流程没送审的 Marker。DEG、表达基因和聚类富集基因若没有作者的 Marker 语义，只记为 `context_only`，不冒充正式 Marker。

### 4. 人工补看图表和补充材料

对 `unresolved`、图中文字无法读取、正文只写“见图/补充表”的项目回到 PDF 核验。需要确认具体的 gene–cell 对应关系；只有同图共现但映射不可读时继续保留为 `unresolved`，不能靠领域常识补证据。

### 5. 重建总表并保留审计轨迹

输出至少包含：

- `markers`：所有核实后的正式 Marker；
- `context_only`：DEG、富集、表达等非正式 Marker 证据；
- `unresolved`：证据存在但尚不能唯一判定者；
- `audit_exclusions`：仅保留真正的误提、非基因实体、引用不成立等排除原因；
- `audit_summary`：逐篇新旧数量与变更原因。

## 验收条件

1. 新结果不得丢失旧版任何仍有有效正式证据的 `include`。
2. 不得存在“仅因层级、组织、物种、是否 PNS 而 exclude”的记录。
3. 每条 `include` 均能回到论文中的 Marker 语义及具体引用位置。
4. 四层表只影响 `four_layer_category`，不影响 `decision`。
5. 新补入的 3 篇与原 40 篇使用同一规则完成审计。
6. 生成逐篇新旧差异表，供人工抽查恢复项和新增项。
