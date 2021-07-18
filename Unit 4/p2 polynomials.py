#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 2 - Polynomials


Sergio Munguia 
"""

import numpy as np
from collections import Counter
import numpy.polynomial.polyutils as pu

class Poly(object):
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2
        pass
    
    def __str__(self, conversion): 
            pass
    
    def __repr__(self):
        print()
        pass
    
    def __getitem__(self):
        pass
    
    def __add__(self, p, q):
        r = Counter()

        for coeff, exp in (p + q):
            r[exp] += coeff
            
        def counter_to_poly(c):
            p = [(coeff, exp) for exp, coeff in c.items() if coeff != 0]
            # sort by exponents in descending order
            p.sort(key = lambda pair: pair[1], reverse = True)
            return p

        return counter_to_poly(r)
            
    def __mul__ (self, c1, c2):
        # c1, c2 are trimmed copies
        [c1, c2] = pu.as_series([c1, c2])
        ret = np.convolve(c1, c2)
        return pu.trimseq(ret)
        
    def __rmul__(self):
        pass
        
    def __eq__(self):
        pass
        
    def __ne__(self):
        pass
    
    
def main():
    x = Poly([(4,3),(3,0)], [(-4,3),(2,1)])
    x.__add__
    print(x)
    
main()
    
    
        
    
        
    
        
        
