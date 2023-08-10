def compare_prices(weight1, price1, weight2, price2):
    price_per_kg1 = price1 / weight1
    price_per_kg2 = price2 / weight2
    if price_per_kg1 < price_per_kg2:
        return 1
    elif price_per_kg1 > price_per_kg2:
        return 2
    else:
        return 0

weight1 = float(input("Enter weight of first package (kg): "))
price1 = float(input("Enter price of first package ($): "))
weight2 = float(input("Enter weight of second package (kg): "))
price2 = float(input("Enter price of second package ($): "))

result = compare_prices(weight1, price1, weight2, price2)

if result == 1:
    print("First package has a better price.")
elif result == 2:
    print("Second package has a better price.")
else:
    print("Both packages have the same price.")