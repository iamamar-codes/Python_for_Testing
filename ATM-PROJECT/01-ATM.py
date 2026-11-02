pin = 1234
balance = 5000

print("Welcome to Pentagone ATM")

card = input("Insert your Card Propely(press 1): ")

if card == "1":
    print("Card inserted")

    user_pin = int(input("Enter your PIN: "))

    if user_pin == pin:
        print("PIN is correct")

        print("1. Balance Enquiry")
        print("2. Withdraw")
        print("3. Check Balance")

        option = input("Enter your option: ")

        if option == "1":
            print("Your balance is", balance)

        elif option == "2":
            amount = int(input("Enter amount to withdraw: "))
            if amount %100 == 0:
                if amount <= balance:
                    balance = balance - amount
                    print("Please collect your cash")
                    print("Remaining balance is", balance)
                else:
                    print("Insufficient balance")
                    print("Your balance is", balance)
            else:
                print("Enter the amount in as multiple of 100 (100,500,1000 etc)")


        elif option == "3":
            print("Your balance is", balance)

        else:
            print("Invalid option")

    else:
        print("Wrong PIN")

else:
    print("Please insert your card")

print("Thank you")