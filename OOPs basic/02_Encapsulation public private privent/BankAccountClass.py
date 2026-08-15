class BankAccount:
    
    def __init__(self,acc_holder,balance):
        self.acc_holder = acc_holder
        self.__balance = balance  # private

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        
        if amount > 0:
            self.__balance += amount
            print(f"Deposit: {amount}")
            return True
        else:
            print("Invalid deposit amount")
            return False

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"withdrawing: {amount}")
            return True
        else:
            print("Insufficient balance")
            return False
        
    def display(self):
        print(f"Account Holder: {self.acc_holder}")
        print(f"Current bal: {self.__balance}")

    
    
acc = BankAccount("raja",1000)

print("\ninitial balance")
acc.display()

print("\nAfter deposit")
acc.deposit(500)
acc.display()

print("\nAfter Withdrawal")
acc.withdraw(200)
acc.display()

print("\nFinal Balance:")
print(acc.get_balance())