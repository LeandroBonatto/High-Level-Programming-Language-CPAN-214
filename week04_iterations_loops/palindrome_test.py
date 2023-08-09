# Prompt the user to enter a string
s = input('Enter a string: ')

# The index of the first character in the string
low = 0

# The index of the last character in the string
high = len(s) - 1

is_palindrome = True
while low < high:
    if s[low] != s[high]:
        is_palindrome = False  # Not a palindrome
        break

    low += 1
    high -= 1

if is_palindrome:
    print(s, 'is a palindrome')
else:
    print(s, 'is not a palindrome')
