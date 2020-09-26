# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 08:32:41 2020

@author: heart
"""


### Issue
myList = [8, 10, 6, 2, 4]

for i in range(len(myList) - 1):
    if myList[i] > myList[i + 1]:
        myList[i], myList[i + 1] = myList[i + 1], myList[i]
#        continue

print(myList)

#######################################################
### Solution
myList = [8, 10, 6, 2, 4]
# it's a litte fake, we need it to enter the while loop
swapped = True

while swapped:
    # no swaps so far
    swapped = False
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            # swap occured
            swapped = True
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print(myList)

### Quick solution with .sort method
myList = [8, 10, 6, 2, 4]
myList.sort()
print(myList)

### Using fun to sort
myList = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    myList.append(val)

while swapped:
    swapped = False
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True
            myList[i], myList[i + 1] = myList[i + 1], myList[i]
            
print("\nSprted:")
print(myList)