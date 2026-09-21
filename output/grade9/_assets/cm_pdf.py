"""cm_pdf.py — Concept Mastery shared ReportLab layer (Grade 9 question bank).

Implements skill-cm-layout-branding Sections 1–17 verbatim (page geometry,
palette, typography, header/footer, title block, learning goal, example box,
spacing, question flow, item labels) as a wrapping, flow-based renderer.

Design notes / deviations, all deliberate and flagged:
  * The layout skill's draw_* helpers use single-line drawString. Grade 9 word
    problems wrap, so every text block is rendered through a ReportLab
    Paragraph (word-wrap + <super>/<sub> for exponents, per layout §3 which
    mandates markup tags, never Unicode glyphs). Paragraph leading is set to
    the skill's per-line heights so vertical rhythm is unchanged.
  * Question-number column = 30pt (toolkit QUESTION_NUMBER_WIDTH and the
    qa-checklist "≥30pt column, no stem overlap" gate). Layout §17 QNUM_W=20 is
    the SUB-ITEM (a./b.) indent measured *inside* the number column — a
    different measurement — so both hold: stems start at CONTENT_X+30, lettered
    sub-items hang at CONTENT_X+30 with their content at CONTENT_X+30+20.
  * logo_missing → blank region (toolkit delivery rule), never a warning box.
  * Grade rules table caps at Grade 8; Grade 9 is treated as an extension of
    the Grade 8 rule (example required, learning goal on, challenge allowed).
"""
__version__ = "1.0.0-g9"

import os
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

# ── SECTION 1 — Page setup (layout skill, verbatim) ──────────────────────────
PAGE_WIDTH   = 8.5 * 72
PAGE_HEIGHT  = 11.0 * 72
MARGIN_TOP    = 0.75 * 72
MARGIN_BOTTOM = 0.75 * 72
MARGIN_LEFT   = 0.875 * 72
MARGIN_RIGHT  = 0.75 * 72
CONTENT_WIDTH = PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT
CONTENT_X     = MARGIN_LEFT
CONTENT_TOP_Y = PAGE_HEIGHT - MARGIN_TOP
CONTENT_BOT_Y = MARGIN_BOTTOM

# ── SECTION 2 — Brand colors (verbatim) ──────────────────────────────────────
CM_BLUE     = HexColor("#1A3E6E")
CM_NAVY     = HexColor("#1A3A8F")
CM_ORANGE   = HexColor("#E8394A")
CM_YELLOW   = HexColor("#F5A623")
CM_MED_BLUE = HexColor("#2D7DD2")
CM_SKY      = HexColor("#B3E8F5")
CM_WHITE    = HexColor("#FFFFFF")
CM_GREY     = HexColor("#CCCCCC")
CM_DARK_GREY= HexColor("#555555")

# ── SECTION 3 — Typography (verbatim sizes; DejaVuSans family only) ───────────
_ASSET_DIR = os.path.dirname(os.path.abspath(__file__))
_DEJAVU     = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
_DEJAVU_B   = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
_DEJAVU_O   = os.path.join(_ASSET_DIR, "DejaVuSans-Oblique.ttf")  # synthesized

pdfmetrics.registerFont(TTFont("DejaVuSans", _DEJAVU))
pdfmetrics.registerFont(TTFont("DejaVuSans-Bold", _DEJAVU_B))
pdfmetrics.registerFont(TTFont("DejaVuSans-Oblique", _DEJAVU_O))
# Map <b>/<i>/<sub>/<super> inside Paragraphs to DejaVu variants — otherwise
# ReportLab falls back to Helvetica and breaks the "DejaVuSans only" rule.
pdfmetrics.registerFontFamily("DejaVuSans", normal="DejaVuSans",
                              bold="DejaVuSans-Bold", italic="DejaVuSans-Oblique",
                              boldItalic="DejaVuSans-Bold")

FONT_PAGE_TITLE    = ("DejaVuSans-Bold", 16)
FONT_LEARNING_GOAL = ("DejaVuSans-Oblique", 10)
FONT_SECTION_LABEL = ("DejaVuSans-Bold", 11)
FONT_BODY          = ("DejaVuSans", 11)
FONT_BODY_BOLD     = ("DejaVuSans-Bold", 11)
FONT_SMALL         = ("DejaVuSans", 9)
FONT_FOOTER        = ("DejaVuSans", 8)

# ── SECTION 4/5 — Header logo + footer geometry (verbatim) ───────────────────
LOGO_PATH   = os.path.join(_ASSET_DIR, "logo.png")
LOGO_H      = 43
LOGO_W      = 120
LOGO_MARGIN = 6
HEADER_HEIGHT = max(28, LOGO_H + LOGO_MARGIN * 2)
FOOTER_HEIGHT = 18

# ── SECTION 6/13 — Spacing constants (verbatim) ──────────────────────────────
GAP_AFTER_HEADER        = 16
GAP_AFTER_PAGE_TITLE    = 10
GAP_AFTER_LEARNING_GOAL = 10
GAP_AFTER_EXAMPLE_BOX   = 24
GAP_AFTER_SECTION_LABEL = 8
GAP_BETWEEN_QUESTIONS   = 23
LINE_SPACING_WITHIN_QUESTION = 20
GAP_BEFORE_FOOTER       = 16
ANSWER_LINE_HEIGHT      = 36
BOTTOM_LIMIT            = MARGIN_BOTTOM

# ── SECTION 9 — Example box constants (verbatim) ─────────────────────────────
EXAMPLE_BOX_PADDING = 10
EXAMPLE_BOX_RADIUS  = 6
EX_PAD_TOP   = 10
EX_LABEL_H   = 14
EX_GAP_LABEL = 6
EX_LINE_H    = 15
EX_PAD_BOTTOM= 10

# ── SECTION 11/17 — Question flow constants ──────────────────────────────────
QUESTION_NUMBER_WIDTH = 30   # top-level number column (toolkit + qa gate ≥30)
QNUM_W = 20                  # layout §17 sub-item indent (inside the column)
WORD_PROBLEM_WORK_SPACE = 80
SHORT_BLANK_W = 120

# ── Paragraph styles ─────────────────────────────────────────────────────────
def _style(name, font, size, color, leading, align=TA_LEFT, space_after=0):
    return ParagraphStyle(name, fontName=font, fontSize=size, textColor=color,
                          leading=leading, alignment=align, spaceAfter=space_after)

ST_BODY   = _style("body",   "DejaVuSans",      11, CM_DARK_GREY, 15)
ST_BODY_B = _style("bodyb",  "DejaVuSans-Bold", 11, CM_DARK_GREY, 15)
ST_SMALL  = _style("small",  "DejaVuSans",       9, CM_DARK_GREY, 12)
ST_ITALIC = _style("ital",   "DejaVuSans-Oblique",10, CM_MED_BLUE, 14)
ST_LABEL  = _style("label",  "DejaVuSans-Bold", 11, CM_MED_BLUE, 15)
ST_HEAD   = _style("head",   "DejaVuSans-Bold", 12, CM_BLUE, 16)
ST_EXLINE = _style("exline", "DejaVuSans",      11, CM_DARK_GREY, EX_LINE_H)
ST_EXLABEL= _style("exlabel","DejaVuSans-Bold", 11, CM_MED_BLUE, EX_LABEL_H)


class CMFlow:
    """Flow renderer: header/footer per page, cursor, keep-together ensure()."""

    def __init__(self, out_path, topic_title, subtitle=None, info_line=None,
                 name_date=False, grade_badge=None, meta_right=None,
                 logo_missing_silent=True):
        self.out_path = out_path
        self.topic_title = topic_title      # footer-left + page-1 title (topic only)
        self.subtitle = subtitle
        self.info_line = info_line          # e.g. "MTH1W · Class — Guided Practice"
        self.name_date = name_date
        self.grade_badge = grade_badge      # e.g. "Grade 9" (exams only)
        self.meta_right = meta_right        # list of lines under badge (exams)
        self.logo_missing_silent = logo_missing_silent
        self.c = canvas.Canvas(out_path, pagesize=(PAGE_WIDTH, PAGE_HEIGHT))
        self.c.setTitle(topic_title)
        self.page_num = 0
        self.y = None
        self._page1_done = False

    # ---- page scaffolding -----------------------------------------------------
    def _draw_header(self):
        logo_x = PAGE_WIDTH - MARGIN_RIGHT - LOGO_W
        logo_y = PAGE_HEIGHT - LOGO_MARGIN - LOGO_H
        if os.path.exists(LOGO_PATH):
            self.c.drawImage(ImageReader(LOGO_PATH), logo_x, logo_y,
                             width=LOGO_W, height=LOGO_H,
                             preserveAspectRatio=True, mask="auto")
        # missing -> blank region (delivery rule), no box

    def _draw_footer(self):
        text_y = MARGIN_BOTTOM / 2 - 3
        self.c.setFillColor(CM_DARK_GREY)
        self.c.setFont(*FONT_FOOTER)
        self.c.drawString(MARGIN_LEFT, text_y, self.topic_title)
        self.c.drawCentredString(PAGE_WIDTH / 2, text_y,
                                 "Copyright © 2026 by Concept Mastery")
        self.c.drawRightString(PAGE_WIDTH - MARGIN_RIGHT, text_y, str(self.page_num))

    def _new_page(self):
        if self.page_num > 0:
            self.c.showPage()
        self.page_num += 1
        self._draw_header()
        self._draw_footer()
        self.y = CONTENT_TOP_Y - GAP_AFTER_HEADER

    def start(self):
        self._new_page()
        self._title_block()

    def ensure(self, height):
        if self.y - height < BOTTOM_LIMIT:
            self._new_page()

    # ---- measured paragraph primitive ----------------------------------------
    def _para(self, text, style, width=None, x=None, ensure=True, gap=0):
        width = width if width is not None else CONTENT_WIDTH
        x = x if x is not None else CONTENT_X
        p = Paragraph(text, style)
        w, h = p.wrap(width, 100000)
        if ensure:
            self.ensure(h + gap)
        p.drawOn(self.c, x, self.y - h)
        self.y -= (h + gap)
        return h

    def _measure(self, text, style, width):
        p = Paragraph(text, style)
        _, h = p.wrap(width, 100000)
        return p, h

    def space(self, h):
        self.y -= h

    # ---- SECTION 7b — title block (page 1 only) ------------------------------
    def _title_block(self):
        self.c.setFillColor(CM_BLUE)
        self.c.setFont(*FONT_PAGE_TITLE)
        self.c.drawCentredString(PAGE_WIDTH / 2, self.y, self.topic_title)
        self.y -= 16 + GAP_AFTER_PAGE_TITLE
        if self.subtitle:
            self.c.setFillColor(CM_MED_BLUE)
            self.c.setFont(*FONT_LEARNING_GOAL)
            self.c.drawCentredString(PAGE_WIDTH / 2, self.y, self.subtitle)
            self.y -= 10 + GAP_AFTER_LEARNING_GOAL
        if self.grade_badge:
            self.c.setFillColor(CM_BLUE)
            self.c.setFont("DejaVuSans-Bold", 10)
            self.c.drawCentredString(PAGE_WIDTH / 2, self.y, self.grade_badge)
            self.y -= 10 + 6
        if self.meta_right:
            self.c.setFillColor(CM_DARK_GREY)
            self.c.setFont("DejaVuSans", 10)
            self.c.drawCentredString(PAGE_WIDTH / 2, self.y, "   ·   ".join(self.meta_right))
            self.y -= 10 + 8
        if self.info_line:
            self.c.setFillColor(CM_MED_BLUE)
            self.c.setFont("DejaVuSans", 9)
            self.c.drawCentredString(PAGE_WIDTH / 2, self.y, self.info_line)
            self.y -= 9 + 8
        if self.name_date:
            self.c.setFillColor(CM_DARK_GREY)
            self.c.setFont(*FONT_BODY)
            line_y = self.y - 4
            self.c.drawString(CONTENT_X, line_y, "Name:")
            self.c.setStrokeColor(CM_GREY); self.c.setLineWidth(0.5)
            self.c.line(CONTENT_X + 42, line_y - 2, CONTENT_X + 250, line_y - 2)
            self.c.drawString(CONTENT_X + 300, line_y, "Date:")
            self.c.line(CONTENT_X + 338, line_y - 2, CONTENT_X + CONTENT_WIDTH, line_y - 2)
            self.y -= 22

    # ---- SECTION 8 — learning goal -------------------------------------------
    def learning_goal(self, text):
        if not text:
            return
        self._para(f"Goal: {text}", ST_ITALIC, gap=GAP_AFTER_LEARNING_GOAL)

    # ---- generic heading / directions ----------------------------------------
    def heading(self, text, color=CM_BLUE):
        st = _style("h", "DejaVuSans-Bold", 12, color, 16)
        # keep heading with at least the next ~40pt of content
        self._para(text, st, gap=GAP_AFTER_SECTION_LABEL)

    def directions(self, text):
        self._para(text, ST_BODY, gap=10)

    def body(self, text, style=None, gap=8, x=None, width=None):
        self._para(text, style or ST_BODY, gap=gap, x=x, width=width)

    # ---- SECTION 9 — example box (worked, wraps safely) ----------------------
    def example_box(self, solution_lines, label="Example:"):
        if isinstance(solution_lines, str):
            solution_lines = [solution_lines]
        inner_w = CONTENT_WIDTH - 2 * EXAMPLE_BOX_PADDING
        # measure wrapped content
        paras = []
        content_h = 0
        for line in solution_lines:
            p, h = self._measure(line, ST_EXLINE, inner_w)
            paras.append((p, h)); content_h += h
        box_h = EX_PAD_TOP + EX_LABEL_H + EX_GAP_LABEL + content_h + EX_PAD_BOTTOM
        self.ensure(box_h + GAP_AFTER_EXAMPLE_BOX)
        top = self.y
        self.c.setFillColor(CM_SKY)
        self.c.setStrokeColor(CM_MED_BLUE)
        self.c.setLineWidth(1)
        self.c.roundRect(CONTENT_X, top - box_h, CONTENT_WIDTH, box_h,
                         EXAMPLE_BOX_RADIUS, stroke=1, fill=1)
        label_y = top - EX_PAD_TOP - EX_LABEL_H + 3
        self.c.setFillColor(CM_MED_BLUE)
        self.c.setFont(*FONT_SECTION_LABEL)
        self.c.drawString(CONTENT_X + EXAMPLE_BOX_PADDING, label_y, label)
        line_y = top - EX_PAD_TOP - EX_LABEL_H - EX_GAP_LABEL
        for p, h in paras:
            p.drawOn(self.c, CONTENT_X + EXAMPLE_BOX_PADDING, line_y - h)
            line_y -= h
        self.y = top - box_h - GAP_AFTER_EXAMPLE_BOX

    # ---- SECTION 11 — numbered question --------------------------------------
    def question(self, num, stem, level=None, marks=None, answer="work",
                 sub_items=None, work_pts=None, num_prefix=None):
        """answer in {'work','short','lines','none'}.
        sub_items: list of (label, text, answer) tuples rendered as a./b./...
        """
        stem_x = CONTENT_X + QUESTION_NUMBER_WIDTH
        stem_w = CONTENT_WIDTH - QUESTION_NUMBER_WIDTH
        # tag suffix (level + marks) right-aligned on first stem line region
        tag = ""
        if marks is not None:
            tag = f"  [{marks}]"
        stem_full = stem + (f" <font color='#2D7DD2'><b>{tag.strip()}</b></font>" if tag else "")
        # measure stem
        p_stem, h_stem = self._measure(stem_full, ST_BODY, stem_w)
        # estimate needed height for keep-together (stem + one answer unit)
        ans_h = self._answer_height(answer, sub_items, work_pts)
        self.ensure(h_stem + ans_h + GAP_BETWEEN_QUESTIONS)
        # draw number
        self.c.setFillColor(CM_DARK_GREY)
        self.c.setFont(*FONT_BODY)
        label = num_prefix if num_prefix else f"{num}."
        self.c.drawString(CONTENT_X, self.y - 11, label)
        # draw stem
        p_stem.drawOn(self.c, stem_x, self.y - h_stem)
        self.y -= h_stem
        # sub items
        if sub_items:
            for lab, txt, _a in sub_items:
                sub_x = stem_x
                content_x = stem_x + QNUM_W
                p_sub, h_sub = self._measure(txt, ST_BODY, stem_w - QNUM_W)
                self.ensure(h_sub + 6)
                self.c.setFillColor(CM_DARK_GREY); self.c.setFont(*FONT_BODY)
                self.c.drawString(sub_x, self.y - 11, lab)
                p_sub.drawOn(self.c, content_x, self.y - h_sub)
                self.y -= h_sub + 4
            self.y -= (GAP_BETWEEN_QUESTIONS - 4)
        else:
            self._draw_answer(answer, work_pts, stem_x)
            self.y -= GAP_BETWEEN_QUESTIONS

    def _answer_height(self, answer, sub_items, work_pts):
        if sub_items:
            return 24 * len(sub_items)
        if answer == "work":
            return (work_pts or WORD_PROBLEM_WORK_SPACE)
        if answer == "short":
            return ANSWER_LINE_HEIGHT - 14
        if answer == "lines":
            return ANSWER_LINE_HEIGHT - 14
        return 6

    def _draw_answer(self, answer, work_pts, stem_x):
        if answer == "none":
            self.y -= 4
            return
        if answer == "work":
            self.y -= (work_pts or WORD_PROBLEM_WORK_SPACE)
            return
        if answer == "short":
            self.y -= 6
            self.c.setStrokeColor(CM_GREY); self.c.setLineWidth(0.5)
            self.c.line(stem_x, self.y, stem_x + SHORT_BLANK_W, self.y)
            self.y -= (ANSWER_LINE_HEIGHT - 20)
            return
        if answer == "lines":
            self.y -= 6
            self.c.setStrokeColor(CM_GREY); self.c.setLineWidth(0.5)
            self.c.line(stem_x, self.y, CONTENT_X + CONTENT_WIDTH, self.y)
            self.y -= (ANSWER_LINE_HEIGHT - 20)
            return

    # ---- answer-key / solution entry -----------------------------------------
    def key_entry(self, num, lines):
        """Answer-key row: bold number, then wrapped solution lines."""
        if isinstance(lines, str):
            lines = [lines]
        stem_x = CONTENT_X + QUESTION_NUMBER_WIDTH
        stem_w = CONTENT_WIDTH - QUESTION_NUMBER_WIDTH
        paras = [self._measure(l, ST_BODY, stem_w) for l in lines]
        total = sum(h for _, h in paras)
        self.ensure(total + 10)
        self.c.setFillColor(CM_BLUE); self.c.setFont(*FONT_BODY_BOLD)
        self.c.drawString(CONTENT_X, self.y - 11, f"{num}.")
        for p, h in paras:
            p.drawOn(self.c, stem_x, self.y - h)
            self.y -= h
        self.y -= 8

    def build(self):
        self.c.showPage()   # close the final page (footer already drawn on it)
        self.c.save()
        return self.out_path
