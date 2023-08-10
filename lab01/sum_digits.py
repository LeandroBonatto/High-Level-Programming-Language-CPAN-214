num = int(input('Enter a number between 0 and 1000: '))

first = num // 1000
num = num % 1000
sec = num / 100
num = num % 100
third = num // 10
fourth = num % 10
print("The sum of the digits is {}".format(first + sec + third + fourth))

