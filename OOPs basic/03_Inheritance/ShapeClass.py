class Shape:
    def __init__(self,name):
        self.name = name

    def area(self):
        print("Area not defined for generic shape")

class Rectangle(Shape):

    def __init__(self, name,length,width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self): # method over loading
        super().area()
        print(f"area of rectangle {self.length * self.width}")

class Circle(Shape):

    def __init__(self, name,radius):
        super().__init__(name)
        self.radius = radius

    def area(self):     # method over loading
        super().area()   # calling parent  Ovirride
        print(f"area of circle is {3.14 * self.radius ** 2}")

rectangle = Rectangle("rectangle",20,10)
circle = Circle("circle",5)
rectangle.length = 25      # updating
rectangle.area()
circle.area()

