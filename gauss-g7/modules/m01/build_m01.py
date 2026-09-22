"""Build all Module 1 artifacts: lesson plan, Diagnostic Form A (+ key, combined), persistence rubric,
strategy card, error log template, placement report template."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
from common import (OUT, GRADE, ORIGINALITY, ERROR_CODES, CORE_MOVES, PACING, CEMC_URL,  # noqa: E402
                    CONTEST_FORMAT)
import cm_pdf as K  # noqa: E402
from cm_pdf import CMDoc, Figure, WORK_SPACE, merge  # noqa: E402
import cm_figures as FG  # noqa: E402
import content as C  # noqa: E402

MOD = C.MODULE
TOPIC = MOD["topic_title"]
FT = "GaussM01Orientation"
LETTERS = "ABCDE"
METHOD_LABEL = "Method box — a correct diagram, table or equation earns points even if the answer is wrong."


PART_DIR = os.path.join(OUT, ".parts")   # second halves of combined files (page numbers continue)


def doc(kind, subtitle, start_page=1):
    d = CMDoc(TOPIC, GRADE, FT + kind, PART_DIR if start_page > 1 else OUT, start_page=start_page)
    d.title_block(subtitle)
    return d


def fig_for(key):
    if key == "L_shape":
        return Figure("diagram", FG.polygon([(0, 0), (10, 0), (10, 5), (6, 5), (6, 8), (0, 8)],
                                            side_labels=[(0, "10"), (1, "5"), (3, "3"), (4, "6"), (5, "8")]), h=140)
    if key == "angles":
        return Figure("diagram", FG.angles_on_line([54, 84, 42], ["54°", "2x°", "x°"], "O"), h=110)
    raise KeyError(key)


def points(i):
    for _, a, b, p in C.TIERS:
        if a <= i <= b:
            return p


def ans_text(it):
    if it.get("opts"):
        return f"({it['key']}) {it['opts'][LETTERS.index(it['key'])]}"
    return it["key"]


# ============================================================================ Diagnostic Form A
def build_diagnostic():
    d = doc("DiagnosticFormA", "Entrance Diagnostic · Form A")
    d.table([["Name", "", "Date", ""]], [1, 3, 1, 2], style="body", header=False,
            row_heights=[K.ANSWER_LINE_HEIGHT], bold_first_col=True)
    d.text("<b>60 minutes. No calculator.</b> 25 questions in three parts. Questions 1–10 are worth 2 points, "
           "11–20 are worth 5 points and 21–25 are worth 6 points (100 points in total). For questions 1–20, circle "
           "one answer and write its letter on the line or in the box. For questions 21–25, write your answer on the "
           "answer line. Where you see a method box, show your diagram, table or equation: it can earn points even if "
           "your final answer is wrong. Diagrams in this paper are drawn to scale. Skip a question if you are stuck "
           "and come back to it.")
    for name, a, b, p in C.TIERS:
        first = C.DIAG[a - 1]
        fh = d.question_height(first["stem"], first.get("opts"), fig_for(first["fig"]) if first.get("fig") else None,
                               K.ANSWER_LINE_HEIGHT)
        if name == "Challenge":
            d.challenge_label(keep_with=fh)
            d.text(f"Part 3 — Challenge. Questions {a}–{b}, {p} points each. Write your answer on the line.",
                   "small", keep_with=fh)
        else:
            d.heading(f"Part {'1' if a == 1 else '2'} — {name}. Questions {a}–{b}, {p} points each.", keep_with=fh)
        for i in range(a, b + 1):
            it = C.DIAG[i - 1]
            fig = fig_for(it["fig"]) if it.get("fig") else None
            if p == 2:
                d.question(i, it["stem"], "mcq", options=it["opts"], figure=fig)
            elif p == 5:
                if it.get("method"):
                    d.question(i, it["stem"], "word_problem", options=it["opts"], figure=fig,
                               work=WORK_SPACE["std"], method_field=METHOD_LABEL, answer_blank=True)
                else:
                    d.question(i, it["stem"], "word_problem", options=it["opts"], figure=fig,
                               work=WORK_SPACE["line"], answer_blank=True)
            else:
                d.question(i, it["stem"], "multi_step", figure=fig, work=WORK_SPACE["long"],
                           method_field=METHOD_LABEL, answer_blank=True)
    return d.build()


def build_diagnostic_key(start_page=1):
    d = doc("DiagnosticFormAKey", "Entrance Diagnostic · Form A · Marking Key", start_page=start_page)
    d.text(ORIGINALITY, "teacher_small")
    d.heading("Answers and points", keep_with=120)
    rows = [["Q", "Strand", "Points", "Answer", "Q", "Strand", "Points", "Answer"]]
    half = 13
    for k in range(half):
        row = []
        for i in (k + 1, k + 1 + half):
            if i <= 25:
                it = C.DIAG[i - 1]
                row += [str(i), it["s"], str(points(i)), ans_text(it)]
            else:
                row += ["", "", "", ""]
        rows.append(row)
    d.table(rows, [0.5, 0.9, 0.8, 1.6, 0.5, 0.9, 0.8, 1.6], style="body")
    d.text("Strand codes: " + " · ".join(f"<b>{k}</b> {v}" for k, v in C.STRAND_NAMES.items()) +
           ". Blueprint: N 6 · A 4 · G 6 · D 3 · T 4 · L 2 items.", "small")
    d.heading("Figure notes", keep_with=60)
    d.text("Q15 and Q16 are drawn to scale. Q15's missing sides (4 cm and 3 cm) are not labelled on purpose: finding "
           "them is part of the item. Q16's angles are 54°, 84° and 42° as drawn.", "small")
    d.heading("Partial-credit rules", keep_with=100)
    d.bullets([
        "<b>Questions 1–10 (2 points).</b> Correct letter: 2. Otherwise 0. No partial credit.",
        "<b>Questions 11–20 (5 points).</b> Correct letter: 5. On items with a method box, when the letter is wrong or "
        "blank: 3 points for a correct representation with a single arithmetic slip; 2 points for a correct "
        "representation that stops or goes wrong later; 0 otherwise. Items without a method box: 5 or 0.",
        "<b>Questions 21–25 (6 points).</b> Correct answer: 6. Otherwise: 2 points for a correct representation, "
        "4 points for a correct representation plus the key intermediate result below; 0 otherwise.",
        "Score the persistence rubric on its own sheet. Never add or subtract persistence points here.",
    ], "small")
    rows = [["Q", "Correct representation (2)", "Adds to 3 (5-pt) / 4 (6-pt)"]]
    for i, it in enumerate(C.DIAG, 1):
        if it.get("method") or points(i) == 6:
            rows.append([str(i), it["rep"], it.get("slip") or it.get("inter")])
    d.table(rows, [0.5, 3.5, 3])
    d.heading("Per-item teacher notes", keep_with=120)
    rows = [["Q", "Answer", "Concept tested", "Likely error", "Faster method"]]
    for i, it in enumerate(C.DIAG, 1):
        rows.append([str(i), ans_text(it), it["concept"], it["wrong"], it["fast"]])
    d.table(rows, [0.5, 1.3, 2.2, 2.4, 2.6])
    return d.build()


# ============================================================================ Persistence rubric
def build_rubric():
    d = doc("PersistenceRubric", "Persistence Observation Rubric · used during the Entrance Diagnostic")
    d.text(ORIGINALITY, "teacher_small")
    d.text("Score each behaviour 0, 1 or 2 from what you observe during the 60-minute diagnostic. Total out of 12. "
           "<b>This score is recorded separately and never changes the mathematical score.</b> It informs the "
           "placement conversation and the student's first-term goals.")
    d.table([["Name", "", "Date", "", "Observer", ""]], [1, 2.5, 0.8, 1.5, 1.2, 2], style="body",
            header=False, row_heights=[K.ANSWER_LINE_HEIGHT], bold_first_col=True)
    rows = [["Behaviour", "0", "1", "2", "Score"]]
    for name, a, b, c in C.PERSISTENCE:
        rows.append([f"<b>{name}</b>", a, b, c, ""])
    rows.append(["<b>Total (out of 12)</b>", "", "", "", ""])
    d.table(rows, [1.6, 2, 2, 2, 0.8])
    d.heading("Neutral-hint protocol", keep_with=80)
    d.text("Offer at most one neutral hint per student, only after 3 minutes without progress on one item. A neutral "
           "hint contains no mathematics. Use one of: " + " · ".join(C.NEUTRAL_HINTS) +
           " Record the item number and the response. Score behaviour 6 from that response; if no hint was needed, "
           "score behaviour 6 as ‘not observed’ and total out of 10, noting this on the placement report.")
    d.heading("Evidence notes", keep_with=100)
    d.table([["Item(s)", "What you saw"]] + [["", ""] for _ in range(6)], [1, 5],
            row_heights=[None] + [K.ANSWER_LINE_HEIGHT] * 6)
    return d.build()


# ============================================================================ Strategy card (double-sided)
def build_strategy_card():
    d = doc("StrategyCard", "Student Strategy Card · keep this all term")
    d.subheading("Side 1 — The six core moves", keep_with=100)
    rows = [["Move", "Reach for it when you see…", "Do this"]]
    for m, trig, do in CORE_MOVES:
        rows.append([f"<b>{m}</b>", trig, do])
    d.table(rows, [1.7, 2.5, 2.6], style="body")
    d.subheading("How Gauss is scored", keep_with=80)
    d.table([["Part", "Questions", "Points each", "Part total"],
             ["A", "1–10", "5", "50"], ["B", "11–20", "6", "60"], ["C", "21–25", "8", "40"],
             ["All", "25", "", "150"]], [1, 1.5, 1.5, 1.5], style="body")
    d.text("Parts A and B hold 110 of the 150 points (73%). Bank them first.", "bold")
    d.forced_break("card_side")
    d.subheading("Side 2 — Error codes", keep_with=100)
    rows = [["Code", "Name", "It means…"]] + [[f"<b>{c}</b>", n, m] for c, n, m in ERROR_CODES]
    d.table(rows, [0.8, 2, 4.5], style="body")
    d.subheading("Pacing model (60 minutes)", keep_with=100)
    rows = [["Part", "Time", "Per question", "Rule"]] + [list(r) for r in PACING]
    d.table(rows, [1.6, 0.9, 1.6, 3.5], style="body")
    d.text("Stuck for more than twice the per-question time? Mark it ‘?’, move on, come back in the check window.",
           "bold")
    return d.build()


# ============================================================================ Error log template
def build_error_log():
    d = doc("ErrorLog", "Error Log · fill in after every set and every mock")
    d.text("One row for every question you got wrong. Choose the one code that best explains the error. "
           "Codes: " + " · ".join(f"<b>{c}</b> {n}" for c, n, _ in ERROR_CODES) + ".", "small")
    rows = [["Date / set", "Q", "My answer", "Correct answer", "Code", "What I will do differently"]]
    rows += [[""] * 6 for _ in range(28)]
    d.table(rows, [1.4, 0.6, 1.1, 1.1, 0.7, 4], row_heights=[None] + [K.ANSWER_LINE_HEIGHT] * 28)
    return d.build()


# ============================================================================ Placement report template
def build_placement():
    d = doc("PlacementReport", "Placement Report · Entrance Diagnostic Form A")
    d.text(ORIGINALITY, "teacher_small")
    d.table([["Student", "", "Date", ""], ["Tutor", "", "Form", "A"]], [1, 3, 1, 2], style="body", header=False,
            row_heights=[K.ANSWER_LINE_HEIGHT] * 2, bold_first_col=True)
    d.subheading("Mathematical score (out of 100)", keep_with=100)
    d.table([["Section", "Questions", "Maximum", "Score"],
             ["Foundations", "1–10", "20", ""], ["Problem solving", "11–20", "50", ""],
             ["Challenge", "21–25", "30", ""], ["<b>Total</b>", "", "<b>100</b>", ""]], [2, 1.5, 1.5, 1.5], style="body")
    d.subheading("Strand profile", keep_with=100)
    rows = [["Strand", "Questions", "Maximum", "Score"]]
    for k, v in C.STRAND_NAMES.items():
        qs = [i for i, it in enumerate(C.DIAG, 1) if it["s"] == k]
        rows.append([f"{k} — {v}", ", ".join(map(str, qs)), str(sum(points(i) for i in qs)), ""])
    d.table(rows, [3, 2, 1, 1], style="small")
    d.subheading("Persistence observation (recorded separately, out of 12)", keep_with=80)
    d.table([["Score", "Strongest behaviour", "Behaviour to build"], ["", "", ""]], [1, 3, 3], style="body",
            row_heights=[None, K.ANSWER_LINE_HEIGHT])
    d.subheading("Pathway (tick one)", keep_with=100)
    rows = [["", "Pathway", "Score", "What it means"]] + [["☐", f"<b>{n}</b>", r, m] for n, r, m in C.PATHWAYS]
    d.table(rows, [0.4, 1.8, 1, 5], style="body")
    d.text(f"<b>Please note:</b> {C.CAVEAT}", "bold")
    d.subheading("Most frequent error codes on the diagnostic", keep_with=60)
    d.table([[c for c, _, _ in ERROR_CODES], [""] * 8], [1] * 8, style="body", row_heights=[None, K.ANSWER_LINE_HEIGHT])
    d.fill_lines("Tutor notes (two strengths, two targets for the first four weeks):", 3)
    d.fill_lines("Summary for parents (one sentence):", 1)
    return d.build()


# ============================================================================ Lesson plan
def build_lesson_plan():
    d = doc("LessonPlan", "Module 1 · Teacher Lesson Plan · Gauss Contest Preparation")
    d.text(ORIGINALITY, "teacher_small")
    d.heading("1. Module header", keep_with=120)
    d.table([["Field", "Value"],
             ["Module", f"{MOD['num']} — {MOD['title']}"],
             ["Hours · week", f"{MOD['hours']} h (two 90-minute lessons, no extension) · Week {MOD['week']}"],
             ["Teaching mode", MOD["mode"]],
             ["Share of contest points", "Non-content module. It places students and installs the tools every later "
                                         "module uses."],
             ["Curriculum", MOD["ontario"]],
             ["Contest", f"{CONTEST_FORMAT} Reference: {CEMC_URL}"],
             ["Student goal", MOD["goal"]],
             ["Files", "Entrance Diagnostic Form A + marking key · Persistence Observation Rubric · Student Strategy "
                       "Card · Error Log Template · Placement Report Template"]],
            [1.2, 4], bold_first_col=True)
    d.heading("2. Why this module carries this weight")
    d.text("Three hours, no content points — because every later hour depends on it. The diagnostic places each "
           "student on a pathway before content teaching starts, the error log turns every later mistake into data, "
           "and the six core moves are the vocabulary the lesson plans for Modules 2–20 use. Teach this for "
           "<b>accurate placement and habits</b>, not for speed or depth. The one number to land: Parts A and B hold "
           "110 of 150 points (73%).")
    d.heading("3. Prerequisites")
    d.text("<b>Earlier modules:</b> none. Grade 6 mathematics is assumed. <b>Five-minute check</b> (oral, before the "
           "diagnostic): “Have you written a maths contest before? What do you do when you are stuck?” and one warm-up: "
           "“What is 25% of 60?” (15). The purpose is to settle nerves and hear how the student talks about being "
           "stuck; record the answer on the rubric's evidence notes.")
    d.heading("4. Lesson breakdown", keep_with=140)
    for name, rows in (("Lesson A (90 min) — format, scoring, diagnostic", C.LESSON_A),
                       ("Lesson B (90 min) — core moves, error classification, error log", C.LESSON_B)):
        d.subheading(name, keep_with=120)
        d.table([["Min", "Phase", "What happens"]] + [list(r) for r in rows], [0.8, 1.6, 6])
    d.text("Lesson A cannot follow the standard 10/15/20/25/10/10 cycle because the diagnostic needs an unbroken "
           "60 minutes. Lesson B follows the standard cycle.", "small")
    d.heading("5. Content sections and scripts")
    d.subheading("5a. Contest format and the 5/6/8 scoring geometry")
    d.text(CONTEST_FORMAT, "small")
    d.bullets([
        "<b>Say:</b> “Gauss has 25 questions and 60 minutes. Before I tell you the points — which part do you think is "
        "worth the most?” <b>Pause.</b> Most students say Part C.",
        "<b>Build the table on the board with the student:</b> A 10 × 5 = 50, B 10 × 6 = 60, C 5 × 8 = 40. "
        "<b>Ask:</b> “What fraction of the points is in A and B together?” Expected secure answer: 110 of 150, "
        "about three-quarters.",
        "<b>Decision point:</b> if the student still wants to spend most time on Part C, ask: “A perfect Part C and "
        "nothing else — what score? A perfect A and half of B?” (40 vs 80).",
        "<b>Pacing:</b> hand out the Strategy Card and read the pacing model aloud: 15 / 25 / 15 / 5 minutes.",
    ], "small")
    d.subheading("5b. Administering and scoring the diagnostic")
    d.bullets([
        "Materials: paper, pencils, eraser, scrap paper. No calculator. A clock the student can see.",
        "<b>Say exactly:</b> “This is not a test you pass or fail. It shows me what to teach you first. Do what you "
        "can, skip what you can't, and show your thinking in the method boxes — they earn points.”",
        "Start the timer. Warnings at 30 and 50 minutes only. Observe with the persistence rubric; give at most one "
        "neutral hint (rubric sheet protocol).",
        "Score with the marking key: 2/5/6 points, partial credit only as the key states. Fill the strand profile "
        "and total on the placement report before Lesson B.",
        "Never discuss the score during Lesson A. The first conversation about results is the error-classification "
        "conversation in Lesson B.",
    ], "small")
    d.subheading("5c. The error-classification conversation")
    d.text("For each wrong item, follow this order. The student chooses the code; you only ask.", "small")
    d.bullets([
        "<b>Re-attempt cold.</b> “Try this one again now, no help.” If it is now right, ask “What changed?”: "
        "misread → <b>Q</b>; calculation → <b>A</b>; ran out of time → <b>T</b>; “I remembered how” → <b>K</b>.",
        "<b>Still wrong?</b> Ask “What is the question asking?” If the student cannot say → <b>Q</b>.",
        "<b>Can say it but cannot start?</b> Ask “What could you draw or tabulate?” No idea → <b>R</b>; draws it and "
        "then solves → <b>S</b> (the move was available but not chosen).",
        "<b>Has a plan but the idea is wrong</b> (e.g. adds successive percents) → <b>C</b>.",
        "<b>Misread or trusted a figure</b> → <b>V</b>.",
        "Close each item with: “Next time I will…” — the student writes it in the last column of the Error Log.",
    ], "small")
    d.subheading("5d. Setting up the error log")
    d.bullets([
        "Give the student the Error Log Template. Model the first row yourself from a diagnostic item.",
        "Rule: one row per wrong answer, one code per row, and a ‘what I will do differently’ that is an action "
        "(“draw a bar model before calculating”), not a feeling (“be more careful”).",
        "The log is reviewed at the start of every extension session and before every mock (Modules 19–20).",
    ], "small")
    d.subheading("5e. The six core moves — script with original mini-examples")
    rows = [["Move", "Mini-example (say it, board it)", "Model solution", "What student answers sound like"]]
    for m, ex, sol, lev in C.MOVE_SCRIPTS:
        rows.append([f"<b>{m}</b>", ex, sol, lev])
    d.table(rows, [1.6, 2.2, 2.2, 2.6])
    d.text("For each move: read the problem, <b>pause 20 seconds</b>, ask “Which move?”, then let the student run it "
           "before you model. Hand the pen over for the last three moves.", "small")
    d.heading("6. Misconceptions (probe first, then correct)", keep_with=120)
    d.table([["Misconception", "Probing question", "Correction"]] + [list(m) for m in C.MISCONCEPTIONS], [2.2, 2.2, 2.8])
    d.heading("7. Hint ladders for the challenge items (Lesson B review only)", keep_with=120)
    d.text("Not used during the diagnostic itself. In Lesson B, give one level at a time; the student records the "
           "level used (H1, H2, H3) in the error log.", "small")
    rows = [["Item", "H1 — reread, name a constraint", "H2 — a representation, no calculation",
             "H3 — one intermediate relationship"]]
    for i, it in enumerate(C.DIAG, 1):
        if it.get("hints"):
            rows.append([f"Diagnostic Q{i}"] + it["hints"])
    d.table(rows, [1, 2.3, 2.3, 2.3])
    d.heading("8. Differentiation")
    d.text("<b>Struggling</b> (anxious or below 50 on the diagnostic): in Lesson B re-work only Part 1 misses first, with "
           "smaller numbers (e.g. Q12 with 16 marbles), then return to the original. Teach three moves (draw, tabulate, "
           "work backward) deeply before the other three.")
    d.text("<b>On-level:</b> full Lesson B; error-classify every wrong item; attempt two challenge items with the hint "
           "ladder.")
    d.text("<b>Advanced</b> (85+): every challenge item re-done with a second method and a one-line completeness "
           "argument (e.g. why Q25's list has no missing cases); Part C extension: how many three-digit numbers have "
           "digit sum 10?")
    d.heading("9. Per-item teacher notes (Entrance Diagnostic Form A)", keep_with=120)
    d.text("Full notes, partial-credit rules and representation criteria are in the marking key file. Summary:", "small")
    rows = [["Q", "Pts", "Strand", "Answer", "Concept", "Likely error"]]
    for i, it in enumerate(C.DIAG, 1):
        rows.append([str(i), str(points(i)), it["s"], ans_text(it), it["concept"], it["wrong"]])
    d.table(rows, [0.5, 0.5, 0.9, 1.3, 2.4, 2.7])
    d.heading("10. Exit check and parent update")
    d.text("<b>Lesson A exit:</b> the reflection slip (easiest, hardest, one answer to change). "
           "<b>Lesson B exit:</b> (1) “Which part of Gauss holds the most points?” (B, 60). (2) “Give the error code: "
           "you knew 15% of 80 but wrote 8 because you read it as 10%.” (Q). Both right, and a first error-log row in "
           "the student's own words, means the toolkit is installed.")
    d.text("<b>Parent update line:</b> “[Child] completed the Gauss entrance diagnostic and set up an error log; "
           "strongest at ___; we will focus first on ___ (placement: ___ pathway).”")
    return d.build()


def main():
    out = {}
    out["lesson_plan"] = build_lesson_plan()
    import pymupdf
    p = build_diagnostic()
    k = build_diagnostic_key()
    out["diagnostic"], out["diagnostic_key"] = p, k
    k2 = build_diagnostic_key(start_page=len(pymupdf.open(p)) + 1)
    out["diagnostic_combined"] = merge([p, k2], os.path.join(OUT, K.get_filename(GRADE, FT + "DiagnosticFormACombined",
                                                                                 1, 2026, 9)))
    out["rubric"] = build_rubric()
    out["strategy_card"] = build_strategy_card()
    out["error_log"] = build_error_log()
    out["placement"] = build_placement()
    for kk, v in out.items():
        print(kk, v)


if __name__ == "__main__":
    main()
