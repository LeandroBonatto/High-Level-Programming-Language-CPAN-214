# Prompt the user to enter the loan amount and loan period in years
loan_amount = float(input("Enter the loan amount: "))
loan_period = int(input("Enter the loan period in years: "))

# Calculate the number of months in the loan period
num_months = loan_period * 12

# Loop through each interest rate from 5% to 8% with an increment of 1/8
for i in range(5, 9):
  interest_rate = i / 100 / 12
  monthly_payment = loan_amount * interest_rate / (1 - (1 + interest_rate)**(-num_months))
  total_payment = monthly_payment * num_months
  print("Interest rate: {}%".format(i))
  print("Monthly payment: ${:.2f}".format(monthly_payment))
  print("Total payment: ${:.2f}".format(total_payment))
  print("")
