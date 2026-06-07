# GSE181316_规范版.xlsx 表格评估报告

> 评估依据：以 `ENEURO.0066-20.2020.full`（eNeuro 2020）为完整汇报标杆，参考 `PNAS.117.9466.2020.full` 和 `COMMUN-BIOL.5.1105.2022.full` 的汇报材料，评估表格是否满足老师要求的文献阅读规范。

---

## 一、总体评价

**表格设计规范、结构清晰，但存在若干关键信息缺失和字段设计不足。** 表格采用了 4 表拆分设计（papers / datasets / cell_types / processing），遵循了良好的数据库规范化原则。README 表提供了详细的元数据说明，体现了严谨的数据管理意识。

---

## 二、逐项评估：老师要求的 5 个关注点

### 1. 数据下载（data availability）

| 评估项 | 现状 | 评价 |
|--------|------|------|
| GEO 编号 | ✅ `GSE181316`，已填写 | 合格 |
| 数据可获取性 | ✅ `data_availability = both`（supplementary + SRA raw reads） | 优秀 |
| 下载链接 | ✅ `accession_url` 已填 | 合格 |
| 平台信息 | ✅ `10x Chromium 3'`，`vendor = 10x Genomics` | 合格 |
| 样本数 | ✅ `n_samples = 8`，README 有详细说明 | 合格 |
| 细胞总数 | ❌ `n_cells = NA` | **缺失** |

**问题：** `n_cells` 字段为 NA。三篇参考文献均明确报告了细胞总数：
- eNeuro: 13,200 → 质控后 12,236
- PNAS: 5,400 个高质量细胞
- Commun Biol: 16,259 个施万细胞（全局更多）

**建议：** 从正文或补充材料中补全细胞总数，或标注"待从 matrix 统计"。

---

### 2. Marker（标志基因）

| 评估项 | 现状 | 评价 |
|--------|------|------|
| 是否记录 marker | ✅ `markers` 字段已填 | 合格 |
| marker 来源 | ✅ `provenance = Table S2; Table S3` | 合格 |
| 施万细胞 marker | ✅ `S100B;NGFR` | 合格 |
| 其他细胞 marker | ✅ 各细胞类型均有 | 合格 |

**问题：** marker 字段仅记录了基因名称，**缺少以下关键信息**：

1. **缺少 marker 的验证层级说明**——参考 eNeuro 的做法：
   - 感觉神经元：转录组 + 蛋白质组（CSC-MS 608种蛋白）双重验证
   - 运动神经元：仅转录组数据
   - 建议增加 `marker_validation` 字段，标注"transcriptome-only" / "transcriptome+proteome" / "已验证"

2. **缺少 marker 的特异性说明**——参考 PNAS 的做法：
   - Apod 被鉴定为 nmSCs 高特异性新型标志物
   - Sfrp4 被鉴定为神经成纤维细胞特异性标志物
   - 建议增加 `marker_specificity` 字段或注释

3. **施万细胞 marker 过于简单**——仅 S100B;NGFR，参考三篇文献：
   - eNeuro: Sox10, Ngfr, S100b, Mbp, Plp1（区分有髓/无髓）
   - PNAS: 有髓 SC（Mbp, Plp1, Mpz, Prx）vs 无髓 SC（Apod, Ngfr）
   - Commun Biol: 有髓（Mbp, Plp1, Mpz, Prx）vs Remak（Cdh2, Ngfr）vs 修复型（Ngfr高表达）

---

### 3. 组织来源（tissue）

| 评估项 | 现状 | 评价 |
|--------|------|------|
| 组织类型 | ✅ `tissue = skin innervation` | 合格 |
| 物种 | ✅ `species = human` | 合格 |
| 条件/分组 | ✅ `condition = keloid;normal skin;normal scar` | 合格 |

**问题：**

1. **`tissue = skin innervation` 不够精确**——三篇参考文献的组织来源描述：
   - eNeuro: 大鼠坐骨神经（明确到具体神经）
   - PNAS: 小鼠臂丛神经 + 坐骨神经
   - Commun Biol: 大鼠坐骨神经
   - 建议改为 `skin (innervated)` 或 `skin with PNS innervation`，或增加 `tissue_detail` 字段说明具体解剖部位

2. **缺少解剖分区信息**——参考 Commun Biol 的做法：
   - 区分了神经外膜（epineurium）、束膜（perineurium）、内膜（endoneurium）
   - 不同分区的成纤维细胞亚型不同
   - 建议增加 `anatomical_compartment` 字段

---

### 4. 神经细胞（neural cells）

| 评估项 | 现状 | 评价 |
|--------|------|------|
| 是否标注 PNS 细胞 | ✅ `is_pns_cell` 字段 | 优秀 |
| 施万细胞标注 | ✅ `Schwann cell = true` | 合格 |
| 其他神经细胞 | ✅ 非神经细胞均标 false | 合格 |

**问题：**

1. **施万细胞亚型缺失**——三篇参考文献均对施万细胞进行了精细分型：
   - eNeuro: 髓磷脂化 SC / 非髓磷脂化 SC / 修复型 SC
   - PNAS: 有髓 SC（mySCs）/ 无髓 SC（nmSCs）
   - Commun Biol: 有髓 SC / Remak SC / 修复型 SC / 分裂期 SC
   - 当前表格 `subtype = NA`，**建议补充施万细胞亚型**

2. **缺少"为什么没有神经元"的说明**——三篇参考文献均明确解释了：
   - 神经元胞体不在坐骨神经/外周神经组织中
   - 标准 scRNA-seq 只能捕获有核细胞
   - 当前表格 README 未提及此关键信息

3. **缺少神经元数据的引入方式**——参考 eNeuro 的做法：
   - 感觉神经元（DRG）：自行培养 + 双重验证
   - 交感神经元（SCG）：自行培养 + 双重验证
   - 运动神经元：公共数据库（仅转录组）
   - RGCs：公共数据库（仅转录组）
   - 当前表格未涉及神经元数据来源

---

### 5. 数据统计方法（processing / analysis methods）

| 评估项 | 现状 | 评价 |
|--------|------|------|
| 软件工具 | ✅ `software = Seurat` | 合格 |
| 质控标准 | ✅ `qc` 字段已填 | 合格 |
| 标准化方法 | ✅ `normalization = SCTransform` | 合格 |
| 批次校正 | ❌ `batch_correction = NA` | **缺失** |
| 降维方法 | ❌ `dim_reduction = NA` | **缺失** |
| 聚类方法 | ❌ `clustering = NA` | **缺失** |
| 注释方法 | ✅ `annotation = marker-based` | 合格 |
| 差异表达 | ❌ `diff_expr = NA` | **缺失** |
| 细胞通讯 | ❌ `cell_comm = NA` | **缺失** |
| 轨迹分析 | ❌ `trajectory = NA` | **缺失** |

**问题：** processing 表大量字段为 NA，而三篇参考文献均有详细的方法学描述：

| 方法 | eNeuro | PNAS | Commun Biol |
|------|--------|------|-------------|
| 测序平台 | Drop-seq | 10X Genomics v2 | 10X Genomics v2 |
| 比对工具 | - | CellRanger v3.0.2 | CellRanger v3.0.0 |
| 标准化 | scran | sctransform | sctransform |
| 批次校正 | **Harmony** | Harmony | Harmony |
| 降维 | PCA + t-SNE | PCA + UMAP | PCA + UMAP |
| 聚类 | SNN modularity | Seurat v3.0.0 | Leiden |
| 细胞通讯 | **Cellcellinteractnet** (自定义) | **CellPhoneDB** | **SingleCellSignalR** |
| 验证方法 | **CSC-MS 质谱** | RNAscope + IHC | RNAscope |

**建议补充：**
- `batch_correction`: Harmony（如使用了）
- `dim_reduction`: PCA + UMAP
- `clustering`: Leiden 或 Louvain
- `diff_expr`: Wilcoxon rank-sum test（如使用了）
- `cell_comm`: CellPhoneDB / SingleCellSignalR / Cellchat（如使用了）
- 增加 `alignment_tool` 字段：CellRanger / STARsolo / Kallisto
- 增加 `validation_method` 字段：RNAscope / IHC / CSC-MS / flow cytometry

---

## 三、与三篇参考文献的对比总结

### 3.1 表格已覆盖的共性要素（✅）

| 要素 | eNeuro | PNAS | Commun Biol | 当前表格 |
|------|--------|------|-------------|----------|
| GEO 编号 | ✅ GSE147285 | ✅ 有 | ✅ 有 | ✅ GSE181316 |
| 细胞类型列表 | ✅ 7种 | ✅ 12种 | ✅ 32亚群 | ✅ 11种 |
| 标志基因 | ✅ | ✅ | ✅ | ✅ |
| 软件工具 | ✅ | ✅ | ✅ | ✅ Seurat |
| 物种 | ✅ 大鼠 | ✅ 小鼠 | ✅ 大鼠 | ✅ 人 |

### 3.2 表格缺失的共性要素（❌）

| 要素 | eNeuro | PNAS | Commun Biol | 当前表格 |
|------|--------|------|-------------|----------|
| 细胞总数 | ✅ 12,236 | ✅ 5,400 | ✅ 大量 | ❌ NA |
| 批次校正方法 | ✅ Harmony | ✅ Harmony | ✅ Harmony | ❌ NA |
| 降维方法 | ✅ PCA+t-SNE | ✅ PCA+UMAP | ✅ PCA+UMAP | ❌ NA |
| 聚类算法 | ✅ SNN | ✅ Seurat | ✅ Leiden | ❌ NA |
| 细胞通讯工具 | ✅ Cellcellinteractnet | ✅ CellPhoneDB | ✅ SingleCellSignalR | ❌ NA |
| 施万细胞亚型 | ✅ 3种 | ✅ 2种 | ✅ 4种 | ❌ 无亚型 |
| 验证方法 | ✅ CSC-MS | ✅ RNAscope+IHC | ✅ RNAscope | ❌ 无 |

### 3.3 当前表格独有的优势（🌟）

| 优势 | 说明 |
|------|------|
| 规范化 4 表设计 | papers/datasets/cell_types/processing 拆分合理 |
| is_pns_cell 字段 | 明确标注是否为 PNS 神经细胞，三篇文献均未做此标注 |
| README 元数据 | 详细的变更记录和数据来源说明 |
| 受控词表意识 | 有缩写映射和词表外标注机制 |

---

## 四、改进建议（按优先级排序）

### 🔴 高优先级（必须补充）

1. **补全 processing 表的方法学字段**——至少补充：
   - `batch_correction`（是否使用了 Harmony/CCA/其他）
   - `dim_reduction`（PCA + UMAP/t-SNE）
   - `clustering`（Leiden/Louvain/其他）
   - `cell_comm`（CellPhoneDB/SingleCellSignalR/Cellchat/其他）
   - 增加 `validation_method` 字段

2. **补充施万细胞亚型**——在 `subtype` 字段中标注：
   - 有髓 SC / 无髓 SC / 修复型 SC（如文献有区分）
   - 或标注"未细分"

3. **补充细胞总数**——`n_cells` 从正文或 matrix 统计补全

### 🟡 中优先级（建议补充）

4. **增加 marker 验证层级说明**——新增字段或注释：
   - `marker_validation`: transcriptome-only / transcriptome+proteome / IHC-validated

5. **增加解剖分区信息**——新增 `anatomical_compartment` 字段：
   - epineurium / perineurium / endoneurium / whole nerve

6. **补充"无神经元"的说明**——在 README 或注释中说明：
   - 皮肤 scRNA-seq 只能捕获有核细胞
   - 神经元胞体不在皮肤组织中

### 🟢 低优先级（锦上添花）

7. **增加细胞通讯的具体通路记录**——新增 `cell_comm_table` 或字段：
   - 记录关键 LR 对（如施万细胞→成纤维细胞的 Cntf→Cntfr 通路）

8. **增加跨文献对比字段**——新增 `comparable_to` 字段：
   - 标注与哪些已收录文献的细胞类型/方法可比

---

## 五、结论

**表格整体设计规范，结构合理，但在"数据统计方法"和"细胞亚型精细度"两个维度上存在明显不足。** 以 eNeuro 文献的完整汇报为标准，当前表格缺失了约 40% 的关键信息（主要集中在 processing 方法和细胞亚型细分）。建议优先补充 processing 表的方法学字段和施万细胞亚型信息，使表格能够真正满足老师要求的"文献阅读规范"。
