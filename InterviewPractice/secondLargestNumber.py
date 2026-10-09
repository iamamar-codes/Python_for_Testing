class SecondLargestNum:
    def __init__(self, my_list):
        self.my_list = my_list

    def secondLargest(self):
        my_max = my_list[0]
        for x in my_list:
            if x > my_max:
                my_max = x
        print(my_max)


my_list = list((input("enter number Element: ").split()))
print(my_list)

SLN1 = SecondLargestNum(my_list)
SLN1.secondLargest()
