s=input("Enter a string: ")
substr=input("Enter a substring: ")
pos = s.find(substr)
if pos == -1:
    print("Not Found")
else:
    print("Found")