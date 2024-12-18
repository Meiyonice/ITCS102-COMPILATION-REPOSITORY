# ARITHMETIC OPERATORS
# Philippine Denominations

name = input("Enter your username : ")
deposit = eval(input("Enter the amount to deposit : "))

print("========" * 12)
print(f"Hello, {name}. The breakdown of your deposit amount in Philippine denomination is as follows :\n")

thou = deposit // 1000
thou_rem = deposit % 1000

fiveh = thou_rem // 500
fiveh_rem = thou_rem % 500

twoh = fiveh_rem // 200
twoh_rem = fiveh_rem % 200

oneh = twoh_rem // 100
oneh_rem = twoh_rem % 100

fifty = oneh_rem // 50
fifty_rem = oneh_rem % 50

twenty = fifty_rem // 20
twenty_rem = fifty_rem % 20

ten = twenty_rem // 10
ten_rem = twenty_rem % 10

five = ten_rem // 5
five_rem = ten_rem % 5

one = five_rem // 1

print(thou, "\t-\t| 1000")
print(fiveh, "\t-\t| 500")
print(twoh, "\t-\t| 200")
print(oneh, "\t-\t| 100")
print(fifty, "\t-\t| 50")
print(twenty, "\t-\t| 20")
print(ten, "\t-\t| 10")
print(five, "\t-\t| 5")
print(one, "\t-\t| 1")