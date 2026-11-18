# PorikkhaDao deployment (Phase 5)

Stack: **Next.js on Vercel** + **Postgres + Auth on Supabase** (Google sign-in).

---

## What the code expects

| Variable | Where | Notes |
|---|---|---|
| `DATABASE_URL` | Vercel + local `.env.local` | Supabase Postgres **Transaction** pooler URI (`:6543`) |
| `NEXT_PUBLIC_SUPABASE_URL` | Vercel + local | Project URL from Supabase → Settings → API |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | Vercel + local | Anon/publishable key (Config type on Vercel) |
| `TUTOR_EMAILS` | Vercel + local | Comma-separated Google emails allowed as tutors |
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

### 4. Tutor allowlist
Set `TUTOR_EMAILS` to the Google account(s) that may create exams, e.g.:

```env
TUTOR_EMAILS=you@gmail.com,coTutor@gmail.com
```

Anyone else who signs in via an exam link becomes a **student**.

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
| `TUTOR_EMAILS` | Secret or Config | your Gmail(s) |
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

- Tutors: `/en/login` → Google → must be in `TUTOR_EMAILS`
- Students: exam share link → Google → app user role `student`
- Sessions: Supabase Auth cookies (PKCE) via `@supabase/ssr` + `src/proxy.ts`
