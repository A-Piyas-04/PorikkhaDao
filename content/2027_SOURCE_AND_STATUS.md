# HSC 2027 content status

Current scope: HSC **science-group students only**: ICT (single paper), and Physics, Chemistry, Biology and Higher Mathematics 1st/2nd. English and other subjects are excluded from the current generator run. Questions need not be drawn from a 2027 paper; the NCTB curriculum remains the provisional scope reference.

The requested finished bank target is **30 original, checked MCQs per topic, with Bangla and English in each question and each option**. The single-language Physics CSV below is an earlier draft and does not meet that target yet.

This is a source and review record, not a claim that the 2027 bank is complete. As of 17 November 2026, I found NCTB higher secondary curriculum PDFs from the **2012 curriculum series** (rehosted on the current NCTB site), but no official 2027 exam-specific subject-by-subject syllabus notice. Treat these curricula as a provisional basis until the 2027 examination instructions are published and any updates are reconciled.

## Authoritative sources checked

- NCTB higher secondary Physics curriculum (hosted by NCTB; chapter table and learning outcomes): https://objectstorage.ap-dcc-gazipur-1.oraclecloud15.com/n/axvjbnqprylg/b/V2Ministry/o/office-nctb/2024/12/28d03c592c2c4b208f7782d04c78e01d.pdf
- NCTB higher secondary curriculum index (subject coverage): https://nctb.gov.bd/pages/files/6922dbc6933eb65569e0c702
- NCTB 2025–26 higher secondary textbook list: https://nctb.gov.bd/pages/static-pages/6922e145933eb65569e2b37b
- Dhaka Board HSC notices: https://dhakaeducationboard.gov.bd/index.php/site/product/hsccorner

## Existing repository content

- `content/syllabus/physics_2nd_paper.json` is a Phase 0 pilot with two chapters and topic assignments that do not fully match the NCTB Physics 2nd Paper curriculum. Do not ship it as a 2027 production syllabus.
- `content/pilot/physics_2nd_ch1_ch2.csv` is labelled `original-test` and is not a reviewed 2027 exam bank.

## Coverage register

`content/coverage_2027.csv` tracks **5 subjects and 9 papers**: ICT, Physics 1/2, Chemistry 1/2, Biology 1/2 and Higher Mathematics 1/2. The linked source index still contains Bangla and English curriculum PDFs as background research, but they are excluded from the register and generator. The register marks 2027 applicability as unconfirmed.

`content/sources/nctb_chapter_candidates.csv` contains 118 automatically extracted heading candidates from the seven science-group source PDFs. The legacy Bijoy text layer requires conversion; headings can be duplicated or malformed. Bangla and English curricula use a different structure and yielded no chapter headings through this extractor. This file is a review aid only.

Reproduce source extraction with `python -m pip install -r tools/question_bank/requirements-content.txt`, then `python tools/question_bank/discover_nctb_curricula.py` and `python tools/question_bank/extract_nctb_chapter_candidates.py`. The converter's output must be checked visually against each PDF before use.

In this NCTB list, Higher Mathematics is the named math subject; there is no separate general HSC Mathematics entry. ICT is one exam paper. The import schema requires a paper number of 1 or 2, so the ICT JSON uses number 1 and the display name `Single Paper`.

## Drafts created

- `content/syllabus/physics_2nd_paper_2027.json`: all 11 NCTB Physics 2nd Paper chapters and 68 editorial topic groups. The chapter titles follow the NCTB table; the topic boundaries are our grouping of NCTB learning outcomes and still need teacher review. Topic IDs use a separate `phy2_27_` namespace so the old pilot tags retain their meaning.
- `content/syllabus/physics_1st_paper_2027.json`: all ten NCTB Physics 1st Paper chapters with 41 provisional topic groups; source is the same NCTB Physics curriculum linked above.
- `content/import/physics_2nd_2027_ch01.csv`: 16 original English MCQs for Chapter 1. The answer keys and explanations were checked against the following primary educational references; the questions themselves are new wording, not copied questions:
  - OpenStax first law and internal energy: https://openstax.org/books/college-physics-2e/pages/15-1-the-first-law-of-thermodynamics
  - OpenStax reversible/irreversible processes and second law: https://openstax.org/books/university-physics-volume-2/pages/4-1-reversible-and-irreversible-processes
  - OpenStax Carnot cycle and efficiency: https://openstax.org/books/university-physics-volume-2/pages/4-5-the-carnot-cycle
  - OpenStax refrigerators: https://openstax.org/books/university-physics-volume-2/pages/4-3-refrigerators-and-heat-pumps
  - OpenStax entropy: https://openstax.org/books/university-physics-volume-2/pages/4-6-entropy
- `content/syllabus/ict_2027.json`: all six ICT chapters and 37 editorial topic groups, mapped from the [official NCTB ICT curriculum](https://objectstorage.ap-dcc-gazipur-1.oraclecloud15.com/n/axvjbnqprylg/b/V2Ministry/o/office-nctb/2024/12/687441001bc74e04819378e555a6ed8f.pdf). Its 2027 applicability and topic boundaries still need review. It has no MCQ CSV yet.
- `content/syllabus/higher_mathematics_1st_paper_2027.json` and `content/syllabus/higher_mathematics_2nd_paper_2027.json`: each has the ten chapters in the [official NCTB Higher Mathematics curriculum](https://objectstorage.ap-dcc-gazipur-1.oraclecloud15.com/n/axvjbnqprylg/b/V2Ministry/o/office-nctb/2024/12/9c44bb8ff649495698b093d3fe2b9f15.pdf), with 30 editorial topic groups per paper. The topic boundaries and 2027 applicability remain provisional. Neither paper has MCQ CSVs yet.
- `content/syllabus/chemistry_1st_paper_2027.json` and `content/syllabus/chemistry_2nd_paper_2027.json`: each has the five chapters in the [official NCTB Chemistry curriculum](https://objectstorage.ap-dcc-gazipur-1.oraclecloud15.com/n/axvjbnqprylg/b/V2Ministry/o/office-nctb/2024/12/a513203336f643b1b2630f4980537416.pdf), with 21 and 22 provisional topic groups respectively. Neither paper has MCQ CSVs yet.
- `content/syllabus/biology_1st_paper_2027.json` and `content/syllabus/biology_2nd_paper_2027.json`: each has the twelve chapters in the [official NCTB Biology curriculum](https://objectstorage.ap-dcc-gazipur-1.oraclecloud15.com/n/axvjbnqprylg/b/V2Ministry/o/office-nctb/2024/12/ca39e59575134a74b26a35b760d193eb.pdf), with 36 provisional topic groups each. Neither paper has MCQ CSVs yet.

Key check map for the 16 CSV rows (row numbers include the header):

| CSV lines | Check |
|---|---|
| 2–3 | Thermal equilibrium and temperature definition in NCTB Chapter 1; textbook thermometer principle |
| 4–5 | Internal energy as a state property and the definition of an isolated system |
| 6–8 | OpenStax first law, `ΔU = Q − W`; arithmetic checked as 300 J and −100 J |
| 9–10 | OpenStax second law and irreversible free expansion |
| 11–12 | OpenStax Carnot cycle; `1 − 300/600 = 0.5` |
| 13–15 | OpenStax heat engines and refrigerators; `200/800 = 0.25`, `600/200 = 3` |
| 16–17 | OpenStax entropy; `300/300 = 1 J/K`, isolated-system entropy does not decrease |

Run `python tools/question_bank/audit_deliverables.py content/syllabus/physics_2nd_paper_2027.json content/import/physics_2nd_2027_ch01.csv` for structural validation. This check covers tags, empty fields, duplicate stems and options, and allowed values; it cannot certify scientific correctness.

The nine in-scope provisional syllabus outlines contain 321 editorial topic groups. At **20 MCQs/topic** that is **6,420** bilingual questions. Author into `content/bank/topics/<topic_id>.jsonl`, then run `python tools/question_bank/pipeline/bank.py validate|export|import`. Do not bulk-import commercial coaching PDFs without redistribution rights.

## Release gate

For every paper: compare its complete chapter and topic hierarchy against the applicable official NCTB curriculum and any 2027 board changes. For every MCQ: inspect the original wording, each distractor, the answer key, the topic tag, and the explanation; retain a source or calculation record. `verified=true` should require a checked key, not simply a plausible generated answer. A subject teacher should sign off before student-facing publication.

Current production-ready syllabus files: **0** pending curriculum review. Current production-ready MCQs for the science group: **0** pending human key review. Nine provisional in-scope syllabus outlines exist. The pilot remains development-only.
