# LOGICAL OPERATORS
# Logical operators are used to combine and check more than one conditions.
# (and) operator - The result would be True only if both conditions are True.
# (or) operator - The result would be True if either conditions are True.
# (not) operator - It would reverse any result of the condition.
# Scholar Grant Application Program

name = input("What is your name? ")
isEnrolled = input("Are you currently enrolled in DLL? (y/n) ").lower()

if isEnrolled == "y":
    print(f"Hi, {name}. Welcome to the DLL Scholarship Grant System!")

    # Is student's age 18 to 35?
    age = eval(input("How old are you right now? "))

    if age >= 18 and age <= 35:
        print("Your passed the age requirement.")

        # Is student's grades 86 to 100?
        grades = eval(input("What was your last GWA? "))

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