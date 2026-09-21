#!/usr/bin/env python3
"""Concept Mastery — Grade 9 (MTH1W) Number Sense — MODULE TEST + MARKING SCHEME.

Per user revision: 30 questions, 60 minutes, and the last few questions are very
hard. Sections run K/U -> Application -> Thinking -> Communication. Curriculum:
MTH1W. Marks are defined once and drive the paper, blueprint, and scheme, so all
three agree. Builds test_number-sense.pdf (student) and
test_number-sense_marking_scheme.pdf (blueprint + worked solutions, M/A marks).
Run: python3 test_number-sense.py
"""
import os, sys
from fractions import Fraction as F

ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "_assets"))
sys.path.insert(0, ASSETS)
from cm_pdf import (CMFlow, ST_BODY, CM_BLUE, CM_DARK_GREY, CONTENT_X, CONTENT_WIDTH, __version__)

DIR = os.path.dirname(__file__)
OUT_T = os.path.join(DIR, "test_number-sense.pdf")
OUT_M = os.path.join(DIR, "test_number-sense_marking_scheme.pdf")
TOPIC = "Number Sense"
DURATION = "60 minutes"

def fr(x):
    x = F(x); return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)

# qid, section, subtopic, level, category, marks, stem, answer_mode, solution lines
ITEMS = [
    # ── Section A — Knowledge & Understanding (L1), Q1–15 ──
    ("A1","A","Integers","L1","K/U",1,"Evaluate: (-9) + (-7).","short",[f"= {-9-7}.  (A1)"]),
    ("A2","A","Integers","L1","K/U",1,"Evaluate: (-20) - (-8).","short",[f"= -20 + 8 = {-20+8}.  (A1)"]),
    ("A3","A","Order of Operations","L1","K/U",1,"Evaluate: 6 + 4 × 5.","short",[f"= 6 + 20 = {6+4*5}.  (A1)"]),
    ("A4","A","Exponent Rules","L1","K/U",1,"Write as a single power: 3<super>2</super> × 3<super>3</super>.","short",["3<super>2+3</super> = 3<super>5</super>.  (A1)"]),
    ("A5","A","Exponent Rules","L1","K/U",1,"Simplify, m ≠ 0: m<super>8</super> ÷ m<super>5</super>.","short",["m<super>8-5</super> = m<super>3</super>.  (A1)"]),
    ("A6","A","Fractions","L1","K/U",1,"Evaluate in lowest terms: 1/4 + 3/8.","short",[f"2/8 + 3/8 = {fr(F(1,4)+F(3,8))}.  (A1)"]),
    ("A7","A","Fractions","L1","K/U",1,"Evaluate in lowest terms: 2/3 × 9/10.","short",[f"= 18/30 = {fr(F(2,3)*F(9,10))}.  (A1)"]),
    ("A8","A","Decimals/Percent","L1","K/U",1,"Write 0.08 as a percent.","short",["0.08 × 100 = 8%.  (A1)"]),
    ("A9","A","Ratios & Rates","L1","K/U",1,"Simplify the ratio 24 : 36.","short",["÷12: 2 : 3.  (A1)"]),
    ("A10","A","Order of Operations","L1","K/U",2,"Evaluate: 40 - (3 + 2)<super>2</super> ÷ 5.","short",
     [f"(5)<super>2</super>=25; 25÷5=5; 40-5 = {40-(3+2)**2//5}.  (M1, A1)"]),
    ("A11","A","Fractions","L1","K/U",2,"Evaluate in lowest terms: 5/6 - 1/2.","short",
     [f"5/6 - 3/6 = {fr(F(5,6)-F(1,2))}.  (M1 common denom, A1)"]),
    ("A12","A","Applying Percents","L1","K/U",2,"Find 12% of 150.","short",[f"0.12 × 150 = {int(0.12*150)}.  (A2)"]),
    ("A13","A","Square Roots & Irrationals","L1","K/U",2,"Classify each as rational or irrational: √49, √50.","short",
     ["√49 = 7 rational; √50 irrational.  (A1, A1)"]),
    ("A14","A","Decimals/Percent","L1","K/U",2,"Write 5/8 as a decimal and as a percent.","short",
     ["5 ÷ 8 = 0.625 = 62.5%.  (A1, A1)"]),
    ("A15","A","Ratios & Rates","L1","K/U",2,"A car travels 180 km in 3 hours at a steady speed. Find the unit rate (speed).","short",
     [f"180 ÷ 3 = {180//3} km/h.  (M1, A1)"]),
    # ── Section B — Application (L2), Q16–24 ──
    ("B16","B","Fractions","L2","Application",2,"Evaluate in lowest terms: 3/4 ÷ 2/3.","work",
     [f"3/4 × 3/2 = {fr(F(3,4)/F(2,3))}.  (M1 reciprocal, A1)"]),
    ("B17","B","Exponent Rules","L2","Application",2,"Simplify to a single power and evaluate: (2<super>2</super>)<super>3</super> ÷ 2<super>4</super>.","work",
     [f"(2<super>2</super>)<super>3</super>=2<super>6</super>; 2<super>6</super>÷2<super>4</super>=2<super>2</super>={2**2}.  (M1, A1)"]),
    ("B18","B","Applying Percents","L2","Application",2,"A book costs $80 before tax. Find the total with 13% HST.","work",
     [f"80 × 1.13 = ${80*1.13:.2f}.  (M1, A1)"]),
    ("B19","B","Rational Numbers","L2","Application",2,"Order from least to greatest: -0.6, -2/3, -0.55, -1/2.","work",
     ["-2/3 ≈ -0.667, -1/2 = -0.5.", "Order: -2/3, -0.6, -0.55, -1/2.  (M1, A1)"]),
    ("B20","B","Ratios & Rates","L2","Application",2,"5 kg of rice costs $12.50. At the same rate, find the cost of 8 kg.","work",
     [f"Unit rate 12.50 ÷ 5 = $2.50/kg; 8 × 2.50 = ${8*2.5:.2f}.  (M1, A1)"]),
    ("B21","B","Square Roots & Irrationals","L2","Application",2,"Between which two consecutive whole numbers does √60 lie? Justify.","work",
     ["7<super>2</super>=49 < 60 < 64=8<super>2</super>, so between 7 and 8.  (M1, A1)"]),
    ("B22","B","Fractions","L2","Application",3,"Evaluate in lowest terms: 2/3 + 1/4 × 8/5.","work",
     ["Multiply first: 1/4 × 8/5 = 2/5.", f"2/3 + 2/5 = 10/15 + 6/15 = {fr(F(2,3)+F(1,4)*F(8,5))}.  (M1, M1, A1)"]),
    ("B23","B","Applying Percents","L2","Application",3,"A gym's membership rises from 250 to 300 members. Find the percent increase.","work",
     ["Increase = 50.", f"50 ÷ 250 × 100 = {50*100//250}%.  (M1, M1, A1)"]),
    ("B24","B","Ratios & Rates","L2","Application",3,"Share $840 in the ratio 3 : 4 : 5.","work",
     ["Parts = 12; one part = 840 ÷ 12 = $70.", "3×70=$210, 4×70=$280, 5×70=$350.  (M1, A1, A1)"]),
    # ── Section C — Thinking (L3), Q25–29 (last ones very hard) ──
    ("C25","C","Exponent Rules","L3","Thinking",4,
     "Show that (a<super>2</super>b<super>3</super>)<super>2</super> ÷ (a b<super>2</super>) = a<super>3</super>b<super>4</super> for a, b ≠ 0. State each exponent law you use.","work",
     ["(a<super>2</super>b<super>3</super>)<super>2</super> = a<super>4</super>b<super>6</super>  (power of a product / power of a power).  (M1)",
      "a<super>4</super>b<super>6</super> ÷ (a<super>1</super>b<super>2</super>) = a<super>4-1</super>b<super>6-2</super>  (quotient rule).  (M1)",
      "= a<super>3</super>b<super>4</super>.  (A1 result, C1 laws named)"]),
    ("C26","C","Applying Percents","L3","Thinking",4,
     "A jacket's price is increased by 25%, then the new price is discounted 20%. The final price is $120. Find the original price, and comment on the net effect.","work",
     ["Combined factor = 1.25 × 0.80 = 1.00.  (M1)",
      "1.00 × p = 120 → p = $120.  (M1, A1)",
      "Net effect: the two changes cancel — final price equals the original.  (A1)"]),
    ("C27","C","Applying Percents (mixture)","L3","Thinking",5,
     "A 750 mL solution is 20% acid. How much pure acid must be added to make it 40% acid? (Very hard.)","work",
     ["Acid now = 0.20 × 750 = 150 mL. Let x = pure acid added.  (M1)",
      "(150 + x)/(750 + x) = 0.40 → 150 + x = 300 + 0.4x.  (M1)",
      "0.6x = 150 → x = 250 mL of pure acid.  (M1, A1, A1)"]),
    ("C28","C","Applying Percents (chain)","L3","Thinking",5,
     "A number is increased by 20%, then that result is decreased by 15%, giving 102. Find the original number. (Very hard.)","work",
     ["Combined factor = 1.20 × 0.85 = 1.02.  (M1, M1)",
      "1.02 × p = 102 → p = 102 ÷ 1.02 = 100.  (M1, A1, A1)"]),
    ("C29","C","Fractions (work backwards)","L3","Thinking",6,
     "A tank is 2/5 full. After 24 L is added it is 4/7 full. Find the tank's capacity. (Very hard.)","work",
     ["Let C = capacity. (2/5)C + 24 = (4/7)C.  (M1)",
      "24 = (4/7 - 2/5)C = (20/35 - 14/35)C = (6/35)C.  (M1, M1)",
      "C = 24 × 35 ÷ 6 = 140 L.  (M1, A1)",
      "Check: 2/5×140 = 56; 56 + 24 = 80 = 4/7×140. ✓  (A1)"]),
    # ── Section D — Communication (L3), Q30 (very hard justify) ──
    ("D30","D","Square Roots & Irrationals","L3","Communication",4,
     "Ravi claims that √4 + √9 = √13. Is Ravi correct? Justify with a calculation and explain the general rule about square roots and addition. (Very hard.)","work",
     ["√4 + √9 = 2 + 3 = 5, but √13 ≈ 3.61.  (A1 calculation)",
      "Since 5 ≠ √13, Ravi is not correct.  (A1 conclusion)",
      "General rule: the square root does not distribute over addition; √a + √b ≠ √(a+b) in general.  (C1, C1 communication)"]),
]

TOTAL = sum(it[5] for it in ITEMS)
SECTIONS = {
    "A": "Section A — Knowledge & Understanding",
    "B": "Section B — Application",
    "C": "Section C — Thinking",
    "D": "Section D — Communication",
}

def work_for(marks, category):
    if category == "K/U":
        return None   # short ruled blank
    return {2: 52, 3: 84, 4: 118, 5: 150, 6: 182}.get(marks, 40 * marks)


def build_test():
    d = CMFlow(OUT_T, topic_title=TOPIC, subtitle="Module 1 Test",
               grade_badge="Grade 9 · MTH1W",
               meta_right=[f"Time: {DURATION}", f"Total: {TOTAL} marks"],
               name_date=True)
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
    d.space(6)
    d.body("<b>— END OF EXAM —</b>", ST_BODY, gap=4)
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
               info_line="MTH1W · Module 1 Test — Teacher Copy")
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
        tot[it[4]] = tot.get(it[4], 0) + it[5]
        lvltot[it[3]] = lvltot.get(it[3], 0) + it[5]
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
