#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 18:15:51 2017

@author: sergiomac
"""

def count_letters(filename):
    try:
        count_dct = {}
        f = open(filename, "r")
        for line in f.read():
            for char in line:
                if char.isalphabetic():
                    count_dct[char] = count_dct[char]+1
        f.close()

        
    except IOError:
        print("Read error.")
        f.close()
        return{}
        
    return count_dct

count_dct = count_letters("gettysburg.txt")
charfreq_lst = sorted([(f,c) for (f,c) in count_dct.items()])
print(charfreq_lst)