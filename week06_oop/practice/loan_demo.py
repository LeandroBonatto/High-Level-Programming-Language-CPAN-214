from loan import Loan

def main():
    # Enter yearly interest rate
    annual_interest_rate = eval(input
                              ("Enter yearly interest rate, for example, 7.25: "))

    # Enter number of years
    number_of_years = eval(input(
        "Enter number of years as an integer: "))

    # Enter loan amount
    loan_amount = eval(input(
        "Enter loan amount, for example, 120000.95: "))

    # Enter a borrower
    borrower = input("Enter a borrower's name: ")

    # Create a Loan object
    loan = Loan(annual_interest_rate, number_of_years,
                loan_amount, borrower)

    # Display loan date, monthly payment, and total payment
    print("The loan is for", loan.get_borrower())
    print("The monthly payment is", format(
        loan.get_monthly_payment(), '.2f'))
    print("The total payment is", format(
        loan.get_total_payment(), '.2f'))


main()  # Call the main function
