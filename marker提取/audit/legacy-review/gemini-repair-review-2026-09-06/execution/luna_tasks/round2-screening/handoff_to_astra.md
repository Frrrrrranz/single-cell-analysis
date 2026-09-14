# Luna → Astra：Marker 总表第二轮独立复筛交接

> 本文件全部为 Luna建议，不是 Astra 最终裁决，也未修改正式工作簿。模型：GPT-5.6 Luna；思考档位：max。

## 1. 基线与范围

- 当前正式 `our_markers.xlsx`：8abdddb800dce6e84ca711d9cb5905cc114390e77adc499f8ef5471f09021373；markers 数据行 2499，唯一 marker_id 2499。
- 当前正式 `our_markers_by_cell.xlsx`：9b166cd7aef77d39c8019dcc163a6e2aa8dd0ab74927dbe0195060390062c3e2。
- 本轮覆盖 Gemini 首轮全部 490 个首轮审查单元：Batch-01 213，Batch-02 277。这不是 2499 条总表全量复筛；当前首轮只覆盖 473 个基线 ID。
- 论文分布：DOI_10.1016_j.cell.2022.11.005=207, DOI_10.1016_j.isci.2024.111628=81, DOI_10.1016_j.stem.2022.11.013=70, DOI_10.1038_s41467-024-52052-8=15, DOI_10.1038_s41588-022-01243-4=87, DOI_10.1126_science.aat5031=22, DOI_10.7554_elife.62522=8
- Batch-02 声明的旧哈希与当前正式表不一致，但其 277 个稳定 ID 均能在当前正式表找到；未恢复旧表，以当前正式表行值为准。

## 2. 建议优先裁决的拟议变更

共 20 项，均标为 Luna建议，预计由 Astra 逐项批准/拒绝：

- M00071：建议更新 cell_type 为 `nociceptors/neurons`，保留衰老实验上下文；NeuN/RBFOX3 不应写成衰老特异 marker。证据：Batch-01 EVID02 及 `marker提取/review_md/DOI_10.1038_s41467-024-52052-8.md` 的 Results/Fig.3i 定位。
- M01510：建议从正式 marker 语义移到 `context_only`，不物理删除；当前引文仅为引言分类。
- REV_SMG_01_PRR4、REV_ELIFE_01_RIMS2：建议作为候选新增，但必须由 Astra 分配正式 ID；PRR4 是 HPA IHC/蛋白证据，RIMS2 是 PNEC 图示证据，不改写为未经证实的 RNA-only。
- Batch-02 16 项明确去重建议：M00041→M00036、M00042→M00034、M00043→M00035、M00047→M00036、M00048→M00038、M00050→M00039、M00417→M00415、M00418→M00416、M00456→M00455、M00466→M00460、M00467→M00462、M00494→M00491、M00531→M00530、M00554→M00553、M00592→M00585、M00597→M00594。去重必须保留源记录溯源，不能由 Luna 物理删除。

## 3. 两轮分歧与高风险

- M00074 Prph：Gemini 建议与 M00073 合并；Luna建议暂不合并，因为 `neurons` 与 `small-diameter peripherin-positive neurons` 粒度和实验定位不同。
- M00051 ASCL1：Gemini 的模态更新方向可理解，但正式表没有 measurement_type 独立列且现有 notes 已说明 Fig.1B/1D 双模态；Luna建议不做字段更新。
- Batch-02 原 11 条 exclude：EPCAM、SFTPC（Fetal AT1 阴性）以及 APOA1、APOA2、ACTN2、MYH6、GSTA3、PAGE4、SOX2、TP63、TRH。Luna建议保留，因为作者确实使用它们作注释/门控/阴性识别；不能因污染、非目标组织或阴性方向删除。
- Batch-02 原 44 条 context_only：Luna逐条按 negative/low/组合门控及作者 subtype 定义复核，建议保留为 formal include/no_change，而不是仅凭非特异或负方向降级。
- Batch-02 首轮 merge_duplicate 中 18 条没有被确认可合并（例如 PDGFRA/CD141 门控、NOTUM/ WNT2 亚群、proximal basal 与 basal、myofibroblast 子群等）；它们被列为 no_change，待 Astra 抽查。

## 4. 未决与停止条件

- Luna建议 unresolved + hold：REV_ELIFE_02_CALCA, REV_ELIFE_03_CHGA, REV_IPAIN_03_Calca, REV_IPAIN_04_Mrgprd, REV_IPAIN_05_Piezo2, REV_IPAIN_06_Fabp7, REV_BLADDER_01_NRXN1, REV_KIDNEY_01_SLC12A1, REV_KIDNEY_02_AQP2, REV_KIDNEY_03_SLC12A3, REV_KIDNEY_04_NPHS2。这些条目已检查首轮指定图/图注、原引文和本地论文 Markdown 定位，但缺少能稳定绑定申报关系的直接证据；没有把面板未出现当成全文否定。
- 候选 exclude + hold：REV_ELIFE_04_LAMC3, REV_ELIFE_05_FCN1, REV_IPAIN_01_Cd86, REV_IPAIN_02_Glb1。这些是明确错误实体/用途的候选，不进入正式表，但保留候选审计。
- 停止原因统一记录在 `screening_round2.json`：已完成可定位材料的定向检查，剩余缺口需要指定文件/面板补件；没有新线索时不继续全文搜索或重跑提取。

## 5. 低风险保留清单与抽查顺序

- Batch-01：除 M01510、M00071、M00074、M00051 和候选项外，其余首轮单元逐条建议 include/no_change；低风险抽查顺序建议先看 SMG/ bladder 的跨页定位，再看 iPain/ kidney，最后看 eLife。
- Batch-02：其余 keep 项建议 include/no_change；证据主要由 Fig.2/4/7/S7/S8 caption/text 与本地 Markdown 具体行共同支持。优先抽查所有原 exclude/context_only/update，再抽查 16 项去重的 target relation。
- 决定性材料：`marker提取/review_md/gemini-repair-review-2026-09-06/execution/gemini_tasks/round1-screening/batch-01-high-risk-core/evidence_index.json`、Batch-02 同名 evidence_index、两批 `screening_round1.json`，以及 `marker提取/review_md/DOI_*.md`；新增证据图未产生，原有实际查看图像已在 `evidence_index.json` 记录。

## 6. 覆盖边界

- 原 62 候选、原 28 状态接续、28 context_only、121 excluded、953 baseline backfill 不是互斥集合，也未被本轮假定全部完成；验收文件给出实际计数与缺口。下一步应由 Astra 决定是否追加限定批次，而不是把本轮 490 个首轮单元外推为总表全量通过。

## 7. Astra 最终审核建议

1. 先裁决 Batch-02 的政策分歧（exclude/context_only 是否确为作者实际 marker/gating）。
2. 再裁决 M00071、M00074、M00051、M01510 与两个新增候选。
3. 然后逐项核对 16 个去重 target，确认保留溯源与完整关系。
4. 最后抽查低风险 no_change，并在审批记录中区分 evidence-supported、unresolved、candidate-exclude 与未覆盖历史集合。
