# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 17:54:10 2020

@author: heart
"""

### remove duplicates from a list
myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 2, 9]
newList = []

for number in myList:
    if number not in newList:
        newList.append(number)

myList = newList[:]
print("The list with unique elements only:")
print(myList)   

### remove duplicates from a list
myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 2, 9]
newList = []

for number in myList:
    if number in newList:
        continue
    else:
        newList.append(number)

myList = newList[:]
print("The list with unique elements only:")
print(myList) 