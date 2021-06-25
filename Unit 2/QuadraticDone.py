# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#
#   Sergio Munguia
#
#   quadratic.py
#
#   A program that computes the real roots of a quadratic equation.
#   Not: this program crashes if the equation has no real roots.

import pylab
import math # makes the math library available


while True:
    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
    print("This program finds the real solutions to a quadratic\n")

    if b == 0:
        print("\nThere are no real solutions")
    else:
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        
        if root1 == root2:
            print("\nThe one solution is:", root1)
        else:
            print("\nThe two solutions are:", root1,",", root2)

    if b != 0:
        xs = []
        ys = []
        # prepare the domain for the function we graph
        x0 = -4.0    # lower bound
        x1 = +4.0    # upper bound
        
        n = 50                     # n points
        dx = (x1 - x0) / n          # delta between points
        
        
        x = x0
        while x <= x1:
            xs.append(x)
        
            # edit this function
            y = a* x**2 + b*x + c
            ys.append(y)
            x += dx
        
        # after the loop:
        pylab.plot(xs, ys, "ro-")    # creates the graph figure, but does not show it yet
        
        pylab.show()     # what it says...





