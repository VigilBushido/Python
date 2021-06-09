#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sergio Munguia 

Homework 3 - Problem 1: Tuple Input

student_tup = input_tuple(“Enter  rst name, last name, age ( oat), ID (int), fulltime (bool): “,
(str, str,  oat, int, bool), # this is the tuple with expected types
“,”) # , is the separator character on the input line

a.) main() reads input from the user and then calls input_tuple to parse the values
    into a new tuple returned with the value newly assigned value types
    
b.) main2() input from the user and then calls input_tuple_lc to parse the values
    - using list comprehension
    into a new tuple returned with the value newly assigned value types
    
c.) main3() reads a .csv file , currently full with 2 lines of data in my example cars.csv file
    it then calls function read_tuple to assign the values into 5 variables that are returned
    and printed. ends when the all the lines of a file are read. 
    displays to the user to verify everything is correct. for the file specifics & errors
    
Exceptions are applied to all functions as deemed proper, as they have been tested individually
in privately organized  p1.py , p1_lc.py, and p1_rf.py files before being combined into here
"""

def input_tuple(student_tup):
    #that reads from the terminal a sequence of objects with types provided
    #by a tuple given as parameter and 
    #that returns the sequence of objects read as a tuple.
    try: 
        sequence = []
        tup_of_types = (str, str, float, int, bool)
        for tok, i in zip( student_tup , tup_of_types ):
            sequence.append(i(tok))
        sequence = tuple(sequence)
        return sequence
    except TypeError:
        print("error: parse error (Wrong Type Entered in Sequence)")
        sequence = ()
        return sequence
    except ValueError:
        print("error: parse error (ValueError): ", tok)
        sequence = ()
        return sequence
    
def main():
    student_str = (input("Enter first name, last name, age(float), ID (int), fulltime(bool): ")) 
    student_tup = tuple(student_str.split(','))
    if len(student_tup) != 5:
        print("ValueError(Incorrect amount of Values entered)")
        student_tup = ()
        main()
    else:
        converted = input_tuple(student_tup)
        if converted != ():
            print("student tuple parsed:")
            print(converted)
            for i in range(len(converted)):
                print(type(converted[i]), converted[i], end = " ")
        else: print("Fail, Sequence is the Empty Tuple:",converted)       

main()

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
            print(converted)
            for i in range(len(converted)):
                print(type(converted[i]), converted[i], end = " ")
        else: print("Fail, Sequence is the Empty Tuple:",converted)       

main2()

def read_tuple(f, tup_types, sep):
    #that reads from the terminal a sequence of objects with types provided
    #by a tuple given as parameter and 
    #that returns the sequence of objects read as a tuple.
    try: 
        car = f
        car = car.strip('\n').strip('\ufeff').split(sep)
#       print(car)
        parsed_car_tup = [(i(tok)) for tok,i in zip( car , tup_types)]
        make, model, mpg_float, modelYr_int, newcar_bool = tuple(parsed_car_tup)
        return make, model, mpg_float, modelYr_int, newcar_bool
    except TypeError:
        print("error: parse error (Wrong Type)")
        sequence = ()
        return sequence
    except ValueError:
        print("error: parse error (ValueError)")
        sequence = ()
        return sequence
    
    
def main3():
    try:
        file = None # in case open fails
        file = open("cars.csv", "r")
        filecontents = file.readlines()
        print('\n',len(filecontents)," Cars read from .csv file")
        for f in filecontents:
            make, model, mpg_float, modelYr_int, newcar_bool = \
            read_tuple(f, (str, str, float, int, bool), ",")
            #function call
            converted = (make, model, mpg_float, modelYr_int, newcar_bool)
            if converted != ():
                print("\n- car tuple parsed:")
                print(converted)
                for i in range(len(converted)):
                    print(type(converted[i]), converted[i], end = " ")
            else: print("Fail, Sequence is the Empty Tuple:",converted)  

    except FileNotFoundError:
        print("error: file not found")
        import sys
        return sys.exit('Error: Exiting Program')
    except PermissionError:
        print("error: no permission to open file")
        import sys
        return sys.exit('Error: Exiting Program')
    finally:
        print("\nWe are done here , closing the file")
        if file:
            file.close()
        
main3()

        
        

