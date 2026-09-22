#!/usr/bin/env python3
"""Concept Mastery — Grade 9 (MTH1W) Measurement — TEST + MARKING SCHEME.

30 questions, 60 minutes, sections K/U -> Application -> Thinking -> Communication;
last four questions very hard. Curriculum: MTH1W. Marks defined once, drive paper +
blueprint + scheme. All figures DESCRIBED IN WORDS (no diagrams). π ≈ 3.14; π-values
to 1 d.p. Every numeric answer is COMPUTED in Python and formatted into the scheme.
Run: python3 test_measurement.py
"""
import os, sys
ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "_assets"))
sys.path.insert(0, ASSETS)
from cm_pdf import (CMFlow, ST_BODY, CM_BLUE, CM_DARK_GREY, CONTENT_X, __version__)

DIR = os.path.dirname(__file__)
OUT_T = os.path.join(DIR, "test_measurement.pdf")
OUT_M = os.path.join(DIR, "test_measurement_marking_scheme.pdf")
TOPIC = "Measurement"
DURATION = "60 minutes"
PI = 3.14

# qid, section, subtopic, level, category, marks, stem, answer_mode, solution lines
ITEMS = [
    # ── Section A — Knowledge & Understanding (L1), Q1–15 ──
    ("A1","A","Rectangle Area","L1","K/U",1,"Find the area of a rectangle 7 cm by 6 cm.","short",
     [f"A = 7×6 = {7*6} cm<super>2</super>.  (A1)"]),
    ("A2","A","Rectangle Perimeter","L1","K/U",1,"Find the perimeter of a rectangle 8 cm by 3 cm.","short",
     [f"P = 2(8+3) = {2*(8+3)} cm.  (A1)"]),
    ("A3","A","Square Area","L1","K/U",1,"Find the area of a square with side 9 cm.","short",
     [f"A = 9<super>2</super> = {9*9} cm<super>2</super>.  (A1)"]),
    ("A4","A","Triangle Area","L1","K/U",1,"Find the area of a triangle with base 8 cm and height 5 cm.","short",
     [f"A = ½×8×5 = {8*5//2} cm<super>2</super>.  (A1)"]),
    ("A5","A","Cube Volume","L1","K/U",1,"Find the volume of a cube with edge 3 cm.","short",
     [f"V = 3<super>3</super> = {3**3} cm<super>3</super>.  (A1)"]),
    ("A6","A","Cylinder Formula","L1","K/U",1,"State the formula for the volume of a cylinder.","short",
     ["V = πr<super>2</super>h.  (A1)"]),
    ("A7","A","Circumference","L1","K/U",1,"A circle has radius 10 cm. Find its circumference (π ≈ 3.14, 1 d.p.).","short",
     [f"C = 2×3.14×10 = {2*PI*10:.1f} cm.  (A1)"]),
    ("A8","A","Circle Formula","L1","K/U",1,"State the formula for the area of a circle.","short",
     ["A = πr<super>2</super>.  (A1)"]),
    ("A9","A","Square Perimeter","L1","K/U",1,"Find the perimeter of a square with side 12 cm.","short",
     [f"P = 4×12 = {4*12} cm.  (A1)"]),
    ("A10","A","Parallelogram Area","L1","K/U",2,"Find the area of a parallelogram with base 11 cm and height 4 cm.","short",
     [f"A = base×height = 11×4 = {11*4} cm<super>2</super>.  (M1, A1)"]),
    ("A11","A","Trapezoid Area","L1","K/U",2,"Find the area of a trapezoid with parallel sides 8 cm and 4 cm and height 6 cm.","short",
     [f"A = ½(8+4)(6) = {(8+4)*6//2} cm<super>2</super>.  (M1, A1)"]),
    ("A12","A","Circle Area","L1","K/U",2,"A circle has radius 4 cm. Find its area (π ≈ 3.14, 1 d.p.).","short",
     [f"A = 3.14×4<super>2</super> = {PI*16:.1f} cm<super>2</super>.  (M1, A1)"]),
    ("A13","A","Prism Volume","L1","K/U",2,"Find the volume of a rectangular prism 5 cm by 4 cm by 6 cm.","short",
     [f"V = 5×4×6 = {5*4*6} cm<super>3</super>.  (M1, A1)"]),
    ("A14","A","Cube Surface Area","L1","K/U",2,"Find the surface area of a cube with edge 7 cm.","short",
     [f"SA = 6×7<super>2</super> = {6*49} cm<super>2</super>.  (M1, A1)"]),
    ("A15","A","Cylinder Volume","L1","K/U",2,"A cylinder has radius 3 cm and height 5 cm. Find its volume (π ≈ 3.14, 1 d.p.).","short",
     [f"V = 3.14×3<super>2</super>×5 = {PI*9*5:.1f} cm<super>3</super>.  (M1, A1)"]),
    # ── Section B — Application (L2), Q16–24 ──
    ("B16","B","Triangle Area","L2","Application",2,"A triangle has base 14 cm and height 9 cm. Find its area.","work",
     [f"A = ½×14×9 = {14*9//2} cm<super>2</super>.  (M1, A1)"]),
    ("B17","B","Prism Surface Area","L2","Application",2,"A rectangular prism is 8 cm by 5 cm by 4 cm. Find its surface area.","work",
     [f"SA = 2(8×5 + 8×4 + 5×4) = 2(40+32+20) = {2*(40+32+20)} cm<super>2</super>.  (M1, A1)"]),
    ("B18","B","Cylinder Volume","L2","Application",2,"A cylinder has radius 6 cm and height 10 cm. Find its volume (π ≈ 3.14, 1 d.p.).","work",
     [f"V = 3.14×6<super>2</super>×10 = {PI*36*10:.1f} cm<super>3</super>.  (M1, A1)"]),
    ("B19","B","Cone Volume","L2","Application",2,"A cone has radius 3 cm and height 8 cm. Find its volume (π ≈ 3.14, 1 d.p.).","work",
     [f"V = (1/3)(3.14)(3<super>2</super>)(8) = {(1/3)*PI*9*8:.1f} cm<super>3</super>.  (M1, A1)"]),
    ("B20","B","Sphere Surface Area","L2","Application",2,"A sphere has radius 7 cm. Find its surface area (π ≈ 3.14, 1 d.p.).","work",
     [f"SA = 4×3.14×7<super>2</super> = {4*PI*49:.1f} cm<super>2</super>.  (M1, A1)"]),
    ("B21","B","Pyramid Volume","L2","Application",2,"A square-based pyramid has base edge 5 cm and height 12 cm. Find its volume.","work",
     [f"V = (1/3)×5<super>2</super>×12 = (1/3)×25×12 = {25*12//3} cm<super>3</super>.  (M1, A1)"]),
    ("B22","B","Cylinder Surface Area","L2","Application",3,"A cylinder has diameter 8 cm and height 9 cm. Find its surface area (π ≈ 3.14, 1 d.p.).","work",
     ["r = 4: SA = 2πr<super>2</super> + 2πrh = 2×3.14×4<super>2</super> + 2×3.14×4×9.  (M1, M1)",
      f"= 100.48 + 226.08 = {2*PI*16 + 2*PI*4*9:.1f} cm<super>2</super>.  (A1)"]),
    ("B23","B","Composite Area","L2","Application",3,"A composite figure is a 14 cm by 8 cm rectangle with a semicircle of diameter 8 cm on one end. Find the total area (π ≈ 3.14, 1 d.p.).","work",
     ["Rectangle 14×8 = 112; semicircle r = 4: ½×3.14×4<super>2</super> = 25.12.  (M1, M1)",
      f"Total = 112 + 25.12 = {112 + 0.5*PI*16:.1f} cm<super>2</super>.  (A1)"]),
    ("B24","B","Sphere Volume","L2","Application",3,"A sphere has radius 5 cm. Find its volume (π ≈ 3.14, 1 d.p.).","work",
     ["V = (4/3)πr<super>3</super> = (4/3)(3.14)(5<super>3</super>) = (4/3)(3.14)(125).  (M1, M1)",
      f"= {(4/3)*PI*125:.1f} cm<super>3</super>.  (A1)"]),
    # ── Section C — Thinking (L3), Q25–29 (last three very hard) ──
    ("C25","C","Capacity","L3","Thinking",4,
     "A cylindrical water tank has radius 2 m and height 3 m. Find its volume, then how many litres it holds (1 m<super>3</super> = 1000 L). (π ≈ 3.14, 1 d.p.)","work",
     [f"V = 3.14×2<super>2</super>×3 = {PI*4*3:.1f} m<super>3</super>.  (M1, A1)",
      f"Litres = 37.68 × 1000 = {int(round(PI*4*3*1000))} L.  (M1, A1)"]),
    ("C26","C","Composite Solid","L3","Thinking",4,
     "A composite solid is a cube of edge 5 cm with a square-based pyramid (base edge 5 cm, height 9 cm) sitting on top. Find the total volume.","work",
     [f"Cube: 5<super>3</super> = 125; pyramid: (1/3)×5<super>2</super>×9 = {25*9//3}.  (M1, M1)",
      f"Total = 125 + 75 = {5**3 + 25*9//3} cm<super>3</super>.  (A1, A1)"]),
    ("C27","C","Recasting Solids","L3","Thinking",5,
     "A cylinder has radius 5 cm and height 20 cm. It is melted and recast into spheres of radius 5 cm. How many complete spheres can be made? (Very hard.) (π ≈ 3.14, 1 d.p.)","work",
     [f"Cylinder V = 3.14×5<super>2</super>×20 = {PI*25*20:.1f} cm<super>3</super>.  (M1, A1)",
      f"Sphere V = (4/3)(3.14)(5<super>3</super>) = {(4/3)*PI*125:.1f} cm<super>3</super>.  (M1)",
      f"Number = 1570 ÷ 523.3 = {round(PI*25*20/((4/3)*PI*125))} complete spheres.  (M1, A1)"]),
    ("C28","C","Slant & Surface Area","L3","Thinking",5,
     "A cone has radius 9 cm and height 12 cm. Find its slant height, then its total surface area. (Very hard.) (π ≈ 3.14, 1 d.p.)","work",
     [f"Slant l = √(9<super>2</super> + 12<super>2</super>) = √225 = {int((9**2+12**2)**0.5)} cm.  (M1, A1)",
      "SA = πr<super>2</super> + πrl = 3.14×9<super>2</super> + 3.14×9×15 = 254.34 + 423.9.  (M1)",
      f"= {PI*81 + PI*9*15:.1f} cm<super>2</super>.  (A1, A1)"]),
    ("C29","C","Silo (Cylinder + Cone)","L3","Thinking",6,
     "A grain silo is a cylinder of radius 4 m and height 9 m topped by a cone of radius 4 m and height 3 m. Find the total volume of the silo. (Very hard.) (π ≈ 3.14, 1 d.p.)","work",
     [f"Cylinder V = 3.14×4<super>2</super>×9 = {PI*16*9:.1f} m<super>3</super>.  (M1, A1)",
      f"Cone V = (1/3)(3.14)(4<super>2</super>)(3) = {(1/3)*PI*16*3:.1f} m<super>3</super>.  (M1, A1)",
      f"Total = 452.16 + 50.24 = {PI*16*9 + (1/3)*PI*16*3:.1f} m<super>3</super>.  (M1, A1)"]),
    # ── Section D — Communication (L3), Q30 (very hard justify) ──
    ("D30","D","Optimization Reasoning","L3","Communication",4,
     "A cube and a sphere have exactly the same volume. Explain, with reasoning, which one has the smaller surface area, and state the general optimization principle this illustrates. (Very hard.)","work",
     ["The sphere has the smaller surface area.  (A1)",
      "For a fixed volume, the sphere is the solid with the least surface area of all; among boxes the cube is best, "
      "but the sphere beats the cube.  (C1)",
      "General principle: for a given volume the surface area is minimized by the most 'compact' shape — the sphere.  (C1)",
      "This is why bubbles and water droplets form spheres.  (C1)"]),
]

TOTAL = sum(it[5] for it in ITEMS)
SECTIONS = {"A": "Section A — Knowledge & Understanding", "B": "Section B — Application",
            "C": "Section C — Thinking", "D": "Section D — Communication"}

def work_for(marks, category):
    if category == "K/U":
        return None
    return {2: 52, 3: 84, 4: 118, 5: 150, 6: 182}.get(marks, 40 * marks)


def build_test():
    d = CMFlow(OUT_T, topic_title=TOPIC, subtitle="Module 7 Test",
               grade_badge="Grade 9 · MTH1W",
               meta_right=[f"Time: {DURATION}", f"Total: {TOTAL} marks"], name_date=True)
    d.start()
    d.body("Instructions: Show all work for full marks. Marks for each question are shown in "
           "brackets. Use <b>π ≈ 3.14</b> and round π-answers to <b>1 d.p.</b> Calculators are permitted "
           "unless your teacher states otherwise.", ST_BODY, gap=12)
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
               info_line="MTH1W · Module 7 Test — Teacher Copy")
    d.start()
    d.heading("Blueprint", color=CM_BLUE)
    d.body(f"Curriculum: MTH1W (Grade 9 de-streamed math). Total: {TOTAL} marks · {DURATION} · "
           "30 questions. Categories: K/U, Application (App), Thinking (Think), Communication (Comm). "
           "π ≈ 3.14; π-values rounded to 1 d.p.", ST_BODY, gap=8)
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
