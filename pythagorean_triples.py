#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sergio Munguia 

Homework 2 Problem 1: Pythagorean Triples
"""

#Algorithm in pseudo-code
# Pythagorean Numbers, This program reads from terminal postive integer n and
# that computes and displays to the terminal all possible pythagorean triples
# (a,b,c) where 0<a,b,c<=n
#
#since a,b,c can never be true for 1^2+1^2=1^2 or 1^2+2^2=2^2
# or a = b = c we start with 1^2 + 2^2 = 3^2 and count up
#from starting to increment c for each value of b then for each value of a , up to n
#
# 1. input: positive integer n 
# 2. check if n is > 0 else print error
# 3. Perform in range loop check for variable a ranging from 1 up to n-1
# 3.1 Inside of that for loop check b in range starting with a + 1 <=so it resets| up to n 
# 3.2 Inside of that for loop check c in range starting with b + 1 <=so it resets| up to n + 1
#     With each iteration of the inner most for loop it checks a^2 + b^2 = c^2 and
#     If its True , print out the triple
#     If its not True, print nothing & inner for loop increments up to < n+1 for var c 
# 3.3 Back to middle for loop as it goes up by 1 to < n for var b 
# 3.4 Then Back to inner most loop as long as its < n
#     Checks if its True, print out the triple 
# 3.5 repeat back and forth between incrementing middle loop by 1 and then inner loop until == n
# 4. If c < n + 1 exits loop 
# 4.1 If b < n exits loop 
# 4.2 The last loop outside increments a and the process starts again. 
# 5.  print out the numbers that are correct in the inner most loop condition check


n = int(input("Enter a positive number for n : "))

if n > 0: 
    for a in range(1,n-1):
        for b in range(a+1,n):
            for c in range(b+1,n+1):
                if a**2 + b**2 == c**2:
                    print(a,b,c)
                    
else:
    print("Error : Not a Positive Number")
    import sys
    sys.exit("Invalid Input")
        
