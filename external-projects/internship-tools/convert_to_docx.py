from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_LINE_SPACING

# Read the cover letter
with open('ArhamHassan_442634_SAPAgileDeveloper_CoverLetter.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Create document
doc = Document()

# Set margins - standard 1 inch
sections = doc.sections
for section in sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

# Split content into lines
lines = content.split('\n')

for i, line in enumerate(lines):
    if line.strip():  # Only add non-empty lines
        p = doc.add_paragraph(line)
        
        # Set font
        for run in p.runs:
            run.font.name = 'Calibri'
            run.font.size = Pt(11)
        
        # Single spacing
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.space_before = Pt(0)
        
        # Add spacing after contact info (first 3 lines), date, address, and paragraphs
        if i < 3:  # Contact info
            p.paragraph_format.space_after = Pt(0)
        elif 'February' in line:  # Date
            p.paragraph_format.space_after = Pt(12)
        elif 'SAP' in line and i < 10:  # Company address
            p.paragraph_format.space_after = Pt(0)
        elif 'Dear' in line:  # Salutation
            p.paragraph_format.space_after = Pt(12)
        elif 'Best regards' in line:  # Closing
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(0)
        elif line == lines[-1]:  # Signature
            p.paragraph_format.space_after = Pt(0)
        else:  # Body paragraphs
            p.paragraph_format.space_after = Pt(6)

# Save document
doc.save('ArhamHassan_442634_SAPAgileDeveloper_CoverLetter.docx')
print("Professional DOCX created successfully!")
