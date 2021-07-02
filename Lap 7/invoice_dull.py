#
#   Sergio Munguia
#
#   invoice.py
#
#   input: customerInvoice.txt
#
#   processing: 
#   CustomerLastname, CustomerFirstname
#   Date
#   Phone Number
#   Item1-Description  Item1-Cost (15 space blocks)
#               1. Open file & Calculate the subtotal, tax, and total values
#                   considering a 7% sales tax
#               2. Display The Results
#
#   Ouput: Display a receipt form of the results
#

def main():
    custinfo = open("customerInvoice.txt",'r')
    data = custinfo.read()
    cust = data.split()

    TAX = .07

    #print header
    print("Broward Clothing Store Receipt")
    print("*"*50)
    print("Customer Name: ", cust[0] + ",", cust[1])
    print("Date: ", cust[2]," " * 7,"Invioce Number: ", cust[3])
    print()
    print()
    print("{0:10}{1:10}".format("Item","Price"))
    print("-"*16)
    print("{0:10}{1:10}".format(cust[4],"$" + cust[5]))
    print("{0:10}{1:10}".format(cust[6],"$" + cust[7]))
    print("{0:10}{1:10}".format(cust[8],"$" + cust[9]))
    print()
    cust5 = float(cust[5])
    cust7 = float(cust[7])
    cust9 = float(cust[9])
    
    subtotal = cust5 + cust7 + cust9
    
    tax = subtotal * TAX
    total = tax + subtotal

    print("{0:10}{1:1}".format("Subtotal: ", "$"), end = "")
    print(round(subtotal, 2))
    print("{0:10}{1:1}".format("Tax: ", "$"), end = "")
    print(round(tax, 2))
    print("{0:10}{1:1}".format("Total: ", "$"), end = "")
    print(round(total, 2))
main()
    
    
    

