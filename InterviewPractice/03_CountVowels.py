#Write a function that counts how many vowels (a, e, i, o, u) are in a given string.
class CountVowels:
    def __init__(self,word):
        self.word = word
    def check_vow(self):
        count = 0
        for c in self.word:
            if c in "aeiouAEIOU":
                count +=1
        return count

word = input("Enter your Word: ")
obj = CountVowels(word)
print("Total Vowels:",obj.check_vow())

