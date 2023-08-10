class Rectangle:
    def __init__(self, width=1.0, height=2.0):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def get_total_area(self):
        return self.__width * self.__height

    def get_total_perimeter(self):
        return 2 * (self.__width + self.__height)

rectangle1 = Rectangle(4.0, 40.0)
rectangle2 = Rectangle(3.5, 35.7)

print("Rectangle 1 with a width of ", rectangle1.get_width(), "and a height of ",
      rectangle1.get_height(), "has area of ",  rectangle1.get_total_area(),
      "and perimeter of", rectangle1.get_total_perimeter())

print("Rectangle 2 with a width of ", rectangle2.get_width(), "and a height of ",
      rectangle2.get_height(), "has area of ", rectangle2.get_total_area(),
      "and perimeter of", rectangle2.get_total_perimeter())

