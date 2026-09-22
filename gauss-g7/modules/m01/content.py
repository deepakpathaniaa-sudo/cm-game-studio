"""Module 1 — Contest Mindset, Diagnostic and Toolkit. Content data (single source).
Original Concept Mastery items. Not reproduced from CEMC or any third party.
Strand codes: N number/fraction/percent/ratio · A algebra & patterns · G geometry & measurement ·
D data & probability · T number theory & counting · L logic."""
NB = " "
M = "−"

MODULE = dict(
    num=1, title="Contest Mindset, Diagnostic and Toolkit", topic_title="Contest Mindset and Diagnostic",   # footer/title form (layout §5 fit)
    hours=3.0, week=1, mode="— (non-content: orientation and diagnosis)", share="non-content",
    ontario="Ontario Mathematics (2020), Grade 7 — Strand A: Social-Emotional Learning Skills in Mathematics and "
            "the Mathematical Processes (verify expectation codes against the official document). The diagnostic "
            "samples Strands B–E.",
    goal="Know how Gauss is scored, and use six core moves to start any problem.",
)

STRAND_NAMES = {"N": "Number, fractions, percent, ratio", "A": "Algebra and patterns", "G": "Geometry and measurement",
                "D": "Data and probability", "T": "Number theory and counting", "L": "Logic"}
TIERS = [("Foundations", 1, 10, 2), ("Problem solving", 11, 20, 5), ("Challenge", 21, 25, 6)]

# fig keys are drawn by the build script from cm_figures primitives.
DIAG = [
    # ---------------- Foundations (2 points) ----------------
    dict(s="N", stem="What is <sup>3</sup>/<sub>4</sub> of 36?".replace("<sup>", "<super>").replace("</sup>", "</super>"),
         opts=["9", "12", "24", "27", "48"], key="D", v=27, wrong="(A) 9 — found 1/4 only",
         concept="Fraction of a quantity", fast="36 ÷ 4 = 9, then × 3."),
    dict(s="N", stem="What is 15% of 80?", opts=["8", "12", "15", "16", "65"], key="B", v=12,
         wrong="(E) 65 — subtracted 15 from 80", concept="Percent of a quantity", fast="10% is 8, 5% is 4; 8 + 4."),
    dict(s="A", stem="If 4<i>n</i> + 7 = 43, what is the value of <i>n</i>?", opts=["4", "7", "9", "12.5", "36"],
         key="C", v=9, wrong="(D) 12.5 — added 7 instead of subtracting: 50 ÷ 4",
         concept="Solving a one-step-then-two-step equation", fast="Undo: 43 − 7 = 36, 36 ÷ 4 = 9."),
    dict(s="A", stem="The pattern 5, 12, 19, 26, … continues by adding 7 each time. What is the 10th number in the pattern?",
         opts=["50", "61", "65", "68", "75"], key="D", v=68, wrong="(E) 75 — used 5 + 10 × 7 (one step too many)",
         concept="Arithmetic sequence: nth term", fast="10th term = first + 9 steps = 5 + 63."),
    dict(s="G", stem="A rectangle is 12 cm long and 7 cm wide. What is its perimeter?",
         opts=["19 cm", "26 cm", "38 cm", "84 cm", "168 cm"], key="C", v=38,
         wrong="(D) 84 cm — found the area", concept="Perimeter of a rectangle", fast="2 × (12 + 7)."),
    dict(s="G", stem="Two angles of a triangle measure 48° and 67°. What is the measure of the third angle?",
         opts=["45°", "55°", "65°", "115°", "295°"], key="C", v=65, wrong="(D) 115° — added the two angles and stopped",
         concept="Angle sum of a triangle", fast="180 − 48 − 67 = 180 − 115."),
    dict(s="D", stem="What is the mean (average) of 8, 11, 12, 15 and 24?", opts=["11", "12", "13", "14", "70"],
         key="D", v=14, wrong="(B) 12 — gave the median", concept="Mean of a data set", fast="Sum 70, ÷ 5."),
    dict(s="T", stem="Which of the following is a prime number?", opts=["59", "39", "51", "57", "91"], key="A", v=59,
         wrong="(E) 91 — looks prime, but 91 = 7 × 13", concept="Primes; divisibility by 3 and 7",
         fast="Digit sums 12, 6, 12 show 39, 51, 57 are multiples of 3; 91 = 7 × 13."),
    dict(s="T", stem="What is the lowest common multiple of 6 and 8?", opts=["2", "12", "14", "16", "24"], key="E", v=24,
         wrong="(A) 2 — gave the greatest common factor", concept="Lowest common multiple",
         fast="List multiples of 8 until one is a multiple of 6: 8, 16, 24."),
    dict(s="L", stem="Ana, Ben and Cy each own exactly one pet: a cat, a dog or a fish, all different. Ben does not "
                     "own the dog. Cy owns the cat. Who owns the fish?",
         opts=["Ben", "Ana", "Cy", "Ana or Ben", "It cannot be determined"], key="A", v="Ben",
         wrong="(E) — did not combine the two clues", concept="Logical deduction from constraints",
         fast="Cat is Cy's; Ben is not dog, so Ben has the fish."),
    # ---------------- Problem solving (5 points) ----------------
    dict(s="N", stem="A jacket costs $80. It is on sale for 25% off. Then 13% tax is added to the sale price. "
                     "What is the final cost?",
         opts=["$60.00", "$67.80", "$70.40", "$80.00", "$90.40"], key="B", v="67.80",
         wrong="(C) $70.40 — added −25% and +13% to get −12% of $80", concept="Successive percent change",
         fast="80 × 0.75 = 60; 60 × 1.13 = 67.80.", method=True,
         rep="A correct two-step chain (sale price 60, then tax on 60) or 80 × 0.75 × 1.13.",
         slip="Chain correct but one multiplication slipped."),
    dict(s="N", stem="The ratio of red marbles to blue marbles in a bag is 3 : 5. There are 48 marbles. "
                     "How many more blue marbles than red marbles are there?",
         opts=["6", "12", "18", "30", "48"], key="B", v=12,
         wrong="(A) 6 — found one part (48 ÷ 8) and stopped", concept="Ratio with a fixed total (parts of a whole)",
         fast="8 parts = 48, so a part is 6; blue − red = 2 parts = 12.", method=True,
         rep="A bar model or ratio table with 8 equal parts totalling 48.",
         slip="Part size 6 found but final difference slipped."),
    dict(s="N", stem="Mia ate <super>1</super>/<sub>3</sub> of a pizza. Leo then ate <super>1</super>/<sub>4</sub> of what "
                     "was left. What fraction of the whole pizza remains?",
         opts=["<super>1</super>/<sub>6</sub>", "<super>5</super>/<sub>12</sub>", "<super>1</super>/<sub>2</sub>",
               "<super>7</super>/<sub>12</sub>", "<super>2</super>/<sub>3</sub>"], key="C", v="1/2",
         wrong="(B) 5/12 — took 1/4 of the whole, not of the rest", concept="Fraction of a remainder (‘of what’)",
         fast="Left after Mia: 2/3; Leo leaves 3/4 of that: 2/3 × 3/4 = 1/2."),
    dict(s="A", stem="Squares are built in a row from toothpicks: 1 square uses 4 toothpicks, 2 squares use 7, "
                     "and 3 squares use 10. How many toothpicks are needed for 20 squares in a row?",
         opts=["60", "61", "63", "80", "81"], key="B", v=61,
         wrong="(D) 80 — used 4 per square, ignoring shared sides", concept="Linear pattern from a table",
         fast="First square 4, each new square adds 3: 4 + 19 × 3.", method=True,
         rep="A table of squares vs toothpicks showing +3, or the rule 3n + 1.",
         slip="Rule correct, final evaluation slipped."),
    dict(s="G", stem="The figure is made of rectangles and all corners are right angles. Some side lengths, in cm, "
                     "are shown. What is the area of the figure, in cm²?",
         fig="L_shape", opts=["56", "62", "68", "74", "80"], key="C", v=68,
         wrong="(E) 80 — used the full 10 × 8 rectangle", concept="Composite area; finding a missing side",
         fast="10 × 8 − (10 − 6) × (8 − 5) = 80 − 12.", method=True,
         rep="The figure split into two rectangles, or the 10 × 8 rectangle with the missing 4 × 3 corner marked.",
         slip="Correct decomposition, one product or sum slipped."),
    dict(s="G", stem="In the diagram, O lies on a straight line. Find the value of <i>x</i>.", fig="angles",
         opts=["21", "42", "63", "84", "126"], key="B", v=42,
         wrong="(C) 63 — solved 2x + 54 = 180", concept="Angles on a straight line; one-variable equation",
         fast="3x = 180 − 54 = 126."),
    dict(s="G", stem="A rectangular prism has a volume of 360 cm³. Its base is 8 cm by 9 cm. What is its height?",
         opts=["3 cm", "4 cm", "5 cm", "20 cm", "45 cm"], key="C", v=5,
         wrong="(E) 45 cm — divided by 8 only", concept="Volume of a prism (reverse)", fast="Base area 72; 360 ÷ 72."),
    dict(s="D", stem="A bag has 4 red marbles, 5 blue marbles and some green marbles. The probability of picking a "
                     "blue marble is <super>1</super>/<sub>3</sub>. How many green marbles are in the bag?",
         opts=["2", "3", "5", "6", "15"], key="D", v=6,
         wrong="(E) 15 — gave the total, not the green count", concept="Probability as a fraction of the total; reverse",
         fast="Blue is 1/3 of the total, so total = 15; green = 15 − 9.", method=True,
         rep="An equation such as 5 ÷ total = 1/3, or total = 15 stated.",
         slip="Total 15 found, subtraction slipped."),
    dict(s="T", stem="How many whole numbers from 1 to 100 are multiples of 3 or multiples of 5 (or both)?",
         opts=["33", "41", "47", "53", "58"], key="C", v=47,
         wrong="(D) 53 — counted multiples of 15 twice", concept="Inclusion–exclusion counting",
         fast="33 + 20 − 6.", method=True,
         rep="A Venn diagram or the three counts 33, 20 and 6.", slip="Counts correct, combination slipped."),
    dict(s="L", stem="Four friends finish a race with no ties. Ari finishes before Bo. Bo finishes before Dee. "
                     "Cal finishes immediately after Dee. Who finishes third?",
         opts=["Ari", "Bo", "Cal", "Dee", "It cannot be determined"], key="D", v="Dee",
         wrong="(C) Cal — placed Cal before Dee", concept="Ordering from constraints",
         fast="Chain: Ari, Bo, Dee, then Cal right after Dee."),
    # ---------------- Challenge (6 points, written answers) ----------------
    dict(s="N", stem="In a club, the ratio of boys to girls is 3 : 4. After 6 more boys join (and nobody leaves), "
                     "the numbers of boys and girls are equal. How many members does the club have now?",
         key="48", v=48, wrong="42 — the total before the 6 boys joined", concept="Ratio change when one part changes",
         fast="The gap of 1 part is 6, so 4 parts = 24 girls; now 24 + 24.",
         rep="A bar/ratio model with parts 3k and 4k, or 3k + 6 = 4k.", inter="k = 6 (or 18 boys and 24 girls before).",
         hints=["Reread: which group changes and which stays the same?", "Draw 3 bars for boys and 4 for girls, same size.",
                "The extra 6 boys fill exactly one bar."]),
    dict(s="A", stem="The sum of five consecutive even numbers is 170. What is the largest of the five numbers?",
         key="38", v=38, wrong="34 — gave the middle number", concept="Consecutive numbers: sum = count × middle",
         fast="Middle = 170 ÷ 5 = 34; largest = 34 + 4.",
         rep="Numbers written as n − 4, n − 2, n, n + 2, n + 4 (or n, n + 2, …).", inter="The middle number is 34.",
         hints=["Reread: ‘even’ — how far apart are the numbers?", "Write the five numbers around a middle number m.",
                "Their sum is 5m."]),
    dict(s="G", stem="A 4 × 4 × 4 cube is built from 64 small cubes. The outside of the large cube is painted. "
                     "How many small cubes have paint on exactly two faces?",
         key="24", v=24, wrong="8 — counted the corner cubes (three faces)", concept="Spatial counting on a cube's edges",
         fast="Each of the 12 edges has 4 − 2 = 2 middle cubes: 12 × 2.",
         rep="A sketch or layer view marking corner, edge and face cubes.", inter="2 two-face cubes on each edge.",
         hints=["Reread: exactly two faces — where on a cube does a small cube touch two painted faces?",
                "Sketch one edge of 4 cubes; mark which cubes touch three faces.",
                "Each edge has 2 cubes that are not corners."]),
    dict(s="D", stem="Two fair six-sided dice are rolled. What is the probability that the two numbers rolled add to 8?",
         key="5/36", v="5/36", wrong="5/11 — counted sums as equally likely", concept="Outcome space for two dice",
         fast="Pairs (2,6), (3,5), (4,4), (5,3), (6,2): 5 of 36.",
         rep="A 6 × 6 outcome grid or organised list of ordered pairs.", inter="5 favourable outcomes identified.",
         hints=["Reread: how many different results can two dice show together?", "Build a 6 × 6 grid of sums.",
                "There are 36 equally likely outcomes; count the 8s."]),
    dict(s="T", stem="How many three-digit whole numbers have digits that add to 5?",
         key="15", v=15, wrong="10 or 21 — missed or double-counted cases (e.g. allowed a leading 0)",
         concept="Organised casework; completeness", fast="Hundreds digit 5, 4, 3, 2, 1 gives 1 + 2 + 3 + 4 + 5 cases.",
         rep="An organised list or table by hundreds digit.", inter="At least three cases counted correctly (e.g. 1, 2, 3).",
         hints=["Reread: can the first digit be 0?", "Make a table with one row for each hundreds digit.",
                "With hundreds digit h, the other two digits add to 5 − h: that has 6 − h ways."]),
]

# ------------------------------------------------------------------ Six core moves: scripts with original mini-examples
MOVE_SCRIPTS = [
    ("Draw it", "A 12 m rope is cut into three pieces. The second is twice the first. The third is 2 m longer than "
     "the second. How long is the longest piece?",
     "Draw three bars: 1 unit, 2 units, 2 units + 2 m. Five units + 2 = 12, so a unit is 2 m; longest = 6 m.",
     "Not yet: guesses 4 m each. Developing: writes x, 2x, but stalls on the third. Secure: draws the bars and says "
     "“five equal units and an extra 2”."),
    ("Tabulate it", "In how many ways can you make 30¢ using only dimes and nickels?",
     "Table: dimes 0, 1, 2, 3 with nickels 6, 4, 2, 0. Four ways.",
     "Not yet: lists 2–3 at random and stops. Developing: lists in no order and misses one. Secure: orders by dimes "
     "and says “I know I have them all because dimes go 0 to 3”."),
    ("Try a small case", "Ten people each shake hands once with every other person. How many handshakes?",
     "2 people: 1. 3 people: 3. 4 people: 6. Each new person adds one more than the last: 1+2+…+9 = 45.",
     "Not yet: says 100 (10 × 10). Developing: says 90 (forgets each shake is counted twice). Secure: builds the "
     "small cases and explains the +2, +3 pattern."),
    ("Work backward", "Lia spends half her money, then spends $4 more, and has $6 left. How much did she start with?",
     "From $6: undo ‘spend $4’ → $10; undo ‘spend half’ → $20.",
     "Not yet: 6 × 2 + 4 = 16 (undoes in the wrong order). Developing: gets $20 but by trial. Secure: reverses each "
     "step and checks forward."),
    ("Eliminate options", "Which could be the product of two consecutive whole numbers? "
     "(A) 41 (B) 55 (C) 72 (D) 89 (E) 91",
     "One of two consecutive numbers is even, so the product is even. Only 72 survives (8 × 9).",
     "Not yet: multiplies pairs at random. Developing: finds 8 × 9 by search. Secure: eliminates four odd options "
     "in five seconds, then confirms."),
    ("Check reasonableness", "A student writes 19 × 21 = 299. Is that reasonable?",
     "19 × 21 is close to 20 × 20 = 400, so 299 is too small. (It is 399.)",
     "Not yet: accepts it. Developing: redoes the long multiplication. Secure: estimates in two seconds and flags it."),
]

MISCONCEPTIONS = [
    ("Part C is where the points are, so spend most time there.",
     "Where are 110 of the 150 points?", "Parts A and B hold 110 points (73%). Bank them first; Part C gets a fixed 15 minutes."),
    ("If I am not sure, leave it blank.",
     "What do you lose by writing your best elimination guess?",
     "Check the current-year rules on the CEMC page; where a wrong answer costs nothing, never leave a blank — "
     "eliminate, then choose."),
    ("The diagram shows the answer — I can measure it.",
     "What does ‘Diagrams are not drawn to scale’ mean for Q16?",
     "Use the given numbers and facts, not the look of the picture. Diagnostic figures are to scale, but contest ones may not be."),
    ("I must do the questions in order.",
     "You are stuck on Q14 at minute 25. What should happen next?",
     "Mark it ‘?’, move on, return in the check window. Order is a suggestion, time is not."),
    ("Checking wastes time.", "How many points would Q-reading errors have cost you on the diagnostic?",
     "The last 5 minutes are for re-reading marked questions; Q errors are the cheapest points to recover."),
    ("A wrong answer means I am bad at maths.", "What code would you give this error?",
     "Every error gets a code; codes show what to practise. The log turns mistakes into a plan."),
    ("Showing work is only for the teacher.", "On Q15, which part of your drawing earned points?",
     "Representations earn method credit here and catch errors in the contest. Draw first, calculate second."),
]

PERSISTENCE = [
    ("Starts independently", "Waits for help or leaves most items untouched for more than 2 minutes.",
     "Starts familiar items; stalls on unfamiliar ones.", "Starts every item within about a minute, unprompted."),
    ("Creates a representation", "No diagrams, tables or equations on Parts 2–3.",
     "Some representations, incomplete or only when prompted by a method box.",
     "Draws, tabulates or writes an equation on most Part 2–3 items without prompting."),
    ("Tries a second strategy", "Stops after the first approach fails.", "Repeats the same approach more carefully.",
     "Switches approach when stuck (e.g. from equation to table)."),
    ("Uses time deliberately", "Spends over 5 minutes on one item, or finishes early with blanks.",
     "Some pacing; returns to few skipped items.", "Moves on from stuck items and returns; uses the full hour."),
    ("Checks or revises", "No visible checking.", "Occasional checking, mostly on easy items.",
     "Visible checks: estimates, substitutes back, re-reads the question."),
    ("Responds constructively to a neutral hint", "Disengages or asks for the answer.",
     "Uses the hint partly, then stalls.", "Uses the hint to take the next step independently."),
]
NEUTRAL_HINTS = ["“What is the question asking you to find?”", "“What do you know so far?”",
                 "“Is there a way to picture this?”"]

PATHWAYS = [
    ("Advanced", "85–100", "Full programme at pace; Part C extension tasks every module; second-method requirement."),
    ("Core", "65–84", "Full programme as sequenced."),
    ("Core plus bridge", "50–64", "Full programme plus a weekly 30-minute bridge on the two weakest strands."),
    ("Foundations first", "below 50", "Foundations block on the flagged strands, then join the programme; "
                                      "re-diagnose with Form B."),
]
CAVEAT = ("These thresholds are unpiloted starting hypotheses. They will be revised once Form A data from this cohort "
          "are available. No student is rejected on a low Challenge score alone; placement also weighs the strand "
          "profile, the persistence observation and the tutor's judgement.")

LESSON_A = [
    ("0–10", "Welcome and contest format", "Section 5a script: what Gauss is, 25 questions, 60 minutes, five options. "
     "Student predicts which part is worth most."),
    ("10–20", "Scoring geometry", "Build the 5/6/8 table together; the 73% insight; pacing model from the strategy card."),
    ("20–80", "Entrance Diagnostic, Form A", "60 minutes, calculator-free. You observe and score the persistence rubric "
     "(separate sheet). At most one neutral hint per student, recorded."),
    ("80–90", "Exit reflection", "Student writes: easiest question, hardest question, one question they would change "
     "their answer on. Collect papers."),
]
LESSON_B = [
    ("0–10", "Retrieval", "Scoring geometry quiz: What is Part B worth in total? Score for all of A and half of B? "
     "Which part holds 73% of the points?"),
    ("10–25", "Concept / strategy", "The six core moves (section 5e script), each with its trigger. Hand out the "
     "Strategy Card."),
    ("25–45", "Guided practice", "Return the scored diagnostic. Re-work three of the student's missed items together, "
     "naming the core move each needed."),
    ("45–70", "Paired → independent", "Error-classification conversation (section 5c) on every remaining wrong item; "
     "student fills the first rows of the Error Log. Challenge items 21–25 re-attempted with the hint ladder."),
    ("70–80", "Method comparison", "Diagnostic Q12 or Q19: bar model vs equation, Venn diagram vs list. Which move "
     "was faster? Which was safer?"),
    ("80–90", "Exit check", "Two items (section 10). Placement conversation outline; parent update sent after class."),
]
