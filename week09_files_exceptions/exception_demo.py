try:
    number1 = int(input("Enter an integer: "))
    number2 = int(input("Enter an integer: "))
    result = number1 / number2
    print("Result is " + str(result))
except ZeroDivisionError:  # Catch zero divisor error
    print("Division by zero!")
except:
    print("Something wrong in the input")
else:
    print("The else clause is executed if there is no exception.")
finally:
    print("The finally clause is executed in ALL cases.")

print('>>> END <<<')
