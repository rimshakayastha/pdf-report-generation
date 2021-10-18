from fpdf import FPDF
import os



if os.path.exists("test.txt"):
  os.remove("test.txt")



pdf=FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hello World!')

pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hello World!')
pdf.output('test.pdf', 'F')