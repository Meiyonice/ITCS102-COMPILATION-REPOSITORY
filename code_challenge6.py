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
	age = eval(input("Enter your age : "))
	print()

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