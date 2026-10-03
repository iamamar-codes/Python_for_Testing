# # find the area of circle
# radius = int(input("Enter the Radius of circle "))
# area = (3.14 * radius ** 2)
# print(f"Area of circle is {area}")
#
# # takes two numbers as input and print whether the first number is greater than , less than or equal to the second number
# num1 = int(input("Enter first number "))
# num2 = int(input("Enter second number "))
# if num1 > num2:
#     print("Num1 is greater then num2")
# elif num1 < num2:
#     print("Num2 is greater then num1")
# else:
#     print("num1 is Equal to the second Number ")
#
# #use ternary operator to find the maximum of three numbers entered by the user.
# a = int(input("Enter first number "))
# b = int(input("Enter second number "))
# c = int(input("Enter third number "))
#
# if a >= b and  a >= c:
#     print("First number is maximum")
# elif b >= a and b >= c:
#     print("Second number is maximum")
# else:
#     print("Third number is maximum")
#
# #Develop a Python script that calculates the square of a given number.
# square_number = int(input("Enter a Number "))
# result = square_number ** 2
# print(f"{result} is the Square value of {square_number}")
#
# #Take a number as input and check whether it is positive, negative, or zero.
# my_num = int(input("enter a number "))
# if my_num >0:
#     print("positive")
# elif my_num <0:
#     print("negative")
# else:
#     print("zero")

#Take marks as input (out of 100) and print the grade:
std_marks = int(input("Enter your marks "))
if std_marks >= 90:
    print("A")
elif std_marks >= 75 and std_marks <=89:
    print("B")

elif std_marks >=50 and std_marks <= 74:
    print("c")
else:
    print("Fail")

