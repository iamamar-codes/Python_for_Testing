class Heroin:
    def __init__(self):
        self.name= "Kajol"
        self.age = 50
    def dance(self):
        print("Kajol is dancing")

h1 = Heroin()
print(h1.name)
print(h1.age)
h1.dance()

h1.Movie = "Dheera"   #Adding
print(h1.Movie)

h1.age = 55    #Modifing
print(h1.age)

del h1.age     #Delete
print(h1.age)
h1.dance()