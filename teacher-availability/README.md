# TeachTime — Teacher Availability

A small, **standalone** web app (independent of the Game Studio app in this repo):

- **Teachers** create an account and log in to add/edit their weekly class availability.
- **Parents** browse and search availability by **teacher name, grade, or subject** — **no login required**.

Auth uses Node's built-in `crypto` (scrypt password hashing + an HttpOnly session cookie) —
no auth libraries. Storage has two interchangeable backends, chosen automatically:

| Condition | Backend | Use |
|---|---|---|
| `SUPABASE_URL` **and** `SUPABASE_SECRET_KEY` set | Supabase Postgres | Vercel / production (persists) |
| neither set | JSON file (`data/db.json`) | local dev |

## Run locally

```bash
cd teacher-availability
npm install
npm start
```

| URL | Who | Login? |
|---|---|---|
| http://localhost:4000/ | Parents — search availability | No |
| http://localhost:4000/teacher | Teachers — manage availability | Yes (register on first use) |

With no env vars, it uses the local JSON file. To exercise the Supabase path locally, set the
two env vars (see `.env.example`) before `npm start`.

## Deploy to Vercel

The Supabase Postgres tables (`ta_teachers`, `ta_slots`, `ta_sessions`) already exist in the
**cm-whiteboard** project (`cqzpzhdleqyrmedymypg`). They have RLS enabled with **no policies**,
so only the server's **secret** key can read/write them — the browser never touches Supabase.

1. **Import the repo** at https://vercel.com/new → select `deepakpathaniaa-sudo/cm-game-studio`.
2. **Set _Root Directory_ to `teacher-availability`** (Vercel → Project → Settings → Build & Deploy,
   or during import). This is required because the app lives in a subfolder.
3. **Add Environment Variables** (Settings → Environment Variables), for Production (and Preview):
   - `SUPABASE_URL` = `https://cqzpzhdleqyrmedymypg.supabase.co`
   - `SUPABASE_SECRET_KEY` = the **service_role / secret** key from
     Supabase → project **cm-whiteboard** → Settings → API. **Server-side only — never commit it.**
4. **Deploy.** Vercel reads `vercel.json` and runs `server.js` as one Node function that serves
   both the pages and the API. Check `/(your-domain)/healthz` → should show `{"ok":true,"backend":"supabase"}`.

### Deploy from the CLI

Fastest — a helper script does all of it (run it on your own machine; it needs your Vercel login):

```bash
cd teacher-availability
./deploy.sh
```

It installs/uses the Vercel CLI, logs you in, links the project, sets `SUPABASE_URL`, prompts
for `SUPABASE_SECRET_KEY` (hidden input), and deploys to production. Running from this folder
makes it the project root, so no "Root Directory" setting is needed.

Prefer to do it by hand:

```bash
cd teacher-availability
npm i -g vercel
vercel login
vercel link
printf '%s' "https://cqzpzhdleqyrmedymypg.supabase.co" | vercel env add SUPABASE_URL production
vercel env add SUPABASE_SECRET_KEY production   # paste the service_role secret when prompted
vercel --prod
```

## API

Public (no auth):
- `GET /api/availability?name=&grade=&subject=&day=&open=1` → `{ slots, subjects }`

Teacher (session cookie required):
- `POST /api/auth/register` · `POST /api/auth/login` · `POST /api/auth/logout` · `GET /api/me`
- `GET /api/my-slots` · `POST /api/slots` · `PUT /api/slots/:id` · `DELETE /api/slots/:id`

A teacher can only read/modify their own slots; server-side validation enforces valid days,
`HH:MM` times, grade 1–12 (or blank), mode, and status.

## Notes

- Passwords are hashed with scrypt; sessions are random tokens in an HttpOnly, SameSite=Lax
  cookie (`Secure` is added automatically when `NODE_ENV=production`, which Vercel sets).
- The Supabase **secret** key grants full access to the cm-whiteboard project. Keep it only in
  Vercel's env vars. If it ever leaks, rotate it in the Supabase dashboard.
- The local JSON file store is for dev only; it does **not** persist on Vercel's serverless
  filesystem, which is why production uses Supabase.
