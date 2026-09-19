# TeachTime — Project Progress

_Status of the standalone Teacher Availability web app._
_Last updated: 2026-09-19._

Branch: `claude/teacher-availability-webapp-kes515` · PR: cm-game-studio #2 (draft)

---

## Summary

The app is **built, tested locally, and deploy-ready for Vercel**. The database (Supabase Postgres,
`ta_*` tables in the `cm-whiteboard` project) is **provisioned**. The only remaining step is the
**user-run Vercel deploy** (needs the Vercel login + the Supabase secret key), which cannot be done
from the build session.

Overall: **~90% done** — code and DB complete; production deploy is the open item.

---

## ✅ Done

### Product / features
- [x] Teacher accounts: register, log in, log out, "who am I" (`/api/me`).
- [x] Teacher availability CRUD: add, edit, delete slots; flip open↔booked.
- [x] Slot fields: subject, grade (or "all grades"), day, start/end time, mode, status, notes.
- [x] Weekly recurring slots (repeat until deleted).
- [x] Parent **public** search — **no login** — by name, grade, subject, day, and "open only".
- [x] Results grouped per teacher, with slot counts.

### Backend
- [x] Express server (`server.js`) serving pages + JSON API.
- [x] Simple auth with Node's built-in `crypto`: scrypt password hashing + HttpOnly session cookie.
      No auth libraries.
- [x] Server-side validation (day, `HH:MM` times, end > start, grade 1–12/blank, mode, status).
- [x] Per-teacher ownership enforced on every write.
- [x] Swappable storage layer (`store.js`): Supabase in prod, JSON file in local dev — one interface.

### Database (Supabase, project `cm-whiteboard`)
- [x] Tables created: `ta_teachers`, `ta_slots`, `ta_sessions` (with indexes + cascade delete).
- [x] RLS **enabled with no policies** → only the server's secret key can access them.
- [x] Schema + the grade filter verified with live insert/select/delete against the DB.

### Deploy prep
- [x] `vercel.json` (runs `server.js`, bundles `public/**`).
- [x] `deploy.sh` one-shot Vercel CLI script + manual steps in `README.md`.
- [x] `.env.example` documenting `SUPABASE_URL` and `SUPABASE_SECRET_KEY`.

### Testing (this session, local, file backend)
- [x] register / login / wrong-password → 401 / duplicate email → 409.
- [x] add slot; invalid slot (end ≤ start) → 400.
- [x] `GET /api/my-slots` without cookie → 401.
- [x] public `GET /api/availability` with no auth; subject filter; grade filter returns matching
      grade **and** "all grades" slots.
- [x] all page routes return HTTP 200.

### Docs
- [x] `README.md` (run + deploy).
- [x] `docs/FUNCTIONALITY.md` (features + every function).
- [x] `docs/PROGRESS.md` (this file).

---

## ⏳ In progress / handoff to user
- [ ] **Deploy to Vercel** — run `./deploy.sh` (or the dashboard steps); set env vars; verify
      `/healthz` shows `"backend":"supabase"`. _Requires the user's Vercel login + Supabase secret key._
- [ ] End-to-end test of the **Supabase backend via the running app** (only possible once the
      secret key is set as an env var — the schema itself is already verified).

---

## ❌ Not built yet (possible next steps)
- [ ] Password reset / "forgot password" and email verification.
- [ ] Parent-side **booking / requests** (today `status` is set by the teacher only).
- [ ] Rate limiting / lockout on login and register.
- [ ] Admin view / teacher directory management.
- [ ] Time-zone handling and calendar (.ics) export.
- [ ] Automated test suite in CI (current tests were run manually).
- [ ] Custom branding / rename from the "TeachTime" placeholder.
- [ ] Move to a **dedicated** Supabase project (currently shares `cm-whiteboard`; its secret key can
      reach that project's other tables — noted as a security trade-off the user accepted).

---

## ⚠️ Known notes / risks
- The local **JSON file** store is dev-only; it does **not** persist on Vercel's serverless
  filesystem — production **must** use Supabase.
- The Supabase **secret key** grants full access to the whole `cm-whiteboard` project. Keep it only
  in Vercel env vars; rotate if it leaks.
- Pre-existing (not from this app): four other tables in `cm-whiteboard`
  (`demo_reminders`, `cancel_notify`, `reschedule_notify`, `mh_cancel_emails`) have **RLS disabled**
  and are exposed to the anon key — worth fixing separately.
