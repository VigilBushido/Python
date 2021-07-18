#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 13:00:01 2017

@author: sergiomac
"""
class Vehicle(object):
    def __init__(self):
        self.speed = 0
    def accelerate(self,dv):
        self.speed += dv
    def brake(self, dv):
        self.speed -= dv
        
class Car(Vehicle):
    def __init__(self, wheels):
        Vehicle.__init__(self)
        self.wheels = wheels
        
c = Car(4)
c.accelerate(1)
print(c.speed)