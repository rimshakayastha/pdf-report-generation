#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Sample FDA Report')
pdf.output('FDA Report.pdf', 'F')

