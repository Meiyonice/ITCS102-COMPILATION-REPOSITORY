# These are some of my personal projects during the first semester of my first year in college.

from time import sleep
from os import system
from random import randint

def topiks():
    # Rock, Paper, Scissors

    print("> TOPIKS")
    print("  (The classic game of Rock, Paper and Scissors but simulated in a text-based program.)\n")

    count = 0
    userWin = 0
    compWin = 0

    while True :
        count += 1
        
        print(f"ROUND {count} | You:{userWin} | Computer:{compWin}")
        print("1 = ROCK\n2 = PAPER\n3 = SCISSORS\n0 = EXIT")

        pik = input("What's your PIK? : ")

        computer = randint(1,3)

        if computer == 1 :
            computer1 = "ROCK"
        elif computer == 2 :
            computer1 = "PAPER"
        else :
            computer1 = "SCISSORS"

        if not pik and pik == "" :
            print("Thank you for using the program.\nHope to see you again!")
            break
        elif pik == "1" or pik == "2" or pik == "3" :
            pik = eval(pik)

            sleep(.7)
            print("BATO!")
            sleep(1)
            print("BATO!")
            sleep(1)
            print("PIK!")
            sleep(.7)
            system("cls")

            if pik == 1 :
                print("You picked ROCK.")
                print(f"The computer picked {computer1}.")

                if pik == computer :
                    print("You tied.\n")
                else :
                    if computer == 2 :
                        print("The computer won.\n")
                        compWin += 1
                    else :
                        print("You won!\n")
                        userWin += 1
            elif pik == 2 :
                print("You picked PAPER.")
                print(f"The computer picked {computer1}.")

                if pik == computer :
                    print("You tied.\n")
                else :
                    if computer == 3 :
                        print("The computer won.\n")
                        compWin += 1
                    else :
                        print("You won!\n")
                        userWin += 1
            else :
                print("You picked SCISSORS.")
                print(f"The computer picked {computer1}.")

                if pik == computer :
                    print("You tied.\n")
                else :
                    if computer == 1 :
                        print("The computer won.\n")
                        compWin += 1
                    else :
                        print("You won!\n")
                        userWin += 1
        elif pik == "0":
            print("\nThank you for using the program!")
            break
        else :
            count -= 1
            system("cls")

def shopping():
    # SHOPPING BY MARLON EJAY RAMIREZ

    print("> Shopping Simulator")
    print("  (A shopping simulation with an established menu.)\n")

    menu = {"ball":200,"car":70,"pencil":10}
    total = 0

    print("Ball-₱200 | Car-₱70 | Pencil-₱10\n")

    while True:
        item = input("What's your order? (press enter to submit your order): ")

        if not item and item == "":
            print(f"\nYour total is {total} pesos! Thank you, please come again.")
            break
        elif item in menu:
            while True:
                quantity = input("How many are you going to buy?: ")

                if not quantity.isnumeric():
                    print("Enter the amount.")
                else:
                    total += (menu[item] * eval(quantity))
                    break
        else:
            print("Please enter a valid item.")

def hollow_triangle():
    # Hollow Right Triangle
    print("> Hollow Right Triangle")
    print("  (A hollow right triangle, for which you can customize the width.)\n")

    num = input("Enter the width of the triangle: ")

    if not num.isnumeric() or int(num) <= 0:
        print("\nPlease enter a valid number.")
    else:
        num = eval(num)
        num -= 2
        print("\n*")
        for x in range(0, num):
            print("* ", end="")
            print("  " * x, end="")
            print("* ", end="")
            print()
        print("* " * (x + 3), "\n")