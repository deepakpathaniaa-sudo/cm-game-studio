#!/usr/bin/env python3
"""qa_pdf.py — automated pre-delivery checks for Concept Mastery PDFs.

Extended from skill-cm-qa-checklist/scripts/qa_pdf.py (same checks, same PASS/FAIL table):
  * file-name regex updated to layout §16 (the original regex predates it, as its label says);
  * title-block and footer checks read the actual page regions (PyMuPDF) instead of
    'first 600 characters' / 'last line', which misfire on text-heavy teacher files;
  * font check via PyMuPDF (pdffonts is not installed in this environment);
  * added: text inside the content area, logo image on every page, no JS / links.
Usage: python qa_pdf.py file.pdf [--companion other.pdf ...] [--expect-pages N] [--topic "Title"]
Exit code 1 on any FAIL."""
import sys, re, hashlib, argparse, os
import pymupdf

LETTER = (612, 792)
BAD_TITLE = ["LOGO MISSING", "Workbook", "Study Book", " WB"]
NAME_RE = re.compile(r"^CM_G[1-8]_Math_[A-Za-z0-9]+_v\d+_\d{4}-\d{2}\.pdf$")   # layout §16
MARGIN_L, MARGIN_R, MARGIN_T, MARGIN_B = 63, 54, 54, 54


def stems(doc):
    out = []
    for p in doc:
        for b in p.get_text("dict")["blocks"]:
            for ln in b.get("lines", []):
                t = "".join(s["text"] for s in ln["spans"]).strip()
                if len(t) > 25 and not re.match(r"^\(?[A-E]\)", t):
                    out.append(hashlib.md5(t.lower().encode()).hexdigest())
    return out


def item_stems(doc):
    """Question stems only: text lines right of a number column that start an item."""
    out = []
    for p in doc:
        words = p.get_text("words")
        nums = [w for w in words if re.fullmatch(r"\d{1,2}\.", w[4]) and abs(w[0] - MARGIN_L) < 2]
        for nw in nums:
            line = " ".join(w[4] for w in sorted(words, key=lambda w: w[0])
                            if nw[1] - 6 <= w[1] and w[3] <= nw[3] + 2 and w[0] > nw[2])   # includes superscripts
            if len(line) > 12:
                out.append((p.number + 1, line))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf"); ap.add_argument("--companion", nargs="*", default=[])
    ap.add_argument("--expect-pages", type=int); ap.add_argument("--topic")
    ap.add_argument("--combined", action="store_true", help="concatenated parts: skip within-file duplicate scan")
    a = ap.parse_args()
    d = pymupdf.open(a.pdf); results = []
    def rec(name, ok, where=""): results.append((name, "PASS" if ok else "FAIL", where))

    sizes = {(round(p.rect.width), round(p.rect.height)) for p in d}
    rec("Page size 8.5x11", sizes == {LETTER}, str(sizes))
    if a.expect_pages: rec("Page count", len(d) == a.expect_pages, f"{len(d)}")

    # title block region: below header gap, above first content (layout §7b)
    tb = d[0].get_text(clip=pymupdf.Rect(0, MARGIN_T, 612, MARGIN_T + 60)).strip()
    rec("Title block: no forbidden strings", not any(b in tb for b in BAD_TITLE), tb.replace("\n", " | ")[:70])
    rec("Title block: no 'Grade N'", not re.search(r"\bGRADE\s*\d", tb, re.I))
    rec("No LOGO MISSING anywhere", not any("LOGO MISSING" in p.get_text() for p in d))
    rec("Logo image on every page", all(len(p.get_images()) >= 1 for p in d), "")

    # footer: left zone == topic on every page, copyright centre, page number right
    fl = []
    for i, p in enumerate(d):
        band = p.get_text("words", clip=pymupdf.Rect(0, 792 - MARGIN_B, 612, 792))
        left = " ".join(w[4] for w in band if w[2] <= 220)
        right = " ".join(w[4] for w in band if w[0] > 500)
        centre = " ".join(w[4] for w in band if w[2] > 220 and w[0] <= 500)
        fl.append((left, centre, right, i + 1))
    lefts = {f[0] for f in fl}
    rec("Footer-left identical on all pages", len(lefts) == 1, "; ".join(sorted(lefts))[:70])
    if a.topic:
        rec("Footer-left == topic title", lefts == {a.topic}, a.topic)
        tt = d[0].get_text(clip=pymupdf.Rect(0, MARGIN_T, 612, MARGIN_T + 40)).strip().splitlines()[0]
        rec("Title block == topic title", tt == a.topic, tt)
    rec("Footer copyright on all pages", all(f[1] == "Copyright © 2026 by Concept Mastery" for f in fl))
    rec("Footer page numbers sequential", [f[2] for f in fl] == [str(i) for i in range(1, len(d) + 1)])

    # text inside the content area (header band holds the logo only; footer band holds footer only)
    out_txt = []
    for p in d:
        for b in p.get_text("dict")["blocks"]:
            if b["type"] != 0: continue
            x0, y0, x1, y1 = b["bbox"]
            in_footer = y0 >= 792 - MARGIN_B
            if not in_footer and (x0 < MARGIN_L - 1 or x1 > 612 - MARGIN_R + 1 or y0 < MARGIN_T - 1 or y1 > 792 - MARGIN_B + 1):
                out_txt.append((p.number + 1, round(x0), round(y0), round(x1), round(y1)))
    rec("No text outside content area", not out_txt, str(out_txt[:3]))

    mine = item_stems(d)
    hs = [hashlib.md5(t.lower().encode()).hexdigest() for _, t in mine]
    if a.combined:
        rec("Duplicate scan (combined file: parts repeat by design)", True, "skipped")
    else:
      rec("No duplicate item stems within file", len(hs) == len(set(hs)), f"{len(hs)} stems, {len(hs)-len(set(hs))} dup")
    for c in a.companion:
        other = {hashlib.md5(t.lower().encode()).hexdigest() for _, t in item_stems(pymupdf.open(c))}
        shared = set(hs) & other
        rec(f"No duplicate stems vs {os.path.basename(c)[:40]}", not shared, f"{len(shared)} shared")

    fname = os.path.basename(a.pdf)
    rec("File name pattern (layout §16)", bool(NAME_RE.match(fname)), fname)

    fonts = set()
    for p in d:
        for f in p.get_fonts(full=True):
            fonts.add((f[3], f[1]))
    rec("Only DejaVuSans fonts", all("DejaVuSans" in n for n, _ in fonts), ",".join(sorted(n for n, _ in fonts)))
    rec("All fonts embedded", all(ext in ("ttf", "cff", "otf", "n/a") and ext != "n/a" for _, ext in fonts) or
        all(ext != "n/a" for _, ext in fonts), ",".join(sorted({e for _, e in fonts})))
    rec("No JavaScript / external links", not any(l.get("uri") for p in d for l in p.get_links()) and
        "JavaScript" not in (d.pdf_catalog() and d.xref_object(d.pdf_catalog()) or ""))

    w = max(len(n) for n, _, _ in results)
    for n, s, wh in results: print(f"{n.ljust(w)}  {s}  {wh}")
    sys.exit(1 if any(s == "FAIL" for _, s, _ in results) else 0)


if __name__ == "__main__":
    main()
