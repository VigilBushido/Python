#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 05:00:08 2017

@author: sergiomac
"""

# COP4930 Python Programming
# 
# Algorithm for searching the first occurance of a substring in a string 
#  (same as the Python string find method)
# It returns the index in the string where the substring starts
# if present, or -1, if not.
# E.g.
#   s ="0123456789"
#   ss = "45"
# search for ss in s returns 4
# search for a substring that does not exist returns -1 

# (pseudo-code uses indentation to mark compound statements, like in Python)
# time complexity T(s,ss) = O(length(s) * length(ss))
#
# function search(s,ss)
# 1.  i = 0
# 2.  found = -1   # not found yet
# 3.  if length(ss) > length(s) return -1
# 4.  while i < length(s) - length(ss) and found==-1
# 5.      j = 0   # to iterate through the substring's chars
# 6.      while j<length(ss) and s[i+j]==ss[j]
# 7.           j = j+1
# 8.      if j == length(ss)
# 9.            found = i
# 10.     i = i + 1
# 11. return found


def search(s,ss):
    """Searches for a substring ss in a string s."""
    
    i = 0
    found = -1
    if len(ss) <= len(s):  
        while i < len(s) - len(ss) and found == -1:
            j = 0
            while j < len(ss) and s[i+j] == ss[j]:
                j = j + 1
            if j == len(ss):
                found = i
            i = i + 1
            
    return found


def testif(b, testname, msgOK="", msgFailed=""):
    if b:
        print("Success: "+ testname + "; " + msgOK)
    else:
        print("Failed: "+ testname + "; " + msgFailed)
    return b
#"""Function used for testing. 
#param b: boolean, normally a tested condition: true if test passed, false otherwise
#param testname: the test name
#param msgOK: string to be printed if param b==True  ( test condition true)
#param msgFailed: string to be printed if param b==False
#returns b
#"""
    


# testing:
s ="0123456789"
ss1 = "45"
ss2 = "49"

# simplify testing by using a testing function and the find method
testif(search(s,ss1) == s.find(ss1), "test 1")

testif(search(s,ss2) == s.find(ss2), "test 2")

testif(search(s,s+ss1) == s.find(s+ss1), "test 3")

testif(search("", "abc") == -1, "test 4 - search in ''")

testif(search("", "") == -1, "test 5 - search for '' in ''")

testif(search("abcd", "") == 0, "test 6 - search for '' in nonempty string")