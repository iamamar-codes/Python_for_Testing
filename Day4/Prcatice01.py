# Print numbers from 1 to 10 using a while loop.
i = 1
while i <= 10:
    print(i)
    i += 1

# Print all even numbers between 1 and 20 using a while loop.
i = 2
while i <= 20:
    print(i)
    i += 2

# Take a number as input and print its multiplication table (1 to 10) using while.
num = int(input("Enter any number "))
i = 1
while i <= 10:
    print(i * num)
    i += 1

# Print the element of the following list using a loop
my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(my_list):
    print(my_list[idx])
    idx += 1

# Search for a number x in this tuple loop:
tpl = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter the searching number "))
i = 0
while i < len(tpl):
    if tpl[i] == x:
        print("FOUND")
        break
    i += 1
