#Write a function that counts how many vowels (a, e, i, o, u) are in a given string.
class FindVowels:
    def __init__(self,word):
        self.word = word
    def count(self):
        count = 0
        for c in self.word:
            if c in "aeiouAEIOU":
                count +=1
        return count
word= input("Enter your word here: ")

obj1= FindVowels(word)
print(obj1.count())

