class Animal:
    def sound(self):
        return "Some generic animal sound"
        
class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return "Meow"

# Function that works with any animal
def make_sound(animal):
    print(animal.sound())

# List of different animals
animals = [Dog(), Cat(), Animal()]

# Polymorphism with loop
for animal in animals:
    print(animal.sound())  

print("------")

# Polymorphism with function
make_sound(Dog())   # Bark
make_sound(Cat())   # Meow
make_sound(Animal()) # Some generic animal sound
