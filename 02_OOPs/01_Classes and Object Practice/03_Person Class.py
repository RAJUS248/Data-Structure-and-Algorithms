class Person:
    species = 'Human' # class property

    def __init__(self,name):
        self.name = name

    def greet(self):
        return f"hello {self.name}"

    def msg(self):

        message = self.greet()
        print(f'{message} welcome')

p = Person('raj')
p.msg()

p.name = 'ram'   # change the name 
p.msg()

# Delete Properties
# del p.name
# p.msg()

print(p.species)
print(p.name)

# Modifying Class Properties

Person.species = 'Human Being'
print(p.species)


# Add New Properties

p.age = 23
p.city = 'rmd'

print(p.name)
print(p.age)
print(p.city)



