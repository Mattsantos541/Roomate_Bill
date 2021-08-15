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

    def pay(self, bill):
        pass


class PdfReport:
    """Create a Pdf file that contains data about the flatmates:
    their names, due amount, period of the bill"""

    def __init__(self, filename):
        self.filename = filename

    def generate( self, flatmate1, flatmate2, bill):
        pass
