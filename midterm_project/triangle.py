from Geometric_Shape import GeometricShape

class Triangle(GeometricShape):
    def __init__(self, side1=3.0, side2=4.0, side3=5.0, color="gray", filled=False):
        super().__init__(color, filled)
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
    side1, side2, side3 = eval(input("Enter value side1, side2 and side3: "))
    filled = bool(int(input("Digit number 1 for filled triangle, otherwise digit 0: ")))
    color = input("Choose a color: ")

    triangle = Triangle(side1, side2, side3)
    triangle.set_filled(filled)
    triangle.set_color(color)

    print("Triangle has values sides of {}, {}, {}. "
          "\nArea: {}. "
          "\nPerimeter: {}. "
          "\nColor: {}. "
          "\nFilled: {}".format(triangle.get_side1(), triangle.get_side2(), triangle.get_side3(), triangle.get_area(), triangle.get_color(), triangle.is_filled()))

main()