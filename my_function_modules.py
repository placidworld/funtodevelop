# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 11:36:53 2020

@author: heart
"""

# file my_function.py
def minmax(a, b):
    if a <= b:
        min, max = a, b
    else:
        min, max = b, a
    return min, max

# Module usage from other programs use below
import my_function 
