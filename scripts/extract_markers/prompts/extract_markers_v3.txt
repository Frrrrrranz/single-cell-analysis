你是一位单细胞组学专家。请从以下论文中提取所有细胞类型及其 marker 基因。

【核心要求】
- 提取论文中出现的所有细胞类型及其 marker 基因，不限于某一类细胞
- 包括但不限于：神经元、胶质细胞、上皮细胞、免疫细胞、内皮细胞、成纤维细胞、干细胞、间质细胞等
- 只要论文通过 scRNA-seq 鉴定了细胞类型并提到了用于注释/区分的 marker 基因，就必须提取

【输入要求】
- 只关注 scRNA-seq 分析的 Results、Methods（细胞注释部分）、Figure legends 和 Supplementary tables
- 忽略参考文献页、版权声明、作者贡献等无关页面
- 保留论文原文的基因名写法，不做任何大小写转换（原文写 Mpz 就保留 Mpz，不要转成 MPZ）
- 特别注意：差异表达基因（DEG）不等于 marker 基因。只有论文明确用于注释/区分细胞类型的基因才算 marker

【species 判定】
- 根据论文实验对象填写每个细胞类型对应的物种：human / mouse / rat（单值）
- 跨物种同类型细胞须分条记录各自 species

【is_pns_cell 判定】
- true：外周神经系统相关的神经/胶质细胞（sensory neuron / sympathetic neuron / parasympathetic neuron / enteric neuron / Schwann cell / satellite glia / enteric glia / autonomic neuron 等）
- false：非 PNS 细胞（上皮/免疫/内皮/成纤维/平滑肌/红细胞/胰岛细胞/肝细胞等）
- NA：边界细胞或证据不足无法判定

【证据等级判断标准】
为每个 marker 标注 evidence_level：
1. explicit（明确声明的 marker）：论文明确写 "X is a marker for Y" / "X was used to identify Y" / 专门 marker 基因表 / Methods 注明注释依据
2. implied（隐含的 marker）："X is specifically expressed in Y" / "X was enriched in Y" / 热图或气泡图上作为细胞类型标志基因展示 / Figure legend 强调
3. inferred（从结果推断）：DotPlot/FeaturePlot 中明显区分该细胞类型的基因，论文未明确描述 / UMAP 注释图旁高亮的基因
4. imported（外部导入）：引用其他论文的 marker / 领域常识性 marker。除非论文明确说明，否则不要使用此级别

【输出要求】
严格按以下 JSON 格式输出，不要添加任何额外说明、代码围栏或注释：

{
  "paper_id": "自动检测的 paper_id",
  "cell_types": [
    {
      "cell_type": "细胞类型名称（使用论文原文术语）",
      "subtype": "亚型名称（如有，否则 null）",
      "species": "human / mouse / rat",
      "is_pns_cell": "true / false / NA",
      "markers": [
        {
          "gene": "基因名（原文写法，不做大小写转换）",
          "evidence_level": "explicit",
          "source_section": "在论文中的位置（Table S2 / Fig.1A / Results p.5）",
          "source_context": "包含该基因的原文句子或上下文片段"
        }
      ]
    }
  ]
}

【注意事项】
1. 基因名禁止做任何转换——原文全大写就全大写，原文首字母大写就首字母大写
2. cell_type 名称必须与论文原文一致，不要自创命名，也不要强行归一化到词表
3. 同一细胞类型的不同亚型请分开列出（subtype 字段不同）
4. 如果论文确实没有提到任何 marker 基因，返回空数组：{"cell_types": []}
5. source_section 必须具体到 Table/Figure 编号或章节名（如 "Table S2" / "Results p.5" / "Fig.3A"）
6. source_context 应包含足够的上下文以便复核者定位原文位置
7. 同一 marker 基因如果出现多次，取证据等级最高的那次即可，不要重复
8. 必须提取论文中所有被鉴定的细胞类型，不要因为某细胞类型不属于某一特定类别而跳过
