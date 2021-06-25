#
#   Sergio Munguia
#
#   Convert.py
#
#   Given a temperature in Celcius, calculates
#   and displays the corresponding temperature in
#   Fahrenheit
#
#
#   Input: Temperature in Celcius
#
#   Processing: 1. Prompt user for the temperature in Celcius
#               2. Calculate the temperature in Fahrenheit
#
#               Fahrenheit = 9/5 * Celcius + 32
#
#               3. Display resultig Fahrenheit
#
#   Output: Temperature in Fahrenheit

def main():
    # Processing: 1. Prompt user for the temperature in Celcius
    celcius = eval(input("Please enter tempeture in Celcius: "))

    # 2. Calculate the temperature in Fahrenheit
    fahrenheit = (9.0/5.0) * celcius + 32
    
    # 3. Display resultig Fahrenheit
    print("The temperature in Fahrenheit is ", fahrenheit,)


main()
