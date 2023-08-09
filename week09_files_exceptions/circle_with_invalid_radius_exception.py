import math

class Circle:
    def __init__(self, radius=1):
        self.set_radius(radius)

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            raise InvalidRadiusException(radius)

    def get_area(self):
        return math.pi * self.__radius ** 2

class InvalidRadiusException(RuntimeError):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def get_radius(self):
        return self.__radius
