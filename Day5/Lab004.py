#Default Parameter Value

def my_city(city = "Delhi"):
    print(f"My city is {city}")
my_city("Indore")
my_city("Bangalore")
my_city()   #Delhi
my_city()   #Delhi

#Retun function
def addition(a, b):
    return a + b
result = addition(5, 7)
print(result)