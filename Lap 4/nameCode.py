#
#   Sergio munguia
#
#   nameCode.py
#
#   Program translates a name into a numeric code
#
#   Input: User's name
#
#   Processing: 1. Prompt user for his/her name
#               2. For each character in name
#                       Retrieve Unicode representation
#                       Add value to an accumulator
#               3. Display accumulated value
#
#   Output: Display the code

def main():
    # Prompt user for his/her name
    name = input("Please enter your name: ")


    # Determine names' numeric code
    code = 0
    for c in name:
        code = code + ord(c)

    # Display code
    print("The code for your name is", code)

main()
