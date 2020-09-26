# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 18:38:59 2020

@author: heart
"""


### Method 1
myList = [10, 1, 8, 3, 5]
total = 0

for i in range(len(myList)):
    total += myList[i]

print(total)

### Method 2
myList = [10, 1, 8, 3, 5]
total = 0

for i in myList:
    total += i

print(total)
