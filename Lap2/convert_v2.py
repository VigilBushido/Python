#
#   Sergio Munguia
#
#   Convert_v1.py
#
#   # 1. Calculate the temperature in Fahrenheit
#    for celcius in [0,10,20,30,40,50,60,70,80,90,100]
#    fahrenheit = (9.0/5.0) * celcius + 32
#    
#    for celcius in range(0,110,10):
#    fahrenheit = (9.0/5.0) * celcius + 32
#    celcius = (5.0/9.0) * fahrenheit -32
#
#   
#

def main():

    
    print("Celcius \tFahrenheit")
    print("------- \t---------")
    for celcius in range(0,110,10):
        fahrenheit = (9.0/5.0) * celcius + 32
        print("", celcius,"\t        ", fahrenheit,"")

main()
