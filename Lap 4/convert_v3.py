#
#   Sergio Munguia
#
#   convert_v3.py    
#
#   
#   processing: 1. print the index's & .format specifiy the strings
#               2. repeat the "-" using the repetition string operation *
#               3. for loop the celcius in range(0,110,10)
#               4. print the index's & .format specifiy the variables & space string
#
#   output: Displays the Fahrenheit degree based on Celcius (0-100)


def main():
    
    print("{0:^20} {1} {2:^20}".format("Celcius", " " , "Fahrenheit")) 
    print("=" * 41)
    for celcius in range(0,110,10):
        fahrenheit = (9.0/5.0) * celcius + 32
        fahrenheit = int(fahrenheit)
        print("{0:^20} {1} {2:^20}".format(celcius, " " , fahrenheit))

main()
