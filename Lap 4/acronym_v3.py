#
#   Sergio Munguia
#
#   acronym_v3.py    
#   
# 
#   input: enter a phrase
#
#   processing: 1. ask for the user to enter a phrase
#               2. capitolize the 1st letter of each word
#               3. split the words and assign them to variables
#               4. Index the abbreviation out of each variable
#               5. + Concatenation the 1st letter of each word
#               6. Show the abbreviation to user
#
#   output: Display the abbreviation for the phrase.

def main():
    print("This program builds acronyms")
    print()
    phrase = input("Enter a phrase: ")

    phrase = phrase.title()
    phrase1, phrase2, phrase3 = phrase.split()

    print("The acronym is:", end = " ")
    print(phrase1[0] + phrase2[0] + phrase3[0])

main()
    

    
