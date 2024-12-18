# LOOPS
# NESTED FOR LOOPS
# Inverted Mirrored Right Triangle

print()

for x in range(1, 11):
    for a in range(1, x):
        print("  ", end="")
    for b in range(10, x, -1):
        print(" *", end="")
    print()