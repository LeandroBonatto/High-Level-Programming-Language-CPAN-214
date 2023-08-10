weight1, price1 = eval(input("Enter weight and cost for package 1:"))
weight2, price2 = eval(input("Enter weight and cost for package 2:"))

betterprice1 = weight1 / price1
betterprice2 = weight2 / price2


if betterprice1 > betterprice2:
    print('Package 1 has the better price')
elif betterprice2 > betterprice1:
    print('Package 2 has the better price')
else:
    print('Both packages have the same price per unit.')



