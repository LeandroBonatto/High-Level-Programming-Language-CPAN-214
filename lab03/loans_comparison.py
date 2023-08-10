loanAmount = float(input("Enter loan amount: "))
numberOfYears = int(input("Enter number of years as an integer: "))
monthlyInterestRate: 0

monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
totalPayment = monthlyPayment * numberOfYears * 12
monthlyPayment *= 100 / 100
totalPayment *= 100 / 100

for monthlyInterestRate (5000, 8000, 125):
        monthlyInterestRate /= 1000
        monthlyPayment, totalPayment

print('Interest Rate: {}%'.format(monthlyInterestRate))
print('Monthly Payment: {}'.format(monthlyPayment))
print('Total Payment: {}'.format(totalPayment))
