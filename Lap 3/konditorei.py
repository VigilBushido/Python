#
#   Sergio Munguia
#
#   konditorei.py
#
#   Input: ask how many pounds of coffee does the user want
#
#   Processing: coffee shop sells coffee at $10.50 a pound plus the cost of shipping.
#               Each order ships for $0.86 per pound + $1.50 fixed cost for overhead
#
#
#   Output:  Displays the cost of
#                Coffee
#                Shipping
#                ---------
#                Total

def main():
    print("Welcome to the konditorei!")
    print()

    pounds = eval(input("How many pounds of coffee do you want? "))
    print()

    coffee = pounds * 10.50
    shipping = pounds * .86 + 1.50

    coffee = round(coffee , 2)
    shipping = round(shipping, 2)

    total = coffee + shipping
    total = round(total, 2)

    print("Cost of Coffee: ", coffee,"")
    print("Cost of Shipping: ", shipping,"")
    print("-------------------------")
    print("Total Due: ", total,"")

main()
    

    
