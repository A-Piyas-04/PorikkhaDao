# PorikkhaDao web

Tutor exam creation + student attempt UI. Database is **Postgres (Supabase)**.

## Setup

1. Create a Supabase project and apply `src/db/schema-postgres.sql` (see [`docs/deploy-notes.md`](docs/deploy-notes.md)).
2. Copy `.env.example` → `.env.local` and set `DATABASE_URL`, `SESSION_SECRET`, tutor credentials, `NEXT_PUBLIC_APP_URL`.
3. Load the local SQLite bank into Postgres (once):

```powershell
python -m pip install "psycopg[binary]"
$env:DATABASE_URL = "postgresql://..."   # Session/Direct URI
python ..\tools\question_bank\migrate_sqlite_to_postgres.py --skip-schema
```

4. Install and run:

```bash
npm install
npm run dev
```

Open http://localhost:3000/en

**Demo tutor** (unless you changed env): `tutor@porikkhadao.local` / `porikkha123`

## Deploy

Follow [`docs/deploy-notes.md`](docs/deploy-notes.md) for Supabase + Vercel steps.

## Smoke scripts

Scripts talk to the live `DATABASE_URL` + running app. Prefer manual UI smoke after migrate.

Student flow: open share link → name + email → Start → answer → Submit.

Tutor UI: **Results** on My Exams / exam preview.
