#Constructor
class Laptop:

    def __init__(self, name, OS): #create a Constructor
        self.name = name
        self.OS = OS

lap1 = Laptop("HP", "Windows")
print(lap1.name, lap1.OS)

lap2 = Laptop("Mac", "MacOS")
print(lap2.name, lap2.OS)



