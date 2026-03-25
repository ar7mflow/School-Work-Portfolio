import sys

files = [
    (r"c:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 322\Project Files\A2 Rubric.pdf", "A2 Rubric.pdf"),
    (r"c:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 322\Project Files\A2 Info.pdf", "A2 Info.pdf"),
]

for path, name in files:
    print("=" * 80)
    print(f"FILE: {name}")
    print("=" * 80)
    
    # Method 1: PyPDF2
    print("\n>>> Method: PyPDF2")
    try:
        from PyPDF2 import PdfReader
        reader = PdfReader(path)
        print(f"Number of pages: {len(reader.pages)}")
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            print(f"--- Page {i+1} (len={len(text) if text else 0}) ---")
            if text and text.strip():
                print(text)
            else:
                print("[No text extracted]")
            print()
    except Exception as e:
        print(f"Error: {e}")
    
    # Method 2: pdfplumber with layout
    print("\n>>> Method: pdfplumber (layout)")
    try:
        import pdfplumber
        with pdfplumber.open(path) as pdf:
            print(f"Number of pages: {len(pdf.pages)}")
            for i, page in enumerate(pdf.pages):
                # Try extract_text with layout
                text = page.extract_text(layout=True)
                print(f"--- Page {i+1} (len={len(text) if text else 0}) ---")
                if text and text.strip():
                    print(text)
                else:
                    print("[No text extracted]")
                    # Check if page has images
                    print(f"  Page dimensions: {page.width}x{page.height}")
                    print(f"  Number of chars: {len(page.chars)}")
                    print(f"  Number of images: {len(page.images)}")
                    if page.chars:
                        print(f"  First 10 chars: {page.chars[:10]}")
                print()
    except Exception as e:
        print(f"Error: {e}")
    
    # Method 3: pdfplumber raw chars
    print("\n>>> Method: pdfplumber (raw chars)")
    try:
        import pdfplumber
        with pdfplumber.open(path) as pdf:
            for i, page in enumerate(pdf.pages):
                chars = page.chars
                if chars:
                    text = "".join(c["text"] for c in chars)
                    print(f"--- Page {i+1} raw chars (len={len(text)}) ---")
                    print(text[:500] if len(text) > 500 else text)
                else:
                    print(f"--- Page {i+1}: No chars found ---")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n")
