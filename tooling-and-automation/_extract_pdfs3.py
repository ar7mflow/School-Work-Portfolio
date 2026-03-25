import sys
from pdfminer.high_level import extract_text
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar, LTAnno, LTTextBox, LTTextLine, LTFigure, LTImage

files = [
    (r"c:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 322\Project Files\A2 Rubric.pdf", "A2 Rubric.pdf"),
    (r"c:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 322\Project Files\A2 Info.pdf", "A2 Info.pdf"),
]

for path, name in files:
    print("=" * 80)
    print(f"FILE: {name}")
    print("=" * 80)
    
    # Method 1: Simple extraction
    print("\n--- pdfminer extract_text ---")
    try:
        text = extract_text(path)
        if text and text.strip():
            print(text)
        else:
            print("[No text extracted]")
    except Exception as e:
        print(f"Error: {e}")
    
    # Method 2: Page-by-page with element analysis
    print("\n--- pdfminer element analysis ---")
    try:
        for page_num, page_layout in enumerate(extract_pages(path)):
            print(f"\nPage {page_num + 1}: {page_layout.width}x{page_layout.height}")
            element_counts = {}
            for element in page_layout:
                etype = type(element).__name__
                element_counts[etype] = element_counts.get(etype, 0) + 1
                if isinstance(element, LTTextContainer):
                    t = element.get_text().strip()
                    if t:
                        print(f"  TEXT: {t[:200]}")
                elif isinstance(element, LTFigure):
                    print(f"  FIGURE: {element.width:.0f}x{element.height:.0f}")
                    # Recurse into figure
                    for sub in element:
                        if isinstance(sub, LTTextContainer):
                            t = sub.get_text().strip()
                            if t:
                                print(f"    SUB-TEXT: {t[:200]}")
                        elif isinstance(sub, LTImage):
                            print(f"    IMAGE: {sub.name}")
                elif isinstance(element, LTImage):
                    print(f"  IMAGE: {element.name}")
            print(f"  Element types: {element_counts}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n")
