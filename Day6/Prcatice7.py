class Hero:
    def __init__(self):
        self.name = "SRK"
        self.age= 60
        self.numOfMovie= 75
    def act(self):
        print("SRK is good actor")

h1 = Hero()
print(h1.name)
print(h1.age)
print(h1.numOfMovie)

h1.act()