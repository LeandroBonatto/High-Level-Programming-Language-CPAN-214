def print_area(width=1, height=2):
    area = width * height
    print("width:", width, "\theight:", height, "\tarea:", area)


print_area()  # Default arguments width = 1 and height = 2
print_area(4, 2.5)  # Positional arguments' width = 4 and height = 2.5
print_area(height=5, width=3)  # Keyword arguments width
print_area(width=1.2)  # Default height = 2
print_area(height=6.2)  # Default width = 1
