import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

excel_path = r"D:\OneDrive\Desktop\组\db\数据集_按物种组织分类.xlsx"
df = pd.read_excel(excel_path, sheet_name='全部')

print("=== 各解剖大类（组织系统大类）中 L1-L4 覆盖情况统计 ===")
# 统计每个大类下，L1, L2, L3, L4 各自的数据集数量
# 我们需要把 '细胞分层' 拆解
df['L1'] = df['细胞分层'].apply(lambda x: 1 if pd.notna(x) and 'L1' in str(x) else 0)
df['L2'] = df['细胞分层'].apply(lambda x: 1 if pd.notna(x) and 'L2' in str(x) else 0)
df['L3'] = df['细胞分层'].apply(lambda x: 1 if pd.notna(x) and 'L3' in str(x) else 0)
df['L4'] = df['细胞分层'].apply(lambda x: 1 if pd.notna(x) and 'L4' in str(x) else 0)

anatomy_summary = df.groupby('组织系统大类').agg(
    数据集总数=('Species', 'count'),
    含有_L1_神经元=('L1', 'sum'),
    含有_L2_胶质=('L2', 'sum'),
    含有_L3_基质=('L3', 'sum'),
    含有_L4_内分泌=('L4', 'sum')
).reset_index()

# 按照数据集数量降序排列
anatomy_summary = anatomy_summary.sort_values(by='数据集总数', ascending=False)
print(anatomy_summary.to_string(index=False))

print("\n=== 同时含有多个 Tier 的数据集数量分析 ===")
df['tier_count'] = df['L1'] + df['L2'] + df['L3'] + df['L4']
print(df['tier_count'].value_counts().sort_index())
print("\n同时含有 3 个及以上 Tier 的数据集示例:")
multi_tier_df = df[df['tier_count'] >= 3]
for idx, row in multi_tier_df.head(5).iterrows():
    print(f"- 大类: {row['组织系统大类']} | 物种: {row['物种(中文)']} | 分层: {row['细胞分层']} | Title: {row['Publication_Title']}")
