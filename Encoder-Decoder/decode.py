#
#
#   Sergio Munguia
#
#   decode.py
#
#   processing: 1. read the txt file
#               2. (decrypt)compute the letters
#               4. Show the user the decrepted message
#
#   output: display the message
#
def main():
    inphrase = open ("code.txt","r").read()
    phrase = ""

    for i in inphrase.split():
        codename = eval(i)//8 + 1
        phrase = phrase + chr(codename)

    print("This is your decrypted phrase: ", phrase)

main()
