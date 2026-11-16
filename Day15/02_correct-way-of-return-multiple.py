class calci:
    def operations(self,a,b):
        c1=a+b
        c2=a-b
        c3=c1*c2
        c4=a/b
        return c1,c2,c3,c4

c= calci()
x=5
y=2
r1,r2,r3,r4 = c.operations(x,y)
print(r1,r2,r3,r4)