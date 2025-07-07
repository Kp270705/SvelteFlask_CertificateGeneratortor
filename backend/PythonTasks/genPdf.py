from fpdf import FPDF
import os
import shutil
import datetime as dt
from PythonTasks.getFonts import FONTS
from PythonTasks.fileHandle import checkPDFFolderExist
from PythonTasks.sendingMails import send_mails
# import io

def certChoice():

    certChoice = {
        "Choice1": "certificate1_2_3",
        "Choice2": "certificate1_2_3",
        "Choice3": "certificate1_2_3",
        "Choice4": "certificate4",
        "Choice5": "certificate5"
    }

    return certChoice



def add_spacing(input_string, spacing):
    spaced_string = ""
    for char in input_string:
        spaced_string += char + " " * spacing
    return spaced_string

def UpperCase(sentence):
    sentence = sentence.upper()
    return (sentence)

class PDF(FPDF):
    
    def header(self):
        # Add logo or header here if needed
        pass
    
    def footer(self):
        # Add footer here if needed
        pass 

    def load_fonts(self):
        for name, path in FONTS.items():
            style = "B" if "Bold" in name else ""   # crude style detection
            self.add_font(name, style, str(path))


# certificate design1:-        
    def certificate1_2_3(self, name, sId, receiver_mail, course, sem, date, eventname, orgname, i, certType, certificateChoice, action, text_color, organizer1_designation, organizer2_designation, PDF_bg):
        print(f"\n\n:In certificate1_2_3 method:\n")

        self.add_page(orientation="L")
        w = self.w
        h = self.h
        left_margin = 20  # OPTIONAL - Adjust this value for desired left padding
        right_margin = self.w - left_margin  # OPTIONAL - Calculate right margin based on page width
        self.image(f"{PDF_bg}", 0, 0, w, h)
        self.load_fonts()
        self.ln(30)

        sec1 = f"CERTIFICATE"
        # spacedSection1 = add_spacing(sec1, 1)
        self.section1 = f"{sec1}"
        self.set_font("Montserrat-Bold", size=38, style="B")
        self.set_text_color(text_color)
        self.multi_cell(270, 8, text=self.section1, align='C')
        self.ln(4)
        
        sec2 = f"{certType.upper()}"
        spacedSection2 = add_spacing(sec2, 1)
        self.section2 = f"{spacedSection2}"
        self.set_font(f"Montserrat-Medium", size=28)
        self.multi_cell(277, 8, text=self.section2, align='C')
        self.ln(3)
        
        sec3 = f"IS  PROUDLY  PRESENTED  TO"
        # spacedSection3 = add_spacing(sec3, 2)
        self.section3 = f"{sec3}"
        self.set_font("Montserrat-Regular", size=15)
        self.multi_cell(277, 20, text=self.section3, align='C')
        self.ln(5)
        
        spacedSection4 = add_spacing(name.upper(), 1)
        self.section4 = f"{spacedSection4}"
        self.set_font("Montserrat-Bold", size=30, style="UB")
        self.multi_cell(277, 5, text=self.section4, align='C')
        self.ln(6)

        spacedSection5a = add_spacing(course.upper(), 2)
        spacedSection5b = add_spacing(sem.upper(), 2)
        self.section5 = f"{spacedSection5a}                     {spacedSection5b}"
        self.set_font("Montserrat-Black", size=18, style="")
        self.multi_cell(277, 10, text=self.section5, align='C')
        self.ln(10)

        sec6 = ""
        if certType == "of participation":
            sec6 = f"For  participating  in"
        if certType == "of completion":
            sec6 = f"For  completing  the"
        if certType == "of appreciation":
            sec6 = f"For  completing  the"
        if certType == "of recognition":
            sec6 = f"For  completing  the"

        # spacedSection6 = add_spacing(sec6, 2)
        self.section6 = UpperCase(sec6)
        self.set_font("Montserrat-Regular", size=18)
        self.multi_cell(277, 8, text=self.section6, align='C')
        self.ln(8)

        spacedSection7 = add_spacing(eventname.upper(), 1)
        self.section7 = f"{spacedSection7}"
        self.set_font("Poppins-ExtraBold", size=18, style="B")
        self.multi_cell(277, 7, text=self.section7, align='C')
        self.ln(2)

        sec8 = f"ON"
        spacedSection8 = add_spacing(sec8, 1)
        self.section8 = f"{spacedSection8}"
        self.set_font("Poppins-Regular", size=13)
        self.multi_cell(277, 7, text=self.section8, align='C')
        self.ln(1)

        self.section9 = f"{date}"
        self.set_font("Poppins-ExtraBold", size=18, style="B")
        self.multi_cell(277, 10, text=self.section9, align='C')
        self.ln(20)  # Add some space after title

        auth1 = f"        {organizer1_designation}"
        auth2 = f"    {organizer2_designation}"
        spacedSection10a = add_spacing(auth1.upper(), 1)
        spacedSection10b = add_spacing(auth2.upper(), 1)
        self.section10 = f"{spacedSection10a}                   {spacedSection10b}"
        self.set_font("Montserrat-SemiBold", size=10, style="B")
        self.set_left_margin(65)
        self.cell(90, 3, text=f"{spacedSection10a}", align='C')
        self.set_left_margin(50)
        self.cell(50, 3, text=f"{spacedSection10b}", align='C')


# ----------------------------------------------------------------

    def certificate4(self, name, sId, receiver_mail, course, sem, date, eventname, orgname, i, certType, certificateChoice, action, text_color, organizer1_designation, organizer2_designation, PDF_bg):
        print(f"\n\n:In certificate4 method:\n")

        self.add_page(orientation="L")
        w = self.w
        h = self.h
        left_margin = 20  
        right_margin = self.w - left_margin  
        self.image(f"{PDF_bg}", 0, 0, w, h)
        self.load_fonts()
        self.ln(40)

        # self.section1 = f"C E R T I F I C A T E\n"
        sec1 = f"CERTIFICATE"
        # spacedSection1 = add_spacing(sec1, 1)
        self.section1 = f"{sec1}"
        self.set_font("Montserrat-Bold", size=38, style="B")
        self.set_text_color(text_color)
        self.multi_cell(270, 8, text=self.section1, align='C')
        self.ln(4)
        
        sec2 = f"{certType.upper()}"
        spacedSection2 = add_spacing(sec2, 1)
        self.section2 = f"{spacedSection2}"
        self.set_font(f"Montserrat-Medium", size=28)
        self.multi_cell(277, 8, text=self.section2, align='C')
        self.ln(5)
        
        sec3 = f"IS  PROUDLY  PRESENTED  TO"
        # spacedSection3 = add_spacing(sec3, 2)
        self.section3 = f"{sec3}"
        self.set_font("Montserrat-Regular", size=15)
        self.multi_cell(277, 20, text=self.section3, align='C')
        self.ln(7)
        
        spacedSection4 = add_spacing(name.upper(), 1)
        self.section4 = f"{spacedSection4}"
        self.set_font("Montserrat-Bold", size=25, style="B")
        self.multi_cell(277, 5, text=self.section4, align='C')
        self.ln(6)

        spacedSection5a = add_spacing(course.upper(), 2)
        spacedSection5b = add_spacing(sem.upper(), 2)
        self.section5 = f"{spacedSection5a}                     {spacedSection5b}"
        self.set_font("Montserrat-Black", size=15, style="")
        self.multi_cell(277, 10, text=self.section5, align='C')
        self.ln(10)
        
        # self.section6 = f"F O R   P A R T I C I P A T I N G  I N"
        sec6=""
        if certType == "of participation":
            sec6 = f"For  participating  in"
        if certType == "of completion":
            sec6 = f"For  completing  the"
        if certType == "of appreciation":
            sec6 = f"For  completing  the"
        if certType == "of recognition":
            sec6 = f"For  completing  the"
            
        # spacedSection6 = add_spacing(sec6, 2)
        self.section6 = f"{sec6}"
        self.set_font("Montserrat-Medium", size=20)
        self.multi_cell(277, 8, text=self.section6, align='C')
        self.ln(4)

        spacedSection7 = add_spacing(eventname.upper(), 0)
        self.section7 = f"{spacedSection7}"
        self.set_font("Poppins-SemiBold", size=18, style="B")
        self.multi_cell(277, 5, text=self.section7, align='C')
        self.ln(1)

        sec8 = f"ON"
        spacedSection8 = add_spacing(sec8, 1)
        self.section8 = f"{spacedSection8}"
        self.set_font("Poppins-Regular", size=13)
        self.multi_cell(277, 5, text=self.section8, align='C')
        self.ln(1)

        self.section9 = f"{date}"
        self.set_font("Poppins-SemiBold", size=18, style="B")
        self.multi_cell(277, 6, text=self.section9, align='C')
        self.ln(24)

        auth1 = f"    {organizer1_designation}"
        auth2 = f"    {organizer2_designation}"
        spacedSection10a = add_spacing(auth1.upper(), 0)
        spacedSection10b = add_spacing(auth2.upper(), 0)
        self.section10 = f"{spacedSection10a}                   {spacedSection10b}"
        self.set_font("Montserrat-Black", size=10, style="")
        self.set_left_margin(60)
        self.cell(100, 3, text=f"{spacedSection10a}", align='C')
        self.set_left_margin(160)
        self.cell(50, 3, text=f"{spacedSection10b}", align='C')       


# --------------------------------------------------------------------------

    def certificate5(self, name, sId, receiver_mail, course, sem, date, eventname, orgname, i, certType, certificateChoice, action, text_color, organizer1_designation, organizer2_designation, PDF_bg):
        print(f"\n\n:In certificate5 method:\n")

        self.add_page(orientation="L")
        w = self.w
        h = self.h
        left_margin = 20  
        right_margin = self.w - left_margin  
        self.image(f"{PDF_bg}", 0, 0, w, h)
        self.load_fonts()
        self.ln(20)

        sec1 = f"  CERTIFICATE"
        spacedSection1 = add_spacing(sec1, 3)
        self.section1 = f"{sec1}"
        self.set_font("Merriweather-Bold", size=25, style="B")
        self.set_text_color(2, 63, 48)
        self.multi_cell(270, 8, text=spacedSection1, align='C')
        self.ln(40)
        
        sec2 = f"{certType.upper()}"
        spacedSection2 = add_spacing(sec2, 1)
        self.section2 = f"{spacedSection2}"
        self.set_font("Merriweather-Regular", size=15)
        self.set_text_color(0)
        self.multi_cell(277, 8, text=spacedSection2, align='C')
        self.ln(3)
        
        sec3 = f"IS  PROUDLY  PRESENTED  TO"
        self.section3 = f"{sec3}"
        self.set_font("Montserrat-Regular", size=15)
        self.multi_cell(277, 20, text=self.section3, align='C')
        self.ln(6)
        
        spacedSection4 = add_spacing(name.upper(), 1)
        self.section4 = f"{spacedSection4}"
        self.set_font("Merriweather-Regular", size=25, style="U")
        self.set_text_color(218, 165,32)
        self.multi_cell(277, 5, text=self.section4, align='C')
        self.ln(6)

        spacedSection5a = add_spacing(course.upper(), 2)
        spacedSection5b = add_spacing(sem.upper(), 2)
        self.section5 = f"{spacedSection5a}                   {spacedSection5b}"
        self.set_font("Montserrat-Black", size=15, style="")
        self.set_text_color(0)
        self.multi_cell(277, 10, text=self.section5, align='C')
        self.ln(5)
        
        sec6=""
        if certType == "of participation":
            sec6 = f"For  participating  in"
        if certType == "of completion":
            sec6 = f"For  completing  the"
        if certType == "of appreciation":
            sec6 = f"For  completing  the"
        if certType == "of recognition":
            sec6 = f"For  completing  the"

        self.section6 = f"{sec6}"
        self.set_font("PlayfairDisplay-VariableFont_wght", size=15)
        self.set_left_margin(105)
        self.cell(18, 8, text=self.section6, align='L')


        spacedSection7 = add_spacing(eventname, 0)
        self.section7 = f"{spacedSection7}"
        self.set_font("Merriweather-Black", size=15, style="")
        self.set_left_margin(2)
        self.cell(100, 8, text=self.section7, align='C')
        self.ln(10)


        sec8 = f" ON"
        spacedSection8 = add_spacing(sec8, 1)
        self.section8 = f"{spacedSection8}"
        self.set_font("Poppins-Regular", size=13)
        self.multi_cell(277, 5, text=self.section8, align='C')
        self.ln(1)

        self.section9 = f" {date}"
        self.set_font("Poppins-SemiBold", size=18, style="B")
        self.multi_cell(277, 6, text=self.section9, align='C')
        self.ln(20)

        auth1 = f"    {organizer1_designation}"
        auth2 = f"    {organizer2_designation}"
        spacedSection10a = add_spacing(auth1.upper(), 1)
        spacedSection10b = add_spacing(auth2.upper(), 1)
        self.section10 = f"{spacedSection10a}   {spacedSection10b}"
        self.set_font("Montserrat-Black", size=10, style="")
        self.set_left_margin(80)
        self.cell(80, 3, text=f"{spacedSection10a}", align='C')
        self.set_left_margin(60)
        self.cell(60, 3, text=f"{spacedSection10b}", align='C')


# --------------------------------------------------------------------------     

def getCertData(csvData, eventname, orgName, certType, organizer1_designation, organizer2_designation, certificateChoice, action,  PDF_TemplatePath):
    # print(f"In getData...")
    print(f"\n------------------------------------------------------\n")
    
    for i, csv in enumerate(csvData, start=1):
        pdf = PDF()
        pdf.set_left_margin(10)
        pdf.set_right_margin(10)
        pdf.set_top_margin(10)
        pdf.set_auto_page_break(auto=True, margin=15)
        fontcolor = 0
        certgenArgs = []
        print(f"User{i} Data:")
        print(csv.name, csv.sId, csv.emailId, csv.course, csv.semester, csv.date)
        checkPDFFolderExist(i)

        if action == "Generate":
            if certificateChoice == "Choice1":
                pdf.certificate1_2_3(csv.name, csv.sId, csv.emailId, csv.course, csv.semester, csv.date,eventname, orgName, i, certType, certificateChoice, action, fontcolor, organizer1_designation, organizer2_designation, PDF_TemplatePath)

            if certificateChoice == "Choice2":
                pdf.certificate1_2_3(csv.name, csv.sId, csv.emailId, csv.course, csv.semester, csv.date, eventname, orgName, i, certType, certificateChoice, action, 0, organizer1_designation, organizer2_designation, PDF_TemplatePath)
            
            if certificateChoice == "Choice3":
                pdf.certificate1_2_3(csv.name, csv.sId, csv.emailId, csv.course, csv.semester, csv.date, eventname, orgName, i, certType, certificateChoice, action, 220, organizer1_designation, organizer2_designation, PDF_TemplatePath)
            
            if certificateChoice == "Choice4":
                pdf.certificate4(csv.name, csv.sId, csv.emailId, csv.course, csv.semester, csv.date, eventname, orgName, i, certType, certificateChoice, action, fontcolor, organizer1_designation, organizer2_designation, PDF_TemplatePath)

            print(f"\n{i} certificate is being generated...\n")
            pdf.output(f"./static/PDFFolder/{action}Certificate{i}.pdf")
            send_mails(f"kunalpathak4774@gmail.com", csv.emailId, f"./static/PDFFolder/{action}Certificate{i}.pdf", eventname, certType)


        if action == "Preview":
            if i>1: # this condition is for generating pdf for first row of csv file. Used in preview mode.
                print(f"\n\n\t-----In Preview mode only first rows data's certificate will be generated.-----\n")
                break
            if certificateChoice == "Choice1":
                pdf.certificate1_2_3(csv.name, csv.sId, csv.emailId, csv.course, csv.semester, csv.date,eventname, orgName, i, certType, certificateChoice, action, fontcolor, organizer1_designation, organizer2_designation, PDF_TemplatePath)

            if certificateChoice == "Choice2":
                pdf.certificate1_2_3(csv.name, csv.sId, csv.emailId, csv.course, csv.semester, csv.date, eventname, orgName, i, certType, certificateChoice, action, 220, organizer1_designation, organizer2_designation, PDF_TemplatePath)
            
            if certificateChoice == "Choice3":
                pdf.certificate1_2_3(csv.name, csv.sId, csv.emailId, csv.course, csv.semester, csv.date, eventname, orgName, i, certType, certificateChoice, action, 220, organizer1_designation, organizer2_designation, PDF_TemplatePath)
            
            if certificateChoice == "Choice4":
                pdf.certificate4(csv.name, csv.sId, csv.emailId, csv.course, csv.semester, csv.date, eventname, orgName, i, certType, certificateChoice, action, fontcolor, organizer1_designation, organizer2_designation, PDF_TemplatePath)
            print(f"\n Preview of {i} certificate completed...\n")
            pdf.output(f"./static/PDFFolder/{action}Certificate{i}.pdf")
            print(f"\n\n------------------------------------------------------\n")
            # here we did not send any email, because it is just preview of selected certificate.
