import pdfplumber
import easyocr
import io
import sys
from PIL import Image
import numpy as np

reader = easyocr.Reader(['en'], gpu=False)

def ocr_pdf(pdf_path):
    print(f"\n{'='*80}")
    print(f"EXTRACTING TEXT FROM: {pdf_path}")
    print(f"{'='*80}\n")
    
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, 1):
            print(f"\n--- PAGE {page_num} ---\n")
            
            # Try to get images from the page
            images = page.images
            if images:
                for img_info in images:
                    # Extract the image using the page
                    # pdfplumber stores image data differently
                    pass
            
            # Convert page to image using pdfplumber's to_image
            img = page.to_image(resolution=300)
            # Convert to PIL Image
            pil_img = img.original
            # Convert to numpy array for easyocr
            img_array = np.array(pil_img)
            
            # Run OCR
            results = reader.readtext(img_array, detail=0, paragraph=True)
            
            for text in results:
                print(text)
            
            sys.stdout.flush()

# Process both PDFs
pdf1 = r"C:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 322\Project Files\A2 Rubric.pdf"
pdf2 = r"C:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 322\Project Files\A2 Info.pdf"

ocr_pdf(pdf1)
ocr_pdf(pdf2)

print("\n\nDONE - All text extracted.")
