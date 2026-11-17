# PorikkhaDao web (Phase 1)

Tutor exam creation UI on the Phase 0 SQLite bank.

## Setup

1. Ensure Phase 0 DB exists at `../content/db/porikkhadao.sqlite` with imported questions.
2. Copy env values from `.env.local` (already created for local demo).
3. Install and run:

```bash
npm install
npm run dev
```

Open http://localhost:3000/en

**Demo tutor:** `tutor@porikkhadao.local` / `porikkha123`

## Smoke scripts

```bash
node scripts/smoke-phase1.mjs
node scripts/smoke-phase2.mjs
```

Phase 1 creates a published exam. Phase 2 verifies two independent student attempts (submit + expired scoring).

Student flow: open share link → name + email → Start → answer on phone → Submit.
