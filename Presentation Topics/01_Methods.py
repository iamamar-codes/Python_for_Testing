class Car:
    def __init__(self):
        self.brand="BMW"
    def start(self): #static method
        print("Car is Starting")

    @staticmethod
    def move():
        print("Car is Moving")
    @classmethod
    def stop(cls):
        print("Car is Stopped")

c1=Car()
print(c1.brand)

c1.start()
c1.move()
c1.stop()

Car.move()
Car.stop()

Car.Start() #Error





