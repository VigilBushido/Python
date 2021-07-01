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

def main():
    print("File wordcount")
    print()

    filename = input("Please enter name of file: ")
    myfile = open(filename,"r")
    data = myfile.read()
    
    words = data.split()

    lines = data.split("\n")
    
    print("The Amount of Characters: ",len(data))
    print("The Amount of Words: ", len(words))
    print("The Amount of Lines: ",len(lines))
    
main()

