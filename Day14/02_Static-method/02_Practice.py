class Calculator:
    def __init__(self):
        self.addition="Addition"
        self.subtraction="Subtraction"
    @staticmethod
    def add(a, b):
        return a+b
    @staticmethod
    def sub(a, b):
        return a-b

cal1 = Calculator()
print(cal1.addition)
print(Calculator.add(10,20))
print(cal1.subtraction)
print(Calculator.sub(20,10))

