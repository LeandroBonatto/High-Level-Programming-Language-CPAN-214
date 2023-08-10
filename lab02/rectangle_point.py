coord1, coord2 = eval(input("Enter a point with two coordinates: "))

if coord1 <= 10/2 and coord2 <= 5/2:
    print('Point ({:.1f},{:.1f}) is in the rectangle'.format(coord1, coord2))
else:
    print('Point ({:.1f},{:.1f}) is not in the rectangle'.format(coord1, coord2))