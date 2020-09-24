# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:05:51 2020

@author: heart
"""

### Build a pyramid 

blocks = int(input("Enter the number of blocks: "))

i = 1
height = 0

while blocks >= i: # Given that blocks is at least 1
    blocks -= i
    height += 1
    i += 1
    
print("The height of the pyramid: ", height)