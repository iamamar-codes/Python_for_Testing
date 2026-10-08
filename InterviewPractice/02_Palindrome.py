# Write a function that takes a string and returns True if it reads the same forwards and backwards, False otherwise.
class Function:
    def __init__(self, string):
        self.string = string

    def display(self):
        my_string = self.string.upper()   #casefold() used for convert first character upper to lower ex. Amar --> amar
        reverse = self.string[::-1].upper()
        if my_string == reverse:
            print("String is Palindrome")
        else:
            print("String is not palindrome")

string = input("Enter your String: ")

obj = Function(string)
obj.display()
