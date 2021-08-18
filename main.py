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

    def __init__(self, name, days_in_the_house):
        self.days_in_the_house = days_in_the_house
        self.name = name

    def pays(self, bill, flatmate2):
        weight = self.days_in_the_house / (self.days_in_the_house + flatmate2.days_in_the_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """Create a Pdf file that contains data about the flatmates:
    their names, due amount, period of the bill"""

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):



the_bill = Bill(amount=120, period="March 2021")
john = Flatmate(name="John", days_in_the_house=20)
marry = Flatmate(name="Joe", days_in_the_house=25)

print("John pays: ", john.pays(bill=the_bill, flatmate2=marry))
print("Marry pays: ", marry.pays(bill=the_bill, flatmate2=john))