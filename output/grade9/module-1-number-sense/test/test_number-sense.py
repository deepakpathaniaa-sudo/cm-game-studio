#!/usr/bin/env python3
"""Concept Mastery — Grade 9 (MTH1W) Number Sense — MODULE TEST + MARKING SCHEME.

Builds test_number-sense.pdf (student, no answers) and
test_number-sense_marking_scheme.pdf (blueprint table + worked solutions with
method (M) / answer (A) marks). Marks are defined once, per exam-generator §2–5,
and drive both files, so blueprint marks = paper marks = scheme marks.
Run: python3 test_number-sense.py
"""
import os, sys
from fractions import Fraction as F

ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "_assets"))
sys.path.insert(0, ASSETS)
from cm_pdf import (CMFlow, ST_BODY, ST_BODY_B, CM_BLUE, CM_MED_BLUE, CM_DARK_GREY,
                    CONTENT_X, CONTENT_WIDTH, __version__)

DIR = os.path.dirname(__file__)
OUT_T = os.path.join(DIR, "test_number-sense.pdf")
OUT_M = os.path.join(DIR, "test_number-sense_marking_scheme.pdf")
TOPIC = "Number Sense"
DURATION = "50 minutes"

# ── Master item table — single source for paper + blueprint + scheme ─────────
# fields: qid, section, subtopic, level, category, marks, stem, answer_mode,
#         solution(list of "text  <M/A tags>")
ITEMS = [
    # ── Section A — Knowledge / Understanding (short answer) ──
    ("A1","A","Integers","L1","K/U",2,
     "Evaluate: (-15) + (-6) - (-4).","short",
     ["(-15) + (-6) + (+4) = (-21) + 4 = -17.  (A1 setup, A1 answer)"]),
    ("A2","A","Order of Operations","L1","K/U",2,
     "Evaluate: 30 - 4 × 2<super>3</super> ÷ 8.","short",
     ["2<super>3</super> = 8; 4 × 8 = 32; 32 ÷ 8 = 4; 30 - 4 = 26.  (M1 order, A1 answer)"]),
    ("A3","A","Exponent Rules","L1","K/U",2,
     "Simplify, leaving your answer as a single power: 6<super>5</super> × 6<super>2</super> ÷ 6<super>3</super>.","short",
     ["Add then subtract exponents: 6<super>5+2-3</super> = 6<super>4</super>.  (M1 method, A1 answer)"]),
    ("A4","A","Fractions","L1","K/U",2,
     "Evaluate in lowest terms: 3/4 - 5/8.","short",
     [f"6/8 - 5/8 = {F(3,4)-F(5,8)}.  (M1 common denom, A1 answer)"]),
    ("A5","A","Fractions ↔ Decimals ↔ Percent","L1","K/U",2,
     "Write 5/8 as a decimal and as a percent.","short",
     ["5 ÷ 8 = 0.625 = 62.5%.  (A1 decimal, A1 percent)"]),
    ("A6","A","Square Roots & Irrationals","L1","K/U",2,
     "State whether √44 is rational or irrational, and name the two consecutive whole numbers it lies between.","short",
     ["44 is not a perfect square → irrational. 6<super>2</super>=36 < 44 < 49=7<super>2</super>, so between 6 and 7.  (A1 classify, A1 bounds)"]),
    ("A7","A","Applying Percents","L1","K/U",2,
     "Find 30% of 250.","short",
     ["0.30 × 250 = 75.  (A2 answer)"]),
    ("A8","A","Ratios, Rates & Proportions","L1","K/U",2,
     "A car travels 180 km in 3 hours at a steady speed. Find its speed as a unit rate.","short",
     ["180 ÷ 3 = 60 km/h.  (M1 setup, A1 answer)"]),
    # ── Section B — Application (structured) ──
    ("B9","B","Fractions","L2","Application",3,
     "Evaluate, showing each step, in lowest terms: (2/3 + 1/2) × 6/5.","work",
     ["2/3 + 1/2 = 4/6 + 3/6 = 7/6.  (M1)",
      "7/6 × 6/5 = 42/30 = 7/5.  (M1 multiply, A1 answer)"]),
    ("B10","B","Applying Percents","L2","Application",3,
     "A phone costs $540 before tax. Find the total cost with 13% HST, and state the amount of tax paid.","work",
     ["Total = 540 × 1.13 = $610.20.  (M1 method, A1 total)",
      "Tax = 610.20 - 540 = $70.20.  (A1 tax)"]),
    ("B11","B","Exponent Rules","L2","Application",2,
     "Simplify to a single power, then evaluate: (5<super>2</super>)<super>2</super> ÷ 5<super>3</super> × 5<super>0</super>.","work",
     ["(5<super>2</super>)<super>2</super> = 5<super>4</super>; 5<super>4</super> ÷ 5<super>3</super> × 1 = 5<super>1</super> = 5.  (M1 laws, A1 value)"]),
    ("B12","B","Ratios, Rates & Proportions","L2","Application",3,
     "A fruit punch mixes orange juice to pineapple juice in the ratio 3 : 5. To make 4000 mL of punch, how much of each juice is needed?","work",
     ["Total parts = 3 + 5 = 8; one part = 4000 ÷ 8 = 500 mL.  (M1)",
      "Orange = 3 × 500 = 1500 mL; pineapple = 5 × 500 = 2500 mL.  (A1 orange, A1 pineapple)"]),
    # ── Section C — Thinking (rich problem) ──
    ("C13","C","Applying Percents (multi-step)","L3","Thinking",5,
     "A jacket's price is first increased by 20%. Later the new price is reduced by 20%. After both changes the jacket sells for $96. "
     "Find the original price. Then decide, with reasoning, whether the final price equals the original price.","work",
     ["Let p be the original price. After +20% then -20%: p × 1.20 × 0.80 = p × 0.96.  (M1 model)",
      "p × 0.96 = 96 → p = 96 ÷ 0.96 = $100.  (M1 solve, A1 answer)",
      "Final = 96, original = 100, so they are NOT equal.  (A1)",
      "Reason: +20% then -20% multiplies by 0.96, i.e. 96% of the original — a net 4% loss. The percentages act on different amounts.  (A1 reasoning)"]),
    # ── Section D — Communication (explain / justify) ──
    ("D14","D","Square Roots & Irrationals","L3","Communication",3,
     "Jordan claims that √16 + √9 = √25. Is Jordan correct? Justify your answer with a calculation and a clear explanation.","work",
     ["√16 + √9 = 4 + 3 = 7, but √25 = 5.  (A1 calculation)",
      "Since 7 ≠ 5, Jordan is not correct.  (A1 conclusion)",
      "Explanation: the square root does not distribute over addition; in general √a + √b ≠ √(a+b).  (C1 communication)"]),
]

TOTAL = sum(it[5] for it in ITEMS)   # 35
SECTIONS = {
    "A": "Section A — Knowledge & Understanding",
    "B": "Section B — Application",
    "C": "Section C — Thinking",
    "D": "Section D — Communication",
}

def work_for(marks, category):
    if category == "K/U":
        return None  # short blank
    return {2: 60, 3: 90, 5: 150}.get(marks, 40 * marks)


def build_test():
    d = CMFlow(OUT_T, topic_title=TOPIC, subtitle="Module 1 Test",
               grade_badge="Grade 9 · MTH1W",
               meta_right=[f"Time: {DURATION}", f"Total: {TOTAL} marks"],
               name_date=True)
    d.start()
    d.body("Instructions: Show all work for full marks. Answers only earn the answer mark. "
           "Marks for each question are shown in brackets.", ST_BODY, gap=12)
    last_section = None
    qnum = 0
    for (qid, sec, sub, lvl, cat, marks, stem, mode, sol) in ITEMS:
        if sec != last_section:
            d.heading(SECTIONS[sec], color=CM_BLUE)
            last_section = sec
        qnum += 1
        stem_tag = f"{stem}  <font color='#2D7DD2'><b>[{marks}]</b></font>"
        d.question(qnum, stem_tag, answer=mode, work_pts=work_for(marks, cat))
    # END OF EXAM
    d.space(6)
    d.body("<b>— END OF EXAM —</b>", ST_BODY, gap=4)
    return d.build()


def _row(d, cols, xs, bold=False, color=CM_DARK_GREY):
    from cm_pdf import CONTENT_TOP_Y
    d.ensure(16)
    font = ("DejaVuSans-Bold", 9) if bold else ("DejaVuSans", 9)
    d.c.setFont(*font); d.c.setFillColor(CM_BLUE if bold else color)
    for text, x in zip(cols, xs):
        d.c.drawString(x, d.y - 10, str(text))
    d.y -= 18


def build_scheme():
    d = CMFlow(OUT_M, topic_title=TOPIC, subtitle="Marking Scheme & Blueprint",
               info_line="MTH1W · Module 1 Test — Teacher Copy")
    d.start()
    # ── Blueprint table (no rules/fills, per layout §6 + TOC style) ──
    d.heading("Blueprint", color=CM_BLUE)
    d.body(f"Total: {TOTAL} marks · {DURATION}. Categories: K/U, Application (App), "
           "Thinking (Think), Communication (Comm).", ST_BODY, gap=8)
    xs = [CONTENT_X, CONTENT_X+55, CONTENT_X+250, CONTENT_X+300, CONTENT_X+360, CONTENT_X+420]
    _row(d, ["Q","Sub-topic","Level","Marks","Category","Section"], xs, bold=True)
    for (qid, sec, sub, lvl, cat, marks, *_r) in ITEMS:
        catshort = {"K/U":"K/U","Application":"App","Thinking":"Think","Communication":"Comm"}[cat]
        _row(d, [qid, sub[:30], lvl, marks, catshort, sec], xs)
    # category totals
    d.space(4)
    tot = {}
    for it in ITEMS:
        tot[it[4]] = tot.get(it[4], 0) + it[5]
    lvltot = {}
    for it in ITEMS:
        lvltot[it[3]] = lvltot.get(it[3], 0) + it[5]
    d.body("<b>By category (marks):</b> " + " · ".join(f"{k} {v}" for k, v in tot.items()), ST_BODY, gap=4)
    d.body("<b>By level (marks):</b> " + " · ".join(f"{k} {lvltot[k]}" for k in ('L1','L2','L3'))
           + f"  →  L1 {lvltot['L1']*100//TOTAL}% · L2 {lvltot['L2']*100//TOTAL}% · L3 {lvltot['L3']*100//TOTAL}%",
           ST_BODY, gap=12)
    # ── Worked solutions with M/A marks ──
    d.heading("Worked Solutions & Mark Allocation", color=CM_BLUE)
    qnum = 0
    for (qid, sec, sub, lvl, cat, marks, stem, mode, sol) in ITEMS:
        qnum += 1
        head = f"<b>({qid} · {cat} · {marks} marks)</b>"
        d.key_entry(qnum, [head] + sol)
    return d.build()


if __name__ == "__main__":
    t = build_test()
    m = build_scheme()
    from collections import Counter
    lv = Counter(it[3] for it in ITEMS)
    lvm = Counter()
    for it in ITEMS: lvm[it[3]] += it[5]
    print(f"engine {__version__}  built {t} and {m}")
    print(f"total_marks={TOTAL}  questions={len(ITEMS)}  by-count {dict(lv)}  by-marks {dict(lvm)}")
