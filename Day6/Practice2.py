class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def details(self):
        print("Brand:",self.brand)
        print("Model:", self.model)
        print("Price:", self.price)

    def call(self):
        print("Calling from Samsung Galaxy S24")

mob = Mobile("Samsung","S24", "₹1,20,000")
mob.details()
mob.call()