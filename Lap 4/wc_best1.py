#
#   
#
#   wc.py
#
#
#
#
#
#
def main():

    filename = input("Please enter name of file: ")
    myfile = open(filename,"r")
    data = myfile.read()
    
    words = data.split()

    lines = data.split("\n")
    
    print("Characters: ",len(data))
    print("Words: ", len(words))
    print("Lines: ",len(lines))
main()

