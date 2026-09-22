#!/usr/bin/env python3
"""Concept Mastery — Grade 9 (MTH1W) Linear Relations — TEST + MARKING SCHEME.

30 questions, 60 minutes, sections K/U -> Application -> Thinking -> Communication;
last four questions very hard. Curriculum: MTH1W. Marks defined once, drive paper +
blueprint + scheme. Run: python3 test_linear-relations.py
"""
import os, sys
ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "_assets"))
sys.path.insert(0, ASSETS)
from cm_pdf import (CMFlow, ST_BODY, CM_BLUE, CM_DARK_GREY, CONTENT_X, __version__)

DIR = os.path.dirname(__file__)
OUT_T = os.path.join(DIR, "test_linear-relations.pdf")
OUT_M = os.path.join(DIR, "test_linear-relations_marking_scheme.pdf")
TOPIC = "Linear Relations"
DURATION = "60 minutes"

# qid, section, subtopic, level, category, marks, stem, answer_mode, solution lines
ITEMS = [
    # ── Section A — Knowledge & Understanding (L1), Q1–15 ──
    ("A1","A","First Differences","L1","K/U",1,"Find the first differences for the y-values 1, 5, 9, 13.","short",["4, 4, 4.  (A1)"]),
    ("A2","A","Variation","L1","K/U",1,"Is y = 8x direct or partial variation?","short",["Direct.  (A1)"]),
    ("A3","A","Variation","L1","K/U",1,"Is y = 2x - 5 direct or partial variation?","short",["Partial.  (A1)"]),
    ("A4","A","Slope","L1","K/U",1,"Find the slope of the line through (0, 0) and (3, 12).","short",["12/3 = 4.  (A1)"]),
    ("A5","A","Intercepts","L1","K/U",1,"State the y-intercept of y = 6x + 9.","short",["9, at (0, 9).  (A1)"]),
    ("A6","A","Slope","L1","K/U",1,"State the slope of the line y = -3x + 2.","short",["-3.  (A1)"]),
    ("A7","A","Intercepts","L1","K/U",1,"Find the x-intercept of y = x - 4.","short",["0 = x - 4 → x = 4, at (4, 0).  (A1)"]),
    ("A8","A","Standard Form","L1","K/U",1,"Write y = 5x + 2 in the standard form Ax + By + C = 0.","short",["5x - y + 2 = 0.  (A1)"]),
    ("A9","A","Correlation","L1","K/U",1,"A scatter plot rises steadily to the right. Is the correlation positive or negative?","short",["Positive.  (A1)"]),
    ("A10","A","First Differences","L1","K/U",2,"Find the first differences of 2, 8, 14, 20 and state whether the relation is linear.","short",["6, 6, 6; constant, so linear.  (M1, A1)"]),
    ("A11","A","Slope","L1","K/U",2,"Find the slope of the line through (1, 2) and (4, 14).","short",["(14-2)/(4-1) = 12/3 = 4.  (M1, A1)"]),
    ("A12","A","Intercepts","L1","K/U",2,"Find the x-intercept and y-intercept of y = 2x - 8.","short",["y-int (0, -8); x-int: 0 = 2x - 8 → (4, 0).  (M1, A1)"]),
    ("A13","A","Equation of a Line","L1","K/U",2,"Write the equation of the line with slope 3 and y-intercept -5.","short",["y = 3x - 5.  (M1, A1)"]),
    ("A14","A","Variation","L1","K/U",2,"A partial variation has initial value 10 and rate of change 4. Write its equation.","short",["y = 4x + 10.  (M1, A1)"]),
    ("A15","A","Standard Form","L1","K/U",2,"Write y = (3/4)x + 2 in standard form with integer coefficients.","short",["Multiply by 4: 4y = 3x + 8, so 3x - 4y + 8 = 0.  (M1, A1)"]),
    # ── Section B — Application (L2), Q16–24 ──
    ("B16","B","Slope","L2","Application",2,"Find the slope of the line through (-2, 7) and (2, -1).","work",
     ["slope = (-1 - 7)/(2 - (-2)) = -8/4 = -2.  (M1, A1)"]),
    ("B17","B","Intercepts","L2","Application",2,"Find the x-intercept and y-intercept of 2x + 5y = 20.","work",
     ["x-int: y = 0 → 2x = 20 → (10, 0).  (M1)", "y-int: x = 0 → 5y = 20 → (0, 4).  (A1)"]),
    ("B18","B","Equation of a Line","L2","Application",2,"Find the equation of the line with slope 5 that passes through (2, 7).","work",
     ["7 = 5(2) + b → b = -3.  (M1)", "y = 5x - 3.  (A1)"]),
    ("B19","B","First Differences","L2","Application",2,"Find the first differences of 4, 9, 16, 25 and state whether the relation is linear.","work",
     ["Differences 5, 7, 9 are not constant.  (M1)", "So the relation is non-linear.  (A1)"]),
    ("B20","B","Standard Form","L2","Application",2,"Write y = (3/4)x - 2 in standard form with integer coefficients.","work",
     ["Multiply by 4: 4y = 3x - 8.  (M1)", "3x - 4y - 8 = 0.  (A1)"]),
    ("B21","B","Variation","L2","Application",2,"A direct variation passes through (6, 24). Find k and write the equation.","work",
     ["k = 24/6 = 4.  (M1)", "y = 4x.  (A1)"]),
    ("B22","B","Line Through Two Points","L2","Application",3,"Find the equation of the line through (1, 4) and (5, 16).","work",
     ["slope = (16-4)/(5-1) = 12/4 = 3.  (M1)", "4 = 3(1) + b → b = 1.  (M1)", "y = 3x + 1.  (A1)"]),
    ("B23","B","Equation from Intercepts","L2","Application",3,"A line has x-intercept 3 and y-intercept -6. Find its slope and its equation.","work",
     ["Through (3, 0) and (0, -6): slope = (-6-0)/(0-3) = 2.  (M1, M1)", "y = 2x - 6.  (A1)"]),
    ("B24","B","Linear Model","L2","Application",3,"A pool is filled at 12 L/min starting from 30 L: V = 12t + 30. Find V at t = 10 min and state the initial value.","work",
     ["V = 12(10) + 30 = 120 + 30 = 150 L.  (M1, A1)", "Initial value is 30 L.  (A1)"]),
    # ── Section C — Thinking (L3), Q25–29 (last three very hard) ──
    ("C25","C","Unknown Coordinate","L3","Thinking",4,
     "The line through (2, 9) and (k, 21) has slope 4. Find k.","work",
     ["(21 - 9)/(k - 2) = 4.  (M1)", "12 = 4(k - 2) → k - 2 = 3.  (M1)", "k = 5.  (A1, A1)"]),
    ("C26","C","Missing Table Value","L3","Thinking",4,
     "A linear table gives y = -5, ?, 7, 13 for x = 0, 1, 2, 3. Find the missing value and the equation of the relation.","work",
     ["Linear → equal first differences; from -5 to 7 over two steps is +12, so +6 each.  (M1)",
      "Missing value: -5 + 6 = 1.  (A1)", "y-intercept -5, slope 6 → y = 6x - 5.  (M1, A1)"]),
    ("C27","C","Linear Model","L3","Thinking",5,
     "A phone plan charges a $30 monthly fee plus $0.20 per minute. Write the cost C in terms of minutes m, find the cost for 150 minutes, and find how many minutes give a $50 bill. (Very hard.)","work",
     ["C = 0.20m + 30.  (M1)", "At m = 150: C = 0.20(150) + 30 = 30 + 30 = $60.  (M1, A1)",
      "For $50: 0.20m + 30 = 50 → 0.20m = 20 → m = 100 minutes.  (M1, A1)"]),
    ("C28","C","Slope, Equation & Intercept","L3","Thinking",5,
     "A line passes through (-3, -1) and (3, 11). Find its slope, its equation, and its x-intercept. (Very hard.)","work",
     ["slope = (11 - (-1))/(3 - (-3)) = 12/6 = 2.  (M1)", "-1 = 2(-3) + b → b = 5, so y = 2x + 5.  (M1, A1)",
      "x-int: 0 = 2x + 5 → x = -5/2, at (-5/2, 0).  (M1, A1)"]),
    ("C29","C","Point of Intersection","L3","Thinking",6,
     "Line A is y = 2x - 1. Line B passes through (1, 7) and (4, 4). Find the equation of Line B, then find the point where the two lines intersect. (Very hard.)","work",
     ["Line B slope = (4 - 7)/(4 - 1) = -3/3 = -1.  (M1)", "7 = -1(1) + b → b = 8, so y = -x + 8.  (M1, A1)",
      "Intersect: 2x - 1 = -x + 8 → 3x = 9 → x = 3.  (M1)", "y = 2(3) - 1 = 5, so (3, 5).  (A1, A1)"]),
    # ── Section D — Communication (L3), Q30 (very hard justify) ──
    ("D30","D","Variation vs Linearity","L3","Communication",4,
     "A student claims \"every straight-line relation is a direct variation.\" Using an example, explain why this is false, and state the condition for a linear relation to be a direct variation. (Very hard.)","work",
     ["Direct variation must pass through the origin, i.e. have y-intercept 0.  (C1)",
      "Counter-example: y = 2x + 3 is a straight line but its y-intercept is 3 ≠ 0, so it is partial, not direct.  (A1, C1)",
      "A linear relation is a direct variation only when its y-intercept is 0 (form y = kx).  (C1)"]),
]

TOTAL = sum(it[5] for it in ITEMS)
SECTIONS = {"A": "Section A — Knowledge & Understanding", "B": "Section B — Application",
            "C": "Section C — Thinking", "D": "Section D — Communication"}

def work_for(marks, category):
    if category == "K/U":
        return None
    return {2: 52, 3: 84, 4: 118, 5: 150, 6: 182}.get(marks, 40 * marks)


def build_test():
    d = CMFlow(OUT_T, topic_title=TOPIC, subtitle="Module 5 Test",
               grade_badge="Grade 9 · MTH1W",
               meta_right=[f"Time: {DURATION}", f"Total: {TOTAL} marks"], name_date=True)
    d.start()
    d.body("Instructions: Show all work for full marks. Marks for each question are shown in "
           "brackets. Calculators are permitted unless your teacher states otherwise.", ST_BODY, gap=12)
    last = None; qnum = 0
    for (qid, sec, sub, lvl, cat, marks, stem, mode, sol) in ITEMS:
        if sec != last:
            d.heading(SECTIONS[sec], color=CM_BLUE); last = sec
        qnum += 1
        d.question(qnum, f"{stem}  <font color='#2D7DD2'><b>[{marks}]</b></font>",
                   answer=mode, work_pts=work_for(marks, cat))
    d.space(6); d.body("<b>— END OF EXAM —</b>", ST_BODY, gap=4)
    return d.build()


def _row(d, cols, xs, bold=False):
    d.ensure(15)
    d.c.setFont(*(("DejaVuSans-Bold", 9) if bold else ("DejaVuSans", 9)))
    d.c.setFillColor(CM_BLUE if bold else CM_DARK_GREY)
    for text, x in zip(cols, xs):
        d.c.drawString(x, d.y - 10, str(text))
    d.y -= 16


def build_scheme():
    d = CMFlow(OUT_M, topic_title=TOPIC, subtitle="Marking Scheme & Blueprint",
               info_line="MTH1W · Module 5 Test — Teacher Copy")
    d.start()
    d.heading("Blueprint", color=CM_BLUE)
    d.body(f"Curriculum: MTH1W (Grade 9 de-streamed math). Total: {TOTAL} marks · {DURATION} · "
           "30 questions. Categories: K/U, Application (App), Thinking (Think), Communication (Comm).",
           ST_BODY, gap=8)
    xs = [CONTENT_X, CONTENT_X+55, CONTENT_X+250, CONTENT_X+300, CONTENT_X+360, CONTENT_X+425]
    _row(d, ["Q", "Sub-topic", "Level", "Marks", "Category", "Section"], xs, bold=True)
    for (qid, sec, sub, lvl, cat, marks, *_r) in ITEMS:
        cs = {"K/U":"K/U","Application":"App","Thinking":"Think","Communication":"Comm"}[cat]
        _row(d, [qid, sub[:30], lvl, marks, cs, sec], xs)
    d.space(4)
    tot = {}; lvltot = {}
    for it in ITEMS:
        tot[it[4]] = tot.get(it[4], 0) + it[5]; lvltot[it[3]] = lvltot.get(it[3], 0) + it[5]
    d.body("<b>By category (marks):</b> " + " · ".join(f"{k} {v}" for k, v in tot.items()), ST_BODY, gap=4)
    d.body("<b>By level (marks):</b> " + " · ".join(f"{k} {lvltot.get(k,0)}" for k in ('L1','L2','L3'))
           + f"  →  L1 {lvltot.get('L1',0)*100//TOTAL}% · L2 {lvltot.get('L2',0)*100//TOTAL}%"
           + f" · L3 {lvltot.get('L3',0)*100//TOTAL}%", ST_BODY, gap=12)
    d.heading("Worked Solutions & Mark Allocation", color=CM_BLUE)
    qnum = 0
    for (qid, sec, sub, lvl, cat, marks, stem, mode, sol) in ITEMS:
        qnum += 1
        d.key_entry(qnum, [f"<b>({qid} · {cat} · {marks} marks)</b>"] + sol)
    return d.build()


if __name__ == "__main__":
    t = build_test(); m = build_scheme()
    from collections import Counter
    lc = Counter(it[3] for it in ITEMS); lm = Counter()
    for it in ITEMS: lm[it[3]] += it[5]
    print(f"engine {__version__}  built {t} and {m}")
    print(f"questions={len(ITEMS)}  total_marks={TOTAL}  by-count {dict(lc)}  by-marks {dict(lm)}")
