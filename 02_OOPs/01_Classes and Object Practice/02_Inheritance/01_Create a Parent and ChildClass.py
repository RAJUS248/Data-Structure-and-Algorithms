# Create a Parent Class
class Person:

    def __init__(self,fname,lname):

        self.fname = fname
        self.lname = lname

    def printname(self):

        print(self.fname,self.lname)

# Create a Child Class

class Student(Person):

    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.gaduateyear = year

    def welcome(self):
        print(f"welcome {self.fname} {self.lname} to the class of {self.gaduateyear}")


p = Person('raj','b')
p.printname()

p1 = Student('raj','b',2025)
p1.welcome()
       