#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 00:25:48 2017

@author: sergiomac
"""

def main():
# Processing: 1. Prompt user for the class grade percent
    while True:
        grade = eval(input("Please enter your grade percent: "))
    
        # 2. Calculate the grade
        if grade >= 90: 
            print ("nice job")
        
        # 3. Display resultig Fahrenheit
        print("Back to Top")


main()
