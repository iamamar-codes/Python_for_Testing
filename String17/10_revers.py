# single String
# str =input("Enter your String: ")
# rev = ""
# for i in str:
#     rev = i + rev
# print(rev)


#String Paragraph
s = input("Enter your String: ")
words = s.split()
result = ""
for i in words:
    result = i + " " + result
print(result)

s1 = "Hello python developers"
s2=s1.split('e')
print(s2)
