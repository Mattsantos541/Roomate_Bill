from flat import Bill, Flatmate
from reports import PdfReport

amount = float(input("Hey user, enter the bill amount: "))
print("This is a", amount)
period = input("what is the bill period? E.g. December 2021")
name1 = input("What is your name? ")
days_in_house1 = int(input(f"how many days did {name1} stay in the house during the bill period? "))
name2 = input("What is name of other flatmate?  ")
days_in_house2 = int(input(f"how many days did {name2} stay in the house during the bill period? "))

the_bill = Bill(amount, period="March 2021")
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{name1} pays: ", flatmate1.pay(the_bill, flatmate2))
print(f"{name2} pays: ", flatmate2.pay(the_bill, flatmate2))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1, flatmate2, bill=the_bill)
