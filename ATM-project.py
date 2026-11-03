import time
pin= 1234
Balnace = 10000
print("Welcome to the SBI ATM")
print("Insert Card 1.Yes 2.No")
card = int(input())
if card == 1:
    print("Enter Your Pin")
    user_pin= int(input())
    if user_pin == pin:
        print("Select Language 1. English 2. Hindi")
        lang = int(input())
        if lang == 1:
            print("Select Option 1.Check balance 2.Withdraw")
            choise = int(input())
            if choise == 1:
                print("Available Balance is", Balnace)
            elif choise == 2:
                print("Enter Withdraw Amount")
                amt = int(input())
                if amt<=Balnace and amt>0 and amt%100==0:
                    print("Proccessing..............")
                    time.sleep(5)
                    print("Collect your Cash and Card")
                    time.sleep(3)
                    print("Thank You, Visit again")
                    print("Want to check your balance? 1.Yes 2.No")
                    check = int(input())
                    if check == 1:
                        print("Current Balance is", Balnace-amt)
                    else:
                        print("Thank You, Visit again")
                else:
                    print("Invalid Input")
            else:
                print("Invalid Input")

        else:
            print("please select English only for now because I dont know how to change language")
    else:
        print("Please Enter correct pin")
else:
    print("Insert your card properly")


