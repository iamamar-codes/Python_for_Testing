class Car:
    def __init__(self, brand, color):
        self.Cbrand= brand
        self.Ccolor= color
    def show(self):
        print("Car Brand is:",self.Cbrand)
        print("Car color is:",self.Ccolor)

c1 = Car("BMW", "Black")
c2 = Car("Audi", "Q3")
c1.show()
c2.show()
