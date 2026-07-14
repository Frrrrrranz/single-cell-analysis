"""
CellxGene 外周神经数据集筛选与存储估算脚本

功能：
1. 物种过滤（仅 Homo sapiens / Mus musculus）
2. 排除空间转录组数据
3. 四层细胞分类映射
4. 仅保留含四层分类中任一细胞类型的数据集（选项 C）
5. Collection 级别去重（选细胞数最多的 dataset）
6. 通过 HTTP HEAD 请求估算 h5ad 文件大小（不下载）

使用方式：
    python filter-cellxgene-datasets.py [--estimate-size] [--head-timeout 10]
"""

import csv
import json
import logging
import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict
from typing import Optional

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

# === 路径配置 ===
PROJECT_ROOT = Path(r"D:\OneDrive\Desktop\组")
DB_DIR = PROJECT_ROOT / "db" / "cellxgene" / "cellxgene_all_details"
INPUT_CSV = DB_DIR / "cellxgene_neural_peripheral_candidates.csv"
OUTPUT_DIR = PROJECT_ROOT / "db" / "cellxgene" / "cellxgene_filtered"

# === 四层细胞分类映射 ===
# NOTE: 键为小写，用于模糊匹配 CellxGene 的 cell_type 标签
# 每个键映射到 (tier, 中文名, 英文标准名)

TIER_MAPPING: dict[str, tuple[int, str, str]] = {
    # --- Tier 1：真正神经元 ---
    "sensory neuron": (1, "感觉神经元", "Sensory neuron"),
    "sensory neuron of dorsal root ganglion": (1, "感觉神经元(DRG)", "Sensory neuron (DRG)"),
    "trigeminal neuron": (1, "感觉神经元(三叉)", "Trigeminal neuron"),
    "motor neuron": (1, "运动神经元", "Motor neuron"),
    "inhibitory motor neuron": (1, "抑制性运动神经元", "Inhibitory motor neuron"),
    "cardiac neuron": (1, "自主神经元(心脏)", "Cardiac neuron"),
    "parasympathetic neuron": (1, "副交感神经元", "Parasympathetic neuron"),
    "sympathetic neuron": (1, "交感神经元", "Sympathetic neuron"),
    "enteric neuron": (1, "肠神经元", "Enteric neuron"),
    "afferent neuron": (1, "传入神经元", "Afferent neuron"),
    "interneuron": (1, "中间神经元(肠)", "Interneuron (ENS)"),
    "neuron": (1, "泛神经元", "Neuron (generic)"),
    "peripheral nervous system neuron": (1, "外周神经元", "Peripheral nervous system neuron"),
    "efferent neuron": (1, "传出神经元", "Efferent neuron"),
    "neuronal receptor cell": (1, "受体神经元(待定)", "Neuronal receptor cell"),  # NOTE: 对应"待定_泛神经"中的部分数据集

    # --- Tier 2：神经胶质 ---
    "schwann cell": (2, "雪旺细胞", "Schwann cell"),
    "non-myelinating schwann cell": (2, "非髓鞘化雪旺细胞", "Non-myelinating Schwann cell"),
    "myelinating schwann cell": (2, "髓鞘形成雪旺细胞", "Myelinating Schwann cell"),
    "schwann cell precursor": (2, "雪旺细胞前体", "Schwann cell precursor"),
    "immature schwann cell": (2, "未成熟雪旺细胞", "Immature Schwann cell"),
    "enteroglial cell": (2, "肠神经胶质细胞", "Enteroglial cell"),
    "enteric glia": (2, "肠胶质", "Enteric glia"),
    "peripheral/enteric glia": (2, "外周/肠胶质", "Peripheral/enteric glia"),
    "glial cell": (2, "胶质细胞(泛)", "Glial cell (generic)"),
    "satellite glial cell": (2, "卫星胶质细胞", "Satellite glial cell"),
    "perineuronal satellite cell": (2, "卫星胶质细胞", "Satellite glial cell"),

    # --- Tier 3：神经相关基质 ---
    "perineurial cell": (3, "神经周细胞", "Perineurial cell"),

    # --- Tier 4：神经内分泌系统 ---
    "enteroendocrine cell": (4, "肠内分泌细胞", "Enteroendocrine cell"),
    "intestinal enteroendocrine cell": (4, "肠内分泌细胞", "Intestinal enteroendocrine cell"),
    "enteroendocrine cell of colon": (4, "结肠肠内分泌细胞", "Enteroendocrine cell of colon"),
    "enteroendocrine cell of small intestine": (4, "小肠肠内分泌细胞", "Enteroendocrine cell of small intestine"),  # NOTE: 修复对小肠内分泌数据集的误筛
    "enterochromaffin-like cell": (4, "肠嗜铬样细胞", "Enterochromaffin-like cell"),
    "type ec enteroendocrine cell": (4, "EC型肠内分泌", "Type EC enteroendocrine cell"),
    "type g enteroendocrine cell": (4, "G型肠内分泌", "Type G enteroendocrine cell"),
    "type d enteroendocrine cell": (4, "D型肠内分泌", "Type D enteroendocrine cell"),
    "type l enteroendocrine cell": (4, "L型肠内分泌", "Type L enteroendocrine cell"),
    "type x enteroendocrine cell": (4, "X型肠内分泌", "Type X enteroendocrine cell"),
    "neuroendocrine cell": (4, "神经内分泌细胞", "Neuroendocrine cell"),
    "pulmonary neuroendocrine cell": (4, "肺神经内分泌细胞", "Pulmonary neuroendocrine cell"),
}

# 需要排除的"伪神经"细胞类型（不属于四层体系）
EXCLUDED_CELL_TYPES = {
    "merkel cell",  # 皮肤机械感受器，非典型外周神经元
}

# 空间转录组技术关键词（用于排除）
SPATIAL_ASSAY_KEYWORDS = [
    "visium", "spatial", "slide-seq", "merfish", "seqfish",
    "stereo-seq", "10x xenium", "cosmx",
]


def isSpatialAssay(assay: str) -> bool:
    """判断是否为空间转录组技术"""
    assayLower = assay.lower()
    return any(kw in assayLower for kw in SPATIAL_ASSAY_KEYWORDS)



def mapCellTypesToTiers(matchedCellTypes: str) -> dict[int, list[str]]:
    """
    将 CellxGene 的 matched_cell_types 字段映射到四层分类体系。

    返回: {tier_number: [匹配到的细胞类型标准名列表]}
    """
    tiersFound: dict[int, list[str]] = {1: [], 2: [], 3: [], 4: []}

    if not matchedCellTypes or matchedCellTypes.strip() == "":
        return tiersFound

    # matched_cell_types 以 | 分隔
    cellTypes = [ct.strip().lower() for ct in matchedCellTypes.split("|")]

    for ct in cellTypes:
        if ct in EXCLUDED_CELL_TYPES:
            continue
        if ct in TIER_MAPPING:
            tier, _, stdName = TIER_MAPPING[ct]
            if stdName not in tiersFound[tier]:
                tiersFound[tier].append(stdName)

    return tiersFound


def hasTierMatch(tiersFound: dict[int, list[str]]) -> bool:
    """检查是否有任何层级匹配（选项 C：仅保留含四层分类中任一细胞的数据集）"""
    return any(len(v) > 0 for v in tiersFound.values())


def estimateFileSizes(urls: list[str], timeout: int = 10) -> dict[str, Optional[int]]:
    """
    通过 HTTP HEAD 请求获取文件大小（不下载）。
    
    返回: {url: size_bytes} 或 {url: None}（如果获取失败）
    """
    # NOTE: 延迟导入，因为 --estimate-size 是可选的
    import urllib.request

    results: dict[str, Optional[int]] = {}
    total = len(urls)

    for i, url in enumerate(urls, 1):
        if i % 10 == 0 or i == 1:
            logger.info(f"  正在查询文件大小 ({i}/{total})...")

        try:
            req = urllib.request.Request(url, method="HEAD")
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                contentLength = resp.headers.get("Content-Length")
                if contentLength:
                    results[url] = int(contentLength)
                else:
                    results[url] = None
        except Exception as e:
            logger.warning(f"  无法获取 {url[:80]}... 的大小: {e}")
            results[url] = None

    return results


def formatBytes(sizeBytes: int) -> str:
    """将字节数格式化为人类可读的字符串"""
    if sizeBytes < 1024:
        return f"{sizeBytes} B"
    elif sizeBytes < 1024 ** 2:
        return f"{sizeBytes / 1024:.1f} KB"
    elif sizeBytes < 1024 ** 3:
        return f"{sizeBytes / (1024 ** 2):.1f} MB"
    else:
        return f"{sizeBytes / (1024 ** 3):.2f} GB"


def main() -> None:
    parser = argparse.ArgumentParser(description="CellxGene 外周神经数据集筛选")
    parser.add_argument(
        "--estimate-size",
        action="store_true",
        help="通过 HTTP HEAD 请求估算 h5ad 文件大小（需网络连接）",
    )
    parser.add_argument(
        "--head-timeout",
        type=int,
        default=10,
        help="HEAD 请求超时时间（秒），默认 10",
    )
    args = parser.parse_args()

    # === 读取输入 CSV ===
    logger.info(f"读取输入文件: {INPUT_CSV}")
    rows: list[dict[str, str]] = []
    with open(INPUT_CSV, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    logger.info(f"  原始数据集数量: {len(rows)}")

    # === Step 1: 物种过滤 ===
    allowedSpecies = {"Homo sapiens", "Mus musculus"}
    speciesFiltered = []
    speciesExcluded = []
    for row in rows:
        species = row.get("species", "")
        # 有些是多物种组合如 "Homo sapiens; Mus musculus"
        speciesSet = {s.strip() for s in species.split(";")}
        if speciesSet & allowedSpecies:
            speciesFiltered.append(row)
        else:
            speciesExcluded.append(row)
    logger.info(f"  物种过滤后: {len(speciesFiltered)} 套 (排除 {len(speciesExcluded)} 套)")

    # === Step 2: 排除空间转录组 ===
    techFiltered = []
    spatialExcluded = []
    for row in speciesFiltered:
        assay = row.get("assay", "")
        if isSpatialAssay(assay):
            spatialExcluded.append(row)
        else:
            techFiltered.append(row)
    logger.info(f"  排除空间转录组后: {len(techFiltered)} 套 (排除 {len(spatialExcluded)} 套)")

    # === Step 3: 四层细胞类型映射 ===
    tierMapped = []
    noTierMatch = []
    for row in techFiltered:
        matchedCells = row.get("matched_cell_types", "")
        tiersFound = mapCellTypesToTiers(matchedCells)
        row["_tiers"] = tiersFound
        row["_tier_1"] = "; ".join(tiersFound[1]) if tiersFound[1] else ""
        row["_tier_2"] = "; ".join(tiersFound[2]) if tiersFound[2] else ""
        row["_tier_3"] = "; ".join(tiersFound[3]) if tiersFound[3] else ""
        row["_tier_4"] = "; ".join(tiersFound[4]) if tiersFound[4] else ""
        row["_tier_count"] = sum(1 for v in tiersFound.values() if v)

        if hasTierMatch(tiersFound):
            tierMapped.append(row)
        else:
            noTierMatch.append(row)
    logger.info(f"  四层分类匹配后: {len(tierMapped)} 套 (无匹配 {len(noTierMatch)} 套)")

    # === Step 4: Collection 去重（选细胞数最多的 dataset） ===
    collectionGroups: dict[str, list[dict]] = defaultdict(list)
    for row in tierMapped:
        collId = row.get("collection_id", "unknown")
        collectionGroups[collId].append(row)

    deduped: list[dict] = []
    dedupedLog: list[dict] = []
    for collId, datasets in collectionGroups.items():
        if len(datasets) == 1:
            deduped.append(datasets[0])
            continue

        # 选细胞数最多的
        def getCellCount(r: dict) -> int:
            try:
                return int(r.get("cell_count", "0"))
            except (ValueError, TypeError):
                return 0

        # 同时考虑四层覆盖度作为次要排序条件
        datasets.sort(
            key=lambda r: (r.get("_tier_count", 0), getCellCount(r)),
            reverse=True,
        )
        best = datasets[0]
        deduped.append(best)

        if len(datasets) > 1:
            dedupedLog.append({
                "collection_id": collId,
                "collection_name": best.get("collection_name", ""),
                "total_datasets": len(datasets),
                "selected_dataset_id": best.get("dataset_id", ""),
                "selected_cell_count": getCellCount(best),
                "dropped_dataset_ids": "; ".join(
                    d.get("dataset_id", "") for d in datasets[1:]
                ),
            })

    logger.info(
        f"  Collection 去重后: {len(deduped)} 套 "
        f"(从 {len(collectionGroups)} 个 collection 中去重)"
    )

    # === 统计汇总 ===
    logger.info("\n" + "=" * 60)
    logger.info("筛选结果统计")
    logger.info("=" * 60)

    # 物种分布
    speciesDist: dict[str, int] = defaultdict(int)
    for row in deduped:
        speciesDist[row.get("species", "unknown")] += 1
    logger.info(f"\n物种分布:")
    for sp, cnt in sorted(speciesDist.items(), key=lambda x: -x[1]):
        logger.info(f"  {sp}: {cnt}")

    # 技术分布
    assayDist: dict[str, int] = defaultdict(int)
    for row in deduped:
        assayDist[row.get("assay", "unknown")] += 1
    logger.info(f"\n测序技术分布:")
    for assay, cnt in sorted(assayDist.items(), key=lambda x: -x[1]):
        logger.info(f"  {assay}: {cnt}")

    # 四层覆盖统计
    tierStats = {1: 0, 2: 0, 3: 0, 4: 0}
    for row in deduped:
        for tier in range(1, 5):
            if row[f"_tier_{tier}"]:
                tierStats[tier] += 1
    tierNames = {1: "真正神经元", 2: "神经胶质", 3: "神经相关基质", 4: "神经内分泌"}
    logger.info(f"\n四层分类覆盖:")
    for tier, cnt in tierStats.items():
        logger.info(f"  Tier {tier} ({tierNames[tier]}): {cnt} 套")

    # 细胞数统计
    totalCells = sum(
        int(r.get("cell_count", "0"))
        for r in deduped
        if r.get("cell_count", "").isdigit()
    )
    logger.info(f"\n总细胞数: {totalCells:,}")

    # 组织分布 Top 15
    tissueDist: dict[str, int] = defaultdict(int)
    for row in deduped:
        tissues = row.get("tissue", "").split("|")
        for t in tissues:
            t = t.strip()
            if t:
                tissueDist[t] += 1
    logger.info(f"\n组织分布 Top 15:")
    for tissue, cnt in sorted(tissueDist.items(), key=lambda x: -x[1])[:15]:
        logger.info(f"  {tissue}: {cnt}")

    # === Step 5: 存储估算（可选） ===
    if args.estimate_size:
        logger.info("\n" + "=" * 60)
        logger.info("存储大小估算（通过 HTTP HEAD 请求）")
        logger.info("=" * 60)

        urls = []
        urlToDataset: dict[str, dict] = {}
        for row in deduped:
            assetUrl = row.get("assets", "").strip()
            if assetUrl and assetUrl.startswith("http"):
                urls.append(assetUrl)
                urlToDataset[assetUrl] = row

        logger.info(f"  需要查询 {len(urls)} 个 h5ad 文件...")
        sizeResults = estimateFileSizes(urls, timeout=args.head_timeout)

        # 汇总
        knownSizes: list[tuple[str, int, dict]] = []
        unknownCount = 0
        for url, size in sizeResults.items():
            ds = urlToDataset.get(url, {})
            if size is not None:
                knownSizes.append((url, size, ds))
            else:
                unknownCount += 1

        knownSizes.sort(key=lambda x: -x[1])

        totalKnownBytes = sum(s for _, s, _ in knownSizes)

        logger.info(f"\n  已知大小的文件: {len(knownSizes)} 个")
        logger.info(f"  未知大小的文件: {unknownCount} 个")
        logger.info(f"  已知文件总大小: {formatBytes(totalKnownBytes)}")

        if unknownCount > 0 and len(knownSizes) > 0:
            avgSize = totalKnownBytes / len(knownSizes)
            estimatedTotal = totalKnownBytes + unknownCount * avgSize
            logger.info(
                f"  估算总大小（含未知）: ~{formatBytes(int(estimatedTotal))}"
            )

        # 按大小排序输出 Top 20
        logger.info(f"\n  最大的 20 个文件:")
        for url, size, ds in knownSizes[:20]:
            dsId = ds.get("dataset_id", "?")
            collName = ds.get("collection_name", "?")[:50]
            logger.info(f"    {formatBytes(size):>10}  {dsId}  {collName}")

        # 把大小信息写回 deduped
        for row in deduped:
            assetUrl = row.get("assets", "").strip()
            if assetUrl in sizeResults and sizeResults[assetUrl] is not None:
                row["_file_size_bytes"] = sizeResults[assetUrl]
                row["_file_size_human"] = formatBytes(sizeResults[assetUrl])
            else:
                row["_file_size_bytes"] = ""
                row["_file_size_human"] = "未知"

    # === 输出结果 ===
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 1. 筛选后的完整数据集
    outputCols = [
        "collection_id", "collection_name", "doi", "dataset_id",
        "cell_count", "species", "tissue", "disease", "assay", "suspension",
        "matched_cell_types", "all_cell_types",
        "_tier_1", "_tier_2", "_tier_3", "_tier_4", "_tier_count",
        "assets", "collection_url",
    ]
    if args.estimate_size:
        outputCols.extend(["_file_size_bytes", "_file_size_human"])

    outputPath = OUTPUT_DIR / "filtered_datasets.csv"
    with open(outputPath, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=outputCols, extrasaction="ignore")
        writer.writeheader()
        # 按 tier_count 降序 → cell_count 降序排序
        deduped.sort(
            key=lambda r: (
                r.get("_tier_count", 0),
                int(r.get("cell_count", "0")) if r.get("cell_count", "").isdigit() else 0,
            ),
            reverse=True,
        )
        writer.writerows(deduped)
    logger.info(f"\n✅ 筛选结果已保存到: {outputPath}")

    # 2. 排除清单
    excludedPath = OUTPUT_DIR / "excluded_datasets.csv"
    excludedRows = []
    for row in speciesExcluded:
        row["_exclude_reason"] = "物种不符（非 human/mouse）"
        excludedRows.append(row)
    for row in spatialExcluded:
        row["_exclude_reason"] = "空间转录组数据"
        excludedRows.append(row)
    for row in noTierMatch:
        row["_exclude_reason"] = "无四层分类匹配"
        excludedRows.append(row)

    excludedCols = [
        "dataset_id", "collection_name", "species", "assay",
        "matched_cell_types", "_exclude_reason",
    ]
    with open(excludedPath, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=excludedCols, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(excludedRows)
    logger.info(f"✅ 排除清单已保存到: {excludedPath}")

    # 3. 去重日志
    if dedupedLog:
        dedupLogPath = OUTPUT_DIR / "dedup_log.csv"
        with open(dedupLogPath, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=list(dedupedLog[0].keys()))
            writer.writeheader()
            writer.writerows(dedupedLog)
        logger.info(f"✅ 去重日志已保存到: {dedupLogPath}")

    # 4. 汇总报告
    reportPath = OUTPUT_DIR / "filter_report.md"
    with open(reportPath, "w", encoding="utf-8") as f:
        f.write("# CellxGene 外周神经数据集筛选报告\n\n")
        f.write(f"- 原始数据集: {len(rows)} 套\n")
        f.write(f"- 物种过滤后: {len(speciesFiltered)} 套 (排除 {len(speciesExcluded)})\n")
        f.write(f"- 排除空间转录组后: {len(techFiltered)} 套 (排除 {len(spatialExcluded)})\n")
        f.write(f"- 四层分类匹配后: {len(tierMapped)} 套 (无匹配 {len(noTierMatch)})\n")
        f.write(f"- Collection 去重后: **{len(deduped)} 套**\n\n")

        f.write("## 四层分类覆盖\n\n")
        f.write("| 层级 | 名称 | 数据集数 |\n")
        f.write("|------|------|----------|\n")
        for tier, cnt in tierStats.items():
            f.write(f"| Tier {tier} | {tierNames[tier]} | {cnt} |\n")

        f.write(f"\n## 物种分布\n\n")
        for sp, cnt in sorted(speciesDist.items(), key=lambda x: -x[1]):
            f.write(f"- {sp}: {cnt}\n")

        f.write(f"\n## 总细胞数\n\n{totalCells:,}\n")

        if args.estimate_size and knownSizes:
            f.write(f"\n## 存储估算\n\n")
            f.write(f"- 已知大小文件: {len(knownSizes)} 个\n")
            f.write(f"- 已知文件总大小: {formatBytes(totalKnownBytes)}\n")
            if unknownCount > 0:
                avgSize = totalKnownBytes / len(knownSizes)
                estimatedTotal = totalKnownBytes + unknownCount * avgSize
                f.write(
                    f"- 估算总大小（含未知）: ~{formatBytes(int(estimatedTotal))}\n"
                )

    logger.info(f"✅ 筛选报告已保存到: {reportPath}")
    logger.info("\n完成！")


if __name__ == "__main__":
    main()
