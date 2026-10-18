#Write a function that counts how many vowels (a, e, i, o, u) are in a given string.
class Newclass:
    def __init__(self, word):
        self.word = word
    def main(self):
        count = 0
        for i in self.word:
            if i in "aeiouAEIOU":
                count = count + 1
        return count
word = input("Enter your word: ")
obj = Newclass(word)
print("Total vowels:",obj.main())


