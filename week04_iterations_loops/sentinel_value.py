data = eval(input('Enter an integer (the input exits ' +
                  'if the input is 0): '))

# Keep reading data until the input is 0
sum_of_data = 0
while data != 0:
    sum_of_data += data

    data = eval(input('Enter an integer (the input exits ' +
                      'if the input is 0): '))

print('The sum is', sum_of_data)
