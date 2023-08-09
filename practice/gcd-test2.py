def gcd(value1, value2):
    while value2:
        value1, value2 = value2, value1 % value2
    return value1

value1 = float(input("Please Enter the first number: "))
value2 = float(input("Please Enter the second number: "))

print(gcd(value1, value2))