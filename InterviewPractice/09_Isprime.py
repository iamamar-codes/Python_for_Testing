class Newclass:
    def __init__(self,num):
        self.num = num
    def main(self):
        for i in range(2, self.num):
            if self.num % i == 0:
                print("Number is not prime")
                break
        else:
            print("Number is prime")
num = int(input("Enter a number"))

obj = Newclass(num)
obj.main()
