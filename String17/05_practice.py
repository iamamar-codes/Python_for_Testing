#Palindrome
str = input("Enter a String: ")
rev = str[::-1]

if rev.upper() == str.upper():
    print("Plindrome")
else:
    print(" not Plindrome")


#Anangrams
wrd1 = input("Enter a Word1: ")
wrd2 = input("Enter a Word2: ")

if sorted(wrd1.upper()) == sorted(wrd2.upper()):
    print("Ananagrams")
else:
    print("no Palindrome")