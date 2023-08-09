class BMI:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height

    def get_bmi(self):
        kilograms_per_pound = 0.45359237
        meters_per_inch = 0.0254
        bmi = self.__weight * kilograms_per_pound / \
              (self.__height * meters_per_inch) * \
              (self.__height * meters_per_inch)
        return round(bmi * 100) / 100

    def get_status(self):
        bmi = self.get_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_weight(self):
        return self.__weight

    def get_height(self):
        return self.__height
