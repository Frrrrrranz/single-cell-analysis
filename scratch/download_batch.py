import subprocess
import json
import re
import time
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

# 读取 HTML 提取所有仍然缺失或校验失败需要重下的文献卡片
html_path = r"d:\OneDrive\Desktop\组\db\cellxgene\cellxgene_filtered\manual_download_helper.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 使用正则匹配新看板中的红色（校验失败）和黄色（当前缺失）卡片
pattern = r'class="card"[^>]*style="border-left:\s*5px\s*solid\s*var\(--(?:danger|warning)-color\);".*?<span class="paper-index">文献 #(\d+)</span>.*?<h2 class="paper-title"[^>]*>(.*?)</h2>.*?DOI:\s*<strong>(.*?)</strong>.*?PMID:\s*<strong>(.*?)</strong>.*?<div class="filename-value">([^<]*)</div>'
matches = re.findall(pattern, content, re.S)

papers = []
for idx, title, doi, pmid, filename in matches:
    papers.append({
        "idx": int(idx),
        "title": title.strip(),
        "doi": doi.strip(),
        "pmid": pmid.strip(),
        "filename": filename.strip()
    })

print(f"成功从新看板中提取了 {len(papers)} 篇需补收的文献（包含缺失与损坏文件）")

def call_opentabs(tool_name, params={}):
    try:
        # 在 Windows 上，我们需要确保正确转义参数
        cmd = ["opentabs", "tool", "call", tool_name, json.dumps(params)]
        # shell=True 在 Windows 下有助于寻找系统 Path 中的 opentabs
        res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', shell=True)
        if res.returncode == 0:
            return json.loads(res.stdout), None
        else:
            return None, res.stderr + "\n" + res.stdout
    except Exception as e:
        return None, str(e)

# 开始批量触发下载
success_count = 0
for paper in papers:
    # 检查目标文件是否已经在归库目录中存在，存在则跳过
    dest_file_path = os.path.join(r"D:\OneDrive\Desktop\组\db\cellxgene\cellxgene_filtered\downloads", paper["filename"])
    if os.path.exists(dest_file_path) and os.path.getsize(dest_file_path) > 0:
        print(f"⏭️ [文献 #{paper['idx']}] 的 PDF 文件已在归库目录中存在，自动跳过。")
        continue
        
    print(f"\n🚀 开始处理 [文献 #{paper['idx']}] DOI: {paper['doi']}")
    
    # 1. 打开谷歌学术检索 Tab
    scholar_url = f"https://scholar.google.com/scholar?q={paper['doi']}"
    print(f"   [Step 1] 打开学术搜索页: {scholar_url}")
    tab_info, err = call_opentabs("browser_open_tab", {"url": scholar_url})
    if err or not tab_info:
        print(f"   ❌ 打开标签页失败: {err}")
        continue
    
    tab_id = tab_info.get("id")
    print(f"   [Step 1] 标签页已打开，ID: {tab_id}。等待 7 秒加载页面...")
    time.sleep(7)
    
    # 1.5 检查是否触发了人机验证
    tabs_info, _ = call_opentabs("browser_list_tabs")
    if tabs_info:
        tabs_list = []
        if isinstance(tabs_info, list):
            tabs_list = tabs_info
        elif isinstance(tabs_info, dict):
            tabs_list = tabs_info.get("downloads", tabs_info.get("elements", tabs_info.get("tabs", [])))
            
        for t in tabs_list:
            if t.get("id") == tab_id:
                curr_url = t.get("url", "").lower()
                curr_title = t.get("title", "").lower()
                if "google.com/sorry" in curr_url or "系统检测" in curr_title or "sorry" in curr_title:
                    print("\n" + "="*60)
                    print("⚠️ 警告：检测到 Google 学术人机验证（验证码拦截）！")
                    print(f"  当前 URL: {t.get('url')}")
                    print(f"  当前 Title: {t.get('title')}")
                    print("="*60)
                    input("\n👉 请在您的 Chrome 浏览器中手动完成人机验证。完成后，回到本终端按下 [Enter] 键继续下载...\n")
                    print("   验证完成！正在等待页面重定向与重新加载...")
                    time.sleep(4)
                    break
    
    # 2. 查询页面上的链接元素
    print(f"   [Step 2] 查询页面链接...")
    res_dict, err = call_opentabs("browser_query_elements", {
        "tabId": tab_id,
        "selector": "a",
        "limit": 100
    })
    if err or not res_dict or "elements" not in res_dict:
        print(f"   ❌ 获取页面元素失败: {err}")
        # 关闭 Tab
        call_opentabs("browser_close_tab", {"tabId": tab_id})
        continue
        
    elements_list = res_dict.get("elements", [])
        
    # 3. 寻找 PDF 下载直达链接
    pdf_url = None
    # 匹配规则：href 属性中包含 pdf / cell.com / nature.com / science.org 并且不是 scholar 内部的链接
    for el in elements_list:
        href = el.get("attributes", {}).get("href", "")
        text = el.get("text", "")
        
        # 排除谷歌学术内部跳转
        if "scholar.google" in href or href.startswith("/scholar"):
            continue
            
        # 如果 text 包含 [PDF] 或 href 包含 pdf，或者是各大出版社 the 直达下载格式
        if "[PDF]" in text or ".pdf" in href.lower() or "pdf" in href.lower():
            pdf_url = href
            break
            
    if not pdf_url:
        # 如果依然没有，再做一次宽松检索，找所有 href 包含 cell.com/nature.com/science.org/springer/wiley 的外部 pdf 链接
        for el in elements_list:
            href = el.get("attributes", {}).get("href", "")
            if any(dom in href for dom in ["cell.com", "nature.com", "science.org", "sciencedirect.com"]):
                if "pdf" in href.lower() or "article" in href.lower():
                    pdf_url = href
                    break

    if pdf_url:
        print(f"   🎯 找到 PDF 下载链接: {pdf_url}")
        # 4. 调用 browser_download_file 触发下载
        print(f"   [Step 3] 触发浏览器下载，保存为: {paper['filename']}")
        dl_info, err = call_opentabs("browser_download_file", {
            "url": pdf_url,
            "filename": paper["filename"]
        })
        if err:
            print(f"   ❌ 触发下载失败: {err}")
        else:
            print(f"   ✅ 下载已成功触发！Download ID: {dl_info.get('downloadId')}")
            success_count += 1
    else:
        print(f"   ⚠️ 未在学术检索页右侧找到 PDF 直达链接，跳过自动下载。")
        
    # 5. 关闭临时标签页
    print(f"   [Step 4] 关闭标签页 ID: {tab_id}")
    call_opentabs("browser_close_tab", {"tabId": tab_id})
    
    # 稍微停顿一下防爬
    time.sleep(5)

print(f"\n🎉 批量下载处理完毕！共成功为 {success_count} 篇文献触发了浏览器下载。")
