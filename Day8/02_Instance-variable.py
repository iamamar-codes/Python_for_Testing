class laptop:
    def __init__(self):
        self.brand = "HP"
        self.color = "Black"
    def display(self):
        # Instance variable
        self.type = "OLED"
# Local varibale type = "LED"

l1= laptop()
print(l1.brand)
print(l1.color)
l1.display()
print(l1.type)