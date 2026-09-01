# Marker 提取唯一有效口径

生效日期：2026-09-01  
确认人：项目导师  
最终决定：**全部有可靠论文证据的 Marker 都要保留。**

本文件是当前 Marker 提取、复核和入库的唯一范围约束。若旧提示词、审计记录、脚本注释或历史结果与本文件冲突，以本文件为准。

## 1. 提取范围

- 逐篇阅读论文，提取论文中所有细胞类型的 Marker，不因细胞是否属于 PNS、L1-L4、任务表登记层级、任务表物种或组织而删除真实 Marker。
- L1-L4 是数据集的四层分类标签，不是单篇论文的排他性提取范围：
  - L1：真正神经元；
  - L2：神经胶质；
  - L3：神经相关基质；
  - L4：神经内分泌。
- 一篇论文可以同时贡献多个层级的 Marker。
- 物种、组织、疾病、四层分类和是否 PNS 只用于标注、检索与后续导出筛选，不控制 Marker 是否保留。

## 2. 正式 Marker 的证据要求

以下证据可作为正式 Marker：

- `author_declared`：作者明确建立 gene–cell Marker 关系；
- `annotation_marker`：作者实际用该基因识别、注释、命名、分选、门控或验证细胞；
- `figure_labeled`：图或图注明确给出可读的 gene–cell 对应关系；
- `supplementary_marker`：补充材料明确列为 Marker 或细胞注释基因。

以下只保留为上下文候选，不进入正式 Marker 总表：

- `cluster_enriched`：仅为 DEG、富集、上调、高表达或 top genes，未用于定义/注释细胞；
- `model_inferred`：仅根据表达图形推断；
- `reference_imported`：只来自外部文献或领域常识，本文未实际使用。

如果已知/经典 Marker 在本文中被实际用于识别、注释或验证细胞，应记为 `annotation_marker`。

## 3. 决策含义

- `include`：论文证据正式、gene–cell 关系可回溯、基因符号可唯一解析、物种可确定；无论细胞属于哪一层都保留。
- `context_only`：证据仅达到 DEG/富集/模型推断/纯外部引用。
- `exclude`：候选并非 Marker、原文不存在、gene–cell 对应错误、重复污染或不是可识别的基因实体。不得因为不属于四层分类或不匹配任务表登记物种而 `exclude`。
- `unresolved`：图表不可读、基因符号不唯一、物种无法确定或证据无法可靠回溯；保留待人工处理，不物理删除。

## 4. 证据与字段要求

- 不得用领域常识补写论文没有出现的 Marker。
- `source_locator` 和 `source_context` 必须能回到正文、图注或补充材料。
- 保留原文基因写法，并另存标准符号；无法唯一标准化时保留为 `unresolved`。
- 跨物种证据按物种拆分记录，但不同于任务表登记物种的 Marker 仍然保留。
- 四层分类建议使用 `four_layer_category=L1/L2/L3/L4/outside/unknown`；历史字段 `target_cell_scope` 和 `in_project_scope` 已弃用，不得再作为纳入门槛。

## 5. 历史结果状态

- 当前 87 条正式 Marker 是旧版 `target_cell_scope` 严格筛选后的结果，不代表 40 篇论文的全部正式 Marker。
- `audited-extraction/` 中旧 `exclude` 记录必须在补充阶段重新判断：若唯一排除理由是细胞层级、PNS 范围或任务物种不匹配，应恢复为 `include`，前提是其他正式证据门槛通过。
- 旧版原始提取和终审结果已从 Git 提交 `85b4727` 恢复到 `.archive/marker-extraction-85b4727/`，仅供对照，不作为当前有效约束。
