class BankAccount:
    def __init__(self):
        self.balance = 500

    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            print("Not Enough Amount ")
        else:
            self.balance -= withdraw_amount
            print("Withdraw amount: ",withdraw_amount)

    def check_balance(self):
        print("Current Balance: ", self.balance)

deposit_amount = int(input("Enter deposit amount: "))


b1 = BankAccount()

b1.deposit(deposit_amount)
b1.check_balance()

withdraw_amount = int(input("Enter withdraw amount: "))
b1.withdraw(withdraw_amount)

b1.check_balance()

