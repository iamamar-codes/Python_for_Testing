#1st way: using only default constructor
class Student:
    def __init__(self):
        self.name = "Rahul"
        self.age = 20
        self.marks = 85
std1 = Student()
print(std1.name)
print(std1.age)
print(std1.marks)


#2nd way: using Parameterised Constructor and method for printing variables
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)

std2 = Student("Rahul",20,85)
std2.display()
