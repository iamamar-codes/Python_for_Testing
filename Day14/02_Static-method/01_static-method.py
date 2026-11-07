class Student:
    school="XYZ SCHOOL"
    def __init__(self,name,marks):
        self.sname= name
        self.smarks= marks
    @staticmethod
    def get_info():
        return print("Students information")

s1 = Student("Amar", 81)
s2= Student("Sameer", 80)
s1.get_info()
print(Student.school)
print(s1.sname, s1.smarks)
print(s2.sname, s2.smarks)

