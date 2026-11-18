#!/usr/bin/env python3
"""Run EasyOCR over a directory of PNGs (avoids PowerShell quoting issues)."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import easyocr
from PIL import Image
import numpy as np


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in-dir", type=Path, required=True)
    ap.add_argument("--out-dir", type=Path, required=True)
    ap.add_argument("--scale", type=float, default=2.0)
    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    reader = easyocr.Reader(["bn", "en"], gpu=False)
    pngs = sorted(args.in_dir.glob("*.png"))
    print(f"images={len(pngs)}")
    for png in pngs:
        im = Image.open(png).convert("RGB")
        if args.scale != 1.0:
            im = im.resize((int(im.width * args.scale), int(im.height * args.scale)))
        arr = np.array(im)
        lines = reader.readtext(arr, detail=0, paragraph=True)
        stem = png.stem
        (args.out_dir / f"{stem}.txt").write_text("\n".join(lines), encoding="utf-8")
        (args.out_dir / f"{stem}.json").write_text(
            json.dumps(lines, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print("ok", stem, "blocks", len(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
