#!/usr/bin/env python3
"""Concept Mastery — Grade 9 (MTH1W) Number Sense — CLASS COPY (guided).

Original content. Layout/branding: skill-cm-layout-branding via _assets/cm_pdf.py.
Every numeric answer is computed here (fractions/math) so the answer page cannot
drift from the questions. Run: python3 class_number-sense.py
"""
import os, sys
from fractions import Fraction as F
import math

ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "_assets"))
sys.path.insert(0, ASSETS)
from cm_pdf import CMFlow, ST_BODY, ST_BODY_B, ST_LABEL, __version__

OUT = os.path.join(os.path.dirname(__file__), "class_number-sense.pdf")
TOPIC = "Number Sense"
SUBTITLE = "Integers · BEDMAS · Exponents · Fractions · Roots · Percent · Ratios"
INFO = "MTH1W · Class — Guided Practice"

# ── Guided-practice items: (level, stem, computed answer string) ─────────────
def fr(f):  # pretty fraction
    f = F(f)
    return f"{f.numerator}/{f.denominator}" if f.denominator != 1 else str(f.numerator)

GUIDED = [
    ("L1", "Evaluate: (-8) + (-5) - (-3).",
     f"{(-8)+(-5)-(-3)}"),
    ("L1", "Simplify using exponent laws: 5<super>6</super> ÷ 5<super>2</super>. Leave the answer in exponent form.",
     "5<super>6-2</super> = 5<super>4</super>"),
    ("L1", "Evaluate: 3 + 4 × 2<super>2</super> - 10 ÷ 5.",
     f"{3 + 4*2**2 - 10//5}  (3 + 16 - 2)"),
    ("L1", "Write 0.35 as a fraction in lowest terms, then as a percent.",
     f"{fr(F(35,100))} ; 35%"),
    ("L2", "Evaluate: 2/3 - 1/4 + 5/6. Give the answer in lowest terms.",
     f"{fr(F(2,3)-F(1,4)+F(5,6))}"),
    ("L2", "Simplify: (2<super>3</super>)<super>2</super> × 2<super>0</super>. Give a single power of 2 and its value.",
     f"2<super>6</super> × 1 = 2<super>6</super> = {2**6}"),
    ("L2", "A jacket costs $80. It is discounted 15%, then 13% HST is added to the sale price. Find the final price.",
     f"Sale 80×0.85 = $68.00; +13% → 68×1.13 = ${68*1.13:.2f}"),
    ("L2", "Between which two consecutive whole numbers does √55 lie? Justify with two perfect squares.",
     f"7 and 8, since 7<super>2</super>=49 < 55 < 64=8<super>2</super>"),
    ("L2", "A recipe uses flour to sugar in the ratio 5 : 2. If 15 cups of flour are used, how much sugar is needed?",
     f"15 ÷ 5 × 2 = {15//5*2} cups"),
    ("L3", "A car travels 240 km in 3 hours, then 150 km in 2.5 hours. Find the average speed for the whole trip. Explain why it is not the average of the two speeds.",
     f"(240+150)/(3+2.5) = 390/5.5 = {390/5.5:.1f} km/h. It weights by distance/time, not a simple mean of 80 and 60."),
    ("L3", "Sam simplified 3<super>2</super> + 3<super>2</super> as 3<super>4</super>. Explain the error and give the correct value.",
     "Error: exponents are only added when MULTIPLYING like bases. Here it is addition: 9 + 9 = 18, not 81."),
    ("L3", "A number increased by 25% gives 90. Work backwards to find the original number, and check your answer.",
     f"x×1.25 = 90 → x = 90/1.25 = {int(90/1.25)}. Check: 72×1.25 = 90 ✓"),
]

# ── worked ("I do") + partial ("we do") per sub-topic ────────────────────────
SUBTOPICS = [
    ("Integers",
     ["Evaluate (-7) - (-2) + (-4).",
      "Rewrite subtraction as adding the opposite: (-7) + (+2) + (-4).",
      "Combine: (-7 + 2) = -5, then (-5) + (-4) = -9.",
      "Answer: -9."],
     ["We do — Evaluate (-9) + (+5) - (-6).",
      "Rewrite: (-9) + (+5) + (____).",
      "Combine step by step:  -9 + 5 = ____ , then ____ + 6 = ____.",
      "Answer: ____."]),
    ("Order of Operations (BEDMAS)",
     ["Evaluate 20 - 2 × (3 + 1)<super>2</super>.",
      "Brackets first: (3 + 1) = 4.  Exponent: 4<super>2</super> = 16.",
      "Multiply: 2 × 16 = 32.   Subtract: 20 - 32 = -12.",
      "Answer: -12."],
     ["We do — Evaluate 6 + 12 ÷ (5 - 2)<super>2</super>.",
      "Brackets: (5 - 2) = ____ .  Exponent: ____<super>2</super> = ____ .",
      "Divide: 12 ÷ ____ = ____ .   Add: 6 + ____ = ____ .",
      "Answer: ____."]),
    ("Exponent Rules",
     ["Simplify (x<super>4</super> × x<super>3</super>) ÷ x<super>2</super>, x ≠ 0.",
      "Product rule (add): x<super>4+3</super> = x<super>7</super>.",
      "Quotient rule (subtract): x<super>7-2</super> = x<super>5</super>.",
      "Answer: x<super>5</super>."],
     ["We do — Simplify (a<super>2</super>)<super>3</super> × a<super>0</super>, a ≠ 0.",
      "Power of a power (multiply): a<super>2×3</super> = a<super>____</super>.",
      "Zero exponent: a<super>0</super> = ____ .",
      "Combine: a<super>____</super> × ____ = a<super>____</super>."]),
    ("Fractions — Four Operations",
     ["Evaluate 3/4 ÷ 2/3 + 1/2.",
      "Divide: multiply by the reciprocal → 3/4 × 3/2 = 9/8.",
      "Common denominator with 1/2 = 4/8:  9/8 + 4/8 = 13/8.",
      "Answer: 13/8 (or 1 5/8)."],
     ["We do — Evaluate 5/6 - 1/4 × 2/3.",
      "Multiplication before subtraction: 1/4 × 2/3 = ____ .",
      "Common denominator for 5/6 and that product: LCD = ____ .",
      "Subtract: ____ - ____ = ____ ."]),
    ("Rational Numbers",
     ["Order these from least to greatest: -0.6, -2/3, 0.5, -1/2.",
      "Write all as decimals: -2/3 ≈ -0.667, -1/2 = -0.5.",
      "Compare: -0.667 < -0.6 < -0.5 < 0.5.",
      "Answer: -2/3, -0.6, -1/2, 0.5."],
     ["We do — Order from least to greatest: -3/4, -0.7, 1/4, -1.",
      "As decimals: -3/4 = ____ , 1/4 = ____ .",
      "Place on a number line and compare the negatives first.",
      "Answer: ____ , ____ , ____ , ____ ."]),
    ("Square Roots & Irrationals",
     ["Is √50 rational or irrational? Estimate it to one decimal place.",
      "50 is not a perfect square, so √50 is irrational.",
      "49 = 7<super>2</super> and 64 = 8<super>2</super>, so √50 is just above 7.",
      "Estimate: √50 ≈ 7.1."],
     ["We do — Is √0.16 rational? Find its exact value.",
      "0.16 = 16/100, and √(16/100) = ____ / ____ .",
      "Simplify: ____ = ____ (a terminating decimal).",
      "So √0.16 is ____ (rational / irrational)."]),
    ("Fractions ↔ Decimals ↔ Percent",
     ["Convert 7/8 to a decimal and a percent.",
      "Divide: 7 ÷ 8 = 0.875.",
      "Percent: 0.875 × 100 = 87.5%.",
      "Answer: 0.875 = 87.5%."],
     ["We do — Convert 3/20 to a decimal and a percent.",
      "Make the denominator 100:  3/20 = ____/100.",
      "Decimal: ____ .   Percent: ____ %.",
      "Answer: 3/20 = ____ = ____ %."]),
    ("Applying Percents",
     ["A $120 game is on sale for 20% off. Find the sale price.",
      "Discount = 20% of 120 = 0.20 × 120 = $24.",
      "Sale price = 120 - 24 = $96  (or 120 × 0.80 = $96).",
      "Answer: $96."],
     ["We do — A $250 tablet has 13% HST added. Find the total cost.",
      "Tax = 13% of 250 = 0.13 × 250 = $____ .",
      "Total = 250 + ____ = $____  (or 250 × 1.13 = $____).",
      "Answer: $____."]),
    ("Ratios, Rates & Proportions",
     ["500 g of cereal costs $3.20. Find the unit rate in $/100 g.",
      "Per gram: 3.20 ÷ 500 = $0.0064/g.",
      "Per 100 g: 0.0064 × 100 = $0.64/100 g.",
      "Answer: $0.64 per 100 g."],
     ["We do — 3 notebooks cost $7.50. Find the cost of 7 notebooks.",
      "Unit rate: 7.50 ÷ 3 = $____ each.",
      "For 7: ____ × 7 = $____ .",
      "Answer: $____."]),
]


def build():
    d = CMFlow(OUT, topic_title=TOPIC, subtitle=SUBTITLE, info_line=INFO, name_date=True)
    d.start()
    d.learning_goal("Use integers, exponent laws, fractions, roots, percents and ratios to solve multi-step problems.")

    # Warm-up (3 quick L1)
    d.heading("Warm-up  (do these first — recall)")
    d.body("Answer quickly to activate prior skills. Answers are on the last page.", ST_BODY, gap=8)
    d.question(1, "Evaluate (-4) + (-9).", answer="short")
    d.question(2, "Write 2 × 2 × 2 × 2 as a single power, then find its value.", answer="short")
    d.question(3, "Reduce the fraction 12/18 to lowest terms.", answer="short")

    # Worked + partial per sub-topic
    d.heading("Worked Examples & Guided Steps")
    d.body("For each skill: study the worked <b>Example</b> ('I do'), then complete the "
           "<b>We do</b> steps together, filling every blank.", ST_BODY, gap=10)
    for name, i_do, we_do in SUBTOPICS:
        d.heading(name, color=d_med())
        d.example_box(i_do)
        d.body(" <br/>".join(we_do), ST_BODY, gap=14)

    # Guided practice
    d.heading("Guided Practice")
    d.body("Show all steps. Level is shown in brackets: L1 fluency, L2 application, L3 thinking.", ST_BODY, gap=10)
    for i, (lvl, stem, _ans) in enumerate(GUIDED, start=1):
        tagged = f"{stem}  <font color='#2D7DD2'><b>[{lvl}]</b></font>"
        ans_mode = "work" if lvl in ("L2", "L3") else "short"
        wp = 70 if lvl == "L3" else (55 if lvl == "L2" else None)
        d.question(i, tagged, answer=ans_mode, work_pts=wp)

    # Answer page (separate — forced new page)
    d._new_page()
    d.c.setFillColor(d_blue()); d.c.setFont("DejaVuSans-Bold", 16)
    d.c.drawCentredString(306, d.y, "Guided Practice — Answers")
    d.y -= 30
    d.body("Warm-up: 1) -13   2) 2<super>4</super> = 16   3) 2/3", ST_BODY, gap=12)
    for i, (lvl, stem, ans) in enumerate(GUIDED, start=1):
        d.key_entry(i, [f"({lvl}) {ans}"])

    path = d.build()
    return path, len(GUIDED)


def d_blue():
    from cm_pdf import CM_BLUE; return CM_BLUE
def d_med():
    from cm_pdf import CM_MED_BLUE; return CM_MED_BLUE


if __name__ == "__main__":
    p, n = build()
    print(f"engine {__version__}  built {p}  guided={n}")
