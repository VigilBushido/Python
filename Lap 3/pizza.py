#
#   Sergio Munguia
#
#   pizza.py
#
#   Input: Ask the user for diameter (inches)
#          Ask the user for price (dollars)
#
#   Processing: A = math.pi * radius ** 2
#
#   Output: the cost per square inch

import math 

def main():
    print("This program computes the cost per square inch of a pizza")
    print()

    diameter = eval(input("Please enter the diameter of the pizza (inches): "))
    price = eval(input("Please enter the price of the pizza (dollars): "))
    area = math.pi * (diameter/2) ** 2

    cost = price / area
    cost = cost * 100
    cost = int(cost)

    print("The cost is ", cost,"cents per square inch")

main()


         
