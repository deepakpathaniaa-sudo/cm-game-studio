"""Build all Module 2 artifacts from content.py (+ drill cluster Integer & Place-Value)."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
from common import OUT, GRADE, ORIGINALITY, ERROR_CODES, CEMC_URL  # noqa: E402
import cm_pdf as K  # noqa: E402
from cm_pdf import CMDoc, Figure, WORK_SPACE, merge  # noqa: E402
import cm_figures as FG  # noqa: E402
import content as C  # noqa: E402
import integer_pv as DR  # noqa: E402

MOD = C.MODULE
TOPIC = MOD["topic_title"]
FT = "GaussM02Integers"
LETTERS = "ABCDE"


PART_DIR = os.path.join(OUT, ".parts")   # second halves of combined files (page numbers continue)


def doc(kind, subtitle, start_page=1):
    d = CMDoc(TOPIC, GRADE, FT + kind, PART_DIR if start_page > 1 else OUT, start_page=start_page)
    d.title_block(subtitle)
    return d


def fig_for(key):
    if key == "pv_blank":
        return Figure("illustration", FG.place_value_chart(C.PV_HEAD), h=48)
    if key == "nl_blank":
        return FG.number_line_figure(-12, 8, step=1, label_every=2)
    raise KeyError(key)


def ans_text(it):
    if it.get("opts"):
        return f"({it['key']}) {it['opts'][LETTERS.index(it['key'])]}"
    return it["key"]


def render_item(d, num, it, teacher=False, show_src=False):
    stem = it["stem"]
    if show_src:
        stem = f"<i>{it['kind']} · {it['src']}.</i> " + stem
    note = None
    if teacher:
        note = (f"<b>Answer {ans_text(it)}</b> · Likely wrong: {it['wrong']} · "
                f"Target {it.get('t', 60)} s · {it['tag'][1]}, level {it['tag'][2]}")
    fig = fig_for(it["fig"]) if it.get("fig") else None
    d.question(num, stem, it["type"], options=it.get("opts"), figure=fig,
               work=WORK_SPACE[it["work"]], teacher=note)


# ============================================================================ Artifact 2: sheet
def build_sheet(teacher, start_page=1):
    kind = "SheetTeacher" if teacher else "SheetStudent"
    d = doc(kind, "Module 2 · In-class Sheet" + (" · Teacher Version" if teacher else ""), start_page=start_page)
    if teacher:
        d.text(ORIGINALITY, "teacher_small")
    d.learning_goal(MOD["goal"])
    for we in (C.WE1, C.WE2):
        d.heading(we["heading"], keep_with=K.example_box_height(len(we["lines"])))
        d.example_box(we["lines"])
    num = 1
    for block, title, blurb in C.SHEET_BLOCKS:
        items = [it for it in C.SHEET if it["block"] == block]
        first = items[0]
        first_h = d.question_height(first["stem"], first.get("opts"),
                                    fig_for(first["fig"]) if first.get("fig") else None, WORK_SPACE[first["work"]])
        if block == "exit":
            d.box("Strategy triggers:", C.TRIGGERS)
        if block == "stretch":
            d.challenge_label(keep_with=first_h)
            d.text(blurb, "small", keep_with=first_h)
        else:
            d.heading(title, keep_with=first_h)
            d.text(blurb, "small", keep_with=first_h)
        if teacher:
            d.text(C.TEACHER_TIMING[block], "teacher_small", keep_with=first_h)
        for it in items:
            render_item(d, num, it, teacher)
            num += 1
    return d.build()


# ============================================================================ Artifact 3: homework
def build_homework():
    d = doc("Homework", "Module 2 · Homework")
    d.learning_goal(MOD["goal"])
    d.text(f"<b>{C.HOMEWORK_TIME}</b> Work without a calculator. Circle one answer for each question. "
           "Then check with the answer strip and fill in the error log for every wrong answer.")
    for i, it in enumerate(C.HOMEWORK, 1):
        if it.get("challenge"):
            first_h = d.question_height(it["stem"], it["opts"], None, WORK_SPACE[it["work"]])
            d.challenge_label(keep_with=first_h)
        render_item(d, i, it, show_src=True)
    d.forced_break("answer_strip")
    d.heading("Self-check answer strip", keep_with=60)
    d.text("Final answers only. Fold this page under before you start; unfold it when you have finished.", "small")
    d.table([["Q"] + [str(i) for i in range(1, 11)], ["Answer"] + [it["key"] for it in C.HOMEWORK]],
            [2] + [1] * 10, style="body", header=True, bold_first_col=True)
    d.heading("Error log", keep_with=120)
    d.text("One row for every wrong answer. Codes: " +
           " · ".join(f"<b>{c}</b> {name}" for c, name, _ in ERROR_CODES), "small")
    rows = [["Q", "My answer", "Correct", "Code", "What I will do differently"]] + [[""] * 5 for _ in range(8)]
    d.table(rows, [1, 2, 2, 1.2, 7], row_heights=[None] + [K.ANSWER_LINE_HEIGHT] * 8)
    return d.build()


def build_solutions(start_page=1):
    d = doc("HomeworkSolutions", "Module 2 · Homework Full Solutions", start_page=start_page)
    d.text(ORIGINALITY, "teacher_small")
    d.text("Each solution follows the CM six-part standard: main solution · second method · faster contest method · "
           "concept tested · likely student mistake · extension question.", "small")
    for i, (it, sol) in enumerate(zip(C.HOMEWORK, C.HW_SOLUTIONS), 1):
        d.heading(f"{i}. Answer {ans_text(it)}", keep_with=4 * K.BODY_LEADING)
        d.text(f"<i>{it['kind']} · {it['src']}.</i> {it['stem']}", "small")
        parts = [
            ("Main solution", sol["main"]),
            ("Second method", sol["second"]),
            ("Faster contest method", it["fast"]),
            ("Concept tested", it["concept"]),
            ("Likely student mistake", it["wrong"]),
            ("Extension question", f"{it['ext']} <i>Answer:</i> {sol['ext_ans']}"),
        ]
        d.bullets([f"<b>{a}.</b> {b}" for a, b in parts])
    return d.build()


# ============================================================================ Artifact 4: drill book
def build_drill_book():
    sets, mixed = DR.build_sets()
    total, bad = DR.verify_all()
    assert not bad, bad
    d = CMDoc("Integer and Place-Value Fluency", GRADE, "GaussDrillIntegerPlaceValue", OUT)
    d.title_block("Drill Book · Gauss Contest Preparation · used from Module 2 all term")
    d.learning_goal("Answer every item correctly in under 30 seconds.")
    d.text("<b>How to use.</b> One set per sitting. Start a timer, work straight through, stop the timer, then mark "
           "with the tear-off key at the back. Write your score and time in the box. Record the code of your most "
           "frequent mistake in the progress tracker. Repeat a set until you are at 90% or better within the target time. "
           "Every item should take under 45 seconds; anything longer belongs in homework, not here.", "small")
    # Reference page (no worked examples)
    d.heading("Reference page", keep_with=200)
    d.figure(Figure("illustration", FG.place_value_chart(C.PV_HEAD, [7, 3, 5, 0, 9, 1, 2]), h=48))
    d.text("M millions · HTh hundred-thousands · TTh ten-thousands · Th thousands · H hundreds · T tens · O ones. "
           "Count places from the ones digit, in groups of three.", "small")
    ref = [
        ["Area", "Rule or fact"],
        ["Place value", "10<super>1</super> = 10, 10<super>2</super> = 100, 10<super>3</super> = 1 000, 10<super>6</super> = 1 000 000. "
                        "k × 10<super>p</super> is k followed by p zeros."],
        ["Comparing decimals", "Pad to the same number of places, then compare: 0.35 = 0.350 > 0.305."],
        ["Distance from 0", "Ignore the sign: −8.2 is 8.2 from 0. Farthest from 0 is not the same as smallest."],
        ["Adding integers", "a + (−b) = a − b. On a number line, + moves right, − moves left."],
        ["Subtracting integers", "a − (−b) = a + b. The distance between a and b is (larger) − (smaller)."],
        ["Crossing zero", "From −11 to 6 is 11 + 6 = 17: jump to 0, then jump on."],
        ["Time", "60 s = 1 min, 60 min = 1 h. Trade 60, never 100. Make the next hour first."],
        ["Money", "$1 = 100¢. Work in cents if the decimal point worries you."],
        ["Partner products", "2 × 5 = 10 · 4 × 25 = 100 · 8 × 125 = 1 000 · 2 × 50 = 100 · 5 × 20 = 100."],
        ["Factor out", "a × c + b × c = (a + b) × c. Look for a shared number before multiplying."],
        ["Compensation", "998 = 1 000 − 2 and 1 003 = 1 000 + 3: add the round parts, then the small parts."],
        ["Nines", "10<super>n</super> − 1 is n nines; its digit sum is 9n. 10<super>n</super> − 47 is (n − 2) nines then 53."],
        ["Die", "Faces 1 to 6 add to 21. Opposite faces add to 7."],
        ["Digit sum", "Add the digits; skip zeros; pair to 10 where you can."],
    ]
    d.table(ref, [1.3, 4])
    # Sets
    for s in sets:
        tier_txt = {1: "single step, clean numbers", 2: "two steps, contest-shaped numbers",
                    3: "reverse and multi-step"}[s["tier"]]
        first_h = d.question_height(s["items"][0]["stem"], area=K.ANSWER_LINE_HEIGHT)
        d.heading(f"Set {s['num']} — {tier_txt}", keep_with=3 * K.BODY_LEADING + first_h)
        d.score_box([f"Target {s['target']} min", "Time", "Score (of 20)"])
        for k, it in enumerate(s["items"], 1):
            d.question(k, it["stem"], "short")
    d.heading("Mixed final set — all three skill areas", keep_with=120)
    d.score_box([f"Target {DR.MIXED_TARGET} min", "Time", "Score (of 25)"])
    for k, it in enumerate(mixed, 1):
        d.question(k, it["stem"], "short")
    # Progress tracker
    d.heading("Progress tracker", keep_with=200)
    d.text("One row per attempt. Error code = the code of your most frequent mistake in that attempt: " +
           " · ".join(f"<b>{c}</b> {name}" for c, name, _ in ERROR_CODES), "small")
    rows = [["Date", "Set", "Score", "Time", "Most frequent error code"]] + [[""] * 5 for _ in range(14)]
    d.table(rows, [2, 1.5, 1.5, 1.5, 3], row_heights=[None] + [K.ANSWER_LINE_HEIGHT] * 14)
    # Tear-off answer key
    d.forced_break("tear_off")
    d.heading("Answer key — tear off along the binding before starting", keep_with=100)
    header = ["#"] + [f"Set {s['num']}" for s in sets] + ["Mixed"]
    rows = [header]
    for k in range(25):
        row = [str(k + 1)]
        for s in sets:
            row.append(s["items"][k]["ans"] if k < len(s["items"]) else "")
        row.append(mixed[k]["ans"])
        rows.append(row)
    d.table(rows, [0.6] + [1.5] * 7)
    path = d.build()
    return path, total, sets, mixed


# ============================================================================ Artifact 1: lesson plan
def build_lesson_plan():
    d = doc("LessonPlan", "Module 2 · Teacher Lesson Plan · Gauss Contest Preparation")
    d.text(ORIGINALITY, "teacher_small")
    d.heading("1. Module header", keep_with=120)
    d.table([["Field", "Value"],
             ["Module", f"{MOD['num']} — {MOD['title']}"],
             ["Hours · week", f"{MOD['hours']} h (two 90-minute lessons + one 60-minute extension) · Week {MOD['week']}"],
             ["Teaching mode", f"{MOD['mode']}: write and teach for speed and zero error"],
             ["Share of contest points", f"{MOD['share']} of observed Gauss G7 points (2021–2026 analysis)"],
             ["Curriculum", MOD["ontario"]],
             ["Canonical topics", MOD["canonical"]],
             ["Past-paper reference", f"Structures only, never printed: {CEMC_URL}"],
             ["Student goal", MOD["goal"]],
             ["Files", "Sheet (student/teacher) · Homework + answer strip + solutions · "
                       "Drill Book: Integer and Place-Value Fluency"]],
            [1.2, 4], bold_first_col=True)
    d.heading("2. Why this module carries this weight")
    d.text(C.WHY)
    d.heading("3. Prerequisites")
    d.text(f"<b>Earlier modules.</b> {C.PREREQ['modules']}")
    d.text(f"<b>Five-minute check.</b> {C.PREREQ['check']}")
    d.heading("4. Lesson breakdown", keep_with=140)
    for name, rows in (("Lesson A (90 min)", C.LESSON_A), ("Lesson B (90 min)", C.LESSON_B),
                       ("Extension session (60 min)", C.EXTENSION)):
        d.subheading(name, keep_with=120)
        d.table([["Min", "Phase", "What happens"]] + [list(r) for r in rows], [0.8, 1.6, 6])
    d.heading("5. Teaching scripts for the worked examples")
    d.text("Scripts are in second person to you; student lines are in quotes. Pause means wait — silence is the tool.",
           "small")
    d.subheading(C.WE1["heading"])
    d.bullets([
        "<b>Board:</b> write only the problem. <b>Say:</b> “Pencils down. You have ten seconds to look, not to calculate. "
        "What do you notice?” <b>Pause</b> the full ten seconds.",
        "<b>Listen for three levels.</b> Not yet: “36 times 7 is 252…” → “Hold that. What is the same in both products?” "
        "Developing: “They both have a 7.” → “What could you do with that 7?” Secure: “36 and 64 make 100, so it’s 700.” "
        "→ “Prove it. Write the regrouped line.”",
        "<b>Ask:</b> “Why is (36 + 64) × 7 the same as 36 × 7 + 64 × 7?” Draw 7 rows of dots split into a block of 36 "
        "and a block of 64. Expected: “Seven rows of 36 and seven rows of 64 make seven rows of 100.”",
        "<b>Decision point:</b> if a student cannot say why, stay on the array; do not move to Q5–6 on faith.",
        "<b>Check move:</b> “Estimate each product. Does 700 make sense?” (about 250 + 450).",
        "<b>Name the trigger</b> and point to the strategy box: two products sharing a number → factor it out. "
        "Hand the pen to the student for Q6.",
    ], "small")
    d.subheading(C.WE2["heading"])
    d.bullets([
        "<b>Split the room</b> (or, one-to-one, time the student twice). Half use Method A (calculate both sums), half use "
        "Method B (pairs). <b>Say:</b> “Go — hands up when done.” Record both times on the board.",
        "<b>Ask Method A:</b> “How did you get 650 for the evens?” Listen for 2 × (1 + … + 25). If a student added "
        "term by term, note the time and do not correct yet.",
        "<b>Ask Method B:</b> “How many pairs? How do you know it is 25, not 24 or 50?” <b>Pause.</b> This is the "
        "counting decision; a student who says 50 has counted terms, not pairs.",
        "<b>Compare:</b> “Both answers are 25. Which method would you use at 30 seconds a question?” Expected secure "
        "answer: “Pairs — one count, no big additions.”",
        "<b>Transfer question:</b> “What if the evens went to 52 and the odds to 51?” (26 pairs → 26). "
        "Name the lesson: when two lists line up term by term, subtract in pairs.",
    ], "small")
    d.heading("6. Misconceptions (probe first, then correct)", keep_with=120)
    d.table([["Misconception", "Probing question (student must say the reasoning aloud)", "Correction"]] +
            [list(m) for m in C.MISCONCEPTIONS], [2, 2.4, 2.8])
    d.heading("7. Hint ladders for challenge items")
    d.text("Give one level at a time. The student writes the level used (H1, H2, H3) beside the item; "
           "log it in the error log so progress shows as fewer hints, not only more correct answers.", "small")
    ladders = [(f"Sheet Q{i}", it) for i, it in enumerate(C.SHEET, 1) if it.get("hints")]
    ladders += [(f"Homework Q{i}", it) for i, it in enumerate(C.HOMEWORK, 1) if it.get("hints")]
    d.table([["Item", "H1 — reread, name a constraint", "H2 — a representation, no calculation",
              "H3 — one intermediate relationship"]] + [[lab] + it["hints"] for lab, it in ladders], [1, 2.3, 2.3, 2.3])
    d.heading("8. Differentiation")
    d.text(f"<b>Struggling.</b> {C.DIFFERENTIATION['struggling']}")
    d.text(f"<b>On-level.</b> {C.DIFFERENTIATION['onlevel']}")
    d.text(f"<b>Advanced.</b> {C.DIFFERENTIATION['advanced']}")
    d.heading("9. Per-item teacher notes", keep_with=150)
    d.subheading("In-class sheet", keep_with=120)
    rows = [["Q", "Answer", "Concept tested", "Likely error", "Faster contest method"]]
    for i, it in enumerate(C.SHEET, 1):
        rows.append([str(i), ans_text(it), it["concept"], it["wrong"], it["fast"]])
    d.table(rows, [0.5, 1.3, 2, 2.4, 2.8])
    d.subheading("Homework", keep_with=120)
    rows = [["Q", "Answer", "Concept tested", "Likely error", "Faster contest method"]]
    for i, it in enumerate(C.HOMEWORK, 1):
        rows.append([str(i), ans_text(it), f"<i>{it['kind']}.</i> {it['concept']}", it["wrong"], it["fast"]])
    d.table(rows, [0.5, 1.3, 2, 2.4, 2.8])
    d.text("Drill book: answers are on its tear-off key. Drill items carry no teacher notes by design — they are "
           "fluency repetitions, not problems.", "small")
    d.heading("10. Exit check and parent update")
    d.text("<b>Lesson A exit:</b> (1) 25 × 37 × 4 = 3 700. (2) −6.5 is farther from 0 than 6.05. "
           "<b>Lesson B exit:</b> Sheet Q17–18 (17 000; 4 000 with a compensation explanation). "
           "Pass mark for moving on: 2/2 on both exits and 90% on Drill Set 2 inside 6 minutes; otherwise repeat "
           "Drill Sets 1–2 in the extension session before Set 3.")
    d.text(f"<b>Parent update line:</b> “{C.PARENT_LINE}”")
    return d.build()


def main():
    out = {}
    out["lesson_plan"] = build_lesson_plan()
    import pymupdf
    s = build_sheet(False)
    t = build_sheet(True)
    out["sheet_student"], out["sheet_teacher"] = s, t
    t2 = build_sheet(True, start_page=len(pymupdf.open(s)) + 1)
    out["sheet_combined"] = merge([s, t2], os.path.join(OUT, K.get_filename(GRADE, FT + "SheetCombined", 1, 2026, 9)))
    h = build_homework()
    sol = build_solutions()
    out["homework"], out["solutions"] = h, sol
    sol2 = build_solutions(start_page=len(pymupdf.open(h)) + 1)
    out["homework_combined"] = merge([h, sol2], os.path.join(OUT, K.get_filename(GRADE, FT + "HomeworkCombined", 1, 2026, 9)))
    out["drill"], n_checked, _, _ = build_drill_book()
    for k, v in out.items():
        print(k, v)
    print("drill items independently checked:", n_checked)


if __name__ == "__main__":
    main()
