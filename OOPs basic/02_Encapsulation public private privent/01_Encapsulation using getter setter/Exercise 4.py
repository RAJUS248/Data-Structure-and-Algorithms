class Shape:
    def __init__(self):
        raise NotImplementedError("Subclass must implement area()")
    

class Rectangle(Shape):
    def __init__(self,length, width):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self,new_length):
        if new_length > 0:
            self.__length = new_length

        else:
            print("❌ Invalid length")

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self,new_width):
        if new_width > 0:
            self.__width = new_width

        else:
            print("❌ Invalid width")

    def area(self):
        return self.__length * self.__width

class Circle(Shape):
    def __init__(self,radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self,new_radius):
        if new_radius > 0:
            self.__radius = new_radius

        else:
            print("❌ Invalid radius")

    def area(self):
        return 3.14 * (self.__radius ** 2)
    
r = Rectangle(10, 5)
print(r.area())   # 50

r.length = 20     # using setter
r.width = -3      # ❌ Invalid width
print(r.area())   # 100

c = Circle(7)
print(c.area())   # 153.86

c.radius = 10     # using setter
print(c.area())   # 314.0
