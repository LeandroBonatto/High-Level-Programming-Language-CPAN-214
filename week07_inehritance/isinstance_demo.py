from circle import Circle
from rectangle import Rectangle


def main():
    # Display circle and rectangle properties
    c = Circle(4)
    r = Rectangle(1, 3)
    print("Circle...")
    display_object(c)
    print("Rectangle...")
    display_object(r)


# Display geometric object properties
def display_object(g):
    print("Area is", g.get_area())
    print("Perimeter is", g.get_perimeter())

    if isinstance(g, Circle):
        print("Diameter is", g.get_diameter())
    elif isinstance(g, Rectangle):
        print("Width is", g.get_width())
        print("Height is", g.get_height())


main()  # Call the main function
