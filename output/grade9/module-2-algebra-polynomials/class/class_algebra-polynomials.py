#!/usr/bin/env python3
"""Concept Mastery — Grade 9 (MTH1W) Algebra & Polynomials — CLASS COPY.

Template matches approved Module 1: warm-up, then per sub-topic one worked
Example + 3-4 questions of rising complexity, generous open work space (no
ruled lines). Curriculum tag: MTH1W. Answers on final page.
Run: python3 class_algebra-polynomials.py
"""
import os, sys
ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "_assets"))
sys.path.insert(0, ASSETS)
from cm_pdf import CMFlow, ST_BODY, CM_BLUE, CM_MED_BLUE, __version__

OUT = os.path.join(os.path.dirname(__file__), "class_algebra-polynomials.pdf")
TOPIC = "Algebra & Polynomials"
SUBTITLE = "Like Terms · Substitution · Polynomials · Monomial Products & Quotients · Exponent Laws"
INFO = "MTH1W · Class — Guided Practice"

SUBTOPICS = [
    ("Collecting Like Terms",
     ["Simplify 5x + 3y - 2x + 4y.",
      "Group like terms: (5x - 2x) + (3y + 4y).",
      "= 3x + 7y.   Answer: 3x + 7y."],
     [("L1", "Simplify: 8a + 3a - 2a.", "9a"),
      ("L1", "Simplify: 6x + 4 - 2x + 5.", "4x + 9"),
      ("L2", "Simplify: 3m - 5n + 7m + 2n - 4.", "10m - 3n - 4"),
      ("L3", "A student wrote 4x + 3x<super>2</super> = 7x<super>3</super>. Explain the error and give the correct simplification.",
       "4x and 3x<super>2</super> are not like terms (different powers), so they cannot be combined: 3x<super>2</super> + 4x.")]),
    ("Evaluating by Substitution",
     ["Evaluate 3x - 2 when x = 4.",
      "Substitute: 3(4) - 2 = 12 - 2.",
      "= 10.   Answer: 10."],
     [("L1", "Evaluate 2x + 5 when x = 3.", "2(3)+5 = 11"),
      ("L2", "Evaluate 4a - b when a = 2 and b = -3.", "4(2) - (-3) = 8 + 3 = 11"),
      ("L2", "Evaluate x<super>2</super> - 3x when x = 5.", "25 - 15 = 10"),
      ("L3", "The cost of renting a hall is C = 15n + 40, where n is the number of hours. Find the cost for 6 hours and state what the 40 represents.",
       "C = 15(6) + 40 = $130; the 40 is the fixed base fee.")]),
    ("Adding & Subtracting Polynomials",
     ["Simplify (3x<super>2</super> + 2x - 1) + (x<super>2</super> - 5x + 4).",
      "Combine like terms: (3x<super>2</super>+x<super>2</super>) + (2x-5x) + (-1+4).",
      "= 4x<super>2</super> - 3x + 3."],
     [("L1", "Simplify: (2x + 3) + (5x - 1).", "7x + 2"),
      ("L2", "Simplify: (4a<super>2</super> - 2a + 6) - (a<super>2</super> + 3a - 2).", "3a<super>2</super> - 5a + 8"),
      ("L2", "Subtract (2x<super>2</super> - x) from (5x<super>2</super> + 3x).", "3x<super>2</super> + 4x"),
      ("L3", "A triangle has perimeter (9x + 4). Two sides are (3x + 1) and (2x - 3). Find the third side.",
       "(9x+4) - (3x+1) - (2x-3) = 4x + 6.")]),
    ("Multiplying by a Constant or Monomial",
     ["Expand 3(2x - 5) and 2x(x + 4).",
      "3(2x - 5) = 6x - 15.  2x(x + 4) = 2x<super>2</super> + 8x.",
      "Distribute the factor to every term."],
     [("L1", "Expand: 4(x + 3).", "4x + 12"),
      ("L1", "Expand: -2(3a - 5).", "-6a + 10"),
      ("L2", "Expand: 3x(2x - 4).", "6x<super>2</super> - 12x"),
      ("L3", "Expand and simplify: 5(2x - 3) - 2(x - 4).", "10x - 15 - 2x + 8 = 8x - 7")]),
    ("Dividing by a Constant or Monomial",
     ["Simplify (6x + 9) ÷ 3 and (8x<super>2</super> - 4x) ÷ 4x.",
      "(6x + 9) ÷ 3 = 2x + 3.  (8x<super>2</super> - 4x) ÷ 4x = 2x - 1.",
      "Divide every term by the divisor."],
     [("L1", "Simplify: (10x + 15) ÷ 5.", "2x + 3"),
      ("L2", "Simplify: (12a<super>2</super> - 8a) ÷ 4.", "3a<super>2</super> - 2a"),
      ("L2", "Simplify: (15x<super>2</super> + 10x) ÷ 5x.", "3x + 2"),
      ("L3", "Simplify: (6x<super>3</super> - 9x<super>2</super> + 3x) ÷ 3x.", "2x<super>2</super> - 3x + 1")]),
    ("Exponent Laws Applied to Terms",
     ["Simplify (2x<super>2</super>)(3x<super>4</super>) and (x<super>5</super>) ÷ (x<super>2</super>).",
      "Multiply: coefficients 2×3=6, add exponents → 6x<super>6</super>.",
      "Divide: subtract exponents → x<super>3</super>."],
     [("L1", "Simplify: a<super>3</super> · a<super>4</super>.", "a<super>7</super>"),
      ("L1", "Simplify: (2m<super>3</super>)(4m<super>2</super>).", "8m<super>5</super>"),
      ("L2", "Simplify: (12x<super>5</super>) ÷ (3x<super>2</super>).", "4x<super>3</super>"),
      ("L3", "Simplify: (2a<super>2</super>b)<super>3</super>.", "8a<super>6</super>b<super>3</super>")]),
]

WARMUP = [
    ("Simplify: 4a + 6a.", "10a"),
    ("State the coefficient of the term -5x<super>2</super>.", "-5"),
    ("Simplify: 7m - m.", "6m"),
]


def build():
    d = CMFlow(OUT, topic_title=TOPIC, subtitle=SUBTITLE, info_line=INFO, name_date=True)
    d.start()
    d.learning_goal("Simplify, evaluate, add, subtract, multiply and divide polynomials using exponent laws.")
    d.heading("Warm-up  (quick recall)")
    for i, (stem, _a) in enumerate(WARMUP, start=1):
        d.question(i, stem, answer="work", work_pts=30)
    d.heading("Examples & Practice")
    d.body("For each skill, study the worked <b>Example</b>, then solve the questions that follow. "
           "Difficulty rises within each set (L1 → L3). Answers are on the last page.", ST_BODY, gap=10)
    n = len(WARMUP); answers = []
    for name, example, qs in SUBTOPICS:
        d.heading(name, color=CM_MED_BLUE)
        d.example_box(example)
        for lvl, stem, ans in qs:
            n += 1
            tagged = f"{stem}  <font color='#2D7DD2'><b>[{lvl}]</b></font>"
            wp = {"L1": 60, "L2": 95, "L3": 130}[lvl]
            d.question(n, tagged, answer="work", work_pts=wp)
            answers.append((n, lvl, ans))
    d._new_page()
    d.c.setFillColor(CM_BLUE); d.c.setFont("DejaVuSans-Bold", 16)
    d.c.drawCentredString(306, d.y, "Answers"); d.y -= 28
    wu = "   ".join(f"W{i}) {a}" for i, (_s, a) in enumerate(WARMUP, start=1))
    d.body("<b>Warm-up:</b> " + wu, ST_BODY, gap=12)
    for num, lvl, ans in answers:
        d.key_entry(num, [f"({lvl}) {ans}"])
    return d.build(), len(answers)


if __name__ == "__main__":
    p, n = build()
    print(f"engine {__version__}  built {p}  practice_questions={n}")
