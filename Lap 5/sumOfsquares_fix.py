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
    m = 0
    lnum = 0
    total = 0
    print("\n")
    print("Squares of numbers: ")
    for num in numstrlist:
        numlist = int(numstrlist[n])
        numlist2 = int(numstrlist[m])
        sqrnum = squareEach(numlist)
        number2 = squareEach(numlist2)
        sumofsqr = sumList(sqrnum, number2)
        total = sumofsqr + sumofsqr
        print(sqrnum, end = " ")
        n = n + 1
        m = m + 2

    print("\n")
    print("Sum of squares: ", end = "")
    print(total, end = " ")

    
def squareEach(number):
    sqrnum = number ** 2
        
    return sqrnum
    
def sumList(number, number2):
    total = number + number2
    return total

    data.close()
main()


    
