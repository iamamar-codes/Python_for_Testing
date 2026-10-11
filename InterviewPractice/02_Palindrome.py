# Write a function that takes a string and returns True if it reads the same forwards and backwards, False otherwise.
class Palindrome:
    def __init__(self, my_string):
        self.my_string = my_string
    def check_pali(self):
        str= self.my_string.upper()
        reverse = self.my_string[::-1].upper()
        if str == reverse:
            print("String is palindrome")
        else:
            print("String is not palindrome")

my_string= input("Enter your String: ")
obj = Palindrome(my_string)
obj.check_pali()

