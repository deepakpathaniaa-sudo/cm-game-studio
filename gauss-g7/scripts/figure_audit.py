"""Crop every logged figure region at print resolution (300 dpi) and audit colour:
a figure passes only if every pixel is neutral grey (|R-G|,|G-B|,|R-B| <= 3), i.e. pure black/white
plus anti-aliasing. Writes crops for visual inspection."""
import sys, os, json, glob, pymupdf
def audit(pdf, out_dir, dpi=300):
    figs = json.load(open(pdf + ".figures.json")); d = pymupdf.open(pdf); res = []
    for k, (page, x0, y0, x1, y1) in enumerate(figs):
        pg = d[page - 1]; H = pg.rect.height
        clip = pymupdf.Rect(x0 - 2, H - y1 - 2, x1 + 2, H - y0 + 2)
        pix = pg.get_pixmap(dpi=dpi, clip=clip)
        s = pix.samples; n = pix.n; bad = 0; dark = 0
        for i in range(0, len(s), n):
            r, g, b = s[i], s[i+1], s[i+2]
            if max(abs(r-g), abs(g-b), abs(r-b)) > 3: bad += 1
            if r < 128: dark += 1
        o = os.path.join(out_dir, f"{os.path.basename(pdf)[:-4]}_fig{k+1}_p{page}.png"); pix.save(o)
        res.append((page, k + 1, bad, dark, o))
    return res
if __name__ == "__main__":
    out = sys.argv[1]; os.makedirs(out, exist_ok=True); fails = 0
    for pdf in sorted(glob.glob(os.path.join(sys.argv[2] if len(sys.argv) > 2 else "output", "*.pdf"))):
        if not os.path.exists(pdf + ".figures.json"): continue
        for page, k, bad, dark, o in audit(pdf, out):
            st = "PASS" if bad == 0 and dark > 0 else "FAIL"; fails += st == "FAIL"
            print(f"{st} {os.path.basename(pdf)} fig{k} p{page} coloured_px={bad} ink_px={dark}")
    sys.exit(1 if fails else 0)
