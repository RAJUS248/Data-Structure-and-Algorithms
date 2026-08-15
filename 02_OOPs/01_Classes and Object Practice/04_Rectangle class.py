class Rectangle:

    def __init__(self, height, width):

        self.height = height
        self.width = width
        
    def area(self):
        retangle_area = self.height * self.width
        print(f"total area of Reactangle {retangle_area}")

    def parameter(self):
        rectangle_parameter = 2 *(self.height + self.width)
        print(f"Parameter of Reactangle {rectangle_parameter}")

    def find(self):
        rectangle.area()
        rectangle.parameter()

rectangle = Rectangle(10,5)
rectangle.find()