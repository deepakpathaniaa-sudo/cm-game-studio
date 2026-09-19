# Concept Mastery Game Studio

A simple Node.js server that serves the student and instructor interfaces for the Concept Mastery Game Studio program.

## Routes

| Route | Description |
|---|---|
| `/` | Student Game Studio (Grade 4 & 5) |
| `/instructor` | Instructor Dashboard |

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
