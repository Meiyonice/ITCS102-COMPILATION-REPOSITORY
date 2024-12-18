# LOOPS
# NESTED FOR LOOPS
# Star and Caret Diamond

for a in range(0, 6):
    for b in range(6, a, -1):
        print(" ", end=" ")
    for c in range(0, a):
        print("*", end=" ")
    for d in range(0, a):
        print("^", end=" ")
    print()
for w in range(1, 6):
    for x in range(0, w+1):
        print(" ", end=" ")
    for y in range(5, w, -1):
        print("^", end=" ")
    for z in range(5, w, -1):
        print("*", end=" ")
    print()