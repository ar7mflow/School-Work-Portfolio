import pypdf
import sys

files = {
    "pq2_main": r"c:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 352\Practice Quiz 2\CISC 352 Artificial Intelligence W26 - CISC 352 Artificial Intelligence W26.pdf",
    "pq2_questions": r"c:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 352\Practice Quiz 2\Quiz 2 Possible Questions - CISC 352 Artificial Intelligence W26.pdf",
    "lectures_1_8": r"c:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 352\Lectures\CISC 352 -- weeks 1-8.pdf",
    "lectures_9_12": r"c:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 352\Lectures\CISC 352 -- weeks 9-12.pdf",
    "dsep": r"c:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 352\Lectures\d-separation.pdf",
    "syllabus": r"c:\Users\arham\Downloads\QUEENS\Courses\300 Level\CISC 352\Syllabus.pdf",
}

for key, path in files.items():
    try:
        reader = pypdf.PdfReader(path)
        text = ""
        for page in reader.pages:
            t = page.extract_text()
            if t:
                text += t
        print(f"\n\n=== FILE: {key} === PAGES: {len(reader.pages)} ===")
        # Print full text
        print(text)
        print(f"=== END {key} ===")
    except Exception as e:
        print(f"=== FILE: {key} ERROR: {e} ===")
