# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 11:25:54 2020

@author: heart
"""

"""
The range() function generates a sequence of numbers. It accpets integers and returns range objects.
The synax of range() looks follows:
range(start, stop, step)

where:
    start is an optional parameter specifying the starting number of the sequence (0 by default)
    stop is an optional parameter specifying the end of the sequence(it is not included)
    step is an optional parameter specifying the difference between the numbers in the sequence (1 by default)

"""

for i in range(3):
    print(i, end = "")
    
for i in range(6, 1, -2):
    print(i, end="")