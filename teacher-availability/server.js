// ─────────────────────────────────────────────────────────────
// Teacher Availability — Express app (runs locally and on Vercel).
//   • Teachers register / log in to manage their availability.
//   • Parents browse & search availability with NO login.
// Storage backend is chosen in store.js (Supabase or JSON file).
// Auth: scrypt password hashing + HttpOnly session cookie (built-in crypto).
// ─────────────────────────────────────────────────────────────
const express = require('express');
const crypto = require('crypto');
const path = require('path');
const { store, SESSION_TTL_MS } = require('./store');

const app = express();
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// ─── constants & helpers ──────────────────────────────────────
const DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
const MODES = ['Online', 'In-person'];
const STATUSES = ['open', 'booked'];

const clean = (s) => String(s == null ? '' : s).trim();
const isTime = (s) => typeof s === 'string' && /^([01]\d|2[0-3]):[0-5]\d$/.test(s);

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
  (req.headers.cookie || '').split(';').forEach((p) => {
    const i = p.indexOf('=');
    if (i > -1) out[p.slice(0, i).trim()] = decodeURIComponent(p.slice(i + 1).trim());
  });
  return out;
}
function setSessionCookie(res, token) {
  const secure = process.env.NODE_ENV === 'production' ? ' Secure;' : '';
  res.setHeader('Set-Cookie',
    `ta_session=${token}; HttpOnly; SameSite=Lax; Path=/;${secure} Max-Age=${SESSION_TTL_MS / 1000}`);
}
async function currentTeacher(req) {
  const token = parseCookies(req).ta_session;
  if (!token) return null;
  const sess = await store.getSession(token);
  if (!sess) return null;
  return store.getTeacherById(sess.teacherId);
}
function requireTeacher(handler) {
  return async (req, res) => {
    try {
      const t = await currentTeacher(req);
      if (!t) return res.status(401).json({ error: 'Not signed in.' });
      req.teacher = t;
      await handler(req, res);
    } catch (e) { res.status(500).json({ error: e.message || 'Server error.' }); }
  };
}
const pub = (t) => ({ id: t.id, name: t.name, email: t.email, subjects: t.subjects || [] });

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

// ─── AUTH ─────────────────────────────────────────────────────
app.post('/api/auth/register', async (req, res) => {
  try {
    const name = clean(req.body.name);
    const email = clean(req.body.email).toLowerCase();
    const password = String(req.body.password || '');
    const subjects = Array.isArray(req.body.subjects)
      ? req.body.subjects.map(clean).filter(Boolean)
      : clean(req.body.subjects).split(',').map((s) => s.trim()).filter(Boolean);
    if (!name) return res.status(400).json({ error: 'Name is required.' });
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return res.status(400).json({ error: 'Enter a valid email.' });
    if (password.length < 6) return res.status(400).json({ error: 'Password must be at least 6 characters.' });
    if (await store.findTeacherByEmail(email)) return res.status(409).json({ error: 'An account with that email already exists.' });
    const teacher = await store.createTeacher({ name, email, subjects, pass: hashPassword(password) });
    const token = crypto.randomBytes(24).toString('hex');
    await store.createSession(token, teacher.id);
    setSessionCookie(res, token);
    res.json({ teacher: pub(teacher) });
  } catch (e) { res.status(500).json({ error: e.message || 'Server error.' }); }
});

app.post('/api/auth/login', async (req, res) => {
  try {
    const email = clean(req.body.email).toLowerCase();
    const password = String(req.body.password || '');
    const teacher = await store.findTeacherByEmail(email);
    if (!teacher || !verifyPassword(password, teacher.pass)) return res.status(401).json({ error: 'Wrong email or password.' });
    const token = crypto.randomBytes(24).toString('hex');
    await store.createSession(token, teacher.id);
    setSessionCookie(res, token);
    res.json({ teacher: pub(teacher) });
  } catch (e) { res.status(500).json({ error: e.message || 'Server error.' }); }
});

app.post('/api/auth/logout', async (req, res) => {
  try {
    const token = parseCookies(req).ta_session;
    if (token) await store.deleteSession(token);
    res.setHeader('Set-Cookie', 'ta_session=; HttpOnly; SameSite=Lax; Path=/; Max-Age=0');
    res.json({ ok: true });
  } catch (e) { res.status(500).json({ error: e.message || 'Server error.' }); }
});

app.get('/api/me', async (req, res) => {
  try {
    const t = await currentTeacher(req);
    res.json({ teacher: t ? pub(t) : null });
  } catch (e) { res.status(500).json({ error: e.message || 'Server error.' }); }
});

// ─── TEACHER SLOTS (auth required) ────────────────────────────
app.get('/api/my-slots', requireTeacher(async (req, res) => {
  res.json({ slots: await store.listSlotsByTeacher(req.teacher.id) });
}));

app.post('/api/slots', requireTeacher(async (req, res) => {
  const v = validateSlot(req.body);
  if (v.error) return res.status(400).json({ error: v.error });
  const slot = await store.createSlot({ teacher_id: req.teacher.id, teacher_name: req.teacher.name, ...v.value });
  res.json({ slot });
}));

app.put('/api/slots/:id', requireTeacher(async (req, res) => {
  const owned = await store.getOwnedSlot(req.params.id, req.teacher.id);
  if (!owned) return res.status(404).json({ error: 'Slot not found.' });
  const v = validateSlot(req.body);
  if (v.error) return res.status(400).json({ error: v.error });
  const slot = await store.updateSlot(req.params.id, req.teacher.id, { ...v.value, teacher_name: req.teacher.name });
  res.json({ slot });
}));

app.delete('/api/slots/:id', requireTeacher(async (req, res) => {
  const ok = await store.deleteSlot(req.params.id, req.teacher.id);
  if (!ok) return res.status(404).json({ error: 'Slot not found.' });
  res.json({ ok: true });
}));

// ─── PUBLIC SEARCH (no login) ─────────────────────────────────
app.get('/api/availability', async (req, res) => {
  try {
    const filters = {
      name: clean(req.query.name),
      subject: clean(req.query.subject),
      day: clean(req.query.day),
      grade: clean(req.query.grade),
      openOnly: req.query.open === '1' || req.query.open === 'true',
    };
    const [slots, subjects] = await Promise.all([store.availability(filters), store.subjects()]);
    res.json({ slots, subjects });
  } catch (e) { res.status(500).json({ error: e.message || 'Server error.' }); }
});

// ─── PAGES ────────────────────────────────────────────────────
app.get('/', (_, res) => res.sendFile(path.join(__dirname, 'public', 'index.html')));
app.get('/teacher', (_, res) => res.sendFile(path.join(__dirname, 'public', 'teacher.html')));
app.get('/healthz', (_, res) => res.json({ ok: true, backend: store.backend }));

// ─── start (local only; on Vercel the app is exported as a handler) ──
if (require.main === module) {
  const PORT = process.env.PORT || 4000;
  app.listen(PORT, () => {
    console.log(`Teacher Availability running at http://localhost:${PORT}`);
    console.log(`  Parents (public search): http://localhost:${PORT}/`);
    console.log(`  Teachers (login):        http://localhost:${PORT}/teacher`);
  });
}

module.exports = app;
