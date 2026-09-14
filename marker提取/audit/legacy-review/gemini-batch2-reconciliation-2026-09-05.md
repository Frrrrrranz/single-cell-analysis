# Gemini 第二批十篇差异裁决

仅核对既有 JSON、总表及相关原文/原图，不调用模型重新提取，不宣称穷尽所有 marker。
总表 2416 → 2474 条；新增 70 条；移出/去重 12 条。

## 逐篇统计

|论文|原表|正式候选|全部候选|匹配|新增|上下文|排除|未决|更新后|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| DOI_10.1002_pros.24020 | 14 | 14 | 16 | 7 | 6 | 2 | 0 | 1 | 20 |
| DOI_10.1016_j.celrep.2018.11.086 | 29 | 21 | 23 | 16 | 3 | 4 | 0 | 0 | 30 |
| DOI_10.1038_s41586-020-2496-1 | 0 | 19 | 20 | 0 | 8 | 11 | 0 | 1 | 8 |
| DOI_10.1038_s41586-021-03710-0 | 18 | 14 | 16 | 9 | 4 | 2 | 1 | 0 | 22 |
| DOI_10.1038_s41586-021-03929-x | 34 | 13 | 13 | 6 | 5 | 0 | 0 | 2 | 34 |
| DOI_10.1126_science.abo0510 | 39 | 18 | 21 | 12 | 8 | 1 | 0 | 0 | 45 |
| DOI_10.1164_rccm.202207-1384oc | 35 | 13 | 15 | 8 | 4 | 2 | 0 | 1 | 37 |
| DOI_10.7554_elife.71752 | 29 | 29 | 33 | 12 | 17 | 3 | 0 | 1 | 45 |
| PMID_37120427 | 0 | 12 | 13 | 0 | 11 | 1 | 0 | 1 | 11 |
| PMID_37664243 | 0 | 12 | 15 | 0 | 4 | 8 | 1 | 2 | 4 |

## 关键结果与限制

- Walkthrough 是 Gemini 自述，不是证据质检。其多篇摘要与实际 JSON 不一致，例如 eLife 排除项实际 MRGPRD（摘要写 TAC1），远端气道排除项实际 Scgb3a2（摘要写 KRT5）；本轮以 JSON 和论文为准。
- 165 条 formal 候选之外，13 条 context、6 条 excluded、1 条 unresolved 均已复核分类。门控/原位定位同样可以是正式 Marker；低特异性不自动排除。
- 肺 Fig.1E 的 TPSB2 被误写为 TPSAB1，已按原图修正；TUBB4 不能直接唯一指认为 TUBB4A，保留未决。
- 前列腺 Fig.4C 无 PIGR/AKR1C1，Fig.3C 无 FGF7，不能继承 Gemini 的 qPCR 验证声明；仅 top-DEG/功能证据保留上下文。
- Fig.S21-S23 明确支持胎儿免疫祖细胞验证；CDH5 用于内皮定位，恢复正式候选。B1 实际门控为 CD3−CD20+、排除最高1% CD38、CCR10loCD27+CD43+，并非 Gemini 声称的完整门控。
- 胎骨髓 Fig.1b 的基因与细胞粒度已对原图核对；CD15 糖抗原→FUT4 不能未经唯一映射验证入表。CD45RA 仅代表蛋白异构体门控，不能解释为全 PTPRC 阴性。
- 胎骨髓 CD34 的 diaphyseal sinusoids 正文 low / 图注 high 冲突，旧两行归档未决；VEGFR2lo 和 Plasma MS4A1lo 恢复 low。
- eLife PRP1 原表条目归档未决，不采用 PRPH 猜测。共享 H14/H15、H10/H11 关系保留联合群；不将原文推测的 proprioceptor 身份强化为已确定。
- 三篇原表无记录。Tabula Muris 对应任务43；两个 PMID 对应任务37的两篇独立论文，保留独立 paper_id。文章登记表历史接入状态本轮未覆盖。
- Gemini 没有列出的原表关系保留既有证据，仅修正已发现的直接错误与重复；不以缺席判无效。缺失补充表没有补抓，无证据的配对保留未决。
- 第一批成果、其他论文行及历史审计表保留。完整原候选、原表快照和裁决理由保存在配套 JSON。

## 全部候选裁决

|论文|原分类/序号|基因|细胞|结果|对应ID|理由|
|---|---|---|---|---|---|---|
| DOI_10.1002_pros.24020 | formal_markers #1 | Krt4 | Urethral Luminal Epithelial Cell | matched | M01195 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text pp. 4-6, Fig. 1D, Fig. 2A, Fig. 4A-C |
| DOI_10.1002_pros.24020 | formal_markers #2 | Tacstd2 | Urethral Luminal Epithelial Cell | matched | M01196 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text pp. 7-8, Fig. 2C, Fig. 3B-E, Fig. S4E |
| DOI_10.1002_pros.24020 | formal_markers #3 | Ly6d | Urethral Luminal Epithelial Cell | add | M02495 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 6, Fig. 2C |
| DOI_10.1002_pros.24020 | formal_markers #4 | Krt19 | Urethral Luminal Epithelial Cell | context_only |  | Results 3.3 仅讨论 Krt19 在 urethral luminal 富集及历史 intermediate 解释，未提供独立注释用途。；Main Text p. 6, Fig. 2C |
| DOI_10.1002_pros.24020 | formal_markers #5 | Nkx3-1 | Secretory Prostate Luminal Epithelial Cell | matched | M01194 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text pp. 5-6, Fig. 1D, Fig. 2A, Fig. S4B |
| DOI_10.1002_pros.24020 | formal_markers #6 | Dpp4 | Secretory Prostate Luminal Epithelial Cell | matched | M01193 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 7, Fig. 2C, Fig. 3B, Fig. S4A |
| DOI_10.1002_pros.24020 | formal_markers #7 | Msmb | Dorsolateral Prostate Luminal Cell | add | M02496 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 4, Fig. 1D |
| DOI_10.1002_pros.24020 | formal_markers #8 | Tgm4 | Anterior Prostate Luminal Cell | add | M02497 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 4, Fig. 1D |
| DOI_10.1002_pros.24020 | formal_markers #9 | Sbp | Ventral Prostate Luminal Cell | add | M02498 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 4, Fig. 1D |
| DOI_10.1002_pros.24020 | formal_markers #10 | Svs2 | Seminal Vesicle and Ejaculatory Duct Luminal Cell | add | M02499 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 4, Fig. 1D |
| DOI_10.1002_pros.24020 | formal_markers #11 | SCGB1A1 | Club Urethral Luminal Epithelial Cell | matched | M01188 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text pp. 8-10, Fig. 4D-F, Fig. 5A, Fig. 5D-F |
| DOI_10.1002_pros.24020 | formal_markers #12 | KRT13 | Hillock Urethral Luminal Epithelial Cell | matched | M01189 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text pp. 5-10, Fig. 2B, Fig. 4D-F, Fig. 5D-F |
| DOI_10.1002_pros.24020 | formal_markers #13 | PSCA | Club and Hillock Urethral Luminal Epithelial Cell | matched | M01191 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 9, Fig. 5B |
| DOI_10.1002_pros.24020 | formal_markers #14 | Calca | Neuroendocrine Epithelial Cell | unresolved |  | 正文明确 CGRP/CHGA，但未唯一确认 CGRP 对应 Calca 及所指物种面板；未查看的 S3 不能作为已核验基因映射。；Main Text p. 4, Fig. S3A-D |
| DOI_10.1002_pros.24020 | context_only #1 | Ly6a | Urethral Luminal Epithelial Cell | add | M02500 | Discussion 明确 urethral luminal cell type expresses markers Sca-1/Trop2/LY6D/KRT4；Sca-1 不独有不妨碍纳入该关系。；Results 3.3 Fig.2C; Discussion |
| DOI_10.1002_pros.24020 | excluded #1 | Prom1 | Seminal Vesicle and Ejaculatory Duct Luminal Cell | context_only |  | 否定其前列腺干细胞用途不等于否定 SV/ED 的表达；当前 SV/ED 配对证据仅 enrichment，保留上下文。；Main Text p. 6, Fig. 2C |
| DOI_10.1016_j.celrep.2018.11.086 | formal_markers #1 | KRT5 | Basal Epithelial Cell | matched | M01199 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 3531, Fig. 1C, Fig. 3E, Fig. 4F, Fig. 5E |
| DOI_10.1016_j.celrep.2018.11.086 | formal_markers #2 | KRT14 | Basal Epithelial Cell | matched | M01198 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 3537, Fig. 1C, Fig. 4B, Fig. 4C, Fig. 4F |
| DOI_10.1016_j.celrep.2018.11.086 | formal_markers #3 | TP63 | Basal Epithelial Cell | add | M02501 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 3530, p. 3531 |
| DOI_10.1016_j.celrep.2018.11.086 | formal_markers #4 | PDPN | Basal Epithelial Cell | matched | M01201 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text pp. 3533-3535, Fig. 2D-G |
| DOI_10.1016_j.celrep.2018.11.086 | formal_markers #5 | KLK3 | Luminal Epithelial Cell | matched | M01215 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 3530, Fig. 1C, Fig. 4A-C |
| DOI_10.1016_j.celrep.2018.11.086 | formal_markers #6 | ACPP | Luminal Epithelial Cell | add | M02502 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 3531, Fig. 1C, Fig. 4B, Fig. 4C |
| DOI_10.1016_j.celrep.2018.11.086 | formal_markers #7 | DHRS7 | Luminal Epithelial Cell | matched | M01213 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 3536, Fig. 1C, Fig. 4F |
| DOI_10.1016_j.celrep.2018.11.086 | formal_markers #8 | DPP4 | Luminal Epithelial Cell | matched | M01214 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text pp. 3533-3535, Fig. 2A-G |
| DOI_10.1016_j.celrep.2018.11.086 | formal_markers #9 | SCGB1A1 | Club Epithelial Cell | matched | M01203 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text pp. 3536-3538, Fig. 1C, Fig. 4B, Fig. 4C, Fig. 4F, Fig. 5E |
| DOI_10.1016_j.celrep.2018.11.086 | formal_markers #10 | PIGR | Club Epithelial Cell | context_only |  | 原图 Fig.4B/3B 为 top-DEG 或功能讨论；Fig.4C/3C 实际 qPCR 面板没有该基因，Gemini 的验证描述不成立。；Main Text p. 3532, Fig. 1C, Fig. 4B, Fig. 4C |
| DOI_10.1016_j.celrep.2018.11.086 | formal_markers #11 | KRT13 | Hillock Epithelial Cell | matched | M01210 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text pp. 3536-3538, Fig. 1C, Fig. 4B, Fig. 4C, Fig. 4F, Fig. 5E |
| DOI_10.1016_j.celrep.2018.11.086 | formal_markers #12 | AKR1C1 | Hillock Epithelial Cell | context_only |  | 原图 Fig.4B/3B 为 top-DEG 或功能讨论；Fig.4C/3C 实际 qPCR 面板没有该基因，Gemini 的验证描述不成立。；Main Text p. 3538, Fig. 1C, Fig. 4B, Fig. 4C |
| DOI_10.1016_j.celrep.2018.11.086 | formal_markers #13 | PSCA | Club Epithelial Cell / Hillock Epithelial Cell | matched | M01202,M01211 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 3533, p. 3538, Fig. 2E-G, Fig. 5C-D |
| DOI_10.1016_j.celrep.2018.11.086 | formal_markers #14 | CHGA | Neuroendocrine Epithelial Cell | matched | M00063 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 3533, Fig. S6D |
| DOI_10.1016_j.celrep.2018.11.086 | formal_markers #15 | SCG2 | Neuroendocrine Epithelial Cell | matched | M00064 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 3533, Fig. S6D |
| DOI_10.1016_j.celrep.2018.11.086 | formal_markers #16 | DCN | Fibroblast | matched | M01208 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text pp. 3535-3536, Fig. 1C, Fig. 3B, Fig. 3C, Fig. 3E, Fig. 5E |
| DOI_10.1016_j.celrep.2018.11.086 | formal_markers #17 | PDPN | Fibroblast | matched | M01209 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 3533, Fig. 2D, Fig. 3C |
| DOI_10.1016_j.celrep.2018.11.086 | formal_markers #18 | FGF7 | Fibroblast | context_only |  | 原图 Fig.4B/3B 为 top-DEG 或功能讨论；Fig.4C/3C 实际 qPCR 面板没有该基因，Gemini 的验证描述不成立。；Main Text p. 3536, Fig. 3B, Fig. 3C |
| DOI_10.1016_j.celrep.2018.11.086 | formal_markers #19 | MYH11 | Smooth Muscle Cell | matched | M01219 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text pp. 3535-3536, Fig. 1C, Fig. 3B, Fig. 3C, Fig. 3E |
| DOI_10.1016_j.celrep.2018.11.086 | formal_markers #20 | ACTA2 | Smooth Muscle Cell | add | M02503 | Results 用 ACTA2/MYH11 等建立 putative smooth muscle 身份；Fig.3C 确有 ACTA2 验证，按 annotation_marker 纳入。；Main Text p. 3536, Fig. 1C, Fig. 3B, Fig. 3C |
| DOI_10.1016_j.celrep.2018.11.086 | formal_markers #21 | CD200 | Endothelial Cell | matched | M01204 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 3533, Fig. 2D, Fig. 3C |
| DOI_10.1016_j.celrep.2018.11.086 | context_only #1 | PECAM1 | Endothelial Cell | matched | M01205 | 本文实际使用 CD31 检测/分选 endothelia，效率较低不取消 Marker 身份。；Main Text p. 3533, Fig. 2D |
| DOI_10.1016_j.celrep.2018.11.086 | context_only #2 | ITGA6 | Basal Epithelial Cell / Stroma | context_only |  | 此处为历史 CD49f 门控评价且混合 basal/stroma，不新增未经拆分的单细胞关系。；Main Text p. 3531 |
| DOI_10.1038_s41586-020-2496-1 | formal_markers #1 | Clec4f | Kupffer Cell | add | M02504 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 592, Extended Data Fig. 6g-j |
| DOI_10.1038_s41586-020-2496-1 | formal_markers #2 | Il1b | Kupffer Cell | context_only |  | 该候选用于年龄相关表达、功能或组成变化分析，未证明其在本文被用作所列细胞/年龄亚群的识别标记；共染或 DEG 本身不充分。；Main Text p. 592, Extended Data Fig. 6h-j |
| DOI_10.1038_s41586-020-2496-1 | formal_markers #3 | Alb | Hepatocyte | context_only |  | 该候选用于年龄相关表达、功能或组成变化分析，未证明其在本文被用作所列细胞/年龄亚群的识别标记；共染或 DEG 本身不充分。；Main Text p. 592, Extended Data Fig. 6a-e |
| DOI_10.1038_s41586-020-2496-1 | formal_markers #4 | Pecam1 | Liver Sinusoidal Endothelial Cell | add | M02505 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 592, Extended Data Fig. 6l-o |
| DOI_10.1038_s41586-020-2496-1 | formal_markers #5 | Mrc1 | Liver Sinusoidal Endothelial Cell | context_only |  | 该候选用于年龄相关表达、功能或组成变化分析，未证明其在本文被用作所列细胞/年龄亚群的识别标记；共染或 DEG 本身不充分。；Main Text p. 592, Extended Data Fig. 6k-o |
| DOI_10.1038_s41586-020-2496-1 | formal_markers #6 | Fth1 | Aged Microglia | context_only |  | 该候选用于年龄相关表达、功能或组成变化分析，未证明其在本文被用作所列细胞/年龄亚群的识别标记；共染或 DEG 本身不充分。；Main Text p. 594, Fig. 4d-e, Extended Data Fig. 11e |
| DOI_10.1038_s41586-020-2496-1 | formal_markers #7 | C1qa | Aged Microglia | context_only |  | 该候选用于年龄相关表达、功能或组成变化分析，未证明其在本文被用作所列细胞/年龄亚群的识别标记；共染或 DEG 本身不充分。；Main Text p. 594, Fig. 4e, Supplementary Table 10 |
| DOI_10.1038_s41586-020-2496-1 | formal_markers #8 | B2m | Aged Microglia | context_only |  | 该候选用于年龄相关表达、功能或组成变化分析，未证明其在本文被用作所列细胞/年龄亚群的识别标记；共染或 DEG 本身不充分。；Main Text p. 594, Fig. 4d-e |
| DOI_10.1038_s41586-020-2496-1 | formal_markers #9 | Cxcl16 | Kidney macrophage cluster 10 | add | M02506 | 正文依据列出的 M2 signature 建立 cluster 10 的状态注释；保留具体 cluster，不泛化到所有年轻巨噬细胞。；Main Text p. 594, Fig. 4f, Extended Data Fig. 11f |
| DOI_10.1038_s41586-020-2496-1 | formal_markers #10 | Hexb | Kidney macrophage cluster 10 | add | M02507 | 正文依据列出的 M2 signature 建立 cluster 10 的状态注释；保留具体 cluster，不泛化到所有年轻巨噬细胞。；Main Text p. 594, Fig. 4f, Extended Data Fig. 11f |
| DOI_10.1038_s41586-020-2496-1 | formal_markers #11 | Hp | Kidney macrophage cluster 13 | add | M02508 | 正文依据所列 M1 signature 注释 cluster 13；保留具体 cluster，不泛化到所有衰老巨噬细胞。；Main Text p. 594, Fig. 4f, Extended Data Fig. 11f |
| DOI_10.1038_s41586-020-2496-1 | formal_markers #12 | Itgal | Kidney macrophage cluster 13 | add | M02509 | 正文依据所列 M1 signature 注释 cluster 13；保留具体 cluster，不泛化到所有衰老巨噬细胞。；Main Text p. 594, Fig. 4f, Extended Data Fig. 11f |
| DOI_10.1038_s41586-020-2496-1 | formal_markers #13 | Umod | Loop of Henle Thick Ascending Limb Epithelial Cell | context_only |  | 该候选用于年龄相关表达、功能或组成变化分析，未证明其在本文被用作所列细胞/年龄亚群的识别标记；共染或 DEG 本身不充分。；Main Text p. 592, Fig. 2g-h |
| DOI_10.1038_s41586-020-2496-1 | formal_markers #14 | Col1a1 | Bladder Mesenchymal Stromal Cell | context_only |  | 该候选用于年龄相关表达、功能或组成变化分析，未证明其在本文被用作所列细胞/年龄亚群的识别标记；共染或 DEG 本身不充分。；Main Text p. 592, Fig. 2e-f |
| DOI_10.1038_s41586-020-2496-1 | formal_markers #15 | Dcn | Bladder Mesenchymal Stromal Cell | context_only |  | 该候选用于年龄相关表达、功能或组成变化分析，未证明其在本文被用作所列细胞/年龄亚群的识别标记；共染或 DEG 本身不充分。；Main Text p. 592, Fig. 2f |
| DOI_10.1038_s41586-020-2496-1 | formal_markers #16 | Krt15 | Bladder Urothelial Epithelial Cell | context_only |  | 该候选用于年龄相关表达、功能或组成变化分析，未证明其在本文被用作所列细胞/年龄亚群的识别标记；共染或 DEG 本身不充分。；Main Text p. 592, Fig. 2f |
| DOI_10.1038_s41586-020-2496-1 | formal_markers #17 | Cd79a | B/plasma cells | add | M02510 | 正文明确 B/plasma cell markers；保留联合群，不从联合描述擅自拆分单一细胞特异性。；Main Text p. 592, Fig. 2j |
| DOI_10.1038_s41586-020-2496-1 | formal_markers #18 | Igj | B/plasma cells | add | M02511 | 保留论文原符号 Igj；本轮未查证 Jchain 别名映射。联合群 B/plasma cells。；Main Text p. 592, Fig. 2j |
| DOI_10.1038_s41586-020-2496-1 | formal_markers #19 | Cd3d | T Lymphocyte | context_only |  | 该候选用于年龄相关表达、功能或组成变化分析，未证明其在本文被用作所列细胞/年龄亚群的识别标记；共染或 DEG 本身不充分。；Main Text p. 592, Fig. 2j, Extended Data Fig. 5c |
| DOI_10.1038_s41586-020-2496-1 | context_only #1 | Ptprc | Pan-Immune Leukocyte | unresolved |  | Gemini 仅称跨器官 FACS 使用 CD45；未给具体面板和位置，不能把未查看的补充表当证据。；Methods p. 595, Extended Data Fig. 1 |
| DOI_10.1038_s41586-021-03710-0 | formal_markers #1 | SST | SST inhibitory interneuron | add | M02512 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Figure 1b, Methods p. 11 |
| DOI_10.1038_s41586-021-03710-0 | formal_markers #2 | PVALB | PV inhibitory interneuron | matched | M00101 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Figure 1b, Methods p. 11 |
| DOI_10.1038_s41586-021-03710-0 | formal_markers #3 | VIP | VIP inhibitory interneuron | add | M02513 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Figure 1b, Methods p. 11 |
| DOI_10.1038_s41586-021-03710-0 | formal_markers #4 | SV2C | SV2C inhibitory interneuron | add | M02514 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Figure 1b, Methods p. 11 |
| DOI_10.1038_s41586-021-03710-0 | formal_markers #5 | NRGN | NRGN neuron | matched | M00113 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Figure 1b |
| DOI_10.1038_s41586-021-03710-0 | formal_markers #6 | GFAP | astrocyte | matched | M00099 | 正文 p.569 明确关联 COVID-19 astrocyte cluster；保留疾病亚群，不泛化全部 astrocyte。；Figure 1c, Extended Data Fig. 3a |
| DOI_10.1038_s41586-021-03710-0 | formal_markers #7 | CHI3L1 | astrocyte | matched | M00098 | 正文 p.569 明确关联 COVID-19 astrocyte cluster；保留疾病亚群，不泛化全部 astrocyte。；Figure 1c |
| DOI_10.1038_s41586-021-03710-0 | formal_markers #8 | CD68 | activated microglia | add | M02515 | Fig.3g 明确 CD68 activation-marker IHC；保留激活状态及组织条件。；Main Text p. 4, Figure 3g, Extended Data Fig. 11 |
| DOI_10.1038_s41586-021-03710-0 | formal_markers #9 | CX3CR1 | microglia | matched | M00109 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Figure 3d |
| DOI_10.1038_s41586-021-03710-0 | formal_markers #10 | P2RY12 | microglia | matched | M00112 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Figure 3d |
| DOI_10.1038_s41586-021-03710-0 | formal_markers #11 | C1QC | COVID-19 associated microglia | matched | M00104 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Figure 3d, h |
| DOI_10.1038_s41586-021-03710-0 | formal_markers #12 | IFITM3 | Choroid plexus epithelial cells | context_only |  | Fig.2 的 IFITM3 qPCR 用于验证疾病 DEG，不是脉络丛上皮身份 Marker；与原表 COVID-associated astrocyte 记录是不同关系。；Main Text p. 3, Figure 1f, Figure 2a,b |
| DOI_10.1038_s41586-021-03710-0 | formal_markers #13 | MRC1 | Microglia | matched | M00103 | 正文及 Methods 实际用 MRC1−CD247− 门控排除 macrophage/T cells；方向针对该门控阈值。；Methods p. 11, Figure 3d caption |
| DOI_10.1038_s41586-021-03710-0 | formal_markers #14 | CD247 | Microglia | matched | M00102 | 正文及 Methods 实际用 MRC1−CD247− 门控排除 macrophage/T cells；方向针对该门控阈值。；Methods p. 11 |
| DOI_10.1038_s41586-021-03710-0 | context_only #1 | STAT3 | Choroid plexus epithelial cells | context_only |  | 属于下游炎症通路信号转导分子与差异表达基因，非本底细胞定义标记；Figure 2a, b |
| DOI_10.1038_s41586-021-03710-0 | excluded #1 | SARS-CoV-2 Spike | Endothelial | exclude |  | 被试验证实为抗体非特异性交叉反应假阳性；Main Text p. 4, Extended Data Fig. 9 |
| DOI_10.1038_s41586-021-03929-x | formal_markers #1 | CD34 | Haematopoietic Stem Cell / Multipotent Progenitor | matched | M01365 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text pp. 327-330, Fig. 1b, Fig. 3b, Extended Data Fig. 1d-e, Extended Data Fig. 9f-g |
| DOI_10.1038_s41586-021-03929-x | formal_markers #2 | KIT | Haematopoietic Stem Cell / Multipotent Progenitor | matched | M01366 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 330, Fig. 3b, Extended Data Fig. 9b, f, g |
| DOI_10.1038_s41586-021-03929-x | formal_markers #3 | SPINK2 | HSC/MPP and progenitors | add | M02516 | 已查看 Fig.1b：SPINK2 对应 HSC/MPP & pro.，不缩成仅 HSC。；Main Text p. 328, Fig. 1b |
| DOI_10.1038_s41586-021-03929-x | formal_markers #4 | GYPA | Erythroid Cell | add | M02517 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 328, Methods p. 331, Fig. 1b, Extended Data Fig. 6c |
| DOI_10.1038_s41586-021-03929-x | formal_markers #5 | ITGA2B | Megakaryocyte | matched | M01381 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 328, Methods p. 331, Fig. 1b, Extended Data Fig. 6c |
| DOI_10.1038_s41586-021-03929-x | formal_markers #6 | VPREB1 | B lineage | add | M02518 | Fig.1b 实际标签为 B lineage；不擅自缩窄到 progenitor。；Main Text p. 328, Fig. 1b, Fig. 2b, Extended Data Fig. 4a |
| DOI_10.1038_s41586-021-03929-x | formal_markers #7 | FUT4 | Neutrophil | unresolved |  | 原实验测量 CD15 糖抗原，不能未经唯一映射验证直接当作 FUT4 基因表达。保留抗体实体待核。；Main Text p. 328, Methods p. 331, Fig. 1f, Extended Data Fig. 1e-f, Extended Data Fig. 6c |
| DOI_10.1038_s41586-021-03929-x | formal_markers #8 | GATA2 | Eosinophil/basophil/mast cells | add | M02519 | 已查看 Fig.1b GATA2 对应 Eo/baso/mast cell 联合群，不是明确 progenitor 群。；Main Text p. 328, Fig. 1b, Fig. 1f |
| DOI_10.1038_s41586-021-03929-x | formal_markers #9 | CLEC4C | Plasmacytoid Dendritic Cell | unresolved |  | 所引 Fig.1b 实际 DC 基因为 CLEC10A/CD1C/HLA-DPA1/IL3RA，未见 CLEC4C；pDC 专属对应需进一步定位。；Main Text p. 328, Fig. 1b, Fig. 2a |
| DOI_10.1038_s41586-021-03929-x | formal_markers #10 | CD14 | Monocyte | matched | M01382 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 328, Methods p. 331, Fig. 1b, Fig. 2a, Extended Data Fig. 6c |
| DOI_10.1038_s41586-021-03929-x | formal_markers #11 | CD34 | Tip Endothelial Cell | matched | M01390 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 330, Fig. 3a, Fig. 3b |
| DOI_10.1038_s41586-021-03929-x | formal_markers #12 | KDR | Sinusoidal Endothelial Cell | matched | M01398 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 330, Fig. 3a, Fig. 3b |
| DOI_10.1038_s41586-021-03929-x | formal_markers #13 | CXCL12 | Bone Marrow Stromal Cell | add | M02520 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 330, Fig. 3b |
| DOI_10.1126_science.abo0510 | formal_markers #1 | MS4A1 | B1 Cell | matched | M01507 | 修正 Gemini 虚构的 CD45+CD19+CD38−CCR10− 完整门控；实际为 CD3−CD20+、排除最高1% CD38、CCR10loCD27+CD43+。；Supplementary Methods: ELISpot; Fig.S28G-H |
| DOI_10.1126_science.abo0510 | formal_markers #2 | CD27 | B1 Cell | matched | M01473 | 修正 Gemini 虚构的 CD45+CD19+CD38−CCR10− 完整门控；实际为 CD3−CD20+、排除最高1% CD38、CCR10loCD27+CD43+。；Supplementary Methods: ELISpot; Fig.S28G-H |
| DOI_10.1126_science.abo0510 | formal_markers #3 | SPN | B1 Cell | matched | M01474 | 修正 Gemini 虚构的 CD45+CD19+CD38−CCR10− 完整门控；实际为 CD3−CD20+、排除最高1% CD38、CCR10loCD27+CD43+。；Supplementary Methods: ELISpot; Fig.S28G-H |
| DOI_10.1126_science.abo0510 | formal_markers #4 | VPREB1 | B Cell Progenitor | add | M02521 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Fig.S21A-C (supplementary PDF pp.43-44) |
| DOI_10.1126_science.abo0510 | formal_markers #5 | RAG1 | B Cell Progenitor | add | M02522 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Fig.S21A-C (supplementary PDF pp.43-44) |
| DOI_10.1126_science.abo0510 | formal_markers #6 | DNTT | B Cell Progenitor | add | M02523 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Fig.S21A-C (supplementary PDF pp.43-44) |
| DOI_10.1126_science.abo0510 | formal_markers #7 | KLF1 | Megakaryocyte-Erythroid Progenitor | add | M02524 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Fig.S22A-C (supplementary PDF pp.44-45) |
| DOI_10.1126_science.abo0510 | formal_markers #8 | TESPA1 | Megakaryocyte-Erythroid Progenitor | add | M02525 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Fig.S22A-C (supplementary PDF pp.44-45) |
| DOI_10.1126_science.abo0510 | formal_markers #9 | MPO | Myeloid Progenitor | add | M02526 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Fig.S23A-C (supplementary PDF pp.45-46) |
| DOI_10.1126_science.abo0510 | formal_markers #10 | AZU1 | Myeloid Progenitor | add | M02527 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Fig.S23A-C (supplementary PDF pp.45-46) |
| DOI_10.1126_science.abo0510 | formal_markers #11 | LYVE1 | LYVE1hi macrophages | matched | M01491 | Methods 明确 LYVE1hi 注释；去除未独立证明的 perivascular 特异限定。；Supplementary Materials Fig. S4H |
| DOI_10.1126_science.abo0510 | formal_markers #12 | F13A1 | LYVE1hi macrophages | matched | M01490 | Methods 明确 LYVE1hi 注释；去除未独立证明的 perivascular 特异限定。；Supplementary Materials Fig. S4H |
| DOI_10.1126_science.abo0510 | formal_markers #13 | SLC40A1 | Iron-Recycling Macrophage | matched | M01485 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Supplementary Materials Fig. S4H |
| DOI_10.1126_science.abo0510 | formal_markers #14 | TIMD4 | Iron-Recycling Macrophage | matched | M01486 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Supplementary Materials Fig. S4H |
| DOI_10.1126_science.abo0510 | formal_markers #15 | TREM2 | TREM2 macrophages | matched | M01509 | Methods 作者群名为 TREM2 macrophages；microglia-associated transcripts 不能将该群直接定为 microglia。；Supplementary Materials Fig. S4H |
| DOI_10.1126_science.abo0510 | formal_markers #16 | P2RY12 | TREM2 macrophages | matched | M01508 | Methods 作者群名为 TREM2 macrophages；microglia-associated transcripts 不能将该群直接定为 microglia。；Supplementary Materials Fig. S4H |
| DOI_10.1126_science.abo0510 | formal_markers #17 | MMP9 | Osteoclast | matched | M01498 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Supplementary Materials Fig. S4H |
| DOI_10.1126_science.abo0510 | formal_markers #18 | SDC1 | Plasma Cell | matched | M01502 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Supplementary Materials Fig. S25B |
| DOI_10.1126_science.abo0510 | context_only #1 | PTPRC | Pan-Leukocyte | matched | M01475 | 实际免疫细胞富集门控证据符合 annotation_marker。；Supplementary Materials Methods pp. 3-8 |
| DOI_10.1126_science.abo0510 | context_only #2 | CDH5 | Vascular Endothelial Cell | add | M02528 | Fig.S21-S23 图注明确 CDH5 for endothelial cells，空间定位用途也符合 Marker 规则。；Fig.S21-S23 captions |
| DOI_10.1126_science.abo0510 | excluded #1 | CD5 | B1 Cell | context_only |  | CD5 未用于本次人 B1 门控，不能据此断言基因表达被否定；记录未采用的历史标记。；Supplementary Materials Methods p. 13, Fig. S25A |
| DOI_10.1164_rccm.202207-1384oc | formal_markers #1 | SCGB3A2 | Terminal Airway-enriched Secretory Cell | matched | M00323 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text pp. 1173-1176, Fig. 1E, Fig. 2C-G, Fig. 3F-G, Fig. 4B-D |
| DOI_10.1164_rccm.202207-1384oc | formal_markers #2 | SFTPB | Terminal Airway-enriched Secretory Cell | matched | M00326 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text pp. 1174-1176, Fig. 1E, Fig. 2C, Fig. 2F, Fig. 2H, Fig. 3F-H, Fig. 4B-D |
| DOI_10.1164_rccm.202207-1384oc | formal_markers #3 | MGP | Terminal Airway-enriched Secretory Cell | context_only |  | MGP 在 Fig.2C 是相对 S/AT2 的高表达 DEG；所引位置未显示作者用其独立识别/验证 TASC。；Main Text p. 1174, Fig. 2C, Fig. 2D |
| DOI_10.1164_rccm.202207-1384oc | formal_markers #4 | RNASE1 | Terminal Airway-enriched Secretory Cell | matched | M00322 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 1174, p. 1178, Fig. 2C, Fig. 4B |
| DOI_10.1164_rccm.202207-1384oc | formal_markers #5 | KRT5 | Distal Airway Basal Cell | add | M02529 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 1176, p. 1178, Fig. 1E, Fig. 3I, Fig. 4J |
| DOI_10.1164_rccm.202207-1384oc | formal_markers #6 | SCGB1A1 | Common Secretory Cell | add | M02530 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 1174, p. 1176, Fig. 1E, Fig. 2F, Fig. 3H |
| DOI_10.1164_rccm.202207-1384oc | formal_markers #7 | SFTPC | Alveolar Type 2 Cell | matched | M00301 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 1174, p. 1176, Fig. 1E, Fig. 2C, Fig. 2J |
| DOI_10.1164_rccm.202207-1384oc | formal_markers #8 | TUBB4A | Ciliated Cell | unresolved |  | Fig.2E 标记 TUBB4 蛋白；现有证据未唯一确定 TUBB4A，不能据此填写具体基因。；Main Text p. 1174, p. 1178, Fig. 1E, Fig. 2E, Fig. 4J |
| DOI_10.1164_rccm.202207-1384oc | formal_markers #9 | SERPINB3 | Intermediate Cell | matched | M00309 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 1174, p. 1178, Fig. 1E, Fig. 4E |
| DOI_10.1164_rccm.202207-1384oc | formal_markers #10 | CDH19 | Glial / Schwann Cell | matched | M00026 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 1174, p. 1176, Fig. 1E, Fig. 2L, Fig. 3A-C |
| DOI_10.1164_rccm.202207-1384oc | formal_markers #11 | MPZ | Glial / Schwann Cell | matched | M00027 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 1174, Fig. 1E |
| DOI_10.1164_rccm.202207-1384oc | formal_markers #12 | CD8A | CD8+ T Cell | add | M02531 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 1176, Fig. 1E, Fig. 3A-B, Fig. 3I-J |
| DOI_10.1164_rccm.202207-1384oc | formal_markers #13 | TPSB2 | Mast Cell | add | M02532 | 已查看原始 Fig.1E，修正 TPSAB1→TPSB2 的图标签误读。；Fig.1E, PDF p.3, immune panel MC column |
| DOI_10.1164_rccm.202207-1384oc | context_only #1 | KRT6A | Intermediate Cell (Squamous Metaplasia-like) | matched | M00308,M00320 | 原表已保留 KRT6A 的明确 IC/ALI 状态证据，不因疾病状态排除。；Main Text p. 1176, p. 1178, Fig. 3D, Fig. 4E, Fig. 4J |
| DOI_10.1164_rccm.202207-1384oc | excluded #1 | Scgb3a2 | Common Secretory Cell (mouse) | context_only |  | 未发现鼠 TASC 不等于 Scgb3a2 在鼠 secretory cells 不表达；原文是物种比较，保留上下文。；Main Text p. 1174, p. 1180, Fig. E2Y |
| DOI_10.7554_elife.71752 | formal_markers #1 | RBFOX3 | Sensory neurons | add | M02533 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 2, Methods p. 15, Figure 1-figure supplement 1 |
| DOI_10.7554_elife.71752 | formal_markers #2 | SNAP25 | Sensory neurons | matched | M00009 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 16, Figure 1A |
| DOI_10.7554_elife.71752 | formal_markers #3 | MBP | Non-neuronal cells | matched | M01903 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 16, Figure 1A |
| DOI_10.7554_elife.71752 | formal_markers #4 | APOE | Non-neuronal cells | matched | M01906 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 16, Figure 1A |
| DOI_10.7554_elife.71752 | formal_markers #5 | TAC1 | peptidergic nociceptors | matched | M01900 | 保留原文 peptidergic pooled group；去除 c- 专属限定，不把共享表达展开到每个 H cluster。；Main Text p. 3, p. 6; Figure 1C; Figure 2D |
| DOI_10.7554_elife.71752 | formal_markers #6 | CALCA | peptidergic nociceptors | matched | M01915 | 保留原文 peptidergic pooled group；去除 c- 专属限定，不把共享表达展开到每个 H cluster。；Main Text p. 3, Figure 1C |
| DOI_10.7554_elife.71752 | formal_markers #7 | TRPV1 | peptidergic nociceptors | add | M02534 | 保留原文 peptidergic pooled group；去除 c- 专属限定，不把共享表达展开到每个 H cluster。；Main Text p. 4, Figure 1C |
| DOI_10.7554_elife.71752 | formal_markers #8 | NTRK1 | peptidergic nociceptors | add | M02535 | 保留原文 peptidergic pooled group；去除 c- 专属限定，不把共享表达展开到每个 H cluster。；Main Text p. 4, Figure 1C |
| DOI_10.7554_elife.71752 | formal_markers #9 | NEFH | H14/H15 | add | M02536 | 正文明确 H14/H15 联合描述；不误写成 H14 单一亚群。；Main Text p. 4, p. 6; Figure 1C, Figure 2D, Figure 4C-D |
| DOI_10.7554_elife.71752 | formal_markers #10 | NTRK3 | H14/H15 | add | M02537 | 正文明确 H14/H15 联合描述；不误写成 H14 单一亚群。；Main Text p. 4, Figure 1-figure supplement 5 |
| DOI_10.7554_elife.71752 | formal_markers #11 | PVALB | Proprioceptors | matched | M01908 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 4, p. 8; Figure 1C, Figure 4B |
| DOI_10.7554_elife.71752 | formal_markers #12 | ETV1 | H15 | add | M02538 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 4, Figure 1-figure supplement 5 |
| DOI_10.7554_elife.71752 | formal_markers #13 | TRPM8 | H8 | add | M02539 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 4, p. 8; Figure 2B, Figure 4A |
| DOI_10.7554_elife.71752 | formal_markers #14 | PIEZO2 | H8 | add | M02540 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 8, Figure 4A |
| DOI_10.7554_elife.71752 | formal_markers #15 | TRPM8 | H9 | add | M02541 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 4, p. 8; Figure 2B, Figure 4A |
| DOI_10.7554_elife.71752 | formal_markers #16 | PIEZO2 | H9 | add | M02542 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 4, p. 8; Figure 2B, Figure 4A |
| DOI_10.7554_elife.71752 | formal_markers #17 | OSMR | Nonpeptidergic nociceptors | matched | M00003,M00004 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 6, p. 10; Figure 2C, 2D; Figure 5A |
| DOI_10.7554_elife.71752 | formal_markers #18 | IL31RA | H10/H11 | add | M02543 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 6, Figure 2C |
| DOI_10.7554_elife.71752 | formal_markers #19 | HRH1 | H10/H11 | add | M02544 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 6, Figure 2C |
| DOI_10.7554_elife.71752 | formal_markers #20 | NPPB | H10/H11 | add | M02545 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 6, Figure 2C |
| DOI_10.7554_elife.71752 | formal_markers #21 | MRGPRX1 | Nonpeptidergic nociceptors / mechanical itch | matched | M01901 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 10, Figure 5B |
| DOI_10.7554_elife.71752 | formal_markers #22 | PIEZO2 | Nonpeptidergic nociceptors / mechanical itch | matched | M01913 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 10, Figure 5C |
| DOI_10.7554_elife.71752 | formal_markers #23 | SST | Nonpeptidergic pruriceptors / chemical itch | matched | M01914 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 10, Figure 5B, Figure 5C |
| DOI_10.7554_elife.71752 | formal_markers #24 | JAK1 | Nonpeptidergic pruriceptors / chemical itch | matched | M00010 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 10, Figure 5B |
| DOI_10.7554_elife.71752 | formal_markers #25 | TRPA1 | H5 | add | M02546 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 4, Figure 2B |
| DOI_10.7554_elife.71752 | formal_markers #26 | NTRK2 | H5 | add | M02547 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 4, Figure 2B |
| DOI_10.7554_elife.71752 | formal_markers #27 | CALCA | H5 | add | M02548 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 4, Figure 2B |
| DOI_10.7554_elife.71752 | formal_markers #28 | NTRK1 | H5 | add | M02549 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 4, Figure 2B |
| DOI_10.7554_elife.71752 | formal_markers #29 | SCN1A | Novel mechanosensors | matched | M01907 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 6, Figure 2B |
| DOI_10.7554_elife.71752 | context_only #1 | TMEM100 | Somatosensory neurons | context_only |  | 属于跨物种机制讨论，非人特异性细胞定义的正式 Marker；Main Text p. 4, Figure 2A |
| DOI_10.7554_elife.71752 | context_only #2 | S1PR3 | Somatosensory neurons | context_only |  | 机制探讨与小鼠对比分析，非正式细胞注释标记；Main Text p. 4, Figure 2A |
| DOI_10.7554_elife.71752 | excluded #1 | MRGPRD | Nonpeptidergic nociceptors | context_only |  | 本文未检出人 MRGPRD 的跨物种比较不等于通用证伪；无正式人类 Marker 关系。；Main Text p. 12 |
| DOI_10.7554_elife.71752 | unresolved #1 | PRPH | Non-neuronal cells | unresolved |  | 基因符号不明确，无法唯一映射到 HGNC 标准符号；Main Text p. 16 |
| PMID_37120427 | formal_markers #1 | Scn10a | Nociceptors | add | M02550 | NaV1.8-Cre 用于 nociceptor 靶向；不能限定为 peptidergic。；Main Text p. 2, Figure 1 |
| PMID_37120427 | formal_markers #2 | Piezo2 | NaV1.8+ nociceptors | add | M02551 | 正文与 Fig.6 验证 nociceptor 子集共表达，未把该门控专属映射为 PEP2；移除 PEP2 过度限定。；Main Text p. 2, Figure 1a-c; Figure 6a,b,e |
| PMID_37120427 | formal_markers #3 | Ntrk1 | NaV1.8+ nociceptors | add | M02552 | 正文与 Fig.6 验证 nociceptor 子集共表达，未把该门控专属映射为 PEP2；移除 PEP2 过度限定。；Main Text p. 5, Figure 6a,b,e |
| PMID_37120427 | formal_markers #4 | Piezo2 | large-diameter neurons | add | M02553 | 保留作者 putative proprioceptor 推测程度及 PIEZO2+/NaV1.8−/NTRK1− 组合。；Main Text p. 2, p. 5; Figure 1a,b; Figure 6g |
| PMID_37120427 | formal_markers #5 | Scn10a | large-diameter neurons | add | M02554 | 保留作者 putative proprioceptor 推测程度及 PIEZO2+/NaV1.8−/NTRK1− 组合。；Main Text p. 5, Figure 6f,g |
| PMID_37120427 | formal_markers #6 | SCN10A | Human Nociceptors | add | M02555 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 5, Figure 6c,d,e,f |
| PMID_37120427 | formal_markers #7 | PIEZO2 | Human Nociceptors | add | M02556 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 5, Figure 6c-f |
| PMID_37120427 | formal_markers #8 | NTRK1 | Human Nociceptors | add | M02557 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 5, Figure 6c-f |
| PMID_37120427 | formal_markers #9 | PIEZO2 | putative proprioceptors | add | M02558 | 正文只称 consistent with proprioceptors，保留 putative 限定。；Main Text p. 5, Figure 6f,h |
| PMID_37120427 | formal_markers #10 | Nefh | Neurofilament / Large diameter neurons / Proprioceptors | unresolved |  | Fig.1a 图注 NF 是 neurofilament 类别缩写，并未唯一指定 Nefh 基因，不能从缩写补写基因。；Figure 1a legend |
| PMID_37120427 | formal_markers #11 | Trpm8 | TRPM8+ cool sensing neurons | add | M02559 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Figure 1a legend |
| PMID_37120427 | formal_markers #12 | Th | TH-containing neurons | add | M02560 | 作者 Fig.1a 明确 TH-containing 类别，但未在该证据指定 cLTMR 身份。；Figure 1a legend |
| PMID_37120427 | context_only #1 | Calca | Peptidergic nociceptors | context_only |  | 刺激诱导性表达变化/机制验证，未用于稳态细胞注释定义；Main Text p. 5, Figure 7e |
| PMID_37664243 | formal_markers #1 | SCN10A | Human Nociceptors | add | M02561 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 5, p. 10; Figure 5B, Figure 6A-E |
| PMID_37664243 | formal_markers #2 | DCN | Human VLMC-like cells / Fibroblasts | add | M02562 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 5, p. 10; Figure 5B, Figure 6B-F |
| PMID_37664243 | formal_markers #3 | GPC3 | Human VLMC-like cells / Fibroblasts | add | M02563 | 已对照已有正文/图注中的细胞注释、命名或验证关系；保留原作者粒度。；Main Text p. 10, Figure 6G |
| PMID_37664243 | formal_markers #4 | RBFOX3 | Human DRG neurons | add | M02564 | Fig.6G NeuN 为 neuronal marker，不专属 nociceptor。；Main Text p. 10, Figure 6G |
| PMID_37664243 | formal_markers #5 | COL1A1 | Human VLMC-like cells / Fibroblasts | context_only |  | 用于 collagen 表达/配体受体机制验证，细胞由 DCN/SCN10A 识别；不把被测功能基因正负自动作为身份 Marker。；Main Text p. 10, Figure 5C, Figure 6B, 6D, 6F |
| PMID_37664243 | formal_markers #6 | COL1A1 | Human Nociceptors | context_only |  | 用于 collagen 表达/配体受体机制验证，细胞由 DCN/SCN10A 识别；不把被测功能基因正负自动作为身份 Marker。；Main Text p. 10, Figure 6A, 6C, 6E |
| PMID_37664243 | formal_markers #7 | CD44 | Human Nociceptors | context_only |  | 用于 collagen 表达/配体受体机制验证，细胞由 DCN/SCN10A 识别；不把被测功能基因正负自动作为身份 Marker。；Main Text p. 10, Figure 5D |
| PMID_37664243 | formal_markers #8 | SDC4 | Human VLMC-like cells / Fibroblasts | context_only |  | 用于 collagen 表达/配体受体机制验证，细胞由 DCN/SCN10A 识别；不把被测功能基因正负自动作为身份 Marker。；Main Text p. 10, Figure 5D |
| PMID_37664243 | formal_markers #9 | Scn10a | Nociceptors | unresolved |  | 正文只称基于 cluster-specific markers 注释；候选引用的 Fig.S3 未在现有主文中提供具体 gene–cell 配对，不能凭常识补入。；Main Text p. 7, Figure 3, Supplementary Figure S3 |
| PMID_37664243 | formal_markers #10 | Dcn | Vascular leptomeningeal-like cells / Fibroblasts | unresolved |  | 正文只称基于 cluster-specific markers 注释；候选引用的 Fig.S3 未在现有主文中提供具体 gene–cell 配对，不能凭常识补入。；Main Text p. 7, Figure 3, Supplementary Figure S3 |
| PMID_37664243 | formal_markers #11 | Col1a1 | Vascular leptomeningeal-like cells / Fibroblasts | context_only |  | 用于 collagen 表达/配体受体机制验证，细胞由 DCN/SCN10A 识别；不把被测功能基因正负自动作为身份 Marker。；Main Text p. 7, Figure 4C |
| PMID_37664243 | formal_markers #12 | Cd44 | Nociceptors | context_only |  | 用于 collagen 表达/配体受体机制验证，细胞由 DCN/SCN10A 识别；不把被测功能基因正负自动作为身份 Marker。；Main Text p. 8, Figure 4D |
| PMID_37664243 | context_only #1 | IGF1 | Human VLMC-like cells / Fibroblasts | context_only |  | 疾病状态下的差异表达基因与通路配体分析，未用于细胞常态定义；Main Text p. 10, Table 1, Figure 7A |
| PMID_37664243 | context_only #2 | SEMA6B | Human VLMC-like cells / Fibroblasts | context_only |  | 差异表达分析与机制讨论，非标准细胞标记；Main Text p. 10, Table 1, Figure 7B |
| PMID_37664243 | excluded #1 | COL1A1 | Human Nociceptors | exclude |  | 被原位验证实验明确否决的阳性表达假说；Main Text p. 10, Figure 6A, 6C |

## 原表处置

|ID|处理|理由|
|---|---|---|
| M00001 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00002 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00003 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00004 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00005 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00006 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00007 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00008 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00009 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00010 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00026 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00027 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00028 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00062 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00063 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00064 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00098 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00099 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00100 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00101 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00102 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00103 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00104 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00105 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00106 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00107 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00108 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00109 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00110 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00111 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00112 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00113 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00114 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00115 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00299 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00300 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00301 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00302 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00303 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00304 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00305 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00306 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00307 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00308 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00309 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00310 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00311 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00312 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00313 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00314 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00315 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00316 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00317 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00318 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00319 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00320 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00321 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00322 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00323 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00324 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00325 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00326 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00327 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00328 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M00329 | deduplicate | 同一关系已有 M00323；保留原始行于审计记录。 |
| M00330 | deduplicate | 同一关系已有 M00326；保留原始行于审计记录。 |
| M01184 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01185 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01186 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01187 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01188 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01189 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01190 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01191 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01192 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01193 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01194 | correct | 原 NKX3.1 蛋白/别名写法保留，标准符号按 Gemini 的 Nkx3-1 统一。 |
| M01195 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01196 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01197 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01198 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01199 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01200 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01201 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01202 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01203 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01204 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01205 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01206 | deduplicate | 同一关系已有 M01205；保留原始行于审计记录。 |
| M01207 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01208 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01209 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01210 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01211 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01212 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01213 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01214 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01215 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01216 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01217 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01218 | deduplicate | 同一关系已有 M00063；保留原始行于审计记录。 |
| M01219 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01220 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01221 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01222 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01223 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01365 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01366 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01367 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01368 | deduplicate | 同一关系已有 M01367；保留原始行于审计记录。 |
| M01369 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01370 | correct | 正文及 Fig.3b 明确 VEGFR2lo，保留低表达。 |
| M01371 | deduplicate | 同一关系已有 M01369；保留原始行于审计记录。 |
| M01372 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01373 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01374 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01375 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01376 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01377 | correct | Methods 明确为 CD45RA 异构体门控，PTPRC 方向只指 CD45RA，不代表全基因/全部蛋白。 |
| M01378 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01379 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01380 | correct | Methods 明确为 CD45RA 异构体门控，PTPRC 方向只指 CD45RA，不代表全基因/全部蛋白。 |
| M01381 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01382 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01383 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01384 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01385 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01386 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01387 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01388 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01389 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01390 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01391 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01392 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01393 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01394 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01395 | unresolved | Fig.3b 图注写 CD34hi，正文写 CD34lo，均指 diaphyseal sinusoids；CD34 极性冲突，保留双方证据待核。 |
| M01396 | deduplicate | 同一关系已有 M01398；保留原始行于审计记录。 |
| M01397 | unresolved | Fig.3b 图注写 CD34hi，正文写 CD34lo，均指 diaphyseal sinusoids；CD34 极性冲突，保留双方证据待核。 |
| M01398 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01471 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01472 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01473 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01474 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01475 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01476 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01477 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01478 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01479 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01480 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01481 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01482 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01483 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01484 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01485 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01486 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01487 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01488 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01489 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01490 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01491 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01492 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01493 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01494 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01495 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01496 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01497 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01498 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01499 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01500 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01501 | correct | Fig.S26 明确 MS4A1lo，不能改写为阴性。 |
| M01502 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01503 | deduplicate | 同一关系已有 M01499；保留原始行于审计记录。 |
| M01504 | deduplicate | 同一关系已有 M01501；保留原始行于审计记录。 |
| M01505 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01506 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01507 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01508 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01509 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01899 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01900 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01901 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01902 | unresolved | 原文 PRP1 无法唯一解析为基因，不采用 Gemini 推测的 PRPH。 |
| M01903 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01904 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01905 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01906 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01907 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01908 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01909 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01910 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01911 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01912 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01913 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01914 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01915 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01916 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
| M01917 | retain | 原记录保留；Gemini 未列出不等于无效，未对未涉及关系重新提取。 |
