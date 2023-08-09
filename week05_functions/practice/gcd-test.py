first = float(input(" Please Enter the First Value: "))
sec = float(input(" Please Enter the Second Value: "))

i = 1
while (i <= first and i <= sec):
    if (first % i == 0 and sec % i == 0):
        val = i
    i += 1

print("\n GCD of {0} and {1} = {2}".format(first, sec, val))