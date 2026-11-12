class Student:
    count=0
    def __init__(self,name):
        self.sname=name
        Student.count += 1
    @staticmethod
    def show_total():
     return Student.count

s1 = Student("Amar")
print(Student.count,s1.sname)

s2 = Student("Samar")
print(Student.count,s2.sname)

s3 = Student("Akash")
print(Student.count, s3.sname)

s4 = Student("Piyush")
print(Student.count, s4.sname)

s4 = Student("Ayush")
print(Student.count, s4.sname)

print("Total students:",Student.show_total())
