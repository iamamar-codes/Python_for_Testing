# Loop
for i in range(1, 10):  # print 1-9
    print(i)

for x in range(1, 10, 2):  # print 1,3,5,7,9
    print(x)  # range(Start, Stop, Step)

for counter in range(0, 100):
    print(counter)
    if counter == 20:
        break
print("Counter end here")

for i in range(1, 10):
    if i == 5:
        pass
    else:
        print(i)
