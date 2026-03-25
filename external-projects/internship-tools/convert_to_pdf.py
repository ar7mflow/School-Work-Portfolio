from fpdf2 import FPDF

# Read the cover letter
with open('ArhamHassan_442634_SAPAgileDeveloper_CoverLetter.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=11)
pdf.set_margins(25.4, 25.4, 25.4)  # 1 inch margins

# Split content into lines and add to PDF
for line in content.split('\n'):
    if line.strip():
        pdf.multi_cell(0, 5, line)
    else:
        pdf.ln(5)

# Save PDF
pdf.output('ArhamHassan_442634_SAPAgileDeveloper_CoverLetter.pdf')
print("PDF created successfully!")
