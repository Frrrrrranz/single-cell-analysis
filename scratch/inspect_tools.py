import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

try:
    cmd = 'conda activate py312_work; opentabs tool list'
    res = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True, encoding='utf-8')
    print("=== Raw Output Snippet ===")
    print(res.stdout[:1500])
except Exception as e:
    print("Error:", e)
