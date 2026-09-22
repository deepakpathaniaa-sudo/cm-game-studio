#!/usr/bin/env python3
"""Concept Mastery — Grade 9 (MTH1W) Measurement — HOMEWORK + KEY.

6 questions per level (L1/L2/L3 = 18), distinct concepts, open working space
under each question (no ruled lines). Curriculum: MTH1W. Full worked key.
All figures DESCRIBED IN WORDS (no diagrams). π ≈ 3.14; π-values to 1 d.p.
Every numeric answer is COMPUTED in Python and formatted into the solution.
Run: python3 homework_measurement.py
"""
import os, sys
ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "_assets"))
sys.path.insert(0, ASSETS)
from cm_pdf import CMFlow, ST_BODY, CM_BLUE, __version__

DIR = os.path.dirname(__file__)
OUT_Q = os.path.join(DIR, "homework_measurement.pdf")
OUT_A = os.path.join(DIR, "homework_measurement_answers.pdf")
TOPIC = "Measurement"
SUBTITLE = "Perimeter & Area · Composite Figures · Surface Area · Volume · Pyramids, Cones & Spheres · Optimization"
PI = 3.14

ITEMS = [
    # ── L1 (6) ──
    ("L1", "Rectangle area", "Find the area of a rectangle 9 cm long and 4 cm wide.",
     [f"A = l × w = 9 × 4 = {9*4} cm<super>2</super>."]),
    ("L1", "Square perimeter", "Find the perimeter of a square with side length 8 cm.",
     [f"P = 4 × side = 4 × 8 = {4*8} cm."]),
    ("L1", "Triangle area", "Find the area of a triangle with base 12 cm and height 5 cm.",
     [f"A = ½ × base × height = ½ × 12 × 5 = {12*5//2} cm<super>2</super>."]),
    ("L1", "Circle circumference", "A circle has radius 7 cm. Find its circumference (π ≈ 3.14, 1 d.p.).",
     [f"C = 2πr = 2 × 3.14 × 7 = {2*PI*7:.1f} cm."]),
    ("L1", "Cube volume", "Find the volume of a cube with edge length 4 cm.",
     [f"V = edge<super>3</super> = 4<super>3</super> = {4**3} cm<super>3</super>."]),
    ("L1", "Cylinder volume", "A cylinder has radius 2 cm and height 9 cm. Find its volume (π ≈ 3.14, 1 d.p.).",
     [f"V = πr<super>2</super>h = 3.14 × 2<super>2</super> × 9 = {PI*4*9:.1f} cm<super>3</super>."]),
    # ── L2 (6) ──
    ("L2", "Parallelogram area", "A parallelogram has base 15 cm and height 6 cm. Find its area.",
     [f"A = base × height = 15 × 6 = {15*6} cm<super>2</super>."]),
    ("L2", "Trapezoid area", "A trapezoid has parallel sides 10 cm and 6 cm and a height of 5 cm. Find its area.",
     [f"A = ½(a + b)h = ½(10 + 6)(5) = {(10+6)*5//2} cm<super>2</super>."]),
    ("L2", "Composite area", "A rectangle 12 cm by 5 cm has a semicircle of diameter 5 cm on one end. Find the total area (π ≈ 3.14, 1 d.p.).",
     ["Rectangle 12×5 = 60; semicircle r = 2.5: ½×3.14×2.5<super>2</super> = 9.8.",
      f"Total = 60 + 9.8 = {60 + 0.5*PI*2.5**2:.1f} cm<super>2</super>."]),
    ("L2", "Prism surface area", "A rectangular prism is 5 cm by 3 cm by 2 cm. Find its surface area.",
     [f"SA = 2(lw + lh + wh) = 2(15 + 10 + 6) = {2*(15+10+6)} cm<super>2</super>."]),
    ("L2", "Cylinder surface area", "A cylinder has radius 4 cm and height 8 cm. Find its surface area (π ≈ 3.14, 1 d.p.).",
     ["SA = 2πr<super>2</super> + 2πrh = 2×3.14×4<super>2</super> + 2×3.14×4×8.",
      f"= 100.5 + 200.96 = {2*PI*16 + 2*PI*4*8:.1f} cm<super>2</super>."]),
    ("L2", "Cone volume", "A cone has radius 3 cm and height 7 cm. Find its volume (π ≈ 3.14, 1 d.p.).",
     [f"V = (1/3)πr<super>2</super>h = (1/3)(3.14)(3<super>2</super>)(7) = {(1/3)*PI*9*7:.1f} cm<super>3</super>."]),
    # ── L3 (6) ──
    ("L3", "Sphere volume", "A sphere has radius 3 cm. Find its volume (π ≈ 3.14, 1 d.p.).",
     [f"V = (4/3)πr<super>3</super> = (4/3)(3.14)(3<super>3</super>) = {(4/3)*PI*27:.1f} cm<super>3</super>."]),
    ("L3", "Sphere surface area", "A sphere has radius 5 cm. Find its surface area (π ≈ 3.14, 1 d.p.).",
     [f"SA = 4πr<super>2</super> = 4 × 3.14 × 5<super>2</super> = {4*PI*25:.1f} cm<super>2</super>."]),
    ("L3", "Pyramid volume", "A square-based pyramid has base edge 8 cm and height 9 cm. Find its volume.",
     [f"V = (1/3)×base area×height = (1/3)×8<super>2</super>×9 = (1/3)×64×9 = {64*9//3} cm<super>3</super>."]),
    ("L3", "Volume with hole", "A cylinder of radius 4 cm and height 10 cm has a cylindrical hole of radius 2 cm drilled straight through it. Find the remaining volume (π ≈ 3.14, 1 d.p.).",
     ["Outer: 3.14×4<super>2</super>×10 = 502.4; hole: 3.14×2<super>2</super>×10 = 125.6.",
      f"Remaining = 502.4 − 125.6 = {PI*16*10 - PI*4*10:.1f} cm<super>3</super>."]),
    ("L3", "Cone surface area", "A cone has radius 5 cm and slant height 13 cm. Find its surface area (π ≈ 3.14, 1 d.p.).",
     ["SA = πr<super>2</super> + πrl = 3.14×5<super>2</super> + 3.14×5×13.",
      f"= 78.5 + 204.1 = {PI*25 + PI*5*13:.1f} cm<super>2</super>."]),
    ("L3", "Optimization", "A farmer has 100 m of fencing for a rectangular field and wants the maximum area. Find the dimensions and the maximum area.",
     ["For a fixed perimeter, area is greatest when the rectangle is a square.",
      f"Side = 100÷4 = 25 m; area = 25×25 = {25*25} m<super>2</super>."]),
]


def build_questions():
    d = CMFlow(OUT_Q, topic_title=TOPIC, subtitle=SUBTITLE,
               info_line="MTH1W · Homework — Independent Practice", name_date=True)
    d.start()
    d.learning_goal("Practise perimeter, area, surface area, volume and optimization independently.")
    d.body("Show your full working in the space provided under each question. Use <b>π ≈ 3.14</b> and round "
           "π-answers to <b>1 d.p.</b> Levels: L1 fluency, L2 application, L3 thinking. Worked solutions are in "
           "the Answer Key.", ST_BODY, gap=12)
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
    d.body("Worked solutions with method lines. Curriculum: MTH1W (Grade 9 de-streamed math). "
           "π ≈ 3.14; π-values rounded to 1 d.p.", ST_BODY, gap=12)
    for i, (lvl, concept, stem, sol) in enumerate(ITEMS, start=1):
        d.key_entry(i, [f"<b>[{lvl} · {concept}]</b> " + sol[0]] + sol[1:])
    return d.build()


if __name__ == "__main__":
    p = build_questions(); a = build_answers()
    from collections import Counter
    print(f"engine {__version__}  built {p} and {a}")
    print(f"items={len(ITEMS)}  by-level {dict(Counter(x[0] for x in ITEMS))}")
