# PorikkhaDao (পরীক্ষাদাও) — Lean Development Plan

**Product name:** PorikkhaDao / পরীক্ষাদাও  
**Companion document:** `docs/project-context.md`  
**Strategy:** Question bank first; tutor-first exam workflow; responsive bilingual website; no AI API.  
**Languages:** Bangla and English, user-togglable.  
**Build principle:** Deliver one complete end-to-end tutor/student exam before expanding to every subject.

## 1. Stack (simple and sufficient)

| Layer | Choice | Reason |
|---|---|---|
| Frontend | Next.js + TypeScript + Tailwind CSS | One responsive web app for tutor and student |
| i18n | Bangla / English toggle | Product requirement for BD tutoring market |
| Authentication | Supabase Auth with Google OAuth (**after Phase 3**) | Deferred; Phases 0–3 do not require Supabase yet |
| Database (Phases 0–3) | Local SQLite question bank | Prove filters and exam flow before cloud setup |
| Database (after Phase 3) | Supabase PostgreSQL | Migrate relational bank + add RLS |
| Server logic | Next.js server routes/actions | Fewer services; server-side authorization, exam generation, scoring |
| Hosting | Vercel + Supabase (later) | Simple deployment; free tiers possible within limits |
| Content import | Small Python CLI: CSV/Excel first; permitted HTML/PDF later | Keep scrapers and parsers separate from production exam UI |

Avoid a separate FastAPI service unless a demonstrated requirement justifies it. Do not use Kafka, Redis queues, microservices, vector databases, or AI.

**Deferral:** Supabase authentication and database setup happen **after Phase 3**. Until then, use local SQLite for the question bank and keep auth/cloud wiring out of the critical path.

## 2. MVP pages

1. **Tutor: My Exams** — list exams, create exam, status, share link, view results.
2. **Tutor: Create Exam** — subject, paper, chapter, include/exclude topics, MCQ count, duration, optional difficulty/type filters; show eligible-question count.
3. **Tutor: Preview/Publish** — inspect selected MCQs and confirm publishing; copy URL.
4. **Tutor: Exam Results** — students, completion status, marks, correct/total, submission time.
5. **Student: Exam Landing** — exam title, duration, Google sign-in, Start button.
6. **Student: Attempt** — responsive question list/navigation, answer saving, countdown, Submit.
7. **Content admin (minimal)** — import CSV, inspect invalid records, verify questions. This may begin as a developer-only script rather than a polished page.

All user-facing copy supports Bangla and English via a language toggle.

## 3. Minimal data model

- `users` — auth user ID, display name, email, role (tutor/student; content admin handled separately)
- `subjects` — name_en, name_bn
- `papers` — subject ID, number (1/2)
- `chapters` — paper ID, chapter number/title_en/title_bn, curriculum/version
- `topics` — chapter ID, topic title_en/title_bn/order
- `questions` — stem, options, correct answer, difficulty, type, source, verification status
- `question_topics` — question ID ↔ topic ID (many-to-many)
- `exams` — tutor owner, title, duration, publication state, share token, settings
- `exam_questions` — exam ID, question ID, order, optional option shuffle mapping
- `attempts` — exam ID, student user ID, start, deadline, finalized time, status, score
- `answers` — attempt ID, exam question ID, selected option, last saved timestamp

**Constraints:** unique question in an exam; unique attempt per `(exam_id, student_id)` in MVP; one answer per `(attempt_id, exam_question_id)`; indexed foreign keys and filtering fields. After Phase 3 migration: Supabase RLS and server-side ownership checks.

## 4. Implementation phases

### Phase 0 — Confirm syllabus + prepare initial content

**Goal:** Have real questions to test filters and exam generation.

- Choose **one HSC subject, one paper, and 1–2 chapters**.
- Create the canonical chapter/topic tree using a known curriculum/version (BN + EN labels).
- Create a CSV import template containing question, A/B/C/D, answer, topic IDs, difficulty/type, source, verification flag.
- Collect a pilot batch (target **200–500 original test questions**); verify answers and topic tags.
- Run deduplication and data validation; reject missing answer, missing topic, invalid choices, or unverified records.
- Store in **local SQLite** (`content/db/porikkhadao.sqlite`).

**Done when:** The database can accurately retrieve questions by selected topics, and available counts are honest.

### Phase 1 — Tutor exam creation

**Goal:** Generate and publish a precise exam from the stored bank.

- Implement tutor authorization (local/dev auth acceptable until Supabase after Phase 3).
- Build syllabus selectors: subject → paper → chapter → **multi-select topics** (BN/EN labels).
- Include/exclude topic behavior: default include selected topics only; no accidental questions from excluded topics.
- Add question count, duration, and optional difficulty/type mix.
- Query verified eligible questions and show the eligible count before generation.
- Choose distinct questions using a straightforward randomized selection; record the chosen set so exams do not change later.
- Show preview, publish exam, generate random unguessable share token/URL.
- Language toggle wired for tutor UI strings.

**Done when:** A tutor can publish a test drawn only from allowed topics with no unsupported questions.

### Phase 2 — Student exam taking and timing

**Goal:** Students finish an exam from a link, with trustworthy scores.

- Shared URL loads a limited student landing page; sign-in is mandatory (Google via Supabase after Phase 3).
- First Start action creates the student's one permitted attempt and server deadline (`started_at + duration`).
- Build mobile-first MCQ UI with question navigation, progress indicator, and time remaining.
- Save each answer promptly; resuming after refresh uses the **same attempt and original deadline**.
- Manual Submit finalizes and grades on server.
- Deadline enforcement: **every read/write/submission checks server time**; expired attempts are finalized from stored answers. Add a scheduled server cleanup/finalizer if available so expired records are processed even when the student never reconnects.
- The browser countdown and auto-submit are helpful UX but **not the authority**.
- Do not deliver the correct answer key in student-facing question payloads.

**Done when:** Student A can answer, Student B can answer independently, refresh cannot reset time, and an expired attempt is scored using the saved answers.

### Phase 3 — Tutor results + deployment

**Goal:** Complete the tutor-to-student loop.

- Tutor-only results page: student name/email, attempt status, start/end, answered, correct, score.
- Prevent tutors from accessing other tutors' exam data and students from accessing others' results.
- Add clear empty/error states: no questions available, test not published, expired attempt, login required, already submitted.
- Deploy responsive site; verify on mobile-sized screens and a laptop.
- Test timezones (store UTC; display Bangladesh time) and timed expiration.

**Done when:** A tutor can send a link, students can complete the exam, and the tutor sees accurate marks without additional tools.

### After Phase 3 — Supabase Auth + Postgres

- Set up Supabase project, Google OAuth, migrate SQLite bank to Postgres, enable RLS.

### Phase 4 — Expand content and quality (after MVP)

- Add more subjects, both papers, chapters and subtopics.
- Build repeatable, **rights-compliant** content acquisition: CSV/Excel → source-specific parsers for authorized websites/digital PDFs → validation → review → publish.
- Improve duplicate detection, source tracking, topic-tag audit, and difficulty/type curation.
- Allow tutor to replace a selected question before publishing.
- Add student score visibility, question explanations, and simple topic-wise breakdown only if useful.
- Consider native app/PWA enhancements later; not required to ship.

## 5. Rules for question selection

1. Start with only verified questions from requested subject/paper/chapter(s).
2. Restrict matches to selected topics; **do not include questions tagged with excluded topics**. Cross-topic questions qualify only if all their topic tags are allowed (strict filter).
3. Apply explicitly chosen difficulty or type filters only when those tags are reviewed; avoid guessing missing tags.
4. If eligible questions are fewer than requested, display the actual count and ask the tutor to reduce count or broaden scope; never silently repeat questions.
5. Randomize eligible question selection and order; store that frozen set in `exam_questions`.
6. Score on the server: correct = 1, incorrect/unanswered = 0 in MVP. No negative marking unless added deliberately later.
7. Default one attempt per Google account per published exam; if retries are needed, design them as a separate feature.

## 6. Reliability and security checklist

- [ ] Only tutor owner can modify exam and view all its results.
- [ ] Only authenticated students with a valid exam link can start an attempt.
- [ ] A student cannot access the correct answers or edit another student's attempt.
- [ ] Duration is enforced with server timestamps; timer does not restart after refresh.
- [ ] Answers persist before deadline and scoring uses only stored answers.
- [ ] Expired attempts are finalized even without an active browser (scheduled or equivalent backend process).
- [ ] Answer updates after the deadline are rejected.
- [ ] Double-click/repeated submit cannot create duplicate attempts or scores.
- [ ] A tutor sees available question counts and failures to meet requested counts.
- [ ] The website works on narrow mobile screens as well as desktop.
- [ ] Imported MCQs have usable rights, sources, correct answers, and reviewed topic tags.
- [ ] Bangla/English toggle works on tutor and student surfaces.

## 7. Suggested development order (actual tickets)

1. Phase 0: syllabus topic IDs, CSV import format, SQLite seed, verified pilot questions, eligibility query.
2. Initialize Next.js app with BN/EN i18n toggle.
3. Implement question eligibility query and availability count against SQLite.
4. Implement tutor exam builder, preview and publish/share URL.
5. Implement student sign-in (dev), start, attempt and incremental answers.
6. Implement server-authoritative expiration/finalization and scoring.
7. Implement tutor results and ownership checks.
8. Run end-to-end tests on phone/desktop and deploy.
9. **After Phase 3:** Supabase Auth (Google OAuth) + migrate DB to Postgres + RLS.
10. Only then grow question-bank coverage and import tooling (Phase 4).

## 8. Decisions intentionally kept simple

- **Responsive web, not native Android/iOS.**
- **Bilingual BN/EN with a toggle.**
- **Google OAuth instead of custom password accounts** (wired after Phase 3 via Supabase).
- **One attempt per student per exam.**
- **Relative per-student timer**, starting at first Start action; no shared start/end schedule in MVP.
- **One point per correct MCQ, no negative marking.**
- **Bank selection, not real-time AI question generation.**
- **Difficulty/type metadata optional**, but never automatically assumed reliable.
- **Simple content import first**, no large-scale scraping system built into the app.
- **Local SQLite until after Phase 3**, then Supabase.

## 9. MVP acceptance scenario

A tutor signs in and builds a **Physics 2nd Paper** exam from **only 6 selected topics** of a chapter. The tutor requests **50 MCQs** and **30 minutes**, reviews and publishes, then shares the URL. Students sign in, start their individual timers, answer on mobile, and either submit or expire. All answers saved before expiry are scored. The tutor sees each student's name, completion status, and score. No AI service or Google Form is involved. UI can be used in Bangla or English.

If this scenario works reliably with a verified question bank, the MVP is complete.
