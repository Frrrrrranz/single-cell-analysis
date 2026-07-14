import pandas as pd
import numpy as np
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 读取两个数据集
excel_path = r"D:\OneDrive\Desktop\组\db\数据集_按物种组织分类.xlsx"
csv_path = r"d:\OneDrive\Desktop\组\db\cellxgene\cellxgene_filtered\filtered_datasets.csv"

excel_all = pd.read_excel(excel_path, sheet_name='全部')
csv_all = pd.read_csv(csv_path)

print("=== 基础信息对比 ===")
print(f"同学的 Excel 中 '全部' 页数据集记录数: {len(excel_all)}")
print(f"我们的 CSV 中筛选出的数据集记录数: {len(csv_all)}")

# 1. 检查同学 Excel 中的数据源类型
print("\n=== 同学 Excel 数据来源 (collection链接域名分析) ===")
def get_source_domain(url):
    if pd.isna(url):
        return "Unknown"
    url = str(url).strip()
    if "cellxgene" in url:
        return "CellxGene"
    elif "ncbi.nlm.nih.gov" in url:
        return "GEO"
    elif "milbrandtlab" in url:
        return "Glia Portal"
    elif "omicsdi.org" in url:
        return "OmicsDI"
    else:
        return url.split('/')[2] if '//' in url else url

excel_all['source_type'] = excel_all['collection链接'].apply(get_source_domain)
print(excel_all['source_type'].value_counts())

# 2. 检查 Collection ID / Dataset ID 匹配情况
# 提取双方有效的 collection_id
excel_cellxgene = excel_all[excel_all['source_type'] == 'CellxGene'].copy()
excel_cids = set(excel_cellxgene['collection_id'].dropna().unique())
csv_cids = set(csv_all['collection_id'].dropna().unique())

print(f"\n同学的 CellxGene Collection 数量: {len(excel_cids)}")
print(f"我们的 CellxGene Collection 数量: {len(csv_cids)}")

common_cids = excel_cids.intersection(csv_cids)
only_excel_cids = excel_cids - csv_cids
only_csv_cids = csv_cids - excel_cids

print(f"共同的 Collection 数量: {len(common_cids)}")
print(f"仅在同学 Excel 中出现的 Collection 数量: {len(only_excel_cids)}")
print(f"仅在我们 CSV 中出现的 Collection 数量: {len(only_csv_cids)}")

# 3. 详细列出仅在一方出现的 Collection
print("\n--- 仅在同学 Excel 中出现的 CellxGene 记录 (Collection Name) ---")
for cid in only_excel_cids:
    row = excel_cellxgene[excel_cellxgene['collection_id'] == cid].iloc[0]
    print(f"- Title: {row['Publication_Title']} | ID: {cid}")

print("\n--- 仅在我们 CSV 中出现的 Collection (Collection Name) ---")
for cid in only_csv_cids:
    row = csv_all[csv_all['collection_id'] == cid].iloc[0]
    print(f"- Title: {row['collection_name']} | ID: {cid}")

# 4. 统计同学 Excel 中非 CellxGene 的数据集
excel_non_cellxgene = excel_all[excel_all['source_type'] != 'CellxGene']
print(f"\n同学 Excel 中非 CellxGene 的数据集数量: {len(excel_non_cellxgene)}")
for idx, row in excel_non_cellxgene.iterrows():
    print(f"- 物种: {row['物种(中文)']} | 大类: {row['组织系统大类']} | 主组织: {row['主组织']} | Title: {row['Publication_Title']} | 链接: {row['collection链接']}")
