# DOI_10.1038_s41586-020-2922-4 (人肺图谱) 复核判定报告

> 判定方式：recheck-pipeline-v2（证据包 + 主代理直判 + 定向 grep 重组双栏拼接句）
> 判定日期：2026-09-03

## 摘要

补录 8（A 门 7 + 归属修正补录 1）；升级 26（B 门 10 + D 门顺带 16）；移除 34（流式抗体错位 19 + C 门语义重复/错位 7 + D 门双标签重复 3 + M00160 归属移除 1 + 拼写变体重复 3 + M00141 标签分裂重复 1）；标签修正 3；拼写修正 2；维持不录 33 条 A 门候选中的 26 条（含 19 条自动噪声）。
总表行数：113 → 87（-26 净变化；详见落表对账）。

## A 门逐条判定

| # | 候选基因 | 判定 | cell_type | gene_symbol | species | evidence_type | source_locator | 原句（重组后完整） | 理由 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | TBX5 | 不录 | - | - | - | - | - | "d, Alveolar section of human lung probed by smFISH for pericyte marker COX4I2 and transcription factor TBX5. TBX5 is enriched in pericytes (arrowheads, 92% of TBX5+ cells were COX4I2+, n = 250)." (EDF5d legend) | 作者明确称 TBX5 为 transcription factor 并用 enriched 措辞；pericyte marker 指 COX4I2 非 TBX5。原候选句系 MCC 统计句双栏拼接伪影，重组后不成立 |
| 2 | DPP4 | 不录 | - | - | - | - | - | "…coronaviruses) and DPP4 (MERS coronavirus) were both detected in AT2 cells…" (Results §) | 病毒受体表达描述，无 marker 措辞、无注释用途 |
| 3 | MKI67 | 不录 | - | - | - | - | - | "…proliferation marker MKI67 (green) in basal cells (marked by KRT5, red)…" (EDF3e legend) | proliferation marker 是增殖状态用途，非细胞群识别；同句 KRT5 有 marked by 措辞（见 D 门顺带升级 M00153） |
| 4 | MUC5B | **补录** | Goblet cells | MUC5B | human | author_declared | Extended Data Fig. 11a legend | "a, Scatter plots showing median expression levels (ln(CPM + 1)) in indicated cell types of each expressed human gene and mouse orthologue … canonical goblet cell markers MUC5B and MUC5AC and transcription factor SPDEF in mouse (left) and human (right) goblet cells." | "canonical goblet cell markers" 明确 marker 身份；Gob (goblet) 为 Fig.1a 注释细胞类型，此前整簇漏提 |
| 5 | MUC5AC | **补录** | Goblet cells | MUC5AC | human | author_declared | Extended Data Fig. 11a legend | 同上 | 同上 |
| 6 | LTF | **补录** | Serous cells | LTF | human | author_declared | Extended Data Fig. 12g legend | "g, Dot plots of expression of serous cell markers LTF, LYZ, BPIFBP1 and HP showing switched expression (type 3 change) from mouse airway epithelial cells to human serous cells, which mice lack (asterisk)." | "serous cell markers" 明确；Ser (serous) 为 Fig.1a 注释类型，整簇漏提 |
| 7 | AT2 | 不录-噪声 | - | - | - | - | - | （证据句为基因面板竖排 OCR 碎片） | 细胞类型名非基因 |
| 8 | AT1 | 不录-噪声 | - | - | - | - | - | 同上 | 细胞类型名 |
| 9 | ECM | 不录-噪声 | - | - | - | - | - | "…green, extracellular matrix (ECM; autofluorescence)…" | 细胞外基质缩写非基因 |
| 10 | HES1 | 不录 | - | - | - | - | - | "…immunostaining of adult human pseudostratified airway for differentiation marker HES1 (green)…Other HES1+ cells have turned off basal marker KRT5." (EDF3) | differentiation marker 是分化状态用途；HES1+ basal cells 为过渡态描述，非细胞群识别 |
| 11 | Bro1 | 不录-噪声 | - | - | - | - | - | "Bro1, bronchial vessel 1 cell…" (Fig.1a legend 缩写表) | 细胞类型缩写（已有 Bro1/ACKR1 行 M00161） |
| 12 | S34857 | 不录-噪声 | - | - | - | - | - | "…viability marker Sytox blue (1:3,000, ThermoFisher S34857)…" | 试剂货号；viability marker 是试剂用途 |
| 13 | NKX2 | 不录-噪声 | - | - | - | - | - | "…HHIP (448441-C3), SFTPC (314101-C2), NKX2-1 (434721-C3)…" | NKX2-1 探针货号列表中的截断 token；NKX2-1 未被本文用于细胞群注释（仅 qPCR 探针），且完整词为 NKX2-1 |
| 14 | MYRF | 不录 | - | - | - | - | - | "These include what may be long-sought master regulators of AT1 cells (for example, MYRF)…"; "…other AT1 transcription factors such as MYRF, which is AT1-selective in both species"; "…probed by smFISH for AT1 marker AGER and transcription factor MYRF." | 作者通篇以 master regulator/transcription factor/AT1-selective 呈现 MYRF，从未称 marker；AT1 marker 指 AGER |
| 15 | SS2 | 不录-噪声 | - | - | - | - | - | "…fied by technology (10x versus SS2)…" | Smart-seq2 平台缩写 |
| 16 | MERS | 不录-噪声 | - | - | - | - | - | "…DPP4 (MERS coronavirus)…" | 疾病缩写 |
| 17 | GRCm38 | 不录-噪声 | - | - | - | - | - | "…the GRCm38.p6 mouse reference genome…" | 参考基因组版本 |
| 18 | NCBI | 不录-噪声 | - | - | - | - | - | "…with the NCBI-106 annotation…" | 数据库注释版本 |
| 19 | MAST | 不录-噪声 | - | - | - | - | - | "…were compared head-to-head using the 'MAST' statistical framework" | 统计工具 |
| 20 | MCC | 不录-噪声 | - | - | - | - | - | "…we calculated MCC scores…" | Matthews 相关系数 |
| 21 | MACS | 不录-噪声 | - | - | - | - | - | "…cell sorting (MACS and FACS) using antibodies…" | 磁珠分选方法 |
| 22 | IPF | 不录-噪声 | - | - | - | - | - | "IPF, endothelial marker CLDN5 (white)…"（图注拼接） | 疾病缩写；该句中 CLDN5 已有 author_declared 行（M00175） |
| 23 | COPD | 不录-噪声 | - | - | - | - | - | "…probed for COPD or emphysema gene SERPINA1…" | 疾病缩写 |
| 24 | SERPINA1 | 不录 | - | - | - | - | - | "…are COPD/emphysema genes SERPINA1 and HHIP, both selectively [expressed]…" | 疾病基因描述，非 marker 措辞、无注释用途 |
| 25 | LYZ | **补录** | Serous cells | LYZ | human | author_declared | Extended Data Fig. 12g legend | 同候选 6 句 | 同候选 6 |
| 26 | BPIFBP1 | **补录（存疑标注）** | Serous cells | BPIFBP1 | human | author_declared | Extended Data Fig. 12g legend | 同候选 6 句；review_md 原文拼写即为 BPIFBP1 | "serous cell markers" 措辞成立故收录；但 BPIFBP1 非标准 HGNC 符号（疑为 BPIFA1/BPIFB1 之 PDF 转写变体），notes 标注"待图版核对拼写" |
| 27 | SK3 | 不录-噪声 | - | - | - | - | - | "…CD4 (BD 340443, clone SK3…" | 流式抗体克隆号 |
| 28 | HIB19 | 不录-噪声 | - | - | - | - | - | "…CD19 (Biolegend 302234, clone HIB19…" | 流式抗体克隆号 |
| 29 | RPA | 不录-噪声 | - | - | - | - | - | "…CD8 (BD 555368, clone RPA-T8…)…CD4…clone RPA-T4…" | 克隆号 RPA-T4/RPA-T8 截断 |
| 30 | CD3 | 不录 | - | - | - | - | - | "Immune cells from subject matched blood were incubated with FcR Block … and then stained with directly conjugated anti-human CD3 (BD 563548), CD4 (BD 340443), CD8 (BD 340692), CD14 (BD 557831), CD19 (Biolegend 302234), CD47 (BD 563761), CD56 (BD 555516), and CD235a (BD 559944) antibodies…" (Methods) | 血免疫细胞流式染色面板，验证/表型确认用途而非 cluster 注释；本文注释链为 "canonical marker genes from the literature + bulk RNA-seq markers"（L850），不含该面板设计句。不满足注释用途门槛 |
| 31 | PLVAP | **补录** | Bronchial endothelial cell | PLVAP | human | annotation_marker | Results §Cell markers, regulators and interactions, p.621 | "Thus, bronchial endothelial cells are distinct from their counterparts in the pulmonary circulation, distinguished by matrix (VWA1 and HSPG2), fenestrated morphology (PLVAP) and cell cycle-associated (MYC and HBEGF) genes." | "distinguished by" 为区分性 marker 措辞，用于区分支气管内皮与肺循环内皮（注释用途成立）；同句 MYC 的 EDF3k 证据（bronchial vessel-specific markers MYC）佐证该特征组指向支气管循环侧。旧范围性排除（非 PNS）已失效。VWA1/HSPG2/HBEGF 同句基因未列入本轮候选，记入 D 门待扩清单 |
| 32 | CDHR3 | 不录 | - | - | - | - | - | "…basal, and goblet cells, and CDHR3 ('common cold' rhinovirus C) was…" | 病毒受体描述 |
| 33 | CD8 | 不录 | - | - | - | - | - | 同候选 30 句（流式染色面板） | 同候选 30；且本文肺组织免疫注释无 CD8+ T cells 独立标签（血细胞标签为 CD8 M/E） |

## B 门逐条判定

| marker_id | gene | cell_type | 判定 | 完整原句（重组后） | 理由 |
|---|---|---|---|---|---|
| M00120 | SFRP2 | Adventitial fibroblast | **升级 author_declared** | "Two clusters expressed classical fibroblast markers (BSG and COL1A2) (Fig. 1e) but one (SPINT2+FGFR4+GPC3+) localized to alveoli ('alveolar fibroblasts') and the other (SFRP2+PI16+SERPINF1+) to vascular adventitia and nearby airways ('adventitial fibroblasts') (Fig. 1f, Extended Data Fig. 4a–d)." | 基因组合签名用于识别并命名新细胞类型（adventitial fibroblasts）；上下文 "classical fibroblast markers" 措辞确立 marker 语境 |
| M00127 | FGFR4 | Alveolar fibroblast | **升级 author_declared** | 同上句 | (SPINT2+FGFR4+GPC3+) 组合签名命名 alveolar fibroblasts |
| M00129 | SPINT2 | Alveolar fibroblast | **升级 author_declared** | 同上句 | 同上 |
| M00133 | CA2 | Alveolar type 2 (AT2) | **升级 author_declared** | Fig.1c 图注："c, Dot plot of AT2 marker expression (10x dataset)."；正文："One cluster (WIF1+HHIP+CA2+) expressed higher levels of some canonical AT2 markers (SFTPA1, SFTPC and ETV5)…" | 图注明确 "AT2 marker expression" dot plot 且 CA2 为 (WIF1+HHIP+CA2+) 签名成员，图用于 AT2 注释 |
| M00135 | HHIP | Alveolar type 2 (AT2) | **升级 author_declared** | EDF3i 图注（重组）："…general AT2, AT2 selective, and AT2-signalling selective marker genes in AT2 and AT2-signalling human lung cells (SS2 data). AT2 selective markers include negative regulators of Hedgehog and Wnt signalling pathways (for example, HHIP and WIF1, highlighted red)…" | "AT2 selective markers include … HHIP and WIF1" 明确 marker 措辞 |
| M00171 | EREG | Dendritic cell (subtype EREG+) | **移除（语义重复）** | "…we prepended a representative marker gene to their 'canonical' identity (for example, IGSF21+ dendritic, EREG+ dendritic, and TREM2+ dendritic)." | 与 M00180 (EREG+ dendritic/EREG) 规范化后为同一细胞同一基因同一证据；保留作者命名标签行 M00180 |
| M00172 | IGSF21 | Dendritic cell (subtype IGSF21+) | **移除（语义重复）** | 同上句 | 与 M00184 重复，保留 M00184 |
| M00173 | TREM2 | Dendritic cell (subtype TREM2+) | **移除（语义重复）** | 同上句 | 与 M00224 重复，保留 M00224 |
| M00180 | EREG | EREG+ dendritic | **升级 author_declared** | 同 M00171 句 + EDF4m 图注 "…EREG+ dendritic cell marker EREG (red) and general dendritic cell marker GPR183 (white) (m)…" | "prepended a representative marker gene" 为明确 marker+命名用途；图注 "EREG+ dendritic cell marker EREG" 双重确认 |
| M00184 | IGSF21 | IGSF21+ dendritic | **升级 author_declared** | 同上句 + EDF4l 图注 "…cell markers IGSF21 (red) and GPR34 (white) (l)…" | 同上 |
| M00194 | ASPN | Myofibroblast | **升级 author_declared** | 正文："One cluster (WIF1+FGF18+ASPN+) is classical myofibroblasts…" + EDF4f 图注 "…for myofibroblast and fibromyocyte marker ASPN (red)…" | 图注明确 "myofibroblast and fibromyocyte marker ASPN" |
| M00196 | WIF1 | Myofibroblast | **升级 author_declared** | "One cluster (WIF1+FGF18+ASPN+) is classical myofibroblasts and localized [to …]" | (WIF1+FGF18+ASPN+) 组合签名命名 classical myofibroblasts |
| M00224 | TREM2 | TREM2+ dendritic | **升级 author_declared** | 同 M00180 句 + EDF4n 图注 "…TREM2+ dendritic cell markers TREM2 (red) and CHI3L1 (white) (n)…" | 同 M00180 |

## B2 门：本篇 0 条候选。

## C 门逐条判定

| 组 | 行1 | 行2 | 判定 | 保留 | 移除 | 理由 |
|---|---|---|---|---|---|---|
| 1 | M00141 AT2/SFTPC | M00142 AT2-signalling (AT2-s)/SFTPC | **不合并** | 均保留（M00141 另见 D 门标签分裂处置） | - | AT2 与 AT2-signalling 是不同细胞群（Fig.1d："AT2-signalling cells (SFTPC+ WIF1−) are intermingled among AT2 cells (SFTPC+ WIF1+)"）；图注 "shared AT2 and AT2-signalling marker SFTPC" 明确两者共享该 marker，两行各自成立 |
| 2 | M00164 classical and nonclassical monocytes/CD14 | M00168 classical monocytes/CD14 | **合并（移除宽标签行）** | M00168 | M00164 | 同源流式抗体行、同基因；保留更具体标签 classical monocytes |
| 3 | M00165 classical and nonclassical monocytes/CD19 | M00169 classical monocytes/CD19 | **两行均移除（归属错误）** | - | M00165、M00169 | CD19 为 B cell marker，挂 monocytes 系流式面板错挂；正确归属 B cells 已有 M00148（CD19/B cells/positive） |
| 4 | M00162 CD4+ T cells/CD4 | M00219 T cells/CD4 | **合并（移除泛标签行）** | M00162 | M00219 | 同源同基因；保留更具体标签 CD4+ T cells |
| 5 | M001167 classical and nonclassical monocytes/NCAM1 | M00170 classical monocytes/NCAM1 | **两行均移除（归属错误）** | - | M00167、M00170 | NCAM1 (CD56) 为 NK marker；正确归属 NK 已有 M00199/M00203 |
| 6 | M00187 immune/PTPRC | M00189 immune and endothelial enriched/PTPRC | **不合并** | 均保留 | - | 不同 locator 与语境（M00187 来自 Cell clustering 注释句、author_declared；M00189 来自 Lung cell processing and staining 的 MACS/FACS 区室平衡句），标签含义不同（聚类区室 vs 处理富集群） |

（注：组 5 行1 marker_id 应为 M001167 之误写，实际 M001167 不存在，正确为 M00167；上表以 M00167 记。）

## D 门检查结论

### D1 聚类对账
Fig.1a 注释标签（缩写表 L144-149 重组）：Bas-d/Bas-p/Bas-px、Bro1/Bro2、Cap/Cap-a/Cap-i1/Cap-i2、Cil/Cil-px、FibM、Gob、Ion、LipF、Lym、Meso、MyoF、Muc、NE、Peri、Ser、VSM、AT1/AT2/AT2-s、AdvF、AlvF、内皮系列、免疫系列（L92-94："all classical lung cell types (41 out of 45, 91%)"，免疫 25 群）。

existing 覆盖缺口的处置：
- **Gob（goblet）**：本轮补录 MUC5B/MUC5AC ✓
- **Ser（serous）**：本轮补录 LTF/LYZ/BPIFBP1/HP ✓
- **文本不可恢复整簇（漏提-待图版核对留档，不强行补录）**：Ion（ionocyte；MC1R 仅激素受体描述，无 marker 措辞）、Club（SCGB1A1 全文 0 命中）、Muc（mucous，仅缩写清单）、Meso（mesothelial）、Bro2、Cap（general capillary）、Cap-a（capillary aerocyte）、Cap-i1/Cap-i2（capillary intermediates）、VSM（vascular smooth muscle）、Bas-d/Bas-p（differentiating/proliferating basal）。这些类型的 marker 基因名仅存在于图版/补充表（Supplementary Table 1/4），review_md 不可恢复。

### D2 marker 归属核对（Ngfr 型错误）——流式抗体面板系统性错挂清理

Methods 血免疫细胞流式面板（CD3/CD4/CD8/CD14/CD19/CD47/CD56/CD235a，L590-595 + Antibodies 段）中 CD19/NCAM1/CD4/CD14/ITGAM/CCR3 被批量挂到非归属细胞。错位行移除清单（正确归属细胞已有对应行）：

| marker_id | 错误归属 | 正确归属（已有行） |
|---|---|---|
| M00147 | B cells/CD14 | classical monocytes（M00168） |
| M00150 | B cells/CD4 | CD4+ T cells（M00162） |
| M00152 | B cells/NCAM1 | NK（M00199/M00203） |
| M00155 | basophils…/CD14 | classical monocytes（M00168） |
| M00156 | basophils…/CD19 | B cells（M00148） |
| M00159 | basophils…/NCAM1 | NK（M00199/M00203） |
| M001197→M00197 | natural killer cells/CD14 | classical monocytes（M00168） |
| M00198 | natural killer cells/CD19 | B cells（M00148） |
| M00200 | NK cells/CD14 | classical monocytes（M00168） |
| M00201 | NK cells/CD19 | B cells（M00148） |
| M00202 | NK cells/CD4 | CD4+ T cells（M00162） |
| M00204 | pDCs,mDCs,CD16+ DCs/CCR3 | basophils/eosinophils（M00154） |
| M00205 | pDCs…/CD14 | classical monocytes（M00168） |
| M00206 | pDCs…/CD19 | B cells（M00148） |
| M00211 | pDCs…/NCAM1 | NK（M00199/M00203） |
| M00217 | T cells/CD14 | classical monocytes（M00168） |
| M00218 | T cells/CD19 | B cells（M00148） |
| M00220 | T cells/ITGAM | 髓系（本文无髓系 ITGAM 行；ITGAM/CD11b 为髓系 marker，T cells 挂载错误） |
| M00221 | T cells/NCAM1 | NK（M00199/M00203） |

保留的流式行（归属正确的）：M00148 (B/CD19)、M00149 (B/CD27)、M001151→M00151 (B/MS4A1)、M00154 (baso/CCR3)、M00157 (baso/IL3RA)、M00158 (baso/ITGB7)、M00162 (CD4+T/CD4)、M00168 (cMono/CD14)、M00199 (NK/NCAM1)、M00203 (NK cells/NCAM1)、M00207 (DC/CD1C)、M00208 (pDC/CD4)、M00209 (pDC/IL3RA)、M00210 (DC/ITGAX)、M00216 (T/CCR7)、M00222 (T/PTPRC)、M00223 (T/SELL)。

**用途问题（记录，供批次报告/用户决策，本轮不动）**：上述流式行均来自血免疫细胞 FACS 染色步骤（验证/分选用途），非 cluster 注释面板。本轮仅修归属错位；是否全量清理此类行超出本批候选范围。

### D2b 其他归属修正

- **M00160 MYC/Bronchial endothelial cell → 移除并补录正确归属**。EDF3k 图注（重组）："smFISH for general endothelial marker CLDN5 (red, centre), bronchial vessel-specific markers MYC (green) and Bro1-specific marker ACKR1 (red, right) on serial sections of bronchial vessel cells (arrowheads)…"。MYC 是 bronchial vessel（Bro1/Bro2）specific marker 而非泛支气管内皮 marker。新行：MYC/Bronchial vessel cells/author_declared/Extended Data Fig.3k legend。

### D3 物种一致性
本篇为 human。发现鼠式写法行（图注原始拼写所致），处置见 D5。

### D4 跨篇一致性
AdvF/AlvF/DC 等命名与四层分类映射在批次层面统一处理，本篇无跨篇冲突发现。

### D5 基因写法核对（拼写变体合并与修正）

| marker_id | 现值 | 处置 | 依据 |
|---|---|---|---|
| M00121 | Pi16 (EDF4d) | **移除（拼写变体重复）** | 修正后与 M00118 (Adventitial fibroblast/PI16) 同键；EDF4 图注 "fibroblast-selective markers Pi16 (white) and Serpinf1 (red)" 措辞并入 M00118 升级依据 |
| M00122 | Serpinf1 (EDF4d) | **移除（拼写变体重复）** | 与 M00119 (AdvF/SERPINF1) 同键 |
| M00130 | Fgfr4 (EDF4b) | **移除（拼写变体重复）** | 与 M00127 (AlvF/FGFR4) 同键；EDF4b "alveolar fibroblast-selective markers Slc7a10 (white) and Frfr4 (red)" 中 Frfr4 为 Fgfr4 之图注拼讹 |
| M00131 | Slc7a10 | **拼写修正 SLC7A10 + 升级 author_declared** | 人基因全大写规范；EDF4b "alveolar fibroblast-selective markers Slc7a10" marker 措辞 |
| M00192 | Eln | **拼写修正 ELN** | 人基因全大写；维持 figure_labeled |

### D6 标签统一（AT2 / AT2-signalling 标签分裂）

历史提取造成同一细胞类型两种标签写法。处置：
- M00140 AT2 → cell_type 改 **Alveolar type 2 (AT2)**（MUC1 无键冲突）
- M00141 AT2/SFTPC (Fig.4d) → 与 M00137 (Alveolar type 2 (AT2)/SFTPC, Fig.1d) 统一标签后同键 → **移除 M00141（保留 M00137 并升级）**；Fig.4d 图注 "probed for COPD or emphysema gene SERPINA1 and AT2 marker SFTPC" 的 marker 措辞并入 M00137 升级依据
- M00142、M00143 AT2-signalling (AT2-s) → cell_type 改 **AT2-signalling cell (AT2-s)**（与 M00144-146 一致；无键冲突）
- M00143 (WIF1/negative) 保留：图注 "AT2-signalling cells (SFTPC+ WIF1−)" 支持其阴性区分特征（polarity=negative 合法）

### D7 D 门顺带升级（图注/正文明确 marker 措辞，证据句已重组核实）

| marker_id | gene | cell_type | 升级依据原句 | locator |
|---|---|---|---|---|
| M00118 | PI16 | Adventitial fibroblast | EDF4 图注："…fibroblast-selective markers Pi16 (white) and Serpinf1 (red)…"（adventitial fibroblast 探针） | Extended Data Fig.4d legend |
| M00119 | SERPINF1 | Adventitial fibroblast | Fig.1f 图注（重组）："…adventitial fibroblast marker SERPINF1 (red, right)…" | Fig.1f legend; Extended Data Fig.4d legend |
| M00128 | GPC3 | Alveolar fibroblast | Fig.1f 图注（重组）："…alveolar fibroblast marker GPC3 (red, left)…" | Fig.1f legend |
| M00131 | SLC7A10 | Alveolar fibroblast | EDF4b："alveolar fibroblast-selective markers Slc7a10 (white) and Frfr4 (red)" | Extended Data Fig.4b legend |
| M00137 | SFTPC | Alveolar type 2 (AT2) | Fig.1d 图注："…shared AT2 and AT2-signalling marker SFTPC (white) and specific AT2 marker WIF1 (red puncta)."；Fig.4d："…AT2 marker SFTPC…" | Fig.1d legend; Fig. 4d legend |
| M00138 | WIF1 | Alveolar type 2 (AT2) | 同上句 "specific AT2 marker WIF1"；EDF3i："AT2 selective markers include … HHIP and WIF1, highlighted red" | Fig.1d legend; Extended Data Fig.3i legend |
| M00142 | SFTPC | AT2-signalling cell (AT2-s)（标签修正后） | "shared AT2 and AT2-signalling marker SFTPC" | Fig.1d legend |
| M00144 | LRP5 | AT2-signalling cell (AT2-s) | EDF3i："AT2-signalling selective markers include Wnt ligands, receptors and transcription factors (for example, WNT5A, LRP5 and TCF7L2 highlighted green)." | Extended Data Fig.3i legend |
| M00145 | TCF7L2 | AT2-signalling cell (AT2-s) | 同上 | Extended Data Fig.3i legend |
| M00146 | WNT5A | AT2-signalling cell (AT2-s) | 同上 | Extended Data Fig.3i legend |
| M00153 | KRT5 | Basal cell | EDF3e："…basal cells (marked by KRT5, red)…"；EDF3g："…basal marker KRT5…" | Extended Data Fig.3e legend |
| M00161 | ACKR1 | Bronchial vessel 1 cell (Bro1) | EDF3k："…Bro1-specific marker ACKR1 (red, right)…" | Extended Data Fig.3k legend |
| M001174→M00174 | GPR183 | Dendritic cell (general) | EDF4m："…general dendritic cell marker GPR183 (white) (m)…" | Extended Data Fig.4m legend |
| M00185 | GPR34 | IGSF21+ dendritic cell | EDF4l："…cell markers IGSF21 (red) and GPR34 (white) (l)…" | Extended Data Fig.4l legend |
| M00195 | FGF18 | Myofibroblast | "One cluster (WIF1+FGF18+ASPN+) is classical myofibroblasts…" | Results §New lung cell types |
| M00225 | CHI3L1 | TREM2+ dendritic cell | EDF4n："…TREM2+ dendritic cell markers TREM2 (red) and CHI3L1 (white) (n)…" | Extended Data Fig.4n legend |

（另：M00182 ASPN/Fibromyocyte 同 EDF4f "myofibroblast and fibromyocyte marker ASPN" 措辞 → 顺带升级；M00212 COX4I2/Pericyte 依 EDF5d "pericyte marker COX4I2" → 顺带升级。M00190 APOE/Lipofibroblast 仅 "Pericyte and lipofibroblast marker staining" 泛述无点名措辞，维持 figure_labeled。）

## 归属修正明细

| marker_id | 错误归属 | 正确归属 | 证据 |
|---|---|---|---|
| M00160 | Bronchial endothelial cell/MYC | Bronchial vessel cells/MYC（新行补录，author_declared） | EDF3k "bronchial vessel-specific markers MYC (green)…on serial sections of bronchial vessel cells" |

## 整簇漏提明细（漏提-待图版核对留档，本轮不落表）

| cell_type | markers | 状态 |
|---|---|---|
| Ionocyte | 基因名仅在图版/补充表（MC1R 为激素受体描述非 marker） | 待图版核对 |
| Club | SCGB1A1 等（review_md 0 命中） | 待图版核对 |
| Mucous (Muc) | 仅缩写清单 | 待图版核对 |
| Mesothelial (Meso) | 仅缩写清单 | 待图版核对 |
| Bronchial vessel 2 cell (Bro2) | 仅缩写清单 | 待图版核对 |
| Capillary 系列（Cap/Cap-a/Cap-i1/Cap-i2） | "expressed capillary markers" 泛述无基因名 | 待图版核对 |
| Vascular smooth muscle (VSM) | 仅缩写清单 | 待图版核对 |
| Bas-d / Bas-p | 状态亚群 | 待图版核对 |

## 计数（供落表脚本与批次报告）

- 补录：8 条（MUC5B、MUC5AC、LTF、LYZ、BPIFBP1、HP、PLVAP、MYC归属补录）
- 升级：B 门 10（M00120/127/129/133/135/180/184/194/196/224）+ D 门顺带 18（M00118/119/128/131/137/138/142/144/145/146/153/161/174/182/185/195/212/225）= 28 条
- 移除：34 条 = 流式错位 19（M00147/150/152/155/156/159/197/198/200/201/202/204/205/206/211/217/218/220/221）+ C 门错位/重复 7（M00164/165/166/167/169/170/219）+ 双标签重复 3（M00171/172/173）+ 拼写变体重复 3（M00121/122/130）+ 标签分裂重复 1（M00141）+ 归属移除 1（M00160）
- 标签修正：3（M00140/142/143）
- 拼写修正：2（M00131→SLC7A10、M00192→ELN）
- 维持不录：A 门 26（含自动噪声 19）+ B 门 0
- 总表行数：113 → 87
