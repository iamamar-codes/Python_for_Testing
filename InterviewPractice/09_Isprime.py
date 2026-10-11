class PrimeNumber:
    def __init__(self,num):
        self.num = num
    def isPrime(self):
        for i in range(2, num):
            if self.num % i == 0:
                print("Number is not prime")
                break
        else:
            print("Number is prime")

num = int(input("Enter a Number: "))

obj = PrimeNumber(num)
obj.isPrime()