# Find the factorial of a number using a loop
class Newclass:
    def __init__(self, number):
        self.number = number
    def main(self):
        fact = 1
        for i in range(1, self.number+1):
            fact *= i
        return fact

number = int(input("Enter a number: "))

obj = Newclass(number)
print(obj.main())