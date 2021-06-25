#
#   Sergio Munguia
#
#   wages.py
#
#   input: hours worked & hourly wage & bonus
#
#   processing: 1. ask the user for the hours worked
#               2. ask the user for the hourly wage
#               3. weekly wage = 40 * rate_per_hour + (Hours-40) * rate_per_hour * 1.5
#               4. show the user his weekly pay
#                                                           
#   output: display weekly pay (including overtime)

while True:
    
    print("This program determines the weekly salary for an employee.")
    print("The salary is the sum of the hourly rate times the hours"\
          " worked, plus the bonus.\nFor work hours exceeding 40 per"\
          " week, an overtime rate \nof 1.5 is applied \nThe user must"\
          " indicate if the worker has received a \nbonus by answering a y/n"\
          " question \nInput Consists of: hours worked, hourly"\
          " rate, bonus \nThe output is the total salary for this"\
          " week")
        
    hours_worked = float(input("Enter the number of hours worked this week: "))
    rate_per_hour = float(input("Enter the salary rate per hour (do not include the '$' sign): "))
    yes_no = str(input("Did the worker get a bonus?(y/n): "))
    if yes_no == "y":
        bonus = float(input("Enter bonus: "))
    elif yes_no == "n":
        bonus = 0
        
    if hours_worked > 40:
        weekpay = 40 * rate_per_hour + (hours_worked - 40) * rate_per_hour * 1.5 + bonus
        overtimepay = (hours_worked - 40) * rate_per_hour * 1.5
    else:
        weekpay = hours_worked * rate_per_hour + bonus
        
    print("\nThe total salary is: ${0:0.2f}".format(weekpay),""\
          "(overtime pay is ${0:0.2f})".format(overtimepay),"\n")
