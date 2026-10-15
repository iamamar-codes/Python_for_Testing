class Mystring:
    def __init__(self, text):
        self.text = text
    def reverse(self):
        rvs = ""
        for i in range(len(text)-1, -1, -1):
            rvs += text[i]
        return rvs

text = input("Enter your string: ")

s = Mystring(text)
print(s.reverse())
