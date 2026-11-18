# PorikkhaDao content (Phase 0)

- `syllabus/` — canonical chapter/topic trees (BN + EN labels)
- `templates/questions_import.csv` — import header template
- `pilot/` — original test-only MCQs (not the final archive)
- `db/porikkhadao.sqlite` — local question bank (created by tools)

Import tooling lives in `tools/question_bank/`.

## HSC 2027 content work

See `coverage_2027.csv` for the current paper register: ICT (single paper), and Physics, Chemistry, Biology, and Higher Mathematics 1st/2nd. English and other subjects are excluded from the current run. `2027_SOURCE_AND_STATUS.md` records source provenance and review gates. The chapter/topic trees are provisional. The `pilot/` CSV and unversioned Physics 2nd Paper JSON remain Phase 0 test data.

## Bulk question archive (current pipeline)

The bulk MCQ archive is built and loaded by the pipeline documented in
[`content/bank/PIPELINE.md`](bank/PIPELINE.md). Source of truth is the per-topic
checkpoint files under `content/bank/topics/`; everything else is derived.

```bash
python tools/question_bank/pipeline/bank.py status     # coverage
python tools/question_bank/pipeline/bank.py validate   # structural + bilingual + de-dup
python tools/question_bank/pipeline/bank.py export      # CSV + bank.json + manifest.json
python tools/question_bank/pipeline/bank.py import      # into app DB, verified=1
```

Outputs land in `content/bank/import/*.csv` (app import template),
`content/bank/bank.json`, and `content/bank/manifest.json`.

### Udvash PDFs

Redistribution rights confirmed — see `CONTENT_RIGHTS.md`. Extract tooling:
`tools/question_bank/udvash_extract/`. Raw OCR: `content/bank/udvash_raw/`.
Curated bilingual records still go to `content/bank/topics/*.jsonl`.
