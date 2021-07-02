#
#   Sergio Munguia
#
#   convert2.py
#
#

def main():
    celcius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celcius + 32
    print("The temperature is {0:0.2f} degrees Fahrenheit.".format(fahrenheit))


    # Print warnings for extreme temps
    if fahrenheit > 90:
        print("It's really hot out there. Be careful!")

    if fahrenheit < 30:
        print("Brrrrr. Be sure to dress warmly!")

main()
