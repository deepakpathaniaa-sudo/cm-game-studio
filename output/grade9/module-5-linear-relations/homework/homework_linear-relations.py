#!/usr/bin/env python3
"""Concept Mastery — Grade 9 (MTH1W) Linear Relations — HOMEWORK + KEY.

6 questions per level (L1/L2/L3 = 18), distinct concepts, open working space
under each question (no ruled lines). Curriculum: MTH1W. Full worked key.
Run: python3 homework_linear-relations.py
"""
import os, sys
ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "_assets"))
sys.path.insert(0, ASSETS)
from cm_pdf import CMFlow, ST_BODY, CM_BLUE, __version__

DIR = os.path.dirname(__file__)
OUT_Q = os.path.join(DIR, "homework_linear-relations.pdf")
OUT_A = os.path.join(DIR, "homework_linear-relations_answers.pdf")
TOPIC = "Linear Relations"
SUBTITLE = "First Differences · Direct & Partial Variation · Slope · Intercepts · Equations of Lines · Standard Form"

ITEMS = [
    # ── L1 (6) ──
    ("L1", "First differences", "The y-values in a table are 6, 10, 14, 18. Find the first differences and state whether the relation is linear.",
     ["Differences: 10-6 = 4, 14-10 = 4, 18-14 = 4.", "Constant (4), so the relation is linear."]),
    ("L1", "Direct or partial", "Is y = 7x + 1 direct or partial variation? Give a reason.",
     ["y-intercept is 1, which is not 0.", "So it is partial variation."]),
    ("L1", "Slope", "Find the slope of the line through (2, 4) and (5, 13).",
     ["slope = (13 - 4)/(5 - 2) = 9/3.", "= 3."]),
    ("L1", "y-intercept", "State the y-intercept of the line y = 5x - 8.",
     ["The constant term is the y-intercept: -8, at (0, -8)."]),
    ("L1", "x-intercept", "Find the x-intercept of the line y = 2x - 10.",
     ["Let y = 0: 0 = 2x - 10 → 2x = 10 → x = 5, at (5, 0)."]),
    ("L1", "Standard form", "Write y = 4x + 1 in the standard form Ax + By + C = 0.",
     ["Move all terms to one side: 4x - y + 1 = 0."]),
    # ── L2 (6) ──
    ("L2", "First differences", "The y-values in a table are 3, 6, 11, 18. Find the first differences and decide whether the relation is linear.",
     ["Differences: 3, 5, 7.", "Not constant, so the relation is non-linear."]),
    ("L2", "Direct variation", "A direct variation passes through (5, 15). Find the constant k and write the equation.",
     ["k = y/x = 15/5 = 3.", "Equation: y = 3x."]),
    ("L2", "Slope", "Find the slope of the line through (-3, 8) and (1, -4).",
     ["slope = (-4 - 8)/(1 - (-3)) = -12/4.", "= -3."]),
    ("L2", "Both intercepts", "Find the x-intercept and the y-intercept of 3x + 4y = 24.",
     ["x-int: y = 0 → 3x = 24 → (8, 0).", "y-int: x = 0 → 4y = 24 → (0, 6)."]),
    ("L2", "Equation of a line", "Find the equation of the line with slope 2 that passes through (3, 5).",
     ["5 = 2(3) + b → 5 = 6 + b → b = -1.", "y = 2x - 1."]),
    ("L2", "Standard form", "Write y = (2/3)x - 4 in standard form with integer coefficients.",
     ["Multiply every term by 3: 3y = 2x - 12.", "Rearrange: 2x - 3y - 12 = 0."]),
    # ── L3 (6) ──
    ("L3", "Missing table value", "A linear table gives y = 1, ?, 13, 19 for x = 0, 1, 2, 3. Find the missing value and explain.",
     ["The relation is linear, so first differences are equal.",
      "From y = 1 to y = 13 over two steps is +12, so +6 each step.", "Missing value: 1 + 6 = 7."]),
    ("L3", "Partial variation model", "A gym charges a $20 joining fee plus $15 per month: C = 15m + 20. Find the cost for 6 months and state the fixed value.",
     ["C = 15(6) + 20 = 90 + 20 = $110.", "The fixed value (joining fee) is $20."]),
    ("L3", "Unknown coordinate", "The line through (2, 5) and (k, 17) has slope 4. Find k.",
     ["(17 - 5)/(k - 2) = 4 → 12 = 4(k - 2).", "k - 2 = 3 → k = 5."]),
    ("L3", "Equation from intercepts", "A line has x-intercept -4 and y-intercept 8. Write its equation.",
     ["Through (-4, 0) and (0, 8): slope = (8 - 0)/(0 - (-4)) = 8/4 = 2.", "y-intercept is 8, so y = 2x + 8."]),
    ("L3", "Line through two points", "Find the equation of the line through (-1, 2) and (3, 14).",
     ["slope = (14 - 2)/(3 - (-1)) = 12/4 = 3.", "2 = 3(-1) + b → 2 = -3 + b → b = 5.", "y = 3x + 5."]),
    ("L3", "Correlation reasoning", "A scatter plot of ice-cream sales versus daily temperature shows points rising to the right in a tight band. Describe the correlation and what it suggests.",
     ["A strong positive linear correlation.",
      "As temperature rises, ice-cream sales tend to rise, so temperature is a good predictor of sales."]),
]


def build_questions():
    d = CMFlow(OUT_Q, topic_title=TOPIC, subtitle=SUBTITLE,
               info_line="MTH1W · Homework — Independent Practice", name_date=True)
    d.start()
    d.learning_goal("Practise first differences, variation, slope, intercepts, equations and standard form independently.")
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
