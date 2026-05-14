# -*- coding: utf-8 -*-
"""
单细胞RNA测序数据分析脚本
文献: Peripheral Nerve Single-Cell Analysis Identifies Mesenchymal Ligands (eNeuro, 2020)
数据: GEO GSE147285 (Drop-seq, 小鼠坐骨神经)

分析流程: 下载数据 → 质控 → 标准化 → 降维 → 聚类 → 细胞类型注释
"""

import os
import gzip
import requests
import warnings
import numpy as np
import pandas as pd
import scanpy as sc
import matplotlib
matplotlib.use('Agg')  # NOTE: 非交互式后端，用于服务器/脚本环境
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')

# ============================================================
# 配置
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

    # 过滤
    sc.pp.filter_cells(adata, min_genes=200)
    sc.pp.filter_cells(adata, max_genes=5000)
    adata = adata[adata.obs['pct_counts_mt'] < 10, :].copy()
    sc.pp.filter_genes(adata, min_cells=3)

    n_after = adata.n_obs
    print(f"  [过滤] {n_before} → {n_after} 个细胞（去除 {n_before - n_after} 个低质量细胞）")
    print(f"         剩余 {adata.n_vars} 个基因")
    print()
    return adata


# ============================================================
# 步骤 4-6：标准化、高变基因、PCA
# ============================================================
def normalize_and_reduce(adata):
    """标准化、高变基因选择、PCA降维"""
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

    # PCA
    sc.pp.pca(adata, n_comps=30)
    print("  [完成] PCA 降维（30个主成分）")

    # 绘制 PCA 方差解释图
    sc.pl.pca_variance_ratio(adata, n_pcs=30, show=False)
    plt.savefig(os.path.join(OUTPUT_DIR, '02_pca_variance.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("  [保存] 02_pca_variance.png")
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
        sc.external.pp.harmony_integrate(adata, key='sample', basis='X_pca', adjusted_basis='X_pca_harmony')
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

    # 构建邻域图
    sc.pp.neighbors(adata, n_pcs=20, use_rep=use_rep)
    print("  [完成] 邻域图构建")

    # UMAP 降维
    sc.tl.umap(adata)
    print("  [完成] UMAP 降维")

    # Leiden 聚类
    sc.tl.leiden(adata, resolution=0.8, flavor='igraph', n_iterations=2)
    print(f"  [完成] Leiden 聚类，共 {adata.obs['leiden'].nunique()} 个聚类")

    # 绘制 UMAP（按聚类着色）
    sc.pl.umap(adata, color='leiden', legend_loc='on data', title='Leiden Clusters', show=False)
    plt.savefig(os.path.join(OUTPUT_DIR, '03_umap_clusters.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("  [保存] 03_umap_clusters.png")

    # 绘制 UMAP（按样本着色）
    sc.pl.umap(adata, color='condition', title='Sample Conditions', show=False)
    plt.savefig(os.path.join(OUTPUT_DIR, '04_umap_conditions.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("  [保存] 04_umap_conditions.png")
    print()
    return adata


# ============================================================
# 步骤 10：细胞类型注释（核心步骤）
# ============================================================
def annotate_cells(adata):
    """基于文献标志基因进行细胞类型注释"""
    print("=" * 60)
    print("步骤 10：细胞类型注释")
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
        plt.savefig(os.path.join(OUTPUT_DIR, '05_dotplot_markers.png'), dpi=150, bbox_inches='tight')
        plt.close()
        print("\n  [保存] 05_dotplot_markers.png")

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
        plt.savefig(os.path.join(OUTPUT_DIR, '06_umap_markers.png'), dpi=150, bbox_inches='tight')
        plt.close()
        print("  [保存] 06_umap_markers.png")

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
    plt.savefig(os.path.join(OUTPUT_DIR, '07_umap_cell_types.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("\n  [保存] 07_umap_cell_types.png")

    # 绘制注释后的小提琴图
    key_markers = []
    for cell_type, genes in available_markers.items():
        if genes:
            key_markers.append(genes[0])
    key_markers = list(dict.fromkeys(key_markers))

    if key_markers:
        sc.pl.stacked_violin(adata_raw, var_names=key_markers, groupby='cell_type',
                             show=False, swap_axes=True)
        plt.savefig(os.path.join(OUTPUT_DIR, '08_violin_markers.png'), dpi=150, bbox_inches='tight')
        plt.close()
        print("  [保存] 08_violin_markers.png")

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
    plt.savefig(os.path.join(OUTPUT_DIR, '09_cell_proportions.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("  [保存] 09_cell_proportions.png")
    print()
    return adata


# ============================================================
# 步骤 11：保存结果
# ============================================================
def save_results(adata):
    """保存分析结果"""
    print("=" * 60)
    print("步骤 11：保存结果")
    print("=" * 60)

    # 保存 AnnData 对象
    adata.write(os.path.join(OUTPUT_DIR, 'adata_annotated.h5ad'))
    print("  [保存] adata_annotated.h5ad（完整分析结果）")

    # 导出细胞注释表
    meta = adata.obs[['sample', 'condition', 'leiden', 'cell_type',
                       'n_genes_by_counts', 'total_counts']].copy()
    meta.to_csv(os.path.join(OUTPUT_DIR, 'cell_annotations.csv'))
    print("  [保存] cell_annotations.csv（细胞注释表）")
    print()


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

    # 4-6. 标准化 + PCA
    adata = normalize_and_reduce(adata)

    # 7. 批次校正
    adata, use_rep = batch_correction(adata)

    # 8-9. 聚类 + UMAP
    adata = cluster_and_visualize(adata, use_rep)

    # 10. 注释
    adata = annotate_cells(adata)

    # 11. 保存
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
