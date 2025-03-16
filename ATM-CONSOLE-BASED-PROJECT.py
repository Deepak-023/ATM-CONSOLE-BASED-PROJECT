print("**********************")
print("Welcome to ATM")
print("**********************")
print()

accounts = {
    1001: ["Deepak", "02-05-2004", 10000, 2304],
    1002: ["Aasrith", "03-01-2004", 20000, 2323],
    1003: ["Hassain", "15-09-2002", 15000, 1521],
    1004: ["Yasin", "30-09-2003", 22000, 3009],
    1005: ["Aravind", "06-02-2003", 31000, 6203],
    1006: ["Ahmed", "04-12-2002", 4000, 4122],
    1007: ["Mahesh", "12-04-2003", 50000, 1204]
}

dobm = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

def display_details(accno):
    print(f"Name: {accounts[accno][0]}")
    print(f"Account Number: {accno}")
    dob = accounts[accno][1].split("-")
    print(f"Date of Birth: {dob[0]}-{dobm[int(dob[1])]}-{dob[2]}")
    print(f"Account Balance: {accounts[accno][2]}")

while True:
    print("\nChoose Your Option")
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. PIN Generation")
    print("4. Mini Statement")
    print("5. Check Balance")
    print("6. Fund Transfer")
    print("7. Change PIN")
    print("8. Exit")
    
    option = int(input("Enter Your Option: "))
    print()
    
    if option == 1:
        accno = int(input("Enter Account Number: "))
        if accno in accounts:
            pin = int(input("Enter PIN: "))
            if accounts[accno][3] == pin:
                amt = int(input("Enter Amount to Withdraw: "))
                if amt > accounts[accno][2]:
                    print("Insufficient Funds")
                else:
                    accounts[accno][2] -= amt
                    print("Withdrawal Successful!")
                    display_details(accno)
            else:
                print("Invalid PIN")
        else:
            print("Account Does Not Exist!")
    
    elif option == 2:
        accno = int(input("Enter Account Number: "))
        if accno in accounts:
            amt = int(input("Enter Amount to Deposit: "))
            accounts[accno][2] += amt
            print("Deposit Successful!")
            display_details(accno)
        else:
            print("Account Does Not Exist!")
    
    elif option == 3:
        accno = int(input("Enter Account Number: "))
        if accno in accounts:
            pin = int(input("Set New PIN: "))
            accounts[accno][3] = pin
            print("PIN Set Successfully!")
            display_details(accno)
        else:
            print("Account Does Not Exist!")
    
    elif option == 4:
        accno = int(input("Enter Account Number: "))
        if accno in accounts:
            pin = int(input("Enter PIN: "))
            if accounts[accno][3] == pin:
                display_details(accno)
            else:
                print("Invalid PIN")
        else:
            print("Account Does Not Exist!")
    
    elif option == 5:
        accno = int(input("Enter Account Number: "))
        if accno in accounts:
            pin = int(input("Enter PIN: "))
            if accounts[accno][3] == pin:
                print(f"Your Current Balance: {accounts[accno][2]}")
            else:
                print("Invalid PIN")
        else:
            print("Account Does Not Exist!")
    
    elif option == 6:
        accno = int(input("Enter Your Account Number: "))
        if accno in accounts:
            pin = int(input("Enter PIN: "))
            if accounts[accno][3] == pin:
                to_acc = int(input("Enter Recipient Account Number: "))
                if to_acc in accounts and to_acc != accno:
                    amt = int(input("Enter Amount to Transfer: "))
                    if amt <= accounts[accno][2]:
                        accounts[accno][2] -= amt
                        accounts[to_acc][2] += amt
                        print("Fund Transfer Successful!")
                        display_details(accno)
                    else:
                        print("Insufficient Balance")
                else:
                    print("Invalid Recipient Account")
            else:
                print("Invalid PIN")
        else:
            print("Account Does Not Exist!")
    
    elif option == 7:
        accno = int(input("Enter Account Number: "))
        if accno in accounts:
            old_pin = int(input("Enter Old PIN: "))
            if accounts[accno][3] == old_pin:
                new_pin = int(input("Enter New PIN: "))
                accounts[accno][3] = new_pin
                print("PIN Updated Successfully!")
                display_details(accno)
            else:
                print("Incorrect Old PIN")
        else:
            print("Account Does Not Exist!")
    
    elif option == 8:
        confirm = input("Are you sure you want to exit? (yes/no): ").lower()
        if confirm == 'yes':
            print("Thank you for using the ATM!")
            break
    
    else:
        print("Invalid Option! Please Try Again.")
