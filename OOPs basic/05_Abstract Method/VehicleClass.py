from abc import ABC,abstractmethod

class Vehicle(ABC):  # Abstract class

    @abstractmethod

    def start_engine(self):

        pass

class Car(Vehicle):
    def start_engine(self):
        print("car engine started with a key")

class Bike(Vehicle):
    pass  # Forgot to define start_engine()


my_bike = Bike()  # ❌ ERROR

my_car = Car()
my_car.start_engine()