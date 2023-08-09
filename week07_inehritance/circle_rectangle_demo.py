from circle import Circle
from rectangle import Rectangle

def main():
    circle = Circle(1.5)
    print("A circle", circle)
    print("The radius is", circle.get_radius())
    print("The area is", circle.get_area())
    print("The diameter is", circle.get_diameter())

    rectangle = Rectangle(2, 4)
    print("\nA rectangle", rectangle)
    print("The area is", rectangle.get_area())
    print("The perimeter is", rectangle.get_perimeter())

main()  # Call the main function
