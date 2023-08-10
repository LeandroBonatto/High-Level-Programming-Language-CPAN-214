class Account:
    def __init__(self, id=0, balance=100):
        self.__id = id
        self.__balance = balance

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def withdraw(self, amount):
            self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

accounts = [Account(i) for i in range(10)]

while True:
    id = int(input("Enter an account id: "))

    account = None
    for acc in accounts:
        if acc.get_id() == id:
            account = acc
            break

    if account == None:
        print("Incorrect id!")
        continue

    print("Main menu")
    print("1: check the balance")
    print("2: withdraw")
    print("3: deposit")
    print("4: exit")

    choice = int(input("Enter a choice: "))

    if choice == 1:
        print("The balance is: ", account.get_balance())
    elif choice == 2:
        amount = float(input("Enter an amount to withdraw: "))
        account.withdraw(amount)
        continue
    elif choice == 3:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
        continue
    elif choice == 4:
        break
    else:
        print("Invalid number.")
        continue