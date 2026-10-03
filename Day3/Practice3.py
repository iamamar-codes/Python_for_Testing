#Take a word as input and print it in uppercase and lowercase.
my_str1 = input("Enter a string ")
print(my_str1.upper())
print(my_str1.lower())

#Take a sentence as input and print its length (number of characters).
my_str2 = input("Enter a string ")
print(len(my_str2))

#Take a string as input and check if a particular letter (e.g., 'a') is present in it or not (hint: use the in keyword).
my_str3 = input("Enter a string ")
if 'a' in my_str3:
    print("Letter 'a' is present")
else:
    print("Letter 'a' is not present")

#Take your full name as input and print only the first 3 letters.
my_str4 = input("Enter your full name ")
print(my_str4[0:3])