# Normal Method

class Student:
    def greet(self):
        print("Hello")

s1 = Student()
s1.greet()


#Parameterized Method

class Student:
    def __init__(self,name):
        self.name = name
    def show(self):
        print("Name:", self.name)

s2 = Student("Amar")
s2.show()
