#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""07_scripts 端到端测试（stdlib unittest + subprocess，零第三方依赖）。

运行：
  python design/07_scripts/tests/test_scripts.py
  # 或
  python -m unittest discover -s design/07_scripts/tests

覆盖：
  - validate.py：合法 JSON 通过；非法物种 / 非法 provenance 被拦截
  - ingest.py：入库计数正确、SQLite 外键无违例、再入库幂等
  - stats.py：生成 index.md
"""
from __future__ import annotations

import os
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parent
FIX = HERE / "fixtures"
ENV = {**os.environ, "PYTHONIOENCODING": "utf-8"}


def run(script: str, *args: object) -> subprocess.CompletedProcess:
    """以子进程方式运行 07_scripts 下的脚本，返回 CompletedProcess。"""
    cmd = [sys.executable, str(SCRIPTS / script), *[str(a) for a in args]]
    return subprocess.run(cmd, capture_output=True, text=True,
                          encoding="utf-8", env=ENV)


class TestValidate(unittest.TestCase):
    def test_valid_passes(self) -> None:
        r = run("validate.py", FIX / "valid.json")
        self.assertEqual(r.returncode, 0, msg=r.stdout + r.stderr)
        self.assertIn("PASS", r.stdout)

    def test_bad_species_fails(self) -> None:
        r = run("validate.py", FIX / "invalid_species.json")
        self.assertEqual(r.returncode, 1)
        self.assertIn("物种", r.stdout)

    def test_bad_provenance_fails(self) -> None:
        r = run("validate.py", FIX / "invalid_provenance.json")
        self.assertEqual(r.returncode, 1)
        self.assertIn("provenance", r.stdout)

    def test_unknown_field_fails(self) -> None:
        # 字段名笔误（marker/cell_count 而非 markers/n_cells_or_pct）必须被拦截，
        # 否则入库脚本会按契约字段取值取不到 → 数据静默丢失（历史 bug）。
        r = run("validate.py", FIX / "invalid_unknown_field.json")
        self.assertEqual(r.returncode, 1)
        self.assertIn("markers", r.stdout)
        self.assertIn("n_cells_or_pct", r.stdout)

    def test_nested_delimiter_fails(self) -> None:
        # 分号既作字段级多值分隔符，又被嵌进括号内部（如 time_series(0d;1d;3d;7d)
        # 或 doublet_removal(a=1;b=2)）会被 stats.py 按 ; 拆碎，污染分面统计（历史 bug）。
        # condition 与 qc 两类字段都必须被拦截，括号内多值应改用 '/'。
        r = run("validate.py", FIX / "invalid_nested_delimiter.json")
        self.assertEqual(r.returncode, 1)
        self.assertIn("括号", r.stdout)

    def test_valid_enrichment_passes(self) -> None:
        # enrichment 是新增的 processing 自由文本多值字段；合法值（如 GO(Metascape)）
        # 不应被「未知字段」误拦。本断言由 valid.json 含 enrichment 隐式覆盖，此处显式记录意图。
        r = run("validate.py", FIX / "valid.json")
        self.assertEqual(r.returncode, 0, msg=r.stdout + r.stderr)
        self.assertNotIn("enrichment", r.stdout)

    def test_enrichment_nested_delimiter_fails(self) -> None:
        # enrichment 括号内并列须用 '/' 不能用 ';'（GO(a;b) 会被 stats 按 ; 拆碎）。
        # 必须被 check_no_nested_delimiter 拦截。
        r = run("validate.py", FIX / "invalid_enrichment.json")
        self.assertEqual(r.returncode, 1)
        self.assertIn("括号", r.stdout)


class TestIngest(unittest.TestCase):
    def test_ingest_idempotent_and_fk(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "db"
            r1 = run("ingest.py", "--db", db, "--json", FIX / "valid.json",
                     "--paper-id", "P0001", "--paper-meta", FIX / "paper_meta.json")
            self.assertEqual(r1.returncode, 0, msg=r1.stdout + r1.stderr)

            conn = sqlite3.connect(str(db / "database.sqlite"))
            n1 = conn.execute("select count(*) from cell_types").fetchone()[0]
            fk = conn.execute("pragma foreign_key_check").fetchall()
            conn.close()
            self.assertEqual(n1, 2, "应入库 2 条 cell_types")
            self.assertEqual(fk, [], "不应有外键违例")

            # 幂等：再入库一次，cell_types 数量不变
            r2 = run("ingest.py", "--db", db, "--json", FIX / "valid.json",
                     "--paper-id", "P0001")
            self.assertEqual(r2.returncode, 0, msg=r2.stdout + r2.stderr)
            conn = sqlite3.connect(str(db / "database.sqlite"))
            n2 = conn.execute("select count(*) from cell_types").fetchone()[0]
            conn.close()
            self.assertEqual(n1, n2, "re-ingest 应幂等（cell_types 不翻倍）")

    def test_cell_subtypes_ingested(self) -> None:
        # 第 5 张表 cell_subtypes：valid.json 含 1 个施万亚群，应入库 1 行且无外键违例。
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "db"
            r = run("ingest.py", "--db", db, "--json", FIX / "valid.json",
                    "--paper-id", "P0001", "--paper-meta", FIX / "paper_meta.json")
            self.assertEqual(r.returncode, 0, msg=r.stdout + r.stderr)
            conn = sqlite3.connect(str(db / "database.sqlite"))
            n = conn.execute("select count(*) from cell_subtypes").fetchone()[0]
            fk = conn.execute("pragma foreign_key_check").fetchall()
            conn.close()
            self.assertEqual(n, 1, "应入库 1 条 cell_subtypes")
            self.assertEqual(fk, [], "cell_subtypes 不应有外键违例")

    def test_paper_id_backfilled(self) -> None:
        # cell_types / cell_subtypes 的 paper_id 由 ingest --paper-id 回填（不在 JSON）。
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "db"
            run("ingest.py", "--db", db, "--json", FIX / "valid.json",
                "--paper-id", "P0001", "--paper-meta", FIX / "paper_meta.json")
            conn = sqlite3.connect(str(db / "database.sqlite"))
            ct_pid = conn.execute("select distinct paper_id from cell_types").fetchall()
            cst_pid = conn.execute("select distinct paper_id from cell_subtypes").fetchall()
            conn.close()
            self.assertEqual(ct_pid, [("P0001",)], "cell_types.paper_id 应回填 P0001")
            self.assertEqual(cst_pid, [("P0001",)], "cell_subtypes.paper_id 应回填 P0001")

    def test_stats_generates_index(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "db"
            run("ingest.py", "--db", db, "--json", FIX / "valid.json",
                "--paper-id", "P0001", "--paper-meta", FIX / "paper_meta.json")
            out = Path(td) / "index.md"
            r = run("stats.py", "--db", db, "--out", out)
            self.assertEqual(r.returncode, 0, msg=r.stdout + r.stderr)
            self.assertTrue(out.exists(), "应生成 index.md")


if __name__ == "__main__":
    unittest.main(verbosity=2)
