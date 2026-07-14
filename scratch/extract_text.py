import sqlite3
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

db_path = r"C:\Users\35221\.gemini\antigravity-ide\conversations\83b71394-57ed-49df-87a5-290c0bb87f75.db"

def clean_non_printable(text):
    # 保留中文、英文、常见标点符号和空白字符
    return "".join(c for c in text if c.isprintable() or c in "\n\r\t")

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 查找最大的 idx 
    cursor.execute("SELECT MAX(idx) FROM steps;")
    max_idx = cursor.fetchone()[0]
    print(f"最大步骤索引 (max_idx): {max_idx}\n")
    
    # 获取第 0 步和最后 5 步
    indices_to_fetch = [0] + list(range(max_idx - 5, max_idx + 1))
    # 去重并排序
    indices_to_fetch = sorted(list(set(i for i in indices_to_fetch if i >= 0)))
    
    for idx in indices_to_fetch:
        cursor.execute("SELECT step_type, status, step_payload FROM steps WHERE idx = ?;", (idx,))
        row = cursor.fetchone()
        if row:
            step_type, status, payload = row
            print(f"==================== Step {idx} | Type {step_type} | Status {status} ====================")
            if payload:
                decoded = payload.decode('utf-8', errors='ignore')
                cleaned = clean_non_printable(decoded)
                # 打印前 1500 个字符
                print(cleaned[:1500])
                if len(cleaned) > 1500:
                    print("... [已截断] ...")
            else:
                print("No payload")
            print()
            
    conn.close()
except Exception as e:
    print("Error:", e)
