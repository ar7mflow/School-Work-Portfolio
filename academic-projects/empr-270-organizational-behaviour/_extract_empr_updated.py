import pypdf
from pathlib import Path
base = Path(r"c:\Users\arham\Downloads\QUEENS\Courses\200 Level\EMPR 270")
files = [
    "UPDATED EMPR 270 Assignment Instructions Winter 2026.pdf",
    "UPDATED EMPR 270 Syllabus Winter 2026.pdf",
    "UPDATED EMPR 270 Weekly Guide Winter 2026.pdf",
]
out = base / "EMPR270_UPDATED_EXTRACT.txt"
parts = []
for name in files:
    path = base / name
    parts.append(f"\n\n===== FILE: {name} =====\n")
    try:
        reader = pypdf.PdfReader(str(path))
        parts.append(f"PAGES: {len(reader.pages)}\n")
        for i, page in enumerate(reader.pages, 1):
            txt = page.extract_text() or ""
            parts.append(f"\n--- PAGE {i} ---\n")
            parts.append(txt)
    except Exception as e:
        parts.append(f"\n[ERROR] {e}\n")
out.write_text("".join(parts), encoding="utf-8", errors="replace")
print(f"WROTE {out}")
