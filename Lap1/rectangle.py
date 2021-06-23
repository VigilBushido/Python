#
#   Sergio Munguia
#
#   rectangle.py
#
#   prompt user for the width and height of a rectangle,
#   calculate its area, and display the result
#

def main():
    #   prompt user for the width and height of a rectangle,
    width = eval(input("Please enter rectangle's width: "))
    height = eval(input(" \"      \"        \"      height: "))

    #   calculate its area
    area = width * height

    #   display the result
    print("The area of a ", width, " by ", height," rectangle is ", area, "\n")

main()
    
