# PorikkhaDao (পরীক্ষাদাও) — Lean Development Plan

**Product name:** PorikkhaDao / পরীক্ষাদাও  
**Companion document:** `docs/project-context.md`  
**Strategy:** Working exam product first; **full content bank before cloud deploy**; responsive bilingual website; no AI API.  
**Languages:** Bangla and English, user-togglable.  
**Build principle:** Deliver one complete end-to-end tutor/student exam (Phases 0–3), then grow the question bank (Phase 4), then auth + hosting (Phase 5).

**Status:** Phases **0–3 complete**. Next: **Phase 4 (content)**, then **Phase 5 (deploy)**.

## 1. Stack (simple and sufficient)

| Layer | Choice | Reason |
|---|---|---|
| Frontend | Next.js + TypeScript + Tailwind CSS | One responsive web app for tutor and student |
| i18n | Bangla / English toggle | Product requirement for BD tutoring market |
| Authentication (Phases 0–4) | Local session (tutor password; student name+email) | Prove product before cloud auth |
| Authentication (Phase 5) | Supabase Auth with Google OAuth | Production identity |
| Database (Phases 0–4) | Local SQLite question bank | Content work stays local and simple |
| Database (Phase 5) | Supabase PostgreSQL | Durable cloud data + RLS |
| Server logic | Next.js server routes/actions | Fewer services; server-side authorization, exam generation, scoring |
| Hosting (Phase 5) | Vercel + Supabase | Viable after Postgres migration (SQLite does not persist on Vercel) |
| Content import | Small Python CLI: CSV/Excel first; permitted HTML/PDF later | Keep acquisition separate from exam UI |

Avoid a separate FastAPI service unless a demonstrated requirement justifies it. Do not use Kafka, Redis queues, microservices, vector databases, or AI.

**Order rule:** Do **not** deploy to cloud until Phase 4 content is ready enough to ship. Supabase + Vercel are **Phase 5**.

## 2. MVP pages

1. **Tutor: My Exams** — list exams, create exam, status, share link, view results.
2. **Tutor: Create Exam** — subject, paper, chapter, include/exclude topics, MCQ count, duration, optional difficulty/type filters; show eligible-question count.
3. **Tutor: Preview/Publish** — inspect selected MCQs and confirm publishing; copy URL.
4. **Tutor: Exam Results** — students, completion status, marks, correct/total, submission time.
5. **Student: Exam Landing** — exam title, duration, identify / Start button.
6. **Student: Attempt** — responsive question list/navigation, answer saving, countdown, Submit.
7. **Content admin (minimal)** — import CSV, inspect invalid records, verify questions. Developer CLI first; polish later if needed.

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

**Constraints:** unique question in an exam; unique attempt per `(exam_id, student_id)` in MVP; one answer per `(attempt_id, exam_question_id)`; indexed foreign keys and filtering fields. Phase 5: Supabase RLS and server-side ownership checks.

## 4. Implementation phases

### Phase 0 — Confirm syllabus + prepare initial content — DONE

**Goal:** Have real questions to test filters and exam generation.

- One HSC subject, one paper, 1–2 chapters; CSV template; pilot MCQs; SQLite bank.

**Done when:** Topic-filtered retrieval and honest eligible counts work.

### Phase 1 — Tutor exam creation — DONE

**Goal:** Generate and publish a precise exam from the stored bank.

**Done when:** A tutor can publish a test drawn only from allowed topics.

### Phase 2 — Student exam taking and timing — DONE

**Goal:** Students finish an exam from a link, with trustworthy scores.

**Done when:** Independent attempts, refresh-safe deadline, expired attempts scored from saved answers.

### Phase 3 — Tutor results + local production readiness — DONE

**Goal:** Complete the tutor-to-student loop on a local production build.

- Tutor-only results page (name/email, status, marks, BD timezone display).
- Ownership checks and empty/error states.
- Local `next build` / `next start` verified; deploy notes for later cloud work.
- **Not** cloud/Vercel deploy (blocked on SQLite persistence).

**Done when:** Tutor sees accurate marks without extra tools; app runs in local production mode.

### Phase 4 — Full content generation (NEXT)

**Goal:** Make the question bank ready to ship **before** cloud deployment.

- Expand canonical syllabus trees (BN + EN) for the chosen coverage (e.g. Physics full paper → Science group → broader HSC as decided).
- Author or acquire **rights-compliant** MCQs at scale; tag to canonical topic IDs.
- Strengthen CSV/Excel import, validation, deduplication, source tracking, verification workflow.
- Replace or supersede Phase 0 pilot/test questions where they are not production-quality.
- Optional later polish (only if useful): tutor replace-question before publish, explanations, topic-wise breakdown.

**Done when:** Tutors can build real exams across the agreed subjects/chapters with enough verified questions and honest eligible counts—without waiting on deploy.

### Phase 5 — Auth, database migration, and deployment

**Goal:** Put PorikkhaDao online with durable data and Google sign-in.

- Set up Supabase project; Google OAuth for tutors and students.
- Migrate SQLite bank + exams/attempts to Postgres; enable RLS / ownership policies.
- Deploy to Vercel (or equivalent); configure env vars and production `NEXT_PUBLIC_APP_URL`.
- Verify mobile + desktop on the live URL; timezone and expiry still correct.
- Schedule or equivalent for finalizing expired attempts in production.

**Done when:** A tutor can send a public link, students sign in with Google, and results work on the hosted site.

## 5. Rules for question selection

1. Start with only verified questions from requested subject/paper/chapter(s).
2. Restrict matches to selected topics; **do not include questions tagged with excluded topics**. Cross-topic questions qualify only if all their topic tags are allowed (strict filter).
3. Apply explicitly chosen difficulty or type filters only when those tags are reviewed; avoid guessing missing tags.
4. If eligible questions are fewer than requested, display the actual count and ask the tutor to reduce count or broaden scope; never silently repeat questions.
5. Randomize eligible question selection and order; store that frozen set in `exam_questions`.
6. Score on the server: correct = 1, incorrect/unanswered = 0 in MVP. No negative marking unless added deliberately later.
7. Default one attempt per student identity per published exam; if retries are needed, design them as a separate feature.

## 6. Reliability and security checklist

- [x] Only tutor owner can modify exam and view all its results.
- [x] Only authenticated students with a valid exam link can start an attempt.
- [x] A student cannot access the correct answers or edit another student's attempt.
- [x] Duration is enforced with server timestamps; timer does not restart after refresh.
- [x] Answers persist before deadline and scoring uses only stored answers.
- [x] Expired attempts are finalized even without an active browser (finalize-on-access + `/api/finalize-expired`).
- [x] Answer updates after the deadline are rejected.
- [x] Double-click/repeated submit cannot create duplicate attempts or scores.
- [x] A tutor sees available question counts and failures to meet requested counts.
- [x] The website works on narrow mobile screens as well as desktop.
- [ ] Imported MCQs have usable rights, sources, correct answers, and reviewed topic tags. *(Phase 4)*
- [x] Bangla/English toggle works on tutor and student surfaces.
- [ ] Google OAuth + hosted production. *(Phase 5)*

## 7. Suggested development order (actual tickets)

1. ~~Phase 0–3: pilot bank, tutor flow, student flow, results, local production~~ **DONE**
2. **Phase 4:** syllabus expansion → content acquisition → validate/import → quality pass
3. **Phase 5:** Supabase Auth + Postgres migration + Vercel deploy + live E2E

## 8. Decisions intentionally kept simple

- **Responsive web, not native Android/iOS.**
- **Bilingual BN/EN with a toggle.**
- **Content before cloud deploy** (Phase 4 before Phase 5).
- **Google OAuth in Phase 5** via Supabase (local auth until then).
- **One attempt per student per exam.**
- **Relative per-student timer**, starting at first Start action.
- **One point per correct MCQ, no negative marking.**
- **Bank selection, not real-time AI question generation.**
- **Simple content import first**, no large-scale scraping built into the app.
- **Local SQLite through Phase 4**; Supabase in Phase 5.

## 9. MVP acceptance scenario

A tutor signs in and builds a **Physics 2nd Paper** exam from **only 6 selected topics** of a chapter. The tutor requests **50 MCQs** and **30 minutes**, reviews and publishes, then shares the URL. Students identify, start their individual timers, answer on mobile, and either submit or expire. All answers saved before expiry are scored. The tutor sees each student's name, completion status, and score. No AI service or Google Form is involved. UI can be used in Bangla or English.

If this scenario works reliably with a verified question bank, the **product MVP (Phases 0–3)** is complete. Shipping to the public internet waits on **Phase 4 content** and **Phase 5 deploy**.
