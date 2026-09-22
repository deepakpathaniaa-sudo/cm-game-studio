#!/usr/bin/env python3
"""Concept Mastery — Grade 9 (MTH1W) Solving Equations & Inequalities — CLASS COPY.

Template matches approved Module 2: warm-up, then per sub-topic one worked
Example + 3-4 questions of rising complexity, generous open work space (no
ruled lines). Curriculum tag: MTH1W. Answers on final page.
Run: python3 class_solving-equations-inequalities.py
"""
import os, sys
ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "_assets"))
sys.path.insert(0, ASSETS)
from cm_pdf import CMFlow, ST_BODY, CM_BLUE, CM_MED_BLUE, __version__

OUT = os.path.join(os.path.dirname(__file__), "class_solving-equations-inequalities.pdf")
TOPIC = "Solving Equations & Inequalities"
SUBTITLE = "One- & Two-Step · Multi-Step · Fractions & Distribution · Rearranging Formulas · Inequalities"
INFO = "MTH1W · Class — Guided Practice"

SUBTOPICS = [
    ("One-Step Equations",
     ["Solve x - 7 = 3.",
      "Add 7 to both sides: x - 7 + 7 = 3 + 7.",
      "x = 10.   Answer: x = 10."],
     [("L1", "Solve: x + 9 = 15.", "x = 6"),
      ("L1", "Solve: 4x = 28.", "x = 7"),
      ("L2", "Solve: x/5 = 6.", "x = 30"),
      ("L3", "Solve -3x = 21, then check your answer by substitution.",
       "x = -7; check: -3(-7) = 21.")]),
    ("Two-Step Equations",
     ["Solve 2x + 3 = 11.",
      "Subtract 3: 2x = 8.  Divide by 2: x = 4.",
      "Answer: x = 4."],
     [("L1", "Solve: 3x + 4 = 19.", "3x = 15, so x = 5"),
      ("L2", "Solve: x/3 - 5 = 1.", "x/3 = 6, so x = 18"),
      ("L2", "Solve: 7 - 2x = 15.", "-2x = 8, so x = -4"),
      ("L3", "Solve 4x + 9 = 1, then check by substitution.",
       "4x = -8, x = -2; check: 4(-2)+9 = 1.")]),
    ("Multi-Step Equations (variables on both sides)",
     ["Solve 5x - 2 = 3x + 8.",
      "Subtract 3x: 2x - 2 = 8.  Add 2: 2x = 10.",
      "Divide by 2: x = 5."],
     [("L1", "Solve: 6x = 2x + 12.", "4x = 12, so x = 3"),
      ("L2", "Solve: 8x - 5 = 3x + 15.", "5x = 20, so x = 4"),
      ("L2", "Solve: 10 - x = 2x + 1.", "9 = 3x, so x = 3"),
      ("L3", "Solve 5x + 3 = 2x + 18, then check by substitution.",
       "3x = 15, x = 5; check: 5(5)+3 = 28 = 2(5)+18.")]),
    ("Equations with Fractions and Distribution",
     ["Solve 2(x + 3) = 14.",
      "Distribute: 2x + 6 = 14.  Subtract 6: 2x = 8.",
      "Divide by 2: x = 4."],
     [("L1", "Solve: 3(x - 1) = 12.", "3x = 15, so x = 5"),
      ("L2", "Solve: (x + 2)/4 = 3.", "x + 2 = 12, so x = 10"),
      ("L2", "Solve: 5(2x - 1) = 25.", "10x - 5 = 25, 10x = 30, x = 3"),
      ("L3", "Solve 4(x + 1) = 2(x + 7), then check by substitution.",
       "4x+4 = 2x+14, 2x = 10, x = 5; check: both sides = 24.")]),
    ("Rearranging Formulas (solve for a variable)",
     ["Solve y = mx + b for x.",
      "Subtract b: y - b = mx.  Divide by m.",
      "x = (y - b)/m."],
     [("L1", "Solve C = 2πr for r.", "r = C/(2π)"),
      ("L2", "Solve A = (1/2)bh for h.", "2A = bh, so h = 2A/b"),
      ("L2", "Solve P = 2l + 2w for w.", "2w = P - 2l, so w = (P - 2l)/2"),
      ("L3", "Solve A = (1/2)(a + b)h for b.",
       "2A = (a+b)h, a+b = 2A/h, b = (2A - ah)/h.")]),
    ("Solving and Graphing Linear Inequalities",
     ["Solve and graph x + 4 &lt; 9.",
      "Subtract 4: x &lt; 5.",
      "Graph: open circle at 5, arrow pointing left."],
     [("L1", "Solve and describe the graph: x - 3 &gt; 2.",
       "x &gt; 5; open circle at 5, arrow right."),
      ("L2", "Solve and describe the graph: 2x + 1 ≤ 9.",
       "2x ≤ 8, x ≤ 4; closed circle at 4, arrow left."),
      ("L2", "Solve and describe the graph: 3x ≥ -6.",
       "x ≥ -2; closed circle at -2, arrow right."),
      ("L3", "Solve and describe the graph of -2x &lt; 8. Explain what happens to the inequality sign.",
       "Divide by -2 and flip: x &gt; -4; open circle at -4, arrow right.")]),
]

WARMUP = [
    ("Solve: x + 5 = 12.", "x = 7"),
    ("Solve: 3x = 18.", "x = 6"),
    ("Solve: x - 4 = 10.", "x = 14"),
]


def build():
    d = CMFlow(OUT, topic_title=TOPIC, subtitle=SUBTITLE, info_line=INFO, name_date=True)
    d.start()
    d.learning_goal("Solve one-step, two-step and multi-step equations, rearrange formulas, and solve and graph linear inequalities.")
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
