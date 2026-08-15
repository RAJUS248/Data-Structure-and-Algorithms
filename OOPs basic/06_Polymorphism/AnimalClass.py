class Animal:
    def sound(self):
        
        return "Some generic animal sound"
        
class dog(Animal):
    def sound(self):
        return "bark"
    
class cat(Animal):

    def sound(self):
        return "meow"
    
   
    
animals = [dog(),cat(),Animal()]

for animal in animals:

    print(animal.sound())  

    