#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sergio Munguia 

Homework 3 - Problem 2. Pythagorean Numbers Revisited

#Algorithm in pseudo-code
# Pythagorean Numbers, This program reads from terminal postive integer n and
# that computes and displays to the terminal all possible pythagorean triples
# (a,b,c) where 0<a,b,c<=n
#
#since a,b,c can never be true for 1^2+1^2=1^2 or 1^2+2^2=2^2
# or a = b = c we start with 1^2 + 2^2 = 3^2 and count up
#from starting to increment c for each value of b then for each value of a , up to n
#
# Try : & Except : exceptions have been added to the program
#
# 1. input: positive integer n 
# 2. check if n is > 0 else print error
# 3. Perform List comprehension 
# 4. Creates a List that can be printed out with all the correct triples (a,b,c) 
# 4.1 that fall through the filter, if a**2 + b**2 == c**2
# 5. Prints out List 

"""

try:
    n = int(input("Enter a positive number for n : "))
    
    if n > 0:                     
        lst = [(a,b,c) for a in range(1,n-1) for b in range(a+1, n) for c in range(b+1,n+1) if a**2 + b**2 == c**2]
        
        print(lst)
                        
    else:
        print("Error : Not a Positive Number")
        import sys
        sys.exit("Invalid Input")
except TypeError:
    print("error: Wrong Type Entered")
except ValueError:
    print("error: Wrong Value Entered")
    
