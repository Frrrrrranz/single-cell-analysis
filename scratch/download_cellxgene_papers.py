import pandas as pd
import requests
import json
import os
import re
import sys
import time
import logging
import concurrent.futures
from bs4 import BeautifulSoup
from scansci_pdf.sources import download as scansciDownload

sys.stdout.reconfigure(encoding='utf-8')

# 配置日志规范，同时输出到控制台和日志文件
PROJECT_DIR = r"D:\OneDrive\Desktop\组"
CELLXGENE_DIR = os.path.join(PROJECT_DIR, "db", "cellxgene", "cellxgene_filtered")
DOWNLOAD_DIR = os.path.join(CELLXGENE_DIR, "downloads")
LOG_FILE = os.path.join(CELLXGENE_DIR, "download_papers.log")

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_FILE, encoding="utf-8")
    ]
)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def sanitize_filename(name):
    """
    替换文件名中的非法字符
    """
    name = str(name)
    name = re.sub(r'[\\/*?:"<>|]', "_", name)
    name = re.sub(r'\s+', " ", name).strip()
    return name[:100]

def get_pmid_and_title_from_europepmc(doi):
    """
    使用 Europe PMC API 从 DOI 获取 PMID 和文章标题
    """
    if not doi or pd.isna(doi) or str(doi).strip() in ["-", "", "nan", "None"]:
        return None, None
    doi_clean = str(doi).strip()
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=doi:{doi_clean}&format=json"
    
    # 卫语句：防止频繁请求被封，稍微加个延时
    time.sleep(1.0)
    
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            data = r.json()
            results = data.get("resultList", {}).get("result", [])
            if results:
                pmid = results[0].get("pmid")
                title = results[0].get("title")
                logging.info(f"成功通过 Europe PMC 转换 DOI [{doi_clean}] -> PMID: {pmid} | Title: {title[:50]}...")
                return pmid, title
            else:
                logging.warning(f"Europe PMC 未能找到 DOI [{doi_clean}] 的信息")
        else:
            logging.warning(f"Europe PMC 请求失败，状态码: {r.status_code}，DOI: {doi_clean}")
    except Exception as e:
        logging.error(f"Europe PMC 请求发生异常: {e}，DOI: {doi_clean}")
    return None, None

def download_file(url, save_path):
    """
    直接 HTTP 下载文件，并验证是否为合法 PDF (禁用重试以防卡死)
    """
    s = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=0)
    s.mount("https://", adapter)
    s.mount("http://", adapter)
    try:
        r = s.get(url, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            content = r.content
            if not content.startswith(b'%PDF'):
                logging.warning(f"下载文件内容头部非 %PDF (前缀为: {content[:10]}), 链接: {url}")
                return False
            with open(save_path, 'wb') as f:
                f.write(content)
            logging.info(f"成功保存 PDF: {os.path.basename(save_path)}")
            return True
        else:
            logging.warning(f"下载请求异常状态码: {r.status_code}, 链接: {url}")
    except Exception as e:
        logging.error(f"下载文件时发生错误 (已跳过): {e}, 链接: {url}")
    return False

def try_scansci_pdf(doi, save_path):
    """
    调用 scansci-pdf 引擎下载文献
    """
    if not doi or pd.isna(doi) or str(doi).strip() in ["-", "", "nan", "None"]:
        return False
    doi_clean = str(doi).strip()
    download_dir = os.path.dirname(save_path)
    
    try:
        # 硬性20秒超时保护
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(
                scansciDownload,
                doi_clean,
                output_dir=download_dir,
                scihub_enabled=True,
                rename=False
            )
            try:
                result = future.result(timeout=20)
            except concurrent.futures.TimeoutError:
                logging.warning(f"scansci-pdf 接口超时，判定为失败。DOI: {doi_clean}")
                return False
        
        if result and result.get("success"):
            temp_pdf_path = result.get("file")
            if temp_pdf_path and os.path.exists(temp_pdf_path):
                # 校验 PDF 格式
                with open(temp_pdf_path, 'rb') as f:
                    pdf_header = f.read(4)
                if pdf_header.startswith(b'%PDF'):
                    if temp_pdf_path != save_path:
                        if os.path.exists(save_path):
                            try:
                                os.remove(save_path)
                            except:
                                pass
                        os.rename(temp_pdf_path, save_path)
                    logging.info(f"成功通过 scansci-pdf 下载: {os.path.basename(save_path)} (来源: {result.get('source')})")
                    return True
                else:
                    logging.warning(f"下载内容非 %PDF, 路径: {temp_pdf_path}")
                    try:
                        os.remove(temp_pdf_path)
                    except:
                        pass
        else:
            logging.warning(f"scansci-pdf 下载失败: {result.get('error', 'unknown error') if result else 'no response'}")
    except Exception as e:
        logging.error(f"scansci-pdf 模块运行异常: {e}")
    return False

def try_pmc(pmid, save_path):
    """
    备用渠道：通过 PMID 查找 PMC 并下载 PDF (禁用重试以防卡死)
    """
    if not pmid or pd.isna(pmid) or str(pmid).strip() in ["-", "", "nan", "None"]:
        return False
    pmid_clean = str(pmid).strip()
    conv_url = f"https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids={pmid_clean}&format=json&tool=pmc_downloader&email=pmc_downloader@example.com"
    logging.info(f"正在尝试 PMC 转换 API 获取 PMID: {pmid_clean}")
    
    s = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=0)
    s.mount("https://", adapter)
    s.mount("http://", adapter)
    try:
        r = s.get(conv_url, headers=HEADERS, timeout=8)
        if r.status_code == 200:
            data = r.json()
            records = data.get("records", [])
            if records:
                pmcid = records[0].get("pmcid")
                if pmcid:
                    logging.info(f"[PMC] 查找到对应 PMCID: {pmcid} (PMID: {pmid_clean})")
                    pdf_url = f"https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/pdf/"
                    return download_file(pdf_url, save_path)
                else:
                    logging.info(f"[PMC] PMID: {pmid_clean} 未能关联到 PMC 全文 ID")
        else:
            logging.warning(f"[PMC] 请求 API 失败，状态码: {r.status_code}")
    except Exception as e:
        logging.error(f"[PMC] 请求发生异常 (已跳过): {e}")
    return False

def generate_manual_html(failed_papers, count, output_path):
    """
    生成辅助手动下载的 HTML 页面
    """
    import urllib.parse
    cards_list = []
    
    for idx, paper in enumerate(failed_papers, 1):
        title = paper['title']
        doi = paper['doi']
        pmid = paper['pmid']
        filename = paper['filename']
        collection_id = paper['collection_id']
        
        doi_clean = str(doi).strip() if doi and doi != "-" else "-"
        scholar_query = urllib.parse.quote(doi_clean if doi_clean != "-" else title)
        scholar_link = f"https://scholar.google.com/scholar?q={scholar_query}"
        scihub_link = f"https://sci-hub.st/{doi_clean}" if doi_clean != "-" else "https://sci-hub.st/"
        doi_link = f"https://doi.org/{doi_clean}" if doi_clean != "-" else "#"
        
        if pmid and pmid != "-":
            pubmed_link = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
            pubmed_btn_text = "PubMed 直达"
            pubmed_btn_class = "btn-pubmed-direct"
        else:
            pubmed_title_query = urllib.parse.quote(title)
            pubmed_link = f"https://pubmed.ncbi.nlm.nih.gov/?term={pubmed_title_query}"
            pubmed_btn_text = "PubMed 搜标题"
            pubmed_btn_class = "btn-pubmed-search"
            
        doi_display = doi_clean
        pmid_display = pmid if pmid else "无"
        
        btn_doi_html = f'<a href="{doi_link}" target="_blank" class="btn btn-doi">打开 DOI 页面</a>' if doi_clean != "-" else ''
        btn_scihub_html = f'<a href="{scihub_link}" target="_blank" class="btn btn-scihub">Sci-Hub 下载</a>' if doi_clean != "-" else ''
        btn_pubmed_html = f'<a href="{pubmed_link}" target="_blank" class="btn {pubmed_btn_class}">{pubmed_btn_text}</a>'
        
        card_html = f"""
        <div class="card" data-title="{title.lower()}" data-doi="{doi_clean.lower()}" data-pmid="{pmid_display.lower()}">
            <div class="card-header">
                <div class="header-left">
                    <span class="paper-index">文献 #{idx}</span>
                    <span class="paper-reason reason-other">自动下载失败</span>
                </div>
                <span class="paper-row-num">Collection ID: {collection_id[:8]}...</span>
            </div>
            <h2 class="paper-title" onclick="copyText('{title.replace("'", "\\'")}')" title="点击复制标题">{title}</h2>
            <div class="meta-info">
                <span class="meta-item">DOI: <strong onclick="copyText('{doi_clean}')" class="clickable-meta" title="点击复制 DOI">{doi_display}</strong></span>
                <span class="meta-item">PMID: <strong onclick="copyText('{pmid_display}')" class="clickable-meta" title="点击复制 PMID">{pmid_display}</strong></span>
            </div>
            <div class="filename-box" onclick="copyFilename(this, '{filename.replace("'", "\\'")}')" title="点击复制规范文件名">
                <div class="filename-box-title">需保存的规范文件名（点击一键复制）：</div>
                <div class="filename-value">{filename}</div>
                <div class="copy-indicator">点击复制</div>
            </div>
            <div class="action-links">
                <a href="{scholar_link}" target="_blank" class="btn btn-scholar">谷歌学术 检索</a>
                {btn_pubmed_html}
                {btn_scihub_html}
                {btn_doi_html}
            </div>
        </div>
        """
        cards_list.append(card_html)
        
    html_template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>外周神经单细胞数据集文献手动下载辅助页面</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Noto+Sans+SC:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #f8fafc;
            --container-bg: #ffffff;
            --card-bg: #ffffff;
            --border-color: #e2e8f0;
            --text-primary: #0f172a;
            --text-secondary: #475569;
            --accent-blue: #0284c7;
            --accent-purple: #7c3aed;
            --success-color: #059669;
            --warning-color: #d97706;
            --danger-color: #dc2626;
            --indigo-color: #4f46e5;
        }
        
        * {
            box-sizing: border-box;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        }

        body {
            font-family: 'Outfit', 'Noto Sans SC', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-primary);
            margin: 0;
            padding: 40px 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .container {
            max-width: 1000px;
            width: 100%;
        }

        header {
            text-align: center;
            margin-bottom: 40px;
        }

        h1 {
            font-size: 2.5rem;
            font-weight: 700;
            color: var(--text-primary);
            margin: 0 0 12px 0;
        }

        .subtitle {
            color: var(--text-secondary);
            font-size: 1.1rem;
            max-width: 700px;
            margin: 0 auto;
            line-height: 1.6;
        }

        .stats-banner {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 15px;
            text-align: center;
            margin-bottom: 30px;
            font-size: 1.1rem;
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05);
        }

        .highlight {
            color: var(--warning-color);
            font-weight: bold;
        }

        .list-container {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .card {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 22px;
            position: relative;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
        }

        .card:hover {
            transform: translateY(-2px);
            border-color: var(--accent-blue);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
        }

        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
        }

        .paper-index {
            background: rgba(245, 158, 11, 0.1);
            color: var(--warning-color);
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.8rem;
            font-weight: 600;
        }

        .paper-reason {
            background: rgba(239, 68, 68, 0.1);
            color: var(--danger-color);
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.8rem;
            font-weight: 600;
            margin-left: 8px;
        }

        .paper-row-num {
            color: var(--text-secondary);
            font-size: 0.8rem;
        }

        .paper-title {
            font-size: 1.25rem;
            margin: 0 0 12px 0;
            line-height: 1.4;
            cursor: pointer;
        }

        .paper-title:hover {
            color: var(--accent-blue);
        }

        .meta-info {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            margin-bottom: 16px;
            font-size: 0.9rem;
            color: var(--text-secondary);
        }

        .clickable-meta {
            color: var(--text-primary);
            cursor: pointer;
            text-decoration: underline;
        }

        .clickable-meta:hover {
            color: var(--accent-blue);
        }

        .filename-box {
            background: #f8fafc;
            border: 1px dashed var(--border-color);
            border-radius: 8px;
            padding: 12px;
            margin-bottom: 20px;
            cursor: pointer;
            position: relative;
        }

        .filename-box:hover {
            background: #f1f5f9;
            border-color: var(--accent-blue);
        }

        .filename-box-title {
            font-size: 0.75rem;
            color: var(--text-secondary);
            margin-bottom: 4px;
        }

        .filename-value {
            font-family: monospace;
            font-size: 0.9rem;
            word-break: break-all;
            color: var(--success-color);
        }

        .copy-indicator {
            position: absolute;
            right: 12px;
            top: 50%;
            transform: translateY(-50%);
            font-size: 0.75rem;
            background: rgba(0, 0, 0, 0.05);
            padding: 2px 6px;
            border-radius: 4px;
            color: var(--text-secondary);
        }

        .action-links {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }

        .btn {
            padding: 8px 16px;
            border-radius: 8px;
            font-size: 0.85rem;
            text-decoration: none;
            font-weight: 500;
            display: inline-flex;
            align-items: center;
        }

        .btn-scholar { background: rgba(2, 132, 199, 0.1); color: var(--accent-blue); }
        .btn-scholar:hover { background: rgba(2, 132, 199, 0.2); }
        .btn-pubmed-direct { background: rgba(124, 58, 237, 0.1); color: var(--accent-purple); }
        .btn-pubmed-direct:hover { background: rgba(124, 58, 237, 0.2); }
        .btn-pubmed-search { background: rgba(79, 70, 229, 0.1); color: var(--indigo-color); }
        .btn-pubmed-search:hover { background: rgba(79, 70, 229, 0.2); }
        .btn-scihub { background: rgba(5, 150, 105, 0.1); color: var(--success-color); }
        .btn-scihub:hover { background: rgba(5, 150, 105, 0.2); }
        .btn-doi { background: rgba(0, 0, 0, 0.05); color: var(--text-primary); }
        .btn-doi:hover { background: rgba(0, 0, 0, 0.1); }

        #toast {
            visibility: hidden;
            min-width: 250px;
            background-color: #1f2937;
            color: #fff;
            text-align: center;
            border-radius: 8px;
            padding: 12px;
            position: fixed;
            z-index: 1000;
            left: 50%;
            bottom: 30px;
            transform: translateX(-50%);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            border: 1px solid var(--accent-blue);
        }

        #toast.show {
            visibility: visible;
        }
    </style>
    <script>
        function copyText(text) {
            navigator.clipboard.writeText(text).then(() => {
                showToast("已成功复制到剪贴板！");
            });
        }
        function copyFilename(element, text) {
            navigator.clipboard.writeText(text).then(() => {
                const indicator = element.querySelector('.copy-indicator');
                indicator.textContent = "已复制";
                indicator.style.color = "var(--success-color)";
                showToast("文件名已复制，下载文献后重命名为此名称即可！");
                setTimeout(() => {
                    indicator.textContent = "点击复制";
                    indicator.style.color = "var(--text-secondary)";
                }, 2000);
            });
        }
        function showToast(msg) {
            const toast = document.getElementById("toast");
            toast.textContent = msg;
            toast.className = "show";
            setTimeout(() => { toast.className = ""; }, 2500);
        }
    </script>
</head>
<body>
    <div class="container">
        <header>
            <h1>外周神经数据集文献手动下载辅助页面</h1>
            <div class="subtitle">对于无法自动下载的文献，请在本页面辅助下手动下载，并将 PDF 文件重命名为页面提示的规范名称保存至 downloads 目录中。</div>
        </header>

        <div class="stats-banner">
            共计需要手动处理文献：<span class="highlight">__COUNT__</span> 篇
        </div>

        <div class="list-container">
            __CARDS_HTML__
        </div>
    </div>
    <div id="toast">已复制</div>
</body>
</html>
"""
    final_html = html_template.replace("__COUNT__", str(count)).replace("__CARDS_HTML__", "\n".join(cards_list))
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_html)
    logging.info(f"生成手动下载网页: {output_path}")

def main():
    logging.info("===== CellxGene 82套数据集文献自动下载与归纳脚本启动 =====")
    
    csv_path = os.path.join(CELLXGENE_DIR, "filtered_datasets.csv")
    if not os.path.exists(csv_path):
        logging.critical(f"缺少输入文件: {csv_path}")
        return
        
    df = pd.read_csv(csv_path)
    logging.info(f"成功读取 {csv_path}，包含数据集记录共: {len(df)} 条")
    
    # 卫语句：检查关键字段是否存在
    required_cols = ["collection_id", "collection_name", "doi", "dataset_id", "assay", "matched_cell_types"]
    for col in required_cols:
        if col not in df.columns:
            logging.critical(f"输入 CSV 缺少关键列: {col}")
            return
            
    # 先做一层 Unique DOI 的统计，避免对同一个 DOI 重复发起 Europe PMC 转换和下载
    # 我们以 doi 作为 Unique 标识。对于无 doi 的记录，使用 collection_id 作为唯一标识
    unique_papers = {}
    
    for idx, row in df.iterrows():
        doi_val = str(row['doi']).strip()
        coll_id = str(row['collection_id']).strip()
        coll_name = str(row['collection_name']).strip()
        
        # 确定唯一标识
        is_doi_valid = doi_val and doi_val not in ["nan", "None", "", "-"]
        paper_key = doi_val if is_doi_valid else f"no_doi_{coll_id}"
        
        if paper_key not in unique_papers:
            unique_papers[paper_key] = {
                "doi": doi_val if is_doi_valid else None,
                "collection_id": coll_id,
                "collection_name": coll_name,
                "dataset_ids": [str(row['dataset_id']).strip()],
                "matched_cell_types": str(row['matched_cell_types']).strip(),
                "assays": [str(row['assay']).strip()],
                "pmid": None,
                "resolved_title": None,
                "download_success": False,
                "filename": None
            }
        else:
            unique_papers[paper_key]["dataset_ids"].append(str(row['dataset_id']).strip())
            # 合并 cell_types 和 assay
            cell_types = str(row['matched_cell_types']).strip()
            if cell_types not in unique_papers[paper_key]["matched_cell_types"]:
                unique_papers[paper_key]["matched_cell_types"] += f"; {cell_types}"
            
            assay_val = str(row['assay']).strip()
            if assay_val not in unique_papers[paper_key]["assays"]:
                unique_papers[paper_key]["assays"].append(assay_val)

    logging.info(f"经合并去重，共计包含独特论文/文献记录数: {len(unique_papers)}")

    # 第一阶段：自动转换 DOI -> PMID 并且查询文献真实标题
    logging.info("\n>>> 阶段一：开始 DOI 到 PMID 批量转换 (使用 Europe PMC)")
    for key, paper in unique_papers.items():
        if paper["doi"]:
            pmid, resolved_title = get_pmid_and_title_from_europepmc(paper["doi"])
            paper["pmid"] = pmid if pmid else "-"
            paper["resolved_title"] = resolved_title if resolved_title else paper["collection_name"]
        else:
            paper["pmid"] = "-"
            paper["resolved_title"] = paper["collection_name"]
            logging.info(f"文献无 DOI，使用 Collection Name 作为标题: {paper['collection_name']}")
            
    # 第二阶段：根据获取的 PMID/DOI 设计规范文件名并下载
    logging.info("\n>>> 阶段二：开始批量下载 PDF 文献")
    for key, paper in unique_papers.items():
        title = paper["resolved_title"]
        doi = paper["doi"]
        pmid = paper["pmid"]
        
        # 规范文件名命名
        prefix = ""
        if pmid and pmid != "-":
            prefix = f"PMID_{pmid}"
        elif doi:
            prefix = f"DOI_{sanitize_filename(doi)}"
        else:
            prefix = f"COLL_{paper['collection_id'][:8]}"
            
        safe_title = sanitize_filename(title)
        filename = f"{prefix}_{safe_title}.pdf"
        paper["filename"] = filename
        save_path = os.path.join(DOWNLOAD_DIR, filename)
        
        logging.info(f"\n--- 处理文献: {title[:60]}... ---")
        
        # 1. 检查断点续传（本地是否已存在）
        if os.path.exists(save_path) and os.path.getsize(save_path) > 10 * 1024:
            logging.info(f"本地已存在合规 PDF，跳过下载。")
            paper["download_success"] = True
            continue
            
        logging.info(f"本地文件未就位，跳过自动下载，标记为待手动处理。")
        paper["download_success"] = False
        
    # 第三阶段：将映射数据还原至原始 82 行数据集，并导出归纳表
    logging.info("\n>>> 阶段三：正在整理归纳数据集文献大表...")
    summary_data = []
    failed_list = []
    
    for idx, row in df.iterrows():
        doi_val = str(row['doi']).strip()
        coll_id = str(row['collection_id']).strip()
        
        is_doi_valid = doi_val and doi_val not in ["nan", "None", "", "-"]
        paper_key = doi_val if is_doi_valid else f"no_doi_{coll_id}"
        
        paper_info = unique_papers.get(paper_key)
        
        pmid_display = paper_info["pmid"] if paper_info else "-"
        title_display = paper_info["resolved_title"] if paper_info else row["collection_name"]
        filename_display = paper_info["filename"] if paper_info else "-"
        status_display = "Y" if (paper_info and paper_info["download_success"]) else "N"
        pdf_path_display = os.path.join(DOWNLOAD_DIR, filename_display) if status_display == "Y" else ""
        
        summary_data.append({
            "collection_id": row["collection_id"],
            "dataset_id": row["dataset_id"],
            "collection_name": row["collection_name"],
            "Publication_Title": title_display,
            "doi": row["doi"] if is_doi_valid else "-",
            "PMID": pmid_display,
            "细胞种类": row["matched_cell_types"],
            "工具": row["assay"],
            "是否下载成功(Y/N)": status_display,
            "本地PDF路径": pdf_path_display
        })
        
    # 转换为 DataFrame 导出 Excel
    summary_df = pd.DataFrame(summary_data)
    summary_excel_path = os.path.join(CELLXGENE_DIR, "pns_papers_summary.xlsx")
    summary_df.to_excel(summary_excel_path, index=False)
    logging.info(f"归纳汇总大表导出成功: {summary_excel_path}")
    
    # 统计独特文献中下载失败的项目，用以生成辅助 HTML
    for key, paper in unique_papers.items():
        if not paper["download_success"]:
            failed_list.append({
                "title": paper["resolved_title"],
                "doi": paper["doi"] if paper["doi"] else "-",
                "pmid": paper["pmid"] if paper["pmid"] else "-",
                "filename": paper["filename"],
                "collection_id": paper["collection_id"]
            })
            
    if failed_list:
        manual_html_path = os.path.join(CELLXGENE_DIR, "manual_download_helper.html")
        generate_manual_html(failed_list, len(failed_list), manual_html_path)
    else:
        # 如果全部成功，删除以前残留的 helper html
        manual_html_path = os.path.join(CELLXGENE_DIR, "manual_download_helper.html")
        if os.path.exists(manual_html_path):
            try:
                os.remove(manual_html_path)
            except:
                pass
        logging.info("恭喜！所有独特文献（共 %d 篇）自动下载已全部成功！" % len(unique_papers))
        
    logging.info(f"\n==================== 下载统计 ====================")
    logging.info(f"数据集记录总数: {len(df)}")
    logging.info(f"去重文献总数: {len(unique_papers)}")
    success_num = sum(1 for p in unique_papers.values() if p["download_success"])
    logging.info(f"独特文献成功下载: {success_num} 篇")
    logging.info(f"独特文献下载失败: {len(unique_papers) - success_num} 篇")
    logging.info("==================================================")

if __name__ == "__main__":
    main()
