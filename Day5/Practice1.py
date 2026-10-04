#Write a function add_numbers(a, b) that takes two numbers and prints their sum.
def add_numbers():
    a=  int(input("Enter a number: "))
    b=  int(input("Enter another number: "))
    return a + b
result = add_numbers()
print("Result is:",result)

#Write a function greet(name, city) that prints "Hello [name], welcome from [city]".
def greet(name, city):
    print(f"Hello {name}, welcome from {city}.")
greet("Sumit", "Jaipur")