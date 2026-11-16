class Calsi:
    def __init__(self):
        self.brand="Calsi"
        self.cost=2000
    def add(self,a,b):
        c=a+b
        return c
    def sub(self,a,b):
        c=a-b
        return c
    def mult(self,a,b):
        c=a*b
        return c
    def div(self,a,b):
        c=a/b
        return c
c1=Calsi()
print(c1.brand)
print(c1.cost)

Add=c1.add(10,20)
print(Add)

Sub=c1.sub(20,10)
print(Sub)

Mult=c1.mult(10,20)
print(Mult)

Div=c1.div(20,10)
print(Div)