#
#   Sergio Munguia
#
#   sumNums.py
#
#   sums a series of numbers entered by the user
#
#   input: How many numbers are to be summed (n)
#           Each of the n numbers
#
#   Processing: 1. Prompt user for how many numbers to sum(n)
#               2. For each of the n numbers
#                   prompt user for number
#                   add number to accumulator (sum)
#               3. Display sum
#
#   Output: The sum of a series of numbers entered by the user

def main():
    print("Sum of numbers ...")
    print()
    
    n = eval(input("How many numbers do you want to sum? "))

    sum = 0
    
    for i in range(n):
            number = eval(input("\tEnter number: "))
            sum = sum + number

    print()
    print("The sum of the numbers is", sum)

main()
    
