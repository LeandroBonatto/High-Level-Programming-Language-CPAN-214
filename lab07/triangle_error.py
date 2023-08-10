import math

class GeometricShape:
    def __init__(self, colour="black", filled=False):
        self.__colour = colour
        self.__filled = filled

    def get_colour(self):
        return self.__colour

    def set_colour(self, colour):
        self.__colour = colour

    def is_filled(self):
        return self.__filled

    def set_filled(self, filled):
        self.__filled = filled

    def __str__(self):
        return "colour: " + self.get_colour() + " and filled: " + str(self.is_filled())

class Triangle(GeometricShape):
    def __init__(self, side1, side2, side3):
        super().__init__(self)
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def get_side1(self):
        return self.__side1

    def get_side2(self):
        return self.__side2

    def get_side3(self):
        return self.__side3

    def set_side1(self, s1):
        self.__side1 = s1

    def set_side2(self, s2):
        self.__side2 = s2

    def set_side3(self, s3):
        self.__side3 = s3

    def get_area(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        return math.sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))

    def get_perimeter(self):
        return self.__side1 + self.__side2 + self.__side3

class TriangleError(RuntimeError):
    def __init__(self, s1=4, s2=6, s3=13):
        super().__init__(self)
        self.__s1 = s1
        self.__s2 = s2
        self.__s3 = s3

    def get_s1(self):
        return self.__s1

    def get_s2(self):
        return self.__s2

    def get_s3(self):
        return self.__s3

    def sides_values(self, s1, s2, s3):
        try:
            totaledge = 0
            if s1 < s2 + s3 and s1 < s2 + s3 and s1 < s2 + s3:
                print('The perimeter is {}'.format(totaledge))
        except:
            raise RuntimeError('Error! The sum of every pair of two sides must be '
                               'greater than the remaining side')


    def __str__(self):
        return "Triangle: side1 = " + str(self.get_s1()) + ", side2 = " + str(
        self.get_s2()) + ", and side3 = " + str(self.get_s3())
