class bank:
    def __init__(self,balance,number):
        self.__balance=balance
        self.__number=number
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if amount>self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance-=amount
    def get(self):
        return self.__balance
    def get2(self):
        return self.__number
c1=bank(1000,"123456789")
print(c1.get())