import random

def playdice():
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    sum = roll1, roll2

    if sum == 2 or sum == 3 or sum == 12:
        print("You rolled {} + {} = {}".format(roll1, roll2, sum))
        print("You lose")
    elif sum == 7 or 11:
        print("You rolled {} + {} = {}".format(roll1, roll2, sum))
        print("You win")

def pointvalue(calc=0):
    roll1, roll2 = playdice()
    sum = roll1, roll2
    while sum != calc or sum != 7:
        print("You rolled {} + {} = {}".format(roll1, roll2, sum))
    if sum == calc:
        print("You win")
        return True
    elif sum == 7:
        print("You lose")
        return False

playdice()