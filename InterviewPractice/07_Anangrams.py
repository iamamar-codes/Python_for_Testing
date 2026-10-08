#sorted(): letters ko alphabetical order mein arrange karta hai.

my_string1 = input("Enter your String: ")
list(my_string1)

my_string2 = input("Enter your String: ")
list(my_string2)

if sorted(my_string1.lower()) == sorted(my_string2.lower()):
    print(f"'{my_string1}','{my_string2}' -> True")
    print("String is Anangrams")
else:
    print(f"'{my_string1}','{my_string2}' -> False")
    print("String is not Anangrams")


