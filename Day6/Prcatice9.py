# class Student_info:
#     def __init__(self):
#         self.name= "Amar Kushwaha"
#         self.course= "Software Test With Python"
#         self.insitute= "Pentagone Space"
#         self.fee= 28000
#
#     def information(self):
#         print("\nStudent details----------------------------")
#         print("Student name is: ", self.name)
#         print("Course:", self.course)
#         print("insitute name:", self.insitute)
#         print("Course fee is: ", self.fee)
#
#     def attendence(self):
#         print("\n")
#         print("Every Student need at least 75% attendance")
#
#
# s1 = Student_info()
# print(s1.name)
# print(s1.course)
# print(s1.insitute)
# print(s1.fee)
#
# s1.information()
# s1.attendence()

class Student_info:
    def __init__(self,name,course, insitute, fee):
        self.name= name
        self.course= course
        self.insitute= insitute
        self.fee= fee

    def information(self):
        print("\nStudent details----------------------------")
        print("Student:", self.name)
        print("Course:", self.course)
        print("insitute name:", self.insitute)
        print("Course fee is: ", self.fee)

    def attendence(self):
        print("\n")
        print("Every Student need at least 75% attendance")

name =input("Student name is: ")
course =input("Student course: ")
insitute= input("Insitute name: ")
fee = input("fee is: ")



s1 = Student_info(name, course, insitute, fee)

s1.information()
s1.attendence()