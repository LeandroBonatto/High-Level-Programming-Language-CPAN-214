from circle_with_invalid_radius_exception import Circle
from circle_with_invalid_radius_exception import InvalidRadiusException

try:
    c1 = Circle(5)
    print("c1's area is", c1.get_area())
    c2 = Circle(-5)
    print("c2's area is", c2.get_area())
    c3 = Circle(0)
    print("c3's area is", c3.get_area())
except InvalidRadiusException as ex:  # Catch invalid radius
    print("Radius", ex.get_radius(), "is invalid")

print('>>> END <<<')
