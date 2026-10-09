class SecondLargestNum:
    def __init__(self, my_list):
        self.my_list = my_list
        self.l= []
    def secondLargest(self):
        for i in range(self.my_list):
            ele = int(input("Enter the eement: "))
            self.l.append(ele)
        print("List: ", self.l)



my_list = int(input("total number of list: "))


SLN1 = SecondLargestNum(my_list)
SLN1.secondLargest()
