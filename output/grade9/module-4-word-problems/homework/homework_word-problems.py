#!/usr/bin/env python3
"""Concept Mastery — Grade 9 (MTH1W) Word Problems & Applications — HOMEWORK + KEY.

6 questions per level (L1/L2/L3 = 18), distinct concepts, open working space
under each question (no ruled lines). Curriculum: MTH1W. Full worked key.
Run: python3 homework_word-problems.py
"""
import os, sys
ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "_assets"))
sys.path.insert(0, ASSETS)
from cm_pdf import CMFlow, ST_BODY, CM_BLUE, __version__

DIR = os.path.dirname(__file__)
OUT_Q = os.path.join(DIR, "homework_word-problems.pdf")
OUT_A = os.path.join(DIR, "homework_word-problems_answers.pdf")
TOPIC = "Word Problems & Applications"
SUBTITLE = "Translating · Number · Money · Mixture · Distance–Rate–Time · Percent · Geometry"

ITEMS = [
    # ── L1 (6) ──
    ("L1", "Translate", "Write an expression for 'seven less than a number n'.", ["n - 7."]),
    ("L1", "Number", "The sum of a number and 15 is 40. Find the number.",
     ["n + 15 = 40, so n = 25."]),
    ("L1", "Money", "Pencils cost $3 each. How many can be bought with $27?",
     ["3p = 27, so p = 9 pencils."]),
    ("L1", "Percent", "Find 10% of $250.", ["0.10 × 250 = $25."]),
    ("L1", "Distance", "A bus travels at 50 km/h for 4 hours. How far does it go?",
     ["d = 50 × 4 = 200 km."]),
    ("L1", "Geometry", "A square has perimeter 48 cm. Find one side length.",
     ["4s = 48, so s = 12 cm."]),
    # ── L2 (6) ──
    ("L2", "Translate & solve", "Three times a number, decreased by 8, is 25. Find the number.",
     ["3n - 8 = 25 → 3n = 33 → n = 11."]),
    ("L2", "Consecutive integers", "The sum of two consecutive integers is 55. Find them.",
     ["n + (n+1) = 55 → 2n + 1 = 55 → n = 27.", "The integers are 27 and 28."]),
    ("L2", "Wages", "A plumber charges a $60 call-out fee plus $45 per hour. A bill was $240. How many hours of work?",
     ["60 + 45h = 240 → 45h = 180 → h = 4 hours."]),
    ("L2", "Mixture", "How many litres of pure water must be added to 2 L of 60% juice to make it 40% juice?",
     ["Juice stays 0.60 × 2 = 1.2 L.", "1.2 = 0.40(2 + w) → 1.2 = 0.8 + 0.4w → w = 1 L."]),
    ("L2", "Percent (work back)", "After 20% off, a coat costs $72. What was the original price?",
     ["0.80p = 72 → p = $90."]),
    ("L2", "Angles", "Two angles are supplementary (sum to 180°). One is 40° more than the other. Find both.",
     ["x + (x + 40) = 180 → 2x = 140 → x = 70.", "The angles are 70° and 110°."]),
    # ── L3 (6) ──
    ("L3", "Equation, both sides", "Five times a number minus 3 equals twice the number plus 12. Find the number.",
     ["5n - 3 = 2n + 12 → 3n = 15 → n = 5."]),
    ("L3", "Consecutive even", "The sum of three consecutive even integers is 78. Find the largest.",
     ["n + (n+2) + (n+4) = 78 → 3n + 6 = 78 → n = 24.", "Integers 24, 26, 28; the largest is 28."]),
    ("L3", "Coins", "A jar holds nickels and dimes: 20 coins worth $1.65 in total. How many of each?",
     ["Let n = nickels: 0.05n + 0.10(20 - n) = 1.65 → -0.05n + 2 = 1.65 → n = 7.",
      "So 7 nickels and 13 dimes."]),
    ("L3", "Blend cost", "Tea worth $5/kg is mixed with tea worth $9/kg to make 12 kg of blend worth $6/kg. How many kg of each?",
     ["Let x = kg of $5 tea: 5x + 9(12 - x) = 6(12) = 72 → -4x + 108 = 72 → x = 9.",
      "So 9 kg of $5 tea and 3 kg of $9 tea."]),
    ("L3", "Closing distance", "Two trains leave the same station in opposite directions at 80 km/h and 100 km/h. After how many hours are they 540 km apart?",
     ["Combined rate 180 km/h; 180t = 540 → t = 3 hours."]),
    ("L3", "Dimensions", "A rectangle's length is 4 cm more than twice its width. Its perimeter is 56 cm. Find the dimensions.",
     ["Let w = width, length = 2w + 4: 2(w + 2w + 4) = 56 → 6w + 8 = 56 → w = 8.",
      "Width 8 cm, length 20 cm."]),
]


def build_questions():
    d = CMFlow(OUT_Q, topic_title=TOPIC, subtitle=SUBTITLE,
               info_line="MTH1W · Homework — Independent Practice", name_date=True)
    d.start()
    d.learning_goal("Set up and solve word problems independently across all seven problem types.")
    d.body("Show your full working in the space provided under each question — begin with a 'let' "
           "statement and an equation. Levels: L1 fluency, L2 application, L3 thinking. Full worked "
           "solutions are in the Answer Key.", ST_BODY, gap=12)
    last = None
    for i, (lvl, concept, stem, _s) in enumerate(ITEMS, start=1):
        if lvl != last:
            names = {"L1": "Level 1 — Fluency", "L2": "Level 2 — Application", "L3": "Level 3 — Thinking"}
            d.heading(names[lvl], color=CM_BLUE); last = lvl
        wp = {"L1": 70, "L2": 100, "L3": 135}[lvl]
        d.question(i, f"{stem}  <font color='#2D7DD2'><b>[{concept}]</b></font>", answer="work", work_pts=wp)
    return d.build()


def build_answers():
    d = CMFlow(OUT_A, topic_title=TOPIC, subtitle="Answer Key — Worked Solutions",
               info_line="MTH1W · Homework — Answer Key")
    d.start()
    d.body("Worked solutions with method lines. Curriculum: MTH1W (Grade 9 de-streamed math).", ST_BODY, gap=12)
    for i, (lvl, concept, stem, sol) in enumerate(ITEMS, start=1):
        d.key_entry(i, [f"<b>[{lvl} · {concept}]</b> " + sol[0]] + sol[1:])
    return d.build()


if __name__ == "__main__":
    p = build_questions(); a = build_answers()
    from collections import Counter
    print(f"engine {__version__}  built {p} and {a}")
    print(f"items={len(ITEMS)}  by-level {dict(Counter(x[0] for x in ITEMS))}")
