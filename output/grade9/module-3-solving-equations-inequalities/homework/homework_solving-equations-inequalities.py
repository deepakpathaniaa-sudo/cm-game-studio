#!/usr/bin/env python3
"""Concept Mastery — Grade 9 (MTH1W) Solving Equations & Inequalities — HOMEWORK + KEY.

6 questions per level (L1/L2/L3 = 18), distinct concepts, open working space
under each question (no ruled lines). Curriculum: MTH1W. Full worked key.
Run: python3 homework_solving-equations-inequalities.py
"""
import os, sys
ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "_assets"))
sys.path.insert(0, ASSETS)
from cm_pdf import CMFlow, ST_BODY, CM_BLUE, __version__

DIR = os.path.dirname(__file__)
OUT_Q = os.path.join(DIR, "homework_solving-equations-inequalities.pdf")
OUT_A = os.path.join(DIR, "homework_solving-equations-inequalities_answers.pdf")
TOPIC = "Solving Equations & Inequalities"
SUBTITLE = "One- & Two-Step · Multi-Step · Fractions & Distribution · Rearranging Formulas · Inequalities"

ITEMS = [
    # ── L1 (6) ──
    ("L1", "One-step", "Solve: x + 11 = 20.", ["Subtract 11: x = 20 - 11 = 9."]),
    ("L1", "Two-step", "Solve: 2x - 6 = 10.", ["Add 6: 2x = 16. Divide by 2: x = 8."]),
    ("L1", "Both sides", "Solve: 5x = 3x + 8.", ["Subtract 3x: 2x = 8. Divide by 2: x = 4."]),
    ("L1", "Distribution", "Solve: 4(x - 2) = 12.", ["Distribute: 4x - 8 = 12. Add 8: 4x = 20. x = 5."]),
    ("L1", "Rearrange", "Solve y = x + c for x.", ["Subtract c from both sides: x = y - c."]),
    ("L1", "Inequality", "Solve and describe the graph: x - 2 &gt; 3.",
     ["Add 2: x &gt; 5.", "Graph: open circle at 5, arrow right."]),
    # ── L2 (6) ──
    ("L2", "One-step", "Solve: x/6 = 7.", ["Multiply both sides by 6: x = 42."]),
    ("L2", "Two-step", "Solve: 8 - 3x = 2.", ["Subtract 8: -3x = -6. Divide by -3: x = 2."]),
    ("L2", "Both sides", "Solve: 9x - 4 = 5x + 12.", ["Subtract 5x: 4x - 4 = 12. Add 4: 4x = 16. x = 4."]),
    ("L2", "Fractions", "Solve: (x - 3)/5 = 4.", ["Multiply by 5: x - 3 = 20. Add 3: x = 23."]),
    ("L2", "Rearrange", "Solve P = 2l + 2w for l.", ["Subtract 2w: 2l = P - 2w. Divide by 2: l = (P - 2w)/2."]),
    ("L2", "Inequality", "Solve and describe the graph: 3x + 2 ≤ 14.",
     ["Subtract 2: 3x ≤ 12. Divide by 3: x ≤ 4.", "Graph: closed circle at 4, arrow left."]),
    # ── L3 (6) ──
    ("L3", "Consecutive", "The sum of two consecutive even integers is 46. Find the integers.",
     ["Let the integers be n and n + 2, so n + (n + 2) = 46.",
      "2n + 2 = 46, 2n = 44, n = 22. The integers are 22 and 24."]),
    ("L3", "Both-sides distribute", "Solve: 5(x - 1) = 3(x + 3).",
     ["Distribute: 5x - 5 = 3x + 9. Subtract 3x: 2x - 5 = 9.",
      "Add 5: 2x = 14. Divide by 2: x = 7."]),
    ("L3", "Fractions", "Solve: x/4 + x/2 = 9.",
     ["Multiply every term by 4: x + 2x = 36.", "3x = 36, so x = 12."]),
    ("L3", "Rearrange", "Solve v = u + at for a.",
     ["Subtract u: v - u = at. Divide by t: a = (v - u)/t."]),
    ("L3", "Inequality (flip)", "Solve and describe the graph: -3x + 1 &lt; 10.",
     ["Subtract 1: -3x &lt; 9. Divide by -3 and reverse the sign: x &gt; -3.",
      "Graph: open circle at -3, arrow right."]),
    ("L3", "Formula & evaluate", "The area of a triangle is A = (1/2)bh. Rearrange for h, then find h when A = 24 and b = 6.",
     ["Rearrange: 2A = bh, so h = 2A/b.", "h = 2(24)/6 = 48/6 = 8."]),
]


def build_questions():
    d = CMFlow(OUT_Q, topic_title=TOPIC, subtitle=SUBTITLE,
               info_line="MTH1W · Homework — Independent Practice", name_date=True)
    d.start()
    d.learning_goal("Practise solving equations, rearranging formulas and solving inequalities independently.")
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
