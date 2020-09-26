# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 09:38:21 2020

@author: heart
"""

### check lottery
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1
        
print(hits)