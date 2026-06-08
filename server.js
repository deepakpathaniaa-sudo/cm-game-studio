const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

const pub = (file) => path.join(__dirname, 'public', file);

app.get('/',           (_, res) => res.sendFile(pub('login.html')));
app.get('/student',    (_, res) => res.sendFile(pub('student.html')));
app.get('/instructor', (_, res) => res.sendFile(pub('instructor.html')));
app.get('/parent',     (_, res) => res.sendFile(pub('parent.html')));
app.get('/admin',      (_, res) => res.sendFile(pub('admin.html')));

app.use(express.static(path.join(__dirname, 'public')));

app.listen(PORT, () => {
  console.log(`CM Game Studio running at http://localhost:${PORT}`);
  console.log(`  Login:      http://localhost:${PORT}/`);
  console.log(`  Student:    http://localhost:${PORT}/student`);
  console.log(`  Instructor: http://localhost:${PORT}/instructor`);
  console.log(`  Parent:     http://localhost:${PORT}/parent`);
  console.log(`  Admin:      http://localhost:${PORT}/admin`);
});
