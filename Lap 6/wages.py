#
#   Sergio Munguia
#
#   wages.py
#
#   input: hours worked & hourly wage
#
#   processing: 1. ask the user for the hours worked
#               2. ask the user for the hourly wage
#               3. weekly wage = 40 * HW + (Hours-40) * HW * 1.5
#               4. show the user his weekly pay
#                                                           
#   output: display weekly pay (including overtime)

def main():

    print("Weekly Pay Calculator")
    print()
        
    hours = eval(input("Enter hours worked: "))
    hw = eval(input("Enter hourly wage: "))

    if hours > 40:
        weekpay = 40 * hw + (hours - 40) * hw * 1.5
    else:
        weekpay = hours * hw
        
    print("Your weekly pay is: ${0:0.2f}".format(weekpay))
    
main()
