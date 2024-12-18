# ARITHMETIC OPERATORS
# Simple Calculator

num1 = eval(input("Enter the first number : "))
num2 = eval(input("Enter the second number : "))

sum = num1 + num2
diff = num1 - num2
prod = num1 * num2
quot = num1 / num2
expo = num1 ** num2
rem = num1 % num2
floor_div = num1 // num2

print("\nThe sum of", num1, "and", num2, "is", sum)
print("The difference of", num1, "and", num2, "is", diff)
print("The product of", num1, "and", num2, "is", prod)
print("The quotient of", num1, "and", num2, "is", quot)
print(num1, "exponent by", num2, "is", num1 ** expo)
print("The remainder of", num1, "and", num2, "is", rem)
print("The floor division of", num1, "and", num2, "is", floor_div)