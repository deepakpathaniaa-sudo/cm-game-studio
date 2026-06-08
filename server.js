const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'student.html'));
});

app.get('/instructor', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'instructor.html'));
});

app.listen(PORT, () => {
  console.log(`Concept Mastery Game Studio running at http://localhost:${PORT}`);
  console.log(`  Student view:    http://localhost:${PORT}/`);
  console.log(`  Instructor view: http://localhost:${PORT}/instructor`);
});
