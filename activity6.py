# INTRODUCTION TO DECISION STRUCTURES
# In some programming language or tutorials, it's reffered to as:
# CONDITIONAL STATEMENTS OR SELECTION STATEMENTS

password = "secret"

my_password = input("Enter your password: ").lower()

# RELATIONAL OPERATORS
# | == | != | > | < | >= | <= |
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
