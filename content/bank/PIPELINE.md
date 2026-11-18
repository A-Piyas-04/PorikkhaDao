# PorikkhaDao question-bank pipeline

One clean, data-driven, resumable pipeline that produces the bulk MCQ archive
for the 5 science-group subjects and loads it into the app.

## Scope

5 subjects, 9 papers, 81 chapters, **321 topics** (no English in this run):

| Subject | Papers | Topics |
|---|---|---|
| ICT | single | 37 |
| Physics | 1st, 2nd | 41 + 68 |
| Chemistry | 1st, 2nd | 21 + 22 |
| Biology | 1st, 2nd | 36 + 36 |
| Higher Mathematics | 1st, 2nd | 30 + 30 |

Current target: **20 MCQs/topic (~6,420)**. Scale later if needed.
Every MCQ is bilingual (English + Bangla in stem, all four options, and
explanation) and ships `verified=1` so it is live in the app immediately.

Udvash PDFs are licensed for this product (see `content/CONTENT_RIGHTS.md`).
Use `tools/question_bank/udvash_extract/` for OCR → parse → topic JSONL.

## Source of truth

- **Syllabus:** `content/syllabus/<subject>_<paper>_paper_2027.json` (+ `ict_2027.json`).
  Chapter/topic trees, IDs locked. Provisional against the 2012-series NCTB
  curriculum until the 2027 board syllabus is confirmed.
- **Authored questions:** `content/bank/topics/<topic_id>.jsonl` — one JSON
  object per line. This is the durable, resumable checkpoint. Everything else
  is derived, so export/import are always safe to re-run.

### Authored record shape (one JSONL line)

```json
{"stem_en":"...","stem_bn":"...",
 "option_a_en":"...","option_a_bn":"...","option_b_en":"...","option_b_bn":"...",
 "option_c_en":"...","option_c_bn":"...","option_d_en":"...","option_d_bn":"...",
 "correct":"A|B|C|D","difficulty":"easy|medium|hard",
 "type":"factual|conceptual|numerical|application",
 "explanation_en":"...","explanation_bn":"..."}
```

## Workflow

Run from the repo root. Prefix Bangla-printing commands with
`PYTHONIOENCODING=utf-8` on Windows.

```bash
# 1. Coverage: authored vs target per paper, invalid/duplicate counts
python tools/question_bank/pipeline/bank.py status

# 2. Validate: structural + bilingual + global de-dup (non-zero exit on error)
python tools/question_bank/pipeline/bank.py validate

# 3. Export: per-chapter CSV (app import template) + bank.json + manifest.json
python tools/question_bank/pipeline/bank.py export

# 4. Import into the app SQLite bank with verified=1 (live in the app)
python tools/question_bank/pipeline/bank.py import

#    Clean launch DB (DESTRUCTIVE: clears bank + dev exams/attempts; keeps users):
python tools/question_bank/pipeline/bank.py import --reset-content
```

`--limit-per-topic N` on export/import caps how many are used per topic (e.g.
author 30 but ship 10 first). `--target N` tunes the "complete topic" threshold
in status/export reports.

## Validation gate (automatic)

`validate` rejects any record that is missing a field, has a bad key /
difficulty / type, lacks Bangla where required, lacks English in stem/options,
leaves an option untranslated, or has duplicate options. Global de-dup drops any
repeated stem across the whole bank. Only clean, unique records are exported or
imported.

## Outputs

- `content/bank/import/<subject>_<paper>_chNN.csv` — matches
  `content/templates/questions_import.csv`; integrable as CSV.
- `content/bank/bank.json` — single consolidated JSON of every question.
- `content/bank/manifest.json` — exact coverage counts.
- App bank: `content/db/porikkhadao.sqlite` (gitignored, regenerable) — what the
  web app reads.

## Authoring input

Write or append bilingual MCQs to `content/bank/topics/<topic_id>.jsonl`, then
`validate` → `export` → `import`. Scanned commercial question-bank PDFs are
reference material only unless you hold redistribution rights; they are not an
import source for this repo.
