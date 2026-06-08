-- ═══════════════════════════════════════════════════════════
-- CM Game Studio — Supabase Schema
-- Run this entire file in Supabase → SQL Editor → New Query
-- ═══════════════════════════════════════════════════════════

-- ─── TABLES ──────────────────────────────────────────────────

create table public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  name text not null,
  role text not null check (role in ('student','parent','instructor','admin')),
  grade int,
  created_at timestamptz default now()
);

create table public.day_unlocks (
  day_number int primary key check (day_number between 1 and 10),
  is_unlocked boolean default false,
  unlocked_by uuid references public.profiles(id),
  unlocked_at timestamptz
);

create table public.student_progress (
  id uuid default gen_random_uuid() primary key,
  student_id uuid references public.profiles(id) on delete cascade,
  day int check (day between 1 and 10),
  completed boolean default false,
  prompts_used int default 0,
  xp int default 0,
  updated_at timestamptz default now(),
  unique(student_id, day)
);

create table public.game_uploads (
  id uuid default gen_random_uuid() primary key,
  student_id uuid references public.profiles(id) on delete cascade,
  student_name text,
  day int,
  file_name text,
  storage_path text,
  uploaded_at timestamptz default now(),
  viewed boolean default false
);

create table public.parent_student (
  parent_id uuid references public.profiles(id) on delete cascade,
  student_id uuid references public.profiles(id) on delete cascade,
  primary key (parent_id, student_id)
);

-- ─── SEED DAY UNLOCKS (Day 1 open by default) ────────────────

insert into public.day_unlocks (day_number, is_unlocked)
select gs, (gs = 1) from generate_series(1,10) gs;

-- ─── AUTO-CREATE PROFILE ON SIGNUP ───────────────────────────

create or replace function public.handle_new_user()
returns trigger as $$
begin
  insert into public.profiles (id, name, role, grade)
  values (
    new.id,
    coalesce(new.raw_user_meta_data->>'name', 'New User'),
    coalesce(new.raw_user_meta_data->>'role', 'student'),
    nullif(new.raw_user_meta_data->>'grade', '')::int
  );
  return new;
end;
$$ language plpgsql security definer;

create or replace trigger on_auth_user_created
  after insert on auth.users
  for each row execute function public.handle_new_user();

-- ─── ROW LEVEL SECURITY ──────────────────────────────────────

alter table public.profiles enable row level security;
alter table public.day_unlocks enable row level security;
alter table public.student_progress enable row level security;
alter table public.game_uploads enable row level security;
alter table public.parent_student enable row level security;

-- profiles
create policy "Own profile readable" on public.profiles
  for select using (auth.uid() = id);
create policy "Staff read all profiles" on public.profiles
  for select using (
    (select role from public.profiles where id = auth.uid()) in ('instructor','admin')
  );
create policy "Own profile updatable" on public.profiles
  for update using (auth.uid() = id);

-- day_unlocks
create policy "Authenticated read day_unlocks" on public.day_unlocks
  for select to authenticated using (true);
create policy "Staff update day_unlocks" on public.day_unlocks
  for update using (
    (select role from public.profiles where id = auth.uid()) in ('instructor','admin')
  );

-- student_progress
create policy "Student read own" on public.student_progress
  for select using (auth.uid() = student_id);
create policy "Student insert own" on public.student_progress
  for insert with check (auth.uid() = student_id);
create policy "Student update own" on public.student_progress
  for update using (auth.uid() = student_id);
create policy "Staff read all progress" on public.student_progress
  for select using (
    (select role from public.profiles where id = auth.uid()) in ('instructor','admin')
  );
create policy "Parent read child progress" on public.student_progress
  for select using (
    exists (select 1 from public.parent_student ps
            where ps.parent_id = auth.uid() and ps.student_id = student_progress.student_id)
  );

-- game_uploads
create policy "Student insert upload" on public.game_uploads
  for insert with check (auth.uid() = student_id);
create policy "Student read own uploads" on public.game_uploads
  for select using (auth.uid() = student_id);
create policy "Staff read all uploads" on public.game_uploads
  for select using (
    (select role from public.profiles where id = auth.uid()) in ('instructor','admin')
  );
create policy "Staff update uploads" on public.game_uploads
  for update using (
    (select role from public.profiles where id = auth.uid()) in ('instructor','admin')
  );
create policy "Parent read child uploads" on public.game_uploads
  for select using (
    exists (select 1 from public.parent_student ps
            where ps.parent_id = auth.uid() and ps.student_id = game_uploads.student_id)
  );

-- parent_student
create policy "Admin manage links" on public.parent_student
  for all using (
    (select role from public.profiles where id = auth.uid()) = 'admin'
  );
create policy "Parent read own links" on public.parent_student
  for select using (auth.uid() = parent_id);
