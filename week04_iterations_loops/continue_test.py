sum = 0
number = 0

while number < 20:
    number += 1
    print("before continue:", number)
    if number == 10 or number == 11: 
        continue
    print("after  continue:", number)
    sum += number

print("The sum is", sum)
