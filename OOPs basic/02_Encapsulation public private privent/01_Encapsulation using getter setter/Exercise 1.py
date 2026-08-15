class Student:
    def __init__(self,marks):
        self.__marks = marks


    # getter
    @property

    def marks(self):
        return self.__marks
    
    # setter
    @marks.setter

    def marks(self,new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks

        else:
            print("❌ Invalid marks!")

    def grade(self):
        if self.__marks >= 80:
            return "A"
        
        if self.__marks >= 60:
            return "B"
        
        if self.__marks >= 40:
            return "C"
        
        else:
            return "F"

s1 = Student(85)
print(s1.marks)     # 85
print(s1.grade())   # A

s1.marks = 70
print(s1.marks)     # 70
print(s1.grade())   # B

s1.marks = 120      # ❌ Invalid marks!
print(s1.marks)     # 70 (unchanged)

    