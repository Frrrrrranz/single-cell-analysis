# 第一轮首筛至第二轮复筛交接文档 (Handoff to Luna)

- **执行阶段**: 第一轮首筛与取证 (Round 1: Screening & Evidence Harvesting)
- **执行模型**: Gemini 3.8 Flash (思考档位: high)
- **下阶段接棒模型**: GPT-5.6 Luna (思考档位: max)
- **终审裁决模型**: GPT-6 Astra (思考档位: medium)
- **本批次编号**: `batch-01-high-risk-core` (第一批：核心高风险纠错与基线核验)
- **交付时间**: 2026-09-06
- **基线版本与哈希**:
  - `our_markers.xlsx` SHA-256: `8abdddb800dce6e84ca711d9cb5905cc114390e77adc499f8ef5471f09021373`
  - `our_markers_by_cell.xlsx` SHA-256: `9b166cd7aef77d39c8019dcc163a6e2aa8dd0ab74927dbe0195060390062c3e2`
  - 基线有效 marker 总行数: **2,499** 行

---

## 1. 本批次筛查范围与整体统计

本批次集中突破涉及现有正式总表准确性、历史高风险纠错、测量实体混淆、跨论文借用伪造、基因家族歧义及历史未决的 5 篇核心高风险论文：
1. `DOI_10.7554_elife.62522` (单细胞多组学人肺发育图谱)
2. `DOI_10.1038_s41467-024-52052-8` (小鼠衰老伤害感受器 iPain 图谱)
3. `DOI_10.1016_j.isci.2024.111628` (人类膀胱单核/单细胞转录组图谱)
4. `DOI_10.1038_s41588-022-01243-4` (人类支气管黏膜下腺 SMG 空间免疫图谱)
5. `DOI_10.1126_science.aat5031` (人类肾脏时空发育与免疫分区图谱)

- **基线正式表覆盖数**: 196 条 (已在 `coverage.json` 中标记为 `completed_round1`)
- **关联高风险候选/历史未决/修补条目**: 17 条
- **本批生成首筛审查单元总数**: **213 条** (详见 `screening_round1.json`)

---

## 2. 核心风险发现与建议复核重点 (Priority Review for Luna)

### 2.1 涉及现有总表准确性的关键风险 (4 条基线记录)

1. **`M01510` (Sst - SST nociceptor subtype, mouse, `DOI_10.1038_s41467-024-52052-8`)**
   - **风险类型**: 引文不支持正式 marker (citation_unsupported_external_reference)。
   - **实核情况**: 原定位为正文 Introduction 第 2 段。实查原文，该处仅为综述性外部背景文献引入（“Those neurons are of different subtypes...”），本文主实验体系并未实际使用 Sst 进行细胞分选、聚类定义或 marker 验证。
   - **Gemini 建议**: 建议判定为 `context_only`，操作建议 `move_to_unresolved`，**从正式总表中移出**至上下文/未决隔离区。
   - **Luna 复核重点**: 确认本文后续 Results 章节及补充表中是否存在本文作者实际运用 Sst 作为 marker 的独立直接证据；若无，应确认移出。

2. **`M00071` (Rbfox3 - senescent nociceptors, mouse, `DOI_10.1038_s41467-024-52052-8`)**
   - **风险类型**: 细胞状态粒度混淆 (cell_granularity_state_confusion)。
   - **实核情况**: 实查 Fig. 3i 图像与图注，NeuN (Rbfox3) 是泛外周神经元背景标志物，作者在该神经元群中利用 SA-β-gal 检测衰老。Rbfox3 本身绝非衰老特异 marker。
   - **Gemini 建议**: 维持 `include`，但操作建议 `update`，将 cell_type 规范为 nociceptors / neurons，并在备注中阐明其 pan-neuronal 属性，纠正“衰老特异”误导。
   - **Luna 复核重点**: 确认 cell_type 与 subtype 规范化表达方式。

3. **`M00074` (Prph - neurons, mouse, `DOI_10.1038_s41467-024-52052-8`)**
   - **风险类型**: 重复记录与粗细粒度重叠 (duplicate_record_granularity_overlap)。
   - **实核情况**: 与 `M00073` (Prph - peripherin-positive neurons, small diameter) 源自同一次实验（Fig. 5c,d），属于粗粒度重复登记。
   - **Gemini 建议**: 建议 `merge_duplicate`，并入 M00073 并保留其更精准的小直径感觉神经元亚型描述。
   - **Luna 复核重点**: 审核两记录的实验定位一致性及合并动作。

4. **`M00051` (ASCL1 - Pulmonary neuroendocrine cell, human, `DOI_10.7554_elife.62522`)**
   - **风险类型**: 测量模态精度 (measurement_entity_precision)。
   - **实核情况**: 实查 PDF p.4，Fig. 1B 为 scATAC-seq 开放染色质峰，ASCL1 在 PNEC 中表现出极强的特异染色质可及性；Fig. 1D 的 RNA 点图主标签为 RIMS2。
   - **Gemini 建议**: 维持 `include`，操作建议 `update`，在元数据中明确其测量模态为 `chromatin_accessibility`（双模态调控 marker），防止用户误解为仅是高表达 RNA。
   - **Luna 复核重点**: 确认单细胞 ATAC-seq 调控标志物在总表中的标准模态标注。

---

### 2.2 坚决否决与排除的严重违规/错配条目 (4 条修补候选)

1. **`REV_IPAIN_01_Cd86` (Cd86 - Macrophage, `DOI_10.1038_s41467-024-52052-8`)**
   - **违规性质**: 跨论文借用外部裁决伪造引文 (cross_paper_borrowed_fabricated_reference)。
   - **实核事实**: 真实 Fig. 1d 热图巨噬细胞标定基因为 H2-Eb1/H2-Aa/H2-Ab1，根本无 Cd86。该条目系前序修补盲目借用其他论文裁决所致。
   - **建议**: `exclude` + `hold`，坚决禁止入库。

2. **`REV_IPAIN_02_Glb1` (Glb1 - Senescent Nociceptor, `DOI_10.1038_s41467-024-52052-8`)**
   - **违规性质**: 测量实体严重混淆 (measurement_entity_error)。
   - **实核事实**: 原提取将 SA-β-gal（衰老相关 β-半乳糖苷酶活性染色）武断转写为 Glb1 基因表达。
   - **建议**: `exclude` + `hold`，维持排除。

3. **`REV_ELIFE_04_LAMC3` (LAMC3 - Pericyte, `DOI_10.7554_elife.62522`)**
   - **违规性质**: 基因–细胞严重配对错位 (gene_cell_misalignment)。
   - **实核事实**: 实查 Fig. 1D 点图，LAMC3 对应的群是 Chondrocytes（软骨细胞），Pericyte 对应标签是 NTRK3。
   - **建议**: `exclude` + `hold`，排除该错误配对。

4. **`REV_ELIFE_05_FCN1` (FCN1 - Interstitial macrophage, `DOI_7554_elife.62522`)**
   - **违规性质**: 基因–细胞严重配对错位 (gene_cell_misalignment)。
   - **实核事实**: 实查 Fig. 1D 点图，FCN1 对应的是 Monocytes（单核细胞），Interstitial macrophage 对应标签是 FOLR2。
   - **建议**: `exclude` + `hold`，排除该错误配对。

---

### 2.3 恢复与补充入库建议 (2 条高确定性候选)

1. **`REV_SMG_01_PRR4` (PRR4 - SMG Serous Cell, `DOI_10.1038_s41588-022-01243-4`)**
   - **性质**: 否决此前不当降级，恢复合法 marker。
   - **实核事实**: PDF p.34 Extended Data Fig. 10g 明确标注 'PRR4 (SMG-serous)'，p.35 图注清晰说明 HPA 免疫组化组织验证。依据 MARKER_POLICY.md 第 2 条与 2.2 条，真实 marker 不能因来自蛋白/IHC 或非新发现而被排除。
   - **建议**: `include` + `add` (推荐 Astra 最终纳入新增总表)。

2. **`REV_ELIFE_01_RIMS2` (RIMS2 - PNEC, `DOI_10.7554_elife.62522`)**
   - **性质**: 纠正前序笔误，恢复遗漏主图 marker。
   - **实核事实**: PDF p.4 Fig. 1D 点图 PNEC 行的首要正向 RNA 标记确为 RIMS2（此前 Codex 曾笔误记为 CHGB，已彻底核实澄清）。
   - **建议**: `include` + `add`。

---

### 2.4 保持未决隔离条目 (11 条，严格执行停止条件)

依据 operations-manual.md 第 7 条“停止条件”，以下条目在直接核查主图后未发现直接文字标签，且补充材料检索成本极高，**坚决不以常识臆断补充证据，也不擅自物理删除**，全部标记为 `unresolved` 并列出剩余缺口：
- **`CALCA` / `CHGA` (`DOI_10.7554_elife.62522`)**: 撤销伪引文 Fig.1B/D，保持未决。
- **`Calca` / `Mrgprd` / `Piezo2` / `Fabp7` (`DOI_10.1038_s41467-024-52052-8`)**: 主热图 Fig. 1d 未见直接独立文字标签，保持未决。
- **`NRXN1` (`DOI_10.1016_j.isci.2024.111628`)**: 原文为 `NRXN+` 家族泛称，无法唯一标准化，保持未决。
- **`SLC12A1` / `AQP2` / `SLC12A3` / `NPHS2` (`DOI_10.1126_science.aat5031`)**: 真实 Fig. 1 图板（PDF p.13）未直接给出单基因表达点图，保持未决。

---

## 3. 证据索引及查看指引

本批次全部证据切片已建立双重校验哈希，Luna 可直接查阅：
- `EVID_01`: `marker_Gemini_evidence_v3/evidence/EVID_01_elife_62522_fig1d.png` (PDF p.4 Fig. 1B/D)
- `EVID_02`: `marker_Gemini_evidence_v3/evidence/EVID_02_ipain_fig1d.png` (PDF p.3 Fig. 1d/h & Fig. 3i)
- `EVID_03`: `marker_Gemini_evidence_v3/evidence/EVID_03_bladder_text_p6.png` (PDF p.6 正文与 Fig. 1E)
- `EVID_04`: `marker_Gemini_evidence_v3/evidence/EVID_04_smg_edfig10g.png` (PDF p.34 Ext Data Fig. 10g)
- `EVID_05`: `marker_Gemini_evidence_v3/evidence/EVID_05_kidney_fig1_p13.png` (PDF p.13 真实 Fig. 1 总图)

---

## 4. 建议 Luna 的复核执行顺序

1. **第一优先级**: 裁决 4 条涉及正式表准确性的基线记录（`M01510` Sst 是否正式移出总表；`M00071` Rbfox3 状态纠正；`M00074` Prph 合并；`M00051` ASCL1 模态标注）。
2. **第二优先级**: 确认 4 条严重违规排除项（Cd86, Glb1, LAMC3-Pericyte, FCN1-Macrophage）的排除裁决。
3. **第三优先级**: 审核 2 条恢复补充建议（PRR4, RIMS2）。
4. **第四优先级**: 确认 11 条未决隔离项及停止原因。
5. **第五优先级**: 抽样复核其余 192 条基线保持 include/no_change 记录。
