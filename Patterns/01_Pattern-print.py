n=int(input("Enter a number:"))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
print("------------------")
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
