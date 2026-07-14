import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = r"D:\OneDrive\Desktop\组\db\数据集_按物种组织分类.xlsx"

try:
    xls = pd.ExcelFile(file_path)
    print("Sheets in the excel file:", xls.sheet_names)
    
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name)
        print(f"\n--- Sheet: {sheet_name} ---")
        print(f"Shape: {df.shape}")
        print("Columns:", list(df.columns))
        print("First 5 rows:")
        print(df.head(5))
except Exception as e:
    print("Error:", e)
