from circle import Circle
from rectangle import Rectangle

def main():
    # Display circle and rectangle properties
    c = Circle(4)
    r = Rectangle(1, 3)
    display_object(c)
    display_object(r)
    print("Are the circle and rectangle the same size?", is_same_area(c, r))

# Display geometric object properties
def display_object(g):
    print(g.__str__())

# Compare the areas of two geometric objects
def is_same_area(g1, g2):
    return g1.get_area() == g2.get_area()

main()  # Call the main function
