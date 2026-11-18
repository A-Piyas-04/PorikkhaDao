"""Map local Udvash PDF filenames to syllabus papers."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PDF_DIR = ROOT / "question-bank-pdfs"
RAW_DIR = ROOT / "content" / "bank" / "udvash_raw"

# subject_id, paper_number, preferred PDF filename (exact match under PDF_DIR)
PAPER_PDFS: list[tuple[str, int, str]] = [
    ("physics", 1, "Physics 1st paper (1).pdf"),
    ("physics", 2, "Physics 2nd paper (1).pdf"),
    ("chemistry", 1, "Chemistry 1st paper (1).pdf"),
    ("chemistry", 2, "Chemistry 2nd paper (1).pdf"),
    ("biology", 1, "Biology 1st paper (1).pdf"),
    ("biology", 2, "Biology 2nd paper.pdf"),
    ("higher_mathematics", 1, "Math 1st paper (1).pdf"),
    ("higher_mathematics", 2, "Math 2nd Paper .pdf"),
]

# Serial order requested for bulk build
BUILD_ORDER: list[tuple[str, int]] = [
    ("physics", 2),
    ("biology", 1),
    ("biology", 2),
    ("chemistry", 1),
    ("chemistry", 2),
    ("higher_mathematics", 1),
    ("higher_mathematics", 2),
]

SOURCE_PREFIX = "Udvash HSC Question Bank 2026; licensed redistribution"


def pdf_path(subject: str, paper: int) -> Path:
    for s, p, name in PAPER_PDFS:
        if s == subject and p == paper:
            path = PDF_DIR / name
            if not path.exists():
                raise FileNotFoundError(path)
            return path
    raise KeyError(f"No PDF registered for {subject} paper {paper}")


def paper_raw_dir(subject: str, paper: int) -> Path:
    return RAW_DIR / f"{subject}_{paper}"


def ranges_file(subject: str, paper: int) -> Path:
    return Path(__file__).resolve().parent / f"{subject}_{paper}_ranges.json"
