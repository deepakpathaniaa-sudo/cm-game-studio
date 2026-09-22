"""Programme-wide content shared by every Gauss G7 module (single source).
Original Concept Mastery content."""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
sys.path.insert(0, os.path.join(ROOT, "drills"))
OUT = os.path.join(ROOT, "output")

GRADE = 7
ORIGINALITY = "Original Concept Mastery items. Not reproduced from CEMC or any third party."
CEMC_URL = "https://cemc.uwaterloo.ca/contests/gauss"
CONTEST_FORMAT = ("Gauss Grade 7: 25 multiple-choice questions, five options (A)–(E), 60 minutes. "
                  "Part A Q1–10 at 5 points, Part B Q11–20 at 6 points, Part C Q21–25 at 8 points; maximum 150. "
                  "Confirm calculator and blank-answer rules on the current CEMC contest page before each sitting.")

ERROR_CODES = [
    ("C", "Concept", "I did not know or misunderstood the idea."),
    ("R", "Representation", "I drew the wrong diagram, table or equation — or none."),
    ("S", "Strategy", "I had the idea but chose a slow or wrong plan."),
    ("A", "Arithmetic", "A calculation slip."),
    ("V", "Visual/spatial", "I misread a diagram or trusted how it looked."),
    ("Q", "Question-reading", "I answered a different question (units, ‘not’, ‘of what’)."),
    ("T", "Time", "I ran out of time or rushed."),
    ("K", "Knew-but-didn't-recall", "I knew it but could not bring it back in the moment."),
]

CORE_MOVES = [
    ("Draw it", "Lengths, shapes, movement or a story with parts",
     "Sketch it and label every number you are given."),
    ("Tabulate it", "Several cases, two quantities that change together, or ‘how many ways’",
     "Make a table; one row per case, in order."),
    ("Try a small case", "Huge numbers, ‘n’, or a pattern you cannot see",
     "Solve the same question with 1, 2, 3 — then look for the rule."),
    ("Work backward", "You know the end result and the steps",
     "Start at the end and undo each step in reverse order."),
    ("Eliminate options", "Five choices and a property you can test (even, multiple of 5, too big)",
     "Cross out the options that fail the test before calculating."),
    ("Check reasonableness", "Every question, last 10 seconds",
     "Estimate. Is the size right? The units? Did I answer what was asked?"),
]

# Pacing model (CM starting heuristic — adjust per student from mock data)
PACING = [
    ("Part A (Q1–10)", "15 min", "about 1.5 min each", "Bank all 50 points. Zero errors beats speed."),
    ("Part B (Q11–20)", "25 min", "about 2.5 min each", "Draw or tabulate before calculating."),
    ("Part C (Q21–25)", "15 min", "about 3 min each", "Attempt every question; record cases."),
    ("Check", "5 min", "—", "Re-read the question for every answer you marked ‘?’."),
]


def cm_pdf():
    import cm_pdf as m
    return m
