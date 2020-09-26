# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 09:17:48 2020

@author: heart
"""

### inner life of lists
list1 = [1]
list2 = list1
list1[0] = 2
print(list2)

######################
# unlike the aboe, list2 = list1, the list2 = list1[:] is able to produce a brand new list
### myList[start:end]
list1 = [1]
list2 = list1[:]
list1[0] = 2
print(list2)

########################
myList = [10, 8, 6, 4, 2]
newList = myList[1:3]
print(newList)