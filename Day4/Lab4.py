#Factorial
number = int(input("Enter a number: "))
fact = 1
if number == 0:
    print("invalid")
elif number < 0:
    print("invalid")
else:
    for i in range(1, number+1):
        fact = fact * i

print(f"Factorial of {number} is: {fact}")