# LOOPING STATEMENTS
# NESTED FOR LOOPS
# Repeating Horizontal Right Triangles

num = eval(input("Enter the amount of triangles: "))

for w in range(1, 6):
    for x in range(num):
        for y in range(w):
            print("^", end=" ")
        for z in range(6, w, -1):
            print(" ", end=" ")
        print(end="")
    print()