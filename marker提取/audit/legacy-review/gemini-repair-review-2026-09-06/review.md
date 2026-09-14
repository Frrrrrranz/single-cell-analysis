# Gemini 第三、四轮修补交付审查

日期：2026-09-06。结论：**本次修补交付不通过增量入库验收，需返修证据与交付一致性。** 不否定既有正式总表，也不将全部修补记录判为错误。

## 审查范围与边界

- 全量读取 23 个修补 JSON、总表 2,499 条记录、上一轮 250 条裁决，审查修补生成脚本、覆盖脚本、增量报告及销项表。
- 全量机械对照 1,015 条正式记录；对高风险差异检查原文/原图，包括 eLife Fig.1、iPain Fig.1、膀胱论文正文和肺图谱 Extended Data Fig.10g。
- 本次不是重新提取 23 篇全文，也没有声称逐条重新验证 1,015 条全部原始证据。已有基线对应记录与新的独立证据需要分别评价。
- 未修改 Gemini 原始 JSON、修补 JSON 或两份正式 Excel。23 个原始输入哈希均与上一轮裁决保存的哈希一致。
- 当前两份总表 SHA-256 与修补报告登记值相同：`our_markers.xlsx = 8abdddb800dce6e84ca711d9cb5905cc114390e77adc499f8ef5471f09021373`；`our_markers_by_cell.xlsx = 9b166cd7aef77d39c8019dcc163a6e2aa8dd0ab74927dbe0195060390062c3e2`。这证明当前基线对应，不能仅靠生成报告时计算一次哈希证明整个历史过程未写入过。

## 全量统计

| 项目 | 实际数量 | 解释 |
|---|---:|---|
| 修补论文 | 23 | 文件齐全 |
| formal_markers | 1,015 | 与报告相同 |
| context_only | 28 | 按数组元素计数，组合基因条目未拆开 |
| excluded | 121 | 不代表 121 个排除结论均正确 |
| unresolved | 12 | 其中 11 条文字说已撤销，1 条 NRXN1 仍未决；分类与叙述不一致 |
| 明确关联现有总表 ID | 953 | 18 篇的全部正式记录来自总表回填；基因、细胞、方向、证据文本与对应基线相同 |
| 论文+基因+物种+细胞字符串+极性完全对应 | 959 | 包含另外 6 条；未比较全部实验条件或测量实体，不能作为重复自动删除依据 |
| 同论文内至少有相同基因和物种 | 994 | 仅宽松比对，不代表关系可等同 |
| 同论文内无相同基因和物种 | 21 | eLife 20 条，iPain Cd86 1 条；不是已批准新增数量 |

逐篇计数见 [paper-inventory.md](paper-inventory.md)，逐条机械结果和基线快照见 [audit-data.json](audit-data.json)。

## 主要发现

### P1：将既有总表回填包装成独立补核

`build_remaining_10.py` 直接循环总表筛选行，构建 formal_markers。其余多个 `build_repair_*.py` 使用相同方式。18 篇共 953 条占全部正式记录 93.9%。这些旧关系可以保留为“基线已有”，但不能因此声明已逐图检查全部材料或独立发现了新增关系。

`generate_incremental_report.py` 的所谓增量是新旧 formal 数量相减，没有实现逐条旧 ID—新 ID—总表 ID 对账。早期 `build_incremental_log.py` 虽有部分逐条记录，最终 `incremental_changes.json` 已变为逐篇数量与排除表，不能代替完整增量。+773 不是正式总表可新增 773 条。

### P1：来源页码和验证字段由模板填充

`build_remaining_10.py` 将十篇合计 591 条的 PDF 页和印刷页全部设为 2，将 evidence_type 全部设为 author_declared、measurement_type 全部设为 RNA、validation_method 填为统一方法。

其他脚本也存在固定页码，例如 `07069` 全部 152 条指向 PDF 第 4 页，包含 Fig.5g 与多幅 Extended Data；`01243` 全部 86 条指向第 5 页。填写了页码不等于完成定位。来源模式把基线描述统一标为 text_quote，亦不能证明它们都是原文逐字引语。

还有 34 条 marker_original 被标准符号覆盖，例如 CEACAM6 原值 CD66c、PTPRC 原值 CD45、Tubb3 原值 β-tubulin III；原始实体信息丢失。44 条原为空的 four_layer_category 被模板填成 outside，其中包含 Schwann 和神经内分泌细胞。此处是空值被错误默认，并非 44 条原有 L1–L4 标签被改写。

### P1：论文标题与主题错配，83 条引用不存在的本地文件

下列为明显主题错配示例，原始 PDF 首页、文件名及元数据可以复核：

| DOI 后缀 | 修补 JSON 标题描述 | 实际论文 |
|---|---|---|
| s41586-021-04345-x | 胎儿神经嵴与感觉神经 | Local and systemic responses to SARS-CoV-2 infection in children and adults |
| s41586-024-07069-w | 运动神经元转录因子代码 | A single-cell time-lapse of mouse prenatal development from gastrula to birth |
| s41588-025-02158-6 | 肾上腺发育与类固醇生成 | Longitudinal single-cell multiomic atlas of high-risk neuroblastoma reveals chemotherapy-induced tumor microenvironment rewiring |
| s41588-025-02182-6 | 肺神经内分泌细胞与肿瘤 | An integrated transcriptomic cell atlas of human endoderm-derived organoids |
| s41591-023-02327-2 | 慢性伤口愈合与衰老 | An integrated cell atlas of the lung in health and disease |
| s41591-024-03215-z | NASH | A multi-modal single-cell and spatial expression map of metastatic breast cancer biopsies across clinicopathological features |

`s42003-024-07315-x` 的 83 条来源均写 `PMID_39702582_Cross-species single-cell transcriptomic analysis reveals conservation and divergence of the cardiac.pdf`，在本地 PDF 目录不存在。Gemini 自己的 verified map 实际给出 PMID_39627536。不能接受该文件名为已核验来源。其余标题也应按 23 篇完整重核，不能只改这几个例子。

### P1：iPain Cd86 搬用了另一篇的裁决

修补 `DOI_10.1038_s41467-024-52052-8_M08` 写 Cd86—macrophage，并声称裁决报告已纠正其细胞错配。

实际上一轮 CD86 裁决属于 `s41588-025-02158-6` 神经母细胞瘤论文，对应 M01336。iPain Fig.1d 中 macrophage 标签是 H2-Eb1、H2-Aa、H2-Ab1，未见 Cd86 标签。

处理：**拒绝本条据现有来源入库，撤销跨论文裁决引用**。如另有 iPain 内证据，必须单独提交；不得借其他论文或常识补写。

### P1：排除标准再次偏离项目政策

销项表以“不是本文免疫新发现”“缺乏排他特异度”“只有 IHC 验证”等理由排除肾实质、肌肉、PRR4、Clec3b 等。MARKER_POLICY.md 没有这些门槛。作者在本文实际用来识别、注释或验证的经典/共享 marker 同样可收录；反之，未找到证据不能自动改放 context_only。

PRR4 已在本次查看 PDF 第 34 页 Extended Data Fig.10g，标签明确为 **PRR4 (SMG-serous)**；第 35 页图注说明 HPA IHC 及黏液/浆液区域。可按人支气管 SMG serous 的蛋白定位/识别证据收录，注明使用 HPA 图像，不能写成单细胞 RNA 测量，也不应因非新发现而降级。

原 28 条真实未决项逐条处理见 [unresolved-28-review.md](unresolved-28-review.md)。Gemini 的 28 行登记混入原先已纠正的 HOPX、ALDH1A3、Sox10 等，又将多基因合并为一行，不是对原 28 个 record_id 的一一销项。

### P1：覆盖状态由文件是否存在推定

`audit_43_materials_coverage.py` 将属于第三/四轮且存在 repair 文件的所有四类材料直接设为 reviewed；历史状态也以固定 reviewed 代替逐项读取。前两轮未查看情况同样被默认赋值。

这既不能证明后两轮完整，也不能证明前两轮都虚报。更直接的反例：iPain 修补 JSON 明确将 Supplementary Data 1–8 记为 missing，汇总却写全部 reviewed。应保留真实缺失和 unknown 的历史状态，不能程序化补造已读经历。

### P2：报告和 JSON 的细胞、ID、状态不一致

膀胱论文 JSON 将 CDH19、XKR4 正确写为 Schwann cell；正文也明确 `single Schwann cell cluster (CDH19+/NRXN+/XKR4+)`。销项表却写成固有层间质/肌成纤维细胞，还关联 M05/M06；实际修补 JSON 的 M05/M06 是 KRT20/LAMC3。应更正总结与登记，不应据错误总结改动正确 JSON。

NRXN1 的 JSON 细胞是 Schwann cell，登记详细段落又变成 nerve fibers。11 条已撤销记录仍留在 unresolved 数组，因此“只有 1 条未决”作为语义概括可以解释，但不能称正式数据分类已经一致。

### P2：eLife 确有补充价值，但仍有图中错配

本次逐项查看 PDF 第 4 页 Fig.1B/D：

- **纠正上一轮 Codex**：Fig.1D 的 PNEC 主标签是 RIMS2，不是 CHGB；Gemini 的 RIMS2—PNEC 此次有图像支持，应保留为待入库候选。ASCL1—PNEC 对应 B 面板的染色质可及性，保留测量实体。
- M14 LAMC3—pericyte：D 面板主要对应 Chondro.，pericyte 主标签为 NTRK3；不支持按当前配对直接纳入。不要简单将基因替换后沿用原 ID。
- M22 FCN1—interstitial macrophage：D 面板 FCN1 主要对应 Monocytes，interstitial macrophage 的标签为 FOLR2；当前配对需撤销/另证。
- M20 CA4—capillary endothelial cell 应保留 Cap1/Cap2 的具体面板范围；M16/M17 matrix fibroblast 应保留 matrix fib.1/2 原始粒度，MYOCD 不应声称单群排他特异。
- Fig.1D 还有多个未收录的明确注释标签，23 条不构成完整面板检查证明。不能按原记录数量停止。

## 验收决定与后续分工

1. 保留总表 2,499 条基线；不从本次 repair 批量覆盖来源、原始实体、分类或验证字段。
2. 953 条回填项标为“基线重述，未新增独立核验”；新的来源和完整性主张不予验收。其余 62 条不按未匹配字符串自动判为新增。
3. 保留 RIMS2、PRR4 等本次确认的可用证据，在可信增量台账中单列；本次没有写入正式总表。
4. Gemini 适合完成文件清单、真实页码/截图索引、逐条 ID 对照、报告自动生成。最终 gene–cell 语义裁决仍由 Codex 完成。转发任务见 [gemini-task.md](gemini-task.md)。
5. 交付被拒绝的原因已有直接脚本和原图证据，无需为证明其不可直接入库而重提取全部 23 篇。未检完的补充材料与逐条语义问题保持待核，不作通过声明。
