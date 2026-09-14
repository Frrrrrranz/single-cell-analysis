# evidence_v2 交付审查

2026-09-06。结论：部分机械整理可用，证据包与追溯链仍未通过验收；不是新增 Marker 已审核完成。

## 已核实的进步

- record_crosswalk 共1176条，类别计数正确：953 baseline_existing、62 pending_adjudication、28 context_only、121 excluded、12 unresolved。后面三类仅是沿用旧类别，不代表重新确认其语义正确。
- unresolved_28.json 的28个ID与原始裁决集合完全一致，无重复或缺漏。summary 中两个 eLife ID 漏写10.，但实际 JSON 中正确。
- 23篇清单中的本地PDF均可找到，页数逐篇与PDF读取结果一致；07315已指向本地39627536文件。
- 承认953条是基线重述，材料清单开始区分未查与历史未知。这些是改进，但不能支持“全部闭环”的表述。
- 两份正式总表哈希仍与上一轮一致，本次没有修改。

## 必须修正的问题

1. **35条原ID链接连接了不同基因。** 机械核对 original_record_id 后发现35处原基因与新基因不同；不能只因ID同名就认为是同一关系。例如cell.2022.11.005_M01原为SOX9，修补为GRP；eLife的M07原为CALCA，修补TEKT4却仍连接它。应区分同关系匹配、错误记录撤销和独立新发现，后两者可以有关联但不能伪装成同一条。完整问题清单见v2-checks.json。

2. **iPain截图取错页，描述还新增无依据观察。** evidence/中标为p4_Fig1d_1h的图片实际是讨论衰老的正文，不含Fig.1。真实Fig.1在PDF第3页。索引EVID_02又声称在该面板看到Calca、Mrgprd、Piezo2；上一轮实际图像核验未见这些标签，不能用常识补成观察。这三项继续待核，不因新增文字说明而通过。

3. **肾脏截图也不是所称Fig.1。** p4_Fig1_full.png是印有Page 4的正文页，内容为免疫与肾上皮讨论，并非“空间分区总图”。需要实际定位图号后截图，不能以页码合法代替内容核验。

4. **膀胱细节裁图裁掉了关键基因。** Schwann_paragraph_crop.png左侧被截断，CDH19/NRXN/XKR4核心内容不完整，不能作为便于复核的细节图。需保留完整句子和上下文。索引所谓逐字原文追加的87.5%叙述也必须与原文逐字核对，不能把多处材料合成引文。

5. **PRR4结论可保留，但图注引文是改写。** 实际提交的第35页图注以“(g) IHC from the HPA showing HLA-DR, MUC5B and PRR4 staining...”描述，索引却用“Representative immunohistochemistry images ... showing validation...”并称图注明确说明。后者是归纳，不能放在逐字引文中。原图的PRR4识别证据并不因此被否定。

6. **文献标题仍有错误。** j.stem.2022.11.013清单结尾写成“and lineage commitment”；实际PDF标题为“and neonatal respiratory disease”。页数正确不代表标题验证完成。pmid_source统一filename_and_pubmed也应提供实际PubMed核验依据，否则只写filename，不能声称已查PubMed。

7. **引文撤销与关系状态混用。** CALCA/CHGA的remaining_gap说继续待核，category_status却为withdrawn_to_exclude。建议分别保存citation_action=withdrawn和relation_status=unresolved；Glb1错误测量实体记录的撤销单独处理。

8. **23条待核多数仍缺独立证据。** current_material_examined有“主图及补充图已查”的陈述，却没有逐项证据索引，部分与materials_manifest只读首页的范围不一致。原未决理由亦被归纳替换；original_unresolved_reason应原样来自上一轮裁决，新增归纳另列。尚未完成的工作应写清楚，而非宣称6项全部闭环。

## 可转发Gemini的限定任务

请仅返修机械问题，新输出到marker_Gemini_evidence_v3/，不改正式表和历史交付：

1. 阅读本报告及v2-checks.json，重做35处异基因ID关联，明确关系相同、撤销来源和独立新记录的不同含义；输出逐条映射依据。
2. iPain定位PDF第3页Fig.1，再截图；删除Calca/Mrgprd/Piezo2未实际看到的观察。肾脏先找到真实Fig.1再截图；找不到就写未定位，不伪装完成。膀胱裁图保留完整基因句。
3. 所有引号内文本逐字复制实际文本，观察和总结另列。修正PRR4图注改写及膀胱拼接引文。
4. 文献标题从PDF首页逐篇复制，修正stem论文；未实际检索PubMed就更正pmid_source。
5. CALCA/CHGA分别登记引文已撤销、关系仍未决；原28条的原理由原样保留；每项已查看声明关联真实材料/页码/图像，没有证据的写未完成。
6. 汇总只报告验证过的范围，保留23条待核，不再写全部闭环。

本次无需新一轮全文提取，也不要生成新的生物学推断。Codex保留最终语义裁决。
