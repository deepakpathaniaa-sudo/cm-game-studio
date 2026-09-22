#!/usr/bin/env python3
"""Concept Mastery — Grade 9 (MTH1W) Solving Equations & Inequalities — TEST + MARKING SCHEME.

30 questions, 60 minutes, sections K/U -> Application -> Thinking -> Communication;
last four questions very hard. Curriculum: MTH1W. Marks defined once, drive paper +
blueprint + scheme. Run: python3 test_solving-equations-inequalities.py
"""
import os, sys
ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "_assets"))
sys.path.insert(0, ASSETS)
from cm_pdf import (CMFlow, ST_BODY, CM_BLUE, CM_DARK_GREY, CONTENT_X, __version__)

DIR = os.path.dirname(__file__)
OUT_T = os.path.join(DIR, "test_solving-equations-inequalities.pdf")
OUT_M = os.path.join(DIR, "test_solving-equations-inequalities_marking_scheme.pdf")
TOPIC = "Solving Equations & Inequalities"
DURATION = "60 minutes"

# qid, section, subtopic, level, category, marks, stem, answer_mode, solution lines
ITEMS = [
    # ── Section A — Knowledge & Understanding (L1), Q1–15 ──
    ("A1","A","One-Step","L1","K/U",1,"Solve: x + 6 = 13.","short",["x = 7.  (A1)"]),
    ("A2","A","One-Step","L1","K/U",1,"Solve: x - 8 = 5.","short",["x = 13.  (A1)"]),
    ("A3","A","One-Step","L1","K/U",1,"Solve: 4x = 32.","short",["x = 8.  (A1)"]),
    ("A4","A","One-Step","L1","K/U",1,"Solve: x/2 = 9.","short",["x = 18.  (A1)"]),
    ("A5","A","Two-Step","L1","K/U",1,"Solve: 2x + 1 = 11.","short",["2x = 10, x = 5.  (A1)"]),
    ("A6","A","Two-Step","L1","K/U",1,"Solve: 5x - 3 = 17.","short",["5x = 20, x = 4.  (A1)"]),
    ("A7","A","Inequalities","L1","K/U",1,"Solve: x + 3 &gt; 7.","short",["x &gt; 4.  (A1)"]),
    ("A8","A","One-Step","L1","K/U",1,"Solve: y - 5 = -2.","short",["y = 3.  (A1)"]),
    ("A9","A","One-Step","L1","K/U",1,"Solve: 6x = 42.","short",["x = 7.  (A1)"]),
    ("A10","A","Two-Step","L1","K/U",2,"Solve: 4x + 3 = 27.","short",["4x = 24, x = 6.  (M1, A1)"]),
    ("A11","A","Two-Step","L1","K/U",2,"Solve: 5x - 7 = 18.","short",["5x = 25, x = 5.  (M1, A1)"]),
    ("A12","A","Fractions","L1","K/U",2,"Solve: x/4 + 2 = 5.","short",["x/4 = 3, x = 12.  (M1, A1)"]),
    ("A13","A","Distribution","L1","K/U",2,"Solve: 2(x + 5) = 16.","short",["2x + 10 = 16, 2x = 6, x = 3.  (M1, A1)"]),
    ("A14","A","Both Sides","L1","K/U",2,"Solve: 7x + 2 = 3x + 14.","short",["4x = 12, x = 3.  (M1, A1)"]),
    ("A15","A","Inequalities","L1","K/U",2,"Solve and describe the graph: 2x ≤ 10.","short",
     ["x ≤ 5; closed circle at 5, arrow left.  (M1, A1)"]),
    # ── Section B — Application (L2), Q16–24 ──
    ("B16","B","Both Sides","L2","Application",2,"Solve: 6x - 5 = 2x + 15.","work",
     ["6x - 2x = 15 + 5, 4x = 20, x = 5.  (M1, A1)"]),
    ("B17","B","Fractions","L2","Application",2,"Solve: 2x/3 + 4 = 10.","work",
     ["2x/3 = 6, 2x = 18, x = 9.  (M1, A1)"]),
    ("B18","B","Distribution","L2","Application",2,"Solve: 3(x - 4) = 2x + 1.","work",
     ["3x - 12 = 2x + 1, x = 13.  (M1, A1)"]),
    ("B19","B","Rearranging","L2","Application",2,"Solve V = lwh for h.","work",
     ["Divide both sides by lw: h = V/(lw).  (M1, A1)"]),
    ("B20","B","Two-Step","L2","Application",2,"Solve: 5 - 3x = -7.","work",
     ["-3x = -12, x = 4.  (M1, A1)"]),
    ("B21","B","Inequalities","L2","Application",2,"Solve and describe the graph: 3x - 2 &gt; 7.","work",
     ["3x &gt; 9, x &gt; 3; open circle at 3, arrow right.  (M1, A1)"]),
    ("B22","B","Distribution","L2","Application",3,"Solve: 4(x + 2) = 2(x + 9).","work",
     ["4x + 8 = 2x + 18.  (M1)", "2x = 10, x = 5.  (M1, A1)"]),
    ("B23","B","Rearranging","L2","Application",3,"Solve A = (1/2)bh for b.","work",
     ["Multiply by 2: 2A = bh.  (M1)", "Divide by h: b = 2A/h.  (M1, A1)"]),
    ("B24","B","Fractions","L2","Application",3,"Solve: x/2 + x/3 = 5.","work",
     ["Multiply every term by 6: 3x + 2x = 30.  (M1)", "5x = 30, x = 6.  (M1, A1)"]),
    # ── Section C — Thinking (L3), Q25–29 (last three very hard) ──
    ("C25","C","Consecutive Integers","L3","Thinking",4,
     "The sum of three consecutive integers is 51. Find the integers.","work",
     ["Let them be n, n+1, n+2: n + (n+1) + (n+2) = 51.  (M1)",
      "3n + 3 = 51, 3n = 48.  (M1)", "n = 16, so the integers are 16, 17, 18.  (A1, A1)"]),
    ("C26","C","Inequalities (flip)","L3","Thinking",4,
     "Solve and describe the graph: -4x + 3 ≥ 19.","work",
     ["-4x ≥ 16.  (M1)", "Divide by -4 and reverse: x ≤ -4.  (M1, A1)",
      "Graph: closed circle at -4, arrow left.  (A1)"]),
    ("C27","C","Formula & Evaluate","L3","Thinking",5,
     "The formula F = (9/5)C + 32 converts Celsius to Fahrenheit. Solve the formula for C, then find C when F = 212. (Very hard.)","work",
     ["F - 32 = (9/5)C.  (M1)", "C = (5/9)(F - 32).  (M1, A1)",
      "At F = 212: C = (5/9)(180) = 100.  (M1, A1)"]),
    ("C28","C","Fractions","L3","Thinking",5,
     "Solve: (x + 2)/3 - (x - 1)/4 = 2. (Very hard.)","work",
     ["Multiply every term by 12: 4(x + 2) - 3(x - 1) = 24.  (M1)",
      "4x + 8 - 3x + 3 = 24, x + 11 = 24.  (M1, M1)", "x = 13.  (A1, A1)"]),
    ("C29","C","Word Problem","L3","Thinking",6,
     "A rectangle's length is 3 cm more than twice its width. Its perimeter is 48 cm. Find the width and the length. (Very hard.)","work",
     ["Let width = w, length = 2w + 3.  (M1)",
      "P = 2(2w + 3) + 2w = 6w + 6 = 48.  (M1, M1)",
      "6w = 42, w = 7.  (M1, A1)", "Length = 2(7) + 3 = 17 cm.  (A1)"]),
    # ── Section D — Communication (L3), Q30 (very hard justify) ──
    ("D30","D","Reasoning on Inequalities","L3","Communication",4,
     "Explain why solving -2x &gt; 6 requires reversing the inequality sign. Give the solution and describe its graph. (Very hard.)","work",
     ["Dividing (or multiplying) both sides by a negative number reverses the direction of the inequality.  (C1)",
      "Divide by -2 and reverse: x &lt; -3.  (A1, C1)",
      "Graph: open circle at -3, arrow left.  (A1)"]),
]

TOTAL = sum(it[5] for it in ITEMS)
SECTIONS = {"A": "Section A — Knowledge & Understanding", "B": "Section B — Application",
            "C": "Section C — Thinking", "D": "Section D — Communication"}

def work_for(marks, category):
    if category == "K/U":
        return None
    return {2: 52, 3: 84, 4: 118, 5: 150, 6: 182}.get(marks, 40 * marks)


def build_test():
    d = CMFlow(OUT_T, topic_title=TOPIC, subtitle="Module 3 Test",
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
               info_line="MTH1W · Module 3 Test — Teacher Copy")
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
