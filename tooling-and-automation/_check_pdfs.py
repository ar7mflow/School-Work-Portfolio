import pdfplumber
import sys
import os
import traceback

# First, let's just check the PDFs exist and have pages
pdf1 = r"C:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 322\Project Files\A2 Rubric.pdf"
pdf2 = r"C:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 322\Project Files\A2 Info.pdf"

for pdf_path in [pdf1, pdf2]:
    print(f"Checking: {pdf_path}")
    print(f"  Exists: {os.path.exists(pdf_path)}")
    if os.path.exists(pdf_path):
        try:
            with pdfplumber.open(pdf_path) as pdf:
                print(f"  Pages: {len(pdf.pages)}")
                for i, page in enumerate(pdf.pages):
                    print(f"  Page {i+1}: images={len(page.images)}, chars={len(page.chars)}")
                    # Try extracting text directly first
                    text = page.extract_text()
                    if text:
                        print(f"  Direct text (first 200 chars): {text[:200]}")
                    else:
                        print(f"  No direct text (image-based PDF)")
        except Exception as e:
            traceback.print_exc()
    print()
