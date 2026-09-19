-- ═══════════════════════════════════════════════════════════
-- CM Game Studio — Teacher Availability
-- Run this in Supabase → SQL Editor → New Query
-- (Safe to run on top of the base schema.sql — uses IF NOT EXISTS.)
-- ═══════════════════════════════════════════════════════════

-- ─── TABLE ───────────────────────────────────────────────────
-- One row = one recurring weekly slot a teacher offers.
create table if not exists public.teacher_availability (
  id           uuid default gen_random_uuid() primary key,
  teacher_id   uuid not null references public.profiles(id) on delete cascade,
  teacher_name text not null,                 -- denormalised for fast search / display
  subject      text not null,                 -- e.g. 'Math', 'English', 'CCAT'
  grade        int,                           -- NULL = all grades
  day_of_week  text not null check (day_of_week in
                 ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')),
  start_time   text not null,                 -- 'HH:MM' 24h
  end_time     text not null,                 -- 'HH:MM' 24h
  mode         text default 'Online' check (mode in ('Online','In-person')),
  status       text default 'open'  check (status in ('open','booked')),
  notes        text,
  created_at   timestamptz default now(),
  updated_at   timestamptz default now()
);

create index if not exists idx_ta_teacher  on public.teacher_availability (teacher_id);
create index if not exists idx_ta_subject  on public.teacher_availability (subject);
create index if not exists idx_ta_grade    on public.teacher_availability (grade);

-- ─── ROW LEVEL SECURITY ──────────────────────────────────────
alter table public.teacher_availability enable row level security;

-- Any signed-in user (parents included) can read availability.
drop policy if exists "Authenticated read availability" on public.teacher_availability;
create policy "Authenticated read availability" on public.teacher_availability
  for select to authenticated using (true);

-- A teacher manages only their own rows. Admins manage everything.
drop policy if exists "Teacher insert own availability" on public.teacher_availability;
create policy "Teacher insert own availability" on public.teacher_availability
  for insert with check (
    auth.uid() = teacher_id
    and (select role from public.profiles where id = auth.uid()) in ('instructor','admin')
  );

drop policy if exists "Teacher update own availability" on public.teacher_availability;
create policy "Teacher update own availability" on public.teacher_availability
  for update using (
    auth.uid() = teacher_id
    or (select role from public.profiles where id = auth.uid()) = 'admin'
  );

drop policy if exists "Teacher delete own availability" on public.teacher_availability;
create policy "Teacher delete own availability" on public.teacher_availability
  for delete using (
    auth.uid() = teacher_id
    or (select role from public.profiles where id = auth.uid()) = 'admin'
  );

-- ─── keep updated_at fresh ───────────────────────────────────
create or replace function public.touch_updated_at()
returns trigger as $$
begin
  new.updated_at = now();
  return new;
end;
$$ language plpgsql;

drop trigger if exists trg_ta_touch on public.teacher_availability;
create trigger trg_ta_touch
  before update on public.teacher_availability
  for each row execute function public.touch_updated_at();
