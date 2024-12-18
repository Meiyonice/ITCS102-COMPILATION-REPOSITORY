# FINALS PROJECT IN ITCS102
# INTERACTIVE MENU PROGRAM
# BY MARLON EJAY R. RAMIREZ
# BSIT-1B

from time import sleep
from os import system
from activities import *
from code_challenges import *
from personal_projects import *

system("cls")

def intro():
    system("cls")
    print(program_title)

def menu():
    print(f"""> {project_types2[choice1]}

        =============================================
                    - {project_types2[choice1]} MENU -\n""")
    order = 1
    for item in project_types1[choice1]:
        print(f"\t\t  {order}. {item}")
        order += 1
    print("""\t\t  0. EXIT
        =============================================\n""")
    global choice2
    choice2 = input("Where would you like to go? ")
    system("cls")

def submenu_top():
    print(f"""
        =============================================
                          - MENU -""")
    
def submenu_bottom():
    print("""\t\t0. EXIT
        =============================================\n""")
    global choice3
    choice3 = input("Where would you like to go? ")
    system("cls")

def progress(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print("\r〘", "☰" * left, " " * right, "〙", f" {percent:.0f}%", sep="", end="", flush=True)

def shutting_down():
    sleep(1)
    system("cls")
    print("\n\tShutting Down Program...\n")

    for i in range(101):
        progress(i)
        sleep(0.1)
    sleep(2)

    print("\n\nDone!")

    sleep(1)
    system("cls")

    print("\nThank you for using the program! Have a nice day. ^^")

def resume():
    input("\npress any button to continue")
    system("cls")

def print_def():
    print("\n> PRINT STATEMENTS")
    print("  (A command that outputs text or data to the screen.)")

def escseq_def():
    print(f"""> ESCAPE SEQUENCES {choice3}
  (Special character combinations in Python that begin with a backslash (\)
  and enable you to include characters in strings that are otherwise difficult
  to type directly or have special meanings.)\n""")
    
def opera_def():
    print("\n> OPERATORS")
    print("  (Operators are used to perform operations on variables and values.)")

def arith_def():
    print("> ARITHMETIC OPERATORS")
    print("  (Arithmetic operators are used with numeric values to perform common mathematical operations.)\n")

def logic_def():
    print("> LOGICAL OPERATORS")
    print("  (Logical operators are used to combine conditional statements.)\n")

def condi_def():
    print("\n> CONDITIONAL STATEMENTS")
    print("  (Statements that execute different actions based on whether a specified condition is true or false.)")

def if_else_def1():
    print("> SIMPLE IF-ELSE STATEMENTS")
    print("  if   (Evaluates the first condition; code runs if it's True.)")
    print("  elif (Evaluates additional conditions if the previous if (or elif) is False.)")
    print("  else (Catches everything that isn't caught by the preceding if or elif statements.)\n")

def if_else_def2():
    print("> NESTED IF-ELSE STATEMENTS")
    print("  (Nested if-else in Python refers to using an if-else structure within another if or else statement.)\n")

def loop_def():
    print("\n> LOOPS")
    print("  (These statements allow you to repeat code blocks.)\n")
    print("TYPES OF LOOPS:")
    print("  For loop   (Use if you have certain or definite amout of times to repeart a code block.")
    print("  While loop (Use if you are uncertain on the amount of times to repeat a code block.\n")

def func_def():
    print("> FUNCTIONS")
    print("  (A block of code commonly used for code reusability, which only runs when it is called.)\n")

program_title = "PYTHON FUNDAMENTALS - INTERACTIVE MENU PROGRAM\n\t  BY MARLON EJAY R. RAMIREZ"

activities = ["PRINT STATEMENTS", "COMMENTS", "OPERATORS", "CONDITIONAL STATEMENTS", 
              "LOOPS", "FUNCTIONS", "DOCSTRINGS", "MODULES", "LISTS"]

code_challenges = ["PRINT STATEMENTS", "OPERATORS", "CONDITIONAL STATEMENTS", 
              "LOOPS", "FUNCTIONS"]

personal_projects = ["SHOPPING SIMULATOR", "HOLLOW RIGHT TRIANGLE", "TOPIKS"]

project_types1 = [activities, code_challenges, personal_projects]

project_types2 = ["ACTIVITIES", "CODE CHALLENGES"]

incomplete_lessons = ["ACTIVITIES", "CODE CHALLENGES"]

loop_menu = True

print("\n\tInitializing Program...\n")

for i in range(101):
    progress(i)
    sleep(0.1)
sleep(2)

print("\n\nDone!")

sleep(1)
system("cls")

for char in program_title:
    print(char, end="", flush=True)
    sleep(0.1)
print("\n")

sleep(1)

name = input("What is your name? ")

print(f"\nHello, {name.title()}!", end=" ")

while loop_menu:
    ask = input("Are you ready to proceed with the program? (y/n): ").lower()

    if ask == "y":
        intro()

        while loop_menu:
            print("""
    ===============================================
                    - MAIN MENU -

            1. ACTIVITIES
            2. CODE CHALLENGES""", end="")

            if not incomplete_lessons:
                print("""
            3. PERSONAL PROJECTS (BONUS)""", end="")
                project_types2.append("PERSONAL PROJECTS")
            else:
                pass
            print("""
            0. EXIT
    ===============================================\n""")

            choice1 = input("Where would you like to go? ").lower()

            system("cls")

            if choice1 == "1":
                choice1 = 0

                if "ACTIVITIES" in incomplete_lessons:
                    incomplete_lessons.remove("ACTIVITIES")
                else:
                    pass
                
                while True:
                    menu()

                    if choice2 == "1":
                        while True:
                            print_def()
                            submenu_top()
                            print("""
                1. SIMPLE PRINTING
                2. STRING CONCATENATION
                3. STRING FORMATTING""")
                            submenu_bottom()

                            if choice3 == "1":
                                print("> SIMPLE PRINTING\n")
                                act1()
                                resume()
                            elif choice3 == "2":
                                print("> STRING CONCATENATION\n")
                                act1V2()
                                resume()
                            elif choice3 == "3":
                                print("> STRING FORMATTING\n")
                                act3()
                                resume()
                            elif choice3 == "0":
                                break
                            else:
                                continue
                    elif choice2 == "2":
                        print("\n> COMMENTS\n")
                        act2()
                        resume()
                    elif choice2 == "3":
                        while True:
                            opera_def()
                            submenu_top()
                            print("""
                1. ARITHMETIC OPERATORS
                2. ASSIGNMENT OPERATORS
                3. RELATIONAL OPERATORS
                4. LOGICAL OPERATORS""")
                            submenu_bottom()

                            if choice3 == "1":
                                arith_def()
                                act4()
                                resume()
                            elif choice3 == "2":
                                print("> ASSIGNMENT OPERATORS")
                                print("  (Assignment operators are used to assign values to variables.)\n")
                                act5()
                                resume()
                            elif choice3 == "3":
                                print("> RELATIONAL OPERATORS")
                                print("  (Comparison or Relational operators are used to compare two values.)\n")
                                act6()
                                resume()
                            elif choice3 == "4":
                                logic_def()
                                act7()
                                resume()
                            elif choice3 == "0":
                                break
                            else:
                                continue
                    elif choice2 == "4":
                        while True:
                            condi_def()
                            submenu_top()
                            print("""
                1. SIMPLE IF-ELSE STATEMENTS
                2. NESTED IF-ELSE STATEMENTS""")
                            submenu_bottom()

                            if choice3 == "1":
                                if_else_def1()
                                act6()
                                resume()
                            elif choice3 == "2":
                                if_else_def2()
                                act7()
                                resume()
                            elif choice3 == "0":
                                break
                            else:
                                continue
                    elif choice2 == "5":
                        while True:
                            loop_def()
                            submenu_top()
                            print("""
                1. SIMPLE FOR LOOP 1
                2. SIMPLE FOR LOOP 2
                3. NESTED FOR LOOP TEST 1
                4. NESTED FOR LOOP TEST 2
                5. NESTED FOR LOOP PATTERN
                6. USEFUL NESTED FOR LOOP 
                7. FUN NESTED FOR LOOP
                8. SIMPLE WHILE LOOP
                9. HYBRID LOOP""")
                            submenu_bottom()

                            if choice3 == "1":
                                print("> SIMPLE FOR LOOP 1\n")
                                act8()
                                resume()
                            elif choice3 == "2":
                                print("> SIMPLE FOR LOOP 2\n")
                                act9()
                                resume()
                            elif choice3 == "3":
                                print("> NESTED FOR LOOP TEST 1\n")
                                act10()
                                resume()
                            elif choice3 == "4":
                                print("> NESTED FOR LOOP TEST 2\n")
                                act11()
                                resume()
                            elif choice3 == "5":
                                print("> NESTED FOR LOOP PATTERN\n")
                                act12()
                                resume()
                            elif choice3 == "6":
                                print("> USEFUL NESTED FOR LOOP\n")
                                act13()
                                resume()
                            elif choice3 == "7":
                                print("> FUN NESTED FOR LOOP\n")
                                act14()
                                resume()
                            elif choice3 == "8":
                                print("> SIMPLE WHILE LOOP\n")
                                act16()
                                resume()
                            elif choice3 == "9":
                                print("> HYBRID LOOP\n")
                                print("  (Combination of for loop and while loop.)")
                                act15()
                                resume()
                            elif choice3 == "0":
                                break
                            else:
                                continue
                    elif choice2 == "6":
                        func_def()
                        act17()
                        resume()
                    elif choice2 == "7":
                        print("> DOCSTRINGS")
                        print("  (Docstrings or Documentation strings are a special type of comment used in programming")
                        print("  to describe what a function, method, class, or module does.)\n")
                        act18()
                        resume()
                    elif choice2 == "8":
                        print("> MODULES")
                        print("  (A file that contains Python code, which can include functions, classes, and variables.)\n")
                        act19()
                        resume()
                    elif choice2 == "9":
                        print("> LISTS")
                        print("  (Lists are ordered, changeable, and allow duplicate values.)\n")
                        act20()
                        resume()
                    elif choice2 == "0":
                        intro()
                        break
                    else:
                        continue
            elif choice1 == "2":
                choice1 = 1

                if "CODE CHALLENGES" in incomplete_lessons:
                    incomplete_lessons.remove("CODE CHALLENGES")
                else:
                    pass
                
                while True:
                    menu()

                    if choice2 == "1":
                        while True:
                            print_def()
                            submenu_top()
                            print("""
                1. ESCAPE SEQUENCES 1
                2. ESCAPE SEQUENCES 2""")
                            submenu_bottom()

                            if choice3 == "1":
                                escseq_def()
                                cc1()
                                resume()
                            elif choice3 == "2":
                                escseq_def()
                                cc2()
                                resume()
                            elif choice3 == "0":
                                break
                            else:
                                continue
                    elif choice2 == "2":
                        while True:
                            opera_def()
                            submenu_top()
                            print("""
                1. ARITHMETIC OPERATORS 1
                2. ARITHMETIC OPERATORS 2
                3. LOGICAL OPERATORS""")
                            submenu_bottom()

                            if choice3 == "1":
                                arith_def()
                                cc3()
                                resume()
                            elif choice3 == "2":
                                arith_def()
                                cc4()
                                resume()
                            elif choice3 == "3":
                                logic_def()
                                cc6()
                                resume()
                            elif choice3 == "0":
                                break
                            else:
                                continue
                    elif choice2 == "3":
                        while True:
                            condi_def()
                            submenu_top()
                            print("""
                1. SIMPLE IF-ELSE STATEMENTS
                2. NESTED IF-ELSE STATEMENTS""")
                            submenu_bottom()

                            if choice3 == "1":
                                if_else_def1()
                                cc5()
                                resume()
                            elif choice3 == "2":
                                if_else_def2()
                                cc7()
                                resume()
                            elif choice3 == "0":
                                break
                            else:
                                continue
                    elif choice2 == "4":
                        while True:
                            loop_def()
                            submenu_top()
                            print("""
                1. SIMPLE FOR LOOP
                2. FOR LOOP PATTERN 1
                3. FOR LOOP PATTERN 2
                4. FOR LOOP PATTERN 3
                5. FOR LOOP PATTERN 4
                6. SIMPLE WHILE LOOP""")
                            submenu_bottom()

                            if choice3 == "1":
                                print("> SIMPLE FOR LOOP\n")
                                cc8()
                                resume()
                            elif choice3 == "2":
                                print("> FOR LOOP PATTERN 1\n")
                                cc9()
                                resume()
                            elif choice3 == "3":
                                print("> FOR LOOP PATTERN 2\n")
                                cc10()
                                resume()
                            elif choice3 == "4":
                                print("> FOR LOOP PATTERN 3\n")
                                cc11()
                                resume()
                            elif choice3 == "5":
                                print("> FOR LOOP PATTERN 4\n")
                                cc12()
                                resume()
                            elif choice3 == "6":
                                print("> SIMPLE WHILE LOOP\n")
                                cc13()
                                resume()
                            elif choice3 == "0":
                                break
                            else:
                                continue
                    elif choice2 == "5":
                        func_def()
                        cc14()
                        resume()
                    elif choice2 == "0":
                        intro()
                        break
                    else:
                        continue
            elif choice1 == "3":
                choice1 = 2

                if "PERSONAL PROJECTS" in project_types2:
                    while True:
                        menu()
                        
                        if choice2 == "1":
                            shopping()
                            resume()
                        elif choice2 == "2":
                            hollow_triangle()
                            resume()
                        elif choice2 == "3":
                            topiks()
                            resume()
                        elif choice2 == "0":
                            intro()
                            break
                        else:
                            continue
                else:
                    intro()
                    continue
            elif choice1 == "0":
                while loop_menu:
                    print("\n   > EXIT\n")

                    ask = input("\tAre you sure you want to exit? (Type X to confirm): ").lower()

                    if ask == "x":
                        shutting_down()
                        loop_menu = False
                    else:
                        intro()
                        break
            else:
                intro()
                continue
    elif ask == "n":
        shutting_down()
        break
        loop_menu = False
    else:
        continue