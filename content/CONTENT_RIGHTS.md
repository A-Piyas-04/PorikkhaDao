# Content rights — Udvash PDFs

The scanned question-bank PDFs under `question-bank-pdfs/` are Udvash
Academic publications. The project owner confirmed redistribution rights for
use in PorikkhaDao (2026-11-18).

## Extraction path

```bash
# 1) OCR MCQ page ranges (resumable, column-split + Tesseract ben+eng)
python tools/question_bank/udvash_extract/extract_ocr.py --paper physics:1
python tools/question_bank/udvash_extract/extract_ocr.py --paper physics:1 --chapter 1

# 2) Parse OCR text → structured JSON
python tools/question_bank/udvash_extract/parse_mcqs.py \
  --ocr-dir content/bank/udvash_raw/physics_1/ocr/ch01 \
  --out content/bank/udvash_raw/physics_1/parsed/ch01.json

# 3) Map into topic JSONL / CSV (verified=false until key review)
python tools/question_bank/udvash_extract/to_bank.py \
  --parsed content/bank/udvash_raw/physics_1/parsed/ch01.json \
  --subject physics --paper 1 --chapter 1 --per-topic 20
```

Raw OCR lands in `content/bank/udvash_raw/`. Authored/curated bilingual
records still live in `content/bank/topics/<topic_id>.jsonl`.

Extracted MCQs must carry `source` provenance such as:

`Udvash HSC Question Bank 2026; licensed redistribution; physics p1 ch01`

Do not mark rows `verified=true` until answer keys are checked against the
PDF answer grid / explanation block. Dense two-column scans need curation
when OCR garbles Bangla stems.
