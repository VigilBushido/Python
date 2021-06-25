#
#   Sergio Munguia
#
#   p3.py
#   A program that computes the equivalent of a dollar amount in change using quarters,
#   dimes, and pennies. No nickels are used for conversion.

while(True):
    dollar = float(input("Enter dollar amount: "))
    if dollar < 0: 
        import sys
        sys.exit("Invalid Input")
    amount = int(dollar * 100)
    totalcoins = 0
    quarters = 0
    dimes = 0
    pennies = 0
    
    if  amount != 0 and amount >= 100:
        quarters = amount // 25
        amount %= 25
        totalcoins += quarters
    if  amount != 0 and amount >= 10: 
        dimes = amount // 10
        amount %= 10
        totalcoins +=  dimes
    if  amount != 0 and amount >= 1:
        pennies = amount // 1
        amount %= 1
        totalcoins +=  pennies

    print("$",dollar," makes ",quarters," quarters ",dimes," dimes ",pennies," pennies "\
          "(coins ",totalcoins,"), total amount in coins: $",dollar)
    