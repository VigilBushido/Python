#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 02:02:15 2017

@author: sergiomac
"""

import math
def main():
    radius_str = input("Enter the radius of your circle: ")
    radius_int = int(radius_str)
    
    circumference = 2 * math.pi * radius_int
    area = math.pi * (radius_int ** 2)
    
    print ("The Circumference is:", circumference, \
       ", and the area is: ", area)

main()