#!/usr/bin/env python3
"""Resumable OCR of Udvash MCQ page ranges (column-split + Tesseract ben+eng).

Usage (repo root):
  python tools/question_bank/udvash_extract/extract_ocr.py --paper physics:1
  python tools/question_bank/udvash_extract/extract_ocr.py --paper physics:1 --chapter 1
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ocr_page import ocr_tesseract  # noqa: E402
from preprocess import render_page, save_columns  # noqa: E402
from registry import pdf_path, paper_raw_dir  # noqa: E402

HERE = Path(__file__).resolve().parent


def load_ranges(subject: str, paper: int) -> dict:
    from registry import ranges_file
    aliases = {
        ("physics", 1): HERE / "phy1_ranges.json",
        ("physics", 2): HERE / "physics_2_ranges.json",
    }
    path = aliases.get((subject, paper), ranges_file(subject, paper))
    if not path.exists():
        raise FileNotFoundError(f"No MCQ range file for {subject} paper {paper}: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def effective_offset(cfg: dict, printed: int) -> int:
    """PDF page = printed + offset (+ optional bump after a printed threshold)."""
    offset = int(cfg["printed_to_pdf_offset"])
    bump_after = cfg.get("offset_bump_after_printed")
    if bump_after is not None and printed > int(bump_after):
        offset += int(cfg.get("offset_bump", 1))
    return offset


def ocr_printed_page(pdf: Path, printed: int, offset: int, out_dir: Path, dpi: int = 300) -> Path:
    pdf_page = printed + offset
    stem = f"p{printed:03d}_pdf{pdf_page:03d}"
    txt_path = out_dir / f"{stem}.txt"
    if txt_path.exists() and txt_path.stat().st_size > 50:
        return txt_path
    img = render_page(pdf, pdf_page, dpi=dpi)
    cols_dir = out_dir / "cols"
    left, right = save_columns(img, cols_dir, stem)
    parts = []
    for col_path, label in ((left, "L"), (right, "R")):
        col_txt = col_path.with_suffix(".txt")
        if col_txt.exists() and col_txt.stat().st_size > 50:
            text = col_txt.read_text(encoding="utf-8", errors="replace")
        else:
            text = ocr_tesseract(col_path, col_txt)
        parts.append(f"===== COL {label} =====\n" + text)
    txt_path.write_text("\n\n".join(parts), encoding="utf-8")
    return txt_path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper", required=True, help="subject:paper e.g. physics:1")
    ap.add_argument("--chapter", type=int, default=None)
    ap.add_argument("--dpi", type=int, default=300)
    args = ap.parse_args()
    subject, paper_s = args.paper.split(":")
    paper = int(paper_s)
    cfg = load_ranges(subject, paper)
    pdf = pdf_path(subject, paper)
    out_dir = paper_raw_dir(subject, paper) / "ocr"
    out_dir.mkdir(parents=True, exist_ok=True)
    chapters = cfg["chapters"]
    if args.chapter is not None:
        chapters = [c for c in chapters if c["chapter"] == args.chapter]
    for ch in chapters:
        start, end = ch["mcq_printed"]
        print(f"Chapter {ch['chapter']}: printed {start}-{end}")
        for printed in range(start, end + 1):
            offset = effective_offset(cfg, printed)
            path = ocr_printed_page(pdf, printed, offset, out_dir / f"ch{ch['chapter']:02d}", args.dpi)
            print(f"  OCR {path.relative_to(out_dir.parent)}")
    print("done")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
