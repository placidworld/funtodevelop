# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 09:57:56 2020

@author: heart
"""

### German Mathematician Lothar Collatz formulated an intriguing hypothesis(it still remains unproved)

### input any integers
c0 = int(input("Please enter any integer: "))
counter = 0

while c0 > 0:
    if c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 / 2
        else:
            c0 = 3 * c0 + 1
        print(int(c0))
    counter += 1

print(counter) 