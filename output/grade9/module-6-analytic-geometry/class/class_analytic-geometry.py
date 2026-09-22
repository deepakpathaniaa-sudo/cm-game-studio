#!/usr/bin/env python3
"""Concept Mastery — Grade 9 (MTH1W) Analytic Geometry — CLASS COPY.

Template matches approved Module 2: warm-up, then per sub-topic one worked
Example + 3-4 questions of rising complexity, generous open work space (no
ruled lines). Curriculum tag: MTH1W. Answers on final page.
Run: python3 class_analytic-geometry.py
"""
import os, sys
ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "_assets"))
sys.path.insert(0, ASSETS)
from cm_pdf import CMFlow, ST_BODY, CM_BLUE, CM_MED_BLUE, __version__

OUT = os.path.join(os.path.dirname(__file__), "class_analytic-geometry.pdf")
TOPIC = "Analytic Geometry"
SUBTITLE = "Slope · Graphing Lines · Parallel & Perpendicular Lines · Length of a Segment · Midpoint"
INFO = "MTH1W · Class — Guided Practice"

SUBTOPICS = [
    ("Slope of a Line",
     ["Find the slope of the line through A(2, 3) and B(6, 11).",
      "m = (y<sub>2</sub> - y<sub>1</sub>) / (x<sub>2</sub> - x<sub>1</sub>) = (11 - 3) / (6 - 2) = 8 / 4.",
      "= 2.   Answer: slope = 2."],
     [("L1", "Find the slope of the line y = 5x - 2.", "The coefficient of x is the slope: m = 5."),
      ("L1", "Find the slope of the line through P(1, 2) and Q(5, 10).", "m = (10 - 2)/(5 - 1) = 8/4 = 2."),
      ("L2", "Find the slope of the line through (-3, 4) and (3, -8).", "m = (-8 - 4)/(3 - (-3)) = -12/6 = -2."),
      ("L3", "The line through (k, 3) and (6, 11) has slope 4. Find the value of k.",
       "8/(6 - k) = 4, so 6 - k = 2, giving k = 4.")]),
    ("Graphing Lines (describing the graph)",
     ["Describe the graph of y = 2x - 4.",
      "Slope = 2 (up 2, right 1); y-intercept (0, -4); x-intercept: 0 = 2x - 4 → (2, 0).",
      "Two points on the line: (0, -4) and (2, 0)."],
     [("L1", "For y = x + 3, state the slope and the y-intercept.", "Slope = 1; y-intercept (0, 3)."),
      ("L1", "For y = -2x + 6, state the y-intercept and find the x-intercept.",
       "y-intercept (0, 6); x-intercept: 0 = -2x + 6 → x = 3 → (3, 0)."),
      ("L2", "For y = 3x - 6, state the slope, the y-intercept, and two points on the line.",
       "Slope = 3; y-intercept (0, -6); e.g. (0, -6) and (2, 0)."),
      ("L3", "Describe the graph of 2x + y = 4: give slope, y-intercept and two plotted points.",
       "Rearrange to y = -2x + 4: slope = -2; y-intercept (0, 4); points (0, 4) and (2, 0).")]),
    ("Parallel Lines (equal slopes)",
     ["Are y = 3x + 1 and y = 3x - 5 parallel?",
      "Both lines have slope 3; the slopes are equal.",
      "Yes — parallel (same slope, different y-intercept)."],
     [("L1", "State the slope of any line parallel to y = 4x + 2.", "Parallel lines share the slope: m = 4."),
      ("L1", "Are y = 2x + 7 and y = 2x - 1 parallel? Explain.", "Yes; both have slope 2, so they are parallel."),
      ("L2", "Write the equation of the line parallel to y = -3x + 5 that passes through (0, 2).",
       "Same slope -3, y-intercept 2: y = -3x + 2."),
      ("L3", "Is the line through (1, 2) and (4, 8) parallel to y = 2x + 9? Justify.",
       "Slope = (8 - 2)/(4 - 1) = 6/3 = 2, equal to 2, so yes — parallel.")]),
    ("Perpendicular Lines (negative reciprocal slopes)",
     ["A line has slope 2. Find the slope of a line perpendicular to it.",
      "Perpendicular slope is the negative reciprocal of 2.",
      "= -1/2.   (Check: 2 × (-1/2) = -1.)"],
     [("L1", "State the slope of a line perpendicular to a line with slope 3.", "Negative reciprocal: -1/3."),
      ("L1", "State the slope of a line perpendicular to y = -4x + 1.",
       "Given slope -4; perpendicular slope = 1/4."),
      ("L2", "A line has slope 2/3. Find the slope of a line perpendicular to it.",
       "Negative reciprocal of 2/3 is -3/2."),
      ("L3", "Are y = 2x + 1 and y = -1/2 x + 4 perpendicular? Justify.",
       "Product of slopes = 2 × (-1/2) = -1, so yes — the lines are perpendicular.")]),
    ("Length of a Line Segment (distance formula)",
     ["Find the length of the segment from A(1, 2) to B(4, 6).",
      "d = √[(x<sub>2</sub> - x<sub>1</sub>)<super>2</super> + (y<sub>2</sub> - y<sub>1</sub>)<super>2</super>] = √[(4-1)<super>2</super> + (6-2)<super>2</super>] = √[9 + 16].",
      "= √25 = 5.   Answer: length = 5."],
     [("L1", "Find the length of the segment from (0, 0) to (6, 8).",
       "d = √[6<super>2</super> + 8<super>2</super>] = √[36 + 64] = √100 = 10."),
      ("L1", "Find the length of the segment from (1, 1) to (4, 5).",
       "d = √[3<super>2</super> + 4<super>2</super>] = √[9 + 16] = √25 = 5."),
      ("L2", "Find the length of the segment from (-2, 3) to (3, 15).",
       "d = √[5<super>2</super> + 12<super>2</super>] = √[25 + 144] = √169 = 13."),
      ("L3", "A triangle has vertices A(0, 0), B(6, 0) and C(6, 8). Find its perimeter.",
       "AB = 6, BC = 8, CA = √[6<super>2</super> + 8<super>2</super>] = 10; perimeter = 6 + 8 + 10 = 24.")]),
    ("Midpoint of a Segment",
     ["Find the midpoint of A(2, 4) and B(8, 10).",
      "M = ((x<sub>1</sub> + x<sub>2</sub>)/2, (y<sub>1</sub> + y<sub>2</sub>)/2) = ((2+8)/2, (4+10)/2).",
      "= (5, 7).   Answer: midpoint (5, 7)."],
     [("L1", "Find the midpoint of (0, 0) and (6, 8).", "M = (3, 4)."),
      ("L1", "Find the midpoint of (1, 3) and (7, 9).", "M = ((1+7)/2, (3+9)/2) = (4, 6)."),
      ("L2", "Find the midpoint of (-4, 2) and (6, -8).", "M = ((-4+6)/2, (2-8)/2) = (1, -3)."),
      ("L3", "M(5, 4) is the midpoint of A(2, 1) and B. Find the coordinates of B.",
       "B = (2·5 - 2, 2·4 - 1) = (8, 7).")]),
]

WARMUP = [
    ("State the slope of the line y = 4x - 1.", "4"),
    ("State the y-intercept of the line y = 2x + 9.", "(0, 9)"),
    ("Find the slope of the line through (0, 1) and (3, 7).", "2"),
]


def build():
    d = CMFlow(OUT, topic_title=TOPIC, subtitle=SUBTITLE, info_line=INFO, name_date=True)
    d.start()
    d.learning_goal("Find slope, graph and compare lines, and compute segment length and midpoint on the Cartesian plane.")
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
