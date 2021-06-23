#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 01:06:24 2017

@author: sergiomac
"""


list = []
list.append(3)
print(list)

print(list[0])
list[0] = "m"
print(list[0])

list2 = [3, "k", "a word", -5, [1,2]]
if list2.index(-5):
    print(list2.index(-5))
    x = list2.index(-5)
# Comment
    print(x)
    list2[list2.index(-5)] = "Hokey"
    print(list2[list2.index("Hokey")])

day = 22
month = "June"
str = "Today is " + month + " " + str(day)
print(str)

str2 = "é."
print(str2[0])

