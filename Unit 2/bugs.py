#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 00:22:06 2017

@author: sergiomac
"""

def main():

    print("Please enter bugs collected on ...")

    total = 0
    for i in range(7):
         
         print("\t Day", i+1, end=' : ')
         bugs = eval(input())
         total = total + bugs
    print("\n The total number of bugs collected is: ", total,"")


main()
