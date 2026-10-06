class Student:
    def __init__(self):
        self.name = "Amar"
        self.age= 24
        self.usn= 608
        self.gender= "Male"
    def study(self):
        print("Amar is not study")

std = Student()
print(std.name)
print(std.age)
print(std.usn)
print(std.gender)
std.study()