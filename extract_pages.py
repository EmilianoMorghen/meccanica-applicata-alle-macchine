import os
import pymupdf

PDF_PATH = "Vangelo secondo Mirko (BELFIORE VERSION) (1) (1)_260303_110049.pdf"
OUTPUT_DIR = "pages"
DPI = 150

os.makedirs(OUTPUT_DIR, exist_ok=True)

doc = pymupdf.open(PDF_PATH)
total = len(doc)

print(f"Extracting {total} pages at {DPI} DPI into '{OUTPUT_DIR}/'...")

for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=DPI)
    output_path = os.path.join(OUTPUT_DIR, f"page_{i+1:03d}.png")
    pix.save(output_path)
    print(f"  [{i+1}/{total}] {output_path}")

print(f"\nDone! {total} pages saved to '{OUTPUT_DIR}/'")
