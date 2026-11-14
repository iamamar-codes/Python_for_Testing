class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=Circle.pi*self.radius**2
        print(area)
    @classmethod
    def show_pi(cls):
        print(Circle.pi)
    @staticmethod
    def is_positive(n):
        if n>0:
            print("Number is greater than 0")
        else:
            print("Number is less than 0")

c1=Circle(5)
c1.area()
Circle.show_pi()
Circle.is_positive(-1)