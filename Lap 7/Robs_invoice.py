#
#   Robert Earnest
#
#   invoice.py
#
#   Creates an invoice based on the data stored in customerinvoice.txt
#
#   Input: The data from the file customerservice.txt
#
#   Processing: 1. Open file for reading
#               2. Read the lines of the file formatting them into a table
#               3. Display the completed invoice receipt table
#
#   Output: An invoice created from the file data.
#

def main():

    infile=open("customerinvoice.txt",'r')

    name=infile.readline()

    print("Broward Clothing Store Receipt\n")
    print(41*"*","\n")

    print("Customer name:",name)

    date=infile.readline()
    invnum=infile.readline()
    
    print("Date:",date[0:10],end="")

    temp1="Invoice Number: "+invnum
    print(temp1.rjust(35))
    print("\n")

    print("Item","Price".rjust(15))
    print()

    print(25*"-","\n")

    sub=0
    item=infile.readline()
    
    while (item != ""):
        
        item=item.split()
        price = eval(item[1])
        sub=sub+price
        print(item[0].ljust(10),("$"+"{0:0.2f}".format(price)).rjust(10))
        print()
        
        item=infile.readline()

    
    print("\nSubtotal:",("$"+"{0}".format(sub)).rjust(11))
    
    tax=sub*.07
    print("\nTax:",("${0:0.2f}".format(tax)).rjust(15))
    
    total=tax+sub
    print("\nTotal:",("${0:0.2f}".format(total)).rjust(14))

    infile.close()
        
main()
    
    
    
