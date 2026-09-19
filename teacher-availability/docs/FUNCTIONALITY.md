# TeachTime — Functionality Reference

_What the app does, and every function/endpoint in it, in detail._

---

## 1. What the app does (in one paragraph)

TeachTime is a standalone web app for publishing and finding **teacher class availability**.
**Teachers** create an account and log in to add the weekly time slots they can teach (subject,
grade, day, start/end time, online vs in-person, open vs booked, and a note). **Parents** open a
public page — **no login** — and search those slots by teacher **name**, **grade**, or **subject**
(plus day, and an "open only" toggle), grouped per teacher. It runs as one small Node/Express
server that serves the pages and a JSON API, and stores data in Supabase Postgres in production
(or a local JSON file in development).

---

## 2. The two user roles

| Role | Page | Login? | Can do |
|---|---|---|---|
| **Teacher** | `/teacher` | Yes (register once, then log in) | Add / edit / delete own slots, flip a slot open↔booked, log out |
| **Parent / anyone** | `/` | No | Search & browse all teachers' availability |

Auth is intentionally simple: a teacher signs up with name + email + password (+ optional
subjects). Passwords are hashed; a login sets a session cookie. Parents never authenticate.

---

## 3. Core concepts / data model

**Teacher** (`ta_teachers`)
- `id`, `name`, `email` (unique), `subjects` (list), `pass` (scrypt hash, never the raw password), `created_at`

**Slot** = one recurring weekly availability (`ta_slots`)
- `id`, `teacher_id`, `teacher_name` (copied in for fast search/display),
- `subject` (text), `grade` (1–12 or **null = "all grades"**),
- `day_of_week` (Monday…Sunday), `start_time`, `end_time` (`HH:MM`),
- `mode` (`Online` | `In-person`), `status` (`open` | `booked`), `notes`,
- `created_at`, `updated_at`

**Session** (`ta_sessions`)
- `token` (random), `teacher_id`, `created_at` — expires after 30 days.

A slot with `grade = null` matches **every** grade filter (it means "all grades").

---

## 4. HTTP API (what the server exposes)

### Public — no login
| Method + path | Purpose | Query / body | Returns |
|---|---|---|---|
| `GET /` | Parent search page (HTML) | — | `index.html` |
| `GET /teacher` | Teacher page (HTML) | — | `teacher.html` |
| `GET /healthz` | Health / which backend is live | — | `{ ok, backend }` |
| `GET /api/availability` | **Search availability** | `name`, `grade`, `subject`, `day`, `open=1` (all optional) | `{ slots[], subjects[] }` |

### Auth
| Method + path | Purpose | Body | Notes |
|---|---|---|---|
| `POST /api/auth/register` | Create teacher account | `{ name, email, password, subjects? }` | Sets session cookie; 409 if email exists; password ≥ 6 chars |
| `POST /api/auth/login` | Log in | `{ email, password }` | 401 on wrong credentials |
| `POST /api/auth/logout` | Log out | — | Clears session + cookie |
| `GET /api/me` | Who am I | — | `{ teacher | null }` |

### Teacher slots — session cookie required (else `401`)
| Method + path | Purpose | Body |
|---|---|---|
| `GET /api/my-slots` | List my slots | — |
| `POST /api/slots` | Create a slot | slot fields |
| `PUT /api/slots/:id` | Edit my slot | slot fields |
| `DELETE /api/slots/:id` | Delete my slot | — |

A teacher can only read/modify **their own** slots (ownership is checked on every write).

---

## 5. Every function, file by file

### `server.js` (the Express app + API)
- **`clean(s)`** — trims a value to a string (null-safe). Used to sanitize all inputs.
- **`isTime(s)`** — regex-validates an `HH:MM` 24-hour time.
- **`hashPassword(pw)`** — makes a random salt and returns `salt:scryptHash` (via Node `crypto`).
- **`verifyPassword(pw, stored)`** — recomputes the hash and compares in constant time
  (`crypto.timingSafeEqual`) to resist timing attacks.
- **`parseCookies(req)`** — reads the `Cookie` header into an object (no cookie library used).
- **`setSessionCookie(res, token)`** — writes the `ta_session` cookie: `HttpOnly`, `SameSite=Lax`,
  30-day `Max-Age`, and `Secure` when `NODE_ENV=production`.
- **`currentTeacher(req)`** — reads the cookie → looks up the session → returns the teacher (or null).
- **`requireTeacher(handler)`** — wraps a route so it runs only if signed in; otherwise returns `401`.
  Also catches errors and returns `500` with a message.
- **`pub(teacher)`** — strips a teacher object down to safe public fields (**never** returns `pass`).
- **`validateSlot(body)`** — server-side validation: subject required, valid day, `HH:MM` times,
  end after start, grade 1–12 or blank, mode/status defaulted safely. Returns `{value}` or `{error}`.
- **Route handlers** — register, login, logout, me, my-slots, create/update/delete slot, availability,
  page routes, and `/healthz` (each described in §4).
- **Startup guard** — `if (require.main === module) app.listen(...)`; on Vercel the app is exported
  as a serverless handler instead of listening.

### `store.js` (storage layer — swappable backend)
Chooses a backend from env vars: **Supabase** if `SUPABASE_URL` + `SUPABASE_SECRET_KEY` are set,
otherwise a **local JSON file**. Both expose the same async methods, so `server.js` never changes:
- **`findTeacherByEmail(email)`**, **`getTeacherById(id)`**, **`createTeacher(t)`**
- **`createSession(token, teacherId)`**, **`getSession(token)`** (enforces 30-day expiry),
  **`deleteSession(token)`**
- **`listSlotsByTeacher(teacherId)`**, **`createSlot(slot)`**, **`getOwnedSlot(id, teacherId)`**,
  **`updateSlot(id, teacherId, fields)`**, **`deleteSlot(id, teacherId)`**
- **`availability({name, subject, day, grade, openOnly})`** — the parent search query
  (grade filter is "grade is null OR grade = X").
- **`subjects()`** — distinct subject list, for the search dropdown.
- The file backend adds an internal **`save()`** (atomic write via temp file + rename) and
  **`match()`** (in-memory filter mirroring the SQL).

### `public/index.html` (parent search page — vanilla JS)
- **`load()`** — builds the query string from the filter inputs and calls `GET /api/availability`.
- **`fillSubjects(subs)`** — populates the Subject dropdown once, from the server's subject list.
- **`render(slots)`** — groups slots by teacher and draws a card per teacher with each slot row;
  updates the "N slots · M teachers" count.
- **`clearFilters()`** — resets all filters and reloads.
- **`esc(s)`** — HTML-escapes text before insertion (prevents HTML/script injection in the page).
- Name input is debounced (~180 ms); the other filters reload on change.

### `public/teacher.html` (teacher login + dashboard — vanilla JS)
- **`api(url, opts)`** — small `fetch` wrapper that sends/receives JSON and throws on non-2xx.
- **`showAuth()` / `showDash()`** — toggles between the login/register screen and the dashboard.
- **`setMode(m)`** — switches the auth form between "Log in" and "Create account".
- **`submitAuth()`** — calls register or login, then shows the dashboard.
- **`logout()`** — calls the logout endpoint and returns to the auth screen.
- **`loadSlots()`** — fetches the teacher's slots (sorted by day then time) and renders them.
- **`renderSlots()`** — draws each slot card with Edit / open↔booked / Delete buttons.
- **`readForm()`** — reads the add/edit form into a slot object.
- **`saveSlot()`** — creates (POST) or updates (PUT) a slot, then reloads.
- **`editSlot(id)`** — loads a slot back into the form for editing.
- **`resetForm()`** — clears the form back to "Add a slot".
- **`toggleStatus(id)`** — flips a slot between open and booked.
- **`removeSlot(id)`** — deletes a slot (with confirm).
- **`showErr/hideErr/esc/toast`** — small UI helpers (inline error banners, escaping, toasts).
- On load it calls `GET /api/me`: if already signed in → dashboard, else → auth screen.

### `public/styles.css`
Shared design tokens (colors, fonts, radius) and component styles (nav, cards, forms, pills,
buttons, toast) used by both pages.

### Config / ops files
- **`package.json`** — dependencies (`express`, `@supabase/supabase-js`) and `npm start`.
- **`vercel.json`** — tells Vercel to run `server.js` as one Node function and bundle `public/**`.
- **`.env.example`** — the two env vars (`SUPABASE_URL`, `SUPABASE_SECRET_KEY`).
- **`deploy.sh`** — one-shot Vercel CLI deploy (login → link → set env vars → deploy).
- **`README.md`** — run + deploy instructions.
- **`data/.gitkeep`** — keeps the `data/` folder; the JSON file backend writes `data/db.json` here
  in local dev.

---

## 6. Security notes (what protects the data)
- Passwords are **scrypt-hashed with a per-user salt**; the raw password is never stored or returned.
- Sessions are random 24-byte tokens in an **HttpOnly, SameSite=Lax** cookie (adds `Secure` in prod).
- All slot inputs are **validated server-side**; teachers can only touch **their own** slots.
- Output is **HTML-escaped** on the pages.
- In production the browser talks only to this server; the Supabase **secret key** stays on the
  server, and the `ta_*` tables have **RLS enabled with no policies** so only that key can reach them.

## 7. Known limits / not built yet
See `docs/PROGRESS.md` for the full status. In short: no "forgot password" / email verification,
no booking by parents (status is set by the teacher), no rate-limiting, and the local JSON backend
is dev-only (production must use Supabase).
