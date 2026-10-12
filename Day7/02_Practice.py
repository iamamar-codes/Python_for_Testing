class Student:
    def __init__(self):
        self.name = "Amar"
        self.age = 24

std = Student()
print("Name:",std.name)
print("Age:",std.age)

std.age = 21
print("Update: ",std.age)

