#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 18:53:42 2017

Sergio Munguia 
"""


class SortedBag(object):
    bag_collection = []
    
    def __init__(self, bag_collection, element):
        self.bag_collection = bag_collection
        self.element = element
        
    def insert(self, element, bag_collection):
        for element in bag_collection:
            self.elements.append(element)
            print('Added {}'.format(element))
            
    def remove(self, element, bag_collection):
        for element in bag_collection:
            self.elements.pop(element)
            print('Removed {}'.format(element))
    
    def __add__(self):
        self.new_bag_collection += self.bag_collection
        return self.new_bag_collection

    def __str__(self, bag_collection):
        self.bag_collection = str(sorted([(x) for (x) in bag_collection.items()]))
        print("This is the bag collection contents:", self.bag_collection)
        
    def __repr__(self):
        return self.__str__()

        
SortedBag()