#
#   Sergio Munguia
#
#   encode.py
#
#   input: a phrase.
#
#   processing: 1. ask the user to enter a phrase
#               2. open file
#               3. compute the encypted code from the phrase
#               3. print to outfile
#               4. display what has been encrypted
#
#   output: show the user what has been encrypted

def main():
    x = input("Please enter a phrase: ")
    outfile = open("code.txt","w")
    for ch in x:
        encrypted = ord(ch) * 8 - 1
        print(encrypted, end = " ",file = outfile)
    print (x)
    print("This has been encrypted and save on file.")
    outfile.close()

main()
