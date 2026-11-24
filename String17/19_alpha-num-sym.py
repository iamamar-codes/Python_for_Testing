str=input("Enter a String: ")
print(str)
if str.isalpha():
    print("Alphabet")
elif str.isdigit():
    print("Numbers")
elif str.isalnum():
    print("both")
else:
    print("other char")
