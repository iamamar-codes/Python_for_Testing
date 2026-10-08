# Find the factorial of a number using a loop
class Factorial:
    def __init__(self, number):
        self.number = number

    def my_fact(self):
        fact = 1
        for i in range(1, number + 1):
            fact = fact * i
        return fact

number = int(input("Ente a number: "))

h1 = Factorial(number)
print(h1.my_fact())
