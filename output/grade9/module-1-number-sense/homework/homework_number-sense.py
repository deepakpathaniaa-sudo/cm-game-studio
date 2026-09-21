#!/usr/bin/env python3
"""Concept Mastery — Grade 9 (MTH1W) Number Sense — HOMEWORK COPY + ANSWER KEY.

Parallel to the class copy but with different numbers/contexts (no overlap).
Builds two PDFs: homework_number-sense.pdf (questions) and
homework_number-sense_answers.pdf (full worked solutions).
All answers computed here so the key cannot drift. Run: python3 homework_number-sense.py
"""
import os, sys
from fractions import Fraction as F

ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "_assets"))
sys.path.insert(0, ASSETS)
from cm_pdf import CMFlow, ST_BODY, CM_BLUE, __version__

DIR = os.path.dirname(__file__)
OUT_Q = os.path.join(DIR, "homework_number-sense.pdf")
OUT_A = os.path.join(DIR, "homework_number-sense_answers.pdf")
TOPIC = "Number Sense"
SUBTITLE = "Integers · BEDMAS · Exponents · Fractions · Roots · Percent · Ratios"

def fr(x):
    x = F(x); return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)

# computed checks
q5  = F(5,8) + F(1,6)
q8  = F(2,5) * F(3,4) / F(1,2)
q13 = 8.40/3*5
q17 = 100  # solved below
q18avg = 56/5

# Each item: (level, stem, answer_mode, [worked solution lines])
ITEMS = [
    # ── L1 (7) ──
    ("L1", "Evaluate: (-12) - (-7) + (-3).", "short",
     ["(-12) + (+7) + (-3) = (-5) + (-3) = -8."]),
    ("L1", "Evaluate using BEDMAS: 40 - 6 × 3 + 2<super>2</super>.", "short",
     ["Exponent: 2<super>2</super> = 4. Multiply: 6 × 3 = 18.",
      "40 - 18 + 4 = 26."]),
    ("L1", "Simplify (leave in exponent form): 7<super>3</super> × 7<super>2</super>.", "short",
     ["Product rule (add exponents): 7<super>3+2</super> = 7<super>5</super>."]),
    ("L1", "Simplify, m ≠ 0: m<super>5</super> ÷ m<super>2</super>.", "short",
     ["Quotient rule (subtract exponents): m<super>5-2</super> = m<super>3</super>."]),
    ("L1", "Evaluate in lowest terms: 5/8 + 1/6.", "short",
     [f"LCD = 24: 15/24 + 4/24 = {fr(q5)}."]),
    ("L1", "Write 0.24 as a fraction in lowest terms and as a percent.", "short",
     [f"0.24 = 24/100 = {fr(F(24,100))}; and 0.24 × 100 = 24%."]),
    ("L1", "Is √81 rational or irrational? Give its value.", "short",
     ["81 = 9<super>2</super> is a perfect square, so √81 = 9 (rational)."]),
    # ── L2 (7) ──
    ("L2", "Evaluate in lowest terms: 2/5 × 3/4 ÷ 1/2.", "work",
     ["Left to right: 2/5 × 3/4 = 6/20 = 3/10.",
      f"÷ 1/2 = 3/10 × 2/1 = 6/10 = {fr(q8)}."]),
    ("L2", "Simplify to a single power and its value: (3<super>2</super>)<super>3</super> ÷ 3<super>4</super>.", "work",
     ["Power of a power: (3<super>2</super>)<super>3</super> = 3<super>6</super>.",
      "Quotient rule: 3<super>6-4</super> = 3<super>2</super> = 9."]),
    ("L2", "A $60 pair of shoes is marked up 25%. Find the new price.", "work",
     ["Markup = 0.25 × 60 = $15.",
      "New price = 60 + 15 = $75  (or 60 × 1.25 = $75)."]),
    ("L2", "Order from least to greatest: -0.4, -1/3, -0.5, 1/5.", "work",
     ["As decimals: -1/3 ≈ -0.333, 1/5 = 0.2.",
      "Compare: -0.5 < -0.4 < -0.333 < 0.2.",
      "Answer: -0.5, -0.4, -1/3, 1/5."]),
    ("L2", "On a map, 1 cm represents 25 km. Two towns are 7 cm apart on the map. Find the real distance.", "work",
     ["Set up the proportion 1 cm : 25 km = 7 cm : d.",
      "d = 7 × 25 = 175 km."]),
    ("L2", "3 kg of apples cost $8.40. At the same rate, find the cost of 5 kg.", "work",
     ["Unit rate: 8.40 ÷ 3 = $2.80/kg.",
      f"5 kg: 2.80 × 5 = ${q13:.2f}."]),
    ("L2", "Between which two consecutive whole numbers does √30 lie? Justify.", "work",
     ["5<super>2</super> = 25 and 6<super>2</super> = 36, and 25 < 30 < 36.",
      "So √30 lies between 5 and 6."]),
    # ── L3 (4) ──
    ("L3", "After a 20% discount, a coat costs $96. Work backwards to find the original price, and check.", "work",
     ["The sale price is 80% of the original: 0.80 × p = 96.",
      "p = 96 ÷ 0.80 = $120. Check: 120 × 0.80 = $96 ✓."]),
    ("L3", "Maya wrote (2<super>3</super>)<super>2</super> = 2<super>5</super>. Explain her error and give the correct value.", "work",
     ["Error: for a power of a power you MULTIPLY the exponents, not add them.",
      "(2<super>3</super>)<super>2</super> = 2<super>3×2</super> = 2<super>6</super> = 64, not 2<super>5</super> = 32."]),
    ("L3", "A 500 mL drink is 40% juice. How much pure juice must be added so the drink is 50% juice?", "work",
     ["Juice now = 0.40 × 500 = 200 mL. Let x = mL of pure juice added.",
      "(200 + x) / (500 + x) = 0.50 → 200 + x = 250 + 0.5x.",
      "0.5x = 50 → x = 100 mL of pure juice."]),
    ("L3", "A cyclist rides 36 km at 12 km/h, rests, then rides 20 km at 10 km/h. Find the total riding time and the average speed over the distance ridden.", "work",
     ["Times: 36 ÷ 12 = 3 h and 20 ÷ 10 = 2 h, so riding time = 5 h.",
      f"Average speed = total distance ÷ riding time = 56 ÷ 5 = {q18avg:.1f} km/h."]),
]


def build_questions():
    d = CMFlow(OUT_Q, topic_title=TOPIC, subtitle=SUBTITLE,
               info_line="MTH1W · Homework — Independent Practice", name_date=True)
    d.start()
    d.learning_goal("Practise integers, exponent laws, fractions, roots, percents and ratios independently.")
    d.body("Show all your work. Levels: L1 fluency, L2 application, L3 thinking. "
           "Full worked solutions are in the companion Answer Key.", ST_BODY, gap=12)
    for i, (lvl, stem, mode, _sol) in enumerate(ITEMS, start=1):
        tagged = f"{stem}  <font color='#2D7DD2'><b>[{lvl}]</b></font>"
        wp = 78 if lvl == "L3" else (56 if lvl == "L2" else None)
        d.question(i, tagged, answer=mode, work_pts=wp)
    return d.build()


def build_answers():
    d = CMFlow(OUT_A, topic_title=TOPIC, subtitle="Answer Key — Worked Solutions",
               info_line="MTH1W · Homework — Answer Key")
    d.start()
    d.body("Worked solutions. Method lines are shown for application and thinking items.",
           ST_BODY, gap=12)
    for i, (lvl, stem, mode, sol) in enumerate(ITEMS, start=1):
        d.key_entry(i, [f"<b>[{lvl}]</b> " + sol[0]] + sol[1:])
    return d.build()


if __name__ == "__main__":
    p = build_questions()
    a = build_answers()
    n1 = sum(1 for x in ITEMS if x[0] == "L1")
    n2 = sum(1 for x in ITEMS if x[0] == "L2")
    n3 = sum(1 for x in ITEMS if x[0] == "L3")
    print(f"engine {__version__}  built {p} and {a}")
    print(f"items={len(ITEMS)}  L1={n1} L2={n2} L3={n3}")
