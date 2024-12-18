# These are all of the code challenges we've done in ITCS102.

from os import system

def cc1():
    # ESCAPE SEQUENCE
    print("Escape Sequence Diamond Pattern\n")

    print("\n\t\t\t\t\t*\n\n\n\t\t\t\t*\t*\t*\n\n\n\t\t\t*\t*\t*\t*\t*\n\n\n\t\t*\t*\t*\t*\t*\t*\t*\n\n\n\t\t\t*\t*\t*\t*\t*\n\n\n\t\t\t\t*\t*\t*\n\n\n\t\t\t\t\t*")

def cc2():
    # ESCAPE SEQUENCE
    print("Escape Sequence Diamond Pattern With Name Inside\n")

    name = input("What is your name? ")

    print("\n\t\t\t\t\t*\n\n\n\t\t\t\t*\t*\t*\n\n\n\t\t\t*\t*\t*\t*\t*\n\n\n\t\t*\t\t   Hi! " + name + "\t\t\t*\n\n\n\t\t\t*\t*\t*\t*\t*\n\n\n\t\t\t\t*\t*\t*\n\n\n\t\t\t\t\t*")

def cc3():
    # ARITHMETIC OPERATORS
    # Simple Calculator
    print("Simple Calculator\n")

    num1 = input("Enter the first number : ")
    num2 = input("Enter the second number : ")

    if not (num1.isnumeric() and num2.isnumeric()):
        print("\nPlease enter a number.")
    else:
        num1 = eval(num1)
        num2 = eval(num2)

        sum = num1 + num2
        diff = num1 - num2
        prod = num1 * num2
        quot = num1 / num2
        expo = num1 ** num2
        rem = num1 % num2
        floor_div = num1 // num2

        print("\nThe sum of", num1, "and", num2, "is", sum)
        print("The difference of", num1, "and", num2, "is", diff)
        print("The product of", num1, "and", num2, "is", prod)
        print("The quotient of", num1, "and", num2, "is", quot)
        print(num1, "exponent by", num2, "is", num1 ** expo)
        print("The remainder of", num1, "and", num2, "is", rem)
        print("The floor division of", num1, "and", num2, "is", floor_div)

def cc4():
    # ARITHMETIC OPERATORS
    # Philippine Denominations
    print("Philippine Denominations\n")

    name = input("Enter your username : ")
    deposit = input("Enter the amount to deposit : ")

    print("========" * 12)
    print(f"Hello, {name}. The breakdown of your deposit amount in Philippine denomination is as follows :\n")

    if not deposit.isnumeric():
        print("NONE.\nPlease enter a number.")
    else:
        deposit = eval(deposit)

        thou = deposit // 1000
        thou_rem = deposit % 1000

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

        print(thou, "\t-\t| 1000")
        print(fiveh, "\t-\t| 500")
        print(twoh, "\t-\t| 200")
        print(oneh, "\t-\t| 100")
        print(fifty, "\t-\t| 50")
        print(twenty, "\t-\t| 20")
        print(ten, "\t-\t| 10")
        print(five, "\t-\t| 5")
        print(one, "\t-\t| 1")

def cc5():
    # CONDITIONALS
    # Create a program that will accept Prelim, Midterm, Semi-Final, Quiz, and Project Grade.
    # Compute the final grade: FG = (prelim x 15%) + (midterm x 15%) +
    # (semifinal x 15%) + (final x 15%) + (quiz x 25%) + (project x 15%).
    # Display a remark "Congratulations! You passed the course" if final grade is 75 and above;
    # Otherwise display "Sorry, you failed."

    print("Final Grade Calculator\n")

    # Input grades
    prelim = input("Enter Prelim Exam Grade : ")
    midterm = input("Enter Midterm Exam Grade : ")
    semifinal= input("Enter Semi-Final Exam Grade : ")
    final = input("Enter Final Exam Grade : ")
    quiz = input("Enter Quiz Grade : ")
    project = input("Enter Project Grade : ")

    if not (prelim.isnumeric() and midterm.isnumeric() and semifinal.isnumeric()
            and final.isnumeric() and quiz.isnumeric() and project.isnumeric()):
        print("\nPlease enter a number.")
    else:
        # Final grade formula
        FG = (eval(prelim) * .15) + (eval(midterm) * .15) + (eval(semifinal) * .15) + (eval(final) * .15) + (eval(quiz) * .25) + (eval(project) * .15)
        FG = round(FG,2)
        print()

        # Requirement to pass
        if FG >= 75:
            print(f"\nYour Final Grade is {FG}.")
            print("Congratulations! You passed the course.")
        else:
            print(f"\nYour Final Grade is {FG}.")
            print("Sorry, you failed.")

def cc6():
    # LOGICAL OPERATORS
    # Age Categorizer
    # Set the age range for each category: toddler, preteen,
    # early adulthood, middle age, post-adulthood, and senior.
    # The oldest age will be set to 122, which is the age of the
    # oldest person ever recorded.

    print("Welcome to Age Categorizer!\n")

    # Permission from the user to use their info.
    consent = input("Do you want to know your age category? It requires your name and age. (Y/N) : ").lower()

    # If Y(yes), the program will continue; if N(no), or if the input does not
    # match any of the options, the program will exit.
    if consent == "y" :
        print("Alright! Let's categorize your age. ;)\n")

        # Enter info
        name = input("Enter your name : ")
        age = input("Enter your age : ")
        print()

        if not age.isnumeric():
            print("Please enter a number.")
        else:
            age = eval(age)
            # Age range for each category
            if age >= 1 and age <= 8:
                print(f"Hello {name}, you fall within the Toddler category.")
            elif age >= 9 and age <= 14 :
                print(f"Hello {name}, you fall within the Preteen category.")
            elif age >= 15 and age <= 18 :
                print(f"Hello {name}, you fall within the Teenager category.")
            elif age >= 19 and age <= 27 :
                print(f"Hello {name}, you fall within the Early Adulthood category.")
            elif age >= 28 and age <= 44 :
                print(f"Hello {name}, you fall within the Middle Age category.")
            elif age >= 45 and age <= 59 :
                print(f"Hello {name}, you fall within the Post-Adulthood category.")
            elif age >= 60 and age <= 122 :
                print(f"Hello {name}, you fall within the Senior category.")
            else :
                print("Invalid input.")
    elif consent == "n" :
        print("Ok. I guess there's always another time. :'(")
    else :
        print("Invalid input.")

def cc7():
    # CONDITIONALS
    # GROCERY
    # All product prices would be taxed 12.3% added to the product price.
    # If the untaxed price is more than 4000 a discount of 3.8% of the ontaxed product price would be applied.
    # If age is more than 60 and not higher 150 a senior discount would be applied to the taxed price, senior discount is 12.3%.
    # Notify customer of his change.

    print("Grocery Program\n")

    name = input("Enter your name : ")
    did_grocery = input("Did you purchase a grocery today? (Y/N) : ")

    # The program will continue if the user answers Y (yes), otherwise terminate
    if did_grocery.lower() == "y" :
        print(f"\n\tHi {name}, Welcome to GROCERY!")
        print("======" * 8)

        grocery_item = input("Item you purchased : ")
        item_price = input("Enter item price : ")
        age = input("Enter your age : ")
        payment = input("Enter payment amount: ")

        if not (item_price.isnumeric() and age.isnumeric() and payment.isnumeric()):
            print("Please only enter numbers for item price, age and payment.")
        else:
            item_price = eval(item_price)
            age = eval(age)
            payment = eval(payment)

            # FEEDBACK
            # Item and price
            print(f"| Hi {name}, you purchased {grocery_item}.")
            print(f"--> Original item price: {round(item_price,2)} pesos")

            # Item price OVER 4000 will receive a discount of 3.8%
            if item_price > 4000 :
                item_price -= (item_price * .038)
                print(f"| The item price is over 4000 pesos.\n| You're eligible for a discount of 3.8%.")
                print(f"--> Discounted item price: {round(item_price,2)} pesos")
            else :
                print("| The item price is not over 4000 pesos.\n| You're not eligible for a discount.")
            
            # Tax of 12.3% will ALWAYS be added to item price
            taxed_price = item_price + (item_price * .123)
            print(f"| A tax of 12.3% will be added to the item price.")
            print(f"--> Taxed item price: {round(taxed_price,2)} pesos")
        
            # Senior discount of 12.3% will be applied to TAXED item price if user is 60-150 years old
            if age >= 60 and age <= 150 :
                taxed_price -= taxed_price * .123
                print("| You're eligible for a senior discount of 12.3%.")
                print(f"--> Item price after senior discount: {round(taxed_price,2)} pesos\n")
            elif age <= 6 :
                print("| You're not old enough to buy grocery.")
                print("| You're not eligible for a senior discount of 12.3%.\n")
            elif age > 150 :
                print("| How are you still alive?!")
                print("| You're not eligible for a senior discount of 12.3%.\n")
            else :
                print("| You're not eligible for a senior discount of 12.3%.\n")

            # Final item price with tax and with/without discount/s
            print(f"Final item price: {round(taxed_price,2)} pesos")
            
            # User change
            change = payment - taxed_price

            if payment >= taxed_price and payment <= 0:  
                print(f"You paid {payment} pesos and received {round(change,2)} pesos in change.")
            else :
                print(f"You only paid {payment} pesos. You owed {round(change,2) * -1} pesos.")
            print("Thank you for using the program. Have a nice day.")
    else :
        print("Thank you for using the program. Have a nice day.")

def cc8():
    # LOOPS
    # FOR LOOPS
    # Loop for 10 times.
    # Sum of all random inputs by the user.

    print("Sum Of All Inputs, Odd And Even Numbers Calculator\n")
    print("Enter 10 numbers! ^v^\n")

    total = 0
    even = 0
    odd = 0

    for x in range(1,11):
        num = input(f"Input #{x}: ")
        
        if not num.isnumeric():
            print("Please enter a number.")
        else:
            num = eval(num)
            total += num

            # Add all even and odd numbers to themselves.
            if num % 2 == 0:
                even += num
            elif num % 1 == 0:
                odd += num
            else:
                print("The number is not an integer.")

    print(f"\nThe sum of all inputs is {round(total, 2)}.")

    # To determine whether there are no even or odd numbers or both.
    if even != 0:
        if odd != 0:
            print(f"The sum of all EVEN numbers is {even}, \nWhile the sum of all ODD numbers is {odd}.")
        else:
            print(f"The sum of all EVEN numbers is {even}. \nThere are no ODD numbers.")
    else:
        if odd != 0:
            print(f"There are no EVEN numbers. \nThe sum of all ODD numbers is {odd}.")
        else:
            print(f"There are no EVEN or ODD numbers.")

def cc9():
    # LOOPS
    # NESTED FOR LOOPS
    # Inverted Mirrored Right Triangle

    print("Inverted Mirrored Right Triangle\n")

    for x in range(1, 11):
        for a in range(1, x):
            print("  ", end="")
        for b in range(10, x, -1):
            print(" *", end="")
        print()

def cc10():
    # LOOPS
    # NESTED FOR LOOPS
    # Star And Caret Diamond

    print("Star And Caret Diamond\n")

    for a in range(0, 6):
        for b in range(6, a, -1):
            print(" ", end=" ")
        for c in range(0, a):
            print("*", end=" ")
        for d in range(0, a):
            print("^", end=" ")
        print()
    for w in range(1, 6):
        for x in range(0, w+1):
            print(" ", end=" ")
        for y in range(5, w, -1):
            print("^", end=" ")
        for z in range(5, w, -1):
            print("*", end=" ")
        print()

def cc11():
    # LOOPS
    # NESTED FOR LOOPS
    # Diamond with one points

    print("Perfect Diamond\n")

    for a in range(0, 5):
        for b in range(5, a, -1):
            print(" ", end=" ")
        for c in range(0, a):
            print("*", end=" ")
        for d in range(1, a):
            print("*", end=" ")
        print()
    for w in range(0, 4):
        for x in range(0, w + 2):
            print(" ", end=" ")
        for y in range(3, w, -1):
            print("*", end=" ")
        for z in range(2, w, -1):
            print("*", end=" ")
        print()

def cc12():
    # LOOPS
    # NESTED FOR LOOPS
    # Star Arrow

    print("Star Arrow\n")

    for a in range(0, 5):
        for b in range(5, a, -1):
            print(" ", end=" ")
        for c in range(0, a):
            print("*", end=" ")
        for d in range(0, a):
            print("*", end=" ")
        print()
    for w in range(1, 5):
        for x in range(1, 5):
            print(" ", end=" ")
        for y in range(1, 3):
            print("*", end=" ")
        print()
    print()

def cc13():
    # LOOPS
    # WHILE LOOPS
    # Add all inputs until the input is 0.

    print("Looping Adder Program\n")
    print("[Instructions: Give numbers you want to add, then input 0 if you want the sum or to end the program.]\n")

    # Boolean Variable 
    isRepeat = True
    sum = 0

    while isRepeat:
        num = input("Enter a number : ")

        if not num.isnumeric():
            print("Please enter a number.")
        else:
            num = eval(num)
            sum += num

            # If the input is 0, the loop will stop.
            if num == 0 and sum > 0:
                print(f"\nThe sum of all numbers given is {sum}.")
                print("Thank you for using the program!")
                isRepeat = False
                break # To make sure that the loop will stop.
            elif sum == 0:
                print("\nThank you for using the program!")
                isRepeat = False
                break # To make sure that the loop will stop.

def cc14():
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
        nonlocal acc
        acc = name, password

    def create_account():
        account()
        global acc1
        acc1 = acc
        deposit()
        if balance > 0:
            nonlocal has_account
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
            nonlocal balance
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
        else:
            amount = eval(amount)
            print()
            nonlocal balance
            if amount >= balance:
                print("AMOUNT IS MORE THAN TO OR EQUAL TO BALANCE")
                print("OPERATION NOT POSSIBLE")
                resume()
            else:
                balance -= amount
                print("OPERATION SUCCESSFUL\n")
                print(f"WITHDRAWN AMOUNT : {amount}")
                check_balance()

    global is_running
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