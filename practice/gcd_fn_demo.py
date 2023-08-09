from gcd_fn import gcd_fn  # Import the module

# Prompt the user to enter two integers
n1 = eval(input('Enter the first integer: '))
n2 = eval(input('Enter the second integer: '))

print('The greatest common divisor for', n1, 'and', n2, 'is', gcd_fn(n1, n2))
