from Geometric_Shape import GeometricShape

class Triangle(GeometricShape):
    def __init__(self, side1=3.0, side2=4.0, side3=5.0, colour="gray", filled=False):
        super().__init__(colour, filled)
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def get_side1(self):
        return self.__side1

    def set_side1(self, side1):
        self.__side1 = side1

    def get_side2(self):
        return self.__side2

    def set_side2(self, side2):
        self.__side2 = side2

    def get_side3(self):
        return self.__side3

    def set_side3(self, side3):
        self.__side3 = side3

    def get_perimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def get_area(self):
        return (self.get_perimeter * (self.get_perimeter - self.__side1)*(self._perimeter - self.__side2) * (self.get_perimeter - self.__side3)) ** 0.5

    def __str__(self):
        return super().__str__() + "Triangle has side1: " + str(self.__side1) \
    + " side2: " + str(self.__side2) + " side3: " + str(self.__side3) \
    + " Area: " + str(self.__area) + " Perimeter: " + str(self.__perimeter)

def main():
    side1 = float(input("Enter side1: "))
    side2 = float(input("Enter side2: "))
    side3 = float(input("Enter side3: "))

    triangle = Triangle(side1, side2, side3)

    print("Area: " + triangle.get_area())

main()