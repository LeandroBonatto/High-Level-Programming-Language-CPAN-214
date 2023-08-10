def sum_of_digits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10
    return sum

number = int(input("Enter an integer between 0 and 1000: "))

print("Sum of digits:", sum_of_digits(number))