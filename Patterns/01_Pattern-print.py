n= int(input("Enter a number for row:"))
for i in range(n): #row
    for j in range(n): #Column
        print("#",end="")
    print()
print("------------------")
for i in range(n):
    for j in range(i):
        print("#", end="")
    print()