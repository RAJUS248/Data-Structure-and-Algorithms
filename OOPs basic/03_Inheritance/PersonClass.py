class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def show_student_info(self):
        self.show_info()    # it may be call here 
        print(f"Student ID: {self.student_id}")

student1 = Student("raja", 20, "2AG21CS081")
# student1.show_info()    # or it may be call here 
student1.show_student_info()

class Employee(Person):

    def __init__(self, name, age, position, salary):
        super().__init__(name, age)
        self.position = position
        self.salary = salary

    def show_details(self):
        self.show_info()
        print(f"Position: {self.position}, salary: {self.salary}")

# employee1 = Employee("raja",22,"software developer",100000 )
# employee1.show_details()


class Manager(Employee):

    def __init__(self, name,age,position,salary,department):
        super().__init__(name,age, position,salary)
        self.department = department

    def show_department_info(self):   
        self.show_details()
        print(f"Department: {self.department}")

department1 = Manager("raja",22,"developer",100000,"CSE" )
department1.show_department_info()
department1.show_info()

