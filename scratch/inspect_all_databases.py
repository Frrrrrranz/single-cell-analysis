import pandas as pd
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

db_dir = r"D:\OneDrive\Desktop\组\db"

print("==================== 开始统计当前数据库信息 ====================\n")

# 1. 主数据库 pns-scrna.xlsx
pns_path = os.path.join(db_dir, "pns-scrna.xlsx")
if os.path.exists(pns_path):
    print("--- 1. 主数据库 (pns-scrna.xlsx) ---")
    try:
        xls = pd.ExcelFile(pns_path)
        print(f"包含的表 (Sheets): {xls.sheet_names}")
        for sheet in xls.sheet_names:
            df = pd.read_excel(xls, sheet)
            print(f"  - 表名: {sheet:<15} | 记录数 (行): {df.shape[0]:<5} | 字段数 (列): {df.shape[1]}")
    except Exception as e:
        print(f"  读取失败: {e}")
    print()

# 2. 导师检索_四层_研究级_collection去重.xlsx
mentor_path = os.path.join(db_dir, "导师检索_四层_研究级_collection去重.xlsx")
if os.path.exists(mentor_path):
    print("--- 2. 导师检索库 (导师检索_四层_研究级_collection去重.xlsx) ---")
    try:
        xls = pd.ExcelFile(mentor_path)
        print(f"包含的表 (Sheets): {xls.sheet_names}")
        for sheet in xls.sheet_names:
            df = pd.read_excel(xls, sheet)
            print(f"  - 表名: {sheet:<15} | 记录数 (行): {df.shape[0]:<5} | 字段数 (列): {df.shape[1]}")
    except Exception as e:
        print(f"  读取失败: {e}")
    print()

# 3. 数据集_按物种组织分类.xlsx
species_path = os.path.join(db_dir, "数据集_按物种组织分类.xlsx")
if os.path.exists(species_path):
    print("--- 3. 物种组织分类数据库 (数据集_按物种组织分类.xlsx) ---")
    try:
        xls = pd.ExcelFile(species_path)
        print(f"包含的表 (Sheets): {xls.sheet_names}")
        for sheet in xls.sheet_names:
            df = pd.read_excel(xls, sheet)
            print(f"  - 表名: {sheet:<15} | 记录数 (行): {df.shape[0]:<5} | 字段数 (列): {df.shape[1]}")
    except Exception as e:
        print(f"  读取失败: {e}")
    print()

# 4. CellxGene 筛选后的数据集 (cellxgene_filtered)
filtered_csv = os.path.join(db_dir, "cellxgene", "cellxgene_filtered", "filtered_datasets.csv")
if os.path.exists(filtered_csv):
    print("--- 4. CellxGene 过滤后数据集 (cellxgene_filtered/filtered_datasets.csv) ---")
    try:
        df = pd.read_csv(filtered_csv)
        print(f"  - 记录数 (行): {df.shape[0]} | 字段数 (列): {df.shape[1]}")
        print(f"  - 关键字段: {list(df.columns)[:8]}...")
    except Exception as e:
        print(f"  读取失败: {e}")
    print()

# 5. CellxGene 原始大细节表 (cellxgene_all_details)
details_json = os.path.join(db_dir, "cellxgene", "cellxgene_all_details", "cellxgene_all_details.json")
if os.path.exists(details_json):
    print("--- 5. CellxGene 原始细节 JSON (cellxgene_all_details/cellxgene_all_details.json) ---")
    try:
        with open(details_json, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"  - JSON 类型: {type(data)}")
        if isinstance(data, list):
            print(f"  - 记录数 (List 长度): {len(data)}")
        elif isinstance(data, dict):
            print(f"  - 键数量 (Dict Keys): {len(data.keys())}")
            # 打印前2个键作为示例
            print(f"  - 前几个键 (Sample Keys): {list(data.keys())[:3]}")
    except Exception as e:
        print(f"  读取失败: {e}")
    print()

# 6. cellxgene_collections_raw.json
collections_raw = os.path.join(db_dir, "cellxgene", "cellxgene_all_details", "cellxgene_collections_raw.json")
if os.path.exists(collections_raw):
    print("--- 6. CellxGene 原始 Collections JSON (cellxgene_all_details/cellxgene_collections_raw.json) ---")
    try:
        with open(collections_raw, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            print(f"  - 记录数: {len(data)}")
        elif isinstance(data, dict):
            print(f"  - 键数量: {len(data.keys())}")
            print(f"  - 示例键: {list(data.keys())[:3]}")
    except Exception as e:
        print(f"  读取失败: {e}")
    print()

# 7. peripheral_neural_sc_datasets_master.csv
master_csv = os.path.join(db_dir, "cellxgene", "cellxgene_all_details", "peripheral_neural_sc_datasets_master.csv")
if os.path.exists(master_csv):
    print("--- 7. 外周神经单细胞 Master 数据集 (cellxgene_all_details/peripheral_neural_sc_datasets_master.csv) ---")
    try:
        df = pd.read_csv(master_csv)
        print(f"  - 记录数 (行): {df.shape[0]} | 字段数 (列): {df.shape[1]}")
    except Exception as e:
        print(f"  读取失败: {e}")
    print()
