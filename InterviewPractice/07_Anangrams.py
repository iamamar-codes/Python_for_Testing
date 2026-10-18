#sorted(): letters ko alphabetical order mein arrange karta hai.

class Newclass:
    def __init__(self, wrd1, wrd2):
        self.wrd1 = wrd1
        self.wrd2= wrd2
    def main(self):
        if sorted(self.wrd1.upper()) == sorted(self.wrd2.upper()):
            print("Words are Anangrams")
        else:
            print("Words are not Anangrams ")
wrd1 = input("Enter word 1: ")
wrd2 = input("Enter word 2: ")

obj = Newclass(wrd1,wrd2)
obj.main()
