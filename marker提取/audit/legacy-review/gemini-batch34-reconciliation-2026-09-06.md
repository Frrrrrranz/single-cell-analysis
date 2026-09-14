# Gemini 第三、四轮23篇差异裁决

仅核对既有 JSON、总表及相关原文/原图，不调用模型重新提取，不宣称穷尽所有 marker。
总表 2474 → 2499 条；新增 25 条；移出/去重 0 条。

## 逐篇统计

|论文|原表|正式候选|全部候选|匹配|新增|上下文|排除|未决|更新后|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| DOI_10.1016_j.cell.2021.07.023 | 146 | 12 | 13 | 12 | 0 | 1 | 0 | 0 | 146 |
| DOI_10.1016_j.cell.2022.11.005 | 207 | 10 | 10 | 8 | 0 | 0 | 0 | 2 | 207 |
| DOI_10.1016_j.isci.2024.111628 | 80 | 12 | 12 | 11 | 0 | 0 | 0 | 1 | 80 |
| DOI_10.1016_j.stem.2022.11.013 | 70 | 12 | 15 | 12 | 0 | 0 | 1 | 2 | 70 |
| DOI_10.1038_s41467-021-21783-3 | 11 | 10 | 11 | 3 | 1 | 2 | 1 | 4 | 12 |
| DOI_10.1038_s41467-023-40173-5 | 47 | 10 | 10 | 10 | 0 | 0 | 0 | 0 | 47 |
| DOI_10.1038_s41467-024-52052-8 | 6 | 11 | 11 | 2 | 3 | 1 | 0 | 5 | 9 |
| DOI_10.1038_s41586-021-03569-1 | 30 | 11 | 11 | 9 | 1 | 1 | 0 | 0 | 31 |
| DOI_10.1038_s41586-021-04345-x | 80 | 11 | 11 | 11 | 0 | 0 | 0 | 0 | 80 |
| DOI_10.1038_s41586-024-07069-w | 152 | 10 | 10 | 8 | 0 | 1 | 0 | 1 | 152 |
| DOI_10.1038_s41588-022-01243-4 | 86 | 10 | 10 | 7 | 0 | 2 | 0 | 1 | 86 |
| DOI_10.1038_s41588-024-01702-0 | 19 | 10 | 10 | 10 | 0 | 0 | 0 | 0 | 19 |
| DOI_10.1038_s41588-025-02158-6 | 33 | 10 | 10 | 8 | 2 | 0 | 0 | 0 | 35 |
| DOI_10.1038_s41588-025-02182-6 | 60 | 10 | 10 | 10 | 0 | 0 | 0 | 0 | 60 |
| DOI_10.1038_s41591-023-02327-2 | 28 | 10 | 10 | 8 | 2 | 0 | 0 | 0 | 30 |
| DOI_10.1038_s41591-024-03215-z | 13 | 10 | 10 | 3 | 3 | 4 | 0 | 0 | 16 |
| DOI_10.1038_s42003-021-02562-8 | 14 | 10 | 10 | 10 | 0 | 0 | 0 | 0 | 14 |
| DOI_10.1038_s42003-024-07315-x | 81 | 10 | 10 | 7 | 2 | 0 | 0 | 1 | 83 |
| DOI_10.1038_s42255-023-00876-x | 60 | 10 | 10 | 10 | 0 | 0 | 0 | 0 | 60 |
| DOI_10.1126_science.aat5031 | 16 | 12 | 12 | 5 | 2 | 1 | 0 | 4 | 18 |
| DOI_10.1126_science.abl4290 | 15 | 10 | 10 | 1 | 5 | 0 | 0 | 4 | 20 |
| DOI_10.7554_elife.62522 | 1 | 10 | 10 | 0 | 2 | 6 | 0 | 2 | 3 |
| PMID_35115729 | 42 | 11 | 14 | 11 | 2 | 0 | 0 | 1 | 44 |

## 关键结果与限制

- 两轮共23篇：242条 formal、6条 context_only、2条 excluded，全部250条既有候选均有裁决；未重新调用提取模型。
- 结果：匹配176、新增25、上下文19、排除2、未决28。原表12条修正（CD86细胞错配1条、SOX2极性1条、斑马鱼物种10条）；本轮没有删除旧行。
- Gemini的优点是结构统一、核心注释marker多数能对应已有关系，并补充了原表遗漏的图示和空间定位证据。
- 最后一轮13篇各恰好10条formal，说明产物是核心精选；不能把“43篇已输出JSON”解释为“所有可靠marker已穷尽”。未出现在Gemini中的旧条目继续保留。
- 明确错配：ALDH1A3应为SMG duct而非mature DC；Sox10/Erbb4为Shh+脊索亚群而非neural crest；HOPX此处为AT2而非AT1；moxd1对应clusters 1/2/7而非cluster6。
- Gemini也纠正了旧表：神经母细胞瘤Fig.1d的CD86确属Macrophages，原表Dendritic cells已修正。
- iPain Fig.1可确认Tac1/Th/Nefh，保留PEP1/cLTMR1/NF2粒度；其余未定位基因不凭经典知识填入。SA-β-gal酶活不能直接改成Glb1基因表达。
- 不能一律把功能基因排除：LCN2有Fig.2b marker图注明证；NPNT有Fig.4d most exclusive marker图注，均正式纳入。单纯病毒进入、EMT评分和driver/regulon候选保留context。
- Ngfr共享表达不否定nmSC用途；ChAT、β-tubulin III及Epcam实际识别/门控用途按同一标准恢复。人PMP2保留厚髓鞘亚群，不强化为人类motor专属。
- matched表示与既有关系对应并保留原细胞粒度，不是重新穷尽审计该论文全部旧条目。未决28条是当前证据缺口，不等于证明基因不存在。补图未核者不标已验证。
- 本轮同步正式总表、按细胞表及图表索引；历史审计不覆盖。原候选、原表目标行快照、输入SHA256和逐条理由见配套JSON。

## 全部候选裁决

|论文|原分类/序号|基因|细胞|结果|对应ID|理由|
|---|---|---|---|---|---|---|
| DOI_10.1016_j.cell.2021.07.023 | formal_markers #1 | TP63 | basal cells | matched | M00900 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 4716, Fig. 1f |
| DOI_10.1016_j.cell.2021.07.023 | formal_markers #2 | KRT5 | basal cells | matched | M00899 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 4716, Fig. 1f |
| DOI_10.1016_j.cell.2021.07.023 | formal_markers #3 | BPIFA1 | Secretory cells | matched | M01007 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 4716, Fig. 1f, m |
| DOI_10.1016_j.cell.2021.07.023 | formal_markers #4 | MUC5AC | goblet cells | matched | M00948 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 4716, Fig. 1f, n |
| DOI_10.1016_j.cell.2021.07.023 | formal_markers #5 | FOXI1 | ionocytes | matched | M00955 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 4716, Fig. 1f |
| DOI_10.1016_j.cell.2021.07.023 | formal_markers #6 | CFTR | ionocytes | matched | M00954 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 4716, Fig. 1f |
| DOI_10.1016_j.cell.2021.07.023 | formal_markers #7 | DEUP1 | deuterosomal cells | matched | M00928 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 4716, Fig. 1f, l |
| DOI_10.1016_j.cell.2021.07.023 | formal_markers #8 | FOXJ1 | ciliated cells | matched | M00921 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 4716, Fig. 1f, j |
| DOI_10.1016_j.cell.2021.07.023 | formal_markers #9 | SCEL | squamous cells | matched | M01029 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 4716, Fig. 1f |
| DOI_10.1016_j.cell.2021.07.023 | formal_markers #10 | TPSB2 | mast cells | matched | M01001 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 4716, Fig. 1f |
| DOI_10.1016_j.cell.2021.07.023 | formal_markers #11 | IL3RA | plasmacytoid DCs | matched | M01004 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 4716, Fig. 1f |
| DOI_10.1016_j.cell.2021.07.023 | formal_markers #12 | CD3E | T cells | matched | M01034 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 4716, Fig. 1f |
| DOI_10.1016_j.cell.2021.07.023 | context_only #1 | ACE2 | Respiratory Epithelium (Secretory and Goblet Cells) | context_only |  | Viral receptor functional entry factor；Main Text p. 4716, Fig. 1i |
| DOI_10.1016_j.cell.2022.11.005 | formal_markers #1 | SOX9 | multipotent progenitors | matched | M00504 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 4841-4843, Fig. 1a-f, Fig. 2a-e |
| DOI_10.1016_j.cell.2022.11.005 | formal_markers #2 | ID2 | multipotent progenitors | matched | M00503 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 4842, Fig. 1d-e |
| DOI_10.1016_j.cell.2022.11.005 | formal_markers #3 | CHGA | neuroendocrine cell | matched | M00031 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 4851-4854, Fig. 7a-f |
| DOI_10.1016_j.cell.2022.11.005 | formal_markers #4 | SYP | neuroendocrine cell | matched | M00032 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 4851, Fig. 7a-b |
| DOI_10.1016_j.cell.2022.11.005 | formal_markers #5 | GHRL | GHRL+ neuroendocrine cell | matched | M00036 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 4851-4853, Fig. 7a-c |
| DOI_10.1016_j.cell.2022.11.005 | formal_markers #6 | TP63 | basal cells | matched | M00449 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 4843-4845, Fig. 3a-d |
| DOI_10.1016_j.cell.2022.11.005 | formal_markers #7 | FOXJ1 | ciliated cell | matched | M00455 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 4843-4845, Fig. 3a-d |
| DOI_10.1016_j.cell.2022.11.005 | formal_markers #8 | COL2A1 | Airway Chondrocyte | unresolved |  | 所引 Fig.1e 是发育年龄 UMAP；既有正文未定位 COL2A1/SOX10 对应标记。需具体 marker 面板，不能从细胞名称补写。；Main Text pp. 4844-4846, Fig. 1e, Fig. 4a |
| DOI_10.1016_j.cell.2022.11.005 | formal_markers #9 | SOX10 | Schwann Cell | unresolved |  | 所引 Fig.1e 是发育年龄 UMAP；既有正文未定位 COL2A1/SOX10 对应标记。需具体 marker 面板，不能从细胞名称补写。；Main Text pp. 4842-4844, Fig. 1e |
| DOI_10.1016_j.cell.2022.11.005 | formal_markers #10 | ACTA2 | airway smooth muscle cell | matched | M00429 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 4842-4845, Fig. 1e, Fig. 4a |
| DOI_10.1016_j.isci.2024.111628 | formal_markers #1 | CDH19 | Schwann cells | matched | M00060 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 3-5, Fig. 1E |
| DOI_10.1016_j.isci.2024.111628 | formal_markers #2 | NRXN1 | Schwann Cell | unresolved |  | 正文仅 NRXN+，没有足以唯一指认为 NRXN1 的证据；保留待核。；Main Text pp. 3-5, Fig. 1E |
| DOI_10.1016_j.isci.2024.111628 | formal_markers #3 | XKR4 | Schwann cells | matched | M00061 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 3-5, Fig. 1E |
| DOI_10.1016_j.isci.2024.111628 | formal_markers #4 | UPK2 | Umbrella cells | matched | M01174 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 3-5, Fig. 1C, Fig. 2A |
| DOI_10.1016_j.isci.2024.111628 | formal_markers #5 | UPK3A | Umbrella cells | matched | M01175 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 3-5, Fig. 1C, Fig. 2A |
| DOI_10.1016_j.isci.2024.111628 | formal_markers #6 | KRT20 | Umbrella cells | matched | M01171 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 5, Fig. 2A |
| DOI_10.1016_j.isci.2024.111628 | formal_markers #7 | LAMC3 | Peri-urothelial fibroblast | matched | M01160 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 3-5, Fig. 1E |
| DOI_10.1016_j.isci.2024.111628 | formal_markers #8 | GAS1 | Lamina propria fibroblast | matched | M01136 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 3-5, Fig. 1E |
| DOI_10.1016_j.isci.2024.111628 | formal_markers #9 | C7 | Intra-muscular fibroblast | matched | M01134 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 3-5, Fig. 1E |
| DOI_10.1016_j.isci.2024.111628 | formal_markers #10 | CXCL14 | CXCL14hi fibroblast | matched | M01115 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 3-5, Fig. 1E |
| DOI_10.1016_j.isci.2024.111628 | formal_markers #11 | ACTG2 | Smooth muscle cells | matched | M01166 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 3-5, Fig. 1E |
| DOI_10.1016_j.isci.2024.111628 | formal_markers #12 | RGS5 | Vascular smooth muscle cells | matched | M01180 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 3-5, Fig. 1E |
| DOI_10.1016_j.stem.2022.11.013 | formal_markers #1 | SOX9 | human lung tip progenitors | matched | M00862 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 20-22, Fig. 1B, Fig. 1J-M |
| DOI_10.1016_j.stem.2022.11.013 | formal_markers #2 | ETV5 | Distal Bud Tip Progenitor Cell | unresolved |  | 现有引文未充分定位具体 gene–cell 关系；不从常识补写。；Main Text pp. 22-26, Fig. 2, Fig. 4 |
| DOI_10.1016_j.stem.2022.11.013 | formal_markers #3 | CD36 | late-stage tip epithelial cells | matched | M00863 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 21-23, Fig. 1H-1M, Fig. 2A-D |
| DOI_10.1016_j.stem.2022.11.013 | formal_markers #4 | CD44 | late-stage tip epithelial cells | matched | M00864 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 21-22, Fig. 1H-I |
| DOI_10.1016_j.stem.2022.11.013 | formal_markers #5 | PDPN | stalk cells | matched | M00882 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 21, Fig. 1E-G |
| DOI_10.1016_j.stem.2022.11.013 | formal_markers #6 | TP63 | CD44−CD36− cells | matched | M00851 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 21-22, Fig. 1H |
| DOI_10.1016_j.stem.2022.11.013 | formal_markers #7 | SFTPC | AT2 cells | matched | M00841 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 20-25, Fig. 1A, Fig. 2B-D, Fig. 3 |
| DOI_10.1016_j.stem.2022.11.013 | formal_markers #8 | LAMP3 | AT2 cells | matched | M00840 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 21-24, Fig. 1B, Fig. 1J, Fig. S1B |
| DOI_10.1016_j.stem.2022.11.013 | formal_markers #9 | SLC34A2 | AT2 cells | matched | M00842 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 21, Fig. 1B |
| DOI_10.1016_j.stem.2022.11.013 | formal_markers #10 | AGER | Alveolar Type 1 Cell | unresolved |  | 现有引文未充分定位具体 gene–cell 关系；不从常识补写。；Main Text pp. 20-25, Fig. 1A, Fig. 3B-D |
| DOI_10.1016_j.stem.2022.11.013 | formal_markers #11 | HOPX | AT2 cells | matched | M00839 | 正文列为 AT2-specific genes LAMP3/HOPX/ACE2；纠正 Gemini 的 AT1 错配，与原 AT2 行一致。；Main Text pp. 21-25, Fig. 1A, Fig. 4, Fig. S4 |
| DOI_10.1016_j.stem.2022.11.013 | formal_markers #12 | NOTUM | myofibroblasts | matched | M00878 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Highlights, Main Text pp. 26-29, Fig. 5A-G |
| DOI_10.1016_j.stem.2022.11.013 | context_only #1 | ACTA2 | myofibroblasts | matched | M00879 | ACTA2 定位/EPCAM 门控是实际注释用途，不因泛表达而排除；恢复正式对应。；Main Text pp. 26-28, Fig. 5 |
| DOI_10.1016_j.stem.2022.11.013 | context_only #2 | EPCAM | EPCAM+ cells | matched | M00855 | ACTA2 定位/EPCAM 门控是实际注释用途，不因泛表达而排除；恢复正式对应。；Main Text p. 21, STAR Methods |
| DOI_10.1016_j.stem.2022.11.013 | excluded #1 | SOX2 | Distal Bud Tip Progenitor | exclude |  | SOX2 并非所有 distal tip 均阴性：早期 SOX2+，晚期降低/阴性。否定未分期的统一阴性配对；旧晚期 CD44+CD36+ 行已更正 low。；Main Text pp. 21-22, Fig. 1B, 1H |
| DOI_10.1038_s41467-021-21783-3 | formal_markers #1 | Csn2 | Alveolar cells (Avd) | matched | M01586 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 3-4, Fig. 2c, Fig. 2f, Fig. 4c |
| DOI_10.1038_s41467-021-21783-3 | formal_markers #2 | Wap | alveolar cells | matched | M01585 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 3-5, Fig. 2c, Fig. 4c |
| DOI_10.1038_s41467-021-21783-3 | formal_markers #3 | Elf5 | Alveolar cells (Avd) | matched | M01587 | 已查看 Fig.2c-d，Elf5 对应 Avd 的 alveolar lineage；纠正泛 LP 标签，沿用原 Avd 关系。；Main Text pp. 2-4, Fig. 2c-d |
| DOI_10.1038_s41467-021-21783-3 | formal_markers #4 | Kit | Luminal Progenitor Cell | exclude |  | Gemini 声称 CD49b+Kit+ 门控；Methods 实际为 CD49b+Sca1−，所引 Kit/CD117 门控不成立。；Methods, Supplementary Figs. 8-9 |
| DOI_10.1038_s41467-021-21783-3 | formal_markers #5 | Tnfsf11 | Hormone-Sensing Mature Luminal Cell | context_only |  | Fig.4 的旁分泌/致瘤功能讨论未建立所列细胞的身份 marker 用途。；Main Text pp. 3-5, Fig. 3e, Fig. 4b-c |
| DOI_10.1038_s41467-021-21783-3 | formal_markers #6 | Igf2 | Hormone-Sensing Mature Luminal Cell | context_only |  | Fig.4 的旁分泌/致瘤功能讨论未建立所列细胞的身份 marker 用途。；Main Text pp. 3-5, Fig. 3e, Fig. 4b-c |
| DOI_10.1038_s41467-021-21783-3 | formal_markers #7 | Acta2 | Basal / Myoepithelial Cell | unresolved |  | 现有引文未充分定位具体 gene–cell 关系；不从常识补写。；Main Text p. 2, Fig. 1b, Supplementary Fig. 1c |
| DOI_10.1038_s41467-021-21783-3 | formal_markers #8 | Krt14 | Basal / Myoepithelial Cell | unresolved |  | 现有引文未充分定位具体 gene–cell 关系；不从常识补写。；Main Text p. 2, Fig. 1b |
| DOI_10.1038_s41467-021-21783-3 | formal_markers #9 | Col1a1 | Mammary Stromal Fibroblast | unresolved |  | 现有引文未充分定位具体 gene–cell 关系；不从常识补写。；Main Text pp. 2-3, Fig. 1b |
| DOI_10.1038_s41467-021-21783-3 | formal_markers #10 | Adgre1 | Mammary Macrophage | unresolved |  | 现有引文未充分定位具体 gene–cell 关系；不从常识补写。；Main Text pp. 2-4, Fig. 1b, Fig. 4a |
| DOI_10.1038_s41467-021-21783-3 | context_only #1 | Epcam | Avd cells | add | M02565 | Fig.2c 为 Avd 群的 lineage-marker 面板，含 Epcam；不因上皮泛标记而剔除。；Fig.2c, PDF p.3 |
| DOI_10.1038_s41467-023-40173-5 | formal_markers #1 | DEUP1 | deuterosomal cells | matched | M00741 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 3, Methods p. 15, Fig. 1B |
| DOI_10.1038_s41467-023-40173-5 | formal_markers #2 | FOXN4 | deuterosomal cells | matched | M00742 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 3, Methods p. 15, Fig. 1B |
| DOI_10.1038_s41467-023-40173-5 | formal_markers #3 | SERPINB4 | suprabasal cells | matched | M00772 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 3, Methods p. 15, Fig. 1B |
| DOI_10.1038_s41467-023-40173-5 | formal_markers #4 | KRT19 | suprabasal cells | matched | M00770 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 3, Methods p. 15, Fig. 1B |
| DOI_10.1038_s41467-023-40173-5 | formal_markers #5 | COL15A1 | systemic venous endothelial cells (SVEC) | matched | M00775 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 3, Methods p. 15, Fig. 1B |
| DOI_10.1038_s41467-023-40173-5 | formal_markers #6 | ACKR1 | systemic venous endothelial cells (SVEC) | matched | M00774 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 3, Methods p. 15, Fig. 1B |
| DOI_10.1038_s41467-023-40173-5 | formal_markers #7 | SCGB3A2 | respiratory airway secretory cells (RAS) | matched | M00761 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 3, Methods p. 15, Fig. 1B |
| DOI_10.1038_s41467-023-40173-5 | formal_markers #8 | KLK11 | respiratory airway secretory cells (RAS) | matched | M00760 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 3, Methods p. 15, Fig. 1B |
| DOI_10.1038_s41467-023-40173-5 | formal_markers #9 | ALDH1A3 | SMG duct cells | matched | M00763 | 正文 ALDH1A3 属于 MIA/ALDH1A3/RARRES1 SMG duct；maDC 为 CCR7/CCL19/LAD1。纠正 Mature Dendritic 错配。；Main Text p. 3, Methods p. 15, Fig. 1B |
| DOI_10.1038_s41467-023-40173-5 | formal_markers #10 | AGER | Alveolar type 1 cells (AT1) | matched | M00729 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 2-4, Fig. 2C |
| DOI_10.1038_s41467-024-52052-8 | formal_markers #1 | Tac1 | PEP1 | add | M02566 | 已查看 Fig.1d/h 的可读 top-3 注释标签，保留图中具体群，不泛化。；Fig.1d/h, PDF p.3 |
| DOI_10.1038_s41467-024-52052-8 | formal_markers #2 | Calca | Peptidergic Nociceptor | unresolved |  | 已查看所引 Fig.1d/h，该基因不在对应群标记标签/点图列；尚无其他可回溯位置，不凭经典 marker 常识纳入。；Main Text pp. 1-3, Fig. 1d, h |
| DOI_10.1038_s41467-024-52052-8 | formal_markers #3 | Mrgprd | Non-Peptidergic Nociceptor | unresolved |  | 已查看所引 Fig.1d/h，该基因不在对应群标记标签/点图列；尚无其他可回溯位置，不凭经典 marker 常识纳入。；Main Text pp. 1-3, Fig. 1d |
| DOI_10.1038_s41467-024-52052-8 | formal_markers #4 | Piezo2 | C-Low Threshold Mechanoreceptor | unresolved |  | 已查看所引 Fig.1d/h，该基因不在对应群标记标签/点图列；尚无其他可回溯位置，不凭经典 marker 常识纳入。；Main Text pp. 1-3, Fig. 1d |
| DOI_10.1038_s41467-024-52052-8 | formal_markers #5 | Th | cLTMR1 | add | M02567 | 已查看 Fig.1d/h 的可读 top-3 注释标签，保留图中具体群，不泛化。；Fig.1d/h, PDF p.3 |
| DOI_10.1038_s41467-024-52052-8 | formal_markers #6 | Sst | SST neurons (somatostatin-positive nociceptor subtype) | matched | M01510 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1, Fig. 1d |
| DOI_10.1038_s41467-024-52052-8 | formal_markers #7 | Nefh | NF2 | add | M02568 | 已查看 Fig.1d/h 的可读 top-3 注释标签，保留图中具体群，不泛化。；Fig.1d/h, PDF p.3 |
| DOI_10.1038_s41467-024-52052-8 | formal_markers #8 | Sox11 | Senescent Nociceptor | context_only |  | Sox11 为动态 driver/regulon 与损伤机制分析，未建立新的细胞身份标记。；Main Text pp. 3-4, Fig. 2f-g, Supplementary Fig. 5a-f |
| DOI_10.1038_s41467-024-52052-8 | formal_markers #9 | Glb1 | Senescent Nociceptor | unresolved |  | 原实验为 SA-β-galactosidase 酶活染色，不能直接改写成 Glb1 基因表达 marker。；Main Text pp. 4-6, Fig. 3h-i |
| DOI_10.1038_s41467-024-52052-8 | formal_markers #10 | Cdkn1a | senescent nociceptors | matched | M00072 | 正文明确 senescence marker p21 核染色；保留旧 senescent nociceptor 条件。；Main Text pp. 4-5, Fig. 3a-e |
| DOI_10.1038_s41467-024-52052-8 | formal_markers #11 | Fabp7 | Satellite Glial Cell | unresolved |  | 已查看所引 Fig.1d/h，该基因不在对应群标记标签/点图列；尚无其他可回溯位置，不凭经典 marker 常识纳入。；Main Text pp. 2-4, Fig. 1d, Fig. 2h |
| DOI_10.1038_s41586-021-03569-1 | formal_markers #1 | KRT8 | damage-associated transient progenitors (DATP) | matched | M00806 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 115-117, Fig. 3c, Fig. 3j |
| DOI_10.1038_s41586-021-03569-1 | formal_markers #2 | CLDN4 | damage-associated transient progenitors (DATP) | matched | M00805 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 115-116, Fig. 3c, Fig. 3h |
| DOI_10.1038_s41586-021-03569-1 | formal_markers #3 | SFTPC | alveolar type II (AT2) cells | matched | M00798 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 116, Fig. 3c, Fig. 3j |
| DOI_10.1038_s41586-021-03569-1 | formal_markers #4 | SFTPB | alveolar type II (AT2) cells | matched | M00797 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 116, Fig. 3c |
| DOI_10.1038_s41586-021-03569-1 | formal_markers #5 | ETV5 | Alveolar Type 2 Cell | context_only |  | Fig.3d 讨论维持 AT2 身份的转录因子 ETV5 降低及再生过程；当前所引证据为变化/功能，未建立单独成熟群识别。；Main Text p. 116, Fig. 3d |
| DOI_10.1038_s41586-021-03569-1 | formal_markers #6 | AGER | alveolar type I (AT1) cells | matched | M00795 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 116, Fig. 3c |
| DOI_10.1038_s41586-021-03569-1 | formal_markers #7 | CLIC5 | alveolar type I (AT1) cells | matched | M00796 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 116, Fig. 3c |
| DOI_10.1038_s41586-021-03569-1 | formal_markers #8 | CAV1 | AT1 cells | add | M02569 | 正文明确 CAV1 为 late AT1 maturation marker，Fig.3e 实际使用；保留成熟条件。；Results, Fig.3e |
| DOI_10.1038_s41586-021-03569-1 | formal_markers #9 | CTHRC1 | pathological fibroblasts | matched | M00819 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Abstract, Main Text pp. 116-117, Fig. 4b-c, Extended Data Fig. 12e |
| DOI_10.1038_s41586-021-03569-1 | formal_markers #10 | COL1A1 | pathological fibroblasts | matched | M00818 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 116-117, Fig. 4b, Extended Data Fig. 12e |
| DOI_10.1038_s41586-021-03569-1 | formal_markers #11 | COL3A1 | pathological fibroblasts (pFBs) | matched | M00820 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 116-117, Fig. 4b, Extended Data Fig. 12e |
| DOI_10.1038_s41586-021-04345-x | formal_markers #1 | SCGB1A1 | club cells | matched | M00342 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 322, Fig. 1b, d |
| DOI_10.1038_s41586-021-04345-x | formal_markers #2 | SCGB3A1 | club cells | matched | M00343 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 322, Fig. 1b |
| DOI_10.1038_s41586-021-04345-x | formal_markers #3 | GALNT4 | secretory | matched | M00393 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 322, Fig. 1b |
| DOI_10.1038_s41586-021-04345-x | formal_markers #4 | TFF1 | goblet 1 | matched | M00349 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 322, Fig. 1b |
| DOI_10.1038_s41586-021-04345-x | formal_markers #5 | MUC5AC | goblet cells | matched | M00354 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 322, Fig. 1b |
| DOI_10.1038_s41586-021-04345-x | formal_markers #6 | SPRR3 | squamous cells | matched | M00396 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 322, Fig. 1b |
| DOI_10.1038_s41586-021-04345-x | formal_markers #7 | KRT14 | Hillock-like populations | matched | M00362 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 322, Fig. 1b, d |
| DOI_10.1038_s41586-021-04345-x | formal_markers #8 | PIFO | ciliated 1 | matched | M00339 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 322, Fig. 1b, d |
| DOI_10.1038_s41586-021-04345-x | formal_markers #9 | CFAP54 | ciliated 2 | matched | M00340 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 322, Fig. 1b, d |
| DOI_10.1038_s41586-021-04345-x | formal_markers #10 | CDC20 | deuterosomal cells | matched | M00347 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 322, Fig. 1b, d |
| DOI_10.1038_s41586-021-04345-x | formal_markers #11 | FOXN4 | deuterosomal cells | matched | M00348 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 322, Fig. 1b, d |
| DOI_10.1038_s41586-024-07069-w | formal_markers #1 | Sox10 | notochord | matched | M01741 | 正文与 Extended Data Fig.4i 为 Noto−、Shh+ notochord 亚群，不能改为 Neural Crest/PNS Glia。沿用原脊索记录。；Main Text pp. 1086-1088, Extended Data Fig. 4i |
| DOI_10.1038_s41586-024-07069-w | formal_markers #2 | Erbb4 | notochord | matched | M01739 | 正文与 Extended Data Fig.4i 为 Noto−、Shh+ notochord 亚群，不能改为 Neural Crest/PNS Glia。沿用原脊索记录。；Main Text pp. 1086-1088, Extended Data Fig. 4i |
| DOI_10.1038_s41586-024-07069-w | formal_markers #3 | Zfp536 | Myelinating Schwann Cell | context_only |  | 正文列为 warrant further investigation 的候选 TF regulator；非已验证 Schwann marker。；Main Text p. 1090, Supplementary Table 23 |
| DOI_10.1038_s41586-024-07069-w | formal_markers #4 | Isl1 | Spinal Motor Neuron Progenitor | unresolved |  | 当前引文未充分确认 Isl1 对应 progenitor 而非分化 motor neuron；不擅自确定发育粒度。；Main Text p. 1088, Fig. 2f |
| DOI_10.1038_s41586-024-07069-w | formal_markers #5 | Pax6 | retinal progenitor cells RPCs | matched | M01780 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1089, Extended Data Fig. 9d-e |
| DOI_10.1038_s41586-024-07069-w | formal_markers #6 | Rax | retinal progenitor cells RPCs | matched | M01781 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1089, Extended Data Fig. 9d-e |
| DOI_10.1038_s41586-024-07069-w | formal_markers #7 | Tbr1 | deep-layer neurons | matched | M01693 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1089, Extended Data Fig. 9 |
| DOI_10.1038_s41586-024-07069-w | formal_markers #8 | Bcl11b | deep-layer neurons | matched | M01691 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1089, Extended Data Fig. 9 |
| DOI_10.1038_s41586-024-07069-w | formal_markers #9 | Kcnab1 | subplate neurons | matched | M01784 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1089, Extended Data Fig. 9 |
| DOI_10.1038_s41586-024-07069-w | formal_markers #10 | Foxp2 | subplate neurons | matched | M01783 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1089, Extended Data Fig. 9 |
| DOI_10.1038_s41588-022-01243-4 | formal_markers #1 | LPO | SMG serous cell | matched | M00294 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 68-71, Fig. 4, Extended Data Fig. 7 |
| DOI_10.1038_s41588-022-01243-4 | formal_markers #2 | CCL28 | SMG Serous Cell | context_only |  | 该位置讨论 CCL28/PIGR 的 IgA 招募/转运与细胞通讯；未证明其在本文用于所列细胞身份注释。；Abstract, Main Text pp. 71-73, Fig. 5a-d |
| DOI_10.1038_s41588-022-01243-4 | formal_markers #3 | PRR4 | SMG Serous Cell | unresolved |  | Fig.5b 并非 PRR4 marker 染色；Extended Data Fig.10g 图注另提 HPA PRR4/MUC5B，需核其原图对应区域后确定该候选。；Main Text p. 71, Fig. 5b |
| DOI_10.1038_s41588-022-01243-4 | formal_markers #4 | MUC5B | SMG-mucous | matched | M00296 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 69-70, Fig. 4b, d |
| DOI_10.1038_s41588-022-01243-4 | formal_markers #5 | ALDH1A3 | SMG duct cells | matched | M00291 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 69-70, Fig. 4b |
| DOI_10.1038_s41588-022-01243-4 | formal_markers #6 | RARRES1 | SMG duct cells | matched | M00293 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 69-70, Fig. 4b |
| DOI_10.1038_s41588-022-01243-4 | formal_markers #7 | MIA | SMG duct cells | matched | M00292 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 70, Fig. 4d |
| DOI_10.1038_s41588-022-01243-4 | formal_markers #8 | ACTA2 | myoepithelial cells | matched | M00265 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 69, Extended Data Fig. 7 |
| DOI_10.1038_s41588-022-01243-4 | formal_markers #9 | CCR10 | IgA plasma cells | matched | M00238 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 71-73, Fig. 5a-d |
| DOI_10.1038_s41588-022-01243-4 | formal_markers #10 | PIGR | SMG Serous Cell | context_only |  | 该位置讨论 CCL28/PIGR 的 IgA 招募/转运与细胞通讯；未证明其在本文用于所列细胞身份注释。；Main Text pp. 71-73, Fig. 5a, h |
| DOI_10.1038_s41588-024-01702-0 | formal_markers #1 | PTPRC | immune cells | matched | M00782 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Methods, Participants, samples and tissue processing; Data integration, clustering |
| DOI_10.1038_s41588-024-01702-0 | formal_markers #2 | EPCAM | epithelial cells | matched | M00781 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Methods, Data integration, clustering, cell type annotation |
| DOI_10.1038_s41588-024-01702-0 | formal_markers #3 | PECAM1 | endothelial cells | matched | M00779 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Methods, Data integration, clustering, cell type annotation |
| DOI_10.1038_s41588-024-01702-0 | formal_markers #4 | SPP1 | Macrophage − SPP1+ | matched | M00785 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text Fig. 1c, Fig. 2c, Table cell type list |
| DOI_10.1038_s41588-024-01702-0 | formal_markers #5 | WNT2 | WNT2+ FB | matched | M00794 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text Fig. 1c, Fig. 2c, Mesenchymal subclusters |
| DOI_10.1038_s41588-024-01702-0 | formal_markers #6 | CA4 | CA4+ capillary | matched | M00776 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text Fig. 1c, Fig. 2c, Endothelial subclustering |
| DOI_10.1038_s41588-024-01702-0 | formal_markers #7 | MUC5B | Secretory—SCGB1A1+/MUC5B+ | matched | M00789 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 598, Fig. 1c, Fig. 6 |
| DOI_10.1038_s41588-024-01702-0 | formal_markers #8 | SCGB3A2 | Secretory—SCGB1A1+/SCGB3A2+ | matched | M00792 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text Fig. 1c, Fig. 2c, Table |
| DOI_10.1038_s41588-024-01702-0 | formal_markers #9 | SCGB1A1 | Secretory—SCGB1A1+/MUC5B+ | matched | M00790 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text Fig. 1c, Fig. 2c, Table |
| DOI_10.1038_s41588-024-01702-0 | formal_markers #10 | KRT17 | KRT5−/KRT17+ | matched | M00783 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text Fig. 1c, Methods Disease interaction cell-type eQTL mapping |
| DOI_10.1038_s41588-025-02158-6 | formal_markers #1 | PHOX2B | Neuroblasts | matched | M01359 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 1143-1144, Fig. 1d, Extended Data Fig. 1c |
| DOI_10.1038_s41588-025-02158-6 | formal_markers #2 | ISL1 | Neuroblasts | matched | M01358 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1143, Fig. 1d |
| DOI_10.1038_s41588-025-02158-6 | formal_markers #3 | PLP1 | Schwann cells | matched | M01362 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1143, Fig. 1d |
| DOI_10.1038_s41588-025-02158-6 | formal_markers #4 | CDH19 | Schwann cell | add | M02570 | 已查看 Fig.1d，列标签与细胞对应明确。；Fig.1d, PDF p.2 |
| DOI_10.1038_s41588-025-02158-6 | formal_markers #5 | CD163 | Macrophages | matched | M01344 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1143, Fig. 1d; CODEX imaging Fig. 4 |
| DOI_10.1038_s41588-025-02158-6 | formal_markers #6 | CD86 | Macrophages | matched | M01336 | Fig.1d 确认 CD86 为 Macrophages；Gemini 该项正确，已修正旧表的 Dendritic cells。；Main Text p. 1143, Fig. 1d |
| DOI_10.1038_s41588-025-02158-6 | formal_markers #7 | IRF8 | Dendritic cells | matched | M01338 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1143, Fig. 1d |
| DOI_10.1038_s41588-025-02158-6 | formal_markers #8 | FLT3 | Dendritic cells | matched | M01337 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1143, Fig. 1d |
| DOI_10.1038_s41588-025-02158-6 | formal_markers #9 | PECAM1 | Endothelial cell | add | M02571 | 已查看 Fig.1d，列标签与细胞对应明确。；Fig.1d, PDF p.2 |
| DOI_10.1038_s41588-025-02158-6 | formal_markers #10 | PTPRB | Endothelial cells | matched | M01339 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1143, Fig. 1d |
| DOI_10.1038_s41588-025-02182-6 | formal_markers #1 | CHGA | Neuroendocrine cells | matched | M00070 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 1203-1204, Fig. 1j, Supplementary Table 5 |
| DOI_10.1038_s41588-025-02182-6 | formal_markers #2 | CHGA | Enteroendocrine cells | matched | M00068 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1203, Fig. 1j |
| DOI_10.1038_s41588-025-02182-6 | formal_markers #3 | ELAVL3 | Neural | matched | M01442 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1203, Fig. 1j |
| DOI_10.1038_s41588-025-02182-6 | formal_markers #4 | DEFA5 | Paneth cells | matched | M01444 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1203, Fig. 1j |
| DOI_10.1038_s41588-025-02182-6 | formal_markers #5 | DEFA6 | Paneth cells | matched | M01445 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1203, Fig. 1j |
| DOI_10.1038_s41588-025-02182-6 | formal_markers #6 | SFTPB | Alveolar type 2 cells | matched | M01402 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1203, Fig. 1j |
| DOI_10.1038_s41588-025-02182-6 | formal_markers #7 | HOPX | Alveolar type 1 cells | matched | M01401 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1203, Fig. 1j |
| DOI_10.1038_s41588-025-02182-6 | formal_markers #8 | PAX8 | Thyrocytes | matched | M01453 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1203, Fig. 1j |
| DOI_10.1038_s41588-025-02182-6 | formal_markers #9 | ASGR1 | Hepatocytes | matched | M01425 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1203, Fig. 1j |
| DOI_10.1038_s41588-025-02182-6 | formal_markers #10 | AVIL | Tuft cells | matched | M01454 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1203, Fig. 1j |
| DOI_10.1038_s41591-023-02327-2 | formal_markers #1 | CALCA | neuroendocrine cell | matched | M00055 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 1566-1567, Fig. 3f |
| DOI_10.1038_s41591-023-02327-2 | formal_markers #2 | FOXI1 | ionocyte | matched | M00715 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1567, Fig. 3f |
| DOI_10.1038_s41591-023-02327-2 | formal_markers #3 | LRMP | tuft cell | matched | M00727 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1567, Fig. 3f |
| DOI_10.1038_s41591-023-02327-2 | formal_markers #4 | CCR7 | migratory DCs | matched | M00717 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1567, Fig. 3g, Extended Data Fig. 4a-c |
| DOI_10.1038_s41591-023-02327-2 | formal_markers #5 | CCL19 | migratory DCs | matched | M00716 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Extended Data Fig. 4a-c |
| DOI_10.1038_s41591-023-02327-2 | formal_markers #6 | LAD1 | migratory DCs | matched | M00718 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Extended Data Fig. 4a-c |
| DOI_10.1038_s41591-023-02327-2 | formal_markers #7 | FAM83D | smooth muscle FAM83D+ | matched | M00724 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Extended Data Fig. 4e, f |
| DOI_10.1038_s41591-023-02327-2 | formal_markers #8 | SPP1 | monocyte-derived macrophages | matched | M00723 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Abstract p. 1563, Fig. 5 |
| DOI_10.1038_s41591-023-02327-2 | formal_markers #9 | MKI67 | Proliferating cells | add | M02572 | Extended Data Fig.2c 明确 MKI67 为 proliferating cells marker；保留增殖状态。；Extended Data Fig.2c caption |
| DOI_10.1038_s41591-023-02327-2 | formal_markers #10 | SCGB3A2 | preterminal bronchiole secretory cells | add | M02573 | 正文明确以组合表达描述 preterminal bronchiole secretory cells；保留具体亚群。；Results: HLCA core, Fig.3d/g |
| DOI_10.1038_s41591-024-03215-z | formal_markers #1 | EPCAM | epithelial cells | matched | M01309 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 3292, Methods; Extended Data Fig. 3a, b |
| DOI_10.1038_s41591-024-03215-z | formal_markers #2 | KRT8 | Epithelial breast cancer cells | add | M02574 | 正文明确 established epithelial BC marker genes，并在当前数据使用；标注上皮属性，不声明恶性专属性。；Results: comparison of single-cell and single-nucleus methods |
| DOI_10.1038_s41591-024-03215-z | formal_markers #3 | KRT18 | Epithelial breast cancer cells | add | M02575 | 正文明确 established epithelial BC marker genes，并在当前数据使用；标注上皮属性，不声明恶性专属性。；Results: comparison of single-cell and single-nucleus methods |
| DOI_10.1038_s41591-024-03215-z | formal_markers #4 | KRT19 | Epithelial breast cancer cells | add | M02576 | 正文明确 established epithelial BC marker genes，并在当前数据使用；标注上皮属性，不声明恶性专属性。；Results: comparison of single-cell and single-nucleus methods |
| DOI_10.1038_s41591-024-03215-z | formal_markers #5 | COL1A1 | Cancer-associated fibroblast | context_only |  | 所列 COL1A1/DCN/ACTA2 来自 iNMF EMT expression program 评分，不支持自动配为 fibroblast/myofibroblast 身份 marker。；Methods p. 3300, Scoring of expression programs |
| DOI_10.1038_s41591-024-03215-z | formal_markers #6 | DCN | Cancer-associated fibroblast | context_only |  | 所列 COL1A1/DCN/ACTA2 来自 iNMF EMT expression program 评分，不支持自动配为 fibroblast/myofibroblast 身份 marker。；Methods p. 3300 |
| DOI_10.1038_s41591-024-03215-z | formal_markers #7 | ACTA2 | Myofibroblast | context_only |  | 所列 COL1A1/DCN/ACTA2 来自 iNMF EMT expression program 评分，不支持自动配为 fibroblast/myofibroblast 身份 marker。；Methods p. 3300 |
| DOI_10.1038_s41591-024-03215-z | formal_markers #8 | CD68 | macrophages | matched | M01315 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 3294-3296, Fig. 3b, Fig. 4 |
| DOI_10.1038_s41591-024-03215-z | formal_markers #9 | CD163 | Macrophage | matched | M01311 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 3294-3296, Fig. 3b, Extended Data Fig. 10 |
| DOI_10.1038_s41591-024-03215-z | formal_markers #10 | SPP1 | Metastatic lesion macrophage | context_only |  | SPP1 的测序方法差异/表达状态分析不足以建立该 macrophage marker 关系。；Main Text p. 3292, Extended Data Fig. 3f |
| DOI_10.1038_s42003-021-02562-8 | formal_markers #1 | CYP3A4 | Hepatocytes | matched | M01323 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 3, Single-cell transcriptome landscape of HB |
| DOI_10.1038_s42003-021-02562-8 | formal_markers #2 | ALB | Hepatocytes | matched | M01321 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 3 |
| DOI_10.1038_s42003-021-02562-8 | formal_markers #3 | APOC3 | Hepatocytes | matched | M01322 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 3 |
| DOI_10.1038_s42003-021-02562-8 | formal_markers #4 | HPGD | Hepatocytes | matched | M01324 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 3 |
| DOI_10.1038_s42003-021-02562-8 | formal_markers #5 | FLT1 | Endothelial cells | matched | M01318 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 3 |
| DOI_10.1038_s42003-021-02562-8 | formal_markers #6 | COL3A1 | Hepatic stellate cells | matched | M01319 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 3 |
| DOI_10.1038_s42003-021-02562-8 | formal_markers #7 | COL6A3 | Hepatic stellate cells | matched | M01320 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 3 |
| DOI_10.1038_s42003-021-02562-8 | formal_markers #8 | CD68 | Kupffer cells | matched | M01327 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 3 |
| DOI_10.1038_s42003-021-02562-8 | formal_markers #9 | CD163 | Kupffer cells | matched | M01326 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 3 |
| DOI_10.1038_s42003-021-02562-8 | formal_markers #10 | GPC3 | Tumor cells | matched | M01329 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 2-3, Fig. 1c, e |
| DOI_10.1038_s42003-024-07315-x | formal_markers #1 | gda | cluster 4 | matched | M01834 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 5-7, Fig. 3h-j |
| DOI_10.1038_s42003-024-07315-x | formal_markers #2 | moxd1 | mono/Mϕ clusters 1, 2 and 7 | add | M02577 | 正文明确 moxd1 富集于 clusters 1/2/7，且 HCR 标示伤口表面；Gemini 的 cluster 6 原句错误。；Fig.3h/k; Results |
| DOI_10.1038_s42003-024-07315-x | formal_markers #3 | havcr1 | mono/Mϕ clusters 3, 4 and 6 | add | M02578 | Fig.3k HCR 验证联合 clusters 3/4/6 的空间关系，保留联合群；旧表仅 cluster6 不是同一粒度。；Fig.3k; Results |
| DOI_10.1038_s42003-024-07315-x | formal_markers #4 | lcp1 | lcp1+ macrophage | matched | M01853 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 6, Fig. 3h-k |
| DOI_10.1038_s42003-024-07315-x | formal_markers #5 | mpeg1.1 | zebrafish mono/Mphi | matched | M01883 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 6 |
| DOI_10.1038_s42003-024-07315-x | formal_markers #6 | tcf21 | epicardial cells and fibroblasts | matched | M01846 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 2 |
| DOI_10.1038_s42003-024-07315-x | formal_markers #7 | Timd4 | mm4 macrophages | matched | M01864 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 5, Fig. 2d |
| DOI_10.1038_s42003-024-07315-x | formal_markers #8 | Lyve1 | mm4 macrophages | matched | M01863 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 5, Fig. 2d |
| DOI_10.1038_s42003-024-07315-x | formal_markers #9 | Folr2 | mm4 macrophages | matched | M01862 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 5, Fig. 2d |
| DOI_10.1038_s42003-024-07315-x | formal_markers #10 | Ccr2 | Infiltrating monocyte / macrophage | unresolved |  | 已查看 Fig.2d：Ccr2 在多个小鼠 cluster 显示，图未将此列单独定义为 infiltrating 身份；旧表 ccr2 是斑马鱼 cluster4，不能跨物种匹配。；Main Text p. 5, Fig. 2d |
| DOI_10.1038_s42255-023-00876-x | formal_markers #1 | Ins1 | β | matched | M01619 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Methods p. 1630, Preprocessing of datasets for atlas building |
| DOI_10.1038_s42255-023-00876-x | formal_markers #2 | Ins2 | β | matched | M01620 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Methods p. 1630 |
| DOI_10.1038_s42255-023-00876-x | formal_markers #3 | Gcg | α | matched | M01612 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Methods p. 1630 |
| DOI_10.1038_s42255-023-00876-x | formal_markers #4 | Ttr | α-cell | matched | M01617 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1617, Extended Data Fig. 3c |
| DOI_10.1038_s42255-023-00876-x | formal_markers #5 | Sst | δ | matched | M01644 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Methods p. 1630 |
| DOI_10.1038_s42255-023-00876-x | formal_markers #6 | Rbp4 | δ-cell | matched | M01647 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1617, Extended Data Fig. 3c |
| DOI_10.1038_s42255-023-00876-x | formal_markers #7 | Ppy | γ | matched | M01641 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Methods p. 1630 |
| DOI_10.1038_s42255-023-00876-x | formal_markers #8 | Ghrl | ε | matched | M01651 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Methods p. 1630 |
| DOI_10.1038_s42255-023-00876-x | formal_markers #9 | Sox10 | Schwann | matched | M00096 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Methods p. 1630 |
| DOI_10.1038_s42255-023-00876-x | formal_markers #10 | Plp1 | Schwann | matched | M00095 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Methods p. 1630 |
| DOI_10.1126_science.aat5031 | formal_markers #1 | LCN2 | pelvic epithelium | add | M02579 | 已查看 Fig.2b 图注明确 AMPs amongst pelvic epithelium marker genes，LCN2 在该标记面板；不是仅凭功能共染。；Fig.2b, PDF p.15 |
| DOI_10.1126_science.aat5031 | formal_markers #2 | KRT17 | pelvic epithelium (PE) | matched | M01105 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1465, Fig. 4b |
| DOI_10.1126_science.aat5031 | formal_markers #3 | CXCL8 | Pelvic Epithelial Cell | context_only |  | CXCL8 共染用于抗菌/趋化功能，CK17 用于识别上皮；未建立独立注释用途。；Main Text p. 1465, Fig. 4a-b |
| DOI_10.1126_science.aat5031 | formal_markers #4 | CD14 | MNPa and MNPd | matched | M01101 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1463, Fig. 3c |
| DOI_10.1126_science.aat5031 | formal_markers #5 | FCGR3A | MNPb | matched | M01102 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1463, Fig. 3c |
| DOI_10.1126_science.aat5031 | formal_markers #6 | CLEC9A | MNP cluster | matched | M01096 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1463, Fig. 3c |
| DOI_10.1126_science.aat5031 | formal_markers #7 | CD1C | cDC2 | matched | M01092 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 1463, Fig. 3c |
| DOI_10.1126_science.aat5031 | formal_markers #8 | MRC1 | MNPd | add | M02580 | 正文及 Fig.3D 图注用 CD206+ 参与 MNPd 的实际分选；保留特定门控而非泛 tissue-resident。；Fig.3D caption |
| DOI_10.1126_science.aat5031 | formal_markers #9 | SLC12A1 | Thick Ascending Limb Epithelial Cell | unresolved |  | 已核所引 Fig.2a 是细胞转录相似性图，不含这些 transporter/podocyte 基因标签；现有正文未定位具体配对，需实际注释补充面板。；Main Text pp. 1461-1463, Fig. 1b, Fig. 2a |
| DOI_10.1126_science.aat5031 | formal_markers #10 | AQP2 | Collecting Duct Principal Cell | unresolved |  | 已核所引 Fig.2a 是细胞转录相似性图，不含这些 transporter/podocyte 基因标签；现有正文未定位具体配对，需实际注释补充面板。；Main Text pp. 1461-1463, Fig. 1b, Fig. 2a |
| DOI_10.1126_science.aat5031 | formal_markers #11 | SLC12A3 | Distal Convoluted Tubule Cell | unresolved |  | 已核所引 Fig.2a 是细胞转录相似性图，不含这些 transporter/podocyte 基因标签；现有正文未定位具体配对，需实际注释补充面板。；Main Text pp. 1461-1463, Fig. 1b, Fig. 2a |
| DOI_10.1126_science.aat5031 | formal_markers #12 | NPHS2 | Podocyte | unresolved |  | 已核所引 Fig.2a 是细胞转录相似性图，不含这些 transporter/podocyte 基因标签；现有正文未定位具体配对，需实际注释补充面板。；Main Text pp. 1461-1463, Fig. 1b, Fig. 2a |
| DOI_10.1126_science.abl4290 | formal_markers #1 | LYVE1 | MΦ LYVE1high | matched | M01467 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 4-6, Fig. 3a-c |
| DOI_10.1126_science.abl4290 | formal_markers #2 | F13A1 | MΦ LYVE1high | add | M02581 | 已查看 Fig.3E，F13A1 为 LYVE1hi macrophages 的 common marker；去除未证实的人类 perivascular 专属定位。；Fig.3E, PDF p.32 |
| DOI_10.1126_science.abl4290 | formal_markers #3 | HLA-DRA | MΦ HLAIIhigh | add | M02582 | 已查看 Fig.3E，HLA-DRA 为 HLAIIhi macrophage common marker。；Fig.3E, PDF p.32 |
| DOI_10.1126_science.abl4290 | formal_markers #4 | TREM2 | LAM-like macrophages | add | M02583 | 已查看 Fig.3B，TREM2 对应 LAM-like 标记群，保留 like 程度。；Fig.3B, PDF p.32 |
| DOI_10.1126_science.abl4290 | formal_markers #5 | DCN | Fibroblasts | add | M02584 | 已查看 Fig.4A，DCN 在作者定义的跨组织 fibroblast marker 面板。；Fig.4A, PDF p.34 |
| DOI_10.1126_science.abl4290 | formal_markers #6 | NPNT | Lung fibroblasts | add | M02585 | 已查看 Fig.4D 与图注，NPNT 是 lung fibroblast 的 most exclusive marker 展示；功能分析不取消此正式标记证据。；Fig.4D, PDF p.34 |
| DOI_10.1126_science.abl4290 | formal_markers #7 | SOX10 | Schwann Cell | unresolved |  | 当前正文/所引概览图未充分定位这些基因到所述细胞的注释证据；不能将经典 marker 常识补成论文原句。；Main Text pp. 2-4, Fig. 1c, g |
| DOI_10.1126_science.abl4290 | formal_markers #8 | TTN | Skeletal Muscle Myonucleus | unresolved |  | 当前正文/所引概览图未充分定位这些基因到所述细胞的注释证据；不能将经典 marker 常识补成论文原句。；Main Text pp. 2-4, Fig. 1c, Fig. 5a |
| DOI_10.1126_science.abl4290 | formal_markers #9 | TNNT2 | Cardiomyocyte | unresolved |  | 当前正文/所引概览图未充分定位这些基因到所述细胞的注释证据；不能将经典 marker 常识补成论文原句。；Main Text pp. 2-4, Fig. 1c, Fig. 5a |
| DOI_10.1126_science.abl4290 | formal_markers #10 | ACTA2 | Vascular Smooth Muscle Cell | unresolved |  | 当前正文/所引概览图未充分定位这些基因到所述细胞的注释证据；不能将经典 marker 常识补成论文原句。；Main Text pp. 2-4, Fig. 1c, Fig. 5a |
| DOI_10.7554_elife.62522 | formal_markers #1 | TMPRSS2 | Alveolar type 2 cell | context_only |  | 这些是病毒进入/易感性/年龄调控研究的被测功能基因；表达或开放染色质不自动成为身份 marker。；Main Text pp. 3-5, Fig. 2, Fig. 3 |
| DOI_10.7554_elife.62522 | formal_markers #2 | ACE2 | Alveolar type 2 cell | context_only |  | 这些是病毒进入/易感性/年龄调控研究的被测功能基因；表达或开放染色质不自动成为身份 marker。；Main Text p. 3, Fig. 2A, Fig. 3B |
| DOI_10.7554_elife.62522 | formal_markers #3 | SLC6A20 | Alveolar type 2 cell | context_only |  | 这些是病毒进入/易感性/年龄调控研究的被测功能基因；表达或开放染色质不自动成为身份 marker。；Main Text pp. 7-9, Fig. 4, L517 |
| DOI_10.7554_elife.62522 | formal_markers #4 | CTSL | Lung macrophage | context_only |  | 这些是病毒进入/易感性/年龄调控研究的被测功能基因；表达或开放染色质不自动成为身份 marker。；Main Text pp. 3-4, Fig. 2 |
| DOI_10.7554_elife.62522 | formal_markers #5 | BSG | Lung endothelial cell | context_only |  | 这些是病毒进入/易感性/年龄调控研究的被测功能基因；表达或开放染色质不自动成为身份 marker。；Main Text pp. 3-4, Fig. 2 |
| DOI_10.7554_elife.62522 | formal_markers #6 | FURIN | Airway epithelial cell | context_only |  | 这些是病毒进入/易感性/年龄调控研究的被测功能基因；表达或开放染色质不自动成为身份 marker。；Main Text pp. 3-4, Fig. 2 |
| DOI_10.7554_elife.62522 | formal_markers #7 | CALCA | Pulmonary neuroendocrine cell | unresolved |  | 已查看 Fig.1B/D：PNEC 标签是 ASCL1/CHGB，未见 CALCA/CHGA；补图可能另有证据，当前不猜测。；Main Text p. 3, Fig. 1A-D, Figure supplement 2 |
| DOI_10.7554_elife.62522 | formal_markers #8 | CHGA | Pulmonary neuroendocrine cell | unresolved |  | 已查看 Fig.1B/D：PNEC 标签是 ASCL1/CHGB，未见 CALCA/CHGA；补图可能另有证据，当前不猜测。；Main Text p. 3, Fig. 1B, D |
| DOI_10.7554_elife.62522 | formal_markers #9 | SFTPC | Alveolar type 2 cell | add | M02586 | 已查看 Fig.1B/D，作者图注明确用于 cluster annotation；可读基因标签与细胞一致。；Fig.1B/D, PDF p.4 |
| DOI_10.7554_elife.62522 | formal_markers #10 | AGER | Alveolar type 1 cell | add | M02587 | 已查看 Fig.1B/D，作者图注明确用于 cluster annotation；可读基因标签与细胞一致。；Fig.1B/D, PDF p.4 |
| PMID_35115729 | formal_markers #1 | Pmp2 | myelinating Schwann cell (mSC) | matched | M00084 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 242-246, Fig. 4a, Fig. 5a-b, Fig. 6a-h |
| PMID_35115729 | formal_markers #2 | Cldn14 | myelinating Schwann cell (mSC) | matched | M00082 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 242, Fig. 4a, Fig. 6a |
| PMID_35115729 | formal_markers #3 | Adamtsl1 | myelinating Schwann cell (mSC) | matched | M00083 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 242, Fig. 4a, Fig. 6a |
| PMID_35115729 | formal_markers #4 | Mbp | myelinating Schwann cell (mSC) | matched | M00078 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 243-245, Fig. 5a-b, Fig. 6c-d, Fig. 7j |
| PMID_35115729 | formal_markers #5 | Prx | myelinating Schwann cell (mSC) | matched | M00076 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 240, Fig. 2d, g |
| PMID_35115729 | formal_markers #6 | Scn7a | non-myelinating Schwann cell (nmSC) | matched | M00087 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 240-241, Fig. 2d-i, Fig. 3a-d |
| PMID_35115729 | formal_markers #7 | Cd34 | endoneurial/epineurial fibroblasts | matched | M01517 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 240, Fig. 2c-i |
| PMID_35115729 | formal_markers #8 | Pdgfra | endoneurial fibroblasts (EFs) | matched | M01516 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text p. 240, Fig. 2c-i |
| PMID_35115729 | formal_markers #9 | Slc2a1 | perineurial fibroblasts | matched | M01529 | 与已有关系对应；采用原表的细胞/亚群及物种粒度，未重复新增。；Main Text pp. 239-241, Fig. 1e, Fig. 3b |
| PMID_35115729 | formal_markers #10 | Clec3b | Epineurial Fibroblast | unresolved |  | 当前主文未找到 Clec3b；候选引文不足以验证其 epineurial 配对，不能由 sheath 位置补写。；Main Text pp. 239-241, Fig. 1e, Fig. 3b |
| PMID_35115729 | formal_markers #11 | PMP2 | Myelinating Schwann cells | add | M02588 | 正文及 Fig.5g-k 明确人 PMP2+ mSC 亚群与厚髓鞘/大直径轴突关联；人证据不强化为已证明的 motor 专属。；Results; Fig.5g-k |
| PMID_35115729 | context_only #1 | Tubb3 | Axons | add | M02589 | 正文明确 β-tubulin III (β-tub) to highlight axons，是实际轴突定位标记；保留蛋白实体。；Results; Fig.5a/b |
| PMID_35115729 | context_only #2 | Chat | Motor Axon | matched | M01525 | ChAT 实际用于 motor axon 识别；恢复正式关系。；Main Text pp. 245-247, Fig. 6e-h, Fig. 7a-f |
| PMID_35115729 | excluded #1 | Ngfr | Non-Myelinating Schwann Cell | matched | M00093 | Ngfr 亦表达于 EF 不取消其 nmSC marker 身份；不能以不独有作为排除门槛。；Main Text p. 240, Fig. 2c-i |

## 原表处置

|ID|处理|理由|
|---|---|---|
| M00013 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00014 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00015 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00016 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00017 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00018 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00019 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00020 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00021 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00022 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00023 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00024 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00025 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00029 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00030 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00031 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00032 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00033 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00034 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00035 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00036 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00037 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00038 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00039 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00040 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00041 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00042 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00043 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00044 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00045 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00046 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00047 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00048 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00049 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00050 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00051 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00055 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00056 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00057 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00060 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00061 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00068 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00069 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00070 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00071 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00072 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00073 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00074 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00075 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00076 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00077 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00078 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00079 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00080 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00081 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00082 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00083 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00084 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00085 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00086 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00087 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00088 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00089 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00090 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00091 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00092 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00093 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00094 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00095 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00096 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00097 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00228 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00229 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00230 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00231 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00232 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00233 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00234 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00235 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00236 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00237 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00238 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00239 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00240 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00241 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00242 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00243 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00246 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00247 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00248 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00249 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00250 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00251 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00252 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00253 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00254 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00255 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00256 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00257 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00258 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00259 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00260 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00261 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00262 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00263 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00264 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00265 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00266 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00267 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00268 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00269 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00270 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00271 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00272 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00273 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00274 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00275 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00276 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00277 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00278 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00279 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00280 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00281 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00282 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00283 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00284 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00285 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00286 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00287 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00288 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00289 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00290 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00291 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00292 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00293 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00294 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00295 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00296 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00298 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00331 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00332 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00333 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00334 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00335 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00336 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00337 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00338 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00339 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00340 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00341 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00342 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00343 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00344 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00345 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00346 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00347 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00348 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00349 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00350 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00351 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00352 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00353 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00354 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00355 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00356 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00357 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00358 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00359 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00360 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00361 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00362 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00363 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00364 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00365 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00366 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00367 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00368 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00369 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00370 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00371 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00372 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00373 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00374 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00375 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00376 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00377 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00378 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00379 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00380 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00381 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00382 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00383 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00384 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00385 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00386 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00387 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00388 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00389 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00390 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00391 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00392 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00393 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00394 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00395 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00396 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00397 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00398 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00399 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00400 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00401 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00402 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00403 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00404 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00405 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00406 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00407 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00408 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00411 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00412 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00413 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00414 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00415 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00416 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00417 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00418 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00419 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00420 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00421 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00422 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00423 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00424 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00425 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00426 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00427 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00428 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00429 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00430 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00431 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00432 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00433 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00434 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00435 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00436 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00437 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00438 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00439 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00440 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00441 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00442 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00443 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00444 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00445 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00446 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00447 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00448 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00449 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00450 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00451 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00452 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00453 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00454 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00455 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00456 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00457 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00458 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00459 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00460 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00461 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00462 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00463 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00464 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00465 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00466 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00467 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00468 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00469 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00470 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00471 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00472 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00473 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00474 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00475 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00476 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00477 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00478 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00479 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00480 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00481 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00482 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00483 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00484 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00485 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00486 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00487 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00488 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00489 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00490 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00491 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00492 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00493 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00494 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00495 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00496 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00497 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00498 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00499 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00500 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00501 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00502 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00503 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00504 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00505 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00506 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00507 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00508 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00509 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00510 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00511 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00512 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00513 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00514 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00515 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00516 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00517 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00518 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00519 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00520 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00521 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00522 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00523 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00524 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00525 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00526 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00527 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00528 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00529 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00530 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00531 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00532 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00533 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00534 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00535 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00536 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00537 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00538 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00539 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00540 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00541 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00542 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00543 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00544 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00545 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00546 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00547 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00548 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00549 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00550 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00551 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00552 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00553 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00554 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00555 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00556 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00557 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00558 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00559 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00560 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00561 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00562 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00563 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00564 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00565 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00566 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00567 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00568 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00569 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00570 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00571 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00572 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00573 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00574 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00575 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00576 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00577 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00578 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00579 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00580 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00581 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00582 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00583 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00584 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00585 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00586 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00587 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00588 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00589 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00590 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00591 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00592 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00593 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00594 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00595 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00596 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00597 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00702 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00703 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00704 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00705 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00706 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00707 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00708 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00709 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00710 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00711 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00712 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00713 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00714 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00715 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00716 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00717 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00718 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00719 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00720 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00721 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00722 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00723 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00724 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00725 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00726 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00727 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00728 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00729 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00730 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00731 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00732 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00733 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00734 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00735 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00736 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00737 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00738 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00739 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00740 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00741 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00742 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00743 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00744 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00745 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00746 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00747 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00748 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00749 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00750 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00751 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00752 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00753 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00754 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00755 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00756 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00757 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00758 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00759 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00760 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00761 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00762 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00763 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00764 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00765 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00766 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00767 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00768 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00769 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00770 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00771 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00772 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00773 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00774 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00775 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00776 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00777 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00778 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00779 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00780 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00781 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00782 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00783 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00784 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00785 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00786 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00787 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00788 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00789 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00790 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00791 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00792 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00793 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00794 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00795 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00796 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00797 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00798 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00799 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00800 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00801 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00802 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00803 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00804 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00805 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00806 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00807 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00808 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00809 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00810 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00811 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00812 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00813 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00814 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00815 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00816 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00817 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00818 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00819 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00820 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00821 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00822 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00823 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00824 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00825 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00826 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00827 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00828 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00829 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00830 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00831 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00832 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00833 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00834 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00835 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00836 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00837 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00838 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00839 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00840 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00841 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00842 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00843 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00844 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00845 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00846 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00847 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00848 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00849 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00850 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00851 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00852 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00853 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00854 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00855 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00856 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00857 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00858 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00859 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00860 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00861 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00862 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00863 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00864 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00865 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00866 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00867 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00868 | correct | 正文对 CD44+CD36+ 晚期远端群描述 SOX2 extremely low，不能记作一般阳性。 |
| M00869 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00870 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00871 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00872 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00873 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00874 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00875 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00876 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00877 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00878 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00879 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00880 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00881 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00882 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00883 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00884 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00885 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00886 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00887 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00888 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00889 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00890 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00891 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00892 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00893 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00894 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00895 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00896 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00897 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00898 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00899 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00900 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00901 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00902 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00903 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00904 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00905 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00906 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00907 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00908 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00909 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00910 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00911 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00912 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00913 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00914 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00915 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00916 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00917 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00918 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00919 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00920 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00921 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00922 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00923 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00924 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00925 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00926 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00927 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00928 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00929 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00930 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00931 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00932 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00933 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00934 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00935 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00936 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00937 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00938 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00939 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00940 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00941 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00942 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00943 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00944 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00945 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00946 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00947 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00948 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00949 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00950 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00951 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00952 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00953 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00954 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00955 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00956 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00957 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00958 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00959 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00960 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00961 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00962 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00963 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00964 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00965 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00966 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00967 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00968 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00969 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00970 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00971 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00972 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00973 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00974 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00975 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00976 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00977 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00978 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00979 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00980 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00981 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00982 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00983 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00984 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00985 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00986 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00987 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00988 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00989 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00990 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00991 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00992 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00993 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00994 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00995 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00996 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00997 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00998 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M00999 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01000 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01001 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01002 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01003 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01004 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01005 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01006 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01007 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01008 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01009 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01010 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01011 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01012 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01013 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01014 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01015 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01016 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01017 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01018 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01019 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01020 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01021 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01022 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01023 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01024 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01025 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01026 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01027 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01028 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01029 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01030 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01031 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01032 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01033 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01034 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01035 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01036 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01037 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01038 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01090 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01091 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01092 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01093 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01094 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01095 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01096 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01097 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01098 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01099 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01100 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01101 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01102 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01103 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01104 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01105 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01106 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01107 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01108 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01109 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01110 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01111 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01112 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01113 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01114 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01115 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01116 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01117 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01118 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01119 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01120 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01121 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01122 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01123 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01124 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01125 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01126 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01127 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01128 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01129 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01130 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01131 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01132 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01133 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01134 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01135 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01136 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01137 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01138 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01139 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01140 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01141 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01142 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01143 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01144 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01145 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01146 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01147 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01148 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01149 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01150 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01151 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01152 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01153 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01154 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01155 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01156 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01157 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01158 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01159 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01160 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01161 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01162 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01163 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01164 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01165 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01166 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01167 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01168 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01169 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01170 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01171 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01172 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01173 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01174 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01175 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01176 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01177 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01178 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01179 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01180 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01181 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01182 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01183 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01303 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01304 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01305 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01307 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01308 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01309 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01310 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01311 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01312 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01313 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01315 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01316 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01317 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01318 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01319 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01320 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01321 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01322 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01323 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01324 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01325 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01326 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01327 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01328 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01329 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01330 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01331 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01332 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01333 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01334 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01335 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01336 | correct | 已查看 Fig.1d，CD86 对应 Macrophages，原 Dendritic cells 为错配。 |
| M01337 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01338 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01339 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01340 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01341 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01342 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01343 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01344 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01345 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01346 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01347 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01348 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01349 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01350 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01351 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01352 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01353 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01354 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01355 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01356 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01357 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01358 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01359 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01360 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01361 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01362 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01363 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01364 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01399 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01400 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01401 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01402 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01403 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01404 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01405 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01406 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01407 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01408 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01409 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01410 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01411 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01412 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01413 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01414 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01415 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01416 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01417 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01418 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01419 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01420 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01421 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01422 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01423 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01424 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01425 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01426 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01427 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01428 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01429 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01430 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01431 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01432 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01433 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01434 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01435 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01436 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01437 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01438 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01439 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01440 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01441 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01442 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01443 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01444 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01445 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01446 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01447 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01448 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01449 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01450 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01451 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01452 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01453 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01454 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01455 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01456 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01457 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01458 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01459 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01460 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01461 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01462 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01463 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01464 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01465 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01466 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01467 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01468 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01469 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01470 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01510 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01511 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01512 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01513 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01514 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01515 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01516 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01517 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01518 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01519 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01520 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01521 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01522 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01523 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01524 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01525 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01526 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01527 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01528 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01529 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01530 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01531 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01535 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01584 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01585 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01586 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01587 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01588 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01589 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01590 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01591 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01592 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01593 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01594 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01595 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01596 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01597 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01598 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01599 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01600 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01601 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01602 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01603 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01604 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01605 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01606 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01607 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01608 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01609 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01610 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01611 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01612 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01613 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01614 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01615 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01616 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01617 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01618 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01619 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01620 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01621 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01622 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01623 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01624 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01625 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01626 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01627 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01628 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01629 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01630 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01631 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01632 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01633 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01634 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01635 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01636 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01637 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01638 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01639 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01640 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01641 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01642 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01643 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01644 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01645 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01646 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01647 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01648 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01649 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01650 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01651 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01652 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01653 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01654 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01655 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01656 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01657 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01658 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01659 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01660 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01661 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01662 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01663 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01664 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01665 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01666 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01667 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01668 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01669 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01670 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01671 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01672 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01673 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01674 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01675 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01676 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01677 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01678 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01679 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01680 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01681 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01682 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01683 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01684 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01685 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01686 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01687 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01688 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01689 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01690 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01691 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01692 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01693 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01694 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01695 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01696 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01697 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01698 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01699 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01700 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01701 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01702 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01703 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01704 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01705 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01706 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01707 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01708 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01709 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01710 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01711 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01712 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01713 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01714 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01715 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01716 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01717 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01718 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01719 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01720 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01721 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01722 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01723 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01724 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01725 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01726 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01727 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01728 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01729 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01730 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01731 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01732 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01733 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01734 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01735 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01736 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01737 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01738 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01739 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01740 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01741 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01742 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01743 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01744 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01745 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01746 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01747 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01748 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01749 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01750 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01751 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01752 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01753 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01754 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01755 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01756 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01757 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01758 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01759 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01760 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01761 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01762 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01763 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01764 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01765 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01766 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01767 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01768 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01769 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01770 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01771 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01772 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01773 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01774 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01775 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01776 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01777 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01778 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01779 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01780 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01781 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01782 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01783 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01784 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01785 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01786 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01787 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01788 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01789 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01790 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01791 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01792 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01793 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01794 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01795 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01796 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01797 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01798 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01799 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01800 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01801 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01802 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01803 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01804 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01805 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01806 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01807 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01808 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01809 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01810 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01811 | correct | Fig.3及正文明确为 zebrafish，补全历史 other 物种字段；未转换基因大小写。 |
| M01812 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01813 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01814 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01815 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01816 | correct | Fig.3及正文明确为 zebrafish，补全历史 other 物种字段；未转换基因大小写。 |
| M01817 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01818 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01819 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01820 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01821 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01822 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01823 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01824 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01825 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01826 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01827 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01828 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01829 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01830 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01831 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01832 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01833 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01834 | correct | Fig.3及正文明确为 zebrafish，补全历史 other 物种字段；未转换基因大小写。 |
| M01835 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01836 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01837 | correct | Fig.3及正文明确为 zebrafish，补全历史 other 物种字段；未转换基因大小写。 |
| M01838 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01839 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01840 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01841 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01842 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01843 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01844 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01845 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01846 | correct | Fig.3及正文明确为 zebrafish，补全历史 other 物种字段；未转换基因大小写。 |
| M01847 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01848 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01849 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01850 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01851 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01852 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01853 | correct | Fig.3及正文明确为 zebrafish，补全历史 other 物种字段；未转换基因大小写。 |
| M01854 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01855 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01856 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01857 | correct | Fig.3及正文明确为 zebrafish，补全历史 other 物种字段；未转换基因大小写。 |
| M01858 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01859 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01860 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01861 | correct | Fig.3及正文明确为 zebrafish，补全历史 other 物种字段；未转换基因大小写。 |
| M01862 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01863 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01864 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01865 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01866 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01867 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01868 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01869 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01870 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01871 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01872 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01873 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01874 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01875 | correct | Fig.3及正文明确为 zebrafish，补全历史 other 物种字段；未转换基因大小写。 |
| M01876 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01877 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01878 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01879 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01880 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01881 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01882 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01883 | correct | Fig.3及正文明确为 zebrafish，补全历史 other 物种字段；未转换基因大小写。 |
| M01884 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01885 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01894 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01895 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01896 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01897 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |
| M01898 | retain | 保留既有证据；Gemini 未列出不代表无效，本轮未重提取未涉及的关系。 |

## 交付核验

两份正式文件已写回并通过 SHA256 一致性检查。总表2499条、43篇；按细胞表1046行。已验证完整单元格值、12条修正范围、49条新增审计记录、历史审计与原样式保留、表格范围及统计缓存；非目标1177条主表记录和455条派生记录保持原值。三次复核报告合计覆盖43个JSON且无重复，43份输入文件哈希均未变化。最终两表渲染已检查。
