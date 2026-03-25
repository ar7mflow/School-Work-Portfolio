import fitz  # PyMuPDF
import sys

files = [
    (r"c:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 322\Project Files\A2 Rubric.pdf", "A2 Rubric.pdf"),
    (r"c:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 322\Project Files\A2 Info.pdf", "A2 Info.pdf"),
]

for path, name in files:
    print("=" * 80)
    print(f"FILE: {name}")
    print("=" * 80)
    
    doc = fitz.open(path)
    print(f"Pages: {len(doc)}")
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        # Method 1: Standard text extraction
        text = page.get_text("text")
        print(f"\n--- Page {page_num + 1} - get_text('text') ---")
        if text.strip():
            print(text)
        else:
            print("[No text]")
        
        # Method 2: Dict extraction - shows structure
        d = page.get_text("dict")
        block_count = len(d.get("blocks", []))
        text_blocks = sum(1 for b in d.get("blocks", []) if b.get("type") == 0)
        image_blocks = sum(1 for b in d.get("blocks", []) if b.get("type") == 1)
        print(f"  Blocks: {block_count} (text={text_blocks}, image={image_blocks})")
        
        # Check for drawings/paths
        paths = page.get_drawings()
        print(f"  Drawings/paths: {len(paths)}")
        
        # Try OCR via PyMuPDF's built-in if available
        try:
            text_ocr = page.get_text("text", flags=fitz.TEXT_PRESERVE_WHITESPACE)
            if text_ocr.strip() and text_ocr.strip() != text.strip():
                print(f"\n  WITH FLAGS:")
                print(text_ocr)
        except:
            pass
    
    doc.close()
    print()
