# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 11:25:54 2020

@author: heart
"""

"""
The range() function generates a sequence of numbers. It accpets integers and returns range objects.
The synax of range() looks follows:
range(start, stop, step)

where:
    start is an optional parameter specifying the starting number of the sequence (0 by default)
    stop is an optional parameter specifying the end of the sequence(it is not included)
    step is an optional parameter specifying the difference between the numbers in the sequence (1 by default)

"""

for i in range(3):
    print(i, end = "")
    
for i in range(6, 1, -2):
    print(i, end="")
    

# create a for loop that counts from 0 to 10, and prints odd numbers to the screen
for i in range(1, 11):
    if i % 2 != 0:
        print(i)
        
# create a while loop that counts from 0 to 10, and prints odd numbers to the screen
x = 1
while x < 11:
    if x % 2 != 0:
        print(x)        
    x += 1
    
# create a program with a for loop and a break statement. The program should iterate over characters in 
# an email address, exit the loop when it reaches @ symbol, and print the part before  @ on one line. 
for ch in "john.smith@jhu.edu":
    if ch == "@":
        break
    print(ch, end="")
    
# create a program with a for loop and a continue statement. The program should iterate over a string of 
# digits, replace each 0 with x, and print the modified string to the screen
    
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, e nd="")


### 
n = 3
while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)
    
###
n = range(4)

for num in n:
    print(num - 1)
else:
    print(num)
    
###
for i in range(0, 6, 3):
    print(i)
    
    
    