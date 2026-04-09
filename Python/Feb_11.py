# Working of ATM
'''
withdrawl, deposit, balance enquiry, mini statement, pin change using dictionary for representing data related to bank account
'''
accounts = {
    "667755441" : {"Name" : "Alex","Balance" : 3000, "Pin" : 1234},
    "667755442" : {"Name" : "Bob","Balance" : 10000, "Pin" : 4321},
    "667755443" : {"Name" : "Charles","Balance" : 30000, "Pin" : 1212},
    "667755444" : {"Name" : "David","Balance" : 5000, "Pin" : 1313},
    }

print("-" * 40)
print("                 WELCOME          ")
print("-" * 40)

user_acc = input("Please Enter Your Account Number ")

if user_acc in accounts:
    correct_pin = accounts[user_acc]["Pin"]
    c = 1
    authorised = True
    
    while c <= 3:
        user_pin = int(input("Please Enter 4 Digit Pin "))
        if user_pin != correct_pin:
            remaining_attempts = 3 - c
            if remaining_attempts == 0:
                authorised = False
                print("Account Locked. Visit Again")
            else:
                print(f"You have {remaining_attempts} Attempts Left")
        else:
            print("Entered Pin is Valid, Please Proceed")
            break
        c += 1
    transactions = []

    while authorised:
        print("Available Options")
        print("1. Withdrawl\n2. Deposit\n3. Balance Enquiry\n4. Mini Statement\n5. Pin Change\n6. Exit")

        choice = int(input("Enter your option(1-6): "))

        if choice == 1:
            amount = int(input("Please Enter the Amount for Withdrawl: "))
            if amount <= accounts[user_acc]["Balance"]:
                accounts[user_acc]["Balance"] -= amount
                print(f"\u20B9{amount} Withdrawn successfully")
                transactions.append(f"\u20B9{amount} Withdrawn | Balance: \u20B9{accounts[user_acc]['Balance']}")
                print(f"Current Balnce: \u20B9{accounts[user_acc]['Balance']}")
            else:
                print("Insufficient Balance")
                
        elif choice == 2:
            amount = int(input("Please Enter the Amount for Deposit: "))
            accounts[user_acc]["Balance"] += amount
            print(f"\u20B9{amount} Successfully Deposited")
            transactions.append(f"\u20B9{amount} Deposited | Balance: \u20B9{accounts[user_acc]['Balance']}")
            print(f"Current Balnce: \u20B9{accounts[user_acc]['Balance']}")
            
        elif choice == 3:
            print(f"Current Balance: \u20B9{accounts[user_acc]['Balance']}")
            
        elif choice == 4:
            print("Mini Statement (Last 5 Transactions):")
            if len(transactions) == 0:
                print("No transactions yet.")
            else:
                for t in transactions[-5:]:
                    print(t)
            
        elif choice == 5:
            old_pin = int(input("Enter your current PIN: "))
            
            if old_pin == accounts[user_acc]["Pin"]:
                new_pin = input("Enter your new 4 digit PIN: ")

                if len(new_pin) == 4 and new_pin.isdigit():
                    
                    if int(new_pin) != accounts[user_acc]["Pin"]:
                        confirm_pin = input("Confirm your new PIN: ")
                        
                        if new_pin == confirm_pin:
                            accounts[user_acc]["Pin"] = int(new_pin)
                            print("PIN changed successfully")
                        else:
                            print("Confirmation PIN does not match")
                            
                    else:
                        print("New PIN cannot be same as old PIN")
                        
                else:
                    print("PIN must be exactly 4 digits")
    
            else:
                print("Incorrect Current PIN Entered")
                
        elif choice == 6:
            print("Thank you.")
            break
        else:
            print("Invalid Choice")
else:
    print("Invalid User")
