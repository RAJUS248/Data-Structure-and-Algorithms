class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks  # ✅ Fixed here

    def set_marks(self, m):
        if 0 <= m <= 100:
            self.__marks = m
        else:
            print("Invalid marks!")

    def display(self):
        print(f"Name: {self.name}, Marks: {self.__marks}")


# Create object
student1 = Student("raja", 100)

# Get current marks
print("Initial Marks:", student1.get_marks())  # ✅ Will now show value

# Update marks
student1.set_marks(95)

# Display updated info
student1.display()
