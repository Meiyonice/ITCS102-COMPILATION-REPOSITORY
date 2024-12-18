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
    print(f"The factorial of {number} is {fact}")

resume = True

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

    choice = input("Which program would you like to run? (1,2,3,4,5,0): ")

    if choice == "1":
        print("THIS IS A PROGRAM THAT WILL SHOW YOU A RIGHT TRIANGLE MADE FROM PYTHON")
        right_Triangle()
        continue
    elif choice == "2":
        print("THIS IS A PROGRAM THAT CALCULATES FACTORIAL")
        number = eval(input("Enter a number: "))
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