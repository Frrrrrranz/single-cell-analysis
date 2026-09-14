# NotebookLM 与 Gemini 网页版核对

日期：2026-09-05。论文：10.1038/s41586-020-2922-4。

## 结论与评价边界

本次 NotebookLM 输出没有显示出比网页版更高的准确性，覆盖范围明显更小。仅比较本次两份输出，不推广为平台的一般性能结论；输入提示词、上传附件、模型版本等是否完全相同尚不清楚。

逐条复核 NotebookLM 的全部22条正式记录，20条细胞—基因—human—positive关系可由正文、图或图注支持，2条所引证据不支持。关系支持率为20/22=90.9%。此数值不代表22条记录的页码、图号、引文、特异性描述和生物学解释均正确，也不是全文提取召回率。网页版112条尚未按相同严格口径全部裁决，因此不提供其整体准确率。

不把我们已有正式表当作金标准：该表也存在已发现的物种错误等问题。

| 指标 | NotebookLM | Gemini网页版 |
|---|---:|---:|
| 正式记录 | 22 | 112 |
| 有正式记录的作者亚群标签 | 22/58（37.9%） | 54/58（93.1%） |
| 全部正式记录的关系支持率 | 20/22（90.9%） | 未完整裁决 |
| 双方共同输出的20条关系 | 19条有支持，1条不支持 | 同样19条有支持，1条不支持 |
| 候选记录 | 1 | 4 |

亚群标签覆盖只统计输出，不代表所有关系正确；网页版额外4个组织区室不计入58个亚群。共同条目按原文基因符号统一大小写、对应作者细胞群、物种和极性匹配，未要求描述性subtype文字相同。共同条目不是独立随机抽样，不能外推为两者的整体准确率。

## NotebookLM 全部正式条目裁决

“支持”仅评价核心细胞—基因关系；更正后的定位见第三列。

| 序号 | NotebookLM关系 | 原文支持或问题 | 裁决 |
|---:|---|---|---|
| 1 | basal—KRT5 | Extended Data Fig.3c/f，PDF17–18页 | 支持 |
| 2 | proximal basal—SERPINB3 | Extended Data Fig.3f，PDF17–18页 | 支持 |
| 3 | ciliated—C20orf85 | Extended Data Fig.3g/h，PDF17–18页；保留原始符号，不在本次核查现行别名 | 支持 |
| 4 | proximal ciliated—DHRS9 | Extended Data Fig.3h，PDF17–18页 | 支持 |
| 5 | AT1—AGER | Extended Data Fig.5c，PDF21页 | 支持 |
| 6 | AT2—WIF1 | Fig.1d，PDF2页；引用中的Fig.1i不存在 | 支持，图号部分错误 |
| 7 | AT2-signalling—WNT5A | Fig.1c及Extended Data Fig.3i；引用中的Fig.1i不存在；source_context中CTNNBIP漏末尾1 | 支持，定位/引文需修 |
| 8 | alveolar fibroblast—GPC3 | Fig.1f及Extended Data Fig.4a | 支持 |
| 9 | adventitial fibroblast—SERPINF1 | Fig.1f及Extended Data Fig.4c | 支持 |
| 10 | myofibroblast—ASPN | Extended Data Fig.4f/g，PDF19–20页；notes对活化来源的解释不纳入本项裁决 | 支持 |
| 11 | lipofibroblast—APOE | Extended Data Fig.4i，PDF19–20页 | 支持 |
| 12 | pericyte—COX4I2 | Extended Data Fig.4h/j，PDF19–20页 | 支持 |
| 13 | airway smooth muscle—DES | Extended Data Fig.5a没有DES，ASM对应展示KCNA5；该条声称的引文不受所引图支持 | 不支持，待另证 |
| 14 | vascular smooth muscle—ADIRF | Extended Data Fig.5a没有ADIRF，VSM对应展示C2orf40 | 不支持，待另证 |
| 15 | bronchial vessel 1—ACKR1 | Extended Data Fig.3k正确；额外引用的Fig.4l为树突状细胞 | 支持，定位部分错误 |
| 16 | bronchial vessel 2—PLVAP | Extended Data Fig.3j的Bro1/2标记面板可支持；不是Bro2独有标记，正文描述对象也是bronchial vessel cells | 支持，需说明Bro1/2共享 |
| 17 | vein—ACKR1 | 正确为Extended Data Fig.3l，而非4l | 支持，图号错误 |
| 18 | artery—GJA5 | 正确为Extended Data Fig.3m，而非4m | 支持，图号错误 |
| 19 | lymphatic—CCL21 | 正确为Extended Data Fig.3n，而非4n | 支持，图号错误 |
| 20 | IGSF21+ DC—IGSF21 | Fig.2b及Extended Data Fig.4l | 支持 |
| 21 | EREG+ DC—EREG | Fig.2b及Extended Data Fig.4m | 支持 |
| 22 | TREM2+ DC—TREM2 | Fig.2b及Extended Data Fig.4n | 支持 |

第13/14项“不支持”表示本文所引证据不足，不能据此判断这些基因在其他研究中是否具有相应生物学作用。PDF可检索文字中未找到独立DES/ADIRF词项，并视觉检查了所引图。

NotebookLM独有的正式关系是VSM—ADIRF和Bro2—PLVAP；前者不支持，后者有图示支持。PLVAP在网页版被列为Bro1/Bro2的上下文候选，因此不是网页版完全没识别到它。其余20条与网页版正式关系重合，其中共同的不支持项是ASM—DES。网页版另外存在已核实的AT2-s—NNMT配对错误，NotebookLM未输出NNMT，不能据此视为主动纠错。

## 覆盖与证据质量问题

1. NotebookLM称有58个annotation labels，但author_cell_labels实际只有54个字符串。它漏了Club、NKT、MP-p、Mono OLR1等作者标签，合并mDC1/mDC2，并引入并非Fig.2a原始标签的“alveolar macrophages/interstitial macrophages”；这不是准确的58群清单。
2. 正式记录仅覆盖22个亚群，而且每群仅1条。连SFTPC都没有正式条目，也缺少基因配对中已经写出的GPR34、CHI3L1等。神经内分泌NE—CHGA/ASCL1也未提取，网页版有这两条。
3. 把MYH11降级为候选的理由是“不专属于该细胞”。项目口径并不要求marker绝对独占；Fig.1e明确展示stromal markers，应依图示关系判断，不能以“与其他细胞共享”为排除门槛。
4. 将Cap-i1概括为没有明确单基因映射忽略了Extended Data Fig.5a的SPRY1。Cap-i2是否可补提需另外核查，不能把两群一概处理。
5. reported_cell_labels_without_formal_markers只列4项，还包含不规范的“T cells proliferating”，未如实反映大量缺失；completion_notes仍宣称全面提取。
6. 页码大量把扩展图填在PDF3/8/10页。实际Extended Data Fig.3为17–18页，Fig.4为19–20页，Fig.5为21页。关系支持不等于定位准确。

## 对前一份报告的更正

前次把我方ASM/FibM—COX4I2阳性记录直接归为配对/极性错误，判断过强。本次完整复读Extended Data Fig.4f/g图注发现，作者文字确实称COX4I2/ACTG2为fibromyocyte和airway smooth muscle markers；同时f图示ASPN+ COX4I2−的MyoF，h/j突出Peri阳性。因此这里存在图文解释和所指细胞范围需要进一步澄清的问题，应标记待复核，不能仅根据f/h/j断言我方两条错误。已同步更正前一份报告。

## 本次选用判断

针对“尽量提全后人工复核”的当前任务，这一份网页版输出更有用；NotebookLM这一份近似少量代表性marker摘要，覆盖损失明显，仍需校对引用且有不支持条目。不能用90.9%这一关系支持率证明NotebookLM整体优于网页版，也不能据本篇断言平台孰优。

输入：本次pasted-text.txt与上次gemini-code-1788582091593.json。证据：本地论文PDF及其已有review_md全文；复用并检查原图渲染，追加复读Extended Data Fig.3/4完整图注。未调用外部资料，也未修改正式工作簿。
