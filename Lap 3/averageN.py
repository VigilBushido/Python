#
#   Sergio Munguia
#
#   averageN.py
#
#   Input: ask the user for the amount of numbers
#
#   Processing: add all the numbers and divide them by the value of n 
#
#   Output: display the average

def main():
    print("Geometric Sequence")
    print()

    n = eval(input("What is the value of the index? : "))
    l, w = eval(input("What are the size of length & width? (seperated by ,): "))

    for i in range(n):
             l = l*.75
             w = w*.75

    l = round(l,2)
    w = round(w,2)
    print()
    print("the values at",n,"th","index of Length is", l,"and Width is", w)

main()

    
    
