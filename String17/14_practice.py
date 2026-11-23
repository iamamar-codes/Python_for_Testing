s=input("Enter a string: ")
substr=input("Enter a substring: ")
pos = s.find(substr)
if pos == -1:
    print("Not Found")
else:
    print("Found")


# Print how many times a substring appears in a string.
# Input: banana, an → Output: 2

s1=input("Enter a string: ")
s2=input("Enter Substring: ")
print(s1.count(s2))
