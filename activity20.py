# LIST
# Instead of using multiple variables such as the following:
# fruit1 = "banana"
# fruit2 = "apple"
# fruit3 = "guyabano"
# fruit4 = "orange"
# fruit5 = "avocado"

# We can instead use a python list such as the one from below:

fruits = ["banana", "apple", "guyabano", "orange", "avocado"]

print(fruits)

# Accessing an item
# INDEX - address/location
#              0         1          2          3         4
# fruits = ["banana", "apple", "guyabano", "orange", "avocado"]
print(f"My favorite fruit is {fruits[2]}.")

# Adding another item onto the list:
fruits.append("longgan")
print(fruits)

# Inserting an item on a specific index:
fruits.insert(3, "chico")
print(fruits)