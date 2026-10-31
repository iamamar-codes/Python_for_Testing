t= (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
print("Search Element from this Tuple ",t )
x = int(input("Enter number: "))
for i in t:
    if i==x:
        print(x,"Founded")
        break
else:
    print("Not Found")