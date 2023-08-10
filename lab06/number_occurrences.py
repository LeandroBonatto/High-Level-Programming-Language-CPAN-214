numbers_counts = 0
numbers = []

for number in numbers:
    if number in numbers_counts:
        numbers_counts[number] += 1
    else:
        numbers_counts[number] = 1

numbers_counts = {}
num = (input('Enter the numbers: '))
totnumcount = max(numbers_counts.values())
totnum = [[numbers_counts, number] for (number, numbers_counts.items()) in totnumcount]

if len(totnum) == 1:
    print('The number with the most occurrence is {}'.format(totnum))
else:
    if len(totnum) == 2:
        print('The number with the most occurrence are {} and {}'.format(totnum[0], totnum[1]))