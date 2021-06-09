#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 03:49:21 2017

student_tup = input_tuple(“Enter  rst name, last name, age ( oat), ID (int), fulltime (bool): “,
(str, str,  oat, int, bool), # this is the tuple with expected types
“,”) # , is the separator character on the input line

"""

def input_tuple_lc(student_tup):
    #that reads from the terminal a sequence of objects with types provided
    #by a tuple given as parameter and 
    #that returns the sequence of objects read as a tuple.
    sequence = []
    try: 
        tup_of_types = (str, str, float, int, bool)
        #implemented using list comprehension
        sequence = [(i(tok)) for tok,i in zip( student_tup , tup_of_types)]
        sequence = tuple(sequence)
        return sequence
    
    except TypeError:
        print("error: parse error (Wrong Type Entered in Sequence)")
        sequence = ()
        return sequence
    except ValueError:
        print("error: parse error (ValueError)")
        sequence = ()
        return sequence

def main2():
    student_str = (input("Enter first name, last name, age(float), ID (int), fulltime(bool): ")) 
    student_tup = tuple(student_str.split(','))
    if len(student_tup) != 5:
        print("ValueError(Incorrect amount of Values entered)")
        student_tup = ()
        main2()
    else:
        converted = input_tuple_lc(student_tup)
        if converted != ():
            print("student tuple parsed:")
            for i in range(len(converted)):
                print(type(converted[i]), converted[i], end = " ")
        else: print("Fail, Sequence is the Empty Tuple:",converted)       

main2()
    
