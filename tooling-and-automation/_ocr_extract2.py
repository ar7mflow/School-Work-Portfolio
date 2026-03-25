import sys
import os
import traceback
import io

print("Starting OCR extraction...", flush=True)

# Check files exist
pdf1 = r"C:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 322\Project Files\A2 Rubric.pdf"
pdf2 = r"C:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 322\Project Files\A2 Info.pdf"

for p in [pdf1, pdf2]:
    print(f"  {os.path.basename(p)}: exists={os.path.exists(p)}", flush=True)

print("\nLoading easyocr (this downloads model on first use)...", flush=True)
import easyocr
import numpy as np
from PIL import Image

reader = easyocr.Reader(['en'], gpu=False, verbose=True)
print("EasyOCR reader ready.\n", flush=True)

print("Loading pdfplumber...", flush=True)
import pdfplumber

output_lines = []

for pdf_path in [pdf1, pdf2]:
    fname = os.path.basename(pdf_path)
    header = f"\n{'='*80}\nFILE: {fname}\n{'='*80}"
    print(header, flush=True)
    output_lines.append(header)
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            num_pages = len(pdf.pages)
            print(f"Total pages: {num_pages}", flush=True)
            
            for page_num, page in enumerate(pdf.pages, 1):
                page_header = f"\n--- PAGE {page_num} of {num_pages} ---"
                print(page_header, flush=True)
                output_lines.append(page_header)
                
                # Render page to image at 300 DPI
                img = page.to_image(resolution=300)
                pil_img = img.original
                img_array = np.array(pil_img)
                
                print(f"  Image size: {pil_img.size}, running OCR...", flush=True)
                
                # Run OCR
                results = reader.readtext(img_array, detail=0, paragraph=True)
                
                page_text = "\n".join(results)
                print(page_text, flush=True)
                output_lines.append(page_text)
                
    except Exception as e:
        err = f"ERROR processing {fname}: {e}\n{traceback.format_exc()}"
        print(err, flush=True)
        output_lines.append(err)

# Also save to file
output_path = r"C:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 322\Project Files\_OCR_OUTPUT.txt"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(output_lines))

print(f"\n\nOutput also saved to: {output_path}", flush=True)
print("DONE.", flush=True)
