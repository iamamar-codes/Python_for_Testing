#Arguments: Function can accept information through arguments.

def greet(name): #single Argument
    print(f"Hello {name} How are you?")
greet("Amar")
greet("Python")

def greet_full_name(firstname, lastname):
    print(f"This is your full name: {firstname} {lastname}")
greet_full_name("Amar", "Kushwaha")


#Arbitrary Arguments, *args
def car_collection(*cars):
    print("My first car ", cars[0])
    print("My Second car ", cars[1])
    print("My Third car ", cars[2])
    print("My Fourth car ", cars[3])
car_collection("BMW", "BUGATI", "PAGANI", "FERRARI")
