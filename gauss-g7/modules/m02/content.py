"""Module 2 — Integers, Place Value and Efficient Arithmetic. Content data (single source).

Original Concept Mastery items. Not reproduced from CEMC or any third party.
Every artifact for M2 (lesson plan, sheet, homework, solutions) is rendered
from these structures; answers are never retyped.
Tags: pillar / sub-topic / difficulty (olympiad skill §4 scale 1–5) / method.
"""
NB = " "          # non-breaking space inside numbers
M = "−"           # minus sign


def n(x):
    """Format an integer with non-breaking thin grouping (CEMC-style spaces)."""
    s = f"{abs(x):,}".replace(",", NB)
    return (M if x < 0 else "") + s


MODULE = dict(
    num=2,
    title="Integers, Place Value and Efficient Arithmetic",
    topic_title="Integers, Place Value and Arithmetic",   # footer/title form (fits layout §5 footer)
    hours=4.0, week=2, mode="A — Secure", share="7.6%",
    ontario="Ontario Mathematics (2020), Grade 7 — Strand B Number: B1 Number Sense, B2 Operations "
            "(expectation-level codes: verify against the official document; the CM code map has no "
            "verified Grade 7 Number rows yet).",
    canonical="Whole Numbers & Place Value · Integers · Decimals · Multiplication & Division · Time & Money",
    goal="Answer integer and place-value questions fast, with zero errors.",
    cemc_ref="Past papers for reference only (not reproduced): CEMC Gauss contests — "
             "https://cemc.uwaterloo.ca/contests/gauss",
)

ORIGINALITY = "Original Concept Mastery items. Not reproduced from CEMC or any third party."

# ---------------------------------------------------------------------------- worked examples
WE1 = dict(
    heading="Worked Example 1 — Restructure before you calculate",
    problem=f"What is the value of 36 × 7 + 64 × 7?",
    lines=[
        "<b>Problem.</b> What is the value of 36 × 7 + 64 × 7?",
        "<b>Scan first (10 seconds).</b> Both products contain × 7. 36 and 64 make 100.",
        "<b>Restructure.</b> 36 × 7 + 64 × 7 = (36 + 64) × 7 = 100 × 7.",
        "<b>Calculate.</b> 100 × 7 = 700.",
        "<b>Check.</b> 36 × 7 is about 250 and 64 × 7 is about 450; 250 + 450 = 700. ✓",
        "<b>Lesson.</b> A repeated factor or a pair that makes a round number is a signal to regroup.",
    ],
    answer=700,
)

WE2 = dict(
    heading="Worked Example 2 — Two methods, one answer: which is faster?",
    problem="What is (2 + 4 + 6 + … + 50) − (1 + 3 + 5 + … + 49)?",
    lines=[
        "<b>Problem.</b> What is (2 + 4 + 6 + … + 50) − (1 + 3 + 5 + … + 49)?",
        "<b>Method A — calculate each sum.</b> Evens: 2 × (1 + 2 + … + 25) = 2 × 325 = 650. "
        "Odds: 1 + 3 + … + 49 = 25 × 25 = 625. Difference: 650 − 625 = 25.",
        "<b>Method B — pair the terms.</b> (2 − 1) + (4 − 3) + … + (50 − 49). There are 25 pairs "
        "and each pair is 1, so the answer is 25.",
        "<b>Compare.</b> Method A needs two sum formulas and a subtraction. Method B needs one count. "
        "Both give 25; Method B is the contest method.",
        "<b>Lesson.</b> When two long lists line up term by term, subtract in pairs.",
    ],
    answer=25,
)

# ---------------------------------------------------------------------------- student sheet items
# type: layout §11 question type. opts: five Gauss options (A)–(E). key: letter or value.
# wrong: likely wrong answer + reason. note: faster contest method. t: time target (s).
PV_HEAD = ["M", "HTh", "TTh", "Th", "H", "T", "O"]

SHEET = [
    # ---- Guided practice (Lesson A) ----
    dict(block="guided", type="short", work="line",
         stem=f"In {n(7350912)}, which digit is in the ten-thousands place? "
              "<i>Scaffold: write the digits into the chart, starting from the ones (O) column.</i>",
         fig="pv_blank", key="5", ans_val=5,
         wrong="3 (one place too far: hundred-thousands) or 9 (counted five places from the left)", concept="Place value: naming a place",
         fast="Group digits in threes from the right; ten-thousands is the middle digit of the thousands group.",
         tag=("Number", "place value", 1, "place-value chart"), t=20),
    dict(block="guided", type="short", work="line",
         stem=f"Which of these numbers is farthest from 0? {M}8.2, 7.9, {M}0.85, 8.1, {M}8.02 "
              "<i>Scaffold: write the distance from 0 of each number first.</i>",
         key=f"{M}8.2", ans_val=-8.2,
         wrong=f"{M}0.85 or 8.1 — chose the smallest-looking or the largest positive number",
         concept="Absolute value as distance from 0",
         fast="Compare only the sizes 8.2, 7.9, 0.85, 8.1, 8.02; the sign never matters.",
         tag=("Number", "integers / decimals", 1, "distance from 0"), t=25),
    dict(block="guided", type="short", work="line",
         stem=f"At 5 a.m. the temperature was {M}11°C. By 2 p.m. it was 6°C. By how many degrees did the "
              "temperature rise? <i>Scaffold: draw a jump to 0, then a jump to 6.</i>",
         fig="nl_blank", key="17", ans_val=17,
         wrong="5 — computed 11 − 6 (dropped the sign)", concept="Integer difference across zero",
         fast="Distance across 0 = 11 + 6.", tag=("Number", "integers", 1, "number-line jumps"), t=25),
    dict(block="guided", type="short", work="line",
         stem="A runner's two laps took 3 min 48 s and 4 min 25 s. What was the total time? "
              "<i>Scaffold: add the seconds first; trade 60 s for 1 min.</i>",
         key="8 min 13 s", ans_val=(8, 13),
         wrong="7 min 73 s or 8 min 73 s — no regrouping, or regrouped by 100",
         concept="Time arithmetic with regrouping",
         fast="Round up: 3:48 + 4:25 = (4:00 − 12 s) + 4:25 = 8:25 − 12 s = 8:13.",
         tag=("Number", "time", 1, "regroup units"), t=30),
    dict(block="guided", type="short", work="line",
         stem="Calculate 125 × 13 × 8. <i>Scaffold: which two factors make a round number?</i>",
         key=n(13000), ans_val=13000,
         wrong="1 625 × 8 done by hand and slipped (e.g. 12 000)", concept="Structural rearrangement (convenient products)",
         fast="125 × 8 = 1 000, so the answer is 13 × 1 000.", tag=("Number", "efficient arithmetic", 2, "regroup factors"), t=20),
    dict(block="guided", type="short", work="line",
         stem="Calculate 19 × 46 + 81 × 46. <i>Scaffold: what do both products share?</i>",
         key=n(4600), ans_val=4600,
         wrong="4 646 or an arithmetic slip from computing 874 + 3 726 by hand",
         concept="Factoring a common multiplier out of a sum",
         fast="(19 + 81) × 46 = 100 × 46.", tag=("Number", "efficient arithmetic", 2, "factor out"), t=20),
    # ---- Independent practice (Lesson A paired → Lesson B) ----
    dict(block="independent", type="word_problem", work="line",
         stem="When the numbers 0.305, 0.35, 0.3, 0.053 and 0.53 are listed from smallest to largest, "
              "which number is in the middle?",
         opts=["0.305", "0.35", "0.3", "0.053", "0.53"], key="A", ans_val=0.305,
         wrong="(B) 0.35 — believes more digits means larger (0.305 > 0.35)",
         concept="Ordering decimals; middle value", fast="Pad to three places: 305, 350, 300, 053, 530 → middle 305.",
         tag=("Number", "decimals", 1, "pad to equal places"), t=30),
    dict(block="independent", type="word_problem", work="line",
         stem=f"What is the sum of the digits of the number {n(4070809)}?",
         opts=["19", "24", "27", "28", "29"], key="D", ans_val=28,
         wrong="(A) 19 — dropped the final 9; (B) 24 — dropped the leading 4",
         concept="Digit sums", fast="Skip the zeros and pair: (4 + 8) + (7 + 9) = 12 + 16 = 28.",
         tag=("Number", "digit sums", 1, "direct"), t=20),
    dict(block="independent", type="word_problem", work="line",
         stem="A bakery sells muffins for $2.35 each. What is the cost of 12 muffins?",
         opts=["$23.50", "$25.85", "$28.20", "$28.70", "$30.55"], key="C", ans_val=28.20,
         wrong="(B) $25.85 — 10 × 2.35 + 2.35 (added one muffin, not two)",
         concept="Decimal money × count", fast="12 × 2.35 = 12 × 2 + 12 × 0.35 = 24 + 4.20.",
         tag=("Number", "money", 1, "split the decimal"), t=30),
    dict(block="independent", type="word_problem", work="line",
         stem="Two boards are each 360 cm long. One is cut completely into 12 cm pieces and the other "
              "into 20 cm pieces. How many more 12 cm pieces are there than 20 cm pieces?",
         opts=["8", "12", "18", "30", "48"], key="B", ans_val=12,
         wrong="(A) 8 — subtracted the lengths 20 − 12", concept="Division and comparison of counts",
         fast="360 ÷ 12 = 30 and 360 ÷ 20 = 18; 30 − 18 = 12.",
         tag=("Number", "division", 2, "compute both counts"), t=30),
    dict(block="independent", type="word_problem", work="line",
         stem="Which number is equal to 4 × 10<super>4</super> + 3 × 10<super>2</super> + 5 × 10?",
         opts=[n(4350), n(40350), n(43050), n(400350), n(403500)], key="B", ans_val=40350,
         wrong="(C) 43 050 — shifted the 3 one place left", concept="Place value with powers of ten",
         fast="Write a place-value row: 4 _ 3 5 _ → 40 350.", tag=("Number", "powers of ten", 1, "expanded form"), t=25),
    dict(block="independent", type="word_problem", work="line",
         stem=f"What is the value of 12 {M} ({M}7) + ({M}15)?",
         opts=[f"{M}10", f"{M}4", "4", "20", "34"], key="C", ans_val=4,
         wrong=f"(A) {M}10 — treated {M}({M}7) as {M}7", concept="Integer addition and subtraction",
         fast="Subtracting −7 is adding 7: 12 + 7 − 15 = 4.", tag=("Number", "integers", 1, "rewrite as addition"), t=25),
    dict(block="independent", type="word_problem", work="line",
         stem="On a standard die the numbers 1 to 6 appear once each, so the six faces add to 21. A die "
              "sits on a table. The five faces that are not touching the table add to 17. What number "
              "is on the face touching the table?",
         opts=["1", "2", "3", "4", "5"], key="D", ans_val=4,
         wrong="(C) 3 — gave the top face (7 − 4) instead of the bottom face", concept="Complement to a known total",
         fast="Hidden = total − visible = 21 − 17.", tag=("Number", "complements", 1, "total minus visible"), t=25),
    dict(block="independent", type="word_problem", work="line",
         stem="A movie starts at 7:48 p.m. and runs for 2 hours 37 minutes. At what time does it end?",
         opts=["9:25 p.m.", "9:45 p.m.", "10:05 p.m.", "10:15 p.m.", "10:25 p.m."], key="E", ans_val=(22, 25),
         wrong="(A) 9:25 p.m. — did not carry the extra hour from 85 minutes", concept="Time arithmetic with regrouping",
         fast="7:48 + 12 min = 8:00; 2 h 37 min − 12 min = 2 h 25 min; 8:00 + 2:25 = 10:25.",
         tag=("Number", "time", 2, "make the next hour"), t=30),
    # ---- Stretch (Part C) ----
    dict(block="stretch", type="multi_step", work="long",
         stem=f"The number 10<super>30</super> {M} 47 is written out in full. What is the sum of its digits? "
              "<i>Use the space to build a table of small cases: 10<super>2</super> − 47, "
              "10<super>3</super> − 47, 10<super>4</super> − 47.</i>",
         opts=["252", "259", "260", "262", "270"], key="C", ans_val=260,
         wrong="(E) 270 — assumed 30 nines; (A) 252 — 28 nines but dropped the final 53",
         concept="Place value in 10ⁿ − k; digit sum of the result",
         fast="10³⁰ − 47 = (10³⁰ − 1) − 46 = 28 nines followed by 53 → 28 × 9 + 5 + 3.",
         tag=("Number", "10ⁿ − k", 4, "small cases → pattern"), t=150, challenge=True,
         hints=["Reread: how many digits does 10<super>30</super> have? How many does 10<super>30</super> − 47 have?",
                "Make a table of 10<super>n</super> − 47 for n = 2, 3, 4, 5. Don't calculate the big one yet.",
                "10<super>n</super> − 47 is (n − 2) nines followed by 53."]),
    dict(block="stretch", type="multi_step", work="long",
         stem="How many digits does the number 5<super>20</super> × 2<super>18</super> have when it is "
              "written out in full?",
         opts=["19", "20", "21", "38", "40"], key="B", ans_val=20,
         wrong="(D) 38 — added the exponents; (C) 21 — used 10²⁰ instead of 25 × 10¹⁸",
         concept="Pairing 5 × 2 = 10 (structural rearrangement with powers)",
         fast="5²⁰ × 2¹⁸ = 5² × (5 × 2)¹⁸ = 25 × 10¹⁸ → 2 digits + 18 zeros.",
         tag=("Number", "powers of ten", 4, "pair 5s with 2s"), t=120, challenge=True,
         hints=["Reread: which pairs of factors make 10?",
                "Rewrite 5<super>20</super> as 5<super>2</super> × 5<super>18</super> and pair each 5 with a 2.",
                "The product is 25 × 10<super>18</super>."]),
    # ---- Exit ticket ----
    dict(block="exit", type="short", work="line",
         stem="Calculate 250 × 17 × 4.", key=n(17000), ans_val=17000,
         wrong="4 250 × 4 slipped (e.g. 16 000)", concept="Convenient products",
         fast="250 × 4 = 1 000.", tag=("Number", "efficient arithmetic", 1, "regroup factors"), t=20),
    dict(block="exit", type="word_problem", work="std",
         stem="Find 999 + 998 + 1002 + 1001 and explain in one or two sentences why your method is fast.",
         key=n(4000), ans_val=4000,
         wrong="An addition slip from column-adding four 4-digit numbers",
         concept="Compensation around a round number",
         fast="Each number is 1 000 ± a little: (−1) + (−2) + 2 + 1 = 0, so 4 × 1 000.",
         tag=("Number", "efficient arithmetic", 2, "compensation"), t=40),
]

SHEET_BLOCKS = [
    ("guided", "Guided practice", "Lesson A · 20 min. Do these together; say the scaffold step aloud first."),
    ("independent", "Independent practice", "Lesson A (paired, Q7–10) and Lesson B (independent, Q11–14). "
                                            "Target: 30 seconds per question, zero errors."),
    ("stretch", "Stretch", "Stretch — Part C level. Record every case you try in the space."),
    ("exit", "Exit ticket", "Lesson B · last 10 min. On your own."),
]
TEACHER_TIMING = {
    "guided": "Timing: 20 min (Lesson A). Cut if long: Q5 (Q6 tests the same structure).",
    "independent": "Timing: Q7–10 paired 12 min (Lesson A); Q11–14 independent 8 min (Lesson B). "
                   "Cut if long: Q10 and Q13 (move to the extension session).",
    "stretch": "Timing: 12 min (Lesson B, paired). Cut if long: Q16 — keep Q15, it is the strand's one Part C structure.",
    "exit": "Timing: 10 min (Lesson B). Never cut.",
}

TRIGGERS = [
    "When you see <b>two products sharing a number</b>, reach for <b>factoring it out</b>: a × c + b × c = (a + b) × c.",
    "When you see <b>numbers close to a round number</b>, reach for <b>compensation</b>: write each as round ± small.",
    "When you see <b>25, 125 or 5</b> in a product, reach for <b>their partners 4, 8 or 2</b>.",
    "When you see <b>a change that crosses 0</b>, reach for <b>two jumps: to 0, then onward</b>.",
    "When you see <b>10<super>n</super> minus something</b>, reach for <b>small cases n = 2, 3, 4</b> and count the 9s.",
]

# ---------------------------------------------------------------------------- homework
HOMEWORK = [
    dict(kind="Retrieval", src="M1 — contest scoring (5/6/8)", type="word_problem", work="line",
         stem="In a 25-question contest, questions 1–10 are worth 5 points each, 11–20 are worth 6 points "
              "each and 21–25 are worth 8 points each. Priya gets questions 1–10 right and five of the "
              "questions 11–20 right. All her other answers are wrong. What is her score?",
         opts=["75", "80", "90", "110", "120"], key="B", ans_val=80,
         wrong="(A) 75 — scored all 15 correct answers at 5 points",
         concept="Contest scoring geometry (Part A/B values)",
         fast="Part A is worth 50 in total; add 5 × 6 = 30.",
         tag=("Logic", "contest format", 1, "compute"), ext="What is the smallest number of correct answers that scores at least 100?"),
    dict(kind="Retrieval", src="M1 — try a small case", type="word_problem", work="line",
         stem="What is the value of 1 + 3 + 5 + 7 + ⋯ + 39?",
         opts=["210", "380", "390", "400", "420"], key="D", ans_val=400,
         wrong="(E) 420 — summed 2 + 4 + ⋯ + 40 (the evens); (A) 210 — summed 1 + 2 + ⋯ + 20",
         concept="Small cases reveal a pattern (sums of odd numbers are squares)",
         fast="Pair first and last: 20 terms make 10 pairs of 40 → 400.",
         tag=("Algebra", "sequences", 2, "small cases"), ext="What is 1 + 3 + 5 + ⋯ + 99?"),
    dict(kind="Retrieval", src="M1 — work backward", type="word_problem", work="line",
         stem="Tomas thinks of a number. He multiplies it by 4 and then subtracts 9. His result is 55. "
              "What number did he think of?",
         opts=["11.5", "16", "46", "64", "229"], key="B", ans_val=16,
         wrong="(A) 11.5 — undid the steps in the wrong order: (55 − 9) ÷ 4",
         concept="Working backward with inverse operations",
         fast="Undo in reverse: 55 + 9 = 64, 64 ÷ 4 = 16. Check: 16 × 4 − 9 = 55.",
         tag=("Algebra", "inverse operations", 1, "work backward"), ext="If he had subtracted 9 first and then multiplied by 4, getting 55, what would be his number?"),
    dict(kind="Current topic", src="M2", type="word_problem", work="line",
         stem="Which of the following numbers is the smallest?",
         opts=["0.7", "0.707", "0.077", "0.0707", "0.07"], key="E", ans_val=0.07,
         wrong="(D) 0.0707 — more zeros and digits looked smaller",
         concept="Ordering decimals", fast="Pad to four places: 7000, 0700, 7070, 0770, 0707.",
         tag=("Number", "decimals", 1, "pad to equal places"), ext="List all five numbers from largest to smallest."),
    dict(kind="Current topic", src="M2", type="word_problem", work="line",
         stem="A rope 4.8 m long is cut completely into pieces 30 cm long. An identical rope is cut "
              "completely into pieces 40 cm long. How many more 30 cm pieces are there than 40 cm pieces?",
         opts=["4", "10", "12", "16", "28"], key="A", ans_val=4,
         wrong="(B) 10 — subtracted the lengths 40 − 30", concept="Division and comparison of counts (with units)",
         fast="480 ÷ 30 = 16 and 480 ÷ 40 = 12.", tag=("Number", "division", 2, "convert, then divide"),
         ext="With a third rope cut into 60 cm pieces, how many fewer pieces than the 30 cm rope?"),
    dict(kind="Current topic", src="M2", type="word_problem", work="line",
         stem="A parking lot charges $1.75 for every 15 minutes or part of 15 minutes. A car parks from "
              "9:52 a.m. until 11:20 a.m. How much does it pay?",
         opts=["$8.75", "$10.27", "$10.50", "$12.25", "$15.75"], key="C", ans_val=10.50,
         wrong="(A) $8.75 — ignored the part block (5 blocks for 88 min)",
         concept="Time difference with regrouping; money × count; ceiling of a division",
         fast="9:52 → 11:20 is 1 h 28 min = 88 min; 90 min is 6 blocks; 6 × 1.75 = 10.50.",
         tag=("Number", "time / money", 2, "count blocks"), ext="What is the latest time the car could leave and still pay $10.50?"),
    dict(kind="Current topic", src="M2", type="word_problem", work="line",
         stem=f"At midnight the temperature was {M}6°C. By 4 a.m. it had fallen 9 degrees. By noon it had "
              "risen 23 degrees from its 4 a.m. value. What was the temperature at noon?",
         opts=[f"{M}20°C", f"{M}8°C", "8°C", "20°C", "38°C"], key="C", ans_val=8,
         wrong="(D) 20°C — started from +6 instead of −6", concept="Integer change on a number line",
         fast="Net change −9 + 23 = +14; −6 + 14 = 8.", tag=("Number", "integers", 1, "net change"),
         ext="Which of the three readings was lowest, and how many degrees below the noon reading was it?"),
    dict(kind="Interleaved", src="M1 work backward + M2 time", type="word_problem", work="line",
         stem="Maya's bus comes at 8:17 a.m. She needs 18 minutes to get ready, 25 minutes for breakfast "
              "and 12 minutes to walk to the stop, and she wants to be at the stop 4 minutes early. What "
              "is the latest time she can get up?",
         opts=["7:08 a.m.", "7:18 a.m.", "7:22 a.m.", "7:28 a.m.", "7:58 a.m."], key="B", ans_val=(7, 18),
         wrong="(C) 7:22 a.m. — forgot the 4 minutes early", concept="Work backward through time with regrouping",
         fast="Total 59 min = 1 h − 1 min: 8:17 − 1 h = 7:17, + 1 min = 7:18.",
         tag=("Number", "time", 2, "work backward"), ext="If breakfast takes 10 minutes longer, when must she get up?"),
    dict(kind="Interleaved", src="M1 eliminate options + M2 middle value", type="word_problem", work="line",
         stem="Which of the following could be the sum of five consecutive whole numbers?",
         opts=["52", "63", "74", "81", "95"], key="E", ans_val=95,
         wrong="(B) 63 or (D) 81 — tried a few sums, found none, and guessed",
         concept="Sum of consecutive numbers = count × middle value; eliminate options",
         fast="Five consecutive numbers sum to 5 × middle, so the sum is a multiple of 5.",
         tag=("Number", "structure", 2, "eliminate options"), ext="Which of the five options could be the sum of four consecutive whole numbers?"),
    dict(kind="Challenge", src="M2 — Part C", type="multi_step", work="std",
         stem="The number N is written with fifty 9s: N = 999…9. What is the sum of the digits of 7 × N?",
         opts=["350", "441", "450", "451", "459"], key="C", ans_val=450,
         wrong="(A) 350 — assumed the answer is 7 × 50", concept="10ⁿ − 1 structure; digit sum",
         fast="7 × N = 7 × 10⁵⁰ − 7 = 6, then forty-nine 9s, then 3 → 6 + 49 × 9 + 3.",
         tag=("Number", "10ⁿ − 1", 4, "small cases → pattern"), challenge=True,
         ext="What is the sum of the digits of 13 × N (N with fifty 9s)?",
         hints=["Reread: N is 10<super>50</super> − 1. What does that make 7 × N?",
                "Make a table: 7 × 9, 7 × 99, 7 × 999. Look at the digits, not the size.",
                "7 × (10<super>n</super> − 1) = 7 × 10<super>n</super> − 7, which is 6, then (n − 1) nines, then 3."]),
]
HOMEWORK_TIME = "Time target: 25 minutes for the whole set (about 2 minutes per question, 6 for the challenge)."

# Full solutions — six-part CM standard (main · second · faster · concept · mistake · extension)
HW_SOLUTIONS = [
    dict(main="Part A: 10 × 5 = 50. Part B: 5 × 6 = 30. Wrong answers score 0. Total 50 + 30 = 80.",
         second="Count all 15 correct at 5 points (75), then add the extra 1 point for each of the 5 Part B questions: 75 + 5 = 80.",
         ext_ans="Use the highest values first: five Part C answers (40) and ten Part B answers (60) make 100 with 15 correct answers. 14 answers score at most 40 + 9 × 6 = 94, so 15 is the smallest."),
    dict(main="There are 20 odd numbers from 1 to 39. Small cases: 1 = 1, 1 + 3 = 4, 1 + 3 + 5 = 9 — the sum of the "
              "first k odd numbers is k × k. So the sum is 20 × 20 = 400.",
         second="Pair first and last: 1 + 39 = 40, 3 + 37 = 40, …; 20 terms make 10 pairs, 10 × 40 = 400.",
         ext_ans="50 odd numbers → 50 × 50 = 2 500."),
    dict(main="Undo each step in reverse order. Result 55 → add back the 9 → 64 → divide by 4 → 16.",
         second="Equation: 4x − 9 = 55, so 4x = 64 and x = 16.",
         ext_ans="4(x − 9) = 55 gives x − 9 = 13.75, x = 22.75."),
    dict(main="Write every number to four decimal places: 0.7000, 0.0700, 0.7070, 0.0770, 0.0707. "
              "The smallest is 0.0700 = 0.07.",
         second="Compare tenths first: 0.07, 0.077 and 0.0707 have 0 tenths. Hundredths: all 7. Thousandths: 0, 7, 0. "
                "Ten-thousandths: 0.0700 vs 0.0707 → 0.07 is smallest.",
         ext_ans="0.707, 0.7, 0.077, 0.0707, 0.07."),
    dict(main="4.8 m = 480 cm. 480 ÷ 30 = 16 pieces; 480 ÷ 40 = 12 pieces. 16 − 12 = 4.",
         second="Every 120 cm of rope gives 4 pieces of 30 cm but only 3 pieces of 40 cm — one extra piece. 480 cm is 4 lots of 120 cm, so there are 4 extra pieces.",
         ext_ans="480 ÷ 60 = 8; 16 − 8 = 8 fewer."),
    dict(main="From 9:52 to 10:52 is 60 min; 10:52 to 11:20 is 28 min. Total 88 min. 88 min is more than "
              "5 blocks (75 min) and at most 6 blocks (90 min), so the car pays for 6 blocks: 6 × $1.75 = $10.50.",
         second="Count up in 15-minute blocks from 9:52: 10:07, 10:22, 10:37, 10:52, 11:07, 11:22. The 6th block "
                "ends at 11:22, after 11:20 → 6 blocks.",
         ext_ans="The 6th block ends at 11:22 a.m."),
    dict(main="Midnight −6°C. Fall 9: −6 − 9 = −15°C at 4 a.m. Rise 23: −15 + 23 = 8°C at noon.",
         second="Net change: −9 + 23 = +14. Start −6, so −6 + 14 = 8.",
         ext_ans="The 4 a.m. reading, −15°C, was lowest; it was 23 degrees below the noon reading of 8°C."),
    dict(main="Add the times needed: 18 + 25 + 12 + 4 = 59 min. Count back 59 min from 8:17: 8:17 − 17 min = 8:00, "
              "then 42 more minutes back = 7:18 a.m.",
         second="59 min = 1 h − 1 min. 8:17 − 1 h = 7:17; add back 1 min → 7:18 a.m.",
         ext_ans="69 min before 8:17 → 7:08 a.m."),
    dict(main="Five consecutive numbers are m − 2, m − 1, m, m + 1, m + 2. They add to 5 × m, a multiple of 5. "
              "Only 95 is a multiple of 5: 17 + 18 + 19 + 20 + 21 = 95.",
         second="Eliminate by trying: the smallest sums are 0+1+2+3+4 = 10, then 15, 20, 25, … — they go up by 5, "
                "so the sum must end in 0 or 5.",
         ext_ans="Four consecutive numbers k, k + 1, k + 2, k + 3 add to 4k + 6. Subtract 6 and test for a multiple of 4: only 74 − 6 = 68 = 4 × 17 works, so 74 = 17 + 18 + 19 + 20."),
    dict(main="N = 10<super>50</super> − 1, so 7 × N = 7 × 10<super>50</super> − 7. Small cases: 7 × 9 = 63, 7 × 99 = 693, "
              "7 × 999 = 6 993. With n nines the product is 6, then (n − 1) nines, then 3. For n = 50: "
              "6 + 49 × 9 + 3 = 450.",
         second="Digit-sum fact from the small cases: 63 → 9, 693 → 18, 6 993 → 27: the digit sum is 9 × (number of 9s). "
                "So 9 × 50 = 450.",
         ext_ans="13 × 999 = 12 987 and 13 × 9 999 = 129 987: the product is 12, then (n − 2) nines, then 87. For n = 50: 1 + 2 + 48 × 9 + 8 + 7 = 450 (again 9 × 50)."),
]

# ---------------------------------------------------------------------------- misconceptions
MISCONCEPTIONS = [
    ("A longer decimal is a larger decimal.", "Which is greater, 0.35 or 0.305? Convince me.",
     "Pad to the same number of places (0.350 vs 0.305) and compare as whole numbers of thousandths."),
    ("Place names are counted from the left.", "Point to the ten-thousands digit in 7 350 912. How did you find it?",
     "Always count from the ones digit; group digits in threes from the right."),
    ("Subtracting a negative makes the answer smaller.", "What is 9 − (−14)? Show me on the number line.",
     "Subtraction is the distance/difference: from −14 up to 9 is 14 + 9 = 23. Rewrite − (−a) as + a."),
    ("Farthest from 0 means the smallest number.", "Which is smaller, −8.2 or 8.1? Which is farther from 0?",
     "Distance from 0 ignores sign; ‘smallest’ uses sign. Say both questions aloud before answering."),
    ("Time is a decimal: 60 seconds behave like 100.", "Write 48 s + 25 s in minutes and seconds.",
     "Trade 60, not 100: 73 s = 1 min 13 s. Circle the unit at each step."),
    ("Calculate first, look later.", "Before you multiply: what do 19 × 46 and 81 × 46 share?",
     "Enforce a 10-second scan for a repeated factor, a round pair, or 25/125 partners before any algorithm."),
    ("10ⁿ − k has n nines.", "Write out 10⁴ − 47. How many 9s? How many digits?",
     "Build the small-case table; the last two digits come from 100 − 47, so there are n − 2 nines."),
    ("A leftover part counts as a piece (or as a whole block when it should not).",
     "From 100 cm, how many 30 cm pieces? From 88 min, how many 15-min blocks are paid?",
     "Pieces round down (a leftover is waste); ‘part of a block’ charges round up. Read which one the question means."),
]

DIFFERENTIATION = dict(
    struggling="Keep the reasoning, shrink the numbers: do Q3 with −3°C → 4°C on the printed number line, "
               "Q6 as 2 × 5 + 8 × 5 with counters, and Q15 as 10² − 47 and 10³ − 47 written out in full. "
               "Then return to the original numbers the same session. Use the place-value chart for every "
               "place-value item; use the number line for every integer item.",
    onlevel="Complete Q1–14 at the 30-second target, then Q15 with the small-case table. Log every error "
            "with a code in the error log.",
    advanced="For every independent item give a second method in the margin. Q15–16: write a one-line "
             "completeness argument (why the pattern holds for every n). Part C extension: find the digit "
             "sum of 10<super>30</super> − 2 026, and of 13 × (10<super>50</super> − 1).",
)

PARENT_LINE = ("[Child] worked on integers, place value and fast mental arithmetic for contest Part A; strongest at "
               "___; we will practise ___ next, with timed drill sets at home (10 minutes a day).")

# ---------------------------------------------------------------------------- lesson plan timing
LESSON_A = [
    ("0–10", "Retrieval", "Prerequisite check (below) + 3 quick M1 items: What are Part A, B and C worth? "
     "Name the six core moves. What error code is ‘I misread the question’?"),
    ("10–25", "Concept / strategy", "Worked Example 1 (restructure before you calculate). Script below. "
     "Introduce the 10-second scan."),
    ("25–45", "Guided practice", "Sheet Q1–6. Student says the scaffold step aloud before writing."),
    ("45–70", "Paired → independent", "Sheet Q7–10 in pairs (12 min, 30 s each target then discuss), "
     "then Drill Book Set 1 alone (8 min, target 10 min for 20 items — stop at 8 and note how far)."),
    ("70–80", "Method comparison", "Worked Example 2: calculate-each-sum vs pair-the-terms. Class votes, then times both."),
    ("80–90", "Exit check (Lesson A)", "Two items on a slip: (1) 25 × 37 × 4 = ?  (2) Which is farther from 0, "
     "−6.5 or 6.05? Record accuracy; anything below 2/2 goes into Lesson B retrieval."),
]
LESSON_B = [
    ("0–10", "Retrieval", "Redo the Lesson A exit items with new numbers: 125 × 29 × 8; farther from 0: −3.7 or 3.69. "
     "Two Drill Set 1 items the student missed."),
    ("10–25", "Concept / strategy", "10ⁿ − k and time/money regrouping. Build the 10ⁿ − 47 table as a class; "
     "model 7:48 + 2:37 by making the next hour."),
    ("25–45", "Guided practice", "Drill Book Set 2 timed (10 min target), then mark and code errors together."),
    ("45–70", "Paired → independent", "Sheet Q11–14 independent (8 min, 30 s each), then Q15–16 in pairs (12 min) "
     "using the hint ladder. Record hint level used."),
    ("70–80", "Method comparison", "Q15: small-case table vs ‘10³⁰ − 47 = (10³⁰ − 1) − 46’. Which transfers to Q16 and HW Q10?"),
    ("80–90", "Exit ticket", "Sheet Q17–18. Hand out homework; set the 25-minute time target."),
]
EXTENSION = [
    ("0–10", "Retrieval", "Five errors from the student's error log, re-worked cold."),
    ("10–30", "Timed accuracy", "Drill Book Sets 3 and 4 back to back. Target: 90% at 30 s per item."),
    ("30–50", "Error analysis", "Code every miss (C R S A V Q T K). For each A or Q error, write the check that would have caught it."),
    ("50–60", "Speed round", "Mixed Final Set items 1–10 against the clock; compare with Set 1 time."),
]
PREREQ = dict(
    modules="M1 (six core moves, error codes, scoring geometry). Grade 6: integers on a number line, decimal "
            "place value to thousandths, whole-number operations.",
    check=f"First five minutes: (1) Order −3, 2, −7, 0 from least to greatest. (2) Which is larger, 0.4 or 0.39? "
          f"(3) 48 + 25 = ? If any item is missed, run the struggling path for that item type.",
)
WHY = ("This category is worth 7.6% of observed Gauss Grade 7 points, and 12 of its 13 observed questions sit in Part A "
       "(5 points each). That makes it a speed-and-accuracy module, not a depth module: the 4.0 hours buy volume, "
       "not difficulty. Teach for zero errors at 30 seconds per item; the single Part C structure here (10ⁿ − k) "
       "gets one focused block in Lesson B.")
