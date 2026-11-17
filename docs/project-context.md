# PorikkhaDao (পরীক্ষাদাও) — Project Context

**Product name:** PorikkhaDao / পরীক্ষাদাও  
**Status:** Phase 0 — content foundation  
**Audience:** Developer, collaborator, or AI coding assistant  
**Market:** Bangladesh HSC (Higher Secondary Certificate) tutoring  
**Languages:** Bangla and English, user-togglable throughout the product UI  
**Guiding principle:** Simple, reliable, tutor-first. No AI features or AI APIs in the MVP.

## 1. Problem

A private tutor frequently needs custom MCQ tests for Bangladesh HSC students. Requirements vary by **subject**, **1st/2nd paper**, **chapter**, and especially **specific subtopics within a chapter**. An exam might contain 30, 50, 60, or 100 MCQs, sometimes from only 6 of 10 topics in a chapter.

The current workflow is slow and repetitive:
1. Find textbooks, chapter PDFs, notes, or online questions from different sources.
2. Upload content to ChatGPT/Claude and request MCQs.
3. Ask for Google Apps Script to generate a Google Form.
4. Publish the form and share it with students.
5. Manage identification, timing, submission, and results separately; Google Forms timing is inconvenient.

The goal is to replace this with one integrated, fast, teacher-controlled workflow.

## 2. Product goal

Build **PorikkhaDao** — a **responsive web app** (mobile-first and usable on desktop) where a **tutor creates a customized HSC MCQ exam from a verified question bank**, shares a link, and receives each student's score.

The UI is **bilingual (Bangla / English)** with a language toggle so tutors and students can switch at any time.

This is **not primarily a student self-practice app**. The exam is created and controlled by the tutor. Students have a minimal, restricted exam-taking interface.

A native Android/iOS app is **not required**. No Google Forms or Google Apps Script in the finished workflow.

## 3. Intended workflow

### Tutor
1. Sign in (Google sign-in is preferred for simplicity).
2. Select **HSC → Subject → 1st/2nd Paper → Chapter(s) → Included Topics**. Explicitly omit topics that should not be tested. Multiple chapters may be supported if straightforward, but single-chapter, multi-topic tests are essential.
3. Set MCQ count (e.g., 30/50/60/100), time limit, and optionally difficulty/type mix.
4. Generate an exam by selecting existing eligible questions from the database; preview and publish it.
5. Copy the shareable exam URL and send it to students.
6. See student names/accounts, attempts, marks, and submitted/expired status in a results view.

### Student
1. Open the shared exam link on phone or computer. No teacher dashboard access.
2. Sign in with Google to establish identity (not a separate lengthy registration flow).
3. Start the exam; see the questions, options, and remaining time.
4. Answer MCQs and submit before the deadline, or have the attempt **automatically finalized when time expires**.
5. Tutor can see the scored attempt. Showing the student their score is a configurable later option; the MVP only promises tutor-visible scores.

**Submission behavior:** Answers should be saved incrementally. On deadline, the backend scores the answers already saved, **even if the browser is closed/offline or the countdown fails**. The client also attempts an immediate auto-submit while open. The server deadline is authoritative; reloading does not reset the timer.

## 4. Role boundaries

| Role | Allowed | Not allowed |
|---|---|---|
| Tutor | Manage own exams; configure, preview, publish; share links; view own students' attempts/scores | View or modify other tutors' private exams/results |
| Student | Open valid shared exam; authenticate with Google; start and answer own attempt; submit | Edit exam/questions; view answer key before permitted; view other students' attempts/scores; access tutor controls |
| Content admin (initially developer only) | Import, review, tag, and correct question-bank content | Needed as a public-facing role in MVP |

**Link possession alone does not grant teacher privileges.** Student access requires an exam link and Google sign-in. Use access controls on the server, not just hidden UI elements.

## 5. Question-bank strategy (important decision)

Use **Approach B: a stored, structured, verified question bank**. The application **does not generate brand-new MCQs from textbook prose at exam time**. It retrieves and assembles previously stored questions, allowing repeatable filtering and reliable answer keys.

Questions may be sourced from original teacher-authored material, openly licensed datasets, permitted/authorized websites, legitimately reusable past questions, or licensed content imports. Merely finding a public PDF/site does **not** give automatic permission to republish its questions. Respect site terms, copyright, and request limits.

### Acquisition and ingestion (separate from student exam flow)
1. Compile a canonical HSC syllabus hierarchy (subject, paper, chapter, topic/subtopic) for the intended curriculum/year.
2. Start with one subject/paper and a small number of chapters, not every HSC book at once.
3. Obtain legally reusable question sets. Import from CSV/Excel first; later add parsers for permitted HTML pages and digital PDFs.
4. Extract question text, four options, correct answer, source attribution, and available explanations.
5. Map the source's chapter/topic headings to the canonical syllabus; only apply automatic topic tags where the mapping is reliable.
6. Mark uncertain answers, difficulty levels, and topic labels for manual review; deduplicate and validate before publication.
7. Store **verified** questions; exclude incomplete/unverified items from exam generation.

OCR for scanned PDFs, arbitrary-webpage scraping, and automatic difficulty/classification are **optional offline data-preparation tooling**, not required product features. No AI models or AI APIs are needed for MVP.

### Phase 0 storage note
Until after Phase 3, the question bank lives in **local SQLite** (`content/db/porikkhadao.sqlite`) with CSV import tooling. **Supabase Auth and Supabase PostgreSQL are deferred until after Phase 3.**

## 6. Essential question metadata

- Question ID; curriculum/version (where applicable)
- Subject; paper (1 or 2); chapter; one or more topics
- Question stem; four choices; correct option
- Difficulty: **easy / medium / hard** (if reviewed; otherwise unclassified)
- Type: **factual / conceptual / numerical / application** (optional, reviewed)
- Source/reference; explanation (optional)
- Verification status; duplicate/quality status

Use canonical topic IDs, not free-text topic labels during filtering. If a question spans two topics, support a many-to-many question-to-topic relation; define and document whether it must match **any** selected topic or **only** selected topics. For the MVP, use **only selected topics** to prevent excluded-topic questions from slipping in, with manual review for cross-topic questions.

Syllabus labels (subject, chapter, topic) should support **Bangla and English** display names for the language toggle.

## 7. Essential exam behavior

- Filter precisely by selected subject, paper, chapters, and **included/excluded topics**.
- Select the requested number of **distinct, verified** questions; never fabricate filler questions when the bank is too small.
- Randomize question order, and optionally option order while keeping the correct answer mapping intact.
- Tutor chooses an exam duration in minutes and publishes a unique URL.
- Each Google-authenticated student can take **one attempt per exam** by default (make policy explicit, not silently duplicated).
- Time starts at a defined server-side start event per student; each student has their own deadline, unless a scheduled shared window is later added.
- Save responses during the attempt; score only on backend. On expiry, finalize saved answers; unanswered questions score zero.
- Tutor views a clear result list: student identity, total answered, correct, score, start/end timestamps, submitted versus expired.
- Do not expose the correct answers through the student exam API before completion or any teacher-authorized review.

## 8. MVP boundaries

**In scope:** Bilingual BN/EN UI toggle; Google sign-in; tutor/student authorization; question-bank import + verification; canonical hierarchy; precise topic filtering; exam creation/preview/publish; shareable link; student MCQ interface; persistent answers; timer/server expiry; automatic scoring; teacher results; mobile and desktop responsive UI.

**Out of scope for initial MVP:** AI APIs, local LLMs, textbook-to-new-question generation, unrestricted scraping, native phone apps, payment system, proctoring/webcam, anti-cheat surveillance, leaderboards, adaptive learning, elaborate analytics, CQ/creative-question grading, multi-tenant school administration, microservices, message queues, RAG, vector databases.

## 9. Key product risks and decisions

- **Content is the bottleneck**: verified topic-tagged MCQs are harder to obtain than the exam UI is to build.
- **Topic accuracy matters more than scale**: prioritize a reliable small bank over thousands of incorrectly tagged questions.
- **Rights and provenance**: track sources/licenses and avoid copying a competitor's protected question bank without permission.
- **Question quality**: incorrect answers, poor distractors, repeated questions, and incorrect difficulty tags reduce trust.
- **Expiry reliability**: ensure the backend can finalize attempts even if clients disconnect.
- **Authentication/privacy**: use Google OAuth, store only necessary identity/results, enforce data ownership.
- **Availability**: tell the tutor how many verified eligible questions exist before generating an exam.

## 10. Definition of a successful first version

A tutor can choose a precise subset of topics in one HSC chapter, generate a 30–50-question timed MCQ exam from verified stored questions, send one URL to students, and later see individually scored submissions—including automatically expired attempts—without using an AI chatbot, Google Forms, or manual scripts.
