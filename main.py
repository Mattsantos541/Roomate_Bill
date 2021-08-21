from FPDF import FPDF

class Bill:
    """
    Object contains data of bill such as total amount and period of bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """Create a flatmate person who lives in the
    flat and pays a share of the bill"""

    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name

    def pay(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """Create a Pdf file that contains data about the flatmates:
    their names, due amount, period of the bill"""

    def __init__(self, filename):
        self.filename = filename

        def generate(self, flatmate1, flatmate2, bill):
            pdf = FPDF(orientation='P', unit='pt', format='A4')
            pdf.add_page()

            # Add the title
            pdf.set_font(family='Times', size=24, style='C')
            pdf.cell(w=0, h=80, txt="Roommate Bill", border=1, align="C", ln=1)

            # Insert period label and value
            pdf.cell(w=100, h=40, txt="Period:", border=1)
            pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

            # Insert name and due amount of the first flatmate
            pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
            pdf.cell(w=150, h=40, txt=flatmate1.pay(), border=1, ln=1)

            # Insert name and due amount of the second flatmate
            pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
            pdf.cell(w=150, h=40, txt=flatmate2.pay(), border=1, ln=1)

            pdf.output("bill.pdf")
the_bill = Bill(amount=120, period="March 2021")
john = Flatmate(name="john", days_in_house=20)
mary = Flatmate(name="mary", days_in_house=25)

print("John pays: ", john.pay(bill=the_bill, flatmate2=mary))
print("Mary pays: ", mary.pay(bill=the_bill, flatmate2=john))

pdf_report = PdfReport(filename= "Report1.pdf")
pdf_report.generate(flatmate1=john, flatmate2= mary, bill= the_bill)
