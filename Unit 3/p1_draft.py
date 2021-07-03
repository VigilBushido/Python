#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 05:52:39 2017

@author: sergiomac
"""

#Algorithm in pseudo-code
# Pythagorean Numbers, This program reads from terminal postive integer n and
# that computes and displays to the terminal all possible pythagorean triples
# (a,b,c) where 0<a,b,c<=n
# 1. input: positive integer n 
# 2. check if n is > 0 else print error
# 3. Perform in range loop check for variable a ranging from 1 to n-1
# 4. Inside of that for loop check b in range starting with a + 1 (so it resets) to n 
# 5. Inside of that for loop check c in range starting with b + 1 (so it resets) to n + 1
# 6. With each iteration of the inner most for loop it checks a^2 + b^2 = c^2 and
# 7. If its True , print out the triple
# 8. If its not True, print nothing & inner for loop increments up to < n+1 for var c 
# 9. Back to middle for loop as it goes up by 1 to < n for var b 
# 10. Back to inner most loop as long as its < n
# 11. Checks if its True, print out the triple 
# 12. If c < n +1 exits loop 
# 13. If b < n exits loop 
# 14. The last loop increments a and the process starts again. 
# 15.  print out the numbers that are correct in the inner most loop condition check
while True:
    n = int(input("Enter a positive number for n : "))
    
    if n > 0: 
        for a in range(1,n-1):
            print(a,"a in outermost")
            for b in range(a+1,n):
                print(b,"b in middle")
                for c in range(b+1,n+1):
                    print(c,"c in inner")
                    print("a = ",a,"b = ",b,"c = ",c)
                    if a**2 + b**2 == c**2:
                        print(a,b,c," Bingo a Triple!!!!")
                        
    else:
        print("Error : Not a Positive Number")
        
