#futval.py
#
#

def main():
    I= eval(input("What is the annualized interest rate as a decimal?: "))
    apr = I / 100
    i=0
    z=1
    while z < 2:
        i=i+1
        z = z * (1 + apr)
    if z >= 2:
        print (i)
main()
