#Create a variable num = "25" (a string). Convert it to an integer and add 5 to it. Print the result
num  = "25"
result = int(num)+5
print(result)

#Create a float variable price = 99.99. Convert it to an integer and print it. What happens to the decimal part?
price = 99.99
converted = int(price) #o/p - 99
rounded = round(price) #o/p - 100
print(converted)
print(rounded)

#Take two numbers as input (they will be strings by default). Convert both to float, multiply them, and print the result.
first_number = float(input("Enter First number "))
second_number = float(input("Enter Second number "))

print(first_number*second_number)

