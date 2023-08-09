# Prompt the user for input
purchaseAmount = eval(input("Enter purchase amount: "))  # enter 85

# Compute sales tax
tax = purchaseAmount * 0.13

# Display tax amount with two digits after decimal point
print("Sales tax is", int(tax * 100) / 100.0)
print("Sales tax is {:.2f}".format(tax))
print("Sales tax is", tax)