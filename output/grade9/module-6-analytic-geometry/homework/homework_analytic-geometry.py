#!/usr/bin/env python3
"""Concept Mastery — Grade 9 (MTH1W) Analytic Geometry — HOMEWORK + KEY.

6 questions per level (L1/L2/L3 = 18), distinct concepts, open working space
under each question (no ruled lines). Curriculum: MTH1W. Full worked key.
Run: python3 homework_analytic-geometry.py
"""
import os, sys
ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "_assets"))
sys.path.insert(0, ASSETS)
from cm_pdf import CMFlow, ST_BODY, CM_BLUE, __version__

DIR = os.path.dirname(__file__)
OUT_Q = os.path.join(DIR, "homework_analytic-geometry.pdf")
OUT_A = os.path.join(DIR, "homework_analytic-geometry_answers.pdf")
TOPIC = "Analytic Geometry"
SUBTITLE = "Slope · Graphing Lines · Parallel & Perpendicular Lines · Length of a Segment · Midpoint"

ITEMS = [
    # ── L1 (6) ──
    ("L1", "Slope", "Find the slope of the line y = 6x + 1.", ["The coefficient of x is the slope: m = 6."]),
    ("L1", "Graphing", "State the slope and the y-intercept of y = x - 5.", ["Slope = 1; y-intercept (0, -5)."]),
    ("L1", "Parallel", "State the slope of any line parallel to y = 5x - 3.", ["Parallel lines share the slope: m = 5."]),
    ("L1", "Perpendicular", "State the slope of a line perpendicular to a line with slope 4.",
     ["Negative reciprocal of 4 is -1/4."]),
    ("L1", "Length", "Find the length of the segment from (0, 0) to (3, 4).",
     ["d = √[3<super>2</super> + 4<super>2</super>] = √[9 + 16] = √25 = 5."]),
    ("L1", "Midpoint", "Find the midpoint of (2, 2) and (8, 6).",
     ["M = ((2+8)/2, (2+6)/2) = (5, 4)."]),
    # ── L2 (6) ──
    ("L2", "Slope", "Find the slope of the line through (2, -1) and (6, 7).",
     ["m = (7 - (-1))/(6 - 2) = 8/4 = 2."]),
    ("L2", "Graphing", "For y = -2x + 8, find the x-intercept and the y-intercept.",
     ["y-intercept (0, 8); x-intercept: 0 = -2x + 8 → x = 4 → (4, 0)."]),
    ("L2", "Parallel", "Write the equation of the line parallel to y = 4x - 7 that passes through (0, 3).",
     ["Same slope 4, y-intercept 3: y = 4x + 3."]),
    ("L2", "Perpendicular", "State the slope of a line perpendicular to y = (2/3)x + 1.",
     ["Negative reciprocal of 2/3 is -3/2."]),
    ("L2", "Length", "Find the length of the segment from (-1, 2) to (11, 7).",
     ["d = √[12<super>2</super> + 5<super>2</super>] = √[144 + 25] = √169 = 13."]),
    ("L2", "Midpoint", "Find the midpoint of (-3, 5) and (7, -1).",
     ["M = ((-3+7)/2, (5-1)/2) = (2, 2)."]),
    # ── L3 (6) ──
    ("L3", "Slope", "The line through (1, 4) and (5, k) has slope 3. Find the value of k.",
     ["(k - 4)/(5 - 1) = 3, so k - 4 = 12, giving k = 16."]),
    ("L3", "Graphing", "Rewrite 4x - 2y = 8 in the form y = mx + b, then state the slope and y-intercept.",
     ["-2y = -4x + 8, so y = 2x - 4.", "Slope = 2; y-intercept (0, -4)."]),
    ("L3", "Parallel", "Determine whether the line through (0, 1) and (3, 10) is parallel to y = 3x - 4.",
     ["Slope = (10 - 1)/(3 - 0) = 9/3 = 3, equal to 3, so yes — the lines are parallel."]),
    ("L3", "Perpendicular", "Are y = 3x + 2 and y = -(1/3)x - 5 perpendicular? Justify.",
     ["Slopes are 3 and -1/3; product = 3 × (-1/3) = -1, so yes — they are perpendicular."]),
    ("L3", "Length", "A triangle has vertices A(1, 1), B(1, 5) and C(4, 1). Find its perimeter.",
     ["AB = 4 (vertical), AC = 3 (horizontal), BC = √[3<super>2</super> + 4<super>2</super>] = 5.",
      "Perimeter = 4 + 3 + 5 = 12."]),
    ("L3", "Midpoint", "M(3, -2) is the midpoint of P(-1, 4) and Q. Find the coordinates of Q.",
     ["Q = (2·3 - (-1), 2·(-2) - 4) = (7, -8)."]),
]


def build_questions():
    d = CMFlow(OUT_Q, topic_title=TOPIC, subtitle=SUBTITLE,
               info_line="MTH1W · Homework — Independent Practice", name_date=True)
    d.start()
    d.learning_goal("Practise slope, graphing, parallel/perpendicular lines, length and midpoint independently.")
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
