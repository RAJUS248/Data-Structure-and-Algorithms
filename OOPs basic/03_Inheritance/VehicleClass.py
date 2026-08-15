class Vehicle:

    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

    def description(self):
        print("this is the vehicle")

class Car(Vehicle):

    def __init__(self, brand, year):
        super().__init__(brand, year)

    def description(self):
        
        print("This is a car")

class Bike(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand, year)

    def description(self):

        print("This is a bike.")


v1 = Vehicle("Honda",2020)
c1 = Car("tata", 2020)
b1 = Bike("Bajaj", 2028)

v1.description()
c1.description()
b1.description()