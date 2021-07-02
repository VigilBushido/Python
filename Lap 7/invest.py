#
#   Sergio Munguia
#
#   invest.py
#
#       input: annual interest rate
#
#       processing: 1. ask the user for the rate
#                   2. while loop until the rate doubles the principal
#                   3. display the number of years
#
#       output: amount of years to double principal



def main():

    print("Number of years for an investment to double.")
    print()

    apr = eval(input("What is the annual interest rate? "))

    principal = 1
    years = 0
    interest = apr / 100
    
    while principal < 2:
        principal = principal * (1 + interest)
        years = years + 1

    print("Years to double: ", round(years))

main()
