str = "Welcome"
print("First character",str[0])
print("Last character",str[-1])

print(str[len(str)//2])

name= input("Enter your name: ")
print(name.title().replace(" ",""))

str1=  input("Enter a string: ")
# rev = str1[::-1]
str2= input("Enter another string: ")
if str1.upper()==str2.upper(): #rev
    print("Palindrome")
else:
    print("Not Palindrome")
