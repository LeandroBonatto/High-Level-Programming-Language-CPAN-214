class Seller():
    def __init__(self, name):
        self.name = name
        self.sales = 0

    def sold(self, sales):
        self.sales = sales

    def goal_performed(self, goal):
        if self.sales > goal:
            print(self.name, "Hit the goal")
        else:
            print(self.name, "Didn't hit the goal")

Seller1 = Seller("Lira")
Seller1.sold(1000)
Seller1.goal_performed(600)

Seller2 = Seller("John")
Seller2.sold(300)
Seller2.goal_performed(500)