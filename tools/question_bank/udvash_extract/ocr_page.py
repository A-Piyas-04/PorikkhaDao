"""OCR one rendered page with Tesseract (ben+eng) or EasyOCR."""
from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

DEFAULT_TESSDATA = Path(os.environ.get(
    "TESSDATA_PREFIX",
    Path.home() / "AppData" / "Local" / "tesseract" / "tessdata",
))


def find_tesseract() -> str:
    which = shutil.which("tesseract")
    if which:
        return which
    candidate = Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
    if candidate.exists():
        return str(candidate)
    raise FileNotFoundError("tesseract.exe not found")


def ocr_tesseract(image: Path, out_txt: Path, lang: str = "ben+eng", psm: int = 6) -> str:
    """OCR an image. Never raises — retries eng-only, then returns empty marker."""
    env = os.environ.copy()
    if DEFAULT_TESSDATA.exists():
        env["TESSDATA_PREFIX"] = str(DEFAULT_TESSDATA)
    out_base = out_txt.with_suffix("")
    tess = find_tesseract()
    attempts = [(lang, psm), ("eng", psm), ("eng", 3), ("eng", 4)]
    last_err = ""
    for attempt_lang, attempt_psm in attempts:
        try:
            proc = subprocess.run(
                [tess, str(image), str(out_base), "-l", attempt_lang, "--psm", str(attempt_psm)],
                check=False,
                env=env,
                capture_output=True,
                text=True,
                errors="replace",
                timeout=120,
            )
            if proc.returncode == 0 and out_txt.exists() and out_txt.stat().st_size > 0:
                return out_txt.read_text(encoding="utf-8", errors="replace")
            last_err = (proc.stderr or proc.stdout or f"exit {proc.returncode}")[:300]
        except Exception as exc:  # noqa: BLE001 — keep OCR pipeline alive
            last_err = str(exc)[:300]
            continue
    out_txt.write_text(f"[OCR_FAILED] {image.name}: {last_err}\n", encoding="utf-8")
    return ""


def ocr_easyocr(image: Path, reader=None) -> str:
    import easyocr
    if reader is None:
        reader = easyocr.Reader(["bn", "en"], gpu=False)
    lines = reader.readtext(str(image), detail=0, paragraph=False)
    return "\n".join(lines)
