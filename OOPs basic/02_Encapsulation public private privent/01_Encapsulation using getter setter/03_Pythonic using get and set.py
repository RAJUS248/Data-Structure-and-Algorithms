class Bankaccount:
    def __init__(self,balance):
        self.__balance = balance    # private attribute

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount    # update balance safely
        else:
            print("❌ Deposit amount must be positive!")

    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

        else:
            print("❌ Invalid withdrawal!")

    # Getter
    @property

    def balance(self):
        return self.__balance       # read balance safely
    
    # Setter
    @balance.setter
    
    def balance(self,new_balance):
        if new_balance >= 0:
            self.__balance = new_balance

        else:
             print("❌ Balance cannot be negative!")

    
    
acc = Bankaccount(1000)

acc.deposit(500)
print(acc.balance)

acc.deposit(-100)


acc.withdraw(100)
print(acc.balance)

acc.withdraw(-100)


acc.balance = 100        # directly set balance
print(acc.balance)

acc.balance = -100


        