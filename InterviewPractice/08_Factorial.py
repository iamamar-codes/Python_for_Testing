# Find the factorial of a number using a loop
class Factorial:
    def __init__(self,number):
        self.number = number
    def check_fact(self):
        fact = 1
        for i in range(1, self.number+1):
            fact *= i
        return fact

number = int(input("Enter a number: "))

obj = Factorial(number)
print(f"Factorial of {number} is:",obj.check_fact())
