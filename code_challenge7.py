# CONDITIONALS
# GROCERY
# All product prices would be taxed 12.3% added to the product price.
# If the untaxed price is more than 4000 a discount of 3.8% of the ontaxed product price would be applied.
# If age is more than 60 and not higher 150 a senior discount would be applied to the taxed price, senior discount is 12.3%.
# Notify customer of his change.

name = input("Enter your name : ")
did_grocery = input("Did you purchase a grocery today? (Y/N) : ")

# The program will continue if the user answers Y (yes), otherwise terminate
if did_grocery.lower() == "y" :
    print(f"\n\tHi {name}, Welcome to GROCERY!")
    print("======" * 8)

    grocery_item = input("Item you purchased : ")
    item_price = input("Enter item price : ")
    age = input("Enter your age : ")
    payment = input("Enter payment amount: ")

    if not (item_price.isnumeric() and age.isnumeric() and payment.isnumeric()):
        print("Please only enter numbers for item price, age and payment.")
    else:
        item_price = eval(item_price)
        age = eval(age)
        payment = eval(payment)

        # FEEDBACK
        # Item and price
        print(f"| Hi {name}, you purchased {grocery_item}.")
        print(f"--> Original item price: {round(item_price,2)} pesos")

        # Item price OVER 4000 will receive a discount of 3.8%
        if item_price > 4000 :
            item_price -= (item_price * .038)
            print(f"| The item price is over 4000 pesos.\n| You're eligible for a discount of 3.8%.")
            print(f"--> Discounted item price: {round(item_price,2)} pesos")
        else :
            print("| The item price is not over 4000 pesos.\n| You're not eligible for a discount.")
        
        # Tax of 12.3% will ALWAYS be added to item price
        taxed_price = item_price + (item_price * .123)
        print(f"| A tax of 12.3% will be added to the item price.")
        print(f"--> Taxed item price: {round(taxed_price,2)} pesos")
    
        # Senior discount of 12.3% will be applied to TAXED item price if user is 60-150 years old
        if age >= 60 and age <= 150 :
            taxed_price -= taxed_price * .123
            print("| You're eligible for a senior discount of 12.3%.")
            print(f"--> Item price after senior discount: {round(taxed_price,2)} pesos\n")
        elif age <= 6 :
            print("| You're not old enough to buy grocery.")
            print("| You're not eligible for a senior discount of 12.3%.\n")
        elif age > 150 :
            print("| How are you still alive?!")
            print("| You're not eligible for a senior discount of 12.3%.\n")
        else :
            print("| You're not eligible for a senior discount of 12.3%.\n")

        # Final item price with tax and with/without discount/s
        print(f"Final item price: {round(taxed_price,2)} pesos")
        
        # User change
        change = payment - taxed_price

        if payment >= taxed_price and payment <= 0:  
            print(f"You paid {payment} pesos and received {round(change,2)} pesos in change.")
        else :
            print(f"You only paid {payment} pesos. You owed {round(change,2) * -1} pesos.")
        print("Thank you for using the program. Have a nice day.")
else :
    print("Thank you for using the program. Have a nice day.")