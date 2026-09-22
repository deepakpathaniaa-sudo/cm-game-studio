#!/usr/bin/env python3
"""Concept Mastery — Grade 9 (MTH1W) Measurement — CLASS COPY.

Template matches approved Module 2: warm-up, then per sub-topic one worked
Example + 3-4 questions of rising complexity, generous open work space (no
ruled lines). Curriculum tag: MTH1W. Answers on final page.
All figures are DESCRIBED IN WORDS (no diagrams). π ≈ 3.14 throughout; values
involving π are rounded to 1 decimal place. Every numeric answer is COMPUTED in
Python and formatted into the answer string so the key cannot drift.
Run: python3 class_measurement.py
"""
import os, sys
ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "_assets"))
sys.path.insert(0, ASSETS)
from cm_pdf import CMFlow, ST_BODY, CM_BLUE, CM_MED_BLUE, __version__

OUT = os.path.join(os.path.dirname(__file__), "class_measurement.pdf")
TOPIC = "Measurement"
SUBTITLE = "Perimeter & Area · Composite Figures · Surface Area · Volume · Pyramids, Cones & Spheres · Optimization"
INFO = "MTH1W · Class — Guided Practice"
PI = 3.14

SUBTOPICS = [
    ("Perimeter & Area of Basic Figures",
     ["A rectangle is 8 cm long and 5 cm wide. Find its perimeter and area.",
      "Perimeter P = 2(l + w) = 2(8 + 5) = 26 cm.",
      "Area A = l × w = 8 × 5 = 40 cm<super>2</super>.   Answer: P = 26 cm, A = 40 cm<super>2</super>."],
     [("L1", "A square has side length 7 cm. Find its perimeter and area.",
       f"P = 4×7 = {4*7} cm; A = 7<super>2</super> = {7*7} cm<super>2</super>."),
      ("L1", "A triangle has base 10 cm and height 6 cm. Find its area.",
       f"A = ½ × base × height = ½ × 10 × 6 = {10*6//2} cm<super>2</super>."),
      ("L2", "A trapezoid has parallel sides 9 cm and 5 cm and a height of 4 cm. Find its area.",
       f"A = ½(a + b)h = ½(9 + 5)(4) = {(9+5)*4//2} cm<super>2</super>."),
      ("L3", "A circle has radius 5 cm. Using π ≈ 3.14, find its circumference and area (1 d.p.).",
       f"C = 2×3.14×5 = {2*PI*5:.1f} cm; A = 3.14×5<super>2</super> = {PI*25:.1f} cm<super>2</super>.")]),
    ("Area of Composite Figures",
     ["A rectangle 10 cm by 6 cm has a semicircle of diameter 6 cm on one short end. Find the total area (π ≈ 3.14, 1 d.p.).",
      "Rectangle: 10 × 6 = 60 cm<super>2</super>. Semicircle radius = 3 cm: ½ × 3.14 × 3<super>2</super> = 14.1 cm<super>2</super>.",
      f"Total = 60 + 14.1 = {60 + 0.5*PI*9:.1f} cm<super>2</super>."],
     [("L1", "A figure is two rectangles joined along a 4 cm edge: one 5 cm by 4 cm and one 3 cm by 4 cm. Find the total area.",
       f"5×4 + 3×4 = 20 + 12 = {5*4 + 3*4} cm<super>2</super>."),
      ("L2", "An L-shape is a 10 cm by 8 cm rectangle with a 4 cm by 3 cm rectangular corner removed. Find its area.",
       f"10×8 − 4×3 = 80 − 12 = {10*8 - 4*3} cm<super>2</super>."),
      ("L2", "A square of side 8 cm has a quarter-circle of radius 8 cm removed from one corner. Find the remaining area (π ≈ 3.14, 1 d.p.).",
       f"64 − ¼×3.14×8<super>2</super> = 64 − 50.2 = {64 - 0.25*PI*64:.1f} cm<super>2</super>."),
      ("L3", "A track shape is a 20 cm by 10 cm rectangle with a semicircle of diameter 10 cm on each short end. Find the total area (π ≈ 3.14, 1 d.p.).",
       f"Rectangle 20×10 = 200; two semicircles = one circle r = 5: 3.14×5<super>2</super> = 78.5. Total = {200 + PI*25:.1f} cm<super>2</super>.")]),
    ("Surface Area of Prisms & Cylinders",
     ["A rectangular prism is 6 cm by 4 cm by 3 cm. Find its surface area.",
      "SA = 2(lw + lh + wh) = 2(6×4 + 6×3 + 4×3) = 2(24 + 18 + 12).",
      f"= 2(54) = {2*(24+18+12)} cm<super>2</super>."],
     [("L1", "A cube has edge length 5 cm. Find its surface area.",
       f"SA = 6×edge<super>2</super> = 6×5<super>2</super> = {6*25} cm<super>2</super>."),
      ("L2", "A cylinder has radius 3 cm and height 10 cm. Find its surface area (SA = 2πr<super>2</super> + 2πrh; π ≈ 3.14, 1 d.p.).",
       f"2×3.14×3<super>2</super> + 2×3.14×3×10 = 56.5 + 188.4 = {2*PI*9 + 2*PI*3*10:.1f} cm<super>2</super>."),
      ("L2", "A triangular prism is 12 cm long. Its triangular faces have base 6 cm and height 4 cm (equal sides 5 cm). Find the total surface area.",
       f"Triangles: 2×(½×6×4) = 24; rectangles: (6+5+5)×12 = 192; SA = {2*(6*4//2) + (6+5+5)*12} cm<super>2</super>."),
      ("L3", "A closed cylinder has diameter 8 cm and height 15 cm. Find its surface area (π ≈ 3.14, 1 d.p.).",
       f"r = 4: 2×3.14×4<super>2</super> + 2×3.14×4×15 = 100.5 + 376.8 = {2*PI*16 + 2*PI*4*15:.1f} cm<super>2</super>.")]),
    ("Volume of Prisms & Cylinders",
     ["A rectangular prism is 7 cm by 4 cm by 5 cm. Find its volume.",
      "V = length × width × height = 7 × 4 × 5.",
      f"= {7*4*5} cm<super>3</super>."],
     [("L1", "A cube has edge length 6 cm. Find its volume.",
       f"V = edge<super>3</super> = 6<super>3</super> = {6**3} cm<super>3</super>."),
      ("L1", "A cylinder has radius 5 cm and height 12 cm. Find its volume (V = πr<super>2</super>h; π ≈ 3.14, 1 d.p.).",
       f"V = 3.14×5<super>2</super>×12 = {PI*25*12:.1f} cm<super>3</super>."),
      ("L2", "A triangular prism has a triangular base of area 15 cm<super>2</super> and length 9 cm. Find its volume.",
       f"V = base area × length = 15 × 9 = {15*9} cm<super>3</super>."),
      ("L3", "A cylindrical tank has diameter 10 cm and height 14 cm. Find its volume (π ≈ 3.14, 1 d.p.).",
       f"r = 5: V = 3.14×5<super>2</super>×14 = {PI*25*14:.1f} cm<super>3</super>.")]),
    ("Surface Area & Volume of Pyramids, Cones & Spheres",
     ["A cone has radius 3 cm, height 4 cm and slant height 5 cm. Find its volume and surface area (π ≈ 3.14, 1 d.p.).",
      "V = (1/3)πr<super>2</super>h = (1/3)(3.14)(9)(4) = 37.7 cm<super>3</super>.",
      f"SA = πr<super>2</super> + πrl = 3.14(9) + 3.14(3)(5) = 28.3 + 47.1 = {PI*9 + PI*3*5:.1f} cm<super>2</super>."],
     [("L1", "A sphere has radius 6 cm. Find its volume (V = (4/3)πr<super>3</super>; π ≈ 3.14, 1 d.p.).",
       f"V = (4/3)×3.14×6<super>3</super> = {(4/3)*PI*216:.1f} cm<super>3</super>."),
      ("L2", "A sphere has radius 4 cm. Find its surface area (SA = 4πr<super>2</super>; π ≈ 3.14, 1 d.p.).",
       f"SA = 4×3.14×4<super>2</super> = {4*PI*16:.1f} cm<super>2</super>."),
      ("L2", "A square-based pyramid has base edge 6 cm and height 10 cm. Find its volume (V = (1/3)×base area×height).",
       f"V = (1/3)×6<super>2</super>×10 = (1/3)×36×10 = {36*10//3} cm<super>3</super>."),
      ("L3", "A cone has radius 6 cm and slant height 10 cm. Find its surface area (π ≈ 3.14, 1 d.p.).",
       f"SA = 3.14×6<super>2</super> + 3.14×6×10 = 113.0 + 188.4 = {PI*36 + PI*6*10:.1f} cm<super>2</super>.")]),
    ("2D & 3D Optimization",
     ["You have 40 m of fencing to enclose a rectangular garden. What dimensions give the maximum area?",
      "For a fixed perimeter, a rectangle has maximum area when it is a square.",
      "Side = 40 ÷ 4 = 10 m, so 10 m × 10 m gives the maximum area of 100 m<super>2</super>."],
     [("L1", "For a fixed perimeter, which rectangle encloses the greatest area?",
       "A square (all four sides equal)."),
      ("L2", "A rectangular pen is built with 24 m of fencing to enclose the maximum area. Find its dimensions and that area.",
       f"Square: side = 24÷4 = 6 m; area = 6×6 = {6*6} m<super>2</super>."),
      ("L2", "For a fixed volume, which rectangular box uses the least material (smallest surface area)?",
       "A cube (all edges equal)."),
      ("L3", "A closed box must hold 1000 cm<super>3</super>. What shape minimizes the surface area, and what are its dimensions?",
       "A cube; edge = ∛1000 = 10 cm, so 10 cm × 10 cm × 10 cm.")]),
]

WARMUP = [
    ("Find the area of a rectangle 6 cm long and 3 cm wide.", "18 cm<super>2</super>"),
    ("Find the perimeter of a square with side 5 cm.", "20 cm"),
    ("State the formula for the area of a triangle.", "A = ½ × base × height"),
]


def build():
    d = CMFlow(OUT, topic_title=TOPIC, subtitle=SUBTITLE, info_line=INFO, name_date=True)
    d.start()
    d.learning_goal("Find perimeter, area, surface area and volume of 2-D and 3-D figures, and reason about optimization.")
    d.body("Throughout this module use <b>π ≈ 3.14</b>. Round answers involving π to <b>1 decimal place (1 d.p.)</b>. "
           "Every figure is described in words — read the dimensions carefully.", ST_BODY, gap=10)
    d.heading("Warm-up  (quick recall)")
    for i, (stem, _a) in enumerate(WARMUP, start=1):
        d.question(i, stem, answer="work", work_pts=30)
    d.heading("Examples & Practice")
    d.body("For each skill, study the worked <b>Example</b>, then solve the questions that follow. "
           "Difficulty rises within each set (L1 → L3). Answers are on the last page.", ST_BODY, gap=10)
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
