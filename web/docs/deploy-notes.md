# PorikkhaDao deployment notes

## Phase order

1. **Phases 0–3** — Local product MVP (done)
2. **Phase 4** — Full content generation (next; stay on SQLite)
3. **Phase 5** — Supabase Auth + Postgres + cloud host (Vercel)

Do **not** deploy for real users until Phase 4 content is ready enough to ship.

## Current stack (through Phase 4)

- Question bank + exams + attempts: **SQLite** at `../content/db/porikkhadao.sqlite`
- Auth: local session cookies (tutor password; students name+email)

## Local production (supported now)

From `web/`:

```bash
cp .env.example .env.local   # if needed
npm install
npm run build
npm run start
```

Open `http://localhost:3000/en`.

Demo tutor: `tutor@porikkhadao.local` / `porikkha123`

### Finalize overdue attempts

```bash
curl -X POST http://localhost:3000/api/finalize-expired
```

## Why not Vercel during Phase 4

Vercel serverless filesystems are ephemeral. SQLite will not persist reliably. Cloud deploy is **Phase 5**, after Postgres.

## Phase 5 checklist (later)

1. Migrate schema + data to Supabase Postgres
2. Wire Google OAuth (tutor + student)
3. Enable RLS / ownership policies
4. `vercel deploy` (or git-linked project) with production env vars
5. Set `NEXT_PUBLIC_APP_URL` to the live domain
6. Schedule `/api/finalize-expired` (or equivalent) in production
