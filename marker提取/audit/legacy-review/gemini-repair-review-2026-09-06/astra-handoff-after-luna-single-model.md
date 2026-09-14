# 下一会话 Astra 交接：审核 Luna 最新 Marker 收尾交付

编制日期：2026-09-06  
项目根：`D:\OneDrive\Desktop\组`  
推荐审查模型：GPT-6 Astra，思考档位 medium（沿用用户此前配置，实际以用户选择为准）

## 1. 你的任务

用户报告Luna最新单模型任务已完成，希望新会话了解上下文并审核其成果。本文件不是终审结论，也不是继续运行Luna旧脚本的指令。

请直接检查最新交付，判断：

1. 两份正式表是否正确发布、结构和汇总是否可靠；
2. 18项已发布变更是否有原始证据支持；
3. “全量2,499条处理、pending=0”是否实质完成了用户要求的筛错，而不仅是建立台账；
4. 历史候选与风险集合是否有真实处理闭环；
5. 这份结果能否称为相对完善的终版，若不能，明确最小必要补核范围。

先进行只读审核并形成具体报告。不要因旧流程写着“Astra批准”就重新启动多模型交接，也不要自动恢复旧表、重新执行发布脚本或批量重提取。若用户同时明确要求修复，沿用既有证据、备份与定向变更规则实施；不要为了审查本身先修改待审成果。

## 2. 用户已确认的目标与工作偏好

- 默认简体中文，结论清楚、简洁，文件用可点击绝对路径。
- Marker已经多轮提取，重心是筛错、纠错和剔除错误关系；明显遗漏顺带补充，不做全文重提取或系统性补漏。
- 用户希望得到相对完善的正式`our_markers.xlsx`及同步按细胞汇总表，不满足于只增加待办或候选。
- 最初设计Gemini首筛、Luna复筛、Astra终审，之后为避免共享工作区冲突改为串行；再经用户同意，后续工作改为Luna单模型一次连续完成，含验证后正式发布。
- 当前最新执行依据是同目录`luna-single-model-completion.md`，不是旧`operations-manual.md`的角色交接要求。
- 不因阴性/low门控、共享表达、非特异、非PNS、非L1–L4、非目标组织或蛋白证据删除真实marker。最终看作者是否实际识别、注释、分选或验证了关系。
- 未决不等于错误；必须保留原记录和历史，不能物理抹去。缺少证据不允许伪造通过，也不能无边界追查。

## 3. 先读哪些文件

审查目录根（下称R）：

`D:\OneDrive\Desktop\组\marker提取\review_md\gemini-repair-review-2026-09-06`

最新Luna工作目录（下称L）：

`D:\OneDrive\Desktop\组\marker提取\review_md\gemini-repair-review-2026-09-06\execution\luna-single-model`

建议顺序：

1. 本文件、`marker提取/MARKER_POLICY.md`、适用AGENTS.md。
2. R下`luna-single-model-completion.md`，了解真实验收门槛。
3. L下`final-report.md`、`PROGRESS.md`、`release.json`、`validation.json`、`published-verification.json`。
4. L下`change_set.json`、`registry/decisions.json`、`registry/evidence.json`、`registry/coverage.json`、`registry/records.json`。
5. L下`registry/historical-crosswalk.json`、`registry/unresolved.json`、`registry/audit_append.json`、`context-match-analysis.json`、`paper-decision-counts.json`及按需检查点。
6. **必须读生成逻辑**：L下`build_registry.mjs`、`build_staged_workbooks.mjs`、`validate_staged.mjs`、`verify_specific_changes.mjs`、`verify_published.mjs`。只读，不直接执行有写入行为的脚本。

旧交付仅作追溯：R下`execution/gemini_tasks/round1-screening/`和`execution/luna_tasks/round2-screening/`。旧Luna的`_build_outputs.py`曾批量生成语义结论，不能当新证据。

## 4. 当前文件状态：哪些已核实，哪些只是报告声明

本交接编写时实际计算了两份正式文件SHA-256，确认与最新release一致：

| 文件 | 当前实测SHA-256 |
|---|---|
| marker提取/表单/our_markers.xlsx | 7873af98ed720a825236d6b526cb575c8ccbbad183b814515eb46866de8a1a4f |
| marker提取/表单/our_markers_by_cell.xlsx | ff3b687008891e580f1bd67c67f99e78a0de1d705c69f8760a8ff72b7ca1d072 |

开始审核时重新计算，变化需解释，不能强制恢复这些值。

最新run_id为`20260906-luna-single-model`。实际交付直接在L下，不存在将全部成果放到run_id子目录的约定结构；只有baseline使用该子目录。不要因目录结构不同误报文件丢失。

启动基线快照位于：

`L/baseline/20260906-luna-single-model/`

包含两份Excel、`baseline_workbook_manifest.json`、`our_markers-data.json`、`our_markers_by_cell-data.json`。启动基线哈希：

- 主表：`8abdddb800dce6e84ca711d9cb5905cc114390e77adc499f8ef5471f09021373`
- 汇总表：`9b166cd7aef77d39c8019dcc163a6e2aa8dd0ab74927dbe0195060390062c3e2`

**以下是Luna声明，尚未由本交接编写者重新解析工作簿独立验收：**

- 基线2,499条、43篇；发布后2,488条active、43篇。
- 新增3、修改1、合并归档13、上下文转存1，共18项正式变更。
- 候选排除3、候选未决11，不是从基线移出14条。
- 数量公式：2499 + 3 - 13 - 1 = 2488。
- `release.status=published`，`validation_status=passed_with_documented_limitations`。
- `published-verification.json`采用“暂存导入验证＋正式文件哈希一致”，不等于独立重新打开正式工作簿逐项验收。

本次为准备上下文，仅做文件读取、哈希核对、脚本检查和JSON统计，未修改正式表、未完成本轮生物学终审。

## 5. 本轮最重要的待审问题

### A. 全量完成状态可能由程序批量生成，必须优先查

`build_registry.mjs`约第163行起遍历所有基线记录，第176行默认`semantic='include'`，对旧Luna单元继承旧判断；其余记录以关键词定位或历史来源记录形成证据。约第420行直接写`processed_baseline=baselineRecords.length`和`pending_baseline=0`。

当前`registry/evidence.json`实际JSON统计为：

- 1,008个`historical_evidence_reused_with_limit`；
- 1,018个`luna_context_crosschecked`；
- 1个`luna_reopened_visual_confirmed`（LAMC3）；
- 14个顶层没有verification_status的旧证据包装项，应查看嵌套内容，不能直接判为缺失。

前两类合计2,026，正是之前未覆盖基线的数量。**这些是证据对象数量，不是准确率或已证实错误数量。**

约第241–247行：只要找到了关键词行，就将旧表`source_context`填入`verbatim_quote`并标为context_crosschecked；没有行则保留历史定位。应抽查引用是否真能逐字回到所报行，避免“找到基因/细胞词”被升级为“核实完整关系或引文”。

需要审查的是实际查证是否发生及是否充分，不能单凭脚本存在断言模型完全没读过资料；也不能凭披露“沿用历史”就接受全量终审通过。请检查真正的具体证据、检查点及局部来源。

### B. 历史集合可能只复制，未完成逐项处置

约第425行的historicalCrosswalk将旧received_crosswalk、mapping_differences和audit数据包装保存。需要核查原62候选、原28未决、28条context_only、121条excluded、953条回填是否关联到本次实际裁决，而非仅出现在JSON中。

这些集合重叠，不能直接相加，也不能把17个旧候选当作原62项已处理子集而不做映射。

### C. 所有18项已发布变更均需逐项核验

新增：

| ID | 申报关系 | 重点 |
|---|---|---|
| M02590 | RIMS2—Pulmonary neuroendocrine cell | Fig.1D对应、真实marker用途、是否已有同关系 |
| M02591 | PRR4—SMG Serous Cell | 本文实际使用HPA/IHC证据还是纯外引；模态与来源准确性 |
| M02592 | LAMC3—Pericyte | 对应方向已在前会话读图确认；查重复与正式标签，change_set中仍出现`Pericyte (claimed in repair)`，不宜把历史申报备注当成作者细胞名称 |

修改M00071：Rbfox3/NeuN的cell_type改为`nociceptors/neurons`。须判断是否有证据支持泛化，是否完整保留衰老实验上下文。“不是衰老特异marker”本身不足以更改作者定义的实验细胞关系。

M01510：Sst转context_only。检查引文是引言背景这一事实是否充分支持本条处置，不能只看一个位置就宣称全文未使用。

13组合并源→目标：

```text
M00047→M00036  M00048→M00038  M00050→M00039
M00417→M00415  M00418→M00416  M00456→M00455
M00466→M00460  M00467→M00462  M00494→M00491
M00531→M00530  M00554→M00553  M00592→M00585
M00597→M00594
```

核对物种、方向、亚群、条件、来源与完整关系；名称单复数相同不能替代语义判定。检查合并后原来源全部留存，保留目标行是否丢掉必要证据。

### D. 工作簿和汇总需独立复核

- 比较基线和正式Excel实际数据，不只比较Luna自己生成的registry。
- 验证change_set外字段未变、源记录已归档、审计完整、ID唯一、未决未进入已确认集合。
- `validation.json`记录主表table范围`A1:AE2503`而active声称2,488；检查是否只是残留空行还是范围/表尾真实问题，不预先定性。
- 汇总行数在validation为1,058，在release/published verification为1,057；先区分是否包含表头。
- 汇总示例中谱系、组织、阶段等多列为空：比较原汇总是否已有值，判断是否重建导致字段丢失。空值本身不证明回归。
- 实际检查格式、筛选、冻结窗格、公式与可读性，查看视觉证据而非只读通过标志。

## 6. 历史错误与正确使用方式

前会话曾简单比较Gemini和Luna：Luna对政策理解较好，但两者均有错误，不能把“选了Luna”理解为其结论可信度自动提高。

已实际打开的eLife图：

`D:\OneDrive\Desktop\组\marker_Gemini_evidence_v3\evidence\DOI_10.7554_elife.62522_p4_Fig1D_dotplot_detail.png`

该图显示LAMC3—Pericytes、COL2A1—Chondrocytes。旧Gemini/Luna一致判为LAMC3错配是共同错误，前会话已明确撤回，最新Luna已申报纠正。对此可核实落实，不重新采信旧错误总结。

其余FCN1、Cd86、Glb1候选排除仍需按具体实体/配对审核，不能因LAMC3纠正就一并恢复。PRR4或RIMS2证据可用也不自动说明必须新增。

## 7. 建议审核步骤与停止条件

1. 重新核文件哈希；读取当前正式表与启动快照时应用Spreadsheets技能、运行时及必要的文档/PDF技能。已有Markdown可直接读，图片须实际打开。
2. 独立对账18项变更和工作簿结构；全部18项审查原始依据，不以抽样代替已发布变更审核。
3. 核验13组合并、3新增、1更新、1上下文转存，记录通过/错误/证据不足。
4. 对1,008条历史复用、1,018条上下文检索以及旧473条记录分层抽查；覆盖每篇论文中实际存在的证据类别，优先缺定位、负向门控、跨物种、图示证据及泛化标签。报告抽查ID、样本数和选择规则。
5. 若证实某种自动规则导致一类记录虚假完成，将该受影响集合列为需要补核，不必为了证明同一问题重复抽查所有记录。具体生物学错误则扩大到同面板/同错误类型关联项。
6. 对历史集合逐项对照本次决策引用，判断哪些仅被复制、哪些真正裁决，准确列出缺口。
7. 给出“可接受终版”“已发布但需限定修正”或“全量审核完成声明不成立”等有依据的结论。机械完整性与生物学证据质量分别报告。

不要以全文穷尽或全面补漏为审核目标，也不要根据未找到文本就批量删除已有关系。审查无法解决的具体缺口如实保留。

## 8. 新审核产物和回复方式

审查输出另存到：

`D:\OneDrive\Desktop\组\marker提取\review_md\gemini-repair-review-2026-09-06\astra-audit-after-luna\`

若已存在先读取并接续，保留既有审查历史。建议输出`review.md`、`findings.json`、`sampled-records.json`及必要证据引用。不要改写Luna原交付来让它看起来通过。

向用户先给简短结论：正式发布是否成立、结果是否可信、最重要的具体错误或未完成范围、下一步最少需要做什么。区分“本次实际检查”“Luna自报”“尚待核实”，不要把这份交接中的风险线索全部当成已确认缺陷。

本会话交接准备工作已经完成。下一会话可从第3节文件和第5节优先问题直接开始，无需重新梳理整段聊天历史。
