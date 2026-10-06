class Student:
    def __init__(self):
        self.name = "Amar"
        self.age= 24
        self.usn= 608
        self.gender= "Male"
    def study(self):
        print("Amar is not studyingn")

s1 = Student()
print(s1.name)
print(s1.age)
print(s1.usn)
print(s1.gender)
s1.study()