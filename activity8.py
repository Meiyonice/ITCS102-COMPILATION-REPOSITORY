# LOOPING STATEMENTS
# These statements allow you to repeat code blocks.
# TYPES OF LOOP:
# FOR LOOP - Use if you have certain or definite amout of times to repeart a code block.
# WHILE LOOP - Use if you are uncertain on the amount of times to repeat a code block.
# Goal: Loop for 10 times and add all random number inputs.

result = 0
even = 0
odd = 0

for loop in range(1, 11):
    num = eval(input(f"Input #{loop}: "))
    result += num

    # Add all even and odd numbers to themselves.
    if num % 2 == 0:
        even += num
    elif num % 1 == 0:
        odd += num
    else:
        print("The number is not an integer.")

print(f"The sum of all inputs is {result}.")
print(f"The sum of all EVEN numbers is {even}.")
print(f"The sum of all ODD numbers is {odd}.")