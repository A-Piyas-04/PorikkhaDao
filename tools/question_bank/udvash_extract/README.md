# Udvash PDF extract

Licensed redistribution confirmed — see `content/CONTENT_RIGHTS.md`.

PDFs are image-only scans. Pipeline:

1. `extract_ocr.py` — render pages, split columns, Tesseract `ben+eng`
2. `parse_mcqs.py` — heuristic MCQ + answer-key parse
3. `to_bank.py` — topic tagging → `content/bank/topics/*.jsonl`

Range maps (printed page → PDF page via offset) live beside this folder,
e.g. `phy1_ranges.json`. Add one per paper as TOC is indexed.

OCR quality varies; prefer curated bilingual JSONL for launch topics, keep
raw OCR as the archive checkpoint.
