"""Render PDF pages and split two-column layouts for cleaner OCR."""
from __future__ import annotations

from pathlib import Path
import fitz
from PIL import Image


def render_page(pdf: Path, page_1based: int, dpi: int = 300) -> Image.Image:
    doc = fitz.open(pdf)
    page = doc[page_1based - 1]
    zoom = dpi / 72.0
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    doc.close()
    return img


def split_columns(img: Image.Image, gap_ratio: float = 0.02) -> tuple[Image.Image, Image.Image]:
    """Split roughly down the middle with a small gap discard."""
    w, h = img.size
    gap = int(w * gap_ratio)
    mid = w // 2
    left = img.crop((0, 0, mid - gap // 2, h))
    right = img.crop((mid + gap // 2, 0, w, h))
    return left, right


def save_columns(img: Image.Image, out_dir: Path, stem: str) -> tuple[Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    left, right = split_columns(img)
    lp = out_dir / f"{stem}_L.png"
    rp = out_dir / f"{stem}_R.png"
    left.save(lp)
    right.save(rp)
    return lp, rp
