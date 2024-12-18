# LOOPING STATEMENTS
# NESTED FOR LOOP
# Upside-Down Mirrored Right Triangle

for w in range(1, 6):
    for x in range(1, w+1):
        print(" ", end=" ")
    for y in range(6, w, -1):
        print("*", end=" ")
    for z in range(6, w, -1):
        print("^", end=" ")
    print()