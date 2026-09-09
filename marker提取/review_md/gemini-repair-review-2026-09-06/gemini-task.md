# 可直接转发 Gemini 的材料整理任务

Codex 已完成第三、四轮修补交付审查，报告在：
`D:\OneDrive\Desktop\组\marker提取\review_md\gemini-repair-review-2026-09-06\review.md`。

本次请做可机械核验的交付整理和证据定位，不重新生成一套精选 marker。先读报告与 MARKER_POLICY.md。保留 marker_Gemini、marker_Gemini_repair、正式 Excel、Codex 审查文件不动；新输出放 `marker_Gemini_evidence_v2/`。

1. **核对 23 篇文献身份与来源。** 从实际 PDF 首页读取标题、DOI、PMID（未出现则注明依据）、完整文件名和页数，不能沿用 default_titles。修正错误主题以及 07315 的不存在来源文件。保存 paper_manifest.json。

2. **重做可追溯增量台账。** 对 1,015 条正式记录和所有 context/excluded/unresolved，逐条记录原 record_id、新 record_id、总表 marker_id（允许多值）、动作、匹配键和理由。953 条已关联总表的记录标为 baseline_existing；未比较实验条件、测量实体或细胞粒度时标为待裁决。禁止按新旧数量差称新增，禁止改写原 marker_original。

3. **按原始 28 个 ID 建立问题表。** 以 Codex 的 unresolved-28-review.md 为清单，每条单独一行，不混入已纠正项凑数，不合并多个基因。保留原未决原因、此次真实材料、页码、观察结果和剩余缺口。未找到证据不自动宣称全文不存在；已撤销条目与仍未决分开。

4. **准备有限范围的原图证据包。** 优先 eLife Fig.1B/D、iPain Fig.1d/h、膀胱正文 Schwann cluster 段落、01243 Extended Data Fig.10g，以及原28项各自声称的位置。每个面板保存清晰截图，文件名含 paper_id、PDF页码、panel。图像观察与逐字引文分开；不要擅自换基因或展开联合群。Codex 已更正：eLife PNEC 为 RIMS2，不是此前写的 CHGB；LAMC3/FCN1 配对须重新核图。iPain Cd86 不能借神经母细胞瘤 M01336 的裁决。PRR4 蛋白识别证据不能因 IHC 而排除。

5. **材料状态逐文件登记。** 区分实际已读范围、已有但未读、缺失、不可读、不可访问；此前是否读过无法证明时注明历史未知，不补写历史状态。主文、图像、图注、附件分开。不能因为有 repair JSON 就设全部 reviewed。暂不开展前20篇的新提取。

6. **只从最终数据生成统计。** 校验重复 ID、错链 ID、文件存在性、页码范围、未决/撤销类别、标题一致性和逐项数量。缺失材料如实报告；不得追求0警告。脚本检查不声称证明引文真实或全文穷尽。

交付 paper_manifest.json、record_crosswalk.json、unresolved_28.json、materials_manifest.json、evidence/截图与索引，以及一份简短 summary.md。将不确定项留给 Codex 最终裁决，无需再次等待执行批准。
