class Vehicle:
    def __init__(self,name,brand):
        self.name = name
        self.brand = brand

    def move(self):
        return 'Move!'

class Car(Vehicle):
    pass
    
class Boat(Vehicle):  

    def move(self):
        return 'Sail'


class Plane(Vehicle):

    def move(self):
        return 'Flay'
    

car = Car('BMW24','BWM')
boat = Boat('RS28','RS')
plane = Plane('SR248','SR')

print('----------------------')
for x in (car,boat,plane):
    print(x.name,x.brand,x.move())