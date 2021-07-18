#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 18:18:18 2017

@author: sergiomac
"""

class Bag(object):
    
    def __init__(self, sequence):
        self.elements = []
        for el in sequence:
            self.elements.append(el)
            print('Added {}'.format(el))
    
    
    def __setitem__(self, index, el):
        self.elements[index] = el
        print("added {}".format(el))
        
bag = Bag(range(0,10))
bag[3] = 33

