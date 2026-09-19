# Concept Mastery Game Studio

A simple Node.js server that serves the student and instructor interfaces for the Concept Mastery Game Studio program.

## Routes

| Route | Description |
|---|---|
| `/` | Login / sign-up |
| `/student` | Student Game Studio (Grade 4 & 5) |
| `/instructor` | Instructor Dashboard |
| `/parent` | Parent progress view |
| `/admin` | Admin console |
| `/availability` | **Teacher availability manager** — teachers add/edit weekly slots (instructor/admin only) |
| `/find-teachers` | **Find a Teacher** — parents search availability by name, grade, or subject |

## Teacher Availability

Teachers publish recurring weekly slots (subject, grade, day, time, mode, open/booked status);
parents browse and filter them by teacher **name**, **grade**, or **subject** (plus day and
open-only).

Backed by the `teacher_availability` table with row-level security: any signed-in user can read
availability, but a teacher can only write their own slots. Run
[`migrations/teacher_availability.sql`](migrations/teacher_availability.sql) in Supabase → SQL
Editor once (it is also included at the end of `schema.sql`). Teachers are users with the
`instructor` role.

## Run Locally

```bash
npm install
npm start
```

Then open:
- Student: http://localhost:3000
- Instructor: http://localhost:3000/instructor

## Deploy to Vercel

### Option 1 — Vercel CLI

```bash
npm install -g vercel
vercel --prod
```

Follow the prompts. Vercel will detect `vercel.json` and deploy automatically.

### Option 2 — Vercel Dashboard

1. Push this folder to a GitHub repository.
2. Go to https://vercel.com/new and import the repo.
3. Leave all settings as defaults and click **Deploy**.

Your app will be live at a `*.vercel.app` URL within seconds.
