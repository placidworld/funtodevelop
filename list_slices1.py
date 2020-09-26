# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 18:15:16 2020

@author: heart
"""

### Check list copy and delete

### results is "C"
l1 = ["A", "B", "C"]
l2 = l1
l3 = l2

del l1[0]
del l2[0]

print(l3)

### ["B", "C"]
l1 = ["A", "B", "C"]
l2 = l1
l3 = l2

del l1[0]
del l2

print(l3)


### []
l1 = ["A", "B", "C"]
l2 = l1
l3 = l2

del l1[0]
del l2[:]

print(l3)

### ["B", "C"]
l1 = ["A", "B", "C"]
l2 = l1[:]
l3 = l2[:]

del l1[0]
del l2[0]

print(l3)

#################
myList = [1, 2, "in", True, "ABC"]

print(1 in myList)
print("A" not in myList)
print(3 not in myList)
print(False in myList)
