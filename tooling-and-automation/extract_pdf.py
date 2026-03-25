"""Extract text from image-based PDFs using pdfplumber + easyocr or pytesseract"""
import sys
import os
import tempfile

def extract_with_pdfplumber_and_ocr(pdf_path, output_path):
    """Extract images from PDF pages and OCR them."""
    import pdfplumber
    from PIL import Image
    import io
    
    print(f"Processing: {pdf_path}")
    print(f"Output: {output_path}")
    
    all_text = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            print(f"  Page {page_num + 1}/{len(pdf.pages)}...")
            
            # Convert pdfplumber page to image
            img = page.to_image(resolution=300)
            
            # Save to temp file
            temp_img_path = os.path.join(tempfile.gettempdir(), f"page_{page_num}.png")
            img.save(temp_img_path)
            
            # Try pytesseract first
            try:
                import pytesseract
                pil_img = Image.open(temp_img_path)
                text = pytesseract.image_to_string(pil_img)
                all_text.append(f"=== PAGE {page_num + 1} ===\n{text}\n")
                print(f"    Got {len(text)} chars via pytesseract")
                continue
            except Exception as e:
                print(f"    pytesseract failed: {e}")
            
            # Try easyocr
            try:
                import easyocr
                reader = easyocr.Reader(['en'], gpu=False)
                results = reader.readtext(temp_img_path)
                text = '\n'.join([r[1] for r in results])
                all_text.append(f"=== PAGE {page_num + 1} ===\n{text}\n")
                print(f"    Got {len(text)} chars via easyocr")
                continue
            except Exception as e:
                print(f"    easyocr failed: {e}")
            
            all_text.append(f"=== PAGE {page_num + 1} ===\n[OCR FAILED]\n")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(all_text))
    
    print(f"Done! Wrote to {output_path}")

if __name__ == '__main__':
    base = r'C:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 322\Project Files'
    
    pdfs = [
        (os.path.join(base, 'A2 Rubric.pdf'), os.path.join(base, 'A2_Rubric_text.txt')),
        (os.path.join(base, 'A2 Info.pdf'), os.path.join(base, 'A2_Info_text.txt')),
    ]
    
    for pdf_path, output_path in pdfs:
        try:
            extract_with_pdfplumber_and_ocr(pdf_path, output_path)
        except Exception as e:
            print(f"ERROR processing {pdf_path}: {e}")
            import traceback
            traceback.print_exc()
