# CONDITIONALS
# Create a program that will accept Prelim, Midterm, Semi-Final, Quiz, and Project Grade.
# Compute the final grade: FG = (prelim x 15%) + (midterm x 15%) +
# (semifinal x 15%) + (final x 15%) + (quiz x 25%) + (project x 15%).
# Display a remark "Congratulations! You passed the course" if final grade is 75 and above;
# Otherwise display "Sorry, you failed."

print("|Final Grade Calculator|\n")

# Input grades
prelim = eval(input("Enter Prelim Exam Grade : "))
midterm = eval(input("Enter Midterm Exam Grade : "))
semifinal= eval(input("Enter Semi-Final Exam Grade : "))
final = eval(input("Enter Final Exam Grade : "))
quiz = eval(input("Enter Quiz Grade : "))
project = eval(input("Enter Project Grade : "))

# Final grade formula
FG = (prelim * .15) + (midterm * .15) + (semifinal * .15) + (final * .15) + (quiz * .25) + (project * .15)
FG = round(FG,2)
print()

# Requirement to pass
if FG >= 75:
	print(f"Your Final Grade is {FG}.")
	print("Congratulations! You passed the course.")
else:
	print(f"Your Final Grade is {FG}.")
	print("Sorry, you failed.")