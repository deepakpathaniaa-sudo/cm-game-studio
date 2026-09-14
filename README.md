# Concept Mastery Game Studio

A Node.js + Supabase web app for the Concept Mastery program. It has role-based
logins (student, parent, instructor, admin), the 10-day Game Studio curriculum,
and a **multi-user Quiz Arena** where admins turn quiz PDFs into interactive
multiple-choice quizzes and students compete on a live leaderboard.

## Routes

| Route | Description |
|---|---|
| `/` | Sign in / create account |
| `/student` | Student Game Studio dashboard (+ Quizzes link) |
| `/instructor` | Instructor dashboard |
| `/parent` | Parent dashboard |
| `/admin` | Admin dashboard (users + **Quizzes** management) |
| `/quiz` | Quiz Arena — take quizzes + leaderboard (any signed-in user) |

## Quiz feature — how it works

1. **Admin uploads a PDF** on the Admin → 🧠 Quizzes tab.
2. The PDF's **text is read in the browser** (via pdf.js — the file never leaves
   the admin's machine).
3. The text is turned into multiple-choice questions (each with **4 options and
   one correct answer**) two ways:
   - **Auto-detect** (default, no setup): a built-in parser extracts questions
     from PDFs that already contain multiple-choice questions + an answer key or
     inline `Answer: B` lines. Handles `A)`, `(A)`, `A.`, upper/lowercase, and
     wrapped lines.
   - **Generate with Claude** (optional): sends the extracted text to the
     `generate-quiz` Supabase Edge Function, which uses the Anthropic API to
     generate questions from *any* material (notes, passages, prose).
4. The admin **reviews and edits every question** in an inline editor, marks the
   correct option, then **publishes**.
5. **Students take the quiz** at `/quiz` — one question at a time, immediate
   feedback, a timer, and a score.
6. Each student attempt is recorded and shown on the **leaderboard** (per quiz,
   and an overall points ranking) that updates as more people play.

## Setup

### 1. Database

Run these in **Supabase → SQL Editor → New Query**, in order:

1. `schema.sql` — base tables (profiles, roles, progress, uploads).
2. `quiz-schema.sql` — quiz tables (`quizzes`, `quiz_questions`,
   `quiz_attempts`) + row-level security. Safe to re-run.

> The Supabase URL and publishable key are set inline in the HTML pages
> (`public/*.html`). Point them at your own project if you fork this.

### 2. (Optional) Claude quiz generation

The app works fully without this — Auto-detect + the manual editor cover
PDFs that already contain multiple-choice questions. Deploy the edge function
to also generate questions from plain prose:

```bash
supabase functions deploy generate-quiz --project-ref <your-project-ref>
supabase secrets set ANTHROPIC_API_KEY=sk-ant-... --project-ref <your-project-ref>
# optional: pick a model (default claude-opus-5)
supabase secrets set QUIZ_MODEL=claude-sonnet-5 --project-ref <your-project-ref>
```

Then the **✨ Generate with Claude** button on the admin Quizzes tab works.
Source: `supabase/functions/generate-quiz/index.ts`.

## Run Locally

```bash
npm install
npm start
```

Then open http://localhost:3000

## Deploy to Vercel

Push to GitHub and import at https://vercel.com/new — `vercel.json` is already
configured. (Vercel serves the static pages + the Express routes; the optional
edge function is deployed to Supabase, not Vercel.)
