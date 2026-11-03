import time
pin = 1234
balance = 10000
print("Welcome to the SBI ATM")
print("Insert Card 1.Yes 2.No")
card = int(input())

if card == 1:
    print("Enter Your Pin")
    user_pin = int(input())

    if user_pin == pin:
        print("Select Language 1. English 2. Hindi")
        lang = int(input())

        if lang == 1:
            print("Select Option")
            print("1. Cash Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            choice = int(input())
            if choice == 1:
                dep_amt = int(input("Enter Deposit Amount: "))
                if dep_amt > 0:
                    balance = balance + dep_amt
                    print("Amount Deposited:", dep_amt)
                    print("Check Balance 1.Yes 2.No")
                    check = int(input())
                    if check == 1:
                        print("Available Balance:", balance)
                    else:
                        print("Thank You, Visit Again")
                else:
                    print("Invalid Deposit Amount")
            elif choice == 2:
                amt = int(input("Enter Withdraw Amount: "))
                if amt <= balance and amt > 0 and amt % 100 == 0:
                    print("Processing..............")
                    time.sleep(3)
                    balance = balance - amt
                    print("Collect your Cash and Card")
                    print("Thank You, Visit Again")
                    print("Want to check your balance? 1.Yes 2.No")
                    check = int(input())
                    if check == 1:
                        print("Current Balance:", balance)
                    else:
                        print("Thank You, Visit Again")
                else:
                    print("Invalid Withdrawal Amount")
            elif choice == 3:
                print("Available Balance:", balance)
            else:
                print("Invalid Input")
        else:
            print("Please select English only for now Because I dont know how to change language")
    else:
        print("Please Enter Correct PIN")
else:
    print("Insert Your Card Properly")



