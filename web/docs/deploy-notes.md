# PorikkhaDao deployment (Phase 5)

Stack: **Next.js on Vercel** + **Postgres on Supabase**. Auth remains local session cookies for now (tutor password; students name+email). Google OAuth / RLS can come later.

---

## What the code expects

| Variable | Where | Notes |
|---|---|---|
| `DATABASE_URL` | Vercel + local `.env.local` | Supabase Postgres URI |
| `SESSION_SECRET` | Vercel + local | Long random string |
| `TUTOR_EMAIL` / `TUTOR_PASSWORD` / `TUTOR_NAME` | Vercel + local | Seeds demo tutor on first boot if missing |
| `NEXT_PUBLIC_APP_URL` | Vercel + local | Public site origin, e.g. `https://your-app.vercel.app` |

App root for Vercel: **`web/`** (not the repo root).

Schema file to paste in Supabase: `web/src/db/schema-postgres.sql`

Data copy script: `tools/question_bank/migrate_sqlite_to_postgres.py`

---

## Your checklist — Supabase

1. Go to [https://supabase.com](https://supabase.com) → **New project**.
2. Pick org, name (e.g. `porikkhadao`), region close to users, set a strong DB password — **save the password**.
3. Wait until the project is healthy.
4. **SQL Editor** → New query → paste the full contents of `web/src/db/schema-postgres.sql` → **Run**.
5. **Project Settings → Database → Connection string**:
   - For **Vercel / the Next app**: copy **Transaction** pooler URI (port **6543**). Use this as `DATABASE_URL`.
   - For **one-time data migrate** from your PC: prefer **Session** pooler or **Direct** (port **5432**).
6. Replace `[YOUR-PASSWORD]` in the URI with the DB password from step 2.
7. (Optional) **Authentication** can stay unused for now — the app still uses its own cookies.

### Load the question bank into Supabase

On your machine (repo root), with a **Session/Direct** `DATABASE_URL`:

```powershell
python -m pip install "psycopg[binary]"
$env:DATABASE_URL = "postgresql://postgres.xxxx:YOUR_PASSWORD@aws-0-....pooler.supabase.com:5432/postgres"
python tools/question_bank/migrate_sqlite_to_postgres.py --skip-schema
```

If tables are empty / first load and you already ran the SQL editor step, `--skip-schema` is correct.  
If you need to wipe and reload:

```powershell
python tools/question_bank/migrate_sqlite_to_postgres.py --skip-schema --clear
```

Expect ~9k+ question rows plus syllabus tables. Confirm in Supabase **Table Editor** (`questions`, `subjects`, …).

---

## Your checklist — Vercel

1. Go to [https://vercel.com](https://vercel.com) → **Add New… → Project**.
2. Import GitHub repo `A-Piyas-04/PorikkhaDao` (connect GitHub if needed).
3. Configure:
   - **Root Directory**: `web`
   - Framework: Next.js (auto)
   - Build command: `npm run build` (default)
   - Install command: `npm install` (default)
4. **Environment Variables** (Production + Preview):

   | Name | Value |
   |---|---|
   | `DATABASE_URL` | Supabase **Transaction** pooler URI |
   | `SESSION_SECRET` | e.g. output of `openssl rand -hex 32` |
   | `TUTOR_EMAIL` | your tutor login email |
   | `TUTOR_PASSWORD` | strong password |
   | `TUTOR_NAME` | display name |
   | `NEXT_PUBLIC_APP_URL` | leave blank until first deploy, then set to `https://<project>.vercel.app` and redeploy |

5. Deploy. Open the URL → `/en/login` with the tutor credentials.
6. After the first successful deploy, set `NEXT_PUBLIC_APP_URL` to that URL (no trailing slash) and **Redeploy** so share links are correct.
7. (Optional) Vercel → Project → **Cron Jobs** or an external ping every few minutes to:

   `GET https://YOUR_DOMAIN/api/finalize-expired`

   so overdue attempts close even if nobody opens results.

---

## Local development against Supabase

```powershell
cd web
copy .env.example .env.local
# edit .env.local — paste DATABASE_URL + secrets
npm install
npm run dev
```

Open `http://localhost:3000/en`.

---

## Git push deploys

Once the Vercel project is linked to the GitHub repo, every push to `main` (or your production branch) redeploys automatically. You do **not** need the Vercel CLI for day-to-day deploys.

---

## Not in this pass

- Supabase Auth / Google OAuth
- Row Level Security policies (app uses the DB password / service connection)
- Expanding the question bank further

Those can follow after the first cloud deploy is stable.
