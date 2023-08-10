class Account:
    def __init__(self, id=0, balance=100, annual_interest_rate=0):
        self.__id = id
        self.__balance = balance
        self.__annual_interest_rate = annual_interest_rate

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def get_annual_interest_rate(self):
        return self.__annual_interest_rate

    def set_annual_interest_rate(self, annual_interest_rate):
        self.__annual_interest_rate = annual_interest_rate

    def get_monthly_interest_rate(self):
        return self.__annual_interest_rate / 12

    def get_monthly_interest(self):
        return self.__balance * self.get_monthly_interest_rate() / 100

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

def main():
    acc1 = Account(1122, 20000, 4.5)
    acc1.withdraw(2500)
    acc1.deposit(3000)

    print("Acc ID: {}"
          "\nBalance: {}"
          "\nMonthly Interest Rate: {}"
          "\nMonthly Interest: {}".format(acc1.get_id(), acc1.get_balance(), acc1.get_monthly_interest_rate(),
                                          acc1.get_monthly_interest()))

main()


