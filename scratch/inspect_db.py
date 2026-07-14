import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

db_path = r"C:\Users\35221\.gemini\antigravity-ide\conversations\83b71394-57ed-49df-87a5-290c0bb87f75.db"

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT idx, step_type, status, step_payload FROM steps LIMIT 10;")
    rows = cursor.fetchall()
    
    for row in rows:
        idx, step_type, status, payload = row
        print(f"=== Step {idx} | Type {step_type} | Status {status} ===")
        if payload:
            print("Payload length:", len(payload))
            # 试着用 utf-8 解码一部分文本
            decoded = payload.decode('utf-8', errors='ignore')
            print("Decoded snippet:")
            print(decoded[:500])
        else:
            print("No payload")
        print()
        
    conn.close()
except Exception as e:
    print("Error:", e)
