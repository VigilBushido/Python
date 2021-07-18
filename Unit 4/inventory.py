#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 18:41:53 2017
Midterm Exam
Sergio Munguia Question 6 
"""

def main():
    inventory = []
    current_inventory = [("snickers bar", 20, 30 , 1.5), ('Tic Tac', 18, 10, 1.0), ('Cheetos', 43, 15, 2.0)]
    tup_types = (str, int, int, float)
    for tok, i in zip( current_inventory , tup_types ):
        inventory.append(i(tok))
        
    for i in range(len(current_inventory)):
        total_sales = (current_inventory[0], current_inventory[2] * current_inventory[3])
        sales_lst = []
        sales_lst = [ (x,y).append(total_sales) for (x,y) in total_sales ]
                            
    
    #total sales amount will be #sold * sell price
    
    #sales_lst = [ (x, y) for (x, y) in inventory zip(tuple(current_inventory current_inventory[3]*current_inventory[0]))]
    
    sum_sales_lst = [ x for x in range(sales_lst) sum_sales_lst.append(sum(sales_lst[1])) ] 
    print(sum_sales_lst)
    
    
    #list comprenehnsion that returns a list wiht the total sales *
    #[(name of prodcut, total sales), ....
    
    
    