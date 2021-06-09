#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 03:49:21 2017

student_tup = input_tuple(“Enter  rst name, last name, age ( oat), ID (int), fulltime (bool): “,
(str, str,  oat, int, bool), # this is the tuple with expected types
“,”) # , is the separator character on the input line


#Read From File a Tuple

"""

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
        print(len(filecontents)," Cars read from .csv file")
        for f in filecontents:
            make, model, mpg_float, modelYr_int, newcar_bool = \
            read_tuple(f, (str, str, float, int, bool), ",")
            
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
    
