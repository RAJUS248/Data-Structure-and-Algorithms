class Car:
    def __init__(self,name,brand):
        self.name = name
        self.brand = brand

    def move(self):
        return 'drive'

class Boat:
    def __init__(self,name,brand):
        self.name = name
        self.brand = brand

    def move(self):
        return 'Sail'


class Plane:
    def __init__(self,name,brand):
        self.name = name
        self.brand = brand

    def move(self):
        return 'Flay'


car = Car('BMW24','BWM')
boat = Boat('RS28','RS')
plane = Plane('SR248','SR')

# car.move()
# boat.move()
# plane.move()

# or
print('----------------------')
for x in (car,boat,plane):
    print(x.name,x.brand,x.move())
    
    
        
        
        