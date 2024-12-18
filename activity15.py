# HYBRID LOOP
# Combination of for loop and while loop
# Goal: Ask the user if he/she wants to print more triangle, user can type yes or no.
# If the user selects yes, program will print another triangle.
# If no, program will terminate.

import os

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
        os.system("cls")
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
        print("PLEASE TYPE \"yes\" OR \"no\"")
        continue