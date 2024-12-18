# These are all of the activities we've done in ITCS102.

from os import system

def act1():
    # PRINT STATEMENTS
    print("Printing Test Program\n")
    print("""INPUT:
print("Hello, World!")\n
OUTPUT:
Hello, World!""")

def act1V2():
    # STRING CONCATENATION
    print("Information Collector\n")

    name = input("What is your name? ")
    age = input("How old are you? ")
    email = input("Please enter your e-mail address: ")

    if not age.isnumeric():
        print("\nPlease enter a number for age.")
    else:
        print("\nINPUT:\nprint(\"Hi, \" + name + \", \" + age + \" years old. E-mail: \"  + email)\n")
        print("OUPUT:\nHi, " + name + ", " + age + " years old. E-mail: "  + email)

    # len() function
    print("\nBONUS: len(name) - Length Function\nYour name has ", len(name), " characters.")

    input("\npress any button to continue")
    system("cls")

    print("Simple Adder Program\n")

    num1 = input("Please enter a number: ")
    num2 = input("Please enter another number: ")

    if not (num1.isnumeric and num2.isnumeric()):
        print("\nPlease enter a number.")
    else:
        num1 = eval(num1)
        num2 = eval(num2)
        print("\nINPUT:\nprint(num1, \"+\", num2, \"=\", num1 + num2)\n\nOUTPUT:")
        print(num1, "+", num2, "=", num1 + num2)

def act2():
    print("Comments Test Program\n")
    print("""INPUT:
# Comments are used to convey information about your code.
# Comments are ignored by the compiler, which is python.
# Nevertheless, still an important part of the program.
# Comments doesn't affect the function of the program.

print("Hello, World!!!")
          
OUTPUT:
Hello, World!!!""")

def act3():
    # STRING FORMATTING
    # Bio-Data Program
    # Goal: Concatenate the 3 inputs to form a singular output/print.

    print("Bio-Data Program\n")

    name = input("Pleas enter your name: ")
    add = input("Please enter your address: ")
    age = input("Please enter your age: ")

    if not age.isnumeric():
        print("\nPlease enter a number for age.")
    else:
        print("\nINPUT:\nprint(f\"Hi { name }, from { address } age of { age }.\")\n")
        print(f"OUTPUT:\nHi {name}, from {add} age of {age}.")

def act4():
    # ARITHMETIC OPERATORS
    # Fahrenheit To Celcius Converter

    print("Fahrenheit To Celcius Converter\n")

    fah = input("Enter temperature in FAHRENHEIT: ")

    if not fah.isnumeric():
        print("\nPlease enter a number.")
    else:
        fah = eval(fah)
        c = (fah - 32) * 5 / 9
        print("\nINPUT:\ncelcius = (fahrenheit - 32) * 5 / 9\n")
        print(f"OUTPUT:\n{fah} degrees Fahrenheit converted to Celcius is {round(c,2)} degrees.")

def act5():
    # ASSIGNMENT OPERATORS
    # | = | += | -= | *= | /= | %= | //= | **= |
    # Create a program that will assign 10 to the value of x.

    print("Incrementer Test Program\n")
    print("""INPUT:
x = 10
print(x)\n
# Add an additional 10 to the current of x.
# (+= ) - Incrementer
x += 10
print(x)\n
# Add an additional 20 to the current of x.
x += 20
print(x)\n
# Lastly, multiply the current of x to 2.
x *= 2
print(x)\n
OUTPUT:\n10\n20\n40\n80""")

def act6():
    # INTRODUCTION TO DECISION STRUCTURES
    # In some programming language or tutorials, it's reffered to as:
    # CONDITIONAL STATEMENTS OR SELECTION STATEMENTS

    print("Password Program\n")
    print("""INPUT:
password = "secret"
my_password = input("Enter your password: ").lower()
          
if my_password == password:
    print("Access Granted.")
    print("Enjoy!")
elif my_password == "awts":
    print("Access Granted.")
    print("Enjoy, Sadboi!")
else:
    print("Access Denied.")
    print("Please Try Again.")\n\nOUTPUT:""")

    password = "secret"
    my_password = input("Enter your password: ").lower()

    # RELATIONAL OPERATORS
    # == / Is equal to / It's asking a question.

    if my_password == password:
        print("Access Granted.")
        print("Enjoy!")
    elif my_password == "awts":
        print("Access Granted.")
        print("Enjoy, Sadboi!")
    else:
        print("Access Denied.")
        print("Please Try Again.")

def act7():
    # LOGICAL OPERATORS
    # Logical operators are used to combine and check more than one conditions.
    # (and) operator - The result would be True only if both conditions are True.
    # (or) operator - The result would be True if either conditions are True.
    # (not) operator - It would reverse any result of the condition.
    # Scholar Grant Application Program

    print("Scholar Grant Application Program\n")
          
    name = input("What is your name? ")
    isEnrolled = input("Are you currently enrolled in DLL? (y/n) ").lower()

    if isEnrolled == "y":
        print(f"Hi, {name}. Welcome to the DLL Scholarship Grant System!")

        # Is student's age 18 to 35?
        age = input("How old are you right now? ")

        if not age.isnumeric():
            print("\nPlease enter a number for age.")
        else:
            age = eval(age)
            if age >= 18 and age <= 35:
                print("Your passed the age requirement.")

                # Is student's grades 86 to 100?
                grades = input("What was your last GWA? ")

                if not grades.isnumeric():
                    print("\nPlease enter a number for grades.")
                else:
                    grades = eval(grades)
                    if grades >= 86 and grades <= 100:
                        print("Your grades complied with the requirements.")

                        # Is student a member of 4Ps?
                        is4Ps = input("Is your family currently enrolled/subscribed to the 4Ps Program? (y/n) ").lower()

                        if is4Ps == "y":
                            print(f"Congratulations, {name}! You are now granted a scholarship.")
                        elif is4Ps == "n":
                            print("Sorry, but it's only for 4Ps members.")
                        else:
                            print("Invalid Input.")
                    else:
                        print("Sorry, your grades didn't complied with the requirement.\nPlease try again next time.")
            else:
                print("Sorry, you didn't passed the age requirement.")
    elif isEnrolled == "n":
        print("Understandable. Thank you for using the program.")
    else:
        print("Invalid Input.")

def act8():
    # LOOPING STATEMENTS
    # These statements allow you to repeat code blocks.
    # TYPES OF LOOP:
    # FOR LOOP - Use if you have certain or definite amout of times to repeart a code block.
    # WHILE LOOP - Use if you are uncertain on the amount of times to repeat a code block.
    # Goal: Loop for 10 times and add all random number inputs.

    print("Sum Of All Inputs, Odd And Even Numbers Calculator\n")
    print("Input 10 numbers and the program will calculate their total sum,")
    print("the sum of odd numbers, and the sum of even numbers.\n")

    result = 0
    even = 0
    odd = 0

    for loop in range(1, 11):
        num = input(f"Input #{loop}: ")
        
        if not num.isnumeric():
            print("Please enter a number.")
        else:
            num = eval(num)
            result += num

            # Add all even and odd numbers to themselves.
            if num % 2 == 0:
                even += num
            elif num % 1 == 0:
                odd += num
            else:
                print("The number is not an integer.")

    print(f"\nThe sum of all inputs is {result}.")
    print(f"The sum of all EVEN numbers is {even}.")
    print(f"The sum of all ODD numbers is {odd}.")

def act9():
    # LOOPING STATEMENTS
    # FOR LOOP
    # Factorial

    print("Factorial Program\n")

    num = input("Enter a number: ")
    fact = 1

    if not num.isnumeric():
        print("\nPlease enter a number.")
    else:
        num = eval(num)
        for x in range(num, 0, -1):
            fact *= x
    print(f"\nThe factorial of {num} is {fact}.")

def act10():
    # LOOPING STATEMENTS
    # NESTED FOR LOOP
    # Sample 1

    print("Simple Nested For Loop Test Program\n")

    for x in range(1, 11):
        print(x, end="")
        for a in range(1, 11):
            print("*", end="")
        print()

def act11():
    # LOOPING STATEMENTS
    # NESTED FOR LOOP
    # Sample 2

    print("Simple Nested For Loop Test Program 2\n")

    for x in range(1, 11):
        print(x, end="")
        for a in range(1, x+1):
            print("*", end="")
        print(x)

def act12():
    # LOOPING STATEMENTS
    # NESTED FOR LOOP
    # Upside-Down Mirrored Right Triangle

    print("Upside-Down Mirrored Right Triangle\n")

    for w in range(1, 6):
        for x in range(1, w+1):
            print(" ", end=" ")
        for y in range(6, w, -1):
            print("*", end=" ")
        for z in range(6, w, -1):
            print("^", end=" ")
        print()

def act13():
    # LOOPING STATEMENTS
    # NESTED FOR LOOP
    # Multiplication Table

    print("Multiplication Table\n")

    col = input("Enter the number of columns: ")

    if not col.isnumeric():
        print("Please enter a number.")
    else:
        col = eval(col)
        for x in range(1, 11):
            for y in range(1, col+1):
                print(f"{x} x {y} = {x * y}", end="\t")
            print()

def act14():
    # LOOPING STATEMENTS
    # NESTED FOR LOOPS
    # Repeating Horizontal Right Triangles

    print("Repeating Horizontal Right Triangles\n")

    num = input("Enter the amount of triangles: ")

    if not num.isnumeric():
        print("Please enter a number.")
    else:
        num = eval(num)
        for w in range(1, 6):
            for x in range(num):
                for y in range(w):
                    print("^", end=" ")
                for z in range(6, w, -1):
                    print(" ", end=" ")
                print(end="")
            print()

def act15():
    # HYBRID LOOP
    # Combination of for loop and while loop
    # Goal: Ask the user if he/she wants to print more triangle, user can type yes or no.
    # If the user selects yes, program will print another triangle.
    # If no, program will terminate.

    print("Triangle Generator\n")

    loop = True # Boolean variable
    nt = 0 # Number of triangles

    while loop == True:
        ask = input("Do you wish to add a triangle? (yes/no) : ")

        # If user typed no, the loop will terminate.
        if ask.lower() == "no":
            print("LOOP HAS ENDED")
            print("THANK YOU FOR USING THE PROGRAM! <3")
            break
            loop = False
        
        # If user typed yes, a triangle will be added.
        elif ask.lower() == "yes":
            system("cls")
            nt += 1
            for w in range(1, 6):
                for x in range(1, nt + 1):
                    for y in range(1, w + 1):
                        print("*", end=" ")
                    for z in range(6, w, -1):
                        print(" ", end=" ")
                    print(end="")
                print()
            continue

        # For everything else that is not "yes" or "no."
        else:
            print("INVALID INPUT")
            print("PLEASE TYPE \"yes\" OR \"no.\"")
            continue

def act16():
    # LOOPING STATEMENTS
    # WHILE LOOP 

    print("Looping Adder Program\n")
    print("[Instructions: Give numbers you want to add, then input 0 if you want the sum or to end the program.]\n")

    # Boolean variable / trigger 
    resume = True 

    # While resume is set to true, the loop will continue. 
    # Continue to ask for a number.
    # Once user types the number ZERO (0), terminate the loop
    # And get the summation of all the number(s) given.
    sum = 0
    while resume:
        num = input("Enter any number: ")

        if not num.isnumeric():
            print("Please enter a number.")
        else:
            num = eval(num)
            if num == 0:
                print("LOOP STOPPED")
                print(f"The sum of all the numbers given is {sum}.")
                break
                resume = False # To make sure that the loop will stop.
            else:
                sum += num 
                continue

def act17():
    # FUNCTIONS
    # FOR CODE REUSABILITY
    # 1. Built-in Functions
    # input(), type(), print(), len(), int(), evalu(), float(), lower(), upper(), str()
    # 2. Programmer-defined Functions 
    # def function_name(parameters):
    #   *code block*

    # Creation of a function
    def greet_Someone():
        print("Hi, I hope you're having a delightful Tuesday afternoon.")

    def greet_Person(name):
        print(f"Hi {name}, I hope you're having a delightful Tuesday afternoon.")

    def right_Triangle():
        for x in range(1, 6):
            for y in range(1, x+1):
                print("*", end=" ")
            for z in range(6, x, -1):
                print(" ",end= " ")
            print()

    def get_info(name, age):
        print(f"Hi {name}, with age {age} yrs old.")

    def factorial(number):
        # Factorial of 4 - 4 x 3 x 2 x 1 
        fact = 1 
        for x in range(number, 0, -1):
            fact *= x
        print(f"The factorial of {number} is {fact}.")

    resume = True

    print("Mini-Compilation Program\n")

    while resume:
        print("---------------------------------")
        print("WELCOME TO MY COMPILATION PROGRAM")
        print("---------------------------------")
        print("PLEASE SELECT FROM THE OPTIONS BELOW:")
        print("1 -- RIGHT TRIANGLE")
        print("2 -- FACTORIAL")
        print("3 -- GREET SOMEONE")
        print("4 -- GREET PERSON")
        print("5 -- GET INFO")
        print("0 -- EXIT")

        choice = input("Which program would you like to run? (1,2,3,4): ")

        if choice == "1":
            print("THIS IS A PROGRAM THAT WILL SHOW YOU A RIGHT TRIANGLE MADE FROM PYTHON")
            right_Triangle()
            continue
        elif choice == "2":
            print("THIS IS A PROGRAM THAT CALCULATES FACTORIAL")
            number = input("Enter a number: ")

            if not number.isnumeric():
                print("Please enter a number.")
                continue
            else:
                number = eval(number)
                factorial(number)
                continue
        elif choice == "3":
            print("THIS IS A PROGRAM THAT GREETS YOU")
            greet_Someone()
            continue
        elif choice == "4":
            print("THIS IS A PROGRAM THAT GREETS YOU WHILE MENTIONING YOUR NAME")
            name = input("What is your name? ")
            greet_Person(name)
            continue
        elif choice == "5":
            print("THIS IS A PROGRAM THAT GETS YOUR NAME AND AGE")
            name = input("What is your name? ")
            age = input("How old are you? ")
            get_info(name, age)
            continue
        elif choice == "0":
            print("PROGRAM TERMINATED")
            break        
        else:
            print("INVALID CHOICE")
            continue

def act18():
    # DOCUMENT STRINGS / DOCSTRINGS

    print("Docstrings Test Program\n")

    # This function is for calculating factorials.
    def factorial(num):
        """This function is for calculating factorials.
        Just put a number inside the parenthesis."""
        fact = 1
        for x in range(num, 0, -1):
            fact *= x
        return fact

    print("""INPUT:
def factorial(num):
        \"""This function is for calculating factorials.
        Just put a number inside the parenthesis.\"""
        fact = 1
        for x in range(num, 0, -1):
            fact *= x
        return fact\nhelp(factorial)\n\nOUTPUT:""")
    
    help(factorial)

def act19():
    # MODULES
    print("Modules Test Program\n")
    print("""INPUT:
from activity18 import factorial\n
print(f"The factorial of 7 is {factorial(7)}").\n
OUTPUT:\nThe factorial of 7 is 5040.""")

def act20():
    # LIST
    # Instead of using multiple variables such as the following:
    # fruit1 = "banana"
    # fruit2 = "apple"
    # fruit3 = "guyabano"
    # fruit4 = "orange"
    # fruit5 = "avocado"
    
    print("Favorite Fruits Program\n")

    # We can instead use a python list such as the one from below:

    fruits = ["banana", "apple", "guyabano", "orange", "avocado"]

    print("""
INDEX - address/location
                 0         1          2          3         4
    fruits = ["banana", "apple", "guyabano", "orange", "avocado"]""")

    print("\n* Accessing an item:")

    choice = input("Enter the index of your favorite fruit: ")

    if not choice.isnumeric():
        print("\nPlease enter a number.")
    else:
        print(f"\nYour favorite fruit is {fruits[eval(choice)]}.")

    print("\n* Adding another item onto the list:")
    add_fruit = input("Enter a fruit you like: ").lower()
    fruits.append(add_fruit)
    print(f"\n{fruits}")

    print("\n* Inserting an item on a specific index:")

    choice = input("Enter your preffered index for the new fruit you will add: ")
    add_fruit = input("Enter a fruit you like: ").lower()

    if not choice.isnumeric():
        print("\nPlease enter a number.\n")
    else:
        fruits.insert(eval(choice), add_fruit)
        print(f"\n{fruits}")

    print("\n* Removing an item from a specific index:")

    choice = input("Enter the index of the fruit you don't like: ")

    if not choice.isnumeric():
        print("\nPlease enter a number.\n")
    else:
        fruits.pop(eval(choice))
        print(f"\n{fruits}")
