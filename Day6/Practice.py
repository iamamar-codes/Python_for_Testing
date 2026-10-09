class Mobile:
    def __init__(self):
        self.name= "Nokia"
        self.color= "Blue"
        self.cost= 1200
    def call(self):
        print("Mobile is ringing")
m1 = Mobile()
print(m1.name)
print(m1.color)
print(m1.cost)

m1.call()