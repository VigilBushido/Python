#
#   Sergio Munguia
#
#   bmi.py
#
#   input: weight(in pounds) & height(in inches)
#
#   processing: 1. ask the user for weight(lbs)
#               2. ask the user for height(inches)
#               3. calculate the BMI using formula (lbs) * 720 / (inches)^2
#               4. display the BMI
#               5. display either above, within, or below healthy range
#
#   output: display the user's BMI and Health
#
#

def main():
    print("Body Mass Index Caclulator")
    print()

    lbs = eval(input("Enter your weight (in pounds): "))
    inches = eval(input("Enter your weight (in inches): "))
        
    bmi = lbs * 720 / inches ** 2

    print("Your BMI is {0:0.4f}".format(bmi))

    if 19 <= bmi <= 25:
        print("That's in the healthy range.")
    elif 0 < bmi < 19:
        print("That's below the healthy range.")
    elif bmi > 25:
        print("That's above the healthy range.")
    else:
        print("That's not valid")

    

main()
