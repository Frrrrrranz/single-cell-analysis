import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

excel_path = r"D:\OneDrive\Desktop\组\db\数据集_按物种组织分类.xlsx"
df_summary = pd.read_excel(excel_path, sheet_name='汇总')

print("--- '汇总' 工作表完整内容 ---")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
print(df_summary)

print("\n--- '全部' 工作表中各种类别的统计 ---")
df_all = pd.read_excel(excel_path, sheet_name='全部')
print("\n【物种分布】")
print(df_all['物种(中文)'].value_counts())
print("\n【组织系统大类分布】")
print(df_all['组织系统大类'].value_counts())
print("\n【物种 x 组织系统大类】")
print(pd.crosstab(df_all['物种(中文)'], df_all['组织系统大类']))
print("\n【细胞分层分布】")
print(df_all['细胞分层'].value_counts())
