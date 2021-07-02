#
#   Sergio Munguia
#
#   sumOfsquares.py
#
#   input: file to evaulate numbers
#   processing: 1. ask the user for the filename
#               2. open the file
#               3. def square function & sumlist function
#               4.
#
#   output: displays the squares, sums, and sums of squares
#           for the numbers in the file
#
#
#    readlines() = converts the numbers into a list of str data type

def main():
    print("Program to find sum of squares from numbers in a file")
    print()
    filename = input("Enter a filename: ")
    print()
    data = open(filename, 'r')
    numstrlist = data.readlines()

    n = 0
    print("List of numbers: ")
    for num in numstrlist:
        numlist = int(numstrlist[n])
        print(numlist, end = " ")
        n = n + 1

    n = 0
    sumofsqr = 0
    print("\n")
    print("Squares of numbers: ")
    for num in numstrlist:
        numlist = int(numstrlist[n])
        sqrnum = squareEach(numlist)
        sumofsqr = sumList(sqrnum, sumofsqr)
        print(sqrnum, end = " ")
        n = n + 1

    print("\n")
    print("Sum of squares: ", end = "")
    print(sumofsqr, end = " ")

    
def squareEach(number):
    sqrnum = number ** 2
    return sqrnum
    
def sumList(number, number2):
    total = number + number2
    return total

    data.close()
main()


    
