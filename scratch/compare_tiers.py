import pandas as pd
import numpy as np
import sys

sys.stdout.reconfigure(encoding='utf-8')

excel_path = r"D:\OneDrive\Desktop\组\db\数据集_按物种组织分类.xlsx"
csv_path = r"d:\OneDrive\Desktop\组\db\cellxgene\cellxgene_filtered\filtered_datasets.csv"

excel_all = pd.read_excel(excel_path, sheet_name='全部')
csv_all = pd.read_csv(csv_path)

# 仅保留共同拥有的 CellxGene 记录进行对比
excel_cellxgene = excel_all[excel_all['collection_id'].isin(csv_all['collection_id'])].copy()

# 把 csv 中的 tier 信息整理成类似 "L1", "L2" 的格式
def get_csv_tiers(row):
    tiers = []
    if pd.notna(row['_tier_1']) and str(row['_tier_1']).strip() != "":
        tiers.append("L1")
    if pd.notna(row['_tier_2']) and str(row['_tier_2']).strip() != "":
        tiers.append("L2")
    if pd.notna(row['_tier_3']) and str(row['_tier_3']).strip() != "":
        tiers.append("L3")
    if pd.notna(row['_tier_4']) and str(row['_tier_4']).strip() != "":
        tiers.append("L4")
    return ";".join(tiers) if tiers else "None"

csv_all['csv_tiers'] = csv_all.apply(get_csv_tiers, axis=1)

# 将两边的数据按 collection_id 合并
merged = pd.merge(
    excel_cellxgene[['collection_id', '细胞分层', 'Publication_Title', '分层依据(具体细胞)']],
    csv_all[['collection_id', 'csv_tiers', 'matched_cell_types']],
    on='collection_id',
    how='inner'
)

# 比较差异
merged['is_match'] = merged['细胞分层'].str.replace(';', '') == merged['csv_tiers'].str.replace(';', '')
# 考虑到顺序可能不同，我们排序一下
def norm_tier(val):
    if pd.isna(val):
        return ""
    parts = sorted([p.strip() for p in str(val).split(';')])
    return ";".join(parts)

merged['excel_tiers_norm'] = merged['细胞分层'].apply(norm_tier)
merged['csv_tiers_norm'] = merged['csv_tiers'].apply(norm_tier)
merged['is_match_strict'] = merged['excel_tiers_norm'] == merged['csv_tiers_norm']

mismatch = merged[~merged['is_match_strict']]
print(f"CellxGene 共同数据集数量: {len(merged)}")
print(f"严格一致的数量: {len(merged[merged['is_match_strict']])}")
print(f"不一致的数量: {len(mismatch)}")

if len(mismatch) > 0:
    print("\n--- 不一致的记录详情 ---")
    for idx, row in mismatch.iterrows():
        print(f"Title: {row['Publication_Title']}")
        print(f"  同学 Excel 的分层: {row['细胞分层']} (依据: {row['分层依据(具体细胞)']})")
        print(f"  我们 CSV 的分层  : {row['csv_tiers']} (匹配到: {row['matched_cell_types']})")
        print("-" * 50)
else:
    print("\n恭喜！双方的 Tier 分类在 CellxGene 共同数据集中完全一致！")
