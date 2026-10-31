cost_price = int(input("Enter the Cost Price: "))
sell_price = int(input("Enter the Sell Price: "))

if cost_price>sell_price:
    print("Loss")
elif cost_price<sell_price:
    print("Profit")
else:
    print("neither Profit nor Loss")
