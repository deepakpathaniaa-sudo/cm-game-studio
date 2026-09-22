"""cm_pdf.py — Concept Mastery shared ReportLab layer.

Completed from the skill-cm-reportlab-toolkit skeleton (0.1.0) against
skill-cm-layout-branding. The LAYOUT block below is the constants block of that
skill, values unchanged. Anything the layout skill does not define is marked
DERIVED (computed from layout constants) or TOOLKIT (owned by the toolkit
skill) — nothing else is invented here. Content scripts import from this file
and never define a layout value of their own.
"""
__version__ = "1.0.0"

import os
import re
import json

from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.utils import ImageReader

_HERE = os.path.dirname(os.path.abspath(__file__))

# =============================================================================
# LAYOUT — skill-cm-layout-branding §1–§17 (values verbatim)
# =============================================================================
# §1 Page setup
PAGE_WIDTH = 8.5 * 72
PAGE_HEIGHT = 11.0 * 72
MARGIN_TOP = 0.75 * 72
MARGIN_BOTTOM = 0.75 * 72
MARGIN_LEFT = 0.875 * 72
MARGIN_RIGHT = 0.75 * 72
CONTENT_WIDTH = PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT
CONTENT_X = MARGIN_LEFT
CONTENT_TOP_Y = PAGE_HEIGHT - MARGIN_TOP
CONTENT_BOT_Y = MARGIN_BOTTOM

# §2 Colours
CM_BLUE = HexColor("#1A3E6E")
CM_NAVY = HexColor("#1A3A8F")
CM_ORANGE = HexColor("#E8394A")
CM_YELLOW = HexColor("#F5A623")
CM_MED_BLUE = HexColor("#2D7DD2")
CM_SKY = HexColor("#B3E8F5")
CM_WHITE = HexColor("#FFFFFF")
CM_GREY = HexColor("#CCCCCC")
CM_DARK_GREY = HexColor("#555555")

# §3 Typography
FONT_HEADER_BRAND = ("DejaVuSans", 8)
FONT_HEADER_GRADE = ("DejaVuSans-Bold", 9)
FONT_PAGE_TITLE = ("DejaVuSans-Bold", 16)
FONT_LEARNING_GOAL = ("DejaVuSans-Oblique", 10)
FONT_SECTION_LABEL = ("DejaVuSans-Bold", 11)
FONT_BODY = ("DejaVuSans", 11)
FONT_BODY_BOLD = ("DejaVuSans-Bold", 11)
FONT_SMALL = ("DejaVuSans", 9)
FONT_FOOTER = ("DejaVuSans", 8)

# §4 Header
LOGO_PATH = os.path.join(_HERE, "logo.png")
LOGO_H = 43
LOGO_W = 120
LOGO_MARGIN = 6
HEADER_HEIGHT = max(28, LOGO_H + LOGO_MARGIN * 2)

# §5 Footer
FOOTER_HEIGHT = 18
COPYRIGHT = "Copyright © 2026 by Concept Mastery"

# §6 / §13 Spacing
GAP_AFTER_HEADER = 16
GAP_AFTER_PAGE_TITLE = 10
GAP_AFTER_LEARNING_GOAL = 10
GAP_AFTER_EXAMPLE_BOX = 24
GAP_AFTER_TIP_BOX = 12
GAP_AFTER_SECTION_LABEL = 8
LINE_SPACING_WITHIN_QUESTION = 20
GAP_BETWEEN_QUESTIONS = 23
GAP_BEFORE_FOOTER = 16
ANSWER_LINE_HEIGHT = 36

# §9 Example box
EXAMPLE_BOX_PADDING = 10
EXAMPLE_BOX_RADIUS = 6
EX_PAD_TOP = 10
EX_LABEL_H = 14
EX_GAP_LABEL = 6
EX_LINE_H = 15
EX_PAD_BOTTOM = 10

# §10 Tip box (retained for reference only — layout §10 forbids calling it)
TIP_BOX_PADDING = 8
TIP_BOX_RADIUS = 4

# §11 Practice questions
QUESTION_NUM_WIDTH = 20
WORD_PROBLEM_WORK_SPACE = 80
SHORT_BLANK_W = 120
BOTTOM_LIMIT = MARGIN_BOTTOM
VALID_Q_TYPES = {"mcq", "short", "word_problem", "multi_step"}

# §14 Images / figure blocks
IMAGE_SIZES = {
    "diagram": {"max_w": 200, "max_h": 150},
    "illustration": {"max_w": 300, "max_h": 200},
    "icon": {"max_w": 40, "max_h": 40},
    "number_line": {"max_w": 400, "max_h": 60},
    "grid": {"max_w": 250, "max_h": 250},
}
IMAGE_PADDING_ABOVE = 6
IMAGE_PADDING_BELOW = 12
IMAGE_MAX_SPACE_PCT = 0.90
IMAGE_ALIGNMENT = {
    "diagram": "left",
    "illustration": "center",
    "icon": "left",
    "number_line": "center",
    "grid": "center",
}

# §14b figure stroke weight (shape library line width)
FIGURE_LINE_W = 1.2

# §17 Item labels
QNUM_W = 20

# §15 Grade rules
GRADE_RULES = {
    1: {"max_questions": 6, "example_required": True, "learning_goal": False, "challenge": False, "tip_box": False},
    2: {"max_questions": 6, "example_required": True, "learning_goal": False, "challenge": False, "tip_box": True},
    3: {"max_questions": 6, "example_required": True, "learning_goal": True, "challenge": True, "tip_box": True},
    4: {"max_questions": 8, "example_required": True, "learning_goal": True, "challenge": True, "tip_box": True},
    5: {"max_questions": 8, "example_required": True, "learning_goal": True, "challenge": True, "tip_box": True},
    6: {"max_questions": 10, "example_required": True, "learning_goal": True, "challenge": True, "tip_box": True},
    7: {"max_questions": 10, "example_required": True, "learning_goal": True, "challenge": True, "tip_box": True},
    8: {"max_questions": 10, "example_required": True, "learning_goal": True, "challenge": True, "tip_box": True},
}

# =============================================================================
# TOOLKIT-owned values (skill-cm-reportlab-toolkit)
# =============================================================================
# Production rule: 20pt overlapped two-digit numbers with stems. Supersedes
# layout §11 QUESTION_NUM_WIDTH for top-level question numbers only; QNUM_W
# (20) still governs sub-item indentation (layout §17).
QUESTION_NUMBER_WIDTH = 30

# =============================================================================
# DERIVED — values the layout skill does not define, computed from it
# =============================================================================
BODY_LEADING = EX_LINE_H                                     # body line pitch = example-box line pitch
SMALL_LEADING = EX_LINE_H * FONT_SMALL[1] / FONT_BODY[1]     # same ratio at 9pt
PARA_GAP = GAP_AFTER_SECTION_LABEL                           # gap between paragraphs
CELL_PAD = TIP_BOX_PADDING / 2                               # table cell padding
FOOTER_MIN_GAP = GAP_AFTER_HEADER                            # min gap footer-left ↔ copyright
FIGURE_LABEL_FONT = FONT_SMALL                               # minimum label size inside figures
WORK_SPACE = {                                               # open working space presets
    "none": 0,
    "line": ANSWER_LINE_HEIGHT,
    "std": WORD_PROBLEM_WORK_SPACE,
    "long": 2 * WORD_PROBLEM_WORK_SPACE,
    "xlong": 3 * WORD_PROBLEM_WORK_SPACE,
}
CHALLENGE_LABEL = "★ Challenge"   # layout §12 asks for U+2B50; DejaVuSans lacks it, U+2605 is the nearest glyph

# =============================================================================
# Fonts
# =============================================================================
_FONT_DIRS = [os.path.join(_HERE, "fonts"), "/usr/share/fonts/truetype/dejavu"]


def _register_fonts():
    for name in ("DejaVuSans", "DejaVuSans-Bold", "DejaVuSans-Oblique"):
        if name in pdfmetrics.getRegisteredFontNames():
            continue
        for d in _FONT_DIRS:
            p = os.path.join(d, name + ".ttf")
            if os.path.exists(p):
                pdfmetrics.registerFont(TTFont(name, p))
                break
        else:
            raise FileNotFoundError(f"{name}.ttf not found in {_FONT_DIRS}")
    pdfmetrics.registerFontFamily("DejaVuSans", normal="DejaVuSans", bold="DejaVuSans-Bold",
                                  italic="DejaVuSans-Oblique", boldItalic="DejaVuSans-Bold")


_register_fonts()


def _style(name, font, color, leading=None, **kw):
    return ParagraphStyle(name, fontName=font[0], fontSize=font[1],
                          leading=leading or BODY_LEADING, textColor=color, **kw)


STYLES = {
    "body": _style("body", FONT_BODY, CM_DARK_GREY),
    "bold": _style("bold", FONT_BODY_BOLD, CM_DARK_GREY),
    "small": _style("small", FONT_SMALL, CM_DARK_GREY, SMALL_LEADING),
    "small_bold": _style("small_bold", ("DejaVuSans-Bold", FONT_SMALL[1]), CM_BLUE, SMALL_LEADING),
    "label": _style("label", FONT_SECTION_LABEL, CM_BLUE),
    "sub": _style("sub", FONT_SECTION_LABEL, CM_MED_BLUE),
    "goal": _style("goal", FONT_LEARNING_GOAL, CM_MED_BLUE),
    "teacher": _style("teacher", FONT_BODY, CM_ORANGE),
    "teacher_small": _style("teacher_small", FONT_SMALL, CM_ORANGE, SMALL_LEADING),
    "challenge": _style("challenge", FONT_SECTION_LABEL, CM_ORANGE),
    "center": _style("center", FONT_BODY, CM_DARK_GREY, alignment=1),
}


def validate_layout_constants():
    """Layout §18a."""
    assert GAP_AFTER_EXAMPLE_BOX == 24
    assert QNUM_W == 20
    assert WORD_PROBLEM_WORK_SPACE == 80
    assert LOGO_W == 120 and LOGO_H == 43
    assert BOTTOM_LIMIT == MARGIN_BOTTOM
    assert QUESTION_NUMBER_WIDTH >= 30
    assert GAP_BETWEEN_QUESTIONS >= 23 and LINE_SPACING_WITHIN_QUESTION >= 20 and ANSWER_LINE_HEIGHT >= 36


def get_filename(grade, topic, version, year, month):
    """Layout §16 — CM_G[Grade]_Math_[Topic]_v[Version]_[YYYY-MM].pdf"""
    topic_clean = topic.replace(" ", "")
    assert re.fullmatch(r"[A-Za-z0-9]+", topic_clean), f"Topic token must be CamelCase alphanumeric: {topic}"
    return f"CM_G{grade}_Math_{topic_clean}_v{version}_{year}-{month:02d}.pdf"


def example_box_height(n_lines):
    """Layout §9 formula (content lines × EX_LINE_H + fixed padding)."""
    return EX_PAD_TOP + EX_LABEL_H + EX_GAP_LABEL + n_lines * EX_LINE_H + EX_PAD_BOTTOM


_SUP_MAP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹ⁿ", "0123456789n")
_SUP_RE = re.compile("[⁰¹²³⁴⁵⁶⁷⁸⁹ⁿ]+")


def sup(text):
    """Layout §3: superscripts via <super> markup, never Unicode glyphs."""
    return _SUP_RE.sub(lambda m: f"<super>{m.group(0).translate(_SUP_MAP)}</super>", text)


class Figure:
    """A vector figure block. `draw(c, x, y_bottom, w, h)` draws inside the box.
    w/h are clamped to IMAGE_SIZES[img_type]; alignment comes from IMAGE_ALIGNMENT."""

    def __init__(self, img_type, draw, w=None, h=None, caption=None):
        lim = IMAGE_SIZES[img_type]
        self.img_type = img_type
        self.draw = draw
        self.w = min(w or lim["max_w"], lim["max_w"])
        self.h = min(h or lim["max_h"], lim["max_h"])
        self.caption = caption

    def block_height(self):
        return IMAGE_PADDING_ABOVE + self.h + IMAGE_PADDING_BELOW


class CMDoc:
    """One PDF. Cursor-based continuous flow (layout §11b/§11c)."""

    def __init__(self, topic_title, grade, file_topic, out_dir, version=1, year=2026, month=9,
                 logo_missing_silent=True, doc_title=None, start_page=1):
        validate_layout_constants()
        self.rules = GRADE_RULES[grade]
        self.topic_title, self.grade = topic_title, grade
        self.logo_missing_silent = logo_missing_silent
        self._check_footer_fit()
        self.filename = get_filename(grade, file_topic, version, year, month)
        os.makedirs(out_dir, exist_ok=True)
        self.path = os.path.join(out_dir, self.filename)
        self.c = canvas.Canvas(self.path, pagesize=(PAGE_WIDTH, PAGE_HEIGHT),
                                  initialFontName=FONT_BODY[0], initialFontSize=FONT_BODY[1])
        self.c.setTitle(doc_title or topic_title)
        self.c.setAuthor("Concept Mastery")
        self.page_num = start_page - 1     # >1 only for the second part of a combined file
        self.start_page = start_page
        self.y = None
        self.figure_log = []      # (page, x0, y0, x1, y1) in PDF points, for colour audit
        self.questions = []       # every rendered question, for validation/QA
        self._page_open = False
        self._new_page()

    # ------------------------------------------------------------------ page furniture
    def _check_footer_fit(self):
        lw = pdfmetrics.stringWidth(self.topic_title, *FONT_FOOTER)
        cw = pdfmetrics.stringWidth(COPYRIGHT, *FONT_FOOTER)
        assert CONTENT_X + lw + FOOTER_MIN_GAP <= PAGE_WIDTH / 2 - cw / 2, \
            f"Footer-left '{self.topic_title}' collides with copyright; shorten topic_title"

    def _draw_header(self):
        c = self.c
        logo_x = PAGE_WIDTH - MARGIN_RIGHT - LOGO_W
        logo_y = PAGE_HEIGHT - LOGO_MARGIN - LOGO_H
        if os.path.exists(LOGO_PATH):
            c.drawImage(ImageReader(LOGO_PATH), logo_x, logo_y, width=LOGO_W, height=LOGO_H,
                        preserveAspectRatio=True, anchor="ne", mask="auto")
        elif not self.logo_missing_silent:
            c.setStrokeColor(CM_ORANGE)
            c.setFillColor(CM_YELLOW)
            c.rect(logo_x, logo_y, LOGO_W, LOGO_H, stroke=1, fill=1)
        # silent: region left blank (math-workbook production rule)

    def _draw_footer(self):
        c = self.c
        text_y = MARGIN_BOTTOM / 2 - 3
        c.setFillColor(CM_DARK_GREY)
        c.setFont(*FONT_FOOTER)
        c.drawString(MARGIN_LEFT, text_y, self.topic_title)
        c.drawCentredString(PAGE_WIDTH / 2, text_y, COPYRIGHT)
        c.drawRightString(PAGE_WIDTH - MARGIN_RIGHT, text_y, str(self.page_num))

    def _new_page(self):
        if self._page_open:
            self.c.showPage()
        self.page_num += 1
        self._draw_header()
        self._draw_footer()   # footer drawn before content/showPage (brand bug-fix rule)
        self._page_open = True
        self.y = CONTENT_TOP_Y - GAP_AFTER_HEADER

    def ensure(self, height):
        """Keep-together: start a new page if `height` will not fit (layout §11c)."""
        if self.y - height < BOTTOM_LIMIT:
            self._new_page()
            if self.y - height < BOTTOM_LIMIT:
                raise ValueError(f"Block of height {height:.0f}pt cannot fit on one page")

    def remaining(self):
        return self.y - BOTTOM_LIMIT

    def forced_break(self, reason):
        """Only for answer keys / answer strips / tear-off pages (layout §11c)."""
        assert reason in ("answer_key", "answer_strip", "tear_off", "card_side"), reason
        self._new_page()

    def space(self, h):
        if self.y - h < BOTTOM_LIMIT:
            self._new_page()
        else:
            self.y -= h

    # ------------------------------------------------------------------ text primitives
    @staticmethod
    def para(text, style="body", width=CONTENT_WIDTH):
        st = STYLES[style] if isinstance(style, str) else style
        p = Paragraph(sup(text), st)
        _, h = p.wrap(width, 10 ** 6)
        return p, h

    @staticmethod
    def para_lines(p):
        return len(p.blPara.lines)

    def title_block(self, subtitle=None):
        """Layout §7b — page 1 only, topic name only."""
        assert self.page_num == self.start_page
        c = self.c
        self.y -= FONT_PAGE_TITLE[1]
        c.setFillColor(CM_BLUE)
        c.setFont(*FONT_PAGE_TITLE)
        c.drawCentredString(PAGE_WIDTH / 2, self.y, self.topic_title)
        self.y -= GAP_AFTER_PAGE_TITLE
        if subtitle:
            self.y -= FONT_LEARNING_GOAL[1]
            c.setFillColor(CM_MED_BLUE)
            c.setFont(*FONT_LEARNING_GOAL)
            c.drawCentredString(PAGE_WIDTH / 2, self.y, subtitle)
            self.y -= GAP_AFTER_LEARNING_GOAL

    def learning_goal(self, text):
        """Layout §8 — 'Goal:' prefix, wraps if long."""
        if not text:
            return
        p, h = self.para(f"Goal: {text}", "goal")
        self.ensure(h)
        p.drawOn(self.c, CONTENT_X, self.y - h)
        self.y -= h + GAP_AFTER_LEARNING_GOAL

    def text(self, text, style="body", indent=0, gap=PARA_GAP, keep_with=0):
        """Flowing paragraph; splits across pages at line boundaries."""
        width = CONTENT_WIDTH - indent
        st = STYLES[style] if isinstance(style, str) else style
        text = sup(text)
        p = Paragraph(text, st)
        _, h = p.wrap(width, 10 ** 6)
        if h + keep_with <= self.remaining():
            p.drawOn(self.c, CONTENT_X + indent, self.y - h)
            self.y -= h + gap
            return
        first_line = st.leading
        if self.remaining() < first_line + keep_with:
            self._new_page()
            return self.text(text, style, indent, gap, keep_with)
        parts = p.split(width, self.remaining())
        if len(parts) < 2:
            self._new_page()
            return self.text(text, style, indent, gap, keep_with)
        for i, part in enumerate(parts):
            _, ph = part.wrap(width, 10 ** 6)
            if i > 0:
                self._new_page()
            part.drawOn(self.c, CONTENT_X + indent, self.y - ph)
            self.y -= ph
        self.y -= gap

    def heading(self, text, keep_with=3 * BODY_LEADING, style="label"):
        """Numbered/section heading; never orphaned (reserves keep_with below it)."""
        p, h = self.para(text, style)
        self.ensure(h + GAP_AFTER_SECTION_LABEL + keep_with)
        p.drawOn(self.c, CONTENT_X, self.y - h)
        self.y -= h + GAP_AFTER_SECTION_LABEL

    def subheading(self, text, keep_with=2 * BODY_LEADING):
        self.heading(text, keep_with, style="sub")

    def bullets(self, items, style="body", marker="–", gap=PARA_GAP / 2):
        """Hanging-indent list at QNUM_W. marker '1.' style if marker == 'num'."""
        for i, it in enumerate(items, 1):
            m = f"{i}." if marker == "num" else marker
            st = STYLES[style]
            it = sup(it)
            p = Paragraph(it, st)
            _, h = p.wrap(CONTENT_WIDTH - QNUM_W, 10 ** 6)
            if h > self.remaining():
                if st.leading * 2 > self.remaining():
                    self._new_page()
                if h > self.remaining():
                    # long item: let text() split it, marker on first line
                    self.c.setFont(st.fontName, st.fontSize)
                    self.c.setFillColor(st.textColor)
                    self.c.drawString(CONTENT_X, self.y - st.fontSize, m)
                    self.text(it, style, indent=QNUM_W, gap=gap)
                    continue
            self.c.setFont(st.fontName, st.fontSize)
            self.c.setFillColor(st.textColor)
            self.c.drawString(CONTENT_X, self.y - st.fontSize, m)
            p.drawOn(self.c, CONTENT_X + QNUM_W, self.y - h)
            self.y -= h + gap
        self.y -= gap

    # ------------------------------------------------------------------ boxes
    def box(self, label, lines, label_style="sub", fill=CM_SKY, stroke=CM_MED_BLUE):
        """Example-box geometry (layout §9) with a caller label. `lines` items are
        paragraph strings or Figure objects. Height is content-derived; never splits."""
        inner_w = CONTENT_WIDTH - 2 * EXAMPLE_BOX_PADDING
        blocks, n_lines, fig_h = [], 0, 0
        for ln in lines:
            if isinstance(ln, Figure):
                # figures stay two-tone: a figure on a CM_SKY fill would carry brand colour
                raise ValueError("Figures may not be placed inside a coloured box")
                fig_h += ln.block_height()
            else:
                p, h = self.para(ln, "body", inner_w)
                blocks.append(p)
                n_lines += self.para_lines(p)
        box_h = example_box_height(n_lines) + fig_h
        self.ensure(box_h)
        c = self.c
        top = self.y
        c.setFillColor(fill)
        c.setStrokeColor(stroke)
        c.setLineWidth(1)
        c.roundRect(CONTENT_X, top - box_h, CONTENT_WIDTH, box_h, EXAMPLE_BOX_RADIUS, stroke=1, fill=1)
        label_y = top - EX_PAD_TOP - EX_LABEL_H + 3
        st = STYLES[label_style]
        c.setFillColor(st.textColor)
        c.setFont(st.fontName, st.fontSize)
        c.drawString(CONTENT_X + EXAMPLE_BOX_PADDING, label_y, label)
        yy = top - EX_PAD_TOP - EX_LABEL_H - EX_GAP_LABEL
        for b in blocks:
            if isinstance(b, Figure):
                yy -= IMAGE_PADDING_ABOVE
                x = self._fig_x(b, CONTENT_X + EXAMPLE_BOX_PADDING, inner_w)
                self._draw_figure(b, x, yy - b.h)
                yy -= b.h + IMAGE_PADDING_BELOW
            else:
                _, h = b.wrap(inner_w, 10 ** 6)
                b.drawOn(c, CONTENT_X + EXAMPLE_BOX_PADDING, yy - h)
                yy -= h
        self.y = top - box_h - GAP_AFTER_EXAMPLE_BOX

    def example_box(self, lines):
        """Layout §9 — label is always 'Example:'."""
        self.box("Example:", lines)

    # ------------------------------------------------------------------ figures
    @staticmethod
    def _fig_x(fig, x0, width):
        align = IMAGE_ALIGNMENT.get(fig.img_type, "center")
        if align == "center":
            return x0 + (width - fig.w) / 2
        if align == "right":
            return x0 + width - fig.w
        return x0

    def _draw_figure(self, fig, x, y_bottom):
        c = self.c
        c.saveState()
        fig.draw(c, x, y_bottom, fig.w, fig.h)
        c.restoreState()
        self.figure_log.append((self.page_num - self.start_page + 1, x, y_bottom, x + fig.w, y_bottom + fig.h))

    def figure(self, fig, indent=0):
        self.ensure(fig.block_height())
        self.y -= IMAGE_PADDING_ABOVE
        x = self._fig_x(fig, CONTENT_X + indent, CONTENT_WIDTH - indent)
        self._draw_figure(fig, x, self.y - fig.h)
        self.y -= fig.h + IMAGE_PADDING_BELOW

    # ------------------------------------------------------------------ questions
    def _options_layout(self, options, width):
        """Return (rows, col_w) — five Gauss options on as few rows as fit."""
        labels = "ABCDE"
        cells = [f"({labels[i]}) {o}" for i, o in enumerate(options)]
        for cols in (len(cells), 3, 2, 1):
            col_w = width / cols
            fits = all(self.para(t, "body", 10 ** 4)[0].minWidth() <= col_w - QNUM_W / 2 for t in cells)
            if fits or cols == 1:
                rows = [cells[i:i + cols] for i in range(0, len(cells), cols)]
                return rows, col_w
        raise AssertionError

    def question_height(self, stem, options=None, figure=None, area=0, teacher=None):
        w = CONTENT_WIDTH - QUESTION_NUMBER_WIDTH
        _, h = self.para(stem, "body", w)
        if figure:
            h += figure.block_height()
        if options:
            rows, col_w = self._options_layout(options, w)
            for r in rows:
                h += LINE_SPACING_WITHIN_QUESTION - BODY_LEADING + max(self.para(t, "body", col_w)[1] for t in r)
        if teacher:
            _, th = self.para(teacher, "teacher", w)
            area = max(area, th + PARA_GAP)
        return h + area + GAP_BETWEEN_QUESTIONS

    def question(self, n, stem, qtype, options=None, figure=None, work=None, teacher=None,
                 method_field=None, answer_blank=False):
        """Numbered item with keep-together. qtype ∈ VALID_Q_TYPES (layout §11).
        mcq/short → answer line / short blank (ANSWER_LINE_HEIGHT);
        word_problem/multi_step → open space `work` (default WORD_PROBLEM_WORK_SPACE), no ruled lines.
        method_field: label for a partial-credit response field (open, outlined) of height `work`.
        teacher: teacher-overlay text, rendered in the answer area (teacher version only)."""
        assert qtype in VALID_Q_TYPES, qtype
        if qtype in ("word_problem", "multi_step"):
            area = WORD_PROBLEM_WORK_SPACE if work is None else work
        else:
            area = ANSWER_LINE_HEIGHT if work is None else work
        total = self.question_height(stem, options, figure, area, teacher)
        if answer_blank:
            total += ANSWER_LINE_HEIGHT
        self.ensure(total - GAP_BETWEEN_QUESTIONS)
        c = self.c
        w = CONTENT_WIDTH - QUESTION_NUMBER_WIDTH
        x = CONTENT_X + QUESTION_NUMBER_WIDTH
        # number + stem
        p, h = self.para(stem, "body", w)
        st = STYLES["body"]
        c.setFont(*FONT_BODY)
        c.setFillColor(CM_DARK_GREY)
        c.drawString(CONTENT_X, self.y - st.fontSize, f"{n}.")
        p.drawOn(c, x, self.y - h)
        self.y -= h
        if figure:
            self.y -= IMAGE_PADDING_ABOVE
            fx = self._fig_x(figure, x, w)
            self._draw_figure(figure, fx, self.y - figure.h)
            self.y -= figure.h + IMAGE_PADDING_BELOW
        if options:
            rows, col_w = self._options_layout(options, w)
            for r in rows:
                self.y -= LINE_SPACING_WITHIN_QUESTION - BODY_LEADING
                rh = 0
                for j, t in enumerate(r):
                    op, oh = self.para(t, "body", col_w)
                    op.drawOn(c, x + j * col_w, self.y - oh)
                    rh = max(rh, oh)
                self.y -= rh
        # answer area
        th = 0
        if teacher:
            tp, th = self.para(teacher, "teacher", w)
            area = max(area, th + PARA_GAP)
        top = self.y
        if method_field and area:
            c.setStrokeColor(CM_GREY)
            c.setLineWidth(0.5)
            c.roundRect(x, top - area, w, area, TIP_BOX_RADIUS, stroke=1, fill=0)
            sp, sh = self.para(method_field, "small", w - 2 * CELL_PAD)
            sp.drawOn(c, x + CELL_PAD, top - CELL_PAD - sh)
            if teacher:
                tp.drawOn(c, x + CELL_PAD, top - CELL_PAD - sh - th)
        elif teacher:
            tp.drawOn(c, x, top - PARA_GAP / 2 - th)
        if not method_field and not teacher:
            if qtype == "mcq" and area:
                c.setStrokeColor(CM_GREY)
                c.setLineWidth(0.5)
                c.line(x, top - area, CONTENT_X + CONTENT_WIDTH, top - area)
            elif qtype == "short" and area:
                c.setStrokeColor(CM_GREY)
                c.setLineWidth(0.5)
                c.line(x, top - area, x + SHORT_BLANK_W, top - area)
        self.y = top - area
        if answer_blank:
            self.y -= ANSWER_LINE_HEIGHT
            c.setFont(*FONT_BODY_BOLD)
            c.setFillColor(CM_DARK_GREY)
            lw = pdfmetrics.stringWidth("Answer:", *FONT_BODY_BOLD)
            ax = CONTENT_X + CONTENT_WIDTH - SHORT_BLANK_W - lw - CELL_PAD
            c.drawString(ax, self.y, "Answer:")
            c.setStrokeColor(CM_GREY)
            c.setLineWidth(0.5)
            c.line(ax + lw + CELL_PAD, self.y, CONTENT_X + CONTENT_WIDTH, self.y)
        self.y -= GAP_BETWEEN_QUESTIONS
        self.questions.append(dict(n=n, stem=stem, type=qtype, page=self.page_num))

    def challenge_label(self, keep_with=4 * BODY_LEADING):
        """Layout §12 label."""
        self.heading(CHALLENGE_LABEL, keep_with, style="challenge")

    # ------------------------------------------------------------------ tables & forms
    def table(self, rows, col_widths, style="small", header=True, row_heights=None, bold_first_col=False):
        """Grid table; header row repeats on split. Cell text wraps. Grid lines are
        CM_GREY 0.5pt (the answer-line stroke) — form cells, not section separators."""
        total_w = sum(col_widths)
        scale = CONTENT_WIDTH / total_w
        col_widths = [cw * scale for cw in col_widths]
        hstyle = "small_bold" if style == "small" else "label"
        data = []
        for i, r in enumerate(rows):
            cells = []
            for j, cell in enumerate(r):
                if hasattr(cell, "wrap"):
                    cells.append(cell)
                    continue
                s = hstyle if (header and i == 0) or (bold_first_col and j == 0) else style
                cells.append(Paragraph(sup(str(cell)), STYLES[s]))
            data.append(cells)
        t = Table(data, colWidths=col_widths, rowHeights=row_heights, repeatRows=1 if header else 0)
        t.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 0.5, CM_GREY),
            ("FONTNAME", (0, 0), (-1, -1), FONT_BODY[0]),   # Table's own default is Helvetica
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), CELL_PAD),
            ("RIGHTPADDING", (0, 0), (-1, -1), CELL_PAD),
            ("TOPPADDING", (0, 0), (-1, -1), CELL_PAD),
            ("BOTTOMPADDING", (0, 0), (-1, -1), CELL_PAD),
        ]))
        self._flow_table(t)

    def _flow_table(self, t):
        while True:
            _, h = t.wrapOn(self.c, CONTENT_WIDTH, self.remaining())
            if h <= self.remaining():
                t.drawOn(self.c, CONTENT_X, self.y - h)
                self.y -= h + PARA_GAP
                return
            parts = t.split(CONTENT_WIDTH, self.remaining())
            if len(parts) < 2:
                self._new_page()
                continue
            first, rest = parts[0], parts[1]
            _, fh = first.wrapOn(self.c, CONTENT_WIDTH, self.remaining())
            first.drawOn(self.c, CONTENT_X, self.y - fh)
            self._new_page()
            t = rest

    def score_box(self, fields):
        """Self-scoring strip: one outlined row of 'label ____' fields (form element)."""
        h = BODY_LEADING + 2 * TIP_BOX_PADDING
        self.ensure(h)
        c = self.c
        c.setStrokeColor(CM_GREY)
        c.setLineWidth(0.5)
        c.roundRect(CONTENT_X, self.y - h, CONTENT_WIDTH, h, TIP_BOX_RADIUS, stroke=1, fill=0)
        fw = CONTENT_WIDTH / len(fields)
        for i, f in enumerate(fields):
            x = CONTENT_X + i * fw + TIP_BOX_PADDING
            base = self.y - TIP_BOX_PADDING - FONT_BODY[1]
            c.setFont(*FONT_BODY_BOLD)
            c.setFillColor(CM_BLUE)
            c.drawString(x, base, f)
            lw = pdfmetrics.stringWidth(f, *FONT_BODY_BOLD)
            if not f.startswith("Target"):
                c.line(x + lw + CELL_PAD, base - 2, CONTENT_X + (i + 1) * fw - TIP_BOX_PADDING, base - 2)
        self.y -= h + PARA_GAP

    def fill_lines(self, label, n=1):
        """A label followed by open short blanks (forms)."""
        p, h = self.para(label, "body")
        self.ensure(h + ANSWER_LINE_HEIGHT * n)
        p.drawOn(self.c, CONTENT_X, self.y - h)
        self.y -= h
        for _ in range(n):
            self.y -= ANSWER_LINE_HEIGHT
            self.c.setStrokeColor(CM_GREY)
            self.c.setLineWidth(0.5)
            self.c.line(CONTENT_X, self.y, CONTENT_X + CONTENT_WIDTH, self.y)
        self.y -= PARA_GAP

    # ------------------------------------------------------------------ output
    def build(self):
        self.c.showPage()
        self._page_open = False
        self.c.save()
        with open(self.path + ".figures.json", "w") as f:
            json.dump(self.figure_log, f)
        return self.path


def merge(paths, out_path):
    """Combined file = parts concatenated in order (math-workbook §4)."""
    from pypdf import PdfWriter, PdfReader
    w = PdfWriter()
    for p in paths:
        for page in PdfReader(p).pages:
            w.add_page(page)
    w.add_metadata({"/Author": "Concept Mastery"})
    with open(out_path, "wb") as f:
        w.write(f)
    figs = []
    offset = 0
    for p in paths:
        try:
            figs += [[pg + offset] + list(r) for pg, *r in json.load(open(p + ".figures.json"))]
        except FileNotFoundError:
            pass
        from pypdf import PdfReader as _R
        offset += len(_R(p).pages)
    with open(out_path + ".figures.json", "w") as f:
        json.dump(figs, f)
    return out_path
