#!/usr/bin/env python3
"""Render early PDF pages so we can locate TOC / MCQ printed-page ranges."""
from __future__ import annotations

import argparse
from pathlib import Path
import fitz

from registry import pdf_path, paper_raw_dir


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper", required=True, help="subject:paper e.g. physics:2")
    ap.add_argument("--start", type=int, default=1)
    ap.add_argument("--end", type=int, default=12)
    ap.add_argument("--dpi", type=int, default=150)
    args = ap.parse_args()
    subject, paper_s = args.paper.split(":")
    paper = int(paper_s)
    pdf = pdf_path(subject, paper)
    out = paper_raw_dir(subject, paper) / "toc"
    out.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf)
    zoom = args.dpi / 72.0
    for page_no in range(args.start, min(args.end, doc.page_count) + 1):
        pix = doc[page_no - 1].get_pixmap(matrix=fitz.Matrix(zoom, zoom))
        path = out / f"pdfp{page_no:03d}.png"
        pix.save(path)
        print(path.name)
    doc.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
