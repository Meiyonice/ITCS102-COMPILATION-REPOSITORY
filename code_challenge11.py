# LOOPS
# NESTED FOR LOOPS
# Diamond with one points

for a in range(0, 5):
    for b in range(5, a, -1):
        print(" ", end=" ")
    for c in range(0, a):
        print("*", end=" ")
    for d in range(1, a):
        print("*", end=" ")
    print()
for w in range(0, 4):
    for x in range(0, w + 2):
        print(" ", end=" ")
    for y in range(3, w, -1):
        print("*", end=" ")
    for z in range(2, w, -1):
        print("*", end=" ")
    print()

# Another way I found while trying to make one for loop for the asterisks

# for a in range(1, 8, 2):
#     for b in range(8, a, -2):
#         print(" ", end=" ")
#     for c in range(0, a):
#         print("*", end=" ")
#     print()
# for x in range(1, 6, 2):
#     for y in range(-2, x, 2):
#         print(" ", end=" ")
#     for z in range(x, 6):
#         print("*", end=" ")
#     print()