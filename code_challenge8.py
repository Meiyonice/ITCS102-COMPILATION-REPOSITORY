# LOOPS
# FOR LOOPS
# Loop for 10 times.
# Sum of all random inputs by the user.

print("Enter 10 numbers! ^v^\n")

total = 0
even = 0
odd = 0

for x in range(1,11):
    num = eval(input(f"Input #{x} : "))
    total += num

    # Sum of all even numbers and sum of all odd numbers.
    if num % 2 == 0:
        even += num
    elif num % 1 == 0:  # I also put a condition for odd numbers to filter out fractions and decimal numbers.
        odd += num
    else:
        pass
print()

print(f"The sum of all inputs is {round(total, 2)}.")

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