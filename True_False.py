# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 20:14:23 2020

@author: heart
"""

### binary
x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print(not(z))

###
x = 4
y = 1

a = x & y  # unless both are the same, value should be 1, otherwise 0
b = x | y 
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)