# LOOPING STATEMENTS
# NESTED FOR LOOP
# Sample 2

for x in range(1, 11):
    print(x, end="")
    for a in range(1, x+1):
        print("*", end="")
    print(x)