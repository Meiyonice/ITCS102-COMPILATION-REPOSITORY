# LOOPING STATEMENTS
# FOR LOOP
# Factorial

num = eval(input("Enter a number: "))

res = 1

for x in range(num, 0, -1):
    res *= x

print(f"The factorial of {num} is {res}.")