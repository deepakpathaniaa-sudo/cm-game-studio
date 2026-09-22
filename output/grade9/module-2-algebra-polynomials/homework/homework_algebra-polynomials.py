#!/usr/bin/env python3
"""Concept Mastery — Grade 9 (MTH1W) Algebra & Polynomials — HOMEWORK + KEY.

6 questions per level (L1/L2/L3 = 18), distinct concepts, open working space
under each question (no ruled lines). Curriculum: MTH1W. Full worked key.
Run: python3 homework_algebra-polynomials.py
"""
import os, sys
ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "_assets"))
sys.path.insert(0, ASSETS)
from cm_pdf import CMFlow, ST_BODY, CM_BLUE, __version__

DIR = os.path.dirname(__file__)
OUT_Q = os.path.join(DIR, "homework_algebra-polynomials.pdf")
OUT_A = os.path.join(DIR, "homework_algebra-polynomials_answers.pdf")
TOPIC = "Algebra & Polynomials"
SUBTITLE = "Like Terms · Substitution · Polynomials · Monomial Products & Quotients · Exponent Laws"

ITEMS = [
    # ── L1 (6) ──
    ("L1", "Like terms", "Simplify: 7x + 2x - 3x.", ["7x + 2x - 3x = 6x."]),
    ("L1", "Substitution", "Evaluate 5x - 4 when x = 3.", ["5(3) - 4 = 15 - 4 = 11."]),
    ("L1", "Add polynomials", "Simplify: (3a + 2) + (4a - 6).", ["(3a + 4a) + (2 - 6) = 7a - 4."]),
    ("L1", "Multiply by constant", "Expand: 6(2x - 3).", ["6·2x - 6·3 = 12x - 18."]),
    ("L1", "Divide by constant", "Simplify: (20x + 8) ÷ 4.", ["20x/4 + 8/4 = 5x + 2."]),
    ("L1", "Exponent law", "Simplify: x<super>6</super> · x<super>3</super>.", ["Add exponents: x<super>6+3</super> = x<super>9</super>."]),
    # ── L2 (6) ──
    ("L2", "Like terms", "Simplify: 5x - 3y - 2x + 8y - 4.", ["(5x - 2x) + (-3y + 8y) - 4 = 3x + 5y - 4."]),
    ("L2", "Substitution", "Evaluate 3a - 2b when a = 4 and b = 5.", ["3(4) - 2(5) = 12 - 10 = 2."]),
    ("L2", "Subtract polynomials", "Simplify: (6x<super>2</super> + 2x - 5) - (2x<super>2</super> - 3x + 1).",
     ["6x<super>2</super>-2x<super>2</super> = 4x<super>2</super>; 2x-(-3x)=5x; -5-1=-6.", "= 4x<super>2</super> + 5x - 6."]),
    ("L2", "Multiply by monomial", "Expand: 4x(3x - 2).", ["4x·3x - 4x·2 = 12x<super>2</super> - 8x."]),
    ("L2", "Divide by monomial", "Simplify: (18x<super>2</super> - 12x) ÷ 6x.", ["18x<super>2</super>/6x - 12x/6x = 3x - 2."]),
    ("L2", "Exponent laws", "Simplify: (3x<super>2</super>)(5x<super>4</super>).", ["Coefficients 3×5=15; add exponents: 15x<super>6</super>."]),
    # ── L3 (6) ──
    ("L3", "Find the error", "Priya wrote 2x + 3x = 5x<super>2</super>. Explain the error and give the correct answer.",
     ["Adding like terms adds the coefficients only; the variable's power is unchanged.",
      "2x + 3x = 5x, not 5x<super>2</super>."]),
    ("L3", "Area (substitute)", "The area of a square is A = s<super>2</super>. If s = 2x, write A in expanded form.",
     ["A = (2x)<super>2</super> = 2<super>2</super>x<super>2</super> = 4x<super>2</super>."]),
    ("L3", "Perimeter (polynomial)", "A rectangle has length (3x + 2) and width (x - 1). Find its perimeter in simplified form.",
     ["P = 2[(3x + 2) + (x - 1)] = 2(4x + 1) = 8x + 2."]),
    ("L3", "Expand & simplify", "Simplify: 3(2x - 1) - 2(x - 4).", ["6x - 3 - 2x + 8 = 4x + 5."]),
    ("L3", "Divide polynomial", "Simplify: (10x<super>3</super> - 15x<super>2</super> + 5x) ÷ 5x.",
     ["Divide each term by 5x: 2x<super>2</super> - 3x + 1."]),
    ("L3", "Power of a monomial", "Simplify: (2a<super>3</super>b<super>2</super>)<super>2</super>.",
     ["Square each factor: 2<super>2</super>a<super>6</super>b<super>4</super> = 4a<super>6</super>b<super>4</super>."]),
]


def build_questions():
    d = CMFlow(OUT_Q, topic_title=TOPIC, subtitle=SUBTITLE,
               info_line="MTH1W · Homework — Independent Practice", name_date=True)
    d.start()
    d.learning_goal("Practise simplifying, evaluating and operating on polynomials independently.")
    d.body("Show your full working in the space provided under each question. Levels: L1 fluency, "
           "L2 application, L3 thinking. Full worked solutions are in the Answer Key.", ST_BODY, gap=12)
    last = None
    for i, (lvl, concept, stem, _s) in enumerate(ITEMS, start=1):
        if lvl != last:
            names = {"L1": "Level 1 — Fluency", "L2": "Level 2 — Application", "L3": "Level 3 — Thinking"}
            d.heading(names[lvl], color=CM_BLUE); last = lvl
        wp = {"L1": 70, "L2": 100, "L3": 135}[lvl]
        d.question(i, f"{stem}  <font color='#2D7DD2'><b>[{concept}]</b></font>", answer="work", work_pts=wp)
    return d.build()


def build_answers():
    d = CMFlow(OUT_A, topic_title=TOPIC, subtitle="Answer Key — Worked Solutions",
               info_line="MTH1W · Homework — Answer Key")
    d.start()
    d.body("Worked solutions with method lines. Curriculum: MTH1W (Grade 9 de-streamed math).", ST_BODY, gap=12)
    for i, (lvl, concept, stem, sol) in enumerate(ITEMS, start=1):
        d.key_entry(i, [f"<b>[{lvl} · {concept}]</b> " + sol[0]] + sol[1:])
    return d.build()


if __name__ == "__main__":
    p = build_questions(); a = build_answers()
    from collections import Counter
    print(f"engine {__version__}  built {p} and {a}")
    print(f"items={len(ITEMS)}  by-level {dict(Counter(x[0] for x in ITEMS))}")
