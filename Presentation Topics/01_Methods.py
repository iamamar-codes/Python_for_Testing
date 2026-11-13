class Student:
    school = "XYZ SCHOOL"   #Static Variables

    def __init__(self,name):
        self.name = name     #Instance Variable
    def show_name(self):   #Instance Method
        print("Name:",self.name)
    @classmethod    #class Method
    def show_school(cls):
        print(cls.school)
    @staticmethod   #Static Method
    def say_hello():
        print("Hello")

s1=Student("Amar")
s1.show_name()

Student.show_school()
Student.say_hello()
s1.say_hello()
