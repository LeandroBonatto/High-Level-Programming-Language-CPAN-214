from bmi import BMI

def main():
    bmi1 = BMI("John Doe", 28, 120, 85)
    print("The BMI for", bmi1.get_name(), "is",
          bmi1.get_bmi(), bmi1.get_status())

    bmi2 = BMI("Peter King", 42, 115, 70)
    print("The BMI for", bmi2.get_name(), "is",
          bmi2.get_bmi(), bmi2.get_status())

main()  # Call the main function
