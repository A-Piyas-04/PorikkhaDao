# Phase 4 — Content deliverables (what to give)

You collect the questions. We import them into PorikkhaDao.  
Hand over **syllabus JSON** + **question CSV/Excel** only. Raw screenshots/PDFs alone are not enough unless you also fill the CSV.

## 1. Syllabus files (JSON)

**Location:** `content/syllabus/`  
**Pattern:** one file per subject + paper  
**Example:** `physics_2nd_paper.json`

Each file must include:

- `curriculum_version` (string)
- `subject`: `id`, `name_en`, `name_bn`
- `paper`: `number` (1 or 2), `name_en`, `name_bn`
- `chapters[]`: `id`, `number`, `title_en`, `title_bn`
- `topics[]` under each chapter: `id`, `order`, `title_en`, `title_bn`

**Topic `id` rules:** stable, unique, ASCII, e.g. `phy2_ch03_t02`.  
Questions will reference these ids. Do not rename ids after questions are tagged.

Copy the structure of `content/syllabus/physics_2nd_paper.json` for new papers.

## 2. Question files (CSV preferred, Excel OK)

**Template headers:** `content/templates/questions_import.csv`

```text
stem,option_a,option_b,option_c,option_d,correct,topic_ids,difficulty,type,source,verified,explanation
```

### Required columns

| Column | Rule |
|---|---|
| `stem` | Full question text (BN and/or EN is fine) |
| `option_a` … `option_d` | Exactly four options, all non-empty |
| `correct` | Only `A`, `B`, `C`, or `D` |
| `topic_ids` | Syllabus topic id. Multi-topic: `id1;id2` |
| `source` | Provenance, e.g. `Dhaka Board 2023`, `original`, `site-name` |
| `verified` | `true` only if you checked the answer; else `false` |

### Optional columns

| Column | Allowed values (or blank) |
|---|---|
| `difficulty` | `easy` / `medium` / `hard` |
| `type` | `factual` / `conceptual` / `numerical` / `application` |
| `explanation` | Short note (optional) |

### Example row

```csv
stem,option_a,option_b,option_c,option_d,correct,topic_ids,difficulty,type,source,verified,explanation
"SI unit of temperature is:","Celsius","Fahrenheit","Kelvin","Calorie","C","phy2_ch01_t01","easy","factual","original",true,""
```

## 3. Suggested folder layout

```text
content/
  syllabus/
    physics_1st_paper.json
    physics_2nd_paper.json
    chemistry_1st_paper.json
    ...
  import/
    physics_2nd_ch01.csv
    physics_2nd_ch02.csv
    chemistry_1st_ch01.csv
    ...
  templates/
    questions_import.csv
```

Prefer **one CSV per chapter** (easier to review). UTF-8 encoding for Bangla.

## 4. Quality checklist (before you send)

- [ ] Every `topic_ids` value exists in the matching syllabus JSON
- [ ] `correct` is A/B/C/D only
- [ ] No blank stem or blank options
- [ ] `verified=true` only for checked keys
- [ ] `source` filled on every row
- [ ] Rights: you may use the content (original / permitted / not a scraped competitor dump)
- [ ] Duplicates removed when obvious

## 5. What NOT to send as the only deliverable

- Unstructured PDF/Word dumps with no CSV
- Images/screenshots without typed text + answer key
- Questions without topic tags
- Questions with wrong or unknown answers marked `verified=true`

PDFs can be **working notes**; the CSV is what we import.

## 6. After you deliver

We will:

1. Seed syllabus JSON into SQLite  
2. `validate` → `import` via `tools/question_bank/cli.py`  
3. Confirm eligible counts per topic in the tutor Create Exam UI  

## 7. Minimum useful first batch (recommended)

If “all HSC” takes time, send in waves:

1. Complete **one full paper** syllabus JSON (all chapters/topics)  
2. CSVs for that paper, chapter by chapter  
3. Then next subject/paper  

That keeps the app usable while the archive grows.
