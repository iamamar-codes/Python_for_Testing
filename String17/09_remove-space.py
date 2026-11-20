str= " Boy Is Walking "
print(str)

# Removing Space from left side
str1=str.lstrip()
print(str1)

# Removing Space from Right side
str2=str.rstrip()
print(str2)

# Removing Space from left and Right side
str3=str.strip()
print(str3)

#1. WAY
str4= " I AM THE BEST "
str5= str4.replace(" ","")
print(str5)

#2. Way
s=input("Enter your String: ")
s1=""
for i in s:
    if i !=" ":
        s1=s1+i
print(s1)

#3. Way
s2=input("Enter your String: ")
s3=""
for i in s:
    if i ==" ":
        pass
    else:
        s3=s3+i
print(s1)
