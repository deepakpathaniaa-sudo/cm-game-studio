#!/usr/bin/env python3
"""Concept Mastery — Grade 9 (MTH1W) Word Problems & Applications — CLASS COPY.

Template matches approved Module 2: warm-up, then per sub-topic one worked
Example + 3-4 questions of rising complexity, generous open work space (no
ruled lines). Curriculum tag: MTH1W. Answers on final page.
Run: python3 class_word-problems.py
"""
import os, sys
ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "_assets"))
sys.path.insert(0, ASSETS)
from cm_pdf import CMFlow, ST_BODY, CM_BLUE, CM_MED_BLUE, __version__

OUT = os.path.join(os.path.dirname(__file__), "class_word-problems.pdf")
TOPIC = "Word Problems & Applications"
SUBTITLE = "Translating · Number · Money · Mixture · Distance–Rate–Time · Percent · Geometry"
INFO = "MTH1W · Class — Guided Practice"

SUBTOPICS = [
    ("Translating Words into Equations",
     ["Write an equation: 'When 6 is added to three times a number, the result is 27.' Then solve.",
      "Let the number be n:  3n + 6 = 27.  Subtract 6:  3n = 21.",
      "Divide by 3:  n = 7.   Answer: the number is 7."],
     [("L1", "Write an expression for 'five more than a number x'.", "x + 5"),
      ("L1", "Write an equation for 'a number decreased by 4 equals 10', then solve.",
       "n - 4 = 10, so n = 14."),
      ("L2", "Twice a number, increased by 9, is 31. Find the number.",
       "2n + 9 = 31 → 2n = 22 → n = 11."),
      ("L3", "When a number is multiplied by 4 and then 7 is subtracted, the result equals 3 times the number plus 2. Find the number.",
       "4n - 7 = 3n + 2 → n = 9.  (Check: 4(9)-7 = 29 = 3(9)+2.)")]),
    ("Number Problems (Consecutive Integers, 'Think of a Number')",
     ["The sum of three consecutive integers is 48. Find them.",
      "Let the integers be n, n+1, n+2:  n + (n+1) + (n+2) = 48.",
      "3n + 3 = 48 → 3n = 45 → n = 15.   Answer: 15, 16, 17."],
     [("L1", "Two consecutive integers have a sum of 27. Find them.",
       "n + (n+1) = 27 → 2n + 1 = 27 → n = 13; integers 13 and 14."),
      ("L2", "The sum of three consecutive even integers is 90. Find them.",
       "n + (n+2) + (n+4) = 90 → 3n + 6 = 90 → n = 28; integers 28, 30, 32."),
      ("L2", "I think of a number, double it, and add 5. The result is 41. What was my number?",
       "2n + 5 = 41 → 2n = 36 → n = 18."),
      ("L3", "The sum of three consecutive odd integers is 111. What is the largest?",
       "3n + 6 = 111 → n = 35; integers 35, 37, 39; largest is 39.")]),
    ("Money Problems (Coins, Prices, Wages)",
     ["A part-time job pays a $20 flat fee plus $14 per hour. How many hours give $104?",
      "Let h be the hours:  14h + 20 = 104.  Subtract 20:  14h = 84.",
      "Divide by 14:  h = 6.   Answer: 6 hours."],
     [("L1", "Tickets cost $8 each. How many tickets can be bought with $56?",
       "8t = 56 → t = 7 tickets."),
      ("L2", "A phone plan charges $25 per month plus $0.10 per text. One month's bill was $32. How many texts were sent?",
       "25 + 0.10t = 32 → 0.10t = 7 → t = 70 texts."),
      ("L2", "Maria has $2.35 in dimes and quarters, 13 coins in total. How many of each? (Let d = dimes.)",
       "0.10d + 0.25(13 - d) = 2.35 → -0.15d = -0.90 → d = 6; so 6 dimes and 7 quarters."),
      ("L3", "A worker earns $18/h for regular hours and $27/h for overtime. In one week she worked 40 regular hours plus some overtime and earned $963. How many overtime hours?",
       "40(18) + 27x = 963 → 720 + 27x = 963 → 27x = 243 → x = 9 overtime hours.")]),
    ("Mixture Problems (Concentration / Blends)",
     ["A store blends coffee worth $8/kg with coffee worth $12/kg to make 10 kg of blend worth $9.20/kg. How many kg of each?",
      "Let x = kg of the $8 coffee, so (10 - x) = kg of the $12 coffee.",
      "8x + 12(10 - x) = 9.20(10) → 8x + 120 - 12x = 92 → -4x = -28 → x = 7.",
      "Answer: 7 kg of the $8 coffee and 3 kg of the $12 coffee."],
     [("L1", "A 500 mL drink is 20% juice. How many millilitres of juice does it contain?",
       "0.20 × 500 = 100 mL."),
      ("L2", "How many litres of pure water must be added to 3 L of 40% saltwater to dilute it to 30% salt?",
       "Salt stays 0.40(3) = 1.2 L. 1.2 = 0.30(3 + w) → 1.2 = 0.9 + 0.3w → w = 1 L."),
      ("L2", "Nuts worth $6/kg are mixed with nuts worth $10/kg to make 8 kg of mix worth $7.50/kg. How many kg of the $6 nuts?",
       "6x + 10(8 - x) = 7.50(8) → -4x + 80 = 60 → x = 5 kg of the $6 nuts."),
      ("L3", "A chemist has 40 mL of 25% acid solution. How many millilitres of pure (100%) acid must be added to make a 40% acid solution?",
       "(10 + a)/(40 + a) = 0.40 → 10 + a = 16 + 0.4a → 0.6a = 6 → a = 10 mL.")]),
    ("Distance–Rate–Time",
     ["A train travels 240 km in 3 hours at constant speed. Find its speed, then the distance it covers in 5 hours at that speed.",
      "Speed = distance ÷ time = 240 ÷ 3 = 80 km/h.",
      "Distance in 5 h = 80 × 5 = 400 km."],
     [("L1", "A car travels at 60 km/h for 2 hours. How far does it go?",
       "d = 60 × 2 = 120 km."),
      ("L2", "A runner covers 21 km in 1.75 hours. Find the average speed in km/h.",
       "21 ÷ 1.75 = 12 km/h."),
      ("L2", "A plane flies 1500 km at 500 km/h. How many hours does the flight take?",
       "t = 1500 ÷ 500 = 3 hours."),
      ("L3", "Two cars leave the same point in opposite directions at 70 km/h and 90 km/h. After how many hours are they 480 km apart?",
       "Combined rate 160 km/h; 160t = 480 → t = 3 hours.")]),
    ("Percent Problems (Discount, Tax, Increase/Decrease, Work Backwards)",
     ["A jacket is marked $80. It is discounted 25%, then 13% tax is added. Find the final price.",
      "Discount: 80 × 0.25 = 20, so the sale price is 60.",
      "Tax: 60 × 0.13 = 7.80, so the final price is 60 + 7.80 = $67.80."],
     [("L1", "Find 15% of $60.", "0.15 × 60 = $9."),
      ("L2", "A $45 item is on sale for 20% off. What is the sale price?",
       "45 - 0.20(45) = 45 - 9 = $36."),
      ("L2", "After a 13% tax is added, a meal costs $56.50. What was the price before tax?",
       "1.13p = 56.50 → p = $50.00."),
      ("L3", "A population increased by 20% to reach 3600. What was the original population?",
       "1.20p = 3600 → p = 3000.")]),
    ("Geometry Word Problems (Perimeter / Area / Angles as Equations)",
     ["The length of a rectangle is 5 cm more than its width. The perimeter is 46 cm. Find the dimensions.",
      "Let w = width, so length = w + 5.  P = 2(w + w + 5) = 46.",
      "2(2w + 5) = 46 → 4w + 10 = 46 → 4w = 36 → w = 9.",
      "Answer: width 9 cm, length 14 cm."],
     [("L1", "A square has perimeter 36 cm. Find the length of one side.",
       "4s = 36 → s = 9 cm."),
      ("L2", "Two angles are complementary (sum to 90°). One is twice the other. Find both angles.",
       "x + 2x = 90 → 3x = 90 → x = 30; angles 30° and 60°."),
      ("L2", "A rectangle is 3 times as long as it is wide. Its perimeter is 64 m. Find its dimensions.",
       "2(w + 3w) = 64 → 8w = 64 → w = 8; width 8 m, length 24 m."),
      ("L3", "The angles of a triangle are in the ratio 1:2:3. Find each angle.",
       "x + 2x + 3x = 180 → 6x = 180 → x = 30; angles 30°, 60°, 90°.")]),
]

WARMUP = [
    ("Write an expression for 'a number n increased by 7'.", "n + 7"),
    ("Write an expression for 'twice a number, decreased by 5'.", "2n - 5"),
    ("The sum of a number and 12 is 20. Write the equation.", "n + 12 = 20"),
]


def build():
    d = CMFlow(OUT, topic_title=TOPIC, subtitle=SUBTITLE, info_line=INFO, name_date=True)
    d.start()
    d.learning_goal("Translate real-world situations into equations and solve number, money, mixture, "
                    "distance, percent and geometry problems.")
    d.heading("Warm-up  (quick recall)")
    for i, (stem, _a) in enumerate(WARMUP, start=1):
        d.question(i, stem, answer="work", work_pts=30)
    d.heading("Examples & Practice")
    d.body("For each problem type, study the worked <b>Example</b>, then solve the questions that follow. "
           "Difficulty rises within each set (L1 → L3). Show your setup (let statement + equation). "
           "Answers are on the last page.", ST_BODY, gap=10)
    n = len(WARMUP); answers = []
    for name, example, qs in SUBTOPICS:
        d.heading(name, color=CM_MED_BLUE)
        d.example_box(example)
        for lvl, stem, ans in qs:
            n += 1
            tagged = f"{stem}  <font color='#2D7DD2'><b>[{lvl}]</b></font>"
            wp = {"L1": 60, "L2": 95, "L3": 130}[lvl]
            d.question(n, tagged, answer="work", work_pts=wp)
            answers.append((n, lvl, ans))
    d._new_page()
    d.c.setFillColor(CM_BLUE); d.c.setFont("DejaVuSans-Bold", 16)
    d.c.drawCentredString(306, d.y, "Answers"); d.y -= 28
    wu = "   ".join(f"W{i}) {a}" for i, (_s, a) in enumerate(WARMUP, start=1))
    d.body("<b>Warm-up:</b> " + wu, ST_BODY, gap=12)
    for num, lvl, ans in answers:
        d.key_entry(num, [f"({lvl}) {ans}"])
    return d.build(), len(answers)


if __name__ == "__main__":
    p, n = build()
    print(f"engine {__version__}  built {p}  practice_questions={n}")
