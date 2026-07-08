import subprocess
import json
import re
import os
import shutil
import sys
import fitz  # PyMuPDF

sys.stdout.reconfigure(encoding='utf-8')

HTML_PATH = r"D:\OneDrive\Desktop\组\db\cellxgene\cellxgene_filtered\manual_download_helper.html"
DEST_DIR = r"D:\OneDrive\Desktop\组\db\cellxgene\cellxgene_filtered\downloads"
LOG_PATH = r"C:\Users\35221\.gemini\antigravity-ide\brain\f8061bb4-46f5-4133-85a8-6edaab730eb9\.system_generated\tasks\task-602.log"

if not os.path.exists(DEST_DIR):
    os.makedirs(DEST_DIR)

def clean_str(s):
    if not s:
        return ""
    return re.sub(r'[^a-z0-9]', '', s.lower())

def get_doi_suffix(doi):
    if not doi or "/" not in doi:
        return ""
    parts = doi.split("/", 1)
    return parts[1].strip()

def call_opentabs(tool_name, params={}):
    try:
        cmd = ["opentabs", "tool", "call", tool_name, json.dumps(params)]
        res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', shell=True)
        if res.returncode == 0:
            return json.loads(res.stdout), None
        else:
            return None, res.stderr + "\n" + res.stdout
    except Exception as e:
        return None, str(e)

def main():
    print("=== 开始 CellxGene 下载文献物理级比对与整理归库 ===")
    
    # 1. 解析 manual_download_helper.html
    if not os.path.exists(HTML_PATH):
        print(f"❌ 找不到 HTML 辅助文件: {HTML_PATH}")
        return
        
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    pattern = r'class="card"[^>]*style="border-left:\s*5px\s*solid\s*var\(--(?:danger|warning)-color\);".*?<span class="paper-index">文献 #(\d+)</span>.*?<h2 class="paper-title"[^>]*>(.*?)</h2>.*?DOI:\s*<strong>(.*?)</strong>.*?PMID:\s*<strong>(.*?)</strong>.*?<div class="filename-value">([^<]*)</div>'
    matches = re.findall(pattern, html_content, re.S)
    
    papers_dict = {}
    for idx, title, doi, pmid, filename in matches:
        idx_num = int(idx)
        papers_dict[idx_num] = {
            "idx": idx_num,
            "title": title.strip(),
            "doi": doi.strip(),
            "pmid": pmid.strip(),
            "filename": filename.strip()
        }
        
    print(f"从辅助 HTML 中成功加载了 {len(papers_dict)} 篇文献的任务定义")
    
    # 2. 从 task-435.log 中解析 Download ID -> 文献 # 映射
    download_id_to_idx = {}
    if os.path.exists(LOG_PATH):
        print(f"正在分析后台任务日志: {LOG_PATH}")
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            log_text = f.read()
            
        # 按 "🚀 开始处理" 分割区块
        blocks = log_text.split("🚀 开始处理")
        for block in blocks:
            idx_match = re.search(r'\[文献 #(\d+)\]', block)
            dl_match = re.search(r'Download ID:\s*(\d+)', block)
            if idx_match and dl_match:
                paper_idx = int(idx_match.group(1))
                download_id = int(dl_match.group(1))
                download_id_to_idx[download_id] = paper_idx
                
        print(f"从后台任务日志中成功提取了 {len(download_id_to_idx)} 条精确的 [Download ID -> 文献 #] 映射")
    else:
        print("⚠️ 未找到后台任务日志，将退回到 DOI/PMID 模糊包含匹配模式。")

    # 3. 调用 OpenTabs 获取近期下载列表，带有强大的物理目录扫描 Fallback 机制
    print("正在从浏览器调取近期下载历史...")
    downloads_list = []
    dl_data, err = call_opentabs("browser_list_downloads", {"limit": 150})
    if not err and dl_data:
        if isinstance(dl_data, list):
            downloads_list = dl_data
        elif isinstance(dl_data, dict):
            downloads_list = dl_data.get("downloads", dl_data.get("elements", []))
            
    if not downloads_list:
        print("⚠️ 无法从浏览器调取记录（可能插件未启动/休眠），直接扫描本地物理下载文件夹...")
        local_dl_dir = r"C:\Users\35221\Downloads"
        if os.path.exists(local_dl_dir):
            for fname in os.listdir(local_dl_dir):
                if fname.lower().endswith(".pdf") or fname.lower().endswith(".htm") or fname.lower().endswith(".html"):
                    downloads_list.append({
                        "id": -1,
                        "filename": os.path.join(local_dl_dir, fname),
                        "url": fname,  # 没有 URL，降级用文件名比对
                        "state": "complete"
                    })
        
    print(f"调取到了 {len(downloads_list)} 条待分析的下载记录")
    
    # 筛选出状态是 complete 且物理文件确实在本地下载目录的记录
    completed_downloads = [d for d in downloads_list if d.get("state") == "complete"]
    print(f"其中已下载完毕的记录有 {len(completed_downloads)} 条")
    
    renamed_count = 0
    
    for dl in completed_downloads:
        dl_id = dl.get("id")
        dl_url = dl.get("url", "")
        dl_file = dl.get("filename", "")
        if not dl_url or not dl_file or not os.path.exists(dl_file):
            continue
            
        dl_url_lower = dl_url.lower()
        dl_file_lower = os.path.basename(dl_file).lower()
        
        matched_paper = None
        
        # 匹配策略 1: 后台日志 Download ID 精确匹配 (主选)
        if dl_id in download_id_to_idx:
            matched_idx = download_id_to_idx[dl_id]
            if matched_idx in papers_dict:
                matched_paper = papers_dict[matched_idx]
                print(f" -> [物理ID匹配成功] Download ID {dl_id} 精确匹配到 文献 #{matched_idx}")
                
        # 匹配策略 2: DOI 后缀包含匹配 (备选，针对非批量任务)
        if not matched_paper:
            for idx_key, paper in papers_dict.items():
                p_doi = paper["doi"]
                if p_doi and p_doi != "-" and p_doi != "无":
                    # 取出 DOI 后缀，例如 s42003-024-07315-x
                    doi_suffix = get_doi_suffix(p_doi)
                    cleaned_suffix = clean_str(doi_suffix)
                    if len(cleaned_suffix) > 5:
                        if cleaned_suffix in clean_str(dl_url) or cleaned_suffix in clean_str(dl_file):
                            matched_paper = paper
                            print(f" -> [DOI后缀匹配成功] DOI后缀 {doi_suffix} 匹配到 文献 #{paper['idx']}")
                            break
                            
        # 匹配策略 3: PMID 包含匹配 (备选)
        if not matched_paper:
            for idx_key, paper in papers_dict.items():
                p_pmid = paper["pmid"]
                if p_pmid and p_pmid != "-" and p_pmid != "无" and len(p_pmid) > 4:
                    if p_pmid in dl_url_lower or p_pmid in dl_file_lower:
                        matched_paper = paper
                        print(f" -> [PMID包含匹配成功] PMID {p_pmid} 匹配到 文献 #{paper['idx']}")
                        break

        # 匹配策略 4: PDF 文本内容特征核对 (针对手动下载文件名被随机命名的 Fallback 匹配)
        if not matched_paper and dl_file.lower().endswith(".pdf") and os.path.getsize(dl_file) > 0:
            try:
                doc_text = ""
                with fitz.open(dl_file) as doc:
                    for page in doc[:2]:
                        doc_text += page.get_text()
                doc_text_clean = clean_str(doc_text)
                
                for idx_key, paper in papers_dict.items():
                    # 用 PMID 校验文本内容
                    p_pmid = paper["pmid"]
                    if p_pmid and p_pmid != "-" and p_pmid != "无" and len(p_pmid) > 4:
                        if p_pmid in doc_text_clean:
                            matched_paper = paper
                            print(f" -> [内容PMID核对成功] 提取到内容包含 PMID {p_pmid}，匹配到 文献 #{paper['idx']}")
                            break
                            
                    # 用 DOI 后缀校验文本内容
                    p_doi = paper["doi"]
                    if not matched_paper and p_doi and p_doi != "-" and p_doi != "无":
                        doi_suffix = get_doi_suffix(p_doi)
                        cleaned_suffix = clean_str(doi_suffix)
                        if len(cleaned_suffix) > 5 and cleaned_suffix in doc_text_clean:
                            matched_paper = paper
                            print(f" -> [内容DOI核对成功] 提取到内容包含 DOI后缀 {doi_suffix}，匹配到 文献 #{paper['idx']}")
                            break
                            
                    # 用标题多长词核对文本内容
                    if not matched_paper:
                        title_words = [w for w in re.split(r'[^a-zA-Z]', paper["title"].lower()) if len(w) > 4]
                        if len(title_words) >= 3:
                            overlap = sum(1 for w in title_words if w in doc_text_clean)
                            if overlap >= 3:
                                matched_paper = paper
                                print(f" -> [内容标题词核对成功] 提取到内容重合单词数 {overlap}，匹配到 文献 #{paper['idx']}")
                                break
            except Exception as e:
                pass

        # 执行搬运与重命名
        if matched_paper:
            target_name = matched_paper["filename"]
            target_path = os.path.join(DEST_DIR, target_name)
            
            try:
                if os.path.exists(target_path):
                    os.remove(target_path)
                shutil.move(dl_file, target_path)
                print(f"   [文献 #{matched_paper['idx']}] 整理成功！")
                print(f"   原文件: {os.path.basename(dl_file)}")
                print(f"   -> 归库: {target_name}\n")
                renamed_count += 1
            except Exception as e:
                print(f"❌ 移动文件 {os.path.basename(dl_file)} 失败: {e}\n")
        else:
            # 过滤掉非 cellxgene 的外部下载噪音
            if any(dom in dl_url_lower for dom in ["cell.com", "nature.com", "science.org", "sciencedirect.com", "aacrjournals.org"]):
                print(f"⚠️ 下载文件 {os.path.basename(dl_file)} 未能成功比对并归库 (URL: {dl_url})\n")

    print(f"=== 归库比对整理完毕！共成功比对并整理归库了 {renamed_count} 篇文献 ===")

if __name__ == "__main__":
    main()
