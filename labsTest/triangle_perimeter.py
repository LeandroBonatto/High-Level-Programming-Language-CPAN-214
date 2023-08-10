def is_valid_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

a = float(input("Enter first edge length: "))
b = float(input("Enter second edge length: "))
c = float(input("Enter third edge length: "))

if is_valid_triangle(a, b, c):
    perimeter = a + b + c
    print("Perimeter:", perimeter)
else:
    print("Input is invalid.")