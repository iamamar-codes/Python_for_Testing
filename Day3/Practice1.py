# find the area of circle
radius = int(input("Enter the Radius of circle "))
area = (3.14 * radius ** 2)
print(f"Area of circle is {area}")

# takes two numbers as input and print whether the first number is greater than , less than or equal to the second number
num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))
if num1 > num2:
    print("Num1 is greater then num2")
elif num1 < num2:
    print("Num2 is greater then num1")
else:
    print("num1 is Equal to the second Number ")

#use ternary operator to find the maximum of three numbers entered by the user.
a = int(input("Enter first number "))
b = int(input("Enter second number "))
c = int(input("Enter third number "))

if a >= b and  a >= c:
    print("First number is maximum")
elif b >= a and b >= c:
    print("Second number is maximum")
else:
    print("Third number is maximum")

#Develop a Python script that calculates the square of a given number.
square_number = int(input("Enter a Number "))
result = square_number ** 2
print(f"{result} is the Square value of {square_number}")




