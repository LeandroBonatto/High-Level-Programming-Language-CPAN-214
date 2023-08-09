from geometric_shape import GeometricShape
import math

class Circle(GeometricShape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_area(self):
        return self.__radius * self.__radius * math.pi

    def get_diameter(self):
        return 2 * self.__radius

    def get_perimeter(self):
        return 2 * self.__radius * math.pi

    def print_circle(self):
        print(self.__str__() + " radius: " + str(self.__radius))

    # Other methods are omitted
    # Override the __str__ method defined in GeometricObject
    def __str__(self):
        return super().__str__() + " and also radius: " + str(self.__radius)


c1 = Circle(10)
c1.set_radius(100)
c1.set_colour('red')

print('>>> END <<<')
