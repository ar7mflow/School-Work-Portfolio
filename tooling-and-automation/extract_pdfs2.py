import pypdf
import sys
import io
import os

# Redirect stdout to utf-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

files = {
    "lectures_1_8": r"c:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 352\Lectures\CISC 352 -- weeks 1-8.pdf",
    "lectures_9_12": r"c:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 352\Lectures\CISC 352 -- weeks 9-12.pdf",
    "dsep": r"c:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 352\Lectures\d-separation.pdf",
}

for key, path in files.items():
    try:
        reader = pypdf.PdfReader(path)
        text = ""
        for page in reader.pages:
            t = page.extract_text()
            if t:
                # Replace problematic characters
                t = t.encode('utf-8', errors='replace').decode('utf-8')
                text += t + "\n"
        print(f"\n\n=== FILE: {key} === PAGES: {len(reader.pages)} ===")
        print(text)
        print(f"=== END {key} ===")
    except Exception as e:
        print(f"=== FILE: {key} ERROR: {e} ===")
