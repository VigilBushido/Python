#
#   Sergio Munguia
#
#   fibonacci.py
#
#   computes and outputs the nth Fibonacci number
#
#       Input: nth number
#       Processsing: 1. Prompt user for number n
#                    2. Determine Fibonacci number such as:
#                       If n == 1 or n == 2
#                           Fibonacci number is 1
#                       Else
#                           Fibonacci number is the sum of the previous two
#                    3. Display the nth Fibonacci number
#
#       Output: nth fibonacci number
#
#       fibonacci : 1, 1 ,2, 3, 5, 8, ....    
#       processing: 1. display the fibonacci place value
#

def main():
    #title
    print("This program calculates the nth Fibonacci value.")
    
    # Prompt user for number n
    n = eval(input("Enter the value of n: "))

    curr, prev = 1, 1

    # Determine Fibonacci number
    for i in range(n-2):
        curr, prev = curr + prev, curr
            
    # Display nth Fibonacci number
    print("The nth Fibonacci number is ", curr)

main()
        
