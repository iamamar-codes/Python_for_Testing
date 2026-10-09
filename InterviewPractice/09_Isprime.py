class NumberisPrime:
    def __init__(self, number):
        self.number = number

    def isprime(self):
        for i in range(2, number):
            if self.number % i == 0:
                print("Number is not a prime")
                break
        else:
         print("Number is a prime")


number = int(input("Enter a number: "))

obj1 = NumberisPrime(number)
obj1.isprime()
