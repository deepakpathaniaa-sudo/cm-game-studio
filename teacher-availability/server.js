// ─────────────────────────────────────────────────────────────
// Teacher Availability — standalone Express app
//   • Teachers register / log in to manage their availability.
//   • Parents browse & search availability with NO login.
// Storage: a single JSON file (data/db.json). No external services.
// Auth: password hashing via Node's built-in crypto (scrypt);
//       session token in an HttpOnly cookie. No auth libraries.
// ─────────────────────────────────────────────────────────────
const express = require('express');
const crypto = require('crypto');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 4000;

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// ─── tiny JSON "database" ─────────────────────────────────────
const DATA_DIR = path.join(__dirname, 'data');
const DB_FILE = path.join(DATA_DIR, 'db.json');
if (!fs.existsSync(DATA_DIR)) fs.mkdirSync(DATA_DIR, { recursive: true });

let db = { teachers: [], slots: [], sessions: {} };
if (fs.existsSync(DB_FILE)) {
  try { db = JSON.parse(fs.readFileSync(DB_FILE, 'utf8')); }
  catch { console.error('Could not parse db.json — starting empty.'); }
}
for (const k of ['teachers', 'slots', 'sessions']) db[k] = db[k] || (k === 'sessions' ? {} : []);

let writeQueued = false;
function save() {
  // debounce rapid writes into one flush
  if (writeQueued) return;
  writeQueued = true;
  setImmediate(() => {
    writeQueued = false;
    const tmp = DB_FILE + '.tmp';
    fs.writeFileSync(tmp, JSON.stringify(db, null, 2));
    fs.renameSync(tmp, DB_FILE); // atomic replace
  });
}

// ─── auth helpers ─────────────────────────────────────────────
const DAYS = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'];
const MODES = ['Online', 'In-person'];
const STATUSES = ['open', 'booked'];
const SESSION_TTL = 1000 * 60 * 60 * 24 * 30; // 30 days

function hashPassword(pw) {
  const salt = crypto.randomBytes(16).toString('hex');
  const hash = crypto.scryptSync(pw, salt, 64).toString('hex');
  return `${salt}:${hash}`;
}
function verifyPassword(pw, stored) {
  const [salt, hash] = String(stored).split(':');
  if (!salt || !hash) return false;
  const test = crypto.scryptSync(pw, salt, 64).toString('hex');
  const a = Buffer.from(test, 'hex'), b = Buffer.from(hash, 'hex');
  return a.length === b.length && crypto.timingSafeEqual(a, b);
}
function parseCookies(req) {
  const out = {};
  (req.headers.cookie || '').split(';').forEach(p => {
    const i = p.indexOf('=');
    if (i > -1) out[p.slice(0, i).trim()] = decodeURIComponent(p.slice(i + 1).trim());
  });
  return out;
}
function currentTeacher(req) {
  const token = parseCookies(req).ta_session;
  if (!token) return null;
  const sess = db.sessions[token];
  if (!sess) return null;
  if (Date.now() - sess.createdAt > SESSION_TTL) { delete db.sessions[token]; save(); return null; }
  return db.teachers.find(t => t.id === sess.teacherId) || null;
}
function requireTeacher(req, res, next) {
  const t = currentTeacher(req);
  if (!t) return res.status(401).json({ error: 'Not signed in.' });
  req.teacher = t;
  next();
}
function publicTeacher(t) { return { id: t.id, name: t.name, email: t.email, subjects: t.subjects || [] }; }

const uid = () => crypto.randomBytes(9).toString('hex');
const isTime = s => typeof s === 'string' && /^([01]\d|2[0-3]):[0-5]\d$/.test(s);
const clean = s => String(s == null ? '' : s).trim();

function validateSlot(body) {
  const subject = clean(body.subject);
  if (!subject) return { error: 'Subject is required.' };
  const day = clean(body.day_of_week);
  if (!DAYS.includes(day)) return { error: 'Invalid day.' };
  if (!isTime(body.start_time) || !isTime(body.end_time)) return { error: 'Times must be HH:MM.' };
  if (body.end_time <= body.start_time) return { error: 'End time must be after start time.' };
  let grade = null;
  if (body.grade !== null && body.grade !== '' && body.grade !== undefined) {
    grade = parseInt(body.grade, 10);
    if (Number.isNaN(grade) || grade < 1 || grade > 12) return { error: 'Grade must be 1–12 or blank.' };
  }
  const mode = MODES.includes(body.mode) ? body.mode : 'Online';
  const status = STATUSES.includes(body.status) ? body.status : 'open';
  return { value: { subject, grade, day_of_week: day, start_time: body.start_time, end_time: body.end_time, mode, status, notes: clean(body.notes) || null } };
}

// ─── AUTH ROUTES ──────────────────────────────────────────────
app.post('/api/auth/register', (req, res) => {
  const name = clean(req.body.name);
  const email = clean(req.body.email).toLowerCase();
  const password = String(req.body.password || '');
  const subjects = Array.isArray(req.body.subjects)
    ? req.body.subjects.map(clean).filter(Boolean)
    : clean(req.body.subjects).split(',').map(s => s.trim()).filter(Boolean);
  if (!name) return res.status(400).json({ error: 'Name is required.' });
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return res.status(400).json({ error: 'Enter a valid email.' });
  if (password.length < 6) return res.status(400).json({ error: 'Password must be at least 6 characters.' });
  if (db.teachers.some(t => t.email === email)) return res.status(409).json({ error: 'An account with that email already exists.' });
  const teacher = { id: uid(), name, email, subjects, pass: hashPassword(password), created_at: new Date().toISOString() };
  db.teachers.push(teacher);
  startSession(res, teacher.id);
  save();
  res.json({ teacher: publicTeacher(teacher) });
});

app.post('/api/auth/login', (req, res) => {
  const email = clean(req.body.email).toLowerCase();
  const password = String(req.body.password || '');
  const teacher = db.teachers.find(t => t.email === email);
  if (!teacher || !verifyPassword(password, teacher.pass)) return res.status(401).json({ error: 'Wrong email or password.' });
  startSession(res, teacher.id);
  save();
  res.json({ teacher: publicTeacher(teacher) });
});

app.post('/api/auth/logout', (req, res) => {
  const token = parseCookies(req).ta_session;
  if (token) { delete db.sessions[token]; save(); }
  res.setHeader('Set-Cookie', 'ta_session=; HttpOnly; SameSite=Lax; Path=/; Max-Age=0');
  res.json({ ok: true });
});

app.get('/api/me', (req, res) => {
  const t = currentTeacher(req);
  res.json({ teacher: t ? publicTeacher(t) : null });
});

function startSession(res, teacherId) {
  const token = crypto.randomBytes(24).toString('hex');
  db.sessions[token] = { teacherId, createdAt: Date.now() };
  const secure = process.env.NODE_ENV === 'production' ? ' Secure;' : '';
  res.setHeader('Set-Cookie',
    `ta_session=${token}; HttpOnly; SameSite=Lax; Path=/;${secure} Max-Age=${SESSION_TTL / 1000}`);
}

// ─── TEACHER SLOT ROUTES (auth required) ──────────────────────
app.get('/api/my-slots', requireTeacher, (req, res) => {
  res.json({ slots: db.slots.filter(s => s.teacher_id === req.teacher.id) });
});

app.post('/api/slots', requireTeacher, (req, res) => {
  const v = validateSlot(req.body);
  if (v.error) return res.status(400).json({ error: v.error });
  const slot = {
    id: uid(),
    teacher_id: req.teacher.id,
    teacher_name: req.teacher.name,
    ...v.value,
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString(),
  };
  db.slots.push(slot);
  save();
  res.json({ slot });
});

app.put('/api/slots/:id', requireTeacher, (req, res) => {
  const slot = db.slots.find(s => s.id === req.params.id);
  if (!slot || slot.teacher_id !== req.teacher.id) return res.status(404).json({ error: 'Slot not found.' });
  const v = validateSlot(req.body);
  if (v.error) return res.status(400).json({ error: v.error });
  Object.assign(slot, v.value, { teacher_name: req.teacher.name, updated_at: new Date().toISOString() });
  save();
  res.json({ slot });
});

app.delete('/api/slots/:id', requireTeacher, (req, res) => {
  const i = db.slots.findIndex(s => s.id === req.params.id && s.teacher_id === req.teacher.id);
  if (i === -1) return res.status(404).json({ error: 'Slot not found.' });
  db.slots.splice(i, 1);
  save();
  res.json({ ok: true });
});

// ─── PUBLIC ROUTE (no login) — parents search here ────────────
app.get('/api/availability', (req, res) => {
  const name = clean(req.query.name).toLowerCase();
  const subject = clean(req.query.subject);
  const day = clean(req.query.day);
  const grade = clean(req.query.grade);
  const openOnly = req.query.open === '1' || req.query.open === 'true';

  const slots = db.slots.filter(s => {
    if (name && !s.teacher_name.toLowerCase().includes(name)) return false;
    if (subject && s.subject !== subject) return false;
    if (day && s.day_of_week !== day) return false;
    if (grade && s.grade !== null && String(s.grade) !== grade) return false;
    if (openOnly && s.status !== 'open') return false;
    return true;
  });
  const subjects = [...new Set(db.slots.map(s => s.subject))].sort((a, b) => a.localeCompare(b));
  res.json({ slots, subjects });
});

// ─── PAGES ────────────────────────────────────────────────────
app.get('/', (_, res) => res.sendFile(path.join(__dirname, 'public', 'index.html')));
app.get('/teacher', (_, res) => res.sendFile(path.join(__dirname, 'public', 'teacher.html')));

app.listen(PORT, () => {
  console.log(`Teacher Availability running at http://localhost:${PORT}`);
  console.log(`  Parents (public search): http://localhost:${PORT}/`);
  console.log(`  Teachers (login):        http://localhost:${PORT}/teacher`);
});
