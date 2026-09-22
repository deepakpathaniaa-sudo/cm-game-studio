#!/usr/bin/env python3
"""Concept Mastery — Grade 9 (MTH1W) Number Sense — CLASS COPY (guided).

Structure (per user revision): a short warm-up, then for EACH sub-topic one
worked Example followed by 3–4 practice questions of varying complexity.
No "I do / We do" labels. Answers on the final page(s). Open working space,
no ruled lines. Curriculum tag: MTH1W. All answers computed in Python.
Run: python3 class_number-sense.py
"""
import os, sys
from fractions import Fraction as F

ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "_assets"))
sys.path.insert(0, ASSETS)
from cm_pdf import CMFlow, ST_BODY, CM_BLUE, CM_MED_BLUE, __version__

OUT = os.path.join(os.path.dirname(__file__), "class_number-sense.pdf")
TOPIC = "Number Sense"
SUBTITLE = "Integers · BEDMAS · Exponents · Fractions · Roots · Percent · Ratios"
INFO = "MTH1W · Class — Guided Practice"

def fr(x):
    x = F(x); return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)

# Per sub-topic: name, worked example (lines), and 3–4 (level, stem, answer) items.
SUBTOPICS = [
    ("Integers",
     ["Evaluate (-8) - (-3) + (-5).",
      "Add the opposite: (-8) + (+3) + (-5).",
      "Combine: (-8 + 3) = -5, then (-5) + (-5) = -10.   Answer: -10."],
     [("L1", "Evaluate: (-6) + (-9).", f"{(-6)+(-9)}"),
      ("L1", "Evaluate: (-15) - (-4).", f"{(-15)-(-4)}"),
      ("L2", "Evaluate: (-3) × 4 + (-2) × (-5).", f"{(-3)*4+(-2)*(-5)}"),
      ("L3", "At 6 a.m. the temperature was -4 °C. It rose 9 °C by noon, then fell 6 °C by evening. Find the evening temperature.",
       f"-4 + 9 - 6 = {-4+9-6} °C")]),
    ("Order of Operations (BEDMAS)",
     ["Evaluate 24 - 3 × (2 + 3)<super>2</super> ÷ 5.",
      "Brackets: 2 + 3 = 5.  Exponent: 5<super>2</super> = 25.",
      "3 × 25 = 75; 75 ÷ 5 = 15; 24 - 15 = 9.   Answer: 9."],
     [("L1", "Evaluate: 8 + 6 × 2.", f"{8+6*2}"),
      ("L2", "Evaluate: (7 - 2)<super>2</super> - 4 × 3.", f"{(7-2)**2-4*3}"),
      ("L2", "Evaluate: 36 ÷ (2 + 4) + 5 × 2.", f"{36//(2+4)+5*2}"),
      ("L3", "Evaluate: 50 - [3 + 2 × (4<super>2</super> - 10)].",
       f"4<super>2</super>-10=6; 2×6=12; 3+12=15; 50-15 = {50-(3+2*(16-10))}")]),
    ("Exponent Rules",
     ["Simplify (x<super>5</super> × x<super>2</super>) ÷ x<super>3</super>, x ≠ 0.",
      "Product rule: x<super>5+2</super> = x<super>7</super>.  Quotient rule: x<super>7-3</super> = x<super>4</super>.",
      "Answer: x<super>4</super>."],
     [("L1", "Write as a single power: 4<super>3</super> × 4<super>2</super>.", "4<super>5</super>"),
      ("L1", "Simplify, n ≠ 0: n<super>6</super> ÷ n<super>2</super>.", "n<super>4</super>"),
      ("L2", "Evaluate: (2<super>3</super>)<super>2</super> × 2<super>0</super>.", f"2<super>6</super> × 1 = {2**6}"),
      ("L3", "Explain why a<super>3</super> + a<super>3</super> ≠ a<super>6</super>, and give the correct simplified form.",
       "Adding like terms adds coefficients, not exponents: a<super>3</super> + a<super>3</super> = 2a<super>3</super>.")]),
    ("Fractions — Four Operations",
     ["Evaluate 5/6 - 1/3 × 3/4.",
      "Multiply first: 1/3 × 3/4 = 1/4.",
      "5/6 - 1/4, LCD 12: 10/12 - 3/12 = 7/12.   Answer: 7/12."],
     [("L1", "Evaluate in lowest terms: 2/5 + 1/10.", f"{fr(F(2,5)+F(1,10))}"),
      ("L1", "Evaluate in lowest terms: 3/4 × 8/9.", f"{fr(F(3,4)*F(8,9))}"),
      ("L2", "Evaluate in lowest terms: 7/8 ÷ 3/4.", f"{fr(F(7,8)/F(3,4))}"),
      ("L3", "Evaluate in lowest terms: 1/2 + 2/3 ÷ 4/3 - 1/6.",
       f"÷ first: 2/3÷4/3 = 1/2; then 1/2 + 1/2 - 1/6 = {fr(F(1,2)+F(1,2)-F(1,6))}")]),
    ("Rational Numbers",
     ["Order from least to greatest: -0.75, -2/3, -0.7, -5/6.",
      "As decimals: -5/6 ≈ -0.833, -2/3 ≈ -0.667.",
      "Order: -5/6 < -0.75 < -0.7 < -2/3."],
     [("L1", "Which is larger: -3/4 or -2/3?", "-2/3 (since -0.667 > -0.75)"),
      ("L2", "Order from least to greatest: -1.2, 3/4, -1/4, 1.5.", "-1.2, -1/4, 3/4, 1.5"),
      ("L2", "Find a rational number between 1/3 and 1/2.", "e.g. 5/12 (the average of 1/3 and 1/2)"),
      ("L3", "Is the sum of two negative rational numbers always negative? Explain with an example.",
       "Yes. e.g. -1/2 + (-1/3) = -5/6 < 0; adding two negatives always gives a negative.")]),
    ("Square Roots & Irrationals",
     ["Is √72 rational or irrational? Estimate it to one decimal place.",
      "72 is not a perfect square → irrational.",
      "8<super>2</super> = 64 and 9<super>2</super> = 81, so √72 ≈ 8.5."],
     [("L1", "Evaluate: √121.", "11 (rational)"),
      ("L1", "Between which two whole numbers does √40 lie?", "6 and 7 (36 < 40 < 49)"),
      ("L2", "Classify each as rational or irrational: √16, √17, 0.25, π.",
       "√16 rational, √17 irrational, 0.25 rational, π irrational"),
      ("L3", "Explain why √2 cannot be written as a terminating or repeating decimal.",
       "√2 is irrational — it is not a ratio of integers, so its decimal never terminates or repeats.")]),
    ("Fractions ↔ Decimals ↔ Percent",
     ["Convert 3/8 to a decimal and a percent.",
      "3 ÷ 8 = 0.375.",
      "0.375 × 100 = 37.5%.   Answer: 0.375 = 37.5%."],
     [("L1", "Write 0.6 as a fraction (lowest terms) and a percent.", f"{fr(F(6,10))} ; 60%"),
      ("L1", "Write 45% as a fraction in lowest terms.", f"{fr(F(45,100))}"),
      ("L2", "Order from least to greatest: 0.7, 3/5, 65%.", "3/5 (0.6), 65% (0.65), 0.7"),
      ("L3", "A student scores 21/25 on a test. Write it as a percent and state whether it is above 80%.",
       "21/25 = 84%; yes, 84% > 80%.")]),
    ("Applying Percents",
     ["A $90 item is discounted 30%. Find the sale price.",
      "Discount = 0.30 × 90 = $27.",
      "Sale price = 90 - 27 = $63  (or 90 × 0.70 = $63)."],
     [("L1", "Find 15% of 200.", f"{int(0.15*200)}"),
      ("L2", "A $45 shirt has 13% HST added. Find the total cost.", f"45 × 1.13 = ${45*1.13:.2f}"),
      ("L2", "A population grows from 400 to 460. Find the percent increase.", "60 ÷ 400 = 15%"),
      ("L3", "After a 20% discount a game costs $72. Work backwards to find the original price.",
       f"0.80 × p = 72 → p = 72 ÷ 0.80 = ${int(72/0.8)}")]),
    ("Ratios, Rates & Proportions",
     ["4 pens cost $5.00. Find the cost of 10 pens.",
      "Unit rate: 5.00 ÷ 4 = $1.25 per pen.",
      "10 × 1.25 = $12.50.   Answer: $12.50."],
     [("L1", "Simplify the ratio 18 : 24.", "3 : 4"),
      ("L2", "A car uses 6 L of fuel per 100 km. How much fuel is needed for 250 km?", f"6 × 2.5 = {6*2.5:.0f} L"),
      ("L2", "Share $60 in the ratio 2 : 3.", "$24 and $36"),
      ("L3", "A recipe for 4 servings uses 300 g of flour. How much flour is needed for 10 servings?",
       f"300 ÷ 4 × 10 = {300//4*10} g")]),
]

WARMUP = [
    ("Evaluate: (-7) + (+3).", f"{-7+3}"),
    ("Write 3 × 3 × 3 as a single power, then find its value.", f"3<super>3</super> = {3**3}"),
    ("Reduce the fraction 20/25 to lowest terms.", f"{fr(F(20,25))}"),
]


def build():
    d = CMFlow(OUT, topic_title=TOPIC, subtitle=SUBTITLE, info_line=INFO, name_date=True)
    d.start()
    d.learning_goal("Use integers, exponent laws, fractions, roots, percents and ratios to solve multi-step problems.")

    d.heading("Warm-up  (quick recall)")
    for i, (stem, _a) in enumerate(WARMUP, start=1):
        d.question(i, stem, answer="work", work_pts=30)

    d.heading("Examples & Practice")
    d.body("For each skill, study the worked <b>Example</b>, then solve the questions that follow. "
           "Difficulty rises within each set (L1 → L3). Answers are on the last page.", ST_BODY, gap=10)

    n = len(WARMUP)
    answers = []   # (num, level, ans)
    for name, example, qs in SUBTOPICS:
        d.heading(name, color=CM_MED_BLUE)
        d.example_box(example)
        for lvl, stem, ans in qs:
            n += 1
            tagged = f"{stem}  <font color='#2D7DD2'><b>[{lvl}]</b></font>"
            wp = {"L1": 60, "L2": 95, "L3": 130}[lvl]  # generous open work space, no lines
            d.question(n, tagged, answer="work", work_pts=wp)
            answers.append((n, lvl, ans))

    # Answers page
    d._new_page()
    d.c.setFillColor(CM_BLUE); d.c.setFont("DejaVuSans-Bold", 16)
    d.c.drawCentredString(306, d.y, "Answers")
    d.y -= 28
    wu = "   ".join(f"W{i}) {a}" for i, (_s, a) in enumerate(WARMUP, start=1))
    d.body("<b>Warm-up:</b> " + wu, ST_BODY, gap=12)
    for num, lvl, ans in answers:
        d.key_entry(num, [f"({lvl}) {ans}"])

    path = d.build()
    return path, len(answers)


if __name__ == "__main__":
    p, n = build()
    from collections import Counter
    c = Counter(a[1] for st in SUBTOPICS for a in [(0, q[0]) for q in st[2]])
    print(f"engine {__version__}  built {p}  practice_questions={n}  levels={dict(c)}")
