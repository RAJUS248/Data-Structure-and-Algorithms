class Product:

    def __init__(self, name, price):

        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price
    
    def set__price(self,new_price):
        if new_price >= 0:
            self.__price = new_price

        else:
            print("price connot be neggative")

    def display(self):
        print(f"product: {self.name}, Price: rs {self.__price}")

product1 = Product("Mobile", 10000)

print("initial",product1.get_price())
        

product1.set__price(35000)
product1.display()