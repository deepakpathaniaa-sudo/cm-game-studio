#!/usr/bin/env python3
"""Concept Mastery — Grade 9 (MTH1W) Algebra & Polynomials — TEST + MARKING SCHEME.

30 questions, 60 minutes, sections K/U -> Application -> Thinking -> Communication;
last four questions very hard. Curriculum: MTH1W. Marks defined once, drive paper +
blueprint + scheme. Run: python3 test_algebra-polynomials.py
"""
import os, sys
ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "_assets"))
sys.path.insert(0, ASSETS)
from cm_pdf import (CMFlow, ST_BODY, CM_BLUE, CM_DARK_GREY, CONTENT_X, __version__)

DIR = os.path.dirname(__file__)
OUT_T = os.path.join(DIR, "test_algebra-polynomials.pdf")
OUT_M = os.path.join(DIR, "test_algebra-polynomials_marking_scheme.pdf")
TOPIC = "Algebra & Polynomials"
DURATION = "60 minutes"

# qid, section, subtopic, level, category, marks, stem, answer_mode, solution lines
ITEMS = [
    # ── Section A — Knowledge & Understanding (L1), Q1–15 ──
    ("A1","A","Like Terms","L1","K/U",1,"Simplify: 9x - 4x.","short",["= 5x.  (A1)"]),
    ("A2","A","Like Terms","L1","K/U",1,"Simplify: 3a + 7 - a.","short",["= 2a + 7.  (A1)"]),
    ("A3","A","Substitution","L1","K/U",1,"Evaluate 4x + 1 when x = 2.","short",["4(2)+1 = 9.  (A1)"]),
    ("A4","A","Add Polynomials","L1","K/U",1,"Simplify: (2x + 5) + (3x - 2).","short",["= 5x + 3.  (A1)"]),
    ("A5","A","Multiply by Constant","L1","K/U",1,"Expand: 5(x - 3).","short",["= 5x - 15.  (A1)"]),
    ("A6","A","Divide by Constant","L1","K/U",1,"Simplify: (8x + 12) ÷ 4.","short",["= 2x + 3.  (A1)"]),
    ("A7","A","Exponent Laws","L1","K/U",1,"Simplify: x<super>4</super> · x<super>5</super>.","short",["x<super>4+5</super> = x<super>9</super>.  (A1)"]),
    ("A8","A","Like Terms","L1","K/U",1,"State the coefficient of the term -6y<super>2</super>.","short",["-6.  (A1)"]),
    ("A9","A","Polynomials","L1","K/U",1,"How many terms are in 3x<super>2</super> - 2x + 7?","short",["3 terms.  (A1)"]),
    ("A10","A","Like Terms","L1","K/U",2,"Simplify: 4m + 3n - m + 2n.","short",["3m + 5n.  (M1, A1)"]),
    ("A11","A","Substitution","L1","K/U",2,"Evaluate 2a + 3b when a = 3 and b = -1.","short",["6 + (-3) = 3.  (M1, A1)"]),
    ("A12","A","Subtract Polynomials","L1","K/U",2,"Simplify: (5x + 4) - (2x - 3).","short",["5x - 2x + 4 + 3 = 3x + 7.  (M1, A1)"]),
    ("A13","A","Multiply by Monomial","L1","K/U",2,"Expand: 2x(3x + 5).","short",["6x<super>2</super> + 10x.  (M1, A1)"]),
    ("A14","A","Divide by Monomial","L1","K/U",2,"Simplify: (9x<super>2</super> - 6x) ÷ 3x.","short",["3x - 2.  (M1, A1)"]),
    ("A15","A","Exponent Laws","L1","K/U",2,"Simplify: (4x<super>2</super>)(2x<super>3</super>).","short",["8x<super>5</super>.  (M1 coeff, A1)"]),
    # ── Section B — Application (L2), Q16–24 ──
    ("B16","B","Like Terms","L2","Application",2,"Simplify: 6x<super>2</super> - 2x + 3x<super>2</super> - 5x.","work",
     ["(6x<super>2</super>+3x<super>2</super>) + (-2x-5x) = 9x<super>2</super> - 7x.  (M1, A1)"]),
    ("B17","B","Add Polynomials","L2","Application",2,"Simplify: (3a<super>2</super> - a + 2) + (a<super>2</super> + 4a - 6).","work",
     ["4a<super>2</super> + 3a - 4.  (M1, A1)"]),
    ("B18","B","Multiply by Constant","L2","Application",2,"Expand: -3(2x - 4).","work",["-6x + 12.  (M1, A1)"]),
    ("B19","B","Divide by Constant","L2","Application",2,"Simplify: (16x<super>2</super> + 8x) ÷ 8.","work",["2x<super>2</super> + x.  (M1, A1)"]),
    ("B20","B","Exponent Laws","L2","Application",2,"Simplify: (20x<super>6</super>) ÷ (5x<super>2</super>).","work",
     ["Coefficients 20÷5=4; subtract exponents: 4x<super>4</super>.  (M1, A1)"]),
    ("B21","B","Substitution","L2","Application",2,"Evaluate x<super>2</super> - 2x + 1 when x = 4.","work",
     ["16 - 8 + 1 = 9.  (M1, A1)"]),
    ("B22","B","Multiply/Expand","L2","Application",3,"Expand and simplify: 4(x + 2) + 3(2x - 1).","work",
     ["4x + 8 + 6x - 3 = 10x + 5.  (M1, M1, A1)"]),
    ("B23","B","Subtract Polynomials","L2","Application",3,"Simplify: (7x<super>2</super> + 3x - 2) - (2x<super>2</super> - 5x + 4).","work",
     ["7x<super>2</super>-2x<super>2</super>=5x<super>2</super>; 3x+5x=8x; -2-4=-6.", "= 5x<super>2</super> + 8x - 6.  (M1, M1, A1)"]),
    ("B24","B","Divide by Monomial","L2","Application",3,"Simplify: (12x<super>3</super> - 8x<super>2</super> + 4x) ÷ 4x.","work",
     ["Divide each term by 4x: 3x<super>2</super> - 2x + 1.  (M1, M1, A1)"]),
    # ── Section C — Thinking (L3), Q25–29 (last very hard) ──
    ("C25","C","Perimeter","L3","Thinking",4,
     "A triangle has perimeter (12x + 3). Two sides are (4x - 1) and (5x + 5). Find the third side.","work",
     ["Third = (12x+3) - (4x-1) - (5x+5).  (M1)",
      "= 12x + 3 - 4x + 1 - 5x - 5.  (M1)", "= 3x - 1.  (A1, A1)"]),
    ("C26","C","Expand & Collect","L3","Thinking",4,
     "Expand and simplify: 2x(3x - 4) - 3(x<super>2</super> - 2x).","work",
     ["2x(3x-4) = 6x<super>2</super> - 8x; 3(x<super>2</super>-2x) = 3x<super>2</super> - 6x.  (M1, M1)",
      "6x<super>2</super> - 8x - 3x<super>2</super> + 6x = 3x<super>2</super> - 2x.  (A1, A1)"]),
    ("C27","C","Area & Perimeter","L3","Thinking",5,
     "A rectangle has area (6x<super>2</super> + 9x) and width 3x. Find its length, then its perimeter in terms of x. (Very hard.)","work",
     ["Length = (6x<super>2</super>+9x) ÷ 3x = 2x + 3.  (M1, A1)",
      "Perimeter = 2[(2x+3) + 3x] = 2(5x+3).  (M1)", "= 10x + 6.  (A1, A1)"]),
    ("C28","C","Formula & Evaluate","L3","Thinking",5,
     "A rectangle has length (3x + 1) and width (x + 4). Write its perimeter P in simplified form, then evaluate P when x = 5. (Very hard.)","work",
     ["P = 2(3x+1) + 2(x+4) = 6x+2+2x+8.  (M1, M1)", "P = 8x + 10.  (A1)",
      "At x = 5: 8(5) + 10 = 50.  (M1, A1)"]),
    ("C29","C","Multi-technique","L3","Thinking",6,
     "Simplify fully: (10x<super>3</super> - 15x<super>2</super>) ÷ 5x + 2x(4 - x) - 3. (Very hard.)","work",
     ["(10x<super>3</super>-15x<super>2</super>)÷5x = 2x<super>2</super> - 3x.  (M1)",
      "2x(4 - x) = 8x - 2x<super>2</super>.  (M1)",
      "2x<super>2</super> - 3x + 8x - 2x<super>2</super> - 3.  (M1, M1)", "= 5x - 3.  (A1, A1)"]),
    # ── Section D — Communication (L3), Q30 (very hard justify) ──
    ("D30","D","Like Terms vs Product","L3","Communication",4,
     "Aisha says 3x + 3x = 3x<super>2</super>. Is she correct? Explain the difference between adding like terms and multiplying them, using this example. (Very hard.)","work",
     ["Adding: 3x + 3x = 6x (add coefficients, keep the variable).  (A1)",
      "Multiplying: 3x × 3x = 9x<super>2</super> (multiply coefficients, add exponents).  (A1)",
      "So Aisha is not correct; 3x + 3x = 6x.  (C1, C1)"]),
]

TOTAL = sum(it[5] for it in ITEMS)
SECTIONS = {"A": "Section A — Knowledge & Understanding", "B": "Section B — Application",
            "C": "Section C — Thinking", "D": "Section D — Communication"}

def work_for(marks, category):
    if category == "K/U":
        return None
    return {2: 52, 3: 84, 4: 118, 5: 150, 6: 182}.get(marks, 40 * marks)


def build_test():
    d = CMFlow(OUT_T, topic_title=TOPIC, subtitle="Module 2 Test",
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
               info_line="MTH1W · Module 2 Test — Teacher Copy")
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
