"""qa_pdf.py — automated pre-delivery QA for CM Grade 9 PDFs.

Implements skill-cm-layout-branding §18b + skill-cm-qa-checklist §1 checks that
can be verified programmatically. Footer text legitimately lives in the bottom
margin, so content-overflow is checked only for blocks above the footer band.
"""
import sys, re
import pymupdf

MARGIN_BOTTOM = 54.0
FOOTER_BAND_TOP = 40.0   # footer text baseline ~24pt up; 8pt glyphs -> exclude band
CONTENT_TOP_LIMIT = 792 - 54   # top margin
ALLOWED_FONT_SUB = "DejaVu"    # embedded subset names contain 'DejaVuSans...'


def check(pdf_path, expected_topic_title, expected_pages=None, min_images_per_page=1):
    doc = pymupdf.open(pdf_path)
    fails = []
    footer_lefts = []
    for pno, page in enumerate(doc, 1):
        r = page.rect
        # page size
        if abs(r.width - 612) > 1 or abs(r.height - 792) > 1:
            fails.append(f"p{pno}: page size {r.width}x{r.height} != 612x792")
        # logo present
        if len(page.get_images()) < min_images_per_page:
            fails.append(f"p{pno}: logo/image missing")
        # fonts DejaVu only — check RENDERED glyphs (an unused base-14 entry in
        # the resource dict is not a visible-font violation)
        used_fonts = set()
        for b in page.get_text("dict")["blocks"]:
            for line in b.get("lines", []):
                for s in line["spans"]:
                    if s["text"].strip():
                        used_fonts.add(s["font"])
        for fontname in used_fonts:
            if ALLOWED_FONT_SUB not in fontname:
                fails.append(f"p{pno}: rendered non-DejaVu font '{fontname}'")
        text = page.get_text()
        # no LOGO MISSING
        if "LOGO MISSING" in text:
            fails.append(f"p{pno}: 'LOGO MISSING' placeholder present")
        # no a) style LIST LABELS — only flag a letter+")" at the start of a
        # visual line (a real bad label), not math like "(200 + x)" mid-line.
        bad = set()
        for b in page.get_text("dict")["blocks"]:
            for line in b.get("lines", []):
                lt = "".join(s["text"] for s in line["spans"]).lstrip()
                m = re.match(r'^([a-f])\)\s', lt)
                if m:
                    bad.add(m.group(1) + ")")
        if bad:
            fails.append(f"p{pno}: non-standard list labels {bad} (use 'a.' not 'a)')")
        # content overflow (exclude footer band)
        page_bottom = r.height
        for b in page.get_text("dict")["blocks"]:
            if b.get("type") != 0:
                continue
            x0, y0, x1, y1 = b["bbox"]
            if y0 > page_bottom - FOOTER_BAND_TOP:
                continue  # footer text zone
            if y1 > page_bottom - MARGIN_BOTTOM + 0.6:
                fails.append(f"p{pno}: content crosses bottom margin (y1={y1:.1f})")
                break
        # footer-left capture (leftmost 8pt text near bottom)
        for b in page.get_text("dict")["blocks"]:
            for line in b.get("lines", []):
                bx0, by0, bx1, by1 = line["bbox"]
                if by0 > page_bottom - FOOTER_BAND_TOP and bx0 < 100:
                    footer_lefts.append(line["spans"][0]["text"].strip())
    # footer-left identical + equals topic title
    uniq = set(footer_lefts)
    if uniq and uniq != {expected_topic_title}:
        fails.append(f"footer-left not constant/expected: got {uniq}, want '{expected_topic_title}'")
    if expected_pages is not None and len(doc) != expected_pages:
        fails.append(f"page count {len(doc)} != expected {expected_pages}")
    npages = len(doc)
    doc.close()
    return fails, npages


def run(pdf_path, topic_title):
    fails, npages = check(pdf_path, topic_title)
    status = "PASS" if not fails else "FAIL"
    print(f"[{status}] {pdf_path}  ({npages} pages)")
    for f in fails:
        print("   -", f)
    return not fails


if __name__ == "__main__":
    ok = run(sys.argv[1], sys.argv[2])
    sys.exit(0 if ok else 1)
