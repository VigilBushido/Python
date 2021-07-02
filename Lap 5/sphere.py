#
#   Sergio Munguia
#
#   sphere.py
#
#   Calculate the area/volume of a sphere given its radius
#
#   Input: Radius of a sphere
#
#   Processing: 1. Display menu with the following options:
#                       1. Calculate area of sphere
#                       2. Calculate volume of sphere
#                       3. Quit
#               2. While (option != Quit)
#                       Prompt user for radius
#                       if (option == Area)
#                           Calculate are of sphere:
#                               Area = 4 * pi * r ** 2
#                           Display Area
#                       if (option == Volume)
#                           Calculate Volume of sphere:
#                               Volume = 4/3 * pi * r ** 3
#                           Display Volume
#
#   Output: Area/Volume of a sphere
#
#   DisplayMenu()
#
import math

def DisplayMenu():
    print()
    print("Please choose one of the following options:")
    print("\t1. Calculate area of a sphere")
    print("\t2. Calculate volume of a sphere")
    print("\t3. Quit")
    print()
    option = eval(input("Option: "))
    print()
    
    return option
#
# Area(radius)
#
# Calculates the area of a sphere given its radius
def Area(radius):
    area = 4 * math.pi * radius ** 2
    return area
#
# Volume(radius)
#
# Calculates the volume of a sphere given its radius
def Volume(radius):
    volume = 4/3 * math.pi * radius ** 3
    return volume

def main():
    print("Sphere Calculator ...")
    
    option = 1
    while (option != 3):
        # Display menu
        option = DisplayMenu()
        
        # Drive menu options
        if (option == 1):
            # Calculate area of a sphere
            print("Area of a sphere ...")
            radius = eval(input("Enter radius: "))
            area = Area(radius)
            print("The area of the sphere is {0:0.3f}".format(area))
        elif (option == 2):
            # Calculate volume of a sphere
            print("Volume of a sphere ...")
            radius = eval(input("Enter radius: "))
            volume = Volume(radius)
            print("The volume of the sphere is {0:0.3f}".format(volume))
        elif (option ==3):
            # Quit
            print("Goodbye ...")
        else:
            # Invalid option
            print("Error ... Invalid option")

main()

        

        
        
