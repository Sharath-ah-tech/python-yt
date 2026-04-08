class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    def withdraw(self, amount):
        if self.__balance <=amount:
            print("Insufficient Balance")
        else:
            self.__balance-=amount
            print(f"Withdraw amount is {amount}")
    def deposit(self, amount):
        self.__balance+=amount
        print(f"Deposied amount is {amount}")
    def show(self):
        print(f"{self.name}, Your Balance amount is {self.__balance}")
b1=Bank("Shardhur", 10000)
b2=Bank("Satyarth", 20000)
b3=Bank("Sahil", 30000)

b1.deposit(5000)
b1.withdraw(25000)
b1.show()

b2.deposit(10000)
b2.withdraw(5000)
b2.show()

b3.deposit(2000)
b3.withdraw(150000)
b3.show()
