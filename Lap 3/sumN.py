#
#   Sergio Munguia
#
#   sumN.py
#
#   Input: ask the user to input a value for n
#
#   Processing: find the sum of the first n natural numbers where
#               the value of n is provided by the user
#
#   Output: Display the value

def main():
    print("This program finds the sum of the first n natural numbers.")
    print()

    n = eval(input("Please enter a value for n: "))

    sum = 0
    for add in range(n + 1):
         sum = sum + add
         
    print("The sum of the first natural numbers where ", n, "is the value is a sum of ", sum,"")

main()
