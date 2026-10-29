a= int(input("Enter a number1: "))
b= int(input("Enter a number2: "))
c= int(input("Enter a number3: "))

if a>b and a>c:
    print("A is greater than B and C")
elif b>a and b>c:
    print("B is greater than A and C")
elif c>a and c>b:
    print("C is greater than A and B")
else:
    print("All Three are Equal")