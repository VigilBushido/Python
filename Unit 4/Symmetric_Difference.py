#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 18:32:49 2017

@author: sergiomac
"""

a_set = {4,1,3,6,4}

b_set = set([3,5,1,0,6])

if a_set.symmetric_difference(b_set) == {4,0,5}:
    print("YES")