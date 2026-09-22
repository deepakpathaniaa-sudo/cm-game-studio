"""cm_figures.py — vector figure primitives (Gauss programme).

Every primitive draws inside a declared (x, y, w, h) box and returns nothing.
Figures are two-tone: ink = black, paper = white. Brand colour never enters a
figure (programme rule: CEMC prints Gauss in black and white). Stroke weight is
FIGURE_LINE_W (layout §14b); labels use FIGURE_LABEL_FONT (DERIVED minimum).

Sprint 0 primitives: number_line, place_value_chart.
Pulled forward for the M1 diagnostic (full versions scheduled Week 7–8):
polygon (side labels, not-to-scale flag), angles_on_line.
"""
__version__ = "1.0.0"

import math
from reportlab.lib.colors import black, white
from reportlab.pdfbase import pdfmetrics
from cm_pdf import FIGURE_LINE_W, FIGURE_LABEL_FONT, Figure

INK = black
PAPER = white
LBL_FONT, LBL_SIZE = FIGURE_LABEL_FONT
TICK = LBL_SIZE * 0.6            # tick half-length, proportional to label size
LBL_GAP = LBL_SIZE * 0.5         # gap between a mark and its label


def _ink(c, width=FIGURE_LINE_W):
    c.setStrokeColor(INK)
    c.setFillColor(INK)
    c.setLineWidth(width)


def _label(c, x, y, text, anchor="c"):
    """Draw a label with its visual centre at (x, y)."""
    c.setFont(LBL_FONT, LBL_SIZE)
    c.setFillColor(INK)
    w = pdfmetrics.stringWidth(text, LBL_FONT, LBL_SIZE)
    by = y - LBL_SIZE * 0.35
    if anchor == "c":
        c.drawString(x - w / 2, by, text)
    elif anchor == "l":
        c.drawString(x, by, text)
    else:
        c.drawString(x - w, by, text)


def _fmt(v):
    s = f"{v:g}"
    return s.replace("-", "−")


# ----------------------------------------------------------------------------- number line
def number_line(start, end, step=1, label_every=1, points=(), jumps=(), label_values=None):
    """Horizontal number line with arrowheads.
    points: [(value, 'filled'|'open', label_or_None)]
    jumps:  [(from, to, label)] drawn as arcs above the line.
    label_values: explicit list of tick values to label (overrides label_every)."""

    def draw(c, x, y, w, h):
        _ink(c)
        pad = LBL_SIZE * 1.5
        x0, x1 = x + pad, x + w - pad
        base = y + LBL_SIZE * 2 if not jumps else y + LBL_SIZE * 2
        c.line(x, base, x + w, base)
        ah = LBL_SIZE * 0.5
        for sx, d in ((x, 1), (x + w, -1)):
            p = c.beginPath()
            p.moveTo(sx, base)
            p.lineTo(sx + d * ah * 1.4, base + ah * 0.7)
            p.lineTo(sx + d * ah * 1.4, base - ah * 0.7)
            p.close()
            c.drawPath(p, fill=1, stroke=0)

        def px(v):
            return x0 + (v - start) / (end - start) * (x1 - x0)

        n = int(round((end - start) / step))
        for i in range(n + 1):
            v = start + i * step
            c.line(px(v), base - TICK, px(v), base + TICK)
            show = (v in label_values) if label_values is not None else (i % label_every == 0)
            if show:
                _label(c, px(v), base - TICK - LBL_GAP - LBL_SIZE * 0.5, _fmt(v))
        for v, kind, lab in points:
            r = LBL_SIZE * 0.35
            c.setFillColor(INK if kind == "filled" else PAPER)
            c.circle(px(v), base, r, stroke=1, fill=1)
            if lab:
                _label(c, px(v), base + TICK + LBL_GAP + LBL_SIZE * 0.5, lab)
        for a, b, lab in jumps:
            xa, xb = px(a), px(b)
            rise = min(h - (base - y) - LBL_SIZE * 1.6, abs(xb - xa) * 0.35)
            p = c.beginPath()
            p.moveTo(xa, base + TICK)
            p.curveTo(xa, base + TICK + rise, xb, base + TICK + rise, xb, base + TICK)
            c.setFillColor(INK)
            c.drawPath(p, stroke=1, fill=0)
            # arrowhead at xb: the curve's end tangent is vertical, so the head points down
            q = c.beginPath()
            q.moveTo(xb, base + TICK)
            q.lineTo(xb - ah * 0.6, base + TICK + ah * 1.4)
            q.lineTo(xb + ah * 0.6, base + TICK + ah * 1.4)
            q.close()
            c.drawPath(q, fill=1, stroke=0)
            if lab:
                _label(c, (xa + xb) / 2, base + TICK + rise * 0.75 + LBL_SIZE * 0.9, lab)

    return draw


def number_line_figure(start, end, **kw):
    h = 60 if kw.get("jumps") else 40
    return Figure("number_line", number_line(start, end, **kw), h=h)


# ----------------------------------------------------------------------------- place-value chart
def place_value_chart(headers, digits=None):
    """Row of place headers over digit cells (digits None → blank cells for students)."""

    def draw(c, x, y, w, h):
        _ink(c, FIGURE_LINE_W * 0.6)
        n = len(headers)
        cw = w / n
        head_h = h * 0.45
        c.setFillColor(PAPER)
        for i, hd in enumerate(headers):
            cx = x + i * cw
            c.rect(cx, y, cw, h - head_h, stroke=1, fill=0)
            c.rect(cx, y + h - head_h, cw, head_h, stroke=1, fill=0)
            words = hd.split("\n")
            for k, wd in enumerate(words):
                _label(c, cx + cw / 2, y + h - head_h / 2 + (len(words) / 2 - k - 0.5) * LBL_SIZE * 1.1, wd)
            if digits:
                c.setFont("DejaVuSans-Bold", LBL_SIZE * 1.6)
                c.setFillColor(INK)
                c.drawCentredString(cx + cw / 2, y + (h - head_h) / 2 - LBL_SIZE * 0.55, str(digits[i]))

    return draw


def place_value_figure(headers, digits=None, img_type="illustration"):
    return Figure(img_type, place_value_chart(headers, digits), w=None, h=60)


# ----------------------------------------------------------------------------- polygon
def polygon(pts, side_labels=(), vertex_labels=(), not_to_scale=False, fill=False):
    """Closed polygon from unit coordinates, scaled uniformly to the box.
    side_labels: [(i, text)] label for edge pts[i]→pts[i+1], placed on the outward side.
    vertex_labels: [(i, text)]. not_to_scale: prints 'Not drawn to scale' under the figure."""
    area2 = sum(pts[i][0] * pts[(i + 1) % len(pts)][1] - pts[(i + 1) % len(pts)][0] * pts[i][1]
                for i in range(len(pts)))
    ccw = area2 > 0

    def draw(c, x, y, w, h):
        margin = LBL_SIZE * 2.2
        foot = LBL_SIZE * 1.8 if not_to_scale else 0
        xs, ys = [p[0] for p in pts], [p[1] for p in pts]
        sx = (w - 2 * margin) / (max(xs) - min(xs))
        sy = (h - 2 * margin - foot) / (max(ys) - min(ys))
        s = min(sx, sy)
        ox = x + margin + ((w - 2 * margin) - s * (max(xs) - min(xs))) / 2 - s * min(xs)
        oy = y + foot + margin - s * min(ys)
        P = [(ox + s * px, oy + s * py) for px, py in pts]
        _ink(c)
        path = c.beginPath()
        path.moveTo(*P[0])
        for q in P[1:]:
            path.lineTo(*q)
        path.close()
        c.setFillColor(INK if fill else PAPER)
        c.drawPath(path, stroke=1, fill=1 if fill else 0)
        for i, t in side_labels:
            (ax, ay), (bx, by) = P[i], P[(i + 1) % len(P)]
            dx, dy = bx - ax, by - ay
            L = math.hypot(dx, dy)
            nx, ny = (dy / L, -dx / L) if ccw else (-dy / L, dx / L)
            tw = pdfmetrics.stringWidth(t, LBL_FONT, LBL_SIZE)
            off = LBL_GAP + abs(nx) * tw / 2 + abs(ny) * LBL_SIZE / 2
            _label(c, (ax + bx) / 2 + nx * off, (ay + by) / 2 + ny * off, t)
        cx = sum(p[0] for p in P) / len(P)
        cy = sum(p[1] for p in P) / len(P)
        for i, t in vertex_labels:
            vx, vy = P[i]
            d = math.hypot(vx - cx, vy - cy)
            _label(c, vx + (vx - cx) / d * LBL_SIZE, vy + (vy - cy) / d * LBL_SIZE, t)
        if not_to_scale:
            _label(c, x + w / 2, y + LBL_SIZE * 0.6, "Not drawn to scale")

    return draw


# ----------------------------------------------------------------------------- angles on a line
def angles_on_line(angles, labels, point_label=None):
    """Straight line with rays from one point splitting 180° into `angles` (sum 180),
    drawn to scale. Each angle gets an arc (radii alternate so arcs never merge)
    and its label on the bisector outside the arc."""
    assert abs(sum(angles) - 180) < 1e-9

    def draw(c, x, y, w, h):
        _ink(c)
        vx, vy = x + w / 2, y + LBL_SIZE * 2
        L = min(w / 2 - LBL_SIZE, h - LBL_SIZE * 3)
        c.line(vx - w / 2 + LBL_SIZE, vy, vx + w / 2 - LBL_SIZE, vy)
        acc = 0
        base_r = L * 0.22
        for k, (a, lab) in enumerate(zip(angles, labels)):
            if k > 0:
                t = math.radians(180 - acc)
                c.line(vx, vy, vx + L * math.cos(t), vy + L * math.sin(t))
            r = base_r * (1 + 0.45 * (k % 2))   # alternate radii so neighbouring arcs read as separate angles
            start = 180 - acc - a
            c.arc(vx - r, vy - r, vx + r, vy + r, startAng=start, extent=a)
            mid = math.radians(start + a / 2)
            lr = r + LBL_SIZE * 1.4
            _label(c, vx + lr * math.cos(mid), vy + lr * math.sin(mid), lab)
            acc += a
        c.circle(vx, vy, FIGURE_LINE_W * 1.2, stroke=0, fill=1)
        if point_label:
            _label(c, vx, vy - LBL_SIZE * 1.2, point_label)

    return draw
