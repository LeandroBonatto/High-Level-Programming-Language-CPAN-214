class GeometricShape(object):
    def __init__(self, colour="green", filled=True):
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
