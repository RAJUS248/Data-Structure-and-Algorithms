class Person:

    def __init__(self,age):
        self.age = age

    def birthady(self):

        self.age += 1
        print(f'happy birthday now your {self.age}')

p = Person(23)
p.birthady()
p.birthady()


# The __str__() Method

# Without the __str__() method:

class Person2:

    def __init__(self,name,age):
        self.name = name
        self.age = age

p = Person2('raj',23)
print(p)
    

# With the __str__() method:

class Person3:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):

        return f'{self.name} and {self.age}'
        

p = Person3('raj',23)
print(p)
        