# LOOPING STATEMENTS
# WHILE LOOP 

# Boolean variable / trigger 
resume = True 

# While resume is set to true, the loop will continue. 
# Continue to ask for a number.
# Once user types the number ZERO (0), terminate the loop
# And get the summation of all the number(s) given.
sum = 0
while resume:
    num = eval(input("Enter any number: "))

    if num == 0:
        print("LOOP STOPPED")
        print(f"The sum of all the numbers given is {sum}")
        break
        resume = False # To make sure that the loop will stop.
    else:
        sum += num 
        continue