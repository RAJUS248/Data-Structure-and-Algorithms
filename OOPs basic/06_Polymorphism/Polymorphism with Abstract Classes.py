from abc import ABC , abstractmethod

class Animal(ABC):
    @abstractmethod

    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"
    
class Cat(Animal):
    def sound(self):
        return "Meow!"
    
animals = [Dog(),Cat(),Animal()]    # ✅ Removed Animal() run

for animal in animals:
    print(animal.sound())

