class Bankaccount:
    def __init__(self,balance):
        self.__balance = balance    # private attribute

    def deposit(self,amount):
       self.__balance += amount    # update balance safely

    def get_balance(self):
        return self.__balance       # read balance safely
    
    
acc = Bankaccount(1000)

acc.deposit(500)
print(acc.get_balance())

acc.deposit(-100)
print(acc.get_balance())

        