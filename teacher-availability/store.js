// ─────────────────────────────────────────────────────────────
// Storage layer with two interchangeable backends:
//   • Supabase Postgres  — when SUPABASE_URL + SUPABASE_SECRET_KEY are set
//                          (used on Vercel / production; data persists).
//   • JSON file          — otherwise (local dev; data/db.json).
// The rest of the app only sees this async interface, never the backend.
// ─────────────────────────────────────────────────────────────
const SESSION_TTL_MS = 1000 * 60 * 60 * 24 * 30; // 30 days

const USE_SUPABASE = !!(process.env.SUPABASE_URL && process.env.SUPABASE_SECRET_KEY);

// ══════════════════════════ SUPABASE BACKEND ══════════════════════════
function supabaseStore() {
  const { createClient } = require('@supabase/supabase-js');
  const sb = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_SECRET_KEY, {
    auth: { persistSession: false, autoRefreshToken: false },
  });
  const die = (e) => { throw new Error(e.message || 'Database error'); };

  return {
    backend: 'supabase',
    async findTeacherByEmail(email) {
      const { data, error } = await sb.from('ta_teachers').select('*').eq('email', email).maybeSingle();
      if (error) die(error);
      return data || null;
    },
    async getTeacherById(id) {
      const { data, error } = await sb.from('ta_teachers').select('*').eq('id', id).maybeSingle();
      if (error) die(error);
      return data || null;
    },
    async createTeacher(t) {
      const { data, error } = await sb.from('ta_teachers')
        .insert({ name: t.name, email: t.email, subjects: t.subjects, pass: t.pass })
        .select().single();
      if (error) die(error);
      return data;
    },
    async createSession(token, teacherId) {
      const { error } = await sb.from('ta_sessions').insert({ token, teacher_id: teacherId });
      if (error) die(error);
    },
    async getSession(token) {
      const { data, error } = await sb.from('ta_sessions').select('*').eq('token', token).maybeSingle();
      if (error) die(error);
      if (!data) return null;
      if (Date.now() - new Date(data.created_at).getTime() > SESSION_TTL_MS) {
        await this.deleteSession(token);
        return null;
      }
      return { teacherId: data.teacher_id };
    },
    async deleteSession(token) {
      const { error } = await sb.from('ta_sessions').delete().eq('token', token);
      if (error) die(error);
    },
    async listSlotsByTeacher(teacherId) {
      const { data, error } = await sb.from('ta_slots').select('*').eq('teacher_id', teacherId);
      if (error) die(error);
      return data || [];
    },
    async createSlot(slot) {
      const { data, error } = await sb.from('ta_slots').insert(slot).select().single();
      if (error) die(error);
      return data;
    },
    async getOwnedSlot(id, teacherId) {
      const { data, error } = await sb.from('ta_slots').select('*')
        .eq('id', id).eq('teacher_id', teacherId).maybeSingle();
      if (error) die(error);
      return data || null;
    },
    async updateSlot(id, teacherId, fields) {
      const { data, error } = await sb.from('ta_slots')
        .update({ ...fields, updated_at: new Date().toISOString() })
        .eq('id', id).eq('teacher_id', teacherId).select().maybeSingle();
      if (error) die(error);
      return data || null;
    },
    async deleteSlot(id, teacherId) {
      const { data, error } = await sb.from('ta_slots').delete()
        .eq('id', id).eq('teacher_id', teacherId).select('id');
      if (error) die(error);
      return (data || []).length > 0;
    },
    async availability({ name, subject, day, grade, openOnly }) {
      let q = sb.from('ta_slots').select('*');
      if (name) q = q.ilike('teacher_name', `%${name}%`);
      if (subject) q = q.eq('subject', subject);
      if (day) q = q.eq('day_of_week', day);
      if (grade) q = q.or(`grade.is.null,grade.eq.${grade}`);
      if (openOnly) q = q.eq('status', 'open');
      const { data, error } = await q;
      if (error) die(error);
      return data || [];
    },
    async subjects() {
      const { data, error } = await sb.from('ta_slots').select('subject');
      if (error) die(error);
      return [...new Set((data || []).map((r) => r.subject))].sort((a, b) => a.localeCompare(b));
    },
  };
}

// ══════════════════════════ JSON FILE BACKEND ══════════════════════════
function fileStore() {
  const fs = require('fs');
  const path = require('path');
  const DATA_DIR = path.join(__dirname, 'data');
  const DB_FILE = path.join(DATA_DIR, 'db.json');
  if (!fs.existsSync(DATA_DIR)) fs.mkdirSync(DATA_DIR, { recursive: true });

  let db = { teachers: [], slots: [], sessions: {} };
  if (fs.existsSync(DB_FILE)) {
    try { db = JSON.parse(fs.readFileSync(DB_FILE, 'utf8')); } catch { /* start empty */ }
  }
  for (const k of ['teachers', 'slots']) db[k] = db[k] || [];
  db.sessions = db.sessions || {};

  let queued = false;
  const save = () => {
    if (queued) return; queued = true;
    setImmediate(() => {
      queued = false;
      const tmp = DB_FILE + '.tmp';
      fs.writeFileSync(tmp, JSON.stringify(db, null, 2));
      fs.renameSync(tmp, DB_FILE);
    });
  };
  const match = (s, { name, subject, day, grade, openOnly }) => {
    if (name && !s.teacher_name.toLowerCase().includes(name.toLowerCase())) return false;
    if (subject && s.subject !== subject) return false;
    if (day && s.day_of_week !== day) return false;
    if (grade && s.grade !== null && String(s.grade) !== String(grade)) return false;
    if (openOnly && s.status !== 'open') return false;
    return true;
  };

  return {
    backend: 'file',
    async findTeacherByEmail(email) { return db.teachers.find((t) => t.email === email) || null; },
    async getTeacherById(id) { return db.teachers.find((t) => t.id === id) || null; },
    async createTeacher(t) {
      const row = { id: require('crypto').randomBytes(9).toString('hex'), name: t.name, email: t.email, subjects: t.subjects, pass: t.pass, created_at: new Date().toISOString() };
      db.teachers.push(row); save(); return row;
    },
    async createSession(token, teacherId) { db.sessions[token] = { teacherId, createdAt: Date.now() }; save(); },
    async getSession(token) {
      const s = db.sessions[token];
      if (!s) return null;
      if (Date.now() - s.createdAt > SESSION_TTL_MS) { delete db.sessions[token]; save(); return null; }
      return { teacherId: s.teacherId };
    },
    async deleteSession(token) { delete db.sessions[token]; save(); },
    async listSlotsByTeacher(teacherId) { return db.slots.filter((s) => s.teacher_id === teacherId); },
    async createSlot(slot) {
      const row = { id: require('crypto').randomBytes(9).toString('hex'), ...slot, created_at: new Date().toISOString(), updated_at: new Date().toISOString() };
      db.slots.push(row); save(); return row;
    },
    async getOwnedSlot(id, teacherId) { return db.slots.find((s) => s.id === id && s.teacher_id === teacherId) || null; },
    async updateSlot(id, teacherId, fields) {
      const s = db.slots.find((x) => x.id === id && x.teacher_id === teacherId);
      if (!s) return null;
      Object.assign(s, fields, { updated_at: new Date().toISOString() }); save(); return s;
    },
    async deleteSlot(id, teacherId) {
      const i = db.slots.findIndex((s) => s.id === id && s.teacher_id === teacherId);
      if (i === -1) return false;
      db.slots.splice(i, 1); save(); return true;
    },
    async availability(f) {
      return db.slots.filter((s) => match(s, f));
    },
    async subjects() {
      return [...new Set(db.slots.map((s) => s.subject))].sort((a, b) => a.localeCompare(b));
    },
  };
}

const store = USE_SUPABASE ? supabaseStore() : fileStore();
console.log(`[store] backend: ${store.backend}`);
module.exports = { store, SESSION_TTL_MS };
