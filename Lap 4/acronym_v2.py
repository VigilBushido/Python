#
#   Sergio Munguia
#
#   acronym.py    
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
    phrase = phrase.split()
    # 1st index the values of the list
    phrase0 = phrase[0]
    phrase1 = phrase[1]
    phrase2 = phrase[2]
    # 2nd index only the begining letter out of those values stored in variable
    phrase0 = phrase0[0]
    phrase1 = phrase1[0]
    phrase2 = phrase2[0]

    print("The acronym is:", end = " ")
    print(phrase0 + phrase1 + phrase2)

main()
