sum_of_nums = 0
number = 18

while number < 30:
    number += 1
    sum_of_nums += number
    print(number)
    if sum_of_nums >= 132:
        break

print('The number is', number)
print('The sum is', sum_of_nums)
