#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sergio Munguia 

Homework Problem 2: Duplicated Sub-strings
"""

#Finds the duplicated sub string first occurrence, then returns it. 
#input: asks the user to enter in a string 
#input: asks the user to enter in a length of sub-string to find duplicated
#
#1. it calls find_dup_str( string, length )  
#1.1 for index 0 up to size of string - length + 1   
#1.2 iterates through string checking index+n size sub-strings against rest_of_string  
#1.3 subsize_string length of n (starts at index and ends before length )  
#1.4 rest_of_string is string from index+length to end (minus subsize_string)  
#1.5 if rest_of_string can't find a dup subsize_string in it & length of rest_of_string is not 0  
#    increase index and repeat process (moving subsize_string along the whole rest_of_string)  
#1.6 if there is no subsize_string length of n found duplicated then return the empty string ""  
#2. it calls find_max_dup( string )  
#2.1 Check if size of string is greater than 1   
#2.2 search from i to length of string i , as the sizes of sub-string increase  
#2.3 find the duplicated string not empty "" string  
#    2.3.1 save the longest_dup_string as the subsize_string returned from find_dup_str()  
#    2.3.2 as i increases, saving the longest subsize_string & return it to user  
#2.4 else return its max string is the empty string  
#3. Print to screen the 1st occurrence of a duplicated sub-string & the max length sub-string 




def find_dup_str(s, n):
    #for index up to size of string - length + 1 
    #iterates through string checking index+n size sub-strings against rest_of_string 
    for index in range(len(s)-n+1):
        #subsize_string length of n (starts at index and ends before length )
        subsize_string = s[index:index+n]
        #rest_of_string is string from index+length to end (minus subsize_string)
        rest_of_string = s[index+n:]
        #if rest_of_string can't find a dup subsize_string in it & length of rest_of_string is not 0 
        #increase index and repeat process (moving subsize_string along the whole rest_of_string)
        if rest_of_string.find(subsize_string) != -1 and len(rest_of_string) != 0:
            return subsize_string
    #if there is no subsize_string length of n found duplicated then return the empty string ""
    return ""
    
def find_max_dup(s):
    longest_dup_string = ""
    #check if size of string is greater than 1 
    if len(s) > 1:
        # search from i to length of string i , as the sizes of sub-string increase
        for i in range(len(s)):
            #find the duplicated string not empty "" string
            if find_dup_str(s, i) != "":
                #save the longest_dup_string as the subsize_string returned
                longest_dup_string = find_dup_str(s, i)
        return longest_dup_string
    #else return its max string is the empty string
    else:
        return ""

original_str = input("Enter in a string: ")
sub_str_length = int(input("Enter in a length of substring: "))

print("Duplicated Sub-String: " + find_dup_str(original_str, sub_str_length))
print("Max Duplicated Sub-String: " + find_max_dup(original_str))

    
