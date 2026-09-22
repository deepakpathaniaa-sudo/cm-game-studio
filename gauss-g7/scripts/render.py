"""Rasterise PDF pages to PNG for visual inspection (print resolution by default)."""
import sys, os, pymupdf
def render(pdf, out_dir, dpi=300, pages=None):
    os.makedirs(out_dir, exist_ok=True)
    d = pymupdf.open(pdf); base = os.path.basename(pdf)[:-4]; outs = []
    for i, p in enumerate(d):
        if pages and (i + 1) not in pages: continue
        o = os.path.join(out_dir, f"{base}_p{i+1:02d}.png"); p.get_pixmap(dpi=dpi).save(o); outs.append(o)
    return outs
if __name__ == "__main__":
    pdf, out = sys.argv[1], sys.argv[2]; dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 300
    pages = [int(x) for x in sys.argv[4].split(",")] if len(sys.argv) > 4 else None
    print("\n".join(render(pdf, out, dpi, pages)))
