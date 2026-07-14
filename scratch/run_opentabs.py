import subprocess
import json
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')

def call_tool(name, params={}):
    cmd = f'conda activate py312_work; opentabs tool call {name} \'{json.dumps(params)}\''
    res = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True, encoding='utf-8')
    return res.stdout, res.stderr

print("=== Opening Tab: Google Scholar for Paper 7 ===")
stdout, stderr = call_tool("browser_open_tab", {"url": "https://scholar.google.com/scholar?q=10.1016/j.cell.2023.11.026"})
print("STDOUT:")
print(stdout)
print("STDERR:")
print(stderr)
