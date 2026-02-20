class Employee:

    def __init__(self, name, position, salary):

        self.name = name
        self.position = position
        self.salary = salary

    def show_details(self):

        print(f"Name: {self.name} ")
        print(f"Position: {self.position}")
        print(f"Salary: {self.salary}")

employee1 = Employee("Raja","Developer",100000)
employee2 = Employee("Rani","Devops",100000)

employee1.show_details()
employee2.show_details()
        