#
#   Sergio Munguia
#
#   month.py
#
#   Input: month number (1-12)
#
#   Processing: 1. ask the user for the month
#               2. cmputer the month of the number
#               3. grab the slice of the month
#                    pos = (n-1) * 3
#
#   Output: Show what the month abbreviation is.


def main():
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    n = eval(input("enter a month number (1-12): "))

    pos = (n-1) * 3

    monthAbbrev = months[pos:pos+3]

    print("The month abbreviation is", monthAbbrev + ".")

main()
            
