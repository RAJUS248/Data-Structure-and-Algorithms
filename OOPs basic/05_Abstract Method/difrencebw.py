# Inheritance   for check delete Abstract method
class Vehicle:
    def start_engine(self):
        print("Engine started.")

class Car(Vehicle):
    pass                # working without def

my_car = Car()
my_car.start_engine()  # Works fine, inherited from Vehicle

# Diffrence b/w Inheritance and abstract method

# Abstract method
from abc import ABC,abstractmethod  # this is importent
class Vehicle1(ABC):                # this is importent
    @abstractmethod                 # this is importent
    def start_engine1(self):
        print("Engine started.")

class Car1(Vehicle1):
    pass                    # not working without def

my_car = Car1()
my_car.start_engine1()  # Not Works fine, inherited from Vehicle
                        # ❌ ERROR — didn't implement start_engine
