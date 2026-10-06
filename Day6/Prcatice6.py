class BankAccount:
    def __init__(self,name,account_number):
        self.name= name
        self.account_number= account_number
        self.balance = 5000
    def details(self):
        print("\nAccount Details")
        print("Name: ",self.name)
        print("Account Number: ",self.account_number)
        print("Your Account balance:",self.balance)
    def deposit(self):
        amount = int(input("\nEnter deposit amount: "))
        self.balance= self.balance + amount
        print("Updated Balance: ",self.balance)

name= input("Enter your name:")
account_number= input("Enter account number:")

bankAcc= BankAccount(name, account_number)
bankAcc.details()
bankAcc.deposit()