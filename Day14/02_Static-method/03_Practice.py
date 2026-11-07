from Day5.Prcatice2 import calculate_total


class Calculator:

    @staticmethod
    def multiply(a,b):
        return a*b
    @staticmethod
    def dividd(a,b):
        if b == 0:
            return "Invalid"
        return a/b

print(Calculator.multiply(10,5))
print(Calculator.dividd(10,2))
print(Calculator.dividd(10,0))