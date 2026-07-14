import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

log_path = r"C:\Users\35221\.gemini\antigravity-ide\brain\b513ab32-f58c-4462-af81-2fdf56ece085\.system_generated\logs\transcript.jsonl"

try:
    with open(log_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    print(f"总共有 {len(lines)} 行记录。\n")
    
    for idx, line in enumerate(lines):
        try:
            data = json.loads(line)
            source = data.get("source", "UNKNOWN")
            step_type = data.get("type", "UNKNOWN")
            content = data.get("content", "")
            
            if step_type == "USER_INPUT":
                print(f"=== [Step {idx}] USER: ===")
                print(content)
                print()
            elif source == "MODEL" and "tool_calls" not in data:
                # 只有模型的文本回复
                print(f"=== [Step {idx}] ASSISTANT: ===")
                # 截取前300字符或打印全部
                print(content[:500] + ("..." if len(content) > 500 else ""))
                print()
        except Exception as e:
            print(f"解析第 {idx} 行失败: {e}")
            
except Exception as e:
    print("读取文件失败:", e)
