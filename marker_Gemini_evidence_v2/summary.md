# Gemini 交付整理与证据核验报告 (v2)

日期：2026-09-06  
执行目标：落实 Codex 审查报告 (`review.md`) 及 `gemini-task.md` 任务清单，完成机械可核验的交付整理、证据定位与追溯台账。保留既有基线与原始/修补 JSON 不动，所有成果交付于 `marker_Gemini_evidence_v2/` 目录。最终 gene–cell 语义裁决由 Codex 完成。

---

## 一、23 篇文献身份与来源核验汇总 (`paper_manifest.json`)

经实际查验 `marker提取/pdf/` 本地 23 篇原始文献 PDF 首页文本与元数据：
- **完整核对 23 篇标题、DOI、PMID 与实际页数**，彻底废弃原模板 `default_titles`。
- **全面纠正 6 篇严重主题错配**：
  1. `s41586-021-04345-x`: 原误填“胎儿神经嵴与感觉神经”，实际论文为 **Local and systemic responses to SARS-CoV-2 infection in children and adults** (36 页)。
  2. `s41586-024-07069-w`: 原误填“运动神经元转录因子代码”，实际论文为 **A single-cell time-lapse of mouse prenatal development from gastrula to birth** (58 页)。
  3. `s41588-025-02158-6`: 原误填“肾上腺发育与类固醇生成”，实际论文为 **Longitudinal single-cell multiomic atlas of high-risk neuroblastoma reveals chemotherapy-induced tumor microenvironment rewiring** (40 页)。
  4. `s41588-025-02182-6`: 原误填“肺神经内分泌细胞与肿瘤”，实际论文为 **An integrated transcriptomic cell atlas of human endoderm-derived organoids** (34 页)。
  5. `s41591-023-02327-2`: 原误填“慢性伤口愈合与衰老”，实际论文为 **An integrated cell atlas of the lung in health and disease** (47 页)。
  6. `s41591-024-03215-z`: 原误填“NASH”，实际论文为 **A multi-modal single-cell and spatial expression map of metastatic breast cancer biopsies across clinicopathological features** (38 页)。
- **纠正 07315 不存在来源文件**：`s42003-024-07315-x` 原修补引用的 `PMID_39702582_...` 本地不存在，已查证本地真实文件为 `PMID_39627536_Cross-species single-cell RNA-seq analysis reveals disparate and conserved cardiac and extracardiac .pdf` (20 页)。

---

## 二、增量台账与逐条对账统计 (`record_crosswalk.json`)

覆盖修补数据全部 **1,176 条** 记录（1,015 条 formal_markers + 28 条 context_only + 121 条 excluded + 12 条 unresolved）：

| 分类类别 | 总记录数 | 对应动作与说明 |
|---|---:|---|
| **formal_markers (基线重述)** | 953 | 标为 `baseline_existing`。全部直接对应既有正式总表 ID，未增加独立文献新证据，不计为新增。 |
| **formal_markers (待裁决候选)** | 62 | 标为 `pending_adjudication`。未声明总表 claimed ID，未比较实验条件与测量实体，交由 Codex 裁决。 |
| **context_only** | 28 | 标为 `context_only`。作者正文上下文提及或单纯富集，未用于定义细胞。 |
| **excluded** | 121 | 标为 `excluded`。排除记录，逐条保留原始理由与匹配键。 |
| **unresolved** | 12 | 标为 `unresolved`。包含符号歧义或待复核项。 |
| **合计** | **1,176** | **无遗漏、无虚报、不按新旧差值夸大新增** |

> **关键原则落实**：
> 1. 严禁改写 `marker_original`，成功恢复了如 `CD45` (PTPRC)、`CD66c` (CEACAM6)、`β-tubulin III` (Tubb3) 等原始符号实体。
> 2. 953 条基线回填记录如实标为 `baseline_existing`，绝不冒充独立核验。

---

## 三、原始 28 个未决项处理结果 (`unresolved_28.json`)

严格按 Codex `unresolved-28-review.md` 中的 28 个原始 `record_id` 逐条梳理，不合并基因、不混入已纠正项：

1. **已同意撤销条目 (withdrawn_to_exclude, 3条)**：
   - `DOI_10.1038_s41467-024-52052-8_M09` (Glb1 - Senescent Nociceptor)：确认系将 SA-β-gal 酶活染色错误改写为转录本，同意撤销并移入 excluded。
   - `DOI_7554_elife.62522_M07` (CALCA - PNEC)：确认原 Fig. 1B/D 无 CALCA 标签，撤销错误原图引文；无其他补充材料前关系保持待核。
   - `DOI_7554_elife.62522_M08` (CHGA - PNEC)：确认原 Fig. 1B/D 无 CHGA 标签，撤销错误原图引文；保持待核。
2. **已有确凿证据纠正/候选条目 (confirmed_candidate, 1条)**：
   - `DOI_10.1038_s41588-022-01243-4_M03` (PRR4 - SMG Serous Cell)：PDF 第 34 页 Extended Data Fig. 10g 明确标注 `PRR4 (SMG-serous)`，第 35 页图注说明 HPA IHC 蛋白定位验证。推翻此前降级决定，符合 MARKER_POLICY 作为有效证据保留。
3. **正文符号无法唯一解析 (still_unresolved, 1条)**：
   - `DOI_10.1016_j.isci.2024.111628_M02` (NRXN1 - Schwann Cell)：正文明确为 `single Schwann cell cluster (CDH19+/NRXN+/XKR4+)`，细胞为 Schwann cell 无误，但 `NRXN+` 属家族通称，无法唯一标准化至 NRXN1，保持 unresolved。
4. **维持待核条目 (pending_verification, 23条)**：
   - 包括 COL2A1、SOX10、ETV5、AGER、Acta2、Krt14、Col1a1、Adgre1、Calca、Mrgprd、Piezo2、Fabp7、Isl1、Ccr2、SLC12A1、AQP2、SLC12A3、NPHS2、TTN、TNNT2、ACTA2、Clec3b 等。未提供独立证据图前保持待核，不以“非新发现/非特异”擅自物理排除。

---

## 四、指定争议面板高清截图与证据索引 (`evidence/`)

已在 `marker_Gemini_evidence_v2/evidence/` 下截取高分辨率清晰图像，并建立结构化图文索引 `evidence_index.json`：
1. `DOI_7554_elife.62522_p4_Fig1B_1D.png` 及 `dotplot_detail.png`:
   - 纠正此前 Codex 误记：Fig. 1D 的 PNEC 基因确为 **RIMS2**（非 CHGB）；Fig. 1B 中展示 ASCL1 染色质可及性开放峰。
   - 证实 LAMC3 对应 Chondrocytes（Pericyte 主标签为 NTRK3）；FCN1 对应 Monocytes（Interstitial macrophage 主标签为 FOLR2）。
2. `DOI_10.1038_s41467-024-52052-8_p4_Fig1d_1h.png` 及 `heatmap_detail.png`:
   - 查证巨噬细胞主标签为 H2-Eb1/Aa/Ab1，无 Cd86 标签；完全否决修补 JSON 挪用神经母细胞瘤裁决的虚假声明。
3. `DOI_10.1016_j.isci.2024.111628_p6_Schwann_full.png` 及 `paragraph_crop.png`:
   - 证实正文原文为 `single Schwann cell cluster (CDH19+/NRXN+/XKR4+)`，细胞为施万细胞无误，纠正销项表中的转述错误。
4. `DOI_10.1038_s41588-022-01243-4_p34_ExtDataFig10g_detail.png` 及 `p35_ExtDataFig10_legend.png`:
   - 清晰展示 `PRR4 (SMG-serous)` 图像标注与 HPA IHC 图注，确证蛋白定位证据。
5. `DOI_10.1126_science.aat5031_p4_Fig1_full.png`:
   - 肾脏空间分区图，维持肾实质待核状态。

---

## 五、材料状态逐文件登记 (`materials_manifest.json`)

- 区分 `actually_reviewed`（实际已查范围）、`available_not_reviewed`（本地存在但未穷尽）、`missing`（本地缺失，如独立 Supplementary Tables）、`history_unknown`（此前轮次是否查看缺乏可信日志，坚决标注历史未知）。
- 绝不因存在 repair JSON 而程序化默认赋值为全部 reviewed。
- 明确暂不开展前 20 篇的新提取。

---

## 六、自检校验与数据一致性结论

- **总表 ID 链接校验**：全部 953 条关联的 `claimed_marker_id` 均在 `our_markers.xlsx` 中 100% 存在，无断链或错链。
- **未决 28 项唯一性校验**：28 条无重复、无遗漏，严格一一对应。
- **截图文件存在性校验**：索引中的高清截图文件在本地磁盘均实际存在。
- **页码合法性**：所有引用的真实 PDF 页码均在其有效页数范围内。
- **交付完整性**：所有 6 项要求已全部闭环，新交付成果完全独立保存于 `marker_Gemini_evidence_v2/`，原始基线与正式文件完好无损。
