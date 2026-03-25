import fitz  # PyMuPDF
import os

output_dir = r"c:\Users\arham\Downloads\QUEENS\Courses\300 Level\_pdf_images"
os.makedirs(output_dir, exist_ok=True)

files = [
    (r"c:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 322\Project Files\A2 Rubric.pdf", "rubric"),
    (r"c:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 322\Project Files\A2 Info.pdf", "info"),
]

for path, prefix in files:
    doc = fitz.open(path)
    for page_num in range(len(doc)):
        page = doc[page_num]
        # Render at 300 DPI for good OCR quality
        mat = fitz.Matrix(300/72, 300/72)
        pix = page.get_pixmap(matrix=mat)
        out_path = os.path.join(output_dir, f"{prefix}_page{page_num+1}.png")
        pix.save(out_path)
        print(f"Saved: {out_path} ({pix.width}x{pix.height})")
    doc.close()

print("\nDone! All pages rendered to PNG.")
