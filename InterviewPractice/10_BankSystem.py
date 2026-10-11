class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self,Damount):
        self.balance =  self.balance+ Damount

    def withdraw(self, Wamount):
        if Wamount > self.balance:
            print("not Efficiant amount")
        else:
            self.balance -= Wamount
    def check_balance(self):
        print("Current balance: ", self.balance)

balance = int(input("balance: "))
obj = BankAccount(balance)
print("Current balance: ", balance)

Damount = int(input("Deposit: "))
obj.deposit(Damount)
print("Deposi amount: ", Damount)

obj.check_balance()

Wamount = int(input("withdraw : "))
print("Withdraw amount: ", Wamount)
obj.withdraw(Wamount)

obj.check_balance()