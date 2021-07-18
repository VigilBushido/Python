#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 18:23:30 2017

@author: sergiomac
"""

class Student(object):

    lastID = 0 
    
    def make_id():
        Student.lastID +=1
        return Student.lastID
    
    def __init__(self,name):
        self.name = name
        self.id = Student.make_id()
        
    def print(self):
        print("student(id = {}, name = {}".format(self.id,self.name))
        

print(Student("Sergio"))
