#!/usr/bin/env python3
"""Concept Mastery — Grade 9 (MTH1W) Word Problems & Applications — TEST + MARKING SCHEME.

30 questions, 60 minutes, sections K/U -> Application -> Thinking -> Communication;
last four questions very hard. Curriculum: MTH1W. Marks defined once, drive paper +
blueprint + scheme. Run: python3 test_word-problems.py
"""
import os, sys
ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "_assets"))
sys.path.insert(0, ASSETS)
from cm_pdf import (CMFlow, ST_BODY, CM_BLUE, CM_DARK_GREY, CONTENT_X, __version__)

DIR = os.path.dirname(__file__)
OUT_T = os.path.join(DIR, "test_word-problems.pdf")
OUT_M = os.path.join(DIR, "test_word-problems_marking_scheme.pdf")
TOPIC = "Word Problems & Applications"
DURATION = "60 minutes"

# qid, section, subtopic, level, category, marks, stem, answer_mode, solution lines
ITEMS = [
    # ── Section A — Knowledge & Understanding (L1), Q1–15 ──
    ("A1","A","Translating","L1","K/U",1,"Write an expression for 'a number x increased by 9'.","short",["x + 9.  (A1)"]),
    ("A2","A","Translating","L1","K/U",1,"Write an expression for 'the product of 6 and a number n'.","short",["6n.  (A1)"]),
    ("A3","A","Translating","L1","K/U",1,"Write an equation for 'a number decreased by 5 is 12'.","short",["n - 5 = 12.  (A1)"]),
    ("A4","A","Percent","L1","K/U",1,"Find 50% of 84.","short",["42.  (A1)"]),
    ("A5","A","Distance–Rate–Time","L1","K/U",1,"A car goes 40 km in 1 hour. Find its speed.","short",["40 km/h.  (A1)"]),
    ("A6","A","Number","L1","K/U",1,"If the first of two consecutive integers is n, write the second.","short",["n + 1.  (A1)"]),
    ("A7","A","Geometry","L1","K/U",1,"One side of a square is s. Write an expression for its perimeter.","short",["4s.  (A1)"]),
    ("A8","A","Translating","L1","K/U",1,"Write an expression for 'twice a number, plus 3'.","short",["2x + 3.  (A1)"]),
    ("A9","A","Money","L1","K/U",1,"A shirt costs $c. Write an expression for the cost of 5 shirts.","short",["5c.  (A1)"]),
    ("A10","A","Number","L1","K/U",2,"The sum of a number and 7 is 20. Find the number.","short",["n + 7 = 20; n = 13.  (M1, A1)"]),
    ("A11","A","Translating","L1","K/U",2,"Three times a number is 27. Find the number.","short",["3n = 27; n = 9.  (M1, A1)"]),
    ("A12","A","Percent","L1","K/U",2,"Find 25% of $48.","short",["0.25 × 48 = $12.  (M1, A1)"]),
    ("A13","A","Distance–Rate–Time","L1","K/U",2,"A runner runs 30 km in 3 hours. Find the average speed.","short",["30 ÷ 3 = 10 km/h.  (M1, A1)"]),
    ("A14","A","Geometry","L1","K/U",2,"A rectangle is 6 cm long and 4 cm wide. Find its perimeter.","short",["2(6 + 4) = 20 cm.  (M1, A1)"]),
    ("A15","A","Number","L1","K/U",2,"A number is doubled and increased by 4 to give 16. Find the number.","short",["2n + 4 = 16 → 2n = 12 → n = 6.  (M1, A1)"]),
    # ── Section B — Application (L2), Q16–24 ──
    ("B16","B","Translating","L2","Application",2,"Four times a number, decreased by 7, is 29. Find the number.","work",
     ["4n - 7 = 29 → 4n = 36 → n = 9.  (M1, A1)"]),
    ("B17","B","Number","L2","Application",2,"The sum of two consecutive integers is 45. Find them.","work",
     ["2n + 1 = 45 → n = 22; integers 22 and 23.  (M1, A1)"]),
    ("B18","B","Money","L2","Application",2,"A taxi charges $4 plus $2 per km. A trip cost $20. How many km was it?","work",
     ["4 + 2k = 20 → 2k = 16 → k = 8 km.  (M1, A1)"]),
    ("B19","B","Mixture","L2","Application",2,"A 400 mL solution is 15% salt. How many millilitres of salt does it contain?","work",
     ["0.15 × 400 = 60 mL.  (M1, A1)"]),
    ("B20","B","Percent","L2","Application",2,"A jacket priced $90 is discounted 30%. Find the sale price.","work",
     ["90 - 0.30(90) = 90 - 27 = $63.  (M1, A1)"]),
    ("B21","B","Distance–Rate–Time","L2","Application",2,"A boat travels 96 km at 24 km/h. How long does the trip take?","work",
     ["t = 96 ÷ 24 = 4 hours.  (M1, A1)"]),
    ("B22","B","Number","L2","Application",3,"The sum of three consecutive integers is 72. Find them.","work",
     ["3n + 3 = 72 → 3n = 69 → n = 23; integers 23, 24, 25.  (M1, M1, A1)"]),
    ("B23","B","Percent","L2","Application",3,"After 13% tax is added, a bill is $79.10. Find the price before tax.","work",
     ["1.13p = 79.10 → p = $70.  (M1, M1, A1)"]),
    ("B24","B","Geometry","L2","Application",3,"Two angles are complementary (sum to 90°). One is 4 times the other. Find both angles.","work",
     ["x + 4x = 90 → 5x = 90 → x = 18; angles 18° and 72°.  (M1, M1, A1)"]),
    # ── Section C — Thinking (L3), Q25–29 (last three very hard) ──
    ("C25","C","Money","L3","Thinking",4,
     "A phone plan costs $30 per month plus $0.05 per minute. One month's bill was $47.50. How many minutes were used?","work",
     ["30 + 0.05m = 47.50.  (M1)", "0.05m = 17.50.  (M1)", "m = 350 minutes.  (A1, A1)"]),
    ("C26","C","Number","L3","Thinking",4,
     "The sum of three consecutive odd integers is 63. Find the integers.","work",
     ["n + (n+2) + (n+4) = 63.  (M1)", "3n + 6 = 63 → 3n = 57 → n = 19.  (M1, A1)",
      "Integers 19, 21, 23.  (A1)"]),
    ("C27","C","Mixture","L3","Thinking",5,
     "Coffee worth $7/kg is blended with coffee worth $13/kg to make 15 kg of blend worth $9/kg. How many kilograms of each type are used? (Very hard.)","work",
     ["Let x = kg of the $7 coffee, (15 - x) = kg of the $13 coffee.  (M1)",
      "7x + 13(15 - x) = 9(15) = 135.  (M1)",
      "7x + 195 - 13x = 135 → -6x = -60 → x = 10.  (A1, A1)",
      "10 kg of $7 coffee and 5 kg of $13 coffee.  (A1)"]),
    ("C28","C","Geometry","L3","Thinking",5,
     "A rectangle's length is 3 m more than twice its width. Its perimeter is 60 m. Find its dimensions and its area. (Very hard.)","work",
     ["Let w = width, length = 2w + 3.  2(w + 2w + 3) = 60.  (M1)",
      "6w + 6 = 60 → 6w = 54 → w = 9; length = 21.  (M1, A1)",
      "Dimensions 9 m by 21 m.  (A1)", "Area = 9 × 21 = 189 m<super>2</super>.  (A1)"]),
    ("C29","C","Distance–Rate–Time","L3","Thinking",6,
     "Two cyclists start 120 km apart and ride toward each other, one at 18 km/h and the other at 22 km/h. After how many hours do they meet, and how far has each travelled? (Very hard.)","work",
     ["Combined closing rate = 18 + 22 = 40 km/h.  (M1)",
      "40t = 120 → t = 3 hours.  (M1, A1)",
      "First cyclist: 18 × 3 = 54 km.  (A1, M1)",
      "Second cyclist: 22 × 3 = 66 km.  (A1)  (Check: 54 + 66 = 120.)"]),
    # ── Section D — Communication (L3), Q30 (very hard justify) ──
    ("D30","D","Percent","L3","Communication",4,
     "A store advertises '30% off, then take an extra 20% off the reduced price.' A customer claims this is the same as 50% off. Use a $100 item to explain why the customer is wrong, and state the single percent discount that is actually equivalent. (Very hard.)","work",
     ["30% off $100 gives $70.  (A1)",
      "An extra 20% off $70 gives 0.80 × 70 = $56.  (A1)",
      "The discounts multiply (0.70 × 0.80 = 0.56), they do not add, so the price is $56.  (C1)",
      "$56 paid means 44% off, not 50% off.  (C1)"]),
]

TOTAL = sum(it[5] for it in ITEMS)
SECTIONS = {"A": "Section A — Knowledge & Understanding", "B": "Section B — Application",
            "C": "Section C — Thinking", "D": "Section D — Communication"}

def work_for(marks, category):
    if category == "K/U":
        return None
    return {2: 52, 3: 84, 4: 118, 5: 150, 6: 182}.get(marks, 40 * marks)


def build_test():
    d = CMFlow(OUT_T, topic_title=TOPIC, subtitle="Module 4 Test",
               grade_badge="Grade 9 · MTH1W",
               meta_right=[f"Time: {DURATION}", f"Total: {TOTAL} marks"], name_date=True)
    d.start()
    d.body("Instructions: Show all work for full marks — a 'let' statement and an equation earn method "
           "marks. Marks for each question are shown in brackets. Calculators are permitted unless your "
           "teacher states otherwise.", ST_BODY, gap=12)
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
               info_line="MTH1W · Module 4 Test — Teacher Copy")
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
