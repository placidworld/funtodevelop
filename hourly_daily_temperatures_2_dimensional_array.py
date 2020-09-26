# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 18:50:45 2020

@author: heart
"""

temps = [[0.0 for h in range(24)] for d in range(31)]

total = 0.0

for day in temps:
    total += day[11]
    
average = total / 31

print("Average temperature at noon:", average)

####################################################
temps = [[0.0 for h in range(24)] for d in range(31)]

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
    
print("The highest temperature was:", highest)


####################################################
temps = [[0.0 for h in range(24)] for d in range(31)]

hotDays = 0

for day in temps:
    if day[11] > 20.0:
        hotDays += 1
        
print(hotDays, "days were hot.")