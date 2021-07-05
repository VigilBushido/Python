#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 3: Function Visualization

Displays a function entered using the math module with a variable x
Graphs it visually using pylab
"""

import pylab
import math

#fun_str = "2 * math.sin(2*math.pi * x)"
fun_str = input("Enter function with variable x: ")
ns = int(input("Enter number of samples: "))
xmin = float(input("Enter xmin: "))
xmax = float(input("Enter xmax: "))

# print table header:
print("{:>10}{:>10}".format("x", "y"))
print("-" * 20)      

xs = []
ys = []
dx = (xmax - xmin) / (ns - 1)

i = 0
for i in range(0, ns):
    x = xmin + i * dx
    xs.append(x)
    y = eval(fun_str)
    ys.append(y)

    print("{0:>+10.4f}{1:>+10.4f}".format(x, y))

pylab.plot(xs, ys, "bo-")
pylab.xlabel('x')
pylab.ylabel("y")
pylab.title(fun_str)
pylab.show()