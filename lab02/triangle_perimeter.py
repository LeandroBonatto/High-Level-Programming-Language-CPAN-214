edge1, edge2, edge3 = eval(input("Enter three edges: "))

totaledge = edge1 + edge2 + edge3

if edge1 < edge2 + edge3 and edge2 < edge1 + edge3 and edge3 < edge1 + edge2:
    print('The perimeter is {}'.format(totaledge))
else:
    print('The input is invalid')
