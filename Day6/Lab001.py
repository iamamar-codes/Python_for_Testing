#class and object

class Car:
    name = "BUGATI"

    def drive(self):
        print("I am driving")

my_car = Car()
my_car.drive()
print(my_car.name)


class Student:
    name= "Rohan"
    marks= 78

std1 = Student()
print(std1.name)
print(std1.marks)
