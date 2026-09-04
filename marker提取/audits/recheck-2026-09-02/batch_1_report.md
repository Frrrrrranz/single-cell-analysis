# Batch 1 复核汇报（五篇范例）

> 批次：B20260903-BATCH1-RECHECK（recheck-pipeline-v2：规则初筛 + 证据包压缩 + 主代理直判）
> 判定日期：2026-09-02 ~ 2026-09-03；落表日期：2026-09-03
> 判定文件：`batch1_work/` 下五篇 `*_verdict.md`（每条候选含原句与理由，可回溯）
> 落表脚本：`scripts/apply_batch1_verdicts.py`（备份 `audited-extraction/recovery/our_markers_pre_batch1_recheck_backup_2026-09-03.xlsx`）
> 计数口径：以落表脚本实际应用为准；verdict 摘要与落表不一致处以落表为准（见 §9 对账说明）

## 0. 总览

| 论文 | 简称 | 行数变化 | 补录 | 升级 | 移除 | is_pns 修正 | 字段修正 |
|---|---|---|---|---|---|---|---|
| DOI_10.1038_s41586-020-2922-4 | 人肺图谱 | 113 → 87 | 8 | 28 | 34 | 0 | 5（标签 3 + 拼写 2） |
| DOI_10.1038_s41588-022-01243-4 | 人肺空间图谱 | 85 → 86 | 5 | 28 | 4 | 72 | 8（标签 7 + locator 1） |
| DOI_10.1038_s41591-024-03215-z | 乳腺癌 MBC | 15 → 13 | 0 | 8 | 2 | 0 | 1（subtype） |
| DOI_10.1101_2025.09.26.678707 | 人肾图谱 v2 | 48 → 48 | 0 | 12 | 0 | 48 | 1（备注） |
| DOI_10.7554_elife.71752 | 人 DRG | 10 → 29 | 19 | 0 | 0 | 0 | 0 |
| PMID_35115729（试点遗留） | 坐骨神经 | 42 → 42 | 0 | 1 | 0 | 0 | 0 |
| **合计** | | **1882 → 1874** | **32** | **77** | **40** | **120** | **15** |

维持不录合计 122 条候选（A 门 113 + B2 门 9，按篇不重复计数）；维持不升级（B 门）合计 12 条（详见 §7）。

---

## 1. 补录：32 条（M01886–M01917）

### 1.1 人肺图谱（8 条，A 门 7 + 归属修正补录 1）

| marker_id | cell_type | gene | evidence_type | 依据（摘录） |
|---|---|---|---|---|
| M01886 | Goblet cells | MUC5B | author_declared | EDF11a "canonical goblet cell markers MUC5B and MUC5AC and transcription factor SPDEF"（Gob 整簇漏提） |
| M01887 | Goblet cells | MUC5AC | author_declared | 同上 |
| M01888 | Serous cells | LTF | author_declared | EDF12g "serous cell markers LTF, LYZ, BPIFBP1 and HP"（Ser 整簇漏提） |
| M01889 | Serous cells | LYZ | author_declared | 同上 |
| M01890 | Serous cells | BPIFBP1 | author_declared | 同上 |
| M01891 | Serous cells | HP | author_declared | 同上 |
| M01892 | Bronchial endothelial cell | PLVAP | author_declared | "Bronchiolar vessel 2 (Br2) cells…expressing PLVAP"，PLVAP 用于支气管血管内皮识别 |
| M01893 | Bronchial vessel cells | MYC | author_declared | EDF3k "bronchial vessel-specific markers MYC"（原 M00160 归属泛支气管内皮错误，移除后按正确归属补录） |

### 1.2 人肺空间图谱（5 条，A 门 1 + D 门整簇 4）

| marker_id | cell_type | gene | evidence_type | 依据（摘录） |
|---|---|---|---|---|
| M01894 | nonmyelinating Schwann cells (nmSchwann) | CADM | author_declared | EDF5g "non-myelinating Schwann cell markers (CADM, GRIK2, NCAM1, ITGB4 and L1CAM)"。注：CADM 非标准 HGNC 符号（疑为 CADM1 的论文写法），PDF 原文即写作 CADM，保留原文拼写待图版核对 |
| M01895 | smooth muscle cells | ACTA2 | author_declared | EDF6f "smooth muscle (ACTA2) markers"（smooth muscle 整簇漏提） |
| M01896 | secretory goblet/club cells | SCGB1A1 | figure_labeled | EDF7e 图注 SCGB1A1 用于 secretory 细胞注释 |
| M01897 | ciliated cells | FOXJ1 | figure_labeled | EDF7e 图注 FOXJ1 用于 ciliated 细胞注释 |
| M01898 | basal cells | KRT14 | figure_labeled | EDF10d/e 图注 KRT14 用于 basal 细胞注释 |

### 1.3 人 DRG（19 条，A 门 8 + D 门追加 8 + 中等置信 3）

| marker_id | cell_type | gene | evidence_type | 依据（摘录） |
|---|---|---|---|---|
| M01899 | H12 | NTRK3 | author_declared | "A second larger group of human neurons H12 is marked by NTRK3 and…SCN1A" |
| M01900 | peptidergic nociceptors | TAC1 | author_declared | Fig5A 图注 "Peptidergic nociceptors marked by expression of TAC1"；主文 "the same three markers"（TAC1/NEFH/OSMR） |
| M01901 | H10 | MRGPRX1 | author_declared | "H10…marked by MRGPRX1" |
| M01902 | non-neuronal cells | PRP1 | author_declared | Methods "markers of non-neuronal cells including PRP1, MBP, QKI, LPAR1, and APOE were tagged as non-neuronal" |
| M01903 | non-neuronal cells | MBP | author_declared | 同上 |
| M01904 | non-neuronal cells | QKI | author_declared | 同上 |
| M01905 | non-neuronal cells | LPAR1 | author_declared | 同上 |
| M01906 | non-neuronal cells | APOE | author_declared | 同上 |
| M01907 | H12 | SCN1A | author_declared | 与 M01899 同句 "marked by NTRK3 and the voltage-gated ion channel SCN1A" |
| M01908 | H15 | PVALB | author_declared | "H15…marked by PVALB and NEFH" |
| M01909 | H15 | NEFH | author_declared | 同上 |
| M01910 | H15 | PIEZO2 | author_declared | 同句 H15 描述 |
| M01911 | H4 | SCN10A | author_declared | "H4…marked by SCN10A and NTRK1" |
| M01912 | H4 | NTRK1 | author_declared | 同上 |
| M01913 | H10 | PIEZO2 | author_declared | H10 簇描述句 |
| M01914 | H11 | SST | author_declared | "H11…marked by SST" |
| M01915 | peptidergic nociceptors | CALCA | author_declared（中等置信） | "peptidergic markers" 列表 + TAC1/CALCA/CALCB/ADCYAP1 类别归属句 |
| M01916 | peptidergic nociceptors | CALCB | author_declared（中等置信） | 同上 |
| M01917 | peptidergic nociceptors | ADCYAP1 | author_declared（中等置信） | 同上 |

> DRG D 门对账确认"疑似大幅漏提"成立：原 10 行仅覆盖 15 个细胞群中的 5 个；人神经元 14 个命名簇中 10 簇整簇漏提 + 非神经元细胞群整体漏提。

---

## 2. 升级：77 条（evidence_type → author_declared）

| 论文 | 条数 | marker_id 明细 |
|---|---|---|
| 人肺图谱 | 28 | B 门 10：M00023–M00025、M00134 类（SFTPA1/ETV5/BSG 等 Results "New lung cell types" 正文 marker 措辞）；D 门顺带 18：M00118–M00120、M00127–M00129、M00131、M00133、M00135、M00137、M00138、M00142、M00144–M00146、M00153、M00161、M00174、M00180、M00182、M00184、M00185、M00194–M00196（重命名措辞 "prepended a representative marker gene"、图注 "fibroblast-selective markers" 等） |
| 人肺空间图谱 | 28 | B 门 1（M00284 IGHA2："B lineage markers (IgD, IgA2 and IgG)"）；B2 门 2；C 门合并升级 1（M00294 LPO："serous (LPO) cell markers"）；D 门顺带 24（M00013–M00025 Schwann 系列、M00212、M00224–M00225、M00235、M00246–M00249、M00251、M00253、M00264、M00279、M00281、M00285、M00292、M00296、M00298 等） |
| 乳腺癌 MBC | 8 | M01304 CD19、M01305 FCRL5、M01308 CD8A、M01309 EPCAM、M01311 CD163、M01313 CD14、M01316 NCAM1、M01317 CD4（Methods "Canonical cell-type-specific markers (for example, EPCAM for epithelial cells, CD19 for B cells…)" + 面板注释用途链完整） |
| 人肾图谱 v2 | 12 | frPT/frTAL 6（M01549–M01554：PROM1/ROBO2/MEG3/ITGB8/TMPRSS4 等 "marked by the expression of" 措辞）+ moMAC-HBEGF+ 6（M01566–M01571：HBEGF/AREG/PLAUR/IL1B/OSM/CXCL8 "another inflammatory population marked by expression of"） |
| 试点遗留 | 1 | M01516 Pdgfra（PMID_35115729 "the fibroblast marker Pdgfra"） |

> 升级判据统一为双重门槛齐备：作者明确 marker 措辞（身份）+ 实际用于识别/命名/分类（用途）。所有升级行 source_context 替换为含 marker 措辞的完整原句。

---

## 3. 身份恢复：0 条

Batch 1 无 B② 门恢复行（乳腺癌 B2 门 9 条、空间图谱 B2 门 4 条经重审全部维持排除，理由更新为双重门槛不满足）。

## 4. 重审改判：0 条改判 include / 13 条维持排除

- 乳腺癌 B2 门 9 条（EMT 程序基因、COL 系列等）：原"范围外"排除 → 重审维持排除，理由更新为双重门槛不满足；
- 空间图谱 B2 门 4 条：维持排除。

## 5. 重复移除：40 条（全部入 audit_exclusions，tag：batch1_recheck_removed_2026-09-03）

| 论文 | 条数 | 分类明细（superseded by） |
|---|---|---|
| 人肺图谱 | 34 | 流式抗体面板归属错位 19（M00147/M00150/M00152/M00155/M00156/M00159/M00197/M00198/M00200/M00201/M00202/M00204/M00205/M00206/M00211/M00217/M00218/M00221 → 正确归属行 CD14→M00168、CD19→M00148、CD4→M00162、NCAM1→M00199 等）；C 门语义重复/归属错误 7（M00164→M00168、M00165→M00148、M00166→M00162、M00167→M00199、M00169→M00148、M00170→M00199、M00219→M00162）；D 门双标签重复 3（M00171→M00180、M00172→M00184、M00173→M00224）；拼写变体重复 3（M00121 Pi16→M00118、M00122 Serpinf1→M00119、M00130 Fgfr4→M00127）；标签分裂重复 1（M00141 AT2→M00137）；归属移除 1（M00160 MYC→新行 M01893） |
| 人肺空间图谱 | 4 | M00297（SMG-serous/LPO → M00294 合并升级）；M00244/M00245（IR-fibro 命名重复 → M00240/M00241）；M00227（CD4 T cells 语义重复 → M00228） |
| 乳腺癌 MBC | 2 | M01306（FCRL5 归属偏移 → M01305）；M01314（CD163 机械扫描未标记的重复 → M01311） |

## 6. 归属修正与字段修正：15 处

- 归属修正 2：M00160（MYC 泛支气管内皮 → bronchial vessel，移除+补录 M01893）；M01306（FCRL5 B regulatory cells 过度具体化 → B cells，由 M01305 承载）；
- 标签修正 10：人肺图谱 M00140/M00143（大小写统一）；空间图谱 M00236/M00237/M00240/M00241（IR-fibro 命名统一）、M00295 等；乳腺癌 M01315（subtype 简化为 CD163+ state）；
- 拼写修正 2：M00131（Slc7a10 → SLC7A10 + species mouse→human 核对）、M00192（Eln → ELN）；
- locator 更新 3：M00228、M00240、M00241、M00282（证据合并后 locator 补全）；
- 备注补充 1：M01578（αSMA 蛋白名 → ACTA2 转换说明）。

## 7. 维持不录：122 条候选 + 维持不升级 12 条

| 论文 | A 门不录 | B2 维持排除 | B 门维持不升级 |
|---|---|---|---|
| 人肺图谱 | 26（自动噪声 19 + 理由不录 7：TBX5/DPP4/MKI67/HES1/MYRF 等，均为转录因子/病毒受体/状态 marker 措辞） | 0 | 0 |
| 人肺空间图谱 | 24（自动噪声 10 + 理由不录 14：CD31/EpCAM 结构取向染色、CD45RA 蛋白异构体无基因符号等） | 4 | 0 |
| 乳腺癌 MBC | 25（EMT 程序基因集 10、其余双栏伪影/无 marker 措辞） | 9（7 条与 A 门重叠，不重复计数） | 1（M01307 FOXP3：注释用途成立但无 marker 措辞，维持 annotation_marker） |
| 人肾图谱 v2 | 24（噪声 token 17 + 理由不录 7：CD4/CDKN1A/PXDN/REL/MID1/PCK1/GDF15 临床 biomarker/功能基因） | 0 | 5（MD/PECs/resMAC-HLAIIhi Methods 反卷积句，维持 annotation_marker） |
| 人 DRG | 10（噪声 7：NP1/NP2/NP3/H10/H12/DRG/ISH + 转述背景 3：Mrgpra3/Etv1/TRPC3） | 0 | 6（M00005–M00009 维持 annotation_marker、M00010 维持 figure_labeled） |
| 试点遗留 | — | — | 1（M01517 Cd34 维持 annotation_marker） |

## 8. is_pns_cell 系统性修正：120 行

- 人肺空间图谱 72 行：提取期全表 85 行误设 `is_pns_cell=true`；按 PNS 白名单规则修正，仅 Schwann 细胞 13 行（M00013–M00025）保持 true。落表后存表 68 行携带修正记录，另 4 行（M00227/M00244/M00245/M00297）先修正后被移除归档；
- 人肾图谱 v2 48 行：肾脏非 PNS 器官，提取期全表误设 true，全部修正为 false（verdict 摘要漏记此项，落表核对时发现）；
- 修正后空间图谱 is_pns_cell=true 共 14 行（13 原有 Schwann + 新补录 M01894 CADM/nmSchwann）。

## 9. 对账说明（verdict 摘要 vs 落表）

1. 人肺图谱升级数：verdict 摘要初稿计 26，落表脚本逐条核对后为 28（B 门 10 + D 门顺带 18，含 M00131 同时做拼写修正与升级）。以落表为准；
2. 人肾图谱 is_pns 修正 48 行为落表时新发现（verdict 未记入摘要），已补入 import_log；
3. 空间图谱 is_pns 修正 72 行中 4 行随后被移除，audit_exclusions 归档值已为修正后状态；
4. 唯一键校验：批次内六篇 paper_id+cell_type+gene_symbol 无冲突；总表 1882 → 1874。

## 10. 发现的问题模式（供 Batch 2–8 参考）

1. **流式抗体面板归属错位（系统性）**：Methods 中 FACS/流式面板基因（CD3/CD4/CD14/CD19/CD56 等）在提取期被批量错挂到非归属细胞类型，人肺图谱 19 行。后续批次凡论文含流式 Methods 面板句，须核对每个抗体的细胞归属；
2. **is_pns_cell 提取期系统性误设**：非 PNS 器官论文（肾）与 PNS 相关论文的非 PNS 细胞（肺空间图谱）均出现全表 true。后续批次落表前先按白名单规则做整表核对，不等 verdict 逐条发现；
3. **双栏 PDF 拼接伪影**：乳腺癌与人肺空间图谱的 review_md 为双栏逐行交错抽取，候选"证据句"常为左右栏拼接（如 IR-Ven-Peri 标记句、EMT 基因列表）。判定前必须按左右栏重组，必要时回 PDF 定向核对；
4. **噪声 token 模式**：疾病缩写（AKI/CKD/MERS）、组蛋白修饰（H3K27ac）、技术平台（SS2/10x）、试剂货号（S34857）、细胞簇名（NP1/H10/TAL/AT2）、数据库名（HLCA/HPA/KPMP）高频出现，占维持不录的 63 条（122 条中）；
5. **同一 marker 措辞句的多基因并列**：如 "canonical goblet cell markers MUC5B and MUC5AC"、"serous cell markers LTF, LYZ, BPIFBP1 and HP"、"markers of non-neuronal cells including PRP1, MBP, QKI, LPAR1, and APOE"——并列基因须整组提取，防止部分漏提（本批整簇漏提 4 组）；
6. **命名重复/标签分裂**：同一细胞群在不同图表用不同名称（immune recruiting fibroblasts vs IR-fibro；AT2 vs Alveolar type 2 (AT2)），提取期产生同键多行。统一标签后按唯一键去重，证据合并至保留行；
7. **鼠式拼写变体**：图注中人鼠同图时基因按鼠式大小写书写（Pi16/Serpinf1/Fgfr4/Slc7a10），与人行构成拼写变体重复。人鼠行需分开保留但拼写按各自物种规范化。

## 11. 产出物清单

- 判定文件：`batch1_work/{五篇 paper_id}_verdict.md` + `RECHECK_BRIEF.md`（判定规范）+ 证据包 `*_pack.md`/`*_candidates.md`/`*_existing.md`；
- 落表脚本：`scripts/apply_batch1_verdicts.py`（幂等：重复运行会跳过已存在唯一键，备份不覆盖）；
- 总表：`marker提取/表单/our_markers.xlsx`（markers 1874 行；import_log +6 条 B20260903-BATCH1-RECHECK；audit_exclusions +40 条；说明与统计追加批次说明）；
- 备份：`marker提取/audited-extraction/recovery/our_markers_pre_batch1_recheck_backup_2026-09-03.xlsx`；
- 本报告：`marker提取/audits/recheck-2026-09-02/batch_1_report.md`。

## 12. 遗留事项（移交后续批次）

- 批次外四篇存在 18 组唯一键重复（历史遗留，备份核对确认先于本批存在）：DOI_10.1016_j.cell.2022.11.005（7 组）、DOI_10.1016_j.stem.2022.11.013（7 组）、DOI_10.1016_j.cell.2021.07.023（3 组）、DOI_10.1002_pros.24020（1 组）。待对应批次复核时按 D 门规则去重；
- M01894 CADM 拼写待图版核对（疑为 CADM1）；
- DRG 中等置信 3 行（CALCA/CALCB/ADCYAP1）建议同学审阅时重点关注。
