# Write a function that takes a string and returns True if it reads the same forwards and backwards, False otherwise.
class Newclass:
    def __init__(self, str):
        self.str = str.upper()
    def main(self):
        reverse = self.str[::-1].upper()
        if self.str == reverse:
            print("String is Palondrome")
        else:
            print("String is not Palidrome")

str = input("Enter a String: ")
obj = Newclass(str)
obj.main()