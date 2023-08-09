def get_area(radius):
    if radius < 0:
        raise RuntimeError("Negative radius")

    return radius * radius * 3.1415


try:
    print(get_area(5))
    print(get_area(-5))
except RuntimeError:
    print("Invalid radius")

print('>>> END <<<')
