class Student:
    count=0
    def __init__(self,name):
        self.sname=name
        Student.count +=1
    def show_total(self):
        print("Total Students",Student.count)

s1= Student("A")
print(Student.count)

s2= Student("B")
print(Student.count)

s3= Student("C")
print(Student.count)

print(Student.count)
print(s1.count) #here we can also use class name
print(s2.sname)

s1.show_total()
s3.show_total()