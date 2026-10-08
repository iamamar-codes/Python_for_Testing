# Find the factorial of a number using a loop
class Factorial:
    def __init__(self, number):
        self.number = number

    def find_fact(self):
        fact = 1
        for i in range(1, number + 1):
            fact = fact * i
        return fact


number = int(input("Enter a number: "))

obj1 = Factorial(number)
print(obj1.find_fact())
