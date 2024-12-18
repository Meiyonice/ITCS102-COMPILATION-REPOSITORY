# ARITHMETIC OPERATORS
# | + | - | * | / | % | ** | // |
# Fahrenheit To Celcius Converter

fah = eval(input("Enter temperature in FAHRENHEIT: "))

c = (fah - 32) * 5 / 9

print(f"{fah} degrees Fahrenheit converted to Celcius is {round(c,2)} degrees.")