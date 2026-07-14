import os
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

conv_dir = r"C:\Users\35221\.gemini\antigravity-ide\conversations"
found_files = []

for f in os.listdir(conv_dir):
    filepath = os.path.join(conv_dir, f)
    if os.path.isfile(filepath):
        size = os.path.getsize(filepath)
        mtime = os.path.getmtime(filepath)
        dt = datetime.fromtimestamp(mtime)
        found_files.append({
            "name": f,
            "path": filepath,
            "size": size,
            "mtime": mtime,
            "dt": dt.strftime("%Y-%m-%d %H:%M:%S")
        })

found_files.sort(key=lambda x: x["mtime"], reverse=True)

print("最近修改的对话文件：")
for t in found_files[:15]:
    print(f"时间: {t['dt']} | 文件: {t['name']:<50} | 大小: {t['size']:<8} 字节")
