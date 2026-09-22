# Gauss Grade 7 programme — Sprint 0 build report (M1 + M2)

Rebuild everything: `./build_all.sh` (verifies answers → builds → figure colour audit → QA on every PDF).
Toolkit: `scripts/cm_pdf.py` v1.0.0 and `scripts/cm_figures.py` v1.0.0. The skill's `cm_pdf.py` was a skeleton and has been completed here.

## Files (output/)

| File | Pages | Items |
|---|---|---|
| M1 Lesson Plan | 7 | — (six core-move scripts, 7 misconceptions, 5 hint ladders) |
| M1 Entrance Diagnostic Form A | 8 | 25 (10 × 2 pts, 10 × 5 pts, 5 × 6 pts = 100); 11 method boxes |
| M1 Diagnostic Marking Key | 3 | 25 answers, partial-credit criteria for 11 items |
| M1 Diagnostic Combined | 11 | paper + key, continuous page numbers |
| M1 Persistence Observation Rubric | 2 | 6 behaviours × 0–2 = 12 |
| M1 Student Strategy Card | 2 (double-sided) | 6 moves, 8 error codes, pacing model |
| M1 Error Log Template | 2 | 28 rows |
| M1 Placement Report Template | 2 | 4 pathways + unpiloted-threshold caveat |
| M2 Lesson Plan | 7 | per-item notes for 18 sheet + 10 homework items |
| M2 Sheet — student | 5 | 2 worked examples, 6 guided, 8 independent, 2 stretch, 5 triggers, 2 exit = 18 numbered |
| M2 Sheet — teacher | 5 | same 18 + answers, likely wrong answer, timing, cut list |
| M2 Sheet — combined | 10 | |
| M2 Homework (+ answer strip + error log) | 3 (2 + 1) | 10 (3 retrieval, 4 current, 2 interleaved, 1 challenge) |
| M2 Homework Solutions | 4 | 10 × six-part solutions |
| M2 Homework Combined | 7 | |
| Drill Book — Integer and Place-Value Fluency | 20 | 6 × 20 + 25 mixed = 145 items |

## Verification (answers solved a second time, by a different method)
- `modules/m02/verify.py`: 28/28 sheet + homework items recomputed by brute force, string manipulation, datetime or exact fractions; for every multiple-choice item exactly one option matches. Worked examples and extension answers are checked too.
- `modules/m01/verify.py`: 25/25 diagnostic items recomputed (permutation search for the logic items, enumeration for counting and probability); blueprint 6/4/6/3/4/2 and the 20/50/30 point split are asserted.
- `drills/integer_pv.py`: 147 generated drill items, each recomputed by an independent checker; 0 mismatches. The generator also rejects degenerate items (where the misconception gives the right answer) and items that repeat a sheet item.

## QA
- Content gate (olympiad skill §10): one correct answer per item (verified above); principal distractor recorded with its error; difficulty tagged 1–5, sheet opens at 1 and ends at 4; median at 1–2 (Part A, Mode A). **Gap:** only the main distractor per item has a written reason; the others are arithmetic-slip values without individual notes.
- `scripts/qa_pdf.py` (extended from the skill script): 16/16 files pass, 16–18 checks each (page size, title block, footer zones, sequential page numbers, logo on every page, text inside content area, duplicate stems within the file and against companion files, file name per layout §16, DejaVuSans only and embedded, no JS or links).
- `scripts/figure_audit.py`: every figure cropped at 300 dpi; 0 coloured pixels (black and white only).
- Render–inspect cycles: M2 sheet 3 · homework 2 · solutions 3 · M2 lesson plan 2 · drill book 2 · diagnostic 3 · key 2 · strategy card 2 · M1 lesson plan 3 · rubric, error log, placement 1 each.

## Checks that fail by design, or are only partly met
- Layout §11 says never mix question types on one page. Continuous flow (§11c) puts short-answer and multiple-choice items on the same page of the sheet and the diagnostic. Not fixed.
- Layout §9 says one example box on every worksheet page. Worked examples are per section; continued pages have none. Not fixed; §9 contradicts §11c.
- QA §4 (KDP grayscale): brand-colour chrome is in colour. The figures are black and white. A KDP black-and-white edition needs a grey chrome palette, which no skill defines.

## Conflicts resolved
- Brand skill vs layout skill (hex values, Arial, footer rules): followed the layout skill, as instructed.
- Question-number column: layout §11 says 20pt; the toolkit and QA skills say at least 30pt because 20pt overlapped. Used 30pt for question numbers and QNUM_W = 20 for sub-items.
- Challenge glyph: DejaVuSans has no ⭐ (U+2B50), so ★ (U+2605) is used.
- Figure colours: layout §14b uses CM_SKY/CM_MED_BLUE; the programme rule is black and white. Followed the programme rule.
- Tip box is banned (layout §10): the strategy-trigger box uses example-box geometry with its own label.
- The skill's `qa_pdf.py` file-name regex predates layout §16. The extended copy uses §16.
- Footer fit: the full module titles collide with the centred copyright at 8pt. Title and footer use "Integers, Place Value and Arithmetic" and "Contest Mindset and Diagnostic"; the lesson-plan header shows the full titles.

## Gaps
- **Past-paper references:** there are no per-item "cf. 20xx Gauss G7 Qn" references. cemc.uwaterloo.ca is blocked by this environment's egress proxy, so question numbers could not be checked. Files link to https://cemc.uwaterloo.ca/contests/gauss only. The programme's own analysis sheet can supply the mapping.
- **Gauss rules:** the format (25 questions, 60 minutes, 5/6/8 points, maximum 150) was confirmed only through search results. The calculator and blank-answer rules are marked "confirm on the current CEMC page".
- **Ontario codes:** strand-level only (B1/B2; Strand A for M1). The curriculum skill has no verified Grade 7 expectation rows.
- **M2 structure coverage:** "ordering powers of ten" is tested only through expanded form (Sheet Q11 and drills). There is no dedicated compare-powers item.
- **Retrieval items:** M2 homework retrieval and interleaving draw on M1, which has no content. They use M1 strategy content (scoring, small case, work backward, eliminate options).
- **Lesson A of M1** breaks the 10/15/20/25/10/10 cycle because the diagnostic needs 60 unbroken minutes. Lesson B follows the cycle.

## Constants not found in any skill (derived in `cm_pdf.py`, marked DERIVED)
Body leading (= EX_LINE_H), 9pt leading, paragraph gap, table cell padding and grid style, minimum figure label size (FONT_SMALL), footer-left/copyright minimum gap, work-space sizes above 80pt, five-option layout, teacher-overlay colour (CM_ORANGE), and an artifact-type token in the §16 file name (encoded in the Topic token, for example `GaussM02IntegersSheetTeacher`).

## Toolkit primitives landed (Sprint 0 track)
Page furniture, question flow with keep-together, five-option layout, method-credit fields, forms and grids, score box, combined files with continuous page numbers, number line (ticks, points, jumps), place-value chart. Pulled forward for the diagnostic: labelled polygon (with a not-to-scale flag) and angles-on-a-line.
