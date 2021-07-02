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
    name = custinfo.readline()
    date = custinfo.readline()
    invoice = custinfo.readline()
    
    TAX = .07

    #print header
    print("Broward Clothing Store Receipt")
    print("*"*50)
    print("Customer Name: ", name)
    print("Date: " + date[0:10], "{}{}".format("Invoice Number: ", invoice).rjust(30))
    print()
    print("{0:15}{1:15}".format("Item","Price"))
    print("-"*20)
    
    sub = 0

    item = custinfo.readline()
    
    while (item != ""):
        item = item.split()
        price = eval(item[1])
        sub = sub + price
        print(item[0].ljust(10),("$"+"{0:0.2f}".format(price)).rjust(10))
        
        item = custinfo.readline()  
    
    tax = sub * TAX
    total = tax + sub
    print()

    print("{0:10}{1:1}".format("Subtotal: ", "$"), end = "")
    print(round(sub, 2))
    print("{0:10}{1:1}".format("Tax: ", "$"), end = "")
    print(round(tax, 2))
    print("{0:10}{1:1}".format("Total: ", "$"), end = "")
    print(round(total, 2))

    custinfo.close()
main()
    
    
    

