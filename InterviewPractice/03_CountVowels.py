#Write a function that counts how many vowels (a, e, i, o, u) are in a given string.
class CountVowels:
    def __init__(self, value):
        self.value = value

    def count_vowels(self):
        count = 0
        for c in self.value.lower():
            if c in "aeiou":
                count +=1
        return count

value = input("Enter your string: ")
obj = CountVowels(value)
print("Number of vowels:",obj.count_vowels())
