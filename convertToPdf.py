from fpdf import FPDF
import os
import datetime

class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('Arial', '', 10)
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
        self.set_y(225)
        self.set_font('Helvetica', 'B', 14)
        self.multi_cell(190, 10, 'The My Personal Health Assistant (MyPHA) for Essilor\n \
          Clinical Risk Reduction: Identifying Challenges and Taking Action!\n', 1, 'C',False)
        self.set_font('Helvetica', '', 14)
        self.multi_cell(190, 10, '\
            For the time period: January 1st 2020 to June 30th 2021\n \
              '+day, 1, 'C',False)

    def logos(self):
        self.set_y(-15)

        self.image('mypha_logo.png', 6, 268, 45,20)
        self.image('ch_logo.png', 140, 270, 67,20)

    def chapter_title(self, name):
        # Arial 12
        self.set_font('Arial', '', 16)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, name, 0, 0, 'L', 0)

        # Line break
        self.ln(4)

    def content(self):
        self.add_font('DejaVu', '', 'font/DejaVuSansCondensed.ttf', uni=True)
        self.set_font('DejaVu', '', 14)
        self.multi_cell(0,10, u'\u2022 one \n \u25E6 two', 0, 'C',False)

    def contents(self):
        self.set_font('Arial', '', 11)
        positionx=12
        self.cell(6, positionx, 'The My Personal Health Assistant (MyPHA) for Essilor.................................................................', 0, 0, 'L', 0)
        self.cell(0,positionx,'1',0, 0, 'R', 0)
        self.ln(4)
        positionx=positionx+12
        self.cell(6, positionx, 'Health Risk Analysis and Reduction Report................................................................................', 0, 0, 'L', 0)
        self.cell(0,positionx,'2',0, 0, 'R', 0)
        self.ln(4)
        positionx=positionx+12
        self.cell(6, positionx, 'Executive Summary .............................................................................................................', 0, 0, 'L', 0) 
        self.cell(0,positionx,'2',0, 0, 'R', 0)
        self.ln(4)
        positionx=positionx+12
        self.cell(6, positionx, 'The MyPHA Program ......................................................................................................', 0, 0, 'L', 0)
        self.cell(0,positionx,'3',0, 0, 'R', 0)
        self.ln(4)
        positionx=positionx+12
        self.cell(6, positionx, '  1. Identifying Essilor Members Risk................................................................................', 0, 0, 'L', 0)
        self.cell(0,positionx,'3',0, 0, 'R', 0)
        self.ln(4)
        positionx=positionx+12
        self.cell(6, positionx, '  2. Understanding the NMEs (Diseases) ..............................................................................', 0, 0, 'L', 0)
        self.cell(0,positionx,'4',0, 0, 'R', 0)
        positionx=positionx+12
        self.cell(6, positionx, '  3. Identifying the Employees and their Families (members) that Need to Act.................................', 0, 0, 'L', 0)
        self.cell(0,positionx,'4',0, 0, 'R', 0)
        positionx=positionx+12
        self.cell(6, positionx, '  Engaging & Educating Members................................................................................................................', 0, 0, 'L', 0)
        self.cell(0,positionx,'4',0, 0, 'R', 0)
        positionx=positionx+12
        self.cell(6, positionx, '  4. Making Contact..............................................................................................................................', 0, 0, 'L', 0)
        self.cell(0,positionx,'4',0, 0, 'R', 0)
        positionx=positionx+12
        self.cell(6, positionx, '  5. PHA Increasing Health Literacy & Risk Reducing Action! ..............................................................', 0, 0, 'L', 0)
        self.cell(0,positionx,'4',0, 0, 'R', 0)
        positionx=positionx+12
        self.cell(6, positionx, '  6. Matching Members with Key Resources: Ending Medical Homelessness: Engaging Primary Care\
(PCP)......................................................................................................................................................', 0, 0, 'L', 0)
        self.cell(0,positionx,'4',0, 0, 'R', 0)
        positionx=positionx+12
        self.cell(6, positionx, '  7. Closing Gaps in Care & Following Safe Pathways ..........................................................................', 0, 0, 'L', 0)
        self.cell(0,positionx,'4',0, 0, 'R', 0)
        positionx=positionx+12
        self.cell(6, positionx, '  8. Ongoing Keys for Success ..............................................................................................................', 0, 0, 'L', 0)
        self.cell(0,positionx,'4',0, 0, 'R', 0)
        positionx=positionx+12
        self.cell(6, positionx, 'The MyPHA ROI..........................................................................................................................................', 0, 0, 'L', 0)
        self.cell(0,positionx,'4',0, 0, 'R', 0)
        positionx=positionx+12
        self.cell(6, positionx, '  Time .......................................................................................................................................................', 0, 0, 'L', 0)
        self.cell(0,positionx,'4',0, 0, 'R', 0)
        positionx=positionx+12
        self.cell(6, positionx, '  Energy & Stress = Distraction & Presenteeism......................................................................................', 0, 0, 'L', 0)
        self.cell(0,positionx,'4',0, 0, 'R', 0)
        positionx=positionx+12
        self.cell(6, positionx, '  Convenience – Keeping Up Positive Momentum .................................................................................', 0, 0, 'L', 0)
        self.cell(0,positionx,'4',0, 0, 'R', 0)
        positionx=positionx+12
        self.cell(6, positionx, '  Primary Care – A 21% Return – Solving Medical Homelessness .........................................................', 0, 0, 'L', 0)
        self.cell(0,positionx,'4',0, 0, 'R', 0)
        positionx=positionx+12
        self.cell(6, positionx, '  Medications – Cost & Compliance.......................................................................................................', 0, 0, 'L', 0)
        self.cell(0,positionx,'4',0, 0, 'R', 0)
        positionx=positionx+12
        self.cell(6, positionx, '  Specialists – Avoiding the “More Medicine is Better Medicine” Mentality........................................', 0, 0, 'L', 0)
        self.cell(0,positionx,'4',0, 0, 'R', 0)
        positionx=positionx+12
        self.cell(6, positionx, '  Imaging ................................................................................................................................................', 0, 0, 'L', 0)
        self.cell(0,positionx,'4',0, 0, 'R', 0)
        positionx=positionx+12
        self.cell(6, positionx, '  The Importance of Using Data – Data Leads to Wisdom.....................................................................', 0, 0, 'L', 0)
        self.cell(0,positionx,'4',0, 0, 'R', 0)
        positionx=positionx+12
        self.cell(6, positionx, '  ROI Analysis of MyPHA ........................................................................................................................', 0, 0, 'L', 0)
        self.cell(0,positionx,'4',0, 0, 'R', 0)
        positionx=positionx+12
        self.cell(6, positionx, '  Conclusion – Doing What We Know ........................................................................................................', 0, 0, 'L', 0)
        self.cell(0,positionx,'4',0, 0, 'R', 0)

    def first_page(self):
      pdf.add_page()
      pdf.image("ScreenShot2021-10-18at12_30_45PM.png", 0, 0, 210, 222)
      pdf.report_title_details()
      pdf.logos()

    def second_page(self):
      pdf.add_page()
      pdf.set_font('Arial', '', 16)
      pdf.cell(0,0,'Health Risk Analysis and Reduction Report',0, 0, 'L', 0)
      pdf.link(0, 30, 50, 12, "https://google.com")
      pdf.ln(8)
      pdf.chapter_title('Contents')
      
      pdf.contents()

    def third_page(self):
      pdf.add_page()
      pdf.chapter_title('Executive Summary')
      # pdf.set_font('Arial', 'B', 16)
      pdf.content()
      pdf.output('test.pdf', 'F')

if os.path.exists("test.txt"):
  os.remove("test.txt")

now=datetime.datetime.now()
day=now.strftime("%A, %B %d, %Y")

pdf=PDF()
#Cover page
pdf.first_page()

#Contents page
pdf.second_page()

#Executive summary page
pdf.third_page()
