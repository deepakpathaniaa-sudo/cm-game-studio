-- ═══════════════════════════════════════════════════════════
-- CM Game Studio — QUIZ Schema (multi-user quizzes + leaderboard)
-- Run this AFTER schema.sql, in Supabase → SQL Editor → New Query.
-- Safe to re-run: uses IF NOT EXISTS / DROP POLICY IF EXISTS guards.
-- ═══════════════════════════════════════════════════════════

-- ─── HELPER: current user's role (SECURITY DEFINER avoids RLS recursion) ───
create or replace function public.current_role()
returns text
language sql
security definer
stable
as $$
  select role from public.profiles where id = auth.uid()
$$;

-- ─── TABLES ──────────────────────────────────────────────────

-- A quiz, created by an admin/instructor (often from an uploaded PDF).
create table if not exists public.quizzes (
  id           uuid primary key default gen_random_uuid(),
  title        text not null,
  description  text,
  grade        int,
  source_file  text,                       -- original PDF file name (reference only)
  created_by   uuid references public.profiles(id) on delete set null,
  created_by_name text,
  is_published boolean not null default false,
  created_at   timestamptz not null default now()
);

-- One multiple-choice question. Exactly 4 options; correct_index in 0..3.
create table if not exists public.quiz_questions (
  id            uuid primary key default gen_random_uuid(),
  quiz_id       uuid not null references public.quizzes(id) on delete cascade,
  position      int not null default 0,
  question      text not null,
  options       jsonb not null,            -- ["A text","B text","C text","D text"]
  correct_index int not null check (correct_index between 0 and 3),
  explanation   text,
  constraint options_are_four check (jsonb_typeof(options) = 'array' and jsonb_array_length(options) = 4)
);

create index if not exists quiz_questions_quiz_idx on public.quiz_questions(quiz_id, position);

-- One completed attempt by a student. Powers the leaderboard.
create table if not exists public.quiz_attempts (
  id           uuid primary key default gen_random_uuid(),
  quiz_id      uuid not null references public.quizzes(id) on delete cascade,
  student_id   uuid not null references public.profiles(id) on delete cascade,
  student_name text,
  score        int not null,               -- number of correct answers
  total        int not null,               -- number of questions
  time_seconds int,
  answers      jsonb,                       -- chosen option index per question
  created_at   timestamptz not null default now()
);

create index if not exists quiz_attempts_quiz_idx    on public.quiz_attempts(quiz_id);
create index if not exists quiz_attempts_student_idx on public.quiz_attempts(student_id);

-- ─── ROW LEVEL SECURITY ──────────────────────────────────────
alter table public.quizzes        enable row level security;
alter table public.quiz_questions enable row level security;
alter table public.quiz_attempts  enable row level security;

-- quizzes ----------------------------------------------------------------
drop policy if exists "Read published quizzes" on public.quizzes;
create policy "Read published quizzes" on public.quizzes
  for select to authenticated
  using (is_published or public.current_role() in ('instructor','admin'));

drop policy if exists "Staff insert quizzes" on public.quizzes;
create policy "Staff insert quizzes" on public.quizzes
  for insert to authenticated
  with check (public.current_role() in ('instructor','admin'));

drop policy if exists "Staff update quizzes" on public.quizzes;
create policy "Staff update quizzes" on public.quizzes
  for update to authenticated
  using (public.current_role() in ('instructor','admin'));

drop policy if exists "Staff delete quizzes" on public.quizzes;
create policy "Staff delete quizzes" on public.quizzes
  for delete to authenticated
  using (public.current_role() in ('instructor','admin'));

-- quiz_questions ---------------------------------------------------------
-- Readable when the parent quiz is published (or the reader is staff).
drop policy if exists "Read questions of readable quiz" on public.quiz_questions;
create policy "Read questions of readable quiz" on public.quiz_questions
  for select to authenticated
  using (
    exists (
      select 1 from public.quizzes q
      where q.id = quiz_questions.quiz_id
        and (q.is_published or public.current_role() in ('instructor','admin'))
    )
  );

drop policy if exists "Staff write questions" on public.quiz_questions;
create policy "Staff write questions" on public.quiz_questions
  for all to authenticated
  using (public.current_role() in ('instructor','admin'))
  with check (public.current_role() in ('instructor','admin'));

-- quiz_attempts ----------------------------------------------------------
-- Students record their own attempts.
drop policy if exists "Student insert own attempt" on public.quiz_attempts;
create policy "Student insert own attempt" on public.quiz_attempts
  for insert to authenticated
  with check (auth.uid() = student_id);

-- Everyone signed in can read attempts (leaderboard shows names + scores).
drop policy if exists "Authenticated read attempts" on public.quiz_attempts;
create policy "Authenticated read attempts" on public.quiz_attempts
  for select to authenticated
  using (true);

-- Staff can clean up attempts if needed.
drop policy if exists "Staff delete attempts" on public.quiz_attempts;
create policy "Staff delete attempts" on public.quiz_attempts
  for delete to authenticated
  using (public.current_role() in ('instructor','admin'));

-- ═══════════════════════════════════════════════════════════
-- Done. Admins can now create quizzes; students can take them and
-- appear on the leaderboard.
-- ═══════════════════════════════════════════════════════════
