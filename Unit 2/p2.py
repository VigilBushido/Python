#
#   Sergio Munguia
#   
#
#   p2.py
#
#   A program that computes the real roots of a quadratic equation.
#

import pylab
import math # makes the math library available


while True:
    print("This program finds the real solutions to a quadratic")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    
    discriminant = b * b - 4 * a * c
    
    if discriminant < 0:
        print("\nno real solutions")
    else:
        discRoot = math.sqrt(discriminant)
        root2 = (-b + discRoot) / (2 * a)
        root1 = (-b - discRoot) / (2 * a)
        
        if root1 == root2:
            print("\none solution: ", root1)
        else:
            print("\ntwo solutions: x1=", root1,",x2=", root2)

    if discriminant >= 0:
        xs = []
        ys = []
        # prepare the domain for the function we graph
        x0 = -5.0    # lower bound
        x1 = +5.0    # upper bound
        
        n = 100                     # n points
        dx = (x1 - x0) / n          # delta between points
        
        x = x0
        while x <= x1:
            xs.append(x)
        
            # edit this function
            y = a* x**2 + b*x + c
            ys.append(y)
            x += dx
        
        # after the loop:
        pylab.plot(xs, ys, "bo-")    # creates the graph figure, but does not show it yet
        pylab.show()     # what it says...





