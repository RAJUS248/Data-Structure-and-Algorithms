class Employee:
    def __init__(self,salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary
    

    @salary.setter
    def salary(self,new_salary):
        if new_salary >= 0:
            self.__salary =new_salary

        else:
            print("❌ Invalid salary")

    def annual_bonus(self):
         
        return (self.__salary * 10)// 100
    
    def display(self):
        print(f"Salary: {self.__salary }, Bonus: {self.annual_bonus()}")


e = Employee(50000)
print(e.salary)          # 50000
print(e.annual_bonus())  # 5000

e.salary = -1000         # ❌ Invalid salary
print(e.salary)          # 50000 (unchanged)
e.display()

        