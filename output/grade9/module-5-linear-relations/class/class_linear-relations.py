#!/usr/bin/env python3
"""Concept Mastery — Grade 9 (MTH1W) Linear Relations — CLASS COPY.

Template matches approved Module 1/2: warm-up, then per sub-topic one worked
Example + 3-4 questions of rising complexity, generous open work space (no
ruled lines). Curriculum tag: MTH1W. Answers on final page.
Run: python3 class_linear-relations.py
"""
import os, sys
ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "_assets"))
sys.path.insert(0, ASSETS)
from cm_pdf import CMFlow, ST_BODY, CM_BLUE, CM_MED_BLUE, __version__

OUT = os.path.join(os.path.dirname(__file__), "class_linear-relations.pdf")
TOPIC = "Linear Relations"
SUBTITLE = "First Differences · Direct & Partial Variation · Slope · Intercepts · Equations of Lines · Standard Form"
INFO = "MTH1W · Class — Guided Practice"

SUBTOPICS = [
    ("Patterns, Tables & First Differences",
     ["A table gives y-values 3, 7, 11, 15 for x = 0, 1, 2, 3. Are they linear?",
      "First differences: 7-3 = 4, 11-7 = 4, 15-11 = 4.",
      "The first differences are constant (4), so the relation is linear."],
     [("L1", "The y-values in a table are 2, 5, 8, 11. Find the first differences and state whether the relation is linear.",
       "Differences 3, 3, 3 are constant, so the relation is linear."),
      ("L1", "A pattern gives the values 4, 9, 14, 19. Are the first differences constant?",
       "Yes: 5, 5, 5 — constant, so it is linear."),
      ("L2", "For the y-values 1, 4, 9, 16, find the first differences and decide whether the relation is linear.",
       "Differences 3, 5, 7 are not constant, so the relation is non-linear."),
      ("L3", "A linear relation has first differences all equal to 6, and y = -2 when x = 0. Write the y-values for x = 0, 1, 2, 3.",
       "Add 6 each step: -2, 4, 10, 16.")]),
    ("Direct vs Partial Variation",
     ["Classify y = 5x and y = 5x + 2.",
      "y = 5x passes through (0, 0), so it is direct variation.",
      "y = 5x + 2 has y-intercept 2 (not 0), so it is partial variation."],
     [("L1", "State whether y = 3x is direct or partial variation.", "Direct variation (passes through the origin)."),
      ("L1", "State whether y = 2x + 7 is direct or partial variation.", "Partial variation (y-intercept 7 ≠ 0)."),
      ("L2", "A taxi charges a $3 flag fee plus $2 per kilometre: C = 2d + 3. Is this direct or partial variation, and what is the initial value?",
       "Partial variation; the initial value (fixed fee) is 3."),
      ("L3", "A partial variation has initial value 8 and rate of change 3. Write its equation and find y when x = 5.",
       "y = 3x + 8; at x = 5, y = 3(5) + 8 = 23.")]),
    ("Slope (Rise over Run, from Two Points)",
     ["Find the slope of the line through (1, 2) and (4, 11).",
      "slope = (11 - 2) / (4 - 1) = 9 / 3.",
      "slope = 3."],
     [("L1", "Find the slope of the line through (0, 0) and (2, 6).", "slope = 6/2 = 3."),
      ("L1", "Find the slope of the line through (1, 3) and (5, 11).", "slope = (11-3)/(5-1) = 8/4 = 2."),
      ("L2", "Find the slope of the line through (-2, 5) and (4, -7).",
       "slope = (-7-5)/(4-(-2)) = -12/6 = -2."),
      ("L3", "A line through (3, k) and (7, 20) has slope 3. Find k.",
       "(20 - k)/(7 - 3) = 3 → 20 - k = 12 → k = 8.")]),
    ("x- and y-Intercepts",
     ["Find the intercepts of y = 2x - 6.",
      "y-intercept: let x = 0 → y = -6, giving (0, -6).",
      "x-intercept: let y = 0 → 0 = 2x - 6 → x = 3, giving (3, 0)."],
     [("L1", "Find the y-intercept of y = 4x + 5.", "y-intercept = 5, at (0, 5)."),
      ("L1", "Find the x-intercept of y = x - 7.", "0 = x - 7 → x = 7, at (7, 0)."),
      ("L2", "For 2x + 3y = 12, find both the x-intercept and the y-intercept.",
       "x-int: y=0 → 2x=12 → (6, 0); y-int: x=0 → 3y=12 → (0, 4)."),
      ("L3", "A line has x-intercept 4 and y-intercept 8. Find its slope and its equation.",
       "Through (4, 0) and (0, 8): slope = (8-0)/(0-4) = -2; y = -2x + 8.")]),
    ("Equation of a Line — Slope + a Point, and from Two Points",
     ["Find the equation of the line with slope 3 through (2, 5).",
      "y = 3x + b, so 5 = 3(2) + b → b = -1.",
      "y = 3x - 1."],
     [("L1", "Write the equation of the line with slope 2 and y-intercept 4.", "y = 2x + 4."),
      ("L2", "Find the equation of the line with slope 4 that passes through (1, 7).",
       "7 = 4(1) + b → b = 3; y = 4x + 3."),
      ("L2", "Find the equation of the line with slope -1 that passes through (0, -3).",
       "y-intercept is -3; y = -x - 3."),
      ("L3", "Find the equation of the line through (2, 3) and (6, 15).",
       "slope = (15-3)/(6-2) = 12/4 = 3; 3 = 3(2)+b → b = -3; y = 3x - 3.")]),
    ("Standard Form Ax + By + C = 0, and Correlation & Linearity",
     ["Write y = 2x + 5 in standard form, and describe a rising scatter.",
      "Move all terms to one side: 2x - y + 5 = 0.",
      "A scatter whose points rise to the right in a tight band shows a strong positive linear correlation."],
     [("L1", "Write y = 3x - 4 in the standard form Ax + By + C = 0.", "3x - y - 4 = 0."),
      ("L2", "Write y = (1/2)x + 3 in standard form with integer coefficients.",
       "Multiply by 2: x - 2y + 6 = 0."),
      ("L2", "A scatter plot's points rise to the right and lie in a narrow band. Describe the correlation in words.",
       "A strong positive linear correlation."),
      ("L3", "A scatter plot of daily temperature versus hot-chocolate sales shows points falling steeply to the right in a tight band. Describe the correlation and what it means.",
       "A strong negative linear correlation: as temperature rises, hot-chocolate sales tend to fall.")]),
]

WARMUP = [
    ("Find the first differences for the y-values 5, 8, 11.", "3, 3"),
    ("Is y = 6x direct or partial variation?", "Direct"),
    ("Find the slope of the line through (0, 0) and (1, 4).", "4"),
]


def build():
    d = CMFlow(OUT, topic_title=TOPIC, subtitle=SUBTITLE, info_line=INFO, name_date=True)
    d.start()
    d.learning_goal("Represent, analyse and write linear relations using first differences, variation, slope, intercepts and equations.")
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
