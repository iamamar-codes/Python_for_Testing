class BankAccount:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 5000

    def details(self):
        print("\nYour Account details")
        print("Enter your name:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

    def deposit(self):
        amount = int(input("\nEnter deposit amount: "))
        self.balance= self.balance + amount
        print("Amount deposited:", amount)
        print("Updated Balance:",self.balance)

name = input("Enter your name: ")
account_number = int(input("Enter your Account Number: "))

bankAcc = BankAccount(name, account_number)
bankAcc.details()
bankAcc.deposit()

