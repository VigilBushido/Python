#
#   Sergio Munguia
#
#   spere.py
#
#   Input: ask the user for the radius of the sphere
#   Processing: compute the volume
#               compute the surface area
#   Output: Show the user both units of measurement rounded to 2nd place.          
#
#   Volume & Area formulas:
#   V=4/3 * pi * r ** 3
#
#   A = 4 * pi * r ** 2

import math

def main():
    print("Volume and Surface Area of a Sphere ...")
    print()

    radius = eval(input("Please enter the radius of the sphere: "))
    volume = 4/3 * math.pi * radius ** 3
    area = 4 * math.pi * radius ** 2

    area = round(area, 2)
    volume = round(volume, 2)

    print("The volume is ", volume,"cubic units.")
    print("The surface area is ", area,"square units.")

main()

    
    
    
