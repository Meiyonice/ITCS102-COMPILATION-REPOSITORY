# FUNCTIONS
# Bank Simulation Program
# - Create account
# - Deposit
# - Withdraw
# - Check balance

# REQUIREMENTS:
# Ask the user to create an account.
# After that, he/she will need to make an intial deposit.
# Before depositing, display the filipino denominations of the amount.
# After displaying the denominations, proceed to deposit said amount.
# If user wants to withdraw, ask for the amount to withdraw.
# Withdrawal amount should not be less than the current balance.
# After withdrawal, show the current balance.
# Current balance option would only display current balance.
# Everything should be repeated until user opts out.

from os import system

# MY FUNCTIONS
def intro():
    print("=============================")
    print("|    WELCOME TO MERBANK®    |")
    print("=============================")
    print("CHOOSE AN OPERATION BELOW :")

def resume():
    input()
    system("cls")

def section():
    system("cls")
    print(f"> {choice}\n")

def exit():
    global is_running
    while is_running:
        exit_confirm = input("ARE YOU SURE YOU WANT TO EXIT? (y/n) : ").lower()
        system("cls")

        if exit_confirm == "y":
            print("THANK YOU FOR USING MERBANK®")
            print("PLEASE COME AGAIN")
            is_running = False
            break
        elif exit_confirm == "n":
            break
        else:
            print("INVALID INPUT\n")
            continue    

def account():
    name = input("NAME : ")
    password = input("PASSWORD : ")
    global acc
    acc = name, password

def create_account():
    account()
    global acc1
    acc1 = acc
    deposit()
    if balance > 0:
        global has_account
        has_account = True
        system("cls")
        print("ACCOUNT CREATED")
        resume()
    else:
        resume()

def denomination(amount):
    print()
    # Philippine Denominations
    thou = amount // 1000
    thou_rem = amount % 1000
    fiveh = thou_rem // 500
    fiveh_rem = thou_rem % 500
    twoh = fiveh_rem // 200
    twoh_rem = fiveh_rem % 200
    oneh = twoh_rem // 100
    oneh_rem = twoh_rem % 100
    fifty = oneh_rem // 50
    fifty_rem = oneh_rem % 50
    twenty = fifty_rem // 20
    twenty_rem = fifty_rem % 20
    ten = twenty_rem // 10
    ten_rem = twenty_rem % 10
    five = ten_rem // 5
    five_rem = ten_rem % 5
    one = five_rem // 1

    if balance == 0 and amount <= 0:
        print("INITIAL DEPOSIT IS REQUIRED")
        resume()
    else:
        print(f"{thou}\t-\t| 1000")
        print(f"{fiveh}\t-\t| 500")
        print(f"{twoh}\t-\t| 200")
        print(f"{oneh}\t-\t| 100")
        print(f"{fifty}\t-\t| 50")
        print(f"{twenty}\t-\t| 20")
        print(f"{ten}\t-\t| 10")
        print(f"{five}\t-\t| 5")
        print(f"{one}\t-\t| 1\n")

def check_balance():
    print(f"CURRENT BALANCE : {balance}")
    resume()

def deposit():
    amount = input("ENTER AMOUNT TO DEPOSIT : ")

    if not amount.isnumeric():
        print("PLEASE ENTER A NUMBER")
    else:
        amount = eval(amount)
        denomination(amount)
        global balance
        # To confirm deposit
        while True:
            ask = input(f"ARE YOU SURE YOU WANT TO DEPOSIT {amount} PESOS? (y/n) : ").lower()

            if ask == "y":
                if amount <= 0:
                    print("\nINSUFFICIENT AMOUNT\n")
                    resume()
                    continue
                else:
                    balance += amount
                    print(f"\nDEPOSITED AMOUNT : {amount}")
                    check_balance()
                    break
            elif ask == "n":
                system("cls")
                print("\nDEPOSIT SESSION EXPIRED\n")
                resume()

                if balance == 0:
                    print("ACCOUNT CAN'T BE CREATED WITHOUT INITIAL DEPOSIT\n")
                    continue
            else:
                system("cls")
                continue

def withdraw():
    amount = input("ENTER WITHDRAWAL AMOUNT : ")

    if not amount.isnumeric():
        print("PLEASE ENTER A NUMBER")
        resume()
    else:
        amount = eval(amount)
        print()
        global balance
        if amount >= balance:
            print("AMOUNT IS MORE THAN TO OR EQUAL TO BALANCE")
            print("OPERATION NOT POSSIBLE")
            resume()
        else:
            balance -= amount
            print("OPERATION SUCCESSFUL\n")
            print(f"WITHDRAWN AMOUNT : {amount}")
            check_balance()

is_running = True # To make sure that the loop will stop
has_account = False
acc = 0
balance = 0

while is_running:
    intro()
    print("1. CREATE ACCOUNT")
    print("2. LOGIN")
    print("0. EXIT\n")

    choice = input("WHAT WOULD YOU LIKE TO DO? (1, 2 or 0) : ").lower()

    if choice == "1":
        section()
        create_account()
        continue
    elif choice == "2":
        section()

        if has_account == False:
            system("cls")
            print("YOU DON'T HAVE AN ACCOUNT YET")
            print("PLEASE CREATE AN ACCOUNT\n")
            create_account()
            continue
        else:
            print("LOGIN\n")
            account()
            system("cls")
            
            if acc1 == acc:
                print("LOGIN SUCCESSFUL")
                resume()

                while is_running:
                    intro()
                    print("1. CHECK BALANCE")
                    print("2. DEPOSIT")
                    print("3. WITHDRAW")
                    print("4. DELETE ACCOUNT")
                    print("0. EXIT\n")

                    choice = input("WHAT WOULD YOU LIKE TO DO? (1, 2, 3, 4 or 0) : ").lower()

                    if choice == "1":
                        section()
                        check_balance()
                        continue
                    elif choice == "2":
                        section()  
                        deposit()
                        continue
                    elif choice == "3":
                        section()
                        withdraw()
                        continue
                    elif choice == "4":
                        system("cls")
                        balance = 0
                        has_account = False
                        break
                    elif choice == "0":
                        section()
                        exit()
                    else:
                        system("cls")
                        continue
            else:
                print("ACCOUNT DOES NOT EXIST")
                resume()
                continue

    elif choice == "0":
        section()
        exit()
    else:
        system("cls")
        continue