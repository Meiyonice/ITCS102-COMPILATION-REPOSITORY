# DOCUMENT STRINGS / DOCSTRINGS

# This function is for calculating factorials.
def factorial(num):
    """This function is for calculating factorials.
    Just put a number inside the parenthesis."""
    fact = 1
    for x in range(num, 0, -1):
        fact *= x
    return fact

# help(input)
# help(print)
# help(help)
help(factorial)

print(factorial(10))