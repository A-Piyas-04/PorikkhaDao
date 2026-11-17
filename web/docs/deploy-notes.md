# PorikkhaDao deployment notes (Phase 3)

## Current stack reality

- Question bank + exams + attempts live in **SQLite**: `../content/db/porikkhadao.sqlite`
- Auth is local session cookies (tutor password; students name+email)
- **Supabase Auth + Postgres are intentionally after Phase 3**

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

Hit periodically (Task Scheduler / cron):

```bash
curl -X POST http://localhost:3000/api/finalize-expired
```

Or open `/api/finalize-expired` in a browser (GET also works).

## Why not Vercel yet

Vercel serverless filesystems are ephemeral. The SQLite file will not persist reliably across invocations. Do **not** deploy this Phase 0–3 SQLite app to Vercel expecting durable exam data.

## After Supabase (next milestone)

1. Migrate schema + data to Postgres
2. Wire Google OAuth (tutor + student)
3. Enable RLS / ownership policies
4. Then use Vercel (`deploy-to-vercel` skill / `vercel deploy`)
5. Set env vars in the Vercel project dashboard (`SESSION_SECRET` replaced by Supabase keys, `NEXT_PUBLIC_APP_URL`, etc.)

`next.config.ts` already sets `serverExternalPackages: ["better-sqlite3"]` for local Node hosting.
