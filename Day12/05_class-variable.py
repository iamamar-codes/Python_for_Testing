class Student:
    School = "ABC"
    def __init__(self,name,age):
        self.sname = name
        self.sage= age

s1= Student("Amar", 24)
s2= Student("Kushwaha", 20)
print(Student.School)
print(s1.School)
print(s2.School)
print(s1.sname)
print(s2.sage)
