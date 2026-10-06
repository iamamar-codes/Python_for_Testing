class Car:
    def __init__(self):
        self.name= "BMW"
        self.model= "M4"
        self.color= "Red"
    def Speed(self):
        print("Top Speed is 380 kmp")
    def Drive(self0):
        print("Drive carefully")
c1=Car()
print(c1.name)
print(c1.model)
print(c1.color)

c1.Speed()
c1.Drive()