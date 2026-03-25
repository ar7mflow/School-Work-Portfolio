import pdfplumber

files = [
    (r"c:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 322\Project Files\A2 Rubric.pdf", "A2 Rubric.pdf"),
    (r"c:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 322\Project Files\A2 Info.pdf", "A2 Info.pdf"),
]

for path, name in files:
    print("=" * 80)
    print(f"FILE: {name}")
    print("=" * 80)
    try:
        with pdfplumber.open(path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    print(f"--- Page {i+1} ---")
                    print(text)
                    print()
                # Also try extracting tables
                tables = page.extract_tables()
                if tables:
                    for ti, table in enumerate(tables):
                        print(f"--- Page {i+1} Table {ti+1} ---")
                        for row in table:
                            print(" | ".join(str(cell) if cell else "" for cell in row))
                        print()
    except Exception as e:
        print(f"Error with pdfplumber: {e}")
        print("Trying PyPDF2...")
        try:
            from PyPDF2 import PdfReader
            reader = PdfReader(path)
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    print(f"--- Page {i+1} ---")
                    print(text)
                    print()
        except Exception as e2:
            print(f"Error with PyPDF2: {e2}")
    print()
