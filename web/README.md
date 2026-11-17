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

## Smoke script

```bash
node scripts/smoke-phase1.mjs
```

Creates a published 50-question exam from 6 thermodynamics topics.
