# LOOPS
# WHILE LOOPS
# Add all inputs until the input is 0.

print("[Instructions: Give numbers you want to add, then input 0 if you want the sum or to end the program.]\n")

# Boolean Variable 
isRepeat = True
sum = 0

while isRepeat:
    num = eval(input("Enter a number : "))
    sum += num

    # If the input is 0, the loop will stop.
    if num == 0 and sum > 0:
        print(f"\nThe sum of all numbers given is {sum}.")
        print("Thank you for using the program!")
        isRepeat = False
        break # To make sure that the loop will stop.
    elif sum == 0:
        print("\nThank you for using the program!")
        isRepeat = False
        break # To make sure that the loop will stop.

# # SHORTER VERSON

# print("[Instructions: Give numbers you want to add, then input 0 if you want the sum or to end the program.]\n")

# sum = 0

# while True:
#     num = eval(input("Enter a number : "))
#     sum += num

#     # If the input is 0, the loop will stop.
#     if num == 0 and sum > 0:
#         print(f"\nThe sum of all numbers given is {sum}.")
#         print("Thank you for using the program!")
#         break
#     elif sum == 0:
#         print("\nThank you for using the program!")
#         break