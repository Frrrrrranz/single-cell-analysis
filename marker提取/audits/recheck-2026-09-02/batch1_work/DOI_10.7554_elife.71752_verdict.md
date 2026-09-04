# DOI_10.7554_elife.71752 复核判定报告

论文：Nguyen MQ et al., Single-nucleus transcriptomic analysis of human dorsal root ganglion neurons, eLife 2021;10:e71752（人 DRG 神经元 snRNA-seq 图谱 + 小鼠 Renthal 数据跨物种对比）
复核人：marker 复核专家（Batch 1，2026-09-02）
原文：D:\OneDrive\Desktop\组\marker提取\review_md\DOI_10.7554_elife.71752.md（引文后括注 review_md 行号 L，便于复核；引文中 "X- y" 类连字符空格为 PDF 换行伪影，已按语义最小归并，如 "voltage- gated"→"voltage-gated"，未改动任何词）

## 摘要

本篇判定统计（elife.71752）：
- **补录 8**（A 门候选命中）：NTRK3、TAC1、MRGPRX1、PRP1、MBP、QKI、LPAR1、APOE
- **升级 0**（B 门 6 条全部维持：M00005–M00009 维持 annotation_marker，M00010 维持 figure_labeled）
- **恢复 0**；**移除 0**；**归属修正 0**（现有 10 行归属均成立；候选材料侧 2 处归属失准在 A 门内处理为不录）
- **维持不录 10**（A 门：噪声 token 7 条——NP1/NP2/NP3/H10/H12/DRG/ISH；转述背景无本文注释用途 3 条——Mrgpra3/Etv1/TRPC3）
- **D 门对账追加补录建议 8 + 中等置信 3**（A 门候选之外新发现：SCN1A、PVALB、NEFH(H15)、PIEZO2(H15)、SCN10A(H4)、NTRK1(H4)、PIEZO2(H10)、SST(H11)；中等置信：CALCA、CALCB、ADCYAP1）
- **D 门确认"疑似大幅漏提"成立**：总表 10 行仅覆盖 15 个细胞群中的 5 个（H3/H6/H10/H11 + QC 层 human DRG neurons）；人神经元 14 个命名簇中 10 簇整簇漏提 + 非神经元细胞群整体漏提（详见"整簇漏提明细"）

试点遗留处置（PMID_35115729，见文末专节）：**升级 1**（M01516 Pdgfra→author_declared）、**维持 1**（M01517 Cd34 维持 annotation_marker）。

---

## A 门逐条判定

| # | 候选基因 | 判定 | cell_type | gene_symbol | species | evidence_type | source_locator | 原句（完整） | 理由 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | NTRK3 | **补录** | H12（human-specific，putative mechanosensor 类） | NTRK3 | human | author_declared | Results p.6，Figure 2B 段落（review_md L222-224） | "A second larger group of human neurons H12 is marked by NTRK3 and the voltage-gated ion channel SCN1A, but is only weakly positive for NEFH, expresses moderate levels of PIEZO2 (Figure 2B, Figure 1—figure supplement 5) and appears distinct from any potential mouse counterpart." | "is marked by NTRK3" 为明确 marker 措辞，H12 为本文自有人簇，NTRK3 参与该簇的识别与描述（图 2B/supp.5 展示）。双重门槛均满足。注意同句 SCN1A 同为 "marked by" 对象（见 D 门追加建议） |
| 2 | MBP | **补录** | non-neuronal cells（human DRG，QC 层界定群） | MBP | human | author_declared | Methods: Single nuclear capture, sequencing, and data analysis（p.16，review_md L709-712） | "Clusters not expressing high levels of neuronal or somatosensory genes like SNAP25, SCN9A, SCN10A, PIEZO2, NEFH, etc. but instead expressing elevated levels of markers of non-neuronal cells including PRP1, MBP, QKI, LPAR1, and APOE were tagged as non-neuronal and were removed to allow reclustering of 'purified' human DRG neurons." | 关键辨析：句中名词短语为 "markers of non-neuronal cells including PRP1, MBP, QKI, LPAR1, and APOE"——是 marker 身份措辞，非单纯富集措辞（"elevated levels of" 只是量词）；且该 marker 列表直接用于非神经元簇的识别/标记（"were tagged as non-neuronal"），注释用途成立 |
| 3 | APOE | **补录** | non-neuronal cells | APOE | human | author_declared | 同上（L709-712） | 同上 | 同上 |
| 4 | NP1 | 不录-噪声 | — | — | — | — | Results p.6（L249） | "one (NP1, expressing Mrgprd) responds to noxious mechanical stimulation" | NP1 为小鼠簇名（Renthal 命名体系），非基因 |
| 5 | DRG | 不录-噪声 | — | — | — | — | Figure supplement 标题（L124） | "Additional markers that support similarities between dorsal root ganglia (DRG) neuronal clusters across species." | DRG 为组织名（dorsal root ganglia 缩写），非基因 |
| 6 | TAC1 | **补录** | peptidergic nociceptors（putative；覆盖 H1/H2/H3/H5/H6） | TAC1 | human | author_declared | Results p.10, Figure 5A 图注；并见 Results p.6（review_md L396-397, L256-270） | "Peptidergic nociceptors marked by expression of TAC1 (blue) and additional SCN10A-positive cells are also present in this region of the ganglion."（Fig 5A 图注）；主文另证："one clear expectation is that TAC1, NEFH, and OSMR should be expressed by distinct and only partially overlapping populations of human DRG neurons. If it is also comprehensive, … then we would anticipate that the same three markers should label the vast majority of neurons. … Finally, these three markers each labeled a large group of neurons (Figure 2—figure supplement 1)."（L256-270） | 作者两处明确以 marker 措辞呈现 TAC1：图注 "Peptidergic nociceptors marked by expression of TAC1"（与现有 OSMR 行 "identified by their expression of OSMR" 结构对应）；主文 "the same three markers"（TAC1/NEFH/OSMR）。类别归属（peptidergic nociceptor）亦源于 TAC1/CALCA/CALCB/ADCYAP1 表达（L131-133 + L145 "peptidergic markers"）。注释用途成立 |
| 7 | NP3 | 不录-噪声 | — | — | — | — | Results p.11（L417） | "Both these genes are prominent markers of NP3 pruriceptors in mouse (Figure 5B)." | NP3 为小鼠簇名，非基因 |
| 8 | Mrgpra3 | 不录 | — | — | mouse | — | Figure 5B 图注（L398-399）；Discussion p.12（L498-499） | "MRGPRX1 is the human chloroquine receptor and the functional equivalent of Mrgpra3, which in mice marks NP2 cells."；"Moreover, in mice, Mrgpra3 (the functional equivalent of MRGPRX1) marks the distinct NP2 neurons." | 有 "marks" 措辞但属转述小鼠已知知识（Mrgpra3→NP2 来自 Han et al. 2013/Renthal 2020 体系）。本文未对小鼠簇做注释（小鼠标签整体借自 Renthal et al. 2020，见 D 门第 1 项），Mrgpra3 未参与本文自身任何细胞群的识别/命名/归类 → 注释用途门槛不满足 |
| 9 | Etv1 | 不录 | — | — | mouse | — | Results p.4（L152-156） | "In mice, proprioceptors are a subtype of Aβ neurons marked by the calcium binding protein parvalbumin, the transcription factor Etv1 and the voltage-gated sodium channel subunits Scn1a and Scn1b (Sharma et al., 2020; Renthal et al., 2020). In the human data, the small H15 group of NTRK3-positive cells had this expression pattern (Figure 1C, Figure 1—figure supplement 5) implying that proprioceptors have conserved transcriptomic markers in humans and mice." | ① 该句为转述小鼠先前文献（Sharma 2020 / Renthal 2020）的背景句，被 mark 的对象是小鼠 proprioceptors；② 候选材料将 cell_type 写作 "Aβ 神经元" 属归属失准——原文 "proprioceptors are a subtype of Aβ neurons marked by…"，marked 的主语是 proprioceptors 而非泛 Aβ 神经元；③ 本文 H15 的识别句另有 NEFH/PIEZO2/PVALB（"distinguished by their expression of"，见 D 门），Etv1 未作为本文注释 marker 呈现 |
| 10 | H12 | 不录-噪声 | — | — | — | — | Results p.6（L222） | "A second larger group of human neurons H12 is marked by NTRK3 and the voltage-gated ion channel SCN1A…" | H12 为人簇名，非基因 |
| 11 | ISH | 不录-噪声 | — | — | — | — | Figure 4 图注（L362-363） | "Confocal images of sections through a human DRG probed for expression of key markers using multiplexed in situ hybridization (ISH); …" | ISH 为方法名（in situ hybridization），非基因 |
| 12 | NP2 | 不录-噪声 | — | — | — | — | Figure 5B 图注（L398-399） | "…the functional equivalent of Mrgpra3, which in mice marks NP2 cells." | NP2 为小鼠簇名，非基因 |
| 13 | TRPC3 | 不录 | — | — | mouse | — | Figure 5B 图注（L399-400） | "Note that coexpression patterns of SST and JAK1 in H11 neurons resembles their expression in mouse NP3 pruriceptors but the ion channel TRPC3 which also marks these cells is primarily expressed in mouse NP1 neurons; …" | "which also marks these cells" 的宾语为小鼠 NP3 pruriceptors（转述先前知识的插注），非本文注释对象；TRPC3 未参与本文任何细胞群注释 → 注释用途门槛不满足 |
| 14 | H10 | 不录-噪声 | — | — | — | — | Discussion p.12（L487） | "…designates cLTMRs as a subset of cells resembling H10 neurons that appear to have lower expression of some pruriceptive markers." | H10 为人簇名，非基因 |
| 15 | MRGPRX1 | **补录** | H10（nonpeptidergic nociceptor / candidate pruriceptor） | MRGPRX1 | human | figure_labeled | Results p.11；Figure 5B（review_md L413-414, L397-399） | "For example, although not prominently expressed, the human chloroquine responsive receptor MRGPRX1 (27) localized selectively to H10 neurons (Figure 5B) perhaps suggesting a relationship to mouse NP2 cells."；Figure 5B 图注："Universal manifold (UMAP) representation of mouse and human DRG neurons showing relative expression level (blue) of genes that distinguish H10 and H11 and mark specific sets of mouse NP1–3 neurons." | 主文为选择性定位措辞（"localized selectively to H10 neurons"），但 Figure 5B 图注明确该图基因为 "genes that distinguish H10 and H11"，MRGPRX1 为其中 H10 侧基因——与现有 M00010（JAK1/H11/figure_labeled）证据基础完全同源，按同口径收录为 figure_labeled |
| 16 | PRP1 | **补录** | non-neuronal cells | PRP1 | human | author_declared | Methods（L709-712） | 同候选 2 原句 | 拼写核实：review_md 全文 "PRP1" 仅出现 1 次（L711），无 "PRPH"/"peripherin" 字样——原文即写作 PRP1（疑为人 peripherin/PRPH 的非规范写法），按规范**保留原文拼写 PRP1**，建议行内加注"原文如此，疑指 PRPH"。marker 措辞与注释用途同候选 2 |
| 17 | QKI | **补录** | non-neuronal cells | QKI | human | author_declared | Methods（L709-712） | 同候选 2 原句 | 同候选 2 |
| 18 | LPAR1 | **补录** | non-neuronal cells | LPAR1 | human | author_declared | Methods（L709-712） | 同候选 2 原句 | 同候选 2 |

---

## B 门逐条判定

| marker_id | gene | cell_type | 判定 | 完整原句 | 理由 |
|---|---|---|---|---|---|
| M00005 | NEFH | human DRG neurons | **维持（不升级，annotation_marker）** | "Clusters not expressing high levels of neuronal or somatosensory genes like SNAP25, SCN9A, SCN10A, PIEZO2, NEFH, etc. but instead expressing elevated levels of markers of non-neuronal cells including PRP1, MBP, QKI, LPAR1, and APOE were tagged as non-neuronal and were removed to allow reclustering of 'purified' human DRG neurons."（Methods, L709-712） | 句中 "markers of …" 措辞指向 PRP1/MBP/QKI/LPAR1/APOE（已作 A 门补录，挂 non-neuronal cells），**与 NEFH 无关**；NEFH 等在句中仅被称为 "neuronal or somatosensory genes"（QC 过滤例举基因），无 marker 措辞 → 升级不成立。归属可辩护：这些基因的高表达是界定"神经元簇"（保留为 'purified' human DRG neurons）的 QC 依据，且 Figure 1A 图注 "a dotplot highlights the expression of markers that help distinguish these groups of cells"（神经元 vs 非神经元，L110-113）为其提供图级支撑（dotplot 具体基因清单不在 review_md 内，无法逐基因核验）→ 维持 annotation_marker，不升级亦不降级 |
| M00006 | PIEZO2 | human DRG neurons | **维持（不升级，annotation_marker）** | 同上 | 同上（"markers of" 措辞不指向 PIEZO2；PIEZO2 在句中为 "somatosensory genes" 例举） |
| M00007 | SCN10A | human DRG neurons | **维持（不升级，annotation_marker）** | 同上 | 同上 |
| M00008 | SCN9A | human DRG neurons | **维持（不升级，annotation_marker）** | 同上 | 同上 |
| M00009 | SNAP25 | human DRG neurons | **维持（不升级，annotation_marker）** | 同上 | 同上 |
| M00010 | JAK1 | H11 | **维持（不升级，figure_labeled）** | "By contrast, Janus kinase 1 (JAK1), a mediator of itch through various types of cytokine signaling, including through OSMR (Oetjen et al., 2017), and the neuropeptide SST are particularly strongly expressed in H11 cells (Figure 5B). Both these genes are prominent markers of NP3 pruriceptors in mouse (Figure 5B)."（Results p.11, L414-417） | H11 语境下 JAK1 只有富集措辞（"particularly strongly expressed in H11 cells"）；"prominent markers" 措辞的宾语是**小鼠 NP3 pruriceptors**（且为转述先前知识），不指向 H11 → author_declared 升级不成立。Figure 5B 图注 "genes that distinguish H10 and H11" 支持 H11 的图级区分角色 → 现有 figure_labeled 定级恰当，维持。（同句 SST 与 JAK1 同理，SST 的 H11 收录建议见 D 门追加，定级 figure_labeled） |

**B 门总体结论**：6 条候选均不升级。核心原因：该 Methods 句的 marker 措辞归属 PRP1/MBP/QKI/LPAR1/APOE（非神经元侧），NEFH 等 5 基因是 QC 过滤例举；JAK1 的 marker 措辞归属小鼠 NP3（转述背景）。M00005–M00009 的 "human DRG neurons" 归属（QC 界定层级）成立，不建议移除。

---

## B2 逐条判定

无 B2 补充候选（0 条）。

## C 门逐条判定

无 C 门候选（0 条）。人工补充检查：NEFH 在现表中出现于 H3/H6（M00001/M00002，author_declared，簇级）与 human DRG neurons（M00005，annotation_marker，QC 泛神经元层）——两者细胞层级与证据用途不同（簇级标记 vs 神经元/非神经元 QC 界定），**不构成语义重复，不合并**。若采纳 D 门 H15 补录建议，NEFH 将新增第 4 个 cell_type 行（H15），同理独立。

---

## D 门检查结论

### 1. 聚类对账（核心项）

**论文报告的细胞类型清单**（从原文提取）：

人 DRG 神经元（reclustering 1837 神经元核，"a range of about a dozen diverse transcriptomic classes"，L104-106）——正文具名共 **14 簇**（H1–H6、H8–H15；**H7 全文未出现**）：
- H1、H2、H5：c-type peptidergic nociceptors（L317-318）
- H3、H6：putative peptidergic/Aδ nociceptors（L143-146）
- H4：c-nociceptors（L226-228）
- H8：cool responsive neurons（L157-159）
- H9：human-specific cool+mechanosensory（L190-191）
- H10、H11：nonpeptidergic nociceptor / candidate pruriceptor（L231-241）
- H12：human-specific，NTRK3/SCN1A 标记的 putative mechanosensor 类（L222-225）
- H13：AδLTMRs（L157-159, L293）
- H14：Aβ cells（L147-150, L293）
- H15：proprioceptors（L155-156, L341-342）

非神经元细胞：**仅 1 个未细分群**（"non-neuronal cells"，于 QC 中被整体标记并剔除，L709-712）。**注意：本文并未对非神经元细胞做亚型注释——不存在施万细胞/成纤维细胞等具名亚簇**（任务材料中"胶质细胞/施万细胞/成纤维等"的预期不适用于本篇；这些内容属 PMID_35115729 等其他篇目）。

小鼠簇：标签整体**借自 Renthal et al. 2020**（NP1/NP2/NP3/cLTMRs/c-peptidergic/Aβ/Aδ/proprioceptors/Trpm8 cells 等；supplement 分析中 "19 clusters of mouse neurons were now analyzed"，L325-327）。本文对小鼠数据只做重聚类展示与对比（L728-737），**未做 de novo 注释**，小鼠簇名及其 marker 关系均为转述。

**对账结论**：总表 10 行的 cell_type 去重 = {H3, H6, H10, H11, human DRG neurons} = 5 个群。对照 15 个应有细胞群（14 个人神经元簇 + 1 个非神经元群），**覆盖 5/15，10 个簇 + 非神经元群整簇漏提**。D 门此前标注"疑似大幅漏提"**确认成立**。小鼠参考簇按上文口径不列入漏提（本文未对其注释）。

另注：NeuN（RBFOX3 蛋白）用于神经元核富集（"samples were enriched for neuronal nuclei by selection using an antibody to NeuN"，L98-99；"IHC analysis (Figure 1—figure supplement 1) supports the use of NeuN enrichment as a means to purify human DRG neurons"，L675-677）——属**方法学/试剂 marker（抗体富集）**，按规范不录；ISH 探针面板（NEFH/TRPM8/PIEZO2/SCN10A/NTRK2/TAC1/OSMR/SST/TRPV1/PVALB/NPPB/HRH1）虽有 "we identified a range of potential markers to better explore the diversity of human DRG neurons"（L332-335）的 panel 级措辞，但 "potential markers" 为探索性措辞且各基因细胞归属须逐句核实，故未按"面板整体收录"规则盲收，仅对逐句达标者补录（结果见下）。

### 2. marker 归属核对

- M00001/M00002（NEFH→H3/H6）：核对 L143-146 "this gene showed graded expression in our data (Figure 1C) and marks several classes of cells just as in mice… Some of these (including H3 and H6) also express peptidergic markers and the pain-related voltage-gated sodium channel SCN10A… and thus have molecular hallmarks of Aδ nociceptors" —— NEFH 标记的 "several classes" 同时包含 H3/H6（Aδ 分支）与 H14/H15（最高表达，Aβ/proprioceptor 分支）；行挂 H3/H6 成立。**发现**：NEFH 标记句覆盖的 H14/H15 侧无行（漏提，但该侧仅有富集措辞，见整簇漏提明细）。
- M00003/M00004（OSMR→H10/H11）：L357-358 "the H10 and H11 classes of neurons, identified by their expression of OSMR" —— 归属成立。
- M00005–M00009（SNAP25 等→human DRG neurons）：QC 界定层级归属成立（详见 B 门）。
- M00010（JAK1→H11）：图级区分归属成立（详见 B 门）。
- 无 Ngfr 型归属错误。候选材料侧 2 处归属失准（Etv1 误挂 "Aβ 神经元"——实为 proprioceptors 亚型；TRPC3 "marks these cells" 误指 H11——实为小鼠 NP3）均已在 A 门判不录，未产生错误行。
- 小误（不影响判定）：现有行 locator 页码与 review_md 页码不完全一致（如 OSMR 句实位于 review_md p.8，行内标 p.6），属提取时页码换算差异，建议下次批量校正。

### 3. 物种一致性

现有 10 行 species=human，与论文主对象（人 DRG）一致；小鼠数据为 Renthal 重分析，本文未对小鼠簇注释，故不应有 mouse 行——现有行无物种错误。新增补录行全部为 human 语境（NTRK3/SCN1A/TAC1/MRGPRX1/PVALB/SCN10A/NTRK1/PIEZO2/SST/PRP1/MBP/QKI/LPAR1/APOE/CALCA/CALCB/ADCYAP1），species=human。

### 4. 基因写法核对

- **PRP1**：原文实际拼写为 "PRP1"（review_md 仅 L711 一处，全文无 PRPH/peripherin）——按规范保留原文拼写，不静默修正，建议加注"疑为 PRPH（peripherin）的非规范写法"。
- 其余候选与新增基因拼写正常（人基因全大写，与原文一致；Mrgpra3/Etv1/Scn1a/Scn1b/Mrgprd/Nppb 等鼠式写法仅出现于小鼠背景句，均未收录）。
- NP1/NP2/NP3/H10/H12/DRG/ISH 等非基因 token 已在 A 门按噪声排除。

### 5. 跨篇一致性

- NTRK3（补录）与 DOI_10.1016_j.cell.2022.11.005 已收录行同名一致；MBP 与 PMID_35115729（Mbp, mSC）/DOI_10.1038_s41588-022-01243-4 跨物种同名一致；APOE 与多篇一致——无命名冲突。
- H 簇命名（H1–H15）为本篇特有标签；NP1–NP3 为 Renthal 体系——建议 four_layer_category 归类时：人神经元簇（含 peptidergic/Aδ/Aβ/proprioceptor/itch 类）按项目四层口径归 L1/L2，non-neuronal cells 行归 L3，与试点篇（PMID_35115729）成纤维/Schwann 行口径对齐。

---

## 归属修正明细

无（现有 10 行无需归属修正；候选侧失准已在 A 门处理）。

---

## 整簇漏提明细

人 DRG 神经元 14 个具名簇中 10 簇无行 + 非神经元群无行。逐簇判定如下（"建议动作"按双重门槛）：

| cell_type（作者标签） | markers | 证据 locator + 原句 | 判定/建议动作 |
|---|---|---|---|
| H1、H2、H5（c-type peptidergic nociceptors） | TAC1（组级） | Results p.10, Figure 5A 图注（L396-397）："Peptidergic nociceptors marked by expression of TAC1 (blue) and additional SCN10A-positive cells are also present in this region of the ganglion."；L131-133："In the human DRG dataset, TAC1 (substance P), CALCA and CALCB (CGRP), and ADCYAP1 (PACAP), are expressed in several transcriptomic classes (H1, H2, H3, H5, and H6, Figure 1C…)"；L317-318："several groups of human cells (H1, H2, and H5) that gene expression predicted should be c-type peptidergic nociceptors, indeed best matched these cells (Figure 3B)." | **补录 TAC1 → peptidergic nociceptors（组级行，覆盖 H1/H2/H3/H5/H6），author_declared**（A 门候选 6）。另：CALCA/CALCB/ADCYAP1 经 L145 "Some of these (including H3 and H6) also express peptidergic markers…" 回指 + Figure 1C "diagnostic markers"（图注 L114-119："UMAP representation of human DRG neurons showing relative expression level (blue) of diagnostic markers… the expression patterns of these and other genes… were used to tentatively match several human and mouse transcriptomic classes"）——**建议补录（中等置信，marker 措辞为回指性）**，evidence_type author_declared |
| H4（c-nociceptors） | SCN10A、NTRK1（正）、NEFH（低） | Results p.6（L226-228）："Similarly, we designated H4 as c-nociceptors because of their expression of nociception-related SCN10A and NTRK1 and low level of NEFH (Figure 2B, Figure 1—figure supplement 5)." | **建议补录 SCN10A、NTRK1 → H4，annotation_marker**（"designated … because of their expression of" 为该簇命名依据句；无 marker 字样故不判 author_declared。置信中等偏高） |
| H8（cool responsive neurons） | TRPM8（富集措辞，无 marker 措辞） | L209-210："…segregates from the putative cool sensing cells (H8) that express TRPM8, GPR26, NTM, and FOXP2…"；L337-339："TRPM8, the cool and menthol receptor is not coexpressed with the ion channels SCN10A or PIEZO2 (Figure 4A), but unlike in mice these cells are NTRK2 positive." | **漏提簇，但无可补录行**：全文对 H8 及其基因仅 "express/expressing/positive" 富集措辞，无 marker 措辞（按边界规则不收录）。如项目要求簇覆盖完整，只能依赖 Figure 1C/supp.4/5 图级 dotplot（基因清单不在 review_md，无法核验）——建议保留为审计记录 |
| H9（human-specific cool+mechanosensory） | TRPM8、PIEZO2、SCN10A、SCN11A（富集措辞） | L190-191："One small but prominent group of human DRG neurons (H9) expresses TRPM8, PIEZO2, SCN10A, and SCN11A (Figure 1—figure supplements 4 and 5, Figure 2B)…" | **漏提簇，但无可补录行**（同上，仅 "expresses" 措辞；Figure 2B 图注亦仅 "their expression of key genes"） |
| **H12（human-specific putative mechanosensor 类）** | NTRK3、SCN1A | Results p.6（L222-224）："A second larger group of human neurons H12 is marked by NTRK3 and the voltage-gated ion channel SCN1A, but is only weakly positive for NEFH, expresses moderate levels of PIEZO2 (Figure 2B, Figure 1—figure supplement 5) and appears distinct from any potential mouse counterpart." | **补录 NTRK3 → H12（A 门候选 1，author_declared）+ 追加补录 SCN1A → H12（D 门新发现，同句 "marked by" 双对象，author_declared）** |
| H13（AδLTMRs） | 无具名基因 | L157-159："Similarly, small groups of both Aδ-low threshold mechanosensors (H13) and cool responsive neurons (H8) were identified by their characteristic expression profiles of functionally important transcripts (Figure 1—figure supplement 5)." | **漏提簇，无可补录行**：识别句未具名任何基因；文本层无法给出 marker 行 |
| H14（Aβ cells） | NEFH（最高表达，富集措辞）、NTRK3（positive 措辞） | L147-152："However, the neuronal classes H14 and H15 expressing the highest levels of NEFH are distinct from the peptidergic neurons…, likely representing different types of large diameter, fast conducting myelinated Aβ neurons. These cell types are neurotrophin three receptor NTRK3 positive, some also contain the brain derived neurotrophic factor receptor NTRK2 but exhibit little expression of NTRK1…" | **漏提簇，无可补录行**（仅 "expressing the highest levels of…/NTRK3 positive" 富集措辞） |
| **H15（proprioceptors）** | PVALB、NEFH、PIEZO2（正）、NTRK2（负） | Results p.8（L341-342）："Similarly, putative proprioceptive neurons (H15) were distinguished by their expression of NEFH, PIEZO2, and PVALB and lack of NTRK2 (Figure 4B, Figure 4—figure supplement 1)."；Figure 4B 图注（L366-367）："Putative proprioceptors, highlighted by double arrowheads, expressing PIEZO2 (green) and PVALB (red), but not NTRK2 (blue) were typically highly clustered in the ganglion." | **建议补录 PVALB、NEFH、PIEZO2 → H15（putative proprioceptive neurons），annotation_marker**（"distinguished by their expression of" 主文识别句 + Figure 4B；与现有 OSMM 行 "identified by their expression of" 同级定类。NEFH/PIEZO2 为同基因不同 cell_type 新行，不与现有行冲突。NTRK2 可作 negative polarity 行酌情补录） |
| H10、H11（nonpeptidergic nociceptor / candidate pruriceptor） | 现有：OSMR（两簇）、JAK1（H11）；缺：PIEZO2（H10）、SST（H11）、MRGPRX1（H10） | ① Results p.11（L421-422）："H10 cells are also distinguished from H11 and mouse pruriceptors by their prominent expression of the stretch-gated ion channel PIEZO2 (Figure 1C, Figure 2—figure supplement 2)."；② Figure 5C 图注（L401-403）："…probed for expression of genes that distinguish H11 (SST, blue) from H10 cells (PIEZO2, green)…"；③ Results p.11（L433-434）："Multiplexed ISH showed that SST divides the OSMR-positive cells into two intermingled types (Figure 5C)…" | 非整簇漏提（两簇已有行），但**区分性 marker 缺失**：**建议补录 PIEZO2 → H10（annotation_marker，句①" distinguished by their prominent expression of"）；SST → H11（figure_labeled，句②图注逐基因区分指定 + 句③主文）；MRGPRX1 → H10（figure_labeled，A 门候选 15）** |
| **non-neuronal cells（唯一非神经元群）** | PRP1、MBP、QKI、LPAR1、APOE | Methods（L709-712）："Clusters not expressing high levels of neuronal or somatosensory genes like SNAP25, SCN9A, SCN10A, PIEZO2, NEFH, etc. but instead expressing elevated levels of markers of non-neuronal cells including PRP1, MBP, QKI, LPAR1, and APOE were tagged as non-neuronal and were removed to allow reclustering of 'purified' human DRG neurons." | **整群漏提 → 补录 5 行（PRP1/MBP/QKI/LPAR1/APOE → non-neuronal cells, human, author_declared）**（A 门候选 2/3/16/17/18）。注意：本文非神经元群无亚型细分，故只建 1 个 cell_type |
| （小鼠参考簇 NP1/NP2/NP3/cLTMRs/Aβ/proprioceptors/Trpm8 cells 等） | Mrgprd→NP1、Mrgpra3→NP2、JAK1/SST/Nppb→NP3、Pvalb/Etv1/Scn1a/Scn1b→小鼠 proprioceptors | 例：L249 "one (NP1, expressing Mrgprd)…"；L491-492 "in mice NP1 cells express a large combination of diagnostic markers (Figure 5—figure supplement 2) including Mrgprd…"；L293 "H11 – NP3 (Nppb) neurons"；L398-399 "Mrgpra3, which in mice marks NP2 cells"；L152-154 "In mice, proprioceptors are…marked by…Etv1 and…Scn1a and Scn1b" | **不列为漏提、不补录**：小鼠簇标签及 marker 关系整体转述自 Renthal et al. 2020 等先前研究（本文未做 de novo 注释），按双重门槛之"注释用途"不满足。若项目口径日后决定收录"跨篇转述性 marker 句"，此处已备齐 locator 与原句可回溯 |

**补录行汇总（供总表落地）**：
- A 门补录 8 行：NTRK3/H12（author_declared）、TAC1/peptidergic nociceptors（author_declared）、MRGPRX1/H10（figure_labeled）、PRP1、MBP、QKI、LPAR1、APOE/non-neuronal cells（author_declared，human）
- D 门追加建议 8 行：SCN1A/H12（author_declared）、PVALB/H15、NEFH/H15、PIEZO2/H15（annotation_marker）、SCN10A/H4、NTRK1/H4（annotation_marker）、PIEZO2/H10（annotation_marker）、SST/H11（figure_labeled）
- D 门追加建议（中等置信）3 行：CALCA、CALCB、ADCYAP1/peptidergic nociceptors（author_declared，回指性 "peptidergic markers" 措辞 + Figure 1C diagnostic markers dotplot）
- 补录后仍无行的簇：H8、H9、H13、H14（文本仅富集措辞，无 marker 措辞；只能依赖图级 dotplot，其基因清单不在 review_md，判定为"漏提但无可核验 marker 行"并留档）

---

## 试点遗留处置（PMID_35115729，Batch 1 并入处置）

### M01516 Pdgfra / endoneurial fibroblasts (EFs)：**升级 author_declared**

- 核实原句（review_md L189-191，Results p.4）："We detected EFs in the Mpz-Sun1 atlas (Fig. 2b) and found they express the fibroblast marker Pdgfra as well as the stem cell markers Cd34 and nmSC marker Ngfr (Fig. 2c)."
- 判定：**升级成立**。作者明确以 marker 措辞呈现——"the fibroblast marker Pdgfra"，且该句语境即 EFs 在 Mpz-Sun1 atlas 中的检出与表征（Fig. 2b-c 展示），marker 身份与注释用途（EF 群的识别/特征化）均成立。这正是 BRIEF B 门所举的升级范例措辞。
- 落地：cell_type 维持 "endoneurial fibroblasts (EFs)"，evidence_type annotation_marker → **author_declared**；source_context 替换为上述完整原句；source_locator 建议 "Results p.4; Fig. 2b-c"。
- 与 M01885（Pdgfra / epineurial fibroblasts / annotation_marker）不冲突：同基因不同 cell_type 的独立行（EFs vs epineurial fibroblasts）。一致性说明：M01885 依据句 "Epineurial fibroblasts, which surround the outermost layer of the nerve, express Pdgfra and Pcolce" 为纯表达措辞，**不应随之升级**，维持 annotation_marker。

### M01517 Cd34 / endoneurial/epineurial fibroblasts：**维持 annotation_marker（不升级）**

- 核实原句：
  ① review_md L189-191："We detected EFs in the Mpz-Sun1 atlas (Fig. 2b) and found they express the fibroblast marker Pdgfra as well as the stem cell markers Cd34 and nmSC marker Ngfr (Fig. 2c)."
  ② Figure 1e 图注（review_md L1146-1148）："Clusters that share 'signature' genes are enclosed in dashed lines, i.e. all mSCs expressed Prx and Mbp, endoneurial/epineurial fibroblasts expressed Pdgfra and Cd34 and immune cells expressed Ptprc (this one missing from figure)."
- 判定：**维持 annotation_marker，不升级**。理由：
  1. 句①中 Cd34 的 marker 措辞是 "the stem cell markers Cd34"——marker 身份指向**干细胞性状**（基因属性描述，类似 BRIEF 边界规则中 "progenitor markers" 类非细胞群识别用途），并非"成纤维细胞群的 marker"；该措辞不能支持把 Cd34 升级为成纤维细胞群的 author_declared marker。
  2. 成纤维细胞语境下的证据（句② "endoneurial/epineurial fibroblasts expressed Pdgfra and Cd34"）为 "signature genes" 图级分组说明 + 纯表达措辞，且另有 "newly identified Ngfr and Cd34 expression in EFs"（L202）、"Cd34 expression overlaps with Pdgfra and Ngfr expression"（L1173）等表达/共定位措辞——支持现有 annotation_marker 定级，不足以升 author_declared。
  3. 对照 M01516：Pdgfra 有 "the fibroblast marker Pdgfra" 直接修饰且主语即 EFs，而 Cd34 无任何 "fibroblast marker Cd34" 式措辞——两行不同判，符合 B 门"marker 措辞须确实指向该基因+该细胞"的规则。
- 落地：evidence_type 维持 annotation_marker；建议将 source_context 中的图注截断句替换为句②完整原句（备档，不属升级要求）。

### 试点遗留小结

- 升级 1：M01516（Pdgfra / EFs / annotation_marker → author_declared，source_context 已换完整原句）
- 维持 1：M01517（Cd34 / endoneurial-epineurial fibroblasts / annotation_marker 不变）
- 连带核查：M01885（Pdgfra / epineurial fibroblasts）维持 annotation_marker，不随 M01516 升级；与 M01516 为同基因不同 cell_type 独立行，无语义重复、无需合并。

---

## 复核方法与可追溯性说明

- 全部判定均回 review_md 原文逐句核实（引文括注 review_md 行号 L），候选材料中的截断句已替换为完整原句。
- evidence_type 定级口径（与现有 10 行保持一致）：显式 marker 措辞（"marked by"/"markers of X including"/"these three markers"）→ author_declared；识别/命名/区分依据句（"identified by their expression of"/"designated … because of"/"distinguished by their expression of"）→ annotation_marker；图注逐基因区分指定（Figure 5B/5C "genes that distinguish H10 and H11"）→ figure_labeled。
- 引文中 "X- y" 连字符空格为 PDF 换行伪影，已按语义最小归并，未改动任何词；PRP1 保留原文拼写。
