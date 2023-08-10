sum_of_stu = eval(input('Enter the number of students: '))
namestu1 = ''
namestu2 = ''
highestscore1 = 0
highestscore2 = 0

if sum_of_stu == 1:
    print('You must introduce two or more students')
else:
    eval(input('Enter the number of students: '))

    for i in range(sum_of_stu):
        name = str(input('Enter a student name: '))
        score = eval(input('Enter a student score: '))
    if score > highestscore1:
        namestu1, namestu2 = highestscore1
        highestscore1, highestscore2 = namestu1
    elif score > highestscore2:
        namestu2, namestu1 = highestscore2
        highestscore2, highestscore1 = namestu2

print('Top two students:')
print('{}`s score is {}'.format(namestu1, highestscore1))
print('{}`s score is {}'.format(namestu2, highestscore2))



