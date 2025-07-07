# def add(a,b):
#     print("Adding numbers")
#     return a + b

# def subtract(a,b):
#     print("Subtracting numbers")
#     return a - b

# def multiply(a,b):
#     print("Multiplying numbers")
#     return a * b

# def divide(a,b):
#     print("Dividing numbers")
#     return a / b

# if __name__ == "__main__":
#     dict1 = {
#         "add": add,
#         "subtract": subtract,
#         "multiply": multiply,
#         "divide": divide
#     }
#     input1 = input("Enter your fav operation: ")
#     print(f"Hello from main...")
#     res = dict1[input1](10, 5)
#     print(f"Result: {res}")

# =============================================

# test code for fpdf:

from fpdf import FPDF
import datetime as dt
from pdf_fonts import FONTS

# --------------------------------------------------------------------------

class PDF(FPDF):

    def load_fonts(self):
        for name, path in FONTS.items():
            style = "B" if "Bold" in name else ""   # crude style detection
            print(f"name: {name}")
            print(f"\tstyle:{style}\n")
            self.add_font(name, style, str(path))
        print(f"\tOut of loop")


# certificate design1:-        
    def certificate1_2_3(self):
        print(f"in certificate1_2_3 method...(of gen_pdf)")
        self.add_page(orientation="L")
        w = self.w
        h = self.h
        self.image(f"./static/Images/Home/FinalTemplate/finalTemplate.png", 0, 0, w, h)
        self.load_fonts()
        self.ln(30)

        sec1 = f"CERTIFICATE"
        self.section1 = f"{sec1}"
        self.set_font("Montserrat-Black", size=38, style="")
        self.set_text_color(0)
        self.multi_cell(270, 8, text=self.section1, align='C')
        self.ln(4)

# --------------------------------------------------------------------------     

if __name__ == "__main__":
    pdf = PDF()
    pdf.set_left_margin(10)
    pdf.set_right_margin(10)
    pdf.set_top_margin(10)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.certificate1_2_3()
    try:
        pdf.output(f"./TestCertificate1.pdf")
    except Exception as e:
        if not e:
            print("\n\npdf file generated\n\n")
        print(f"\n\nNo pdf file generated\nexception: {e}")
    print("\n\npdf file generated\n\n")
    
