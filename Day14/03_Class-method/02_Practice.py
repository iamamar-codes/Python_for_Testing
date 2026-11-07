class Student:
    School= "XYZ SCHOOL"

    @classmethod
    def change_school(cls, name):
        cls.School=name

print(Student.School)
Student.change_school("ABC SCHOOL")
print(Student.School)