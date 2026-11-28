def even_odd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
res=even_odd(2)
print(res)

def count_vowels():
    str=input("Enter a string: ")
    count=0
    for i in str:
        if i in 'aeiouAEIOU':
            count+=1
    print(count)
count_vowels()

def greet(name="Guest"):
    print("hello",name)
greet()
# greet("Amar")

def calculate(a, b):
    add=a+b
    pro=a*b
    return add,pro
total,product=calculate(4,2)
print(f"Sum: {total}, Product: {product}")
