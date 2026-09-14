# Luna 单模型收尾进度

- run_id: 20260906-luna-single-model
- 执行日期: 2026-09-06
- 执行模型: GPT-5.6 Luna（单模型连续执行）
- 启动基线: 2,499 条 markers；43 篇论文；正式表哈希见 baseline/20260906-luna-single-model/baseline_workbook_manifest.json。
- 基线覆盖: 2,499 / 2,499 已建立稳定 review_id 并完成处理状态；pending=0。旧首轮实际覆盖 473，旧第二轮 490（含17个候选），不作为全量完成替代。
- 本次已知纠错: M00071 更新；M01510 转 context_only；13 条完整重复关系合并归档；RIMS2、PRR4、LAMC3—Pericytes 新增；旧 LAMC3 排除结论被 Fig.1D 实图核对替代。
- 当前变更数: 18；新增 3；修改 1；合并归档 13；context_only 转存 1；候选排除归档 3；候选未决隔离 11；基线未决 0。
- 证据限制: 既有490个单元有逐条旧Luna定位；其余记录登记本地Markdown、原source_locator/source_context与历史交叉表，未将缺少逐字命中的记录伪装成新逐图核验。
- 暂存验证: validation.json = passed_with_documented_limitations；暂存版与正式版发布后 SHA256 一致。
- 正式发布: release.json = published；正式表 active markers=2,488，论文=43；正式表哈希已记录。
- 检查点: checkpoints/*.json；台账: registry/；逐项复核: published-verification.json（若本机 Excel/OneDrive 占用导致二次 Artifact Tool 导入不稳定，以暂存导入验证 + 发布后逐文件 SHA256 相等为发布证据）。
