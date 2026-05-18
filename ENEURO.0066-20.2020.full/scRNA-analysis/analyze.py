# -*- coding: utf-8 -*-
"""
单细胞RNA测序数据分析脚本
文献: Peripheral Nerve Single-Cell Analysis Identifies Mesenchymal Ligands (eNeuro, 2020)
数据: GEO GSE147285 (Drop-seq, 小鼠坐骨神经)

分析流程: 下载数据 → 质控(含双细胞检测) → 标准化 → 降维 → 聚类 → 差异表达分析 → 细胞类型注释 → 配体-受体互作分析
"""

import os
import gzip
import yaml
import requests
import warnings
import numpy as np
import pandas as pd
import scanpy as sc
import matplotlib
matplotlib.use('Agg')  # NOTE: 非交互式后端，用于服务器/脚本环境
import matplotlib.pyplot as plt
import seaborn as sns
import logging

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

warnings.filterwarnings('ignore')

# ============================================================
# 加载配置（从 config.yaml 统一读取参数）
# ============================================================
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.yaml')
with open(CONFIG_PATH, 'r', encoding='utf-8') as f:  # NOTE: config.yaml 使用 UTF-8 编码
    CFG = yaml.safe_load(f)
print(f"[配置] 从 config.yaml 加载参数（resolution={CFG['clustering']['resolution']}, "
      f"DE method={CFG['de']['method']}, mt%={CFG['qc']['max_pct_mt']}）")

# ============================================================
# 目录配置
# ============================================================
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'results')
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 设置 Scanpy 参数
sc.settings.verbosity = 2
sc.settings.figdir = OUTPUT_DIR
sc.settings.set_figure_params(dpi=150, frameon=False, figsize=(8, 6))

# GEO 下载链接（4个样本的 DGE 矩阵）
SAMPLES = {
    'Inj_3d': {
        'url': 'https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSM4423506&format=file&file=GSM4423506%5FInj%5FSciatic%5F3d%2Etxt%2Egz',
        'filename': 'GSM4423506_Inj_Sciatic_3d.txt.gz',
        'condition': 'Injured_3DPI',
    },
    'Neo_FACS': {
        'url': 'https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSM4423507&format=file&file=GSM4423507%5FNeo%5FSciatic%5FFACS%2Etxt%2Egz',
        'filename': 'GSM4423507_Neo_Sciatic_FACS.txt.gz',
        'condition': 'Neonatal_FACS',
    },
    'Neo_Beads': {
        'url': 'https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSM4423508&format=file&file=GSM4423508%5FNeo%5FSciatic%5FBeads%2Etxt%2Egz',
        'filename': 'GSM4423508_Neo_Sciatic_Beads.txt.gz',
        'condition': 'Neonatal_Beads',
    },
    'Uninj': {
        'url': 'https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSM4423509&format=file&file=GSM4423509%5FUninj%5FSciatic%2Etxt%2Egz',
        'filename': 'GSM4423509_Uninj_Sciatic.txt.gz',
        'condition': 'Uninjured',
    },
}

# 文献中的标志基因（用于细胞类型注释）
MARKER_GENES = {
    'Schwann cells': ['Sox10', 'S100b', 'Mbp', 'Plp1', 'Ngfr'],
    'Mesenchymal cells': ['Pdgfra', 'Sox9', 'Dpt', 'Etv1', 'Wif1'],
    'Macrophages': ['Aif1', 'Cd68', 'Lyz2'],
    'Endothelial cells': ['Pecam1', 'Cdh5', 'Cldn5'],
    'Pericytes/VSM': ['Acta2', 'Des', 'Rgs5'],
    'Lymphocytes': ['Ptprcap', 'Cd3e', 'Nkg7'],
    'B cells': ['Cd19', 'Cd79a', 'Ms4a1'],
    'Mast cells': ['Cpa3', 'Kit', 'Fcer1a'],
}

# NOTE: 间充质细胞 ECM 标志基因（用于验证注释结果）
# FIXME: 原命名 LIGAND_GENES 具有误导性，实际为 ECM 蛋白而非配体，已修正
ECM_MARKERS = [
    'Col1a1', 'Col1a2', 'Col3a1', 'Col6a1', 'Col6a2', 'Fn1', 'Sparc',
    'Ctgf', 'Tgfbi', 'Sparcl1', 'Mdk', 'Ptprd', 'Slit2', 'Gas6',
]


# ============================================================
# 步骤 1：下载数据
# ============================================================
def download_data():
    """从 GEO 下载 DGE 矩阵文件（带重试机制）"""
    import time
    print("=" * 60)
    print("步骤 1：下载数据")
    print("=" * 60)
    for name, info in SAMPLES.items():
        filepath = os.path.join(DATA_DIR, info['filename'])
        if os.path.exists(filepath) and os.path.getsize(filepath) > 100000:
            print(f"  [跳过] {info['filename']} 已存在")
            continue
        # NOTE: 删除可能损坏的部分下载文件
        if os.path.exists(filepath):
            os.remove(filepath)
        for attempt in range(3):
            try:
                print(f"  [下载] {info['filename']} (尝试 {attempt+1}/3) ...")
                resp = requests.get(info['url'], stream=True, timeout=300)
                resp.raise_for_status()
                with open(filepath, 'wb') as f:
                    for chunk in resp.iter_content(chunk_size=65536):
                        f.write(chunk)
                size_mb = os.path.getsize(filepath) / (1024 * 1024)
                print(f"         完成 ({size_mb:.1f} MB)")
                break
            except Exception as e:
                print(f"         失败: {e}")
                if os.path.exists(filepath):
                    os.remove(filepath)
                if attempt < 2:
                    time.sleep(5)
                else:
                    raise RuntimeError(f"下载 {info['filename']} 失败，请检查网络")
    print()


# ============================================================
# 步骤 2：读取数据并合并
# ============================================================
def load_and_merge():
    """读取所有样本的 DGE 矩阵并合并为一个 AnnData 对象"""
    print("=" * 60)
    print("步骤 2：读取数据并合并")
    print("=" * 60)
    adatas = []
    for name, info in SAMPLES.items():
        filepath = os.path.join(DATA_DIR, info['filename'])
        print(f"  [读取] {info['filename']} ...")

        # Drop-seq DGE 是 基因(行) × 细胞(列) 的 TSV 文件
        df = pd.read_csv(filepath, sep='\t', index_col=0, compression='gzip')
        # 转置为 细胞(行) × 基因(列)，这是 Scanpy 的标准格式
        adata = sc.AnnData(df.T)
        adata.obs['sample'] = name
        adata.obs['condition'] = info['condition']
        # NOTE: 为每个细胞的 barcode 添加样本前缀，避免不同样本间 barcode 冲突
        adata.obs_names = [f"{name}_{bc}" for bc in adata.obs_names]
        adata.var_names_make_unique()

        print(f"         {adata.n_obs} 个细胞, {adata.n_vars} 个基因")
        adatas.append(adata)

    # 合并所有样本
    adata = sc.concat(adatas, join='outer')
    adata.obs_names_make_unique()
    # NOTE: outer join 会产生 NaN（不同样本检测到的基因集不完全一致），填充为 0
    import scipy.sparse as sp
    if sp.issparse(adata.X):
        adata.X = adata.X.toarray()
    adata.X = np.nan_to_num(adata.X, nan=0.0)
    print(f"\n  [合并] 总计 {adata.n_obs} 个细胞, {adata.n_vars} 个基因")
    print()
    return adata


# ============================================================
# 步骤 3：质控过滤
# ============================================================
def quality_control(adata):
    """质控：过滤低质量细胞和低表达基因"""
    print("=" * 60)
    print("步骤 3：质控过滤")
    print("=" * 60)
    n_before = adata.n_obs

    # 计算 QC 指标
    # NOTE: 小鼠线粒体基因以 'mt-' 开头（注意小写）
    adata.var['mt'] = adata.var_names.str.startswith('mt-')
    if adata.var['mt'].sum() == 0:
        # 有些数据集中线粒体基因可能是大写 'MT-'
        adata.var['mt'] = adata.var_names.str.upper().str.startswith('MT-')
    sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], percent_top=None, log1p=False, inplace=True)

    # 绘制 QC 指标分布图
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    axes[0].hist(adata.obs['n_genes_by_counts'], bins=50, color='steelblue', edgecolor='white')
    axes[0].set_xlabel('检测到的基因数')
    axes[0].set_ylabel('细胞数')
    axes[0].set_title('基因数分布')
    axes[0].axvline(x=200, color='red', linestyle='--', label='最低阈值=200')
    axes[0].axvline(x=5000, color='red', linestyle='--', label='最高阈值=5000')
    axes[0].legend(fontsize=8)

    axes[1].hist(adata.obs['total_counts'], bins=50, color='coral', edgecolor='white')
    axes[1].set_xlabel('总 UMI 数')
    axes[1].set_ylabel('细胞数')
    axes[1].set_title('UMI 数分布')

    axes[2].hist(adata.obs['pct_counts_mt'], bins=50, color='seagreen', edgecolor='white')
    axes[2].set_xlabel('线粒体基因比例 (%)')
    axes[2].set_ylabel('细胞数')
    axes[2].set_title('线粒体基因比例分布')
    axes[2].axvline(x=10, color='red', linestyle='--', label='阈值=10%')
    axes[2].legend(fontsize=8)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, '01_qc_metrics.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("  [保存] 01_qc_metrics.png")

    # 过滤（参数从 config.yaml 读取）
    sc.pp.filter_cells(adata, min_genes=CFG['qc']['min_genes'])
    sc.pp.filter_cells(adata, max_genes=CFG['qc']['max_genes'])
    adata = adata[adata.obs['pct_counts_mt'] < CFG['qc']['max_pct_mt'], :].copy()
    sc.pp.filter_genes(adata, min_cells=CFG['qc']['min_cells'])

    n_after = adata.n_obs
    print(f"  [过滤] {n_before} → {n_after} 个细胞（去除 {n_before - n_after} 个低质量细胞）")
    print(f"         剩余 {adata.n_vars} 个基因")
    print()
    return adata


# ============================================================
# 步骤 3b：双细胞检测（Doublet Detection）
# ============================================================
def detect_doublets(adata):
    """使用 Scrublet 检测并去除双细胞

    Scrublet 通过模拟人工双细胞，比较真实细胞与模拟双细胞的
    近邻密度分布，为每个细胞计算双细胞得分。
    """
    print("=" * 60)
    print("步骤 3b：双细胞检测（Scrublet）")
    print("=" * 60)

    n_before = adata.n_obs
    doublet_labels = np.full(adata.n_obs, False)
    doublet_scores = np.zeros(adata.n_obs)

    # NOTE: 不同样本的双细胞率不同，按样本分别检测
    for sample_name in adata.obs['sample'].cat.categories:
        mask = adata.obs['sample'] == sample_name
        sample_adata = adata[mask].copy()

        if sample_adata.n_obs < 50:
            print(f"  [跳过] {sample_name}: 细胞数过少 ({sample_adata.n_obs})")
            continue

        try:
            # Scanpy >= 1.10 内置了 scrublet 接口
            sc.pp.scrublet(sample_adata, random_state=42, batch_key='sample')

            if 'predicted_doublet' in sample_adata.obs:
                n_doublets = sample_adata.obs['predicted_doublet'].sum()
                print(f"  {sample_name}: {n_doublets}/{sample_adata.n_obs} 个双细胞 "
                      f"({n_doublets/sample_adata.n_obs*100:.1f}%)")
                doublet_labels[mask] = sample_adata.obs['predicted_doublet'].values.astype(bool)
                if 'doublet_score' in sample_adata.obs:
                    doublet_scores[mask] = sample_adata.obs['doublet_score'].values
        except Exception as e:
            print(f"  [警告] {sample_name} 双细胞检测失败: {e}")

    # 将结果添加到原始 adata
    adata.obs['doublet_score'] = doublet_scores
    adata.obs['doublet'] = doublet_labels

    # 绘制双细胞得分分布图
    if doublet_scores.max() > 0:
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))

        # 直方图
        axes[0].hist(doublet_scores[~doublet_labels], bins=50, alpha=0.7,
                     color='steelblue', label='Singlet', density=True)
        axes[0].hist(doublet_scores[doublet_labels], bins=50, alpha=0.7,
                     color='coral', label='Doublet', density=True)
        axes[0].set_xlabel('双细胞得分')
        axes[0].set_ylabel('密度')
        axes[0].set_title('双细胞得分分布')
        axes[0].legend()

        # 按样本的统计
        sample_names = []
        doublet_counts = []
        for sample_name in adata.obs['sample'].cat.categories:
            mask = adata.obs['sample'] == sample_name
            sample_names.append(sample_name)
            doublet_counts.append(adata.obs.loc[mask, 'doublet'].sum())

        axes[1].bar(sample_names, doublet_counts, color='coral', edgecolor='white')
        axes[1].set_xlabel('样本')
        axes[1].set_ylabel('双细胞数')
        axes[1].set_title('各样本双细胞数')
        axes[1].tick_params(axis='x', rotation=45)

        plt.tight_layout()
        plt.savefig(os.path.join(OUTPUT_DIR, '02_doublet_detection.png'), dpi=150, bbox_inches='tight')
        plt.close()
        print("  [保存] 02_doublet_detection.png")

    # 去除双细胞
    adata = adata[~adata.obs['doublet'].values, :].copy()
    n_after = adata.n_obs
    print(f"  [去除] {n_before} → {n_after} 个细胞（去除 {n_before - n_after} 个双细胞）")
    print()

    return adata


# ============================================================
# 步骤 4-6：标准化、高变基因、PCA（含动态维度选择）
# ============================================================
def normalize_and_reduce(adata):
    """标准化、高变基因选择、PCA降维（带动态PC选择）"""
    print("=" * 60)
    print("步骤 4-6：标准化 → 高变基因 → PCA")
    print("=" * 60)

    # 保存原始计数用于差异表达分析
    adata.layers['counts'] = adata.X.copy()

    # 标准化：每个细胞的总 UMI 数归一化到 10,000，然后取对数
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)
    print("  [完成] 标准化（归一化到 10,000 + log1p）")

    # 高变基因选择
    sc.pp.highly_variable_genes(adata, n_top_genes=2000, batch_key='sample')
    adata.raw = adata  # NOTE: 保存标准化后的全基因数据，用于后续可视化
    adata = adata[:, adata.var['highly_variable']].copy()
    print(f"  [完成] 选择 {adata.n_vars} 个高变基因")

    # 缩放
    sc.pp.scale(adata, max_value=10)

    # PCA（计算 50 个主成分供后续动态选择）
    sc.pp.pca(adata, n_comps=50, svd_solver='arpack')
    print("  [完成] PCA 降维（50个主成分）")

    # 绘制 PCA 方差解释图
    sc.pl.pca_variance_ratio(adata, n_pcs=50, show=False)
    plt.savefig(os.path.join(OUTPUT_DIR, '03_pca_variance.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("  [保存] 03_pca_variance.png")

    # 动态选择 PC 数：使用 kneed 检测方差解释率的拐点
    try:
        from kneed import KneeLocator
        var_ratio = adata.uns['pca']['variance_ratio']
        n_pcs = min(50, len(var_ratio))
        x = np.arange(1, n_pcs + 1)
        # NOTE: 使用 KneeLocator 检测拐点，方向为递减
        kneedle = KneeLocator(x, var_ratio[:n_pcs], S=1.0, curve='convex', direction='decreasing')
        optimal_pcs = kneedle.knee
        if optimal_pcs is None or optimal_pcs < 5:
            optimal_pcs = 20  # 降级为默认值
        print(f"  [选择] kneed 确定最优 PC 数: {optimal_pcs}")
    except Exception as e:
        optimal_pcs = 20  #  kneed 不可用时降级
        print(f"  [降级] 使用默认 PC 数: {optimal_pcs} ({e})")

    # 保存选择的 PC 数到 uns 中，供后续步骤使用
    adata.uns['optimal_pcs'] = optimal_pcs

    print()
    return adata


# ============================================================
# 步骤 7：批次校正（Harmony）
# ============================================================
def batch_correction(adata):
    """使用 Harmony 进行批次校正"""
    print("=" * 60)
    print("步骤 7：批次校正（Harmony）")
    print("=" * 60)
    try:
        import harmonypy
        sc.external.pp.harmony_integrate(
            adata, key='sample', basis='X_pca', adjusted_basis='X_pca_harmony'
        )
        use_rep = 'X_pca_harmony'
        print("  [完成] Harmony 批次校正成功")
    except Exception as e:
        print(f"  [警告] Harmony 不可用 ({e})，跳过批次校正")
        use_rep = 'X_pca'
    print()
    return adata, use_rep


# ============================================================
# 步骤 8-9：聚类 + UMAP
# ============================================================
def cluster_and_visualize(adata, use_rep):
    """Leiden 聚类和 UMAP 可视化"""
    print("=" * 60)
    print("步骤 8-9：聚类 + UMAP 可视化")
    print("=" * 60)

    optimal_pcs = adata.uns.get('optimal_pcs', 20)
    n_pcs = min(optimal_pcs, 30)  # 最高不超过 30
    print(f"  [信息] 使用 {n_pcs} 个 PC 构建邻域图")

    # 构建邻域图
    sc.pp.neighbors(adata, n_pcs=n_pcs, use_rep=use_rep)
    print("  [完成] 邻域图构建")

    # UMAP 降维
    sc.tl.umap(adata)
    print("  [完成] UMAP 降维")

    # Leiden 聚类（resolution 从 config.yaml 读取：论文为 0.4）
    # NOTE: 论文 Methods 明确写 "clusters were assigned at a resolution of 0.4"
    # FIXME: 原代码使用 0.8 导致过度细分，已修正
    sc.tl.leiden(adata, resolution=CFG['clustering']['resolution'], flavor='igraph', n_iterations=2)
    n_clusters = adata.obs['leiden'].nunique()
    print(f"  [完成] Leiden 聚类（resolution=0.4），共 {n_clusters} 个聚类")

    # 绘制 UMAP（按聚类着色）
    sc.pl.umap(adata, color='leiden', legend_loc='on data', title='Leiden Clusters', show=False)
    plt.savefig(os.path.join(OUTPUT_DIR, '04_umap_clusters.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("  [保存] 04_umap_clusters.png")

    # 绘制 UMAP（按样本着色）
    sc.pl.umap(adata, color='condition', title='Sample Conditions', show=False)
    plt.savefig(os.path.join(OUTPUT_DIR, '05_umap_conditions.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("  [保存] 05_umap_conditions.png")
    print()
    return adata


# ============================================================
# 步骤 10：差异表达分析（DEA）
# ============================================================
def differential_expression(adata):
    """差异表达分析：寻找每个聚类的标志基因

    对应标准 Seurat 流程中的 FindAllMarkers() 步骤。
    这是验证文献标志基因和发现新 marker 的关键步骤。
    """
    print("=" * 60)
    print("步骤 10：差异表达分析")
    print("=" * 60)

    # 差异表达分析（参数从 config.yaml 读取）
    # NOTE: 论文使用 Wilcoxon 秩和检验，已从 t-test 修正为 wilcoxon
    sc.tl.rank_genes_groups(
        adata, groupby='leiden', method=CFG['de']['method'],
        n_genes=CFG['de']['n_genes'], use_raw=CFG['de']['use_raw'],
        pts=True, key='rank_genes_groups'
    )
    print(f"  [完成] 差异表达分析（{CFG['de']['method']}，每个聚类 top {CFG['de']['n_genes']} 基因，含表达比例）")

    # 保存差异表达结果到 CSV（全量）
    de_results = pd.DataFrame()
    for cluster in adata.obs['leiden'].cat.categories:
        cluster_de = sc.get.rank_genes_groups_df(adata, group=cluster, key='rank_genes_groups')
        cluster_de['cluster'] = cluster
        de_results = pd.concat([de_results, cluster_de], ignore_index=True)

    de_results.to_csv(os.path.join(OUTPUT_DIR, 'de_genes.csv'), index=False)
    print("  [保存] de_genes.csv（差异表达基因表，全量）")

    # 保存显著性过滤后的 DE 结果（pvals_adj < 0.05）
    # NOTE: 论文使用 Holm 校正 + p < 0.01（FWER），此处使用 BH 校正 + p_adj < 0.05（FDR）
    # FIXME: 原代码固定取 top 50 基因，未考虑显著性，现将噪声基因排除
    de_significant = de_results[de_results['pvals_adj'] < 0.05].copy()
    de_significant.to_csv(os.path.join(OUTPUT_DIR, 'de_genes_significant.csv'), index=False)
    print(f"  [保存] de_genes_significant.csv（显著性过滤后: {len(de_significant)} 条记录）")
    # 记录每个 cluster 的显著基因数，方便判断聚类停止准则
    sig_counts = de_significant.groupby('cluster').size()
    for cluster, count in sig_counts.items():
        print(f"         Cluster {cluster}: {count} 个显著基因")

    # 绘制差异基因热图（每个聚类 top 5）
    sc.pl.rank_genes_groups_heatmap(
        adata, n_genes=5, groupby='leiden', key='rank_genes_groups',
        show=False, vmin=-3, vmax=3, cmap='RdBu_r',
    )
    plt.savefig(os.path.join(OUTPUT_DIR, '06_heatmap_de_genes.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("  [保存] 06_heatmap_de_genes.png")

    # 绘制差异基因点图
    sc.pl.rank_genes_groups_dotplot(
        adata, n_genes=5, groupby='leiden', key='rank_genes_groups',
        show=False, standard_scale='var',
    )
    plt.savefig(os.path.join(OUTPUT_DIR, '07_dotplot_de_genes.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("  [保存] 07_dotplot_de_genes.png")

    # 绘制差异基因小提琴图
    sc.pl.rank_genes_groups_violin(
        adata, n_genes=5, groupby='leiden', key='rank_genes_groups',
        show=False,
    )
    plt.savefig(os.path.join(OUTPUT_DIR, '08_violin_de_genes.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("  [保存] 08_violin_de_genes.png")

    # 验证注释结果：检查 ECM 标志基因在间充质细胞中的表达
    # NOTE: 这是对细胞类型注释结果的旁证，并非配体-受体分析
    print("\n  [文献验证] 检查间充质细胞 ECM 标志基因表达...")
    adata_raw = adata.raw.to_adata()

    for gene in ECM_MARKERS:
        if gene in adata_raw.var_names:
            sc.pl.umap(adata_raw, color=gene, title=f'ECM marker: {gene}',
                       show=False, color_map='Reds', frameon=False)
            plt.savefig(os.path.join(OUTPUT_DIR, f'ecm_marker_{gene}.png'),
                        dpi=150, bbox_inches='tight')
            plt.close()

    # 统计 ECM 标志基因在不同细胞类型中的平均表达水平
    ecm_found = [g for g in ECM_MARKERS if g in adata_raw.var_names]
    if ecm_found:
        ecm_expr = sc.get.aggregate(adata_raw, by='leiden', func='mean')
        ecm_expr = ecm_expr[:, ecm_found]
        ecm_df = ecm_expr.to_df().T
        ecm_df.columns = [f'Cluster_{c}' for c in ecm_df.columns]
        ecm_df.to_csv(os.path.join(OUTPUT_DIR, 'ecm_marker_expression.csv'))
        print(f"  [保存] ecm_marker_expression.csv（ECM标志基因在各聚类的平均表达）")

    print()
    return adata


# ============================================================
# 步骤 11：细胞类型注释（核心步骤）
# ============================================================
def annotate_cells(adata):
    """基于文献标志基因进行细胞类型注释"""
    print("=" * 60)
    print("步骤 11：细胞类型注释")
    print("=" * 60)

    # 使用 raw 数据（包含全部基因）来检查标志基因
    adata_raw = adata.raw.to_adata()

    # 检查哪些标志基因在数据中存在
    all_markers = []
    available_markers = {}
    for cell_type, genes in MARKER_GENES.items():
        found = [g for g in genes if g in adata_raw.var_names]
        if found:
            available_markers[cell_type] = found
            all_markers.extend(found)
            print(f"  {cell_type}: {found}")
        else:
            print(f"  {cell_type}: [未找到标志基因]")

    # 绘制标志基因点图（dotplot）—— 最关键的注释依据图
    if all_markers:
        sc.pl.dotplot(adata_raw, var_names=available_markers, groupby='leiden',
                      standard_scale='var', show=False)
        plt.savefig(os.path.join(OUTPUT_DIR, '09_dotplot_markers.png'), dpi=150, bbox_inches='tight')
        plt.close()
        print("\n  [保存] 09_dotplot_markers.png")

    # 绘制标志基因在 UMAP 上的表达
    markers_to_plot = []
    for genes in available_markers.values():
        markers_to_plot.extend(genes[:2])  # 每种细胞类型取前2个基因
    markers_to_plot = list(dict.fromkeys(markers_to_plot))  # 去重保序

    if markers_to_plot:
        n_genes = len(markers_to_plot)
        n_cols = 4
        n_rows = (n_genes + n_cols - 1) // n_cols
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(n_cols * 4, n_rows * 3.5))
        axes = axes.flatten() if n_rows > 1 else (axes if n_cols > 1 else [axes])

        for idx, gene in enumerate(markers_to_plot):
            if idx < len(axes):
                sc.pl.umap(adata_raw, color=gene, ax=axes[idx], show=False,
                           title=gene, frameon=False, color_map='Reds')
        # 隐藏多余的子图
        for idx in range(len(markers_to_plot), len(axes)):
            axes[idx].set_visible(False)
        plt.tight_layout()
        plt.savefig(os.path.join(OUTPUT_DIR, '10_umap_markers.png'), dpi=150, bbox_inches='tight')
        plt.close()
        print("  [保存] 10_umap_markers.png")

    # 基于标志基因表达进行自动注释
    # NOTE: 计算每个聚类中各标志基因的平均表达，取最高者作为注释
    print("\n  [注释] 基于标志基因平均表达进行聚类注释...")
    cluster_annotations = {}

    for cluster in adata.obs['leiden'].cat.categories:
        cluster_mask = adata_raw.obs['leiden'] == cluster
        best_score = -1
        best_type = 'Unknown'

        for cell_type, genes in available_markers.items():
            # 计算该聚类中标志基因的平均表达
            expr_values = []
            for gene in genes:
                if gene in adata_raw.var_names:
                    gene_expr = adata_raw[cluster_mask, gene].X
                    if hasattr(gene_expr, 'toarray'):
                        gene_expr = gene_expr.toarray()
                    mean_expr = np.mean(gene_expr)
                    expr_values.append(mean_expr)

            if expr_values:
                score = np.mean(expr_values)
                if score > best_score:
                    best_score = score
                    best_type = cell_type

        cluster_annotations[cluster] = best_type
        print(f"    Cluster {cluster} → {best_type} (score: {best_score:.3f})")

    # 应用注释
    adata.obs['cell_type'] = adata.obs['leiden'].map(cluster_annotations)
    adata_raw.obs['cell_type'] = adata.obs['cell_type']

    # 绘制注释后的 UMAP
    sc.pl.umap(adata, color='cell_type', title='Cell Type Annotation',
               legend_loc='right margin', show=False)
    plt.savefig(os.path.join(OUTPUT_DIR, '11_umap_cell_types.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("\n  [保存] 11_umap_cell_types.png")

    # 绘制注释后的小提琴图
    key_markers = []
    for cell_type, genes in available_markers.items():
        if genes:
            key_markers.append(genes[0])
    key_markers = list(dict.fromkeys(key_markers))

    if key_markers:
        sc.pl.stacked_violin(adata_raw, var_names=key_markers, groupby='cell_type',
                             show=False, swap_axes=True)
        plt.savefig(os.path.join(OUTPUT_DIR, '12_violin_markers.png'), dpi=150, bbox_inches='tight')
        plt.close()
        print("  [保存] 12_violin_markers.png")

    # 统计各细胞类型比例
    print("\n  [统计] 各细胞类型比例:")
    cell_counts = adata.obs['cell_type'].value_counts()
    total = len(adata)
    for ct, count in cell_counts.items():
        pct = count / total * 100
        print(f"    {ct}: {count} 个细胞 ({pct:.1f}%)")

    # 绘制细胞比例饼图
    fig, ax = plt.subplots(figsize=(8, 6))
    colors = plt.cm.Set3(np.linspace(0, 1, len(cell_counts)))
    wedges, texts, autotexts = ax.pie(cell_counts.values, labels=cell_counts.index,
                                       autopct='%1.1f%%', colors=colors, pctdistance=0.85)
    for text in autotexts:
        text.set_fontsize(9)
    ax.set_title('Cell Type Proportions')
    plt.savefig(os.path.join(OUTPUT_DIR, '13_cell_proportions.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("  [保存] 13_cell_proportions.png")
    print()
    return adata


# ============================================================
# 步骤 12：保存结果
# ============================================================
def save_results(adata):
    """保存分析结果"""
    print("=" * 60)
    print("步骤 12：保存结果")
    print("=" * 60)

    # 保存 AnnData 对象
    adata.write(os.path.join(OUTPUT_DIR, 'adata_annotated.h5ad'))
    print("  [保存] adata_annotated.h5ad（完整分析结果）")

    # 导出细胞注释表
    meta = adata.obs[['sample', 'condition', 'leiden', 'cell_type',
                       'n_genes_by_counts', 'total_counts',
                       'doublet_score', 'doublet']].copy()
    meta.to_csv(os.path.join(OUTPUT_DIR, 'cell_annotations.csv'))
    print("  [保存] cell_annotations.csv（细胞注释表）")
    print()


# ============================================================
# 步骤 13：配体-受体互作分析（LIANA+）
# ============================================================
def ligand_receptor_analysis(adata):
    """使用 LIANA+ 进行配体-受体互作分析

    论文核心发现：间充质细胞（Mesenchymal cells）是神经营养配体的最大来源。
    本函数通过 LIANA+ 的 rank_aggregate 方法，整合多种配体-受体数据库，
    输出细胞类型间的配体-受体互作排名。

    NOTE: 论文原工具 Cellcellinteractnet（Python 2.7）未公开，
    LIANA+ 是 2024 年 Nature Cell Biology 发表的主流替代方案。

    当前分析范围：
    - 仅针对 scRNA-seq 数据内部细胞类型间的互作
    - 重点提取 Mesenchymal → Schwann / Endothelial 的互作
    - 验证 ANGPT1、CCL11、VEGFC 等论文核心配体是否在 top 排名中
    - 如果需要引入外部神经元数据（DRG/SCG），需下载 GSE146958 并使用 liana external_resource

    参考文献：
    Dimitrov et al. (2024) LIANA+: Nature Cell Biology
    """
    print("=" * 60)
    print("步骤 13：配体-受体互作分析（LIANA+）")
    print("=" * 60)

    # 检查是否已安装 liana
    try:
        import liana
    except ImportError:
        print("  [警告] liana 未安装，跳过配体-受体分析。")
        print("          安装命令: pip install liana-py")
        print()
        return adata

    # 确保细胞类型注释存在
    if 'cell_type' not in adata.obs:
        print("  [错误] cell_type 列不存在，请先运行 annotate_cells()")
        return adata

    # 使用 log1p 标准化的全基因数据进行互作分析
    # NOTE: LIANA+ 需要原始 counts 或 log-normalized 数据
    if adata.raw is not None:
        adata_use = adata.raw.to_adata()
    else:
        adata_use = adata

    # 同步细胞类型注释
    adata_use.obs['cell_type'] = adata.obs['cell_type']

    # 获取配置参数
    liana_cfg = CFG.get('liana', {})
    resource_name = liana_cfg.get('resource_name', 'mouseconsensus')
    expr_prop = liana_cfg.get('expr_prop', 0.1)
    top_n = liana_cfg.get('top_n', 20)
    target_ligands = liana_cfg.get('target_ligands', [])

    print(f"  [配置] 数据库: {resource_name}, 表达比例阈值: {expr_prop}, top_n: {top_n}")
    print(f"  [验证] 目标配体: {target_ligands}")

    # ---------------------------------
    # 1) 运行 LIANA+ rank_aggregate
    # ---------------------------------
    print("\n  [运行] LIANA+ rank_aggregate（多方法共识排名）...")
    try:
        import liana as li
        li.mt.rank_aggregate(
            adata_use,
            groupby='cell_type',
            resource_name=resource_name,
            expr_prop=expr_prop,
            return_all_lrs=False,
            use_raw=False,
            verbose=True,
        )

        # 提取结果
        if 'liana_res' in adata_use.uns:
            result = adata_use.uns['liana_res']
            print(f"  [结果] 共检测到 {len(result)} 个配体-受体对（全部细胞类型间）")
        else:
            print("  [警告] liana_res 未生成，跳过后续分析")
            return adata

    except Exception as e:
        print(f"  [错误] LIANA+ 分析失败: {e}")
        logger.error("LIANA+ 分析异常", exc_info=True)
        return adata

    # ---------------------------------
    # 2) 提取重点互作：Mesenchymal → 其他细胞
    # ---------------------------------
    print("\n  [重点] 提取 Mesenchymal 作为配体源的互作...")

    # 获取数据中实际存在的细胞类型
    available_types = adata_use.obs['cell_type'].unique()
    print(f"  [信息] 可用细胞类型: {list(available_types)}")

    if 'Mesenchymal cells' not in available_types:
        print("  [警告] 数据中未找到 'Mesenchymal cells'，跳过重点互作分析")
    else:
        # 提取 Mesenchymal → 所有靶细胞的互作
        mes_sources = result[result['source'] == 'Mesenchymal cells'].copy()
        print(f"    → 间充质发出互作: {len(mes_sources)} 个配体-受体对")

        if not mes_sources.empty:
            # 按 magnitude_rank 排序
            mes_sources = mes_sources.sort_values('magnitude_rank')

            # 保存 CSV
            mes_sources.to_csv(os.path.join(OUTPUT_DIR, 'liana_mesenchymal_source.csv'), index=False)
            print(f"    [保存] liana_mesenchymal_source.csv（Mesenchymal 源互作全表）")

            # 打印 top 10
            print("\n    Top 10 Mesenchymal 来源的配体-受体对:")
            top_cols = ['ligand_complex', 'receptor_complex', 'source', 'target',
                        'magnitude_rank', 'specificity_rank']
            print(mes_sources.head(10)[top_cols].to_string(index=False))

        # 提取 Mesenchymal → Schwann 的互作
        if 'Schwann cells' in available_types:
            mes2schwann = mes_sources[mes_sources['target'] == 'Schwann cells']
            if not mes2schwann.empty:
                mes2schwann.to_csv(os.path.join(OUTPUT_DIR, 'liana_mes2schwann.csv'), index=False)
                print(f"\n    → Mesenchymal → Schwann: {len(mes2schwann)} 个互作")
                print(mes2schwann.head(10)[top_cols].to_string(index=False))

        # 提取 Mesenchymal → Endothelial 的互作
        if 'Endothelial cells' in available_types:
            mes2endo = mes_sources[mes_sources['target'] == 'Endothelial cells']
            if not mes2endo.empty:
                mes2endo.to_csv(os.path.join(OUTPUT_DIR, 'liana_mes2endothelial.csv'), index=False)
                print(f"\n    → Mesenchymal → Endothelial: {len(mes2endo)} 个互作")

    # ---------------------------------
    # 3) 验证论文核心配体
    # ---------------------------------
    if target_ligands:
        print("\n  [验证] 论文核心配体在互作结果中的排名:")

        # 在所有 Mesenchymal 来源的互作中查找目标配体
        if 'Mesenchymal cells' in available_types:
            for ligand in target_ligands:
                found = mes_sources[mes_sources['ligand_complex'].str.contains(
                    ligand, case=False, na=False
                )]
                if not found.empty:
                    print(f"    ✅ {ligand}: 找到 {len(found)} 个互作")
                    for _, row in found.iterrows():
                        print(f"       → {row['target']} "
                              f"(受体: {row['receptor_complex']}, "
                              f"magnitude_rank: {row['magnitude_rank']})")
                else:
                    print(f"    ❌ {ligand}: 未在 Mesenchymal 互作中找到")
        else:
            # 跨所有细胞类型搜索
            for ligand in target_ligands:
                found = result[result['ligand_complex'].str.contains(
                    ligand, case=False, na=False
                )]
                if not found.empty:
                    print(f"    ✅ {ligand}: 找到 {len(found)} 个互作")
                    for _, row in found.head(3).iterrows():
                        print(f"       {row['source']} → {row['target']} "
                              f"(受体: {row['receptor_complex']}, "
                              f"rank: {row['magnitude_rank']})")
                else:
                    print(f"    ❌ {ligand}: 未在任何互作中找到")

    # ---------------------------------
    # 4) 可视化
    # ---------------------------------
    print("\n  [可视化] 生成互作点图...")
    try:
        import liana as li

        # 全局互作热图
        li.pl.dotplot(
            adata_use,
            source_labels=['Mesenchymal cells'] if 'Mesenchymal cells' in available_types else None,
            target_labels=['Schwann cells', 'Endothelial cells']
                           if all(t in available_types for t in ['Schwann cells', 'Endothelial cells'])
                           else None,
            top_n=top_n,
            figure_size=(12, 8),
            show=False,
        )
        plt.savefig(os.path.join(OUTPUT_DIR, '14_liana_dotplot.png'), dpi=150, bbox_inches='tight')
        plt.close()
        print("    [保存] 14_liana_dotplot.png")

        # 全部细胞类型间互作计数热图
        if not result.empty:
            # 构建互作计数矩阵
            interaction_matrix = result.pivot_table(
                index='source', columns='target',
                values='magnitude_rank', aggfunc='count'
            ).fillna(0)

            fig, ax = plt.subplots(figsize=(10, 8))
            sns.heatmap(interaction_matrix, annot=True, fmt='.0f', cmap='Reds',
                        ax=ax, cbar_kws={'label': '配体-受体对数量'})
            ax.set_title('Cell-Cell Interaction Count (LIANA+)')
            ax.set_xlabel('Target')
            ax.set_ylabel('Source')
            plt.xticks(rotation=45, ha='right')
            plt.yticks(rotation=0)
            plt.tight_layout()
            plt.savefig(os.path.join(OUTPUT_DIR, '15_liana_interaction_heatmap.png'),
                        dpi=150, bbox_inches='tight')
            plt.close()
            print("    [保存] 15_liana_interaction_heatmap.png")

    except Exception as e:
        print(f"    [警告] 可视化失败: {e}")

    # 将结果保存到原始 adata 中
    if 'liana_res' in adata_use.uns:
        adata.uns['liana_res'] = adata_use.uns['liana_res']

    print("\n  [完成] 配体-受体互作分析")
    print()
    return adata


# ============================================================
# 主函数
# ============================================================
def main():
    print("\n" + "=" * 60)
    print("  单细胞RNA测序数据分析")
    print("  文献: eNeuro, 2020 | 数据: GSE147285")
    print("=" * 60 + "\n")

    # 1. 下载
    download_data()

    # 2. 读取合并
    adata = load_and_merge()

    # 3. 质控
    adata = quality_control(adata)

    # 3b. 双细胞检测（新增）
    adata = detect_doublets(adata)

    # 4-6. 标准化 + PCA（含动态PC选择）
    adata = normalize_and_reduce(adata)

    # 7. 批次校正
    adata, use_rep = batch_correction(adata)

    # 8-9. 聚类 + UMAP
    adata = cluster_and_visualize(adata, use_rep)

    # 10. 差异表达分析（新增）
    adata = differential_expression(adata)

    # 11. 注释
    adata = annotate_cells(adata)

    # 12. 配体-受体互作分析（LIANA+）
    # NOTE: 这是论文核心分析，验证 Mesenchymal 作为配体源的主要发现
    # FIXME: 原分析仅做到细胞注释，未涉及配体-受体互作预测
    adata = ligand_receptor_analysis(adata)

    # 13. 保存
    save_results(adata)

    print("=" * 60)
    print("  分析完成！所有结果保存在 results/ 目录中")
    print("=" * 60)
    print("\n结果文件列表:")
    for f in sorted(os.listdir(OUTPUT_DIR)):
        size = os.path.getsize(os.path.join(OUTPUT_DIR, f))
        print(f"  {f} ({size / 1024:.0f} KB)")


if __name__ == '__main__':
    main()
