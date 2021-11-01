from fpdf import FPDF
import os
import datetime

class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'The My Personal Health Assistant (MyPHA) for Essilor', 0, 0, 'C')
        
        link = self.add_link()
        self.set_link(link, page=1)
        self.link(30, 10, 140, 20, link)
        
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def report_title_details(self):
        self.set_y(220)
        self.set_font('Arial', 'B', 14)
        self.multi_cell(190, 10, 'The My Personal Health Assistant (MyPHA) for Essilor\n Clinical Risk Reduction: Identifying Challenges and Taking Action!\n For the time Period: January 1st 2020 to June 30th 2021\n '+day, 1, 'C',False)

    def logos(self):
        self.set_y(-15)

        self.image('mypha_logo.png', 6, 268, 45,20)
        self.image('ch_logo.png', 140, 270, 67,20)

    def chapter_title(self, name):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, name, 0, 0, 'L', 0)

        pdf.link(0, 30, 50, 12, "https://google.com")
        # Line break
        self.ln(4)

    def content(self):
        self.add_font('DejaVu', '', 'font/DejaVuSansCondensed.ttf', uni=True)
        self.set_font('DejaVu', '', 14)
        self.multi_cell(0,10, u'\u2022 one \n \u25E6 two', 0, 'C',False)

    def contents(self):
        positionx=12
        self.cell(6, positionx, 'The My Personal Health Assistant (MyPHA) for Essilor.................................................................1', 0, 0, 'L', 0)
        self.ln(4)
        positionx=positionx+12
        self.cell(6, positionx,'Health Risk Analysis and Reduction Report..................................................................................2', 0, 0, 'L', 0)
        self.ln(4)
        positionx=positionx+12
        self.cell(6, positionx,'Executive Summary ..................................................................................................................2', 0, 0, 'L', 0) 
        self.ln(4)
        positionx=positionx+12
        self.cell(6, positionx,'The MyPHA Program .................................................................................................................3', 0, 0, 'L', 0)
        self.ln(4)
        positionx=positionx+12
        self.cell(6, positionx,'  1. Identifying Essilor Members Risk.................................................................................3', 0, 0, 'L', 0)
        self.ln(4)
        positionx=positionx+12
        self.cell(6, positionx,'  2. Understanding the NMEs (Diseases) ............................................................................4', 0, 0, 'L', 0)


      

if os.path.exists("test.txt"):
  os.remove("test.txt")

now=datetime.datetime.now()
day=now.strftime("%A, %B %d, %Y")

pdf=PDF()
#Cover page
pdf.add_page()
pdf.image("ScreenShot2021-10-18at12_30_45PM.png", 0, 0, 210, 210)
pdf.report_title_details()
pdf.logos()

#Contents page
pdf.add_page()
pdf.set_font('Arial', 'B', 12)
pdf.cell(0,0,'Health Risk Analysis and Reduction Report',0, 0, 'L', 0)
pdf.ln(4)
pdf.chapter_title('Contents')
pdf.contents()



#Executive summary page
pdf.add_page()
pdf.chapter_title('Executive Summary')
pdf.set_font('Arial', 'B', 16)
pdf.content()
pdf.output('test.pdf', 'F')
