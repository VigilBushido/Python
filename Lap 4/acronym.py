#
#   Sergio Munguia
#
#   acronym.py    
#   
# 
#   input: enter a phrase
#
#   processing: 1. ask for the user to enter a phrase
#               2. define acronym variable
#               3. For loop the phrase.split
#               4. Index the abbreviation out of each value
#               5. + Concatenation the 1st letter of each word
#               6. Show the abbreviation to user
#
#   output: Display the abbreviation for the phrase.
def main():

    print("This program builds acronyms")
    print()

    phrase = input("Enter a phrase: ")
    print()
    acronym = ""

    for a in phrase.split():

         acronym = acronym + a[0].upper()
    
    print("The acronym is:", acronym)


main()
