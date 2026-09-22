#!/usr/bin/env python3
"""Concept Mastery — Grade 9 (MTH1W) Analytic Geometry — TEST + MARKING SCHEME.

30 questions, 60 minutes, sections K/U -> Application -> Thinking -> Communication;
last four questions very hard. Curriculum: MTH1W. Marks defined once, drive paper +
blueprint + scheme. Run: python3 test_analytic-geometry.py
"""
import os, sys
ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "_assets"))
sys.path.insert(0, ASSETS)
from cm_pdf import (CMFlow, ST_BODY, CM_BLUE, CM_DARK_GREY, CONTENT_X, __version__)

DIR = os.path.dirname(__file__)
OUT_T = os.path.join(DIR, "test_analytic-geometry.pdf")
OUT_M = os.path.join(DIR, "test_analytic-geometry_marking_scheme.pdf")
TOPIC = "Analytic Geometry"
DURATION = "60 minutes"

# qid, section, subtopic, level, category, marks, stem, answer_mode, solution lines
ITEMS = [
    # ── Section A — Knowledge & Understanding (L1), Q1–15 ──
    ("A1","A","Slope","L1","K/U",1,"State the slope of the line y = 7x + 2.","short",["m = 7.  (A1)"]),
    ("A2","A","Slope","L1","K/U",1,"State the slope of the line y = -x + 4.","short",["m = -1.  (A1)"]),
    ("A3","A","Graphing","L1","K/U",1,"State the y-intercept of the line y = 5x - 8.","short",["(0, -8).  (A1)"]),
    ("A4","A","Parallel","L1","K/U",1,"State the slope of a line parallel to y = 6x + 1.","short",["m = 6.  (A1)"]),
    ("A5","A","Perpendicular","L1","K/U",1,"State the slope of a line perpendicular to a line with slope 2.","short",["-1/2.  (A1)"]),
    ("A6","A","Midpoint","L1","K/U",1,"Find the midpoint of (0, 0) and (4, 10).","short",["(2, 5).  (A1)"]),
    ("A7","A","Length","L1","K/U",1,"Find the length of the segment from (0, 0) to (0, 7).","short",["7.  (A1)"]),
    ("A8","A","Slope","L1","K/U",1,"Find the slope of the line through (0, 0) and (3, 9).","short",["9/3 = 3.  (A1)"]),
    ("A9","A","Graphing","L1","K/U",1,"Does the point (0, 3) lie on the line y = 2x + 3?","short",["Yes; it is the y-intercept.  (A1)"]),
    ("A10","A","Slope","L1","K/U",2,"Find the slope of the line through (1, 2) and (5, 14).","short",["(14 - 2)/(5 - 1) = 12/4 = 3.  (M1, A1)"]),
    ("A11","A","Length","L1","K/U",2,"Find the length of the segment from (2, 1) to (5, 5).","short",["√[3<super>2</super> + 4<super>2</super>] = √25 = 5.  (M1, A1)"]),
    ("A12","A","Midpoint","L1","K/U",2,"Find the midpoint of (-2, 4) and (6, 10).","short",["((-2+6)/2, (4+10)/2) = (2, 7).  (M1, A1)"]),
    ("A13","A","Perpendicular","L1","K/U",2,"State the slope of a line perpendicular to y = -3x + 2.","short",["Given slope -3; perpendicular 1/3.  (M1, A1)"]),
    ("A14","A","Parallel","L1","K/U",2,"Write the equation of the line parallel to y = 2x - 1 through (0, 5).","short",["y = 2x + 5.  (M1, A1)"]),
    ("A15","A","Graphing","L1","K/U",2,"Find the x-intercept of the line y = -x + 4.","short",["0 = -x + 4 → x = 4 → (4, 0).  (M1, A1)"]),
    # ── Section B — Application (L2), Q16–24 ──
    ("B16","B","Slope","L2","Application",2,"Find the slope of the line through (-2, 5) and (4, -7).","work",
     ["m = (-7 - 5)/(4 - (-2)) = -12/6 = -2.  (M1, A1)"]),
    ("B17","B","Length","L2","Application",2,"Find the length of the segment from (-3, 1) to (2, 13).","work",
     ["√[5<super>2</super> + 12<super>2</super>] = √[25 + 144] = √169 = 13.  (M1, A1)"]),
    ("B18","B","Midpoint","L2","Application",2,"Find the midpoint of (-5, -2) and (7, 8).","work",
     ["((-5+7)/2, (-2+8)/2) = (1, 3).  (M1, A1)"]),
    ("B19","B","Parallel","L2","Application",2,"Determine whether y = 4x + 1 and y = 4x - 9 are parallel.","work",
     ["Both have slope 4; equal slopes, so yes — parallel.  (M1, A1)"]),
    ("B20","B","Perpendicular","L2","Application",2,"State the slope of a line perpendicular to y = (3/4)x + 2.","work",
     ["Negative reciprocal of 3/4 is -4/3.  (M1, A1)"]),
    ("B21","B","Graphing","L2","Application",2,"Find the x-intercept and y-intercept of y = 3x - 12.","work",
     ["y-intercept (0, -12); x-intercept: 0 = 3x - 12 → x = 4 → (4, 0).  (M1, A1)"]),
    ("B22","B","Slope","L2","Application",3,"The line through (2, 3) and (8, k) has slope 2. Find the value of k.","work",
     ["(k - 3)/(8 - 2) = 2, so k - 3 = 12.  (M1, M1)", "k = 15.  (A1)"]),
    ("B23","B","Graphing","L2","Application",3,"Rewrite 2x + y = 6 in the form y = mx + b, then state the slope and y-intercept.","work",
     ["y = -2x + 6.  (M1, A1)", "Slope = -2; y-intercept (0, 6).  (M1)"]),
    ("B24","B","Length","L2","Application",3,"A triangle has vertices A(0, 0), B(9, 0), C(9, 12). Find its perimeter.","work",
     ["AB = 9, BC = 12, CA = √[9<super>2</super> + 12<super>2</super>] = √225 = 15.  (M1, M1)", "Perimeter = 9 + 12 + 15 = 36.  (A1)"]),
    # ── Section C — Thinking (L3), Q25–29 (last three very hard) ──
    ("C25","C","Perpendicular","L3","Thinking",4,
     "A line passes through (1, 2) and (4, 8). Find its slope, then the slope of any line perpendicular to it.","work",
     ["Slope = (8 - 2)/(4 - 1) = 6/3 = 2.  (M1, A1)",
      "Perpendicular slope = negative reciprocal of 2 = -1/2.  (M1, A1)"]),
    ("C26","C","Parallel","L3","Thinking",4,
     "A line passes through (0, -3) and (2, 5). Write its equation, then state whether it is parallel to y = 4x + 7.","work",
     ["Slope = (5 - (-3))/(2 - 0) = 8/2 = 4; y-intercept (0, -3), so y = 4x - 3.  (M1, A1)",
      "Same slope as y = 4x + 7, so yes — parallel.  (M1, A1)"]),
    ("C27","C","Midpoint & Length","L3","Thinking",5,
     "The midpoint of segment AB is M(4, 3). If A = (1, -1), find the coordinates of B, then find the length of AB. (Very hard.)","work",
     ["B = (2·4 - 1, 2·3 - (-1)) = (7, 7).  (M1, A1)",
      "AB = √[(7-1)<super>2</super> + (7-(-1))<super>2</super>] = √[36 + 64] = √100.  (M1)", "= 10.  (A1, A1)"]),
    ("C28","C","Perpendicular & Graphing","L3","Thinking",5,
     "A line is perpendicular to y = (1/2)x + 4 and passes through (0, 5). Write its equation, then find its x-intercept. (Very hard.)","work",
     ["Perpendicular slope = negative reciprocal of 1/2 = -2; y-intercept 5, so y = -2x + 5.  (M1, A1)",
      "x-intercept: 0 = -2x + 5 → x = 5/2.  (M1)", "x-intercept (2.5, 0).  (A1, A1)"]),
    ("C29","C","Length & Right Triangle","L3","Thinking",6,
     "A triangle has vertices P(-2, -1), Q(4, -1), R(4, 7). Find the length of each side and the perimeter, and show the triangle is right-angled. (Very hard.)","work",
     ["PQ = 6 (horizontal), QR = 8 (vertical).  (M1, M1)",
      "PR = √[6<super>2</super> + 8<super>2</super>] = √100 = 10.  (M1)",
      "Perimeter = 6 + 8 + 10 = 24.  (A1, A1)",
      "Since 6<super>2</super> + 8<super>2</super> = 36 + 64 = 100 = 10<super>2</super>, the angle at Q is 90°.  (A1)"]),
    # ── Section D — Communication (L3), Q30 (very hard justify) ──
    ("D30","D","Parallel Lines Reasoning","L3","Communication",4,
     "A student claims that y = 2x + 1 and y = 2x + 6 must eventually cross because \"all straight lines meet somewhere.\" Using slope, explain why the student is incorrect. (Very hard.)","work",
     ["Both lines have slope 2, so they are equally steep (parallel).  (A1)",
      "Their y-intercepts differ (1 and 6), so they are not the same line.  (A1)",
      "Distinct parallel lines never intersect, so the claim is false.  (C1, C1)"]),
]

TOTAL = sum(it[5] for it in ITEMS)
SECTIONS = {"A": "Section A — Knowledge & Understanding", "B": "Section B — Application",
            "C": "Section C — Thinking", "D": "Section D — Communication"}

def work_for(marks, category):
    if category == "K/U":
        return None
    return {2: 52, 3: 84, 4: 118, 5: 150, 6: 182}.get(marks, 40 * marks)


def build_test():
    d = CMFlow(OUT_T, topic_title=TOPIC, subtitle="Module 6 Test",
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
               info_line="MTH1W · Module 6 Test — Teacher Copy")
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
