# Print numbers from 1 to 10 using a for loop with range().
for i in range(1, 11):
    print(i)

# Create a list of 5 fruits. Use a for loop to print each fruit on a separate line.
my_list = ["Apple", "Mango", "Graps", "Dragonfruit"]
for items in my_list:
    print(items)

# Use a for loop to find the sum of all numbers in a list [10, 20, 30, 40, 50].
num = [10, 20, 30, 40, 50]
result = 0
for numbers in num:
    result += numbers
print(result)

#Use a for loop to find the largest number in a list [4, 9, 2, 17, 8] (without using max()).
num1 = [4, 9, 2, 17, 8]
# my_max = max(num1)
# print(my_max)
largest = num1[0]
for numbers in num1:
    if numbers > largest:
        largest = numbers
print(largest)