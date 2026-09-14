# v3 接收审查

2026-09-06。结论：修复后的指定截图与原28项登记可以用于后续裁决；原始crosswalk不能直接作为“同关系”自动合并依据。接收材料不等于所有Marker通过入库。

## 已核实

- 1176条分类计数与上一轮相同，953条为baseline_existing，62条为pending_adjudication。
- 原28个record_id集合完全一致，无重复；original_unresolved_reason逐字与Codex保存的原裁决reason一致。
- 索引所列图像文件均存在。实际查看iPain第3页为真实Fig.1；肾脏第13页为真实Fig.1；膀胱裁图已经保留完整CDH19+/NRXN+/XKR4+句子。
- stem标题已改回neonatal respiratory disease，pmid_source改为filename。
- 正式总表及按细胞表SHA-256仍与既有基线一致，本次没有写入。

## 仍需区别处理

### 基因相同不等于关系相同

v2的明显异基因序号强连已不再出现，但v3的same_relation_match仍将“同基因”当作“同关系”。实际例子：

| 修补项 | 原关系 | 修补关系 | 应如何理解 |
|---|---|---|---|
| HOPX / stem.2022.11.013_M01 | AT1 | AT2 | 细胞纠错关联，不能标为关系不变 |
| ALDH1A3 / 40173_M00763 | Mature DC | SMG duct cells | 细胞纠错关联 |
| ccr2 / 07315_M01837 | mouse Ccr2 | zebrafish ccr2 | 不同物种，不能同关系匹配 |
| Ager / 40173_M00733 | human AGER | mouse Ager | 不同物种 |
| Krt19 / 40173_M00736 | human KRT19 | mouse Krt19 | 不同物种 |
| PMP2 / PMID35115729_M02588 | mouse Pmp2 | human PMP2 | 不同物种 |

严格区分大小写时还有5个原/新基因字符串差异，均为大小写变化，不能称为5个不同基因错误；其中4条正式记录实际跨物种，另1条上下文ccr2也不具备可靠同关系依据。问题在于映射语义，不应仅靠大小写得出物种结论。

Codex已另存v3-received-crosswalk.json：保留全部原字段与Gemini映射类型，新增codex_mapping_status/codex_mapping_differences，将涉及核心字段差异的链接标为待复核；核心字段相同也注明测量实体和条件未核实。文件中的361个差异项包含别名、粒度差异和缺字段，不是361条错误。原交付保持不变。

### 逐字引文仍须以原页为准

- EVID_01的verbatim_quote是“Fig.1D panel label ... in PNEC row”这样的图像解读，应放visual_observation，不能当原文整句。
- EVID_05图注标题正确，但其(A)后写“Schematic overview of mature human kidney zones...”，截图实际为“A. Anatomy of the human kidney.”，不是逐字复制。
- EVID_02的verbatim_quote并不出现在提交的第3页截图中，引用前须定位真实图注页；不要将概括当引文。
- PRR4短摘录与此前原图注吻合，但只截取到areas，为节选而非完整句。其蛋白识别证据继续有效。

## 当前状态

- 原28项：1项PRR4有可纳入证据；1项Glb1错误实体撤销；另外26项关系尚未解决（包括CALCA/CHGA、NRXN1及其余23项），不能只把23当作总未决数。
- 953条基线重述不计独立新增；62条候选仍待按关系、物种、实体和条件裁决。
- 本次完成材料接收和风险标记，没有完成62条入库裁决，也未修改总表。
- 不需要再让Gemini重写整个汇总。后续如分配任务，应限于具体补充材料获取和指定图/表证据定位；同关系判断和最终入库由Codex处理。
