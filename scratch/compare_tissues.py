import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

excel_path = r"D:\OneDrive\Desktop\组\db\数据集_按物种组织分类.xlsx"
csv_path = r"d:\OneDrive\Desktop\组\db\cellxgene\cellxgene_filtered\filtered_datasets.csv"

excel_all = pd.read_excel(excel_path, sheet_name='全部')
csv_all = pd.read_csv(csv_path)

# 只比对 CellxGene 的公共数据
merged = pd.merge(
    excel_all[['collection_id', '组织系统大类', '主组织', 'Publication_Title']],
    csv_all[['collection_id', 'tissue', 'matched_cell_types']],
    on='collection_id',
    how='inner'
)

# 打印 组织系统大类 与 我们的 tissue 的映射关系
print("=== 组织系统大类 vs. CSV tissue 映射统计 ===")
mapping = merged.groupby(['组织系统大类', 'tissue']).size().reset_index(name='count')
print(mapping.to_string(index=False))

print("\n=== 各大类的匹配细胞类型示例 ===")
for category in merged['组织系统大类'].unique():
    sub = merged[merged['组织系统大类'] == category]
    print(f"\n【{category}】 (共 {len(sub)} 个数据集)")
    print("  同学代表性的'主组织':", list(sub['主组织'].unique()[:5]))
    print("  我们匹配到的细胞类型 (前10种去重):")
    all_matched_types = set()
    for types in sub['matched_cell_types'].dropna():
        all_matched_types.update([t.strip() for t in types.split('|')])
    print("    ", list(all_matched_types)[:10])
