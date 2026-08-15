class Employee:

    def __init__(self,name,salary,pin):
        self.name = name
        self._salary = salary
        self.__pin = pin

    def show_details(self):

        print(f'public name : {self.name}')
        print(f'protect salary : {self._salary}')
        print(f'private : {self.__pin}')

emp = Employee('raja',100000,2428)
emp.show_details()
print(emp.name)
print(emp._salary)

try:
    print(emp.__pin)

except AttributeError:
    print("cannot access __pin directly")

# Screate way to acess private
# Python renames it to ClassName_variableName internally
print(emp._Employee__pin)

class Manager(Employee):

    def show_acess(self):

        print(f'manager accessing name: {self.name}')

        print(f'manager accessing salary: {self._salary}')

        try: 
            print(f'manager accessing pin: {self.__pin}')

        except ArithmeticError:
            print(f'manager cannot accessing pin:')

mngr = Manager('ram',123400,1234)
mngr.show_acess()


