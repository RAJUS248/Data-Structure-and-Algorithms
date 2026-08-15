class Complex:

    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(f'{self.real}  + {self.img} i')

    def add(num1,num2):
        newReal = num1.real + num2.real
        newimg = num1.img + num2.img
        return Complex(newReal,newimg)
    
    def __add__(num1,num2):
        newReal = num1.real + num2.real
        newimg = num1.img + num2.img
        return Complex(newReal,newimg)
        

num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(2,4)
num2.showNumber()

num3 = num1.add(num2)
num3.showNumber()

num3 = num1 + num2
num3.showNumber()