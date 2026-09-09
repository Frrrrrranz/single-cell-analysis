# Luna 现有 Marker 正确性轮独立验收

审核日期：2026-09-08  
审核对象：`20260907-luna-existing-marker-correctness`  
审核者：GPT-6 Astra

## 结论

**暂不通过，不得发布两份暂存工作簿。**

Luna 已把 `2502/2502` 个审核单位的状态写成 completed，且已知纠正包基本正确落入暂存主表；但至少有一组 `204` 条记录仍由脚本仅凭既有 `source_context` 和基因/别名词项机械判为 `verified_keep`，没有重新绑定原始来源文件。另有 `445` 条明确继承历史快速一致性裁决，其中 `353` 条集中在两篇本地缺少决定性补充图/图表的预印本。当前 `pending=0` 不能作为证据审核完成的依据。

工作簿交付也仍有阻断缺陷：按细胞汇总的“Marker总数”保留旧值 `2488`，与该表“数据来源”和暂存主表的 `2490` 不一致；相对 2026-09-06 发布前汇总基线，仍少恢复 `759` 个谱系/组织字段。

## 独立抽查范围

- 全量检查 `2502` 条记录的处理状态、evidence binding 分类、来源文件存在性、原上下文回溯性及目标基因/细胞词项定位。
- 建立 `249` 条不重复独立验收样本，覆盖全部 `43` 篇论文：
  - `34` 条 evidence binding 为空的记录全部纳入；
  - `129` 条历史快速裁决分层样本，覆盖其全部 `28` 篇来源论文、全部非 positive 和非 human 风险项；
  - `86` 条其余 target-bound no_change 跨论文样本，每篇最多两/风险优先抽取。
- 对全部 `33` 个 update/restore 动作做字段级基线—暂存比较；重新查看 RIMS2/LAMC3 Fig.1D、PRR4 Extended Data Fig.10g、iPain Fig.2 与 Fig.3，并复核 low/negative 的目标级文本片段。
- 用 Artifact Tool 独立导入两份暂存工作簿，检查表结构、关键区域、公式错误并渲染主表、归档和按细胞汇总；另用只读 openpyxl 重新计算 ID、字段差异、归档字段及历史元数据保留量。

抽样是风险分层验收，不用于估算全表“准确率”。机械定位失败只表示证据尚不能从当前材料独立回溯，不等同于 marker 关系错误。

## 通过的部分

### 已知纠正包

- 暂存主表从 `2488` 增至 `2490`，只恢复 `M00417`、`M01510`，没有删除 ID。
- 共同 ID 中实际有 `29` 个发生字段变化，均属于计划更新范围；未发现越界修改的 marker ID。
- `M02590`、`M02591` 的 update 仅修复台账证据/decision 链，因此主表无字段差异，属于预期情况。
- `M00044`、`M00398`、`M00403` 的 `negative → low`，`M00415` 的正文 CA4 `positive → low`，以及独立恢复 HCR positive 的 `M00417`，与原文/图注一致。
- `M00071` 已恢复为 CCI 损伤背景下的 senescent nociceptor 子集，没有继续泛化为所有 neurons；iPain Fig.3i 显示 SA-β-Gal 与 NeuN 共染。
- `M01510` 的 SST 亚型恢复成立；iPain Fig.2a/f/g 实际使用 SST 作为分群和分析标签。
- RIMS2—PNEC、LAMC3—Pericytes 和 PRR4—SMG-serous 的实图关系成立；LAMC3 的历史申报文案已清理。
- 归档页包含全部 31 个源字段及 11 个审核字段，共 42 列、3164 条数据；证据引用与 change ID 的机械完整性通过。

### 工作簿机械检查

- 暂存主表 `2490` 个唯一 active ID、43 篇论文；没有发现公式错误。
- 按细胞汇总 `1059` 条 Marker 数据、`620` 条图表索引数据；没有发现公式错误。
- 两份暂存文件 SHA-256 与 Luna 的 validation 记录一致。

## 阻断发现

### 1. 204 条记录仍是 source_context 机械通过

`context_backed_review_batch_20260908.py` 的判定条件是目标基因或别名出现在旧 `source_context`，再用正负关键词检查极性。它没有读取原论文文件，却把匹配记录直接改为 `completed / verified_keep / no_change`。

这 `204` 条记录使用 34 个共享 evidence group；34 个 evidence group 的 `source_file` 和 `source_sha256` 均为空。该方法违反本轮方案中“脚本不得根据关键词命中或旧 supported 生成生物学通过结论”的要求。受影响的 204 条必须整体退回待核，不能仅抽样放行。

抽查还发现，抗体 panel 列表被直接转成了宽泛 gene–cell 关系。例如 `M00157` 把 CD123/IL3RA 归给“basophils, neutrophils and eosinophils”，`M00209/M00210` 把 CD123/CD11c 归给合并的 “pDCs, mDCs, CD16+ DCs”，`M00223` 把 CD62L/SELL 归给所有 T cells。原文只说明这些抗体共同属于相应 sorting panel，不能据此证明每个抗体对该合并类别中的每一种细胞均构成正式 marker。至少这些记录需重新核对真实 gating 定义或转为 unresolved/context_only。

### 2. 445 条历史继承记录尚不足以通过 Astra 抽查

分层抽取 129 条：61 条的目标基因不出现在当前本地 Markdown，116 条的记录 source_context 无法在 Markdown 中规范化回溯。这里包含 OCR、图像和补充材料缺失，不能直接判错；但也不能独立确认。

其中两篇预印本占继承池 `353/445`：

- `DOI_10.1101_2025.01.17.633590`：238 条；抽取 25 条，22 条目标基因不在本地 Markdown，主要声称来自 Supplementary Fig.2、Fig.4c、Supplementary Fig.8e/9e。
- `DOI_10.1101_2025.09.26.678707`：115 条；抽取 25 条，14 条目标基因不在本地 Markdown，主要声称来自 Fig.2b/2h、Extended Data Fig.6f。

本地材料只有正文/图注或上游 JSON，没有决定性图表资产。应取得原图/补表后核验；在此之前这些图表型关系不能由历史 quick consistency 自动升级为完成。

### 3. 汇总表仍有 759 个历史字段未恢复

相对 `luna-single-model/baseline/20260906-luna-single-model/our_markers_by_cell.xlsx`：

| 区域 | 历史非空 | 当前暂存非空 | 仍缺失 |
|---|---:|---:|---:|
| Marker表 C 谱系 | 39 | 5 | 34 |
| Marker表 D 组织/区域 | 988 | 887 | 101 |
| 图表索引 C 谱系 | 33 | 0 | 33 |
| 图表索引 D 组织/区域 | 591 | 0 | 591 |
| 合计 | 1651 | 892 | 759 |

Luna 的 validation 只突出“130 行无法唯一匹配”，没有明确说明图表索引的 624 个历史非空字段仍全部为空，因此不足以支持“汇总字段已恢复”的交付表述。

### 4. 汇总统计自相矛盾

按细胞汇总“说明”页同时写：

- 数据来源：2490 条；
- Marker总数：2488。

主表实际为 2490，因此 Marker总数是未更新的旧值。正式发布前必须重新生成并独立对账。

## 返修要求

1. 将 `context_backed_target_marker_review` 的 204 条整体退回 pending，逐证据组打开实际正文、图注、图或补表；抗体 panel 不得自动外推到每个合并细胞类别。
2. 对 445 条历史继承记录至少完成原图/补表可回溯抽查。优先处理两篇预印本的 353 条；拿不到决定性材料的记录改为 unresolved，而不是 completed。
3. 恢复汇总表剩余 759 个历史谱系/组织字段。语义键不唯一时建立显式映射或保留独立 mapping unresolved 清单；不得整列置空。
4. 将“说明”页 Marker总数更新为 2490，并从暂存主表重新推导所有统计。
5. 返修后重新提交：受影响 ID 清单、证据文件与 SHA、精确 change-set、两份新暂存表及独立验证结果。正式表保持不动，直到 Astra 复验通过。

## 附件

- `triage.json`：249 条抽样清单、全量来源机械检查及独立最佳窗口。
- `workbook-data-audit.json`：基线—暂存字段差异、归档列、汇总行数和历史字段保留量。
- `workbook-audit.json`：Artifact Tool 独立导入及公式错误检查。
- `staged-main-preview.png`、`staged-archive-preview.png`、`staged-by-cell-preview.png`：独立渲染结果。

