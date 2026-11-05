class A:
    x = 10
a1 = A()
a2 = A()
a1.x = 20
print(A.x, a1.x, a2.x)