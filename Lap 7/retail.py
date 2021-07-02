#
#       Sergio Munguia
#
#       retail.py
#
#       Calculates retail prices based on the cost of an item
#       and markup rate
#
#   Input: Cost of item
#
#   Processing: 1. While (there are items)
#                       1. Prompt user for cost of item
#                       2. Calculate Item's retail price
#                          retail_price = cost * 2.5
#                       3. Display retail price
#
#   Output: Item's retail price

def main():
    # Declare constant markup
    MARKUP = 2.5

    
    print("Retail Price Calculator")
    print()

    choice = "y"

    while (choice.lower() == "y"):
        #Prompt user for cost of item
        cost = eval(input("Enter item's wholesale cost: "))
        while (cost <= 0):
            print("Error ... Cost must be greater than 0")
            print()
            cost = eval(input("Enter item's wholesale cost: "))

        # Calculate Item's retail price
        retail = cost * MARKUP

        # Display retail price
        print("The retail price is ${0:0.2f}".format(retail))

        choice = input("Do you have another item (y/n)? ").lower()
        print()

main()
        
        
            
