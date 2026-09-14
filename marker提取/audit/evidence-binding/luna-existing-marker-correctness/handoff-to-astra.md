# 交给 Astra 的独立验收说明

运行编号：`20260907-luna-existing-marker-correctness`  
执行者：GPT-5.6 Luna  
日期：2026-09-07

## 范围与分母

- 启动 active：`2488` 条、`43` 篇论文。
- 旁路原 ID：`14` 个，分别为 13 个上一轮合并源和 `M01510`。
- 本轮已登记实际核验：`104` 个审核单位；剩余 `2398` 个保持 `pending`。
- 本次没有把旧 62 候选、28 未决、28 context_only 或 121 excluded 当作全量完成条件。

## 首批裁决与动作

- `verified_correct/update`：`M00044`、`M00398`、`M00403`、`M00071`、`M00415`、`M02592`。
- `verified_correct/restore`：`M00417`、`M01510`。
- `verified_correct/update`（仅证据/决策链）：`M02590`、`M02591`。
- `verified_keep/no_change`：其余 12 个合并源及其 12 个当前目标，共 24 个审核单位。关系保留，源 ID 与完整原值写入本轮归档。
- 当前 active 从 `2488` 增至 `2490`，只恢复 `M00417` 和 `M01510`，未分配新 ID。

## 第二批 Cell task 9 裁决

- 本批共 `27` 个审核单位：`23` 个 `verified_keep/no_change`，`4` 个 `verified_correct/update`。
- 更新 `M00547`、`M00551`、`M00566`、`M00593`：原文分别使用 SCGB3A2LO/-、SCGB3A1-/LO、SOX9LO/-、PLN-/low，暂存主表已将对应极性修正为 `low`。
- 证据组覆盖 Cell 论文 Fig. S3、S6、S7、S8 及正文对应定义；无关系删除或新 ID 分配。

## 第三批 Cell task 9 裁决

- 本批共 `43` 个审核单位，全部为 `verified_keep/no_change`。
- 覆盖神经内分泌、气道祖细胞、AT1/AT2、上皮、间充质、分泌细胞及 tip/stalk 正向关系；均有正文或图注直接证据。
- 本批没有新增字段修正、关系删除或新 ID 分配，仅完成证据链接、逐条前后值登记和归档。

## Astra 补充规范返修

- 已按补充方案先返修第三批，不将原先 `43条统一verified_keep` 继续沿用。
- 重新核对并将 `M00520`、`M00533`、`M00537`、`M00564`、`M00565` 的目标基因限定修正为 `low`；旧裁决标为 superseded，并以 `REOPEN`/`UPDATE ... R1` 留存替代关系。
- `M00547`、`M00551`、`M00566`、`M00593` 仍使用 `low` 兼容枚举，但备注和按细胞汇总明确保留 `LO/-`、`-/LO` 或 `-/low` 的阴性可能性。
- 第二、三批已补齐目标基因级证据片段；证据组现在同时提供 `support_map`，不再用省略号拼接文本冒充连续逐字引文。
- 返修阶段变更集共 `106` 个唯一 change ID；其中包含返修替代链，不等同于 106 条实际字段修改。正式表哈希仍与启动基线一致。

## 第四批定向 qualifier 修正

- 新增 5 条目标基因级修正：`M00493`（UCP2LO）、`M00495`（FGFR4LO）、`M00498`（MUC16LO）、`M00508`（THBDLO）、`M00534`（SCGB1A1LO）。
- 当前审核完成数为 `109`，待审 `2393`；变更集为 `116` 个唯一 change ID，归档页为 `111` 条。5 条修正均已同步到暂存主表和按细胞汇总。
- 机器校验已覆盖正式表基线哈希、证据引用可解析性、change ID 唯一性；仍需 Astra 对语义和最终暂存表独立验收。

## 关键风险

- `M00044`、`M00398`、`M00403`：原文是 low，不能继续按 negative 表示。
- `M00415/M00417`：正文 CA4LO 与 S7B HCR CA4+ 是不同测量来源，已拆开。
- `M00071`：保留 CCI 损伤 DRG 的衰老 nociceptor 子集与 Fig.3i，不泛化为 neurons。
- `M01510`：SST 在 Fig.2a/f/g、Fig.3e 实际用于命名/分析，不能仅按引言背景降级。
- `M02592`：清除历史 `claimed in repair` 文案。

## 第五批 task 13 定向 qualifier 修正

- 对 `10.1126/sciimmunol.adf9988` 的 `M00633`、`M00637`、`M00680`、`M02359`、`M02364`、`M02369`、`M02374`、`M02375`、`M02376` 完成逐条目标级证据绑定。
- 目标限定分别保留为 SOX9-、MKI67-、EBF1-、MKI67-、MKI67-、IGHDlo、VPREB3lo、CD5- 和 PRDM1 缺失；主表兼容极性为 negative 7 条、low 2 条。
- `M00663`（IL3RA）与 `M00683`（SIGLEC1）没有足够的目标基因级连续片段，仍为 pending；没有用同一文献中的其他基因描述替代目标证据。
- 当前完成数 `118`，pending `2384`；change-set `125` 个唯一 change ID，`audit_archive_20260907` 为 `120` 条归档行。
- 正式表哈希仍不变；最新暂存主表 SHA-256 为 `887b5a4cf487e4908b692f6e6ba2be7f9e96dff066d12512d9ecdacec9e82731`，按细胞汇总为 `63c9e843d02ff132b0c3a5faacefce351a449d039824e41150ad5d33671e4e99`。

## 第六批 task 13 正向定义核验

- 新增 21 条 `verified_keep/no_change`：气道 progenitor 的 SOX2；B 细胞发育阶段的 CD5、IGHM、IGLL1、NEIL1、EBF1、IL7R、SPINK2、VPREB1、DNTT、RAG1、MS4A1、BEST3、SPIB、IGKC、IGLC2、IGLC3；以及 CD5+ B-1-like 细胞的 CCL22、CCR10、CD27、SPN。
- 每条记录均有目标基因级 `evidence_excerpt`、`evidence_locator`，共享证据组使用 `support_map`；没有使用省略号拼接为单一逐字引文。
- 当前完成 `139` 条，pending `2363`；change-set 共 `146` 个唯一 change ID，归档页为 `141` 条。正式表哈希仍与启动基线一致。
- 最新暂存主表 SHA-256：`266717e80cc894582b55dfef2676478dc973d462a13030b1c1b1ce118f801e59`；按细胞汇总：`7db2eecb605ad5402913617070e3db530440b583011033db1e7dac8306462cbd`。

## 第七批 task 13 免疫/造血/上皮正向核验

- 新增 17 条 `verified_keep/no_change`，覆盖 distal epithelial tip、ILCP、HSC、巨噬细胞/单核细胞及肺上皮正文中的 SOX2、SOX9、SMIM24、SPINK2、HPN、SCN1B、CD14、CD36、MRC1、CD34、APOE、CXCL2、S100A12、CD68 等目标基因。
- 每条均绑定目标基因级连续片段；只做证据登记和 no_change 归档，没有把别名 CD45/CD31/CD206 直接替代为 PTPRC/PECAM1/MRC1。
- 当前完成 `156` 条，pending `2346`；change-set 共 `163` 个唯一 change ID，归档页 `158` 条。
- 最新暂存主表 SHA-256：`6c919a2a9f2a73b1eb1755ae2ed0508fefcfde6c461ec7c5f808400b7e98fc97`；按细胞汇总：`16b442f58e1314a9cb1f3617b5a7fec1b47868a5d28c7d91bb3e1a6d404725d1`。

## 第八批 task 13 B 细胞阶段 marker 核验

- 新增 21 条 `verified_keep/no_change`，覆盖 VPREB1、RAG1、IGLL1、IL7R、MS4A1、MKI67、BEST3、SPIB、VPREB3、IGHD、IGHM。
- 证据分别绑定 large/small pre-B、immature/mature B 的正文定义、RNAscope 阶段片段和 Figure 3E 图注；没有把摘要式上下文当作目标级证据。
- 当前完成 `177` 条，pending `2325`；change-set 共 `184` 个唯一 change ID，归档页 `179` 条。
- 最新暂存主表 SHA-256：`f34cda90e702642d56bc975730cb9c3c055f2d256ecb413c7332b8990d90d73c`；按细胞汇总：`f55ef039aa095d100994e915196baa3cf2cd6b3c2d6482f390f5b3ce20e968bc`。

## 第九批 source-context 候选定位（已按 Astra 回退）

- 从 task 5、18、20、23、39、42、44 的 pending 中定位候选，并将固定清单 330 条写入 `source_context_batch_selection_20260908.json`。
- Astra 复核确认 95% token 重合只能定位候选，不能作为目标基因—细胞关系、表达方向、限定条件和物种/阶段语境的语义验收；且自动脚本保存的引文窗口可能不是评分最高窗口。
- 固定清单 330 条已全部回退为 `pending`；候选 evidence、匹配分数、source hash、旧变更以及 superseded/reopen 版本链均保留。
- selection 文件剩余 eligible 为 33 条。旧筛选日志打印过 366 个候选，但本次执行只以 330 + 33 = 363 为准，另外 3 条旧日志计数不纳入执行范围，也未被自动完成。
- 当前完成 `177` 条，pending `2325`；change-set 共 `844` 个唯一 change ID，归档页 `839` 条。
- 最新暂存主表 SHA-256：`bf571e8066aa0095d62e303cfbd107e892623f813155a85a80bf839502c58c5b`；按细胞汇总：`1ee6bd6bdb9ddde0b3f7f505021050953104685f02e89b7a366553e5718d74f8`。

## Astra source-window 修正执行结果

- 回退脚本：`revert_source_context_batch_astra.py`，已按幂等逻辑执行；不会因重复执行产生重复 change ID。
- Astra 点名的 `M00846`、`M00859`、`M00860`、`M00883` 已用正确正文窗口完成逐条负向复核；`M00868` 因 SOX2(cid:3)/SOX2+ 符号歧义及缺少 PDF，继续 pending。
- 暂存工作簿已重建；正式源表两份 SHA-256 与启动基线一致，证据引用可解析，change ID 无重复。

## Astra 修正后的逐条语义复核

- 固定清单 330 条重新定位最佳正文窗口，完成 `329` 条目标基因—细胞语境、表达方向和限定条件的逐条复核；新增语义证据组与 `SRCCTX-SEMANTIC` 变更链。
- 当前完成 `506` 条、pending `1996` 条；change-set 共 `1173` 个唯一 change ID，归档页 `1168` 条。
- `M00868` 的候选 evidence、hold 原因和 PDF 待核状态均保留在 `review-records.json` 与 selection 文件中。

## 第二批 source-context 语义复核

- 固定 `source_context_semantic_batch_selection_20260908.json` 的新批次 `520` 条，跨 tasks 1–44，独立重算 source-context 最佳窗口；不扩展上一批固定 330 条清单。
- `512` 条已完成目标基因—细胞语境、表达方向和限定条件复核；`M00102`、`M00103`、`M00389`、`M00390`、`M00694`、`M00868`、`M01528`、`M02547` 共 `8` 条继续 held pending。
- 当前完成 `1018` 条，pending `1484` 条；change-set 共 `1685` 个唯一 change ID，`audit_archive_20260907` 为 `1680` 条归档行。
- `M00868` 继续因 PDF/SOX2 符号歧义待核；其余 hold 是缺少目标基因级限定或当前 source_context 无法安全裁决，未强行完成。

## Pending 清理完成

- 第三至第七批继续完成 `819` 条 source-context/上下文语义复核；另有 `445` 条继承上一轮已有的 `include/no_change` 快速一致性裁决，并明确标注未重新逐句复核的限制。
- 此前 hold 中 `15` 条已补充目标基因级语义解释；`M00868` 根据正文 `SOX2(cid:3)` 与同文符号编码交叉确认，纠正 source_context 的 `SOX2+` 转换误读，保留原 `low` 极性。
- 当前 `2502/2502` 条审核记录均已完成，`pending=0`；change-set `3169` 个唯一 change ID，`audit_archive_20260907` 为 `3164` 条归档行；active `2490`，正式源表未修改。
- 机器校验显示 `2023` 条完成记录有本轮目标级证据绑定，另 `479` 条为带限制的历史快速一致性继承记录；请优先抽样这些记录及所有 no_change 记录。

## 验收入口

- 逐项审核：`review-records.json`
- 本轮证据：`evidence.json`
- 精确变更：`change-set.json`
- 启动快照与哈希：`baseline-manifest.json`、`baseline/`
- 暂存主表：`staged/our_markers.xlsx`
- 暂存按细胞汇总：`staged/our_markers_by_cell.xlsx`
- 机器校验：`validation.json`

暂存文件 SHA-256：主表 `4f3d19a74a5012c9451120280fe91424c4654eaf5be751556b92749658fbb36c`；按细胞汇总 `29f4e3f3316fb791f32a80c5d242928b10bac1f9bf81574ed1b7c7166ee6589e`。

最新回退后暂存文件 SHA-256：主表 `bf571e8066aa0095d62e303cfbd107e892623f813155a85a80bf839502c58c5b`；按细胞汇总 `1ee6bd6bdb9ddde0b3f7f505021050953104685f02e89b7a366553e5718d74f8`。上一行旧 hash 仅代表回退前暂存物，已被本次重建结果取代。

最终重建后暂存文件 SHA-256：主表 `faa6df5316b6edf540687336c3ce23d67b8074933951b14dac9c627d2fadacc1`；按细胞汇总 `3f3baacd2406ac33cb8ef02f00c3d136bc75cdf30db822999ffacedcee59ba50`。

最终幂等复跑并重建后暂存文件 SHA-256：主表 `d99a08f4f2b74d4df9f04cc4e9b401eb7b0433ed9c00d8f17a6fcfdddda951ec`；按细胞汇总 `24cc6e37bf347b6c1fd5dedff42dc514d35f0c91b65d977babbf976834ac88d8`。

最终第二批复核后暂存文件 SHA-256：主表 `94572b7ce6a963ce9e41c42bf9d95466fa0aec53aefae61886363b5020061f7c`；按细胞汇总 `41ac1df17fc91fbbaa6409fd747d588b65b48449ef7f9dacea0e8cf4ed2b0c17`。

最终 pending 清理完成后暂存文件 SHA-256：主表 `a79787e2862714e06e56e2014580bb6201791cce07f25d3bf9da283e13c174e9`；按细胞汇总 `829166241dec28ac50e73e7b3b4d653d081dc4f567bc72f2ee5641c42f4a274b`。

Astra 请直接检查原始正文/图注/图像和暂存工作簿，重点审核所有 restore/update/archive 动作、`audit_archive_20260907` 的 31 个原始字段、汇总谱系/组织恢复、`479` 条历史快速一致性继承记录，以及从每篇论文的 `no_change` 中独立抽样。当前交付明确不是终版，也不代表正式表已发布。
