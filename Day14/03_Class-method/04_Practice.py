class Phone:
    PhoneName= "IPHONE"
    def __init__(self,model,price):
        self.model=model
        self.price=price
    @classmethod
    def detail(cls):
        print(cls.PhoneName)

p1=Phone("11Pro", 59999)
Phone.detail()
print(p1.model)
print(p1.price)
print("------------------------------------")
Phone.detail()
p2=Phone("16 Pro Max", 76000)
print(p2.model)
print(p2.price)

