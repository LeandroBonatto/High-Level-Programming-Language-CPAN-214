class Loan:
    def __init__(self, annual_interest_rate=2.5, number_of_years=1, loan_amount=1000, borrower=" "):
        self.__annual_interest_rate = annual_interest_rate
        self.__number_of_years = number_of_years
        self.__loan_amount = loan_amount
        self.__borrower = borrower

    def get_annual_interest_rate(self):
        return self.__annual_interest_rate

    def get_number_of_years(self):
        return self.__number_of_years

    def get_loan_amount(self):
        return self.__loan_amount

    def get_borrower(self):
        return self.__borrower

    def set_annual_interest_rate(self, annual_interest_rate):
        self.__annual_interest_rate = annual_interest_rate

    def set_number_of_years(self, number_of_years):
        self.__number_of_years = number_of_years

    def set_loan_amount(self, loan_amount):
        self.__loan_amount = loan_amount

    def set_borrower(self, borrower):
        self.__borrower = borrower

    def get_monthly_payment(self):
        monthly_interest_rate = self.__annual_interest_rate / 1200
        monthly_payment = \
            self.__loan_amount * monthly_interest_rate / (1 - (1 /
                                                               (1 + monthly_interest_rate) ** (
                                                                       self.__number_of_years * 12)))
        return monthly_payment

    def get_total_payment(self):
        total_payment = self.get_monthly_payment() * \
                        self.__number_of_years * 12
        return total_payment
