#sorted(): letters ko alphabetical order mein arrange karta hai.
class Anagrams:
    def __init__(self, str1, str2):
        self.str1= str1
        self.str2= str2
    def check_ana(self):
        if sorted(str1.upper()) == sorted(str2.upper()):
            print(f"'{str1}','{str2}' -> True")
            print("String is Anagrams")
        else:
            print(f"'{self.str1}','{self.str2}' -> False")
            print("String is not Anagrams")

str1 = input("Enter your first String: ")
str2 = input("Enter your second String: ")

obj = Anagrams(str1, str2)
obj.check_ana()