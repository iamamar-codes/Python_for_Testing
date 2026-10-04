# Write a function square(num) that returns the square of a number (instead of printing it), then print the result separately when calling it.
def square(num):
    return num ** 2


result = square(6)
print("Square of entered number is:", result)


# Write a function is_even(num) that returns True or False depending on whether the number is even or odd.
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(5))


#Write a function calculate_total(price, tax) that returns the total price after adding tax, then use that returned value in another calculation (like adding a discount)
def calculate_total(price, tax):
     total = price + tax
     return total
total_amount = calculate_total(1000, 50)
print("Total before discount:", total_amount)

discount = 100
final_amount = total_amount - discount
print("Final amount after discount:", final_amount)