# PorikkhaDao deployment (Phase 5)

Stack: **Next.js on Vercel** + **Postgres + Auth on Supabase** (Google sign-in).

---

## What the code expects

| Variable | Where | Notes |
|---|---|---|
| `DATABASE_URL` | Vercel + local `.env.local` | Supabase Postgres **Transaction** pooler URI (`:6543`) |
| `NEXT_PUBLIC_SUPABASE_URL` | Vercel + local | Project URL from Supabase → Settings → API |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | Vercel + local | Anon/publishable key (Config type on Vercel) |
| `SESSION_SECRET` | Vercel + local | Signs short-lived student exam-link cookies |
| `NEXT_PUBLIC_APP_URL` | Vercel + local | Public site origin, e.g. `https://your-app.vercel.app` (Config type) |

App root for Vercel: **`web/`** (not the repo root).

Schema: `web/src/db/schema-postgres.sql`  
Data migrate: `tools/question_bank/migrate_sqlite_to_postgres.py`

---

## Supabase — Google Auth setup (required)

### 1. API keys
Supabase → **Project Settings → API** (or **Connect**):
- Copy **Project URL** → `NEXT_PUBLIC_SUPABASE_URL`
- Copy **anon** / **publishable** key → `NEXT_PUBLIC_SUPABASE_ANON_KEY`

### 2. Enable Google provider
1. Supabase → **Authentication → Providers → Google** → Enable
2. You need a Google Cloud OAuth client:
   1. [Google Cloud Console](https://console.cloud.google.com/) → APIs & Services → Credentials
   2. Create **OAuth client ID** → type **Web application**
   3. **Authorized JavaScript origins**:
      - `http://localhost:3000`
      - `https://YOUR_VERCEL_DOMAIN`
   4. **Authorized redirect URIs** — copy the callback URL shown on the Supabase Google provider page  
      (looks like `https://YOUR_PROJECT_REF.supabase.co/auth/v1/callback`)
   5. Paste **Client ID** + **Client Secret** into Supabase Google provider → Save

### 3. Redirect allow list
Supabase → **Authentication → URL Configuration**:
- **Site URL**: your Vercel URL (or `http://localhost:3000` while testing locally)
- **Redirect URLs** add:
  - `http://localhost:3000/auth/callback`
  - `https://YOUR_VERCEL_DOMAIN/auth/callback`

### 4. Who is a tutor vs student
- **Tutors:** any Google account via `/login` (Supabase Auth).
- **Students:** do not use Google. They open the share link, enter **name + email**, and take the exam.

---

## Load question bank (one-time)

```powershell
python -m pip install "psycopg[binary]"
$env:DATABASE_URL = "postgresql://...@....pooler.supabase.com:5432/postgres"  # Session/Direct
python tools/question_bank/migrate_sqlite_to_postgres.py --skip-schema
```

---

## Vercel env vars

| Name | Visibility | Value |
|---|---|---|
| `DATABASE_URL` | Secret | Transaction pooler URI |
| `NEXT_PUBLIC_SUPABASE_URL` | Config | `https://….supabase.co` |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | Config | anon/publishable key |
| `SESSION_SECRET` | Secret | long random string |
| `NEXT_PUBLIC_APP_URL` | Config | `https://your-app.vercel.app` |

After changing `NEXT_PUBLIC_*` vars, **Redeploy**.

Optional: schedule `GET /api/finalize-expired` so overdue attempts close.

---

## Local development

```powershell
cd web
# fill .env.local from .env.example
npm install
npm run dev
```

Open `http://localhost:3000/en/login` → **Continue with Google**.

---

## Auth flow (app)

- Tutors: `/en/login` → Google → tutor dashboard
- Students: exam share link → name + email → timed attempt (no Google)
- Tutor sessions: Supabase Auth cookies via `@supabase/ssr` + `src/proxy.ts`
- Student sessions: short-lived signed cookie (`SESSION_SECRET`)
