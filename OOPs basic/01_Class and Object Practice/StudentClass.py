class Student:

    def __init__(self, name , age):

        self.name = name
        self.age = age

    def display(self):
        print(f"{self.name} and age {self.age}")
    
 
student1 = Student("raja", 22)
student2 = Student("rani", 22)

student1.display()
student2.display()


# similar but diffrent not using any methods and not calling
class Student1:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

student = Student1("Raja", 85)
print(student.name)           # ✅ Works
print(student.__marks)        # ❌ Fails
print(student._Student1__marks)  # 😬 Works (but avoid)


        
