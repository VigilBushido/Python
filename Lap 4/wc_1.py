#
#   Sergio Munguia
#
#   wc.py    
#   
#   input: File name & extension
#
#   processing: 1. Count the Characters
#               2. Count the Words
#               3. Count the Lines 
#               4. Display amount of Characters:
#                  Display amount of Words
#                  Display amount of Lines
#
#   output: Display the total amount of Characters, Words, and Lines in the file.
#

def main():
    print("File wordcount")
    print()
    infile = input("Enter in a file name: ")
    myfile = open("infile", "r")
    data = myfile.read()
    
    amtofchars = len(data)
    print("The Amount of Characters is: ", amtofchars)

    text = open ("infile", 'r')
    lines = list(text)
    text.close()
    amtofwords = 0
    for line in lines:
        amtofwords = amtofwords + len(line.split())
    print("The Amount of Words is: ", amtofwords)

    numlines = data.count("\n") + 1
    print("The Amount of Lines is: ", numlines)

    infile.close()
    
main()
    
    



    
