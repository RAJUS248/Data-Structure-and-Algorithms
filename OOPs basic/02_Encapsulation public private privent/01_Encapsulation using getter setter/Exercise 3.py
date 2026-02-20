class Temperature:
    def __init__(self,celsius):
        self.__celsius = celsius

    @property

    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self,new_celsius):
        if new_celsius >= -273.15:
            self.__celsius = new_celsius

        else:
            print("❌ Invalid temperature!")

    @property
    def fahrenheit(self):
        return (self.__celsius * 9/5) + 32
    

    @fahrenheit.setter
    def fahrenheit(self,new_celsius):
        self.__celsius = (new_celsius - 32) * 5/9

t = Temperature(25)

print(t.celsius)      # 25
print(t.fahrenheit)   # 77.0

t.fahrenheit = 212    # set via Fahrenheit
print(t.celsius)      # 100
print(t.fahrenheit)   # 212.0
