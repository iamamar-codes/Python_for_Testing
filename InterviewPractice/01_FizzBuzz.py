#Write a program that prints numbers from 1 to 20. But for multiples of 3, print "Fizz" instead of the number, for multiples of 5 print "Buzz", and for multiples of both 3 and 5, print "FizzBuzz".
class Newclass:
    def __init__(self, number):
        self.number = number

    def main(self):
        for i in range(1, self.number+1):
            if i%3 == 0 and i%5 == 0:
                print("Fizz Buzz")
            elif i%3 == 0:
                print("Fizz")
            elif i%5 == 0:
                print("Buzz")
            else:
                print(i)

number = int(input("Enter last number: "))

obj = Newclass(number)
obj.main()

