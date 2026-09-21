#!/usr/bin/env python3
"""Concept Mastery — Grade 9 (MTH1W) Number Sense — HOMEWORK COPY + ANSWER KEY.

Per user revision: 6 questions in EACH level category (L1, L2, L3 = 18 total),
each touching a different concept; NO ruled lines / answer space under questions
(students work on their own paper). Curriculum tag: MTH1W. Full worked key.
All answers computed in Python. Run: python3 homework_number-sense.py
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

# (level, concept, stem, [worked solution lines]) — 6 per level, distinct concepts.
ITEMS = [
    # ── L1 — Fluency (6, different concepts) ──
    ("L1", "Integers", "Evaluate: (-11) + (-8) - (-5).",
     [f"(-11) + (-8) + (+5) = (-19) + 5 = {(-11)+(-8)+5}."]),
    ("L1", "BEDMAS", "Evaluate: 45 - 5 × 3 + 2<super>2</super>.",
     [f"2<super>2</super>=4; 5×3=15; 45 - 15 + 4 = {45-15+4}."]),
    ("L1", "Exponents", "Write as a single power: 9<super>4</super> × 9<super>3</super>.",
     ["Product rule: 9<super>4+3</super> = 9<super>7</super>."]),
    ("L1", "Fractions", "Evaluate in lowest terms: 7/10 - 1/5.",
     [f"7/10 - 2/10 = {fr(F(7,10)-F(1,5))}."]),
    ("L1", "Decimals/Percent", "Write 0.35 as a fraction in lowest terms and as a percent.",
     [f"0.35 = 35/100 = {fr(F(35,100))}; and 35%."]),
    ("L1", "Roots", "Evaluate: √144, and state whether it is rational.",
     ["√144 = 12; rational (144 = 12<super>2</super>)."]),
    # ── L2 — Application (6, different concepts) ──
    ("L2", "Fractions", "Evaluate in lowest terms: 3/8 × 4/9 ÷ 1/3.",
     ["3/8 × 4/9 = 12/72 = 1/6.", f"1/6 ÷ 1/3 = 1/6 × 3 = {fr(F(1,6)/F(1,3))}."]),
    ("L2", "Exponents", "Simplify to a single power and evaluate: (4<super>2</super>)<super>2</super> ÷ 4<super>2</super>.",
     [f"(4<super>2</super>)<super>2</super> = 4<super>4</super>; 4<super>4</super> ÷ 4<super>2</super> = 4<super>2</super> = {4**2}."]),
    ("L2", "Percent (word)", "A $120 coat is discounted 35%. Find the sale price.",
     [f"Discount = 0.35 × 120 = $42; sale price = 120 - 42 = ${120-42}  (or 120 × 0.65)."]),
    ("L2", "Ratios (word)", "A recipe uses sugar to flour in the ratio 2 : 5. If 350 g of flour is used, how much sugar is needed?",
     [f"350 ÷ 5 = 70 g per part; sugar = 2 × 70 = {2*70} g."]),
    ("L2", "Rational numbers", "Order from least to greatest: -0.3, -1/2, 0.25, -2/5.",
     ["Decimals: -1/2 = -0.5, -2/5 = -0.4.", "Order: -1/2, -2/5, -0.3, 0.25."]),
    ("L2", "Roots (estimate)", "Between which two consecutive whole numbers does √85 lie? Justify.",
     ["9<super>2</super> = 81 and 10<super>2</super> = 100, and 81 < 85 < 100.", "So √85 lies between 9 and 10."]),
    # ── L3 — Thinking (6, different concepts) ──
    ("L3", "Percent (work back)", "After a 25% discount, a bike sells for $180. Find the original price and check.",
     ["0.75 × p = 180 → p = 180 ÷ 0.75 = $240.", "Check: 240 × 0.75 = $180 ✓."]),
    ("L3", "Find the error", "Priya wrote 5<super>2</super> × 5<super>3</super> = 25<super>5</super>. Explain her error and give the correct answer.",
     ["Error: keep the base and ADD exponents; do not multiply the bases.",
      "5<super>2</super> × 5<super>3</super> = 5<super>5</super> = 3125, not 25<super>5</super>."]),
    ("L3", "Mixture", "A 600 mL drink is 30% juice. How much pure juice must be added to make it 40% juice?",
     ["Juice now = 0.30 × 600 = 180 mL. Let x = pure juice added.",
      "(180 + x)/(600 + x) = 0.40 → 180 + x = 240 + 0.4x → 0.6x = 60 → x = 100 mL."]),
    ("L3", "Rate reasoning", "A runner covers 12 km in 1 h, then 6 km in 0.5 h. Find the average speed for the whole run and explain why it is not the mean of the two speeds.",
     [f"(12 + 6)/(1 + 0.5) = 18/1.5 = {18/1.5:.0f} km/h.",
      "It divides total distance by total time; the simple mean of 12 and 12 ignores how long each part took."]),
    ("L3", "Fractions multi-step", "Evaluate in lowest terms: (3/4 - 1/2) ÷ (2/3 + 1/6).",
     ["3/4 - 1/2 = 1/4; 2/3 + 1/6 = 5/6.", f"1/4 ÷ 5/6 = 1/4 × 6/5 = {fr(F(1,4)/(F(2,3)+F(1,6)))}."]),
    ("L3", "Proportion (scale)", "On a map, 2 cm represents 15 km. Two towns are 9 cm apart on the map. Find the real distance.",
     ["2 cm : 15 km, so 1 cm : 7.5 km.", f"9 × 7.5 = {9*7.5:.1f} km."]),
]


def build_questions():
    d = CMFlow(OUT_Q, topic_title=TOPIC, subtitle=SUBTITLE,
               info_line="MTH1W · Homework — Independent Practice", name_date=True)
    d.start()
    d.learning_goal("Practise integers, exponent laws, fractions, roots, percents and ratios independently.")
    d.body("Work each question on your own paper and show your steps. Levels: L1 fluency, "
           "L2 application, L3 thinking. Full worked solutions are in the Answer Key.", ST_BODY, gap=12)
    last = None
    for i, (lvl, concept, stem, _sol) in enumerate(ITEMS, start=1):
        if lvl != last:
            names = {"L1": "Level 1 — Fluency", "L2": "Level 2 — Application", "L3": "Level 3 — Thinking"}
            d.heading(names[lvl], color=CM_BLUE)
            last = lvl
        tagged = f"{stem}  <font color='#2D7DD2'><b>[{concept}]</b></font>"
        d.question(i, tagged, answer="none")
    return d.build()


def build_answers():
    d = CMFlow(OUT_A, topic_title=TOPIC, subtitle="Answer Key — Worked Solutions",
               info_line="MTH1W · Homework — Answer Key")
    d.start()
    d.body("Worked solutions with method lines. Curriculum: MTH1W (Grade 9 de-streamed math).",
           ST_BODY, gap=12)
    for i, (lvl, concept, stem, sol) in enumerate(ITEMS, start=1):
        d.key_entry(i, [f"<b>[{lvl} · {concept}]</b> " + sol[0]] + sol[1:])
    return d.build()


if __name__ == "__main__":
    p = build_questions(); a = build_answers()
    from collections import Counter
    lv = Counter(x[0] for x in ITEMS)
    print(f"engine {__version__}  built {p} and {a}")
    print(f"items={len(ITEMS)}  by-level {dict(lv)}")
