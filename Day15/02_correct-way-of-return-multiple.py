class calci:
    def operations(self,a,b):
        c1=a+b
        c2=a-b
        c3=a*b
        c4=a/b
        return c1,c2,c3,c4

c=calci()
r1,r2,r3,r4=c.operations(7,2)
print(r1,r2,r3,r4)