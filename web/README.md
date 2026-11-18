# PorikkhaDao web

Tutor exam creation + student attempts. **Postgres + Google Auth on Supabase**, host on Vercel.

## Setup

1. Apply `src/db/schema-postgres.sql` in Supabase and migrate the bank (see [`docs/deploy-notes.md`](docs/deploy-notes.md)).
2. Enable **Google** in Supabase Auth and create a Google Cloud OAuth client (same doc).
3. Copy `.env.example` → `.env.local` and set:
   - `DATABASE_URL`
   - `NEXT_PUBLIC_SUPABASE_URL`
   - `NEXT_PUBLIC_SUPABASE_ANON_KEY`
   - `SESSION_SECRET`
   - `NEXT_PUBLIC_APP_URL`
4. Install and run:

```bash
npm install
npm run dev
```

Open http://localhost:3000/en/login → **Continue with Google** (any Google account = tutor).

Students open a published exam share link, enter name + email, and take the exam (no Google).

## Deploy

Follow [`docs/deploy-notes.md`](docs/deploy-notes.md).
