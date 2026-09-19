# TeachTime — Teacher Availability

A small, **standalone** web app (independent of the Game Studio app in this repo):

- **Teachers** create an account and log in to add/edit their weekly class availability.
- **Parents** browse and search availability by **teacher name, grade, or subject** — **no login required**.

No external services. Data lives in a single JSON file (`data/db.json`). Auth uses Node's
built-in `crypto` (scrypt password hashing + an HttpOnly session cookie) — no auth libraries.

## Run locally

```bash
cd teacher-availability
npm install
npm start
```

Then open:

| URL | Who | Login? |
|---|---|---|
| http://localhost:4000/ | Parents — search availability | No |
| http://localhost:4000/teacher | Teachers — manage availability | Yes (register on first use) |

Change the port with `PORT=5000 npm start`.

## How it works

- A teacher registers (name, email, password, optional subjects), then adds slots:
  subject, grade (or "all grades"), day, start/end time, mode (Online / In-person),
  status (open / booked), and optional notes. Slots repeat weekly until deleted.
- Parents hit the public search page and filter by name, grade, subject, day, and an
  "open slots only" toggle. Results are grouped per teacher. This page calls only the
  public `GET /api/availability` endpoint and never requires a session.

## API

Public (no auth):
- `GET /api/availability?name=&grade=&subject=&day=&open=1` → `{ slots, subjects }`

Teacher (session cookie required):
- `POST /api/auth/register` · `POST /api/auth/login` · `POST /api/auth/logout` · `GET /api/me`
- `GET /api/my-slots`
- `POST /api/slots` · `PUT /api/slots/:id` · `DELETE /api/slots/:id`

A teacher can only read/modify their own slots; server-side validation enforces valid
days, `HH:MM` times, grade 1–12 (or blank), mode, and status.

## Notes / limitations

- **Persistence:** the JSON file store is for a single long-running Node process (a VM,
  a container, or local dev). It is **not** suitable for serverless platforms with an
  ephemeral/read-only filesystem (e.g. Vercel functions) — there it would reset. For
  production, swap the file store for a real database (Postgres/SQLite); the data access
  is isolated in `server.js`.
- Passwords are hashed (scrypt); sessions are random tokens in an HttpOnly, SameSite=Lax
  cookie (add `Secure` automatically when `NODE_ENV=production`). Serve over HTTPS in
  production.
