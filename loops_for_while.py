# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 11:14:24 2020

@author: heart
"""

# Example 1
word = "Python"
for letter in word:
    print(letter, end="*")
    
# Example 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
        
### You can use the break and continue statements to change the flow of a loop:
text = "Placidworld and Puppy Self Tutorial programs"
for letter in text:
    if letter == "p":
        break
    print(letter, end="")
    
### You can use continue to skip the current iteration, and continue with the next iteration
text = "puppyxpuppyxxx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")
    

### The while and for loops can also have an else clause in Python. The else clause executes after 
### the loop finishes execution as long as it has not been terminated by break
    
n = 0
while n != 3:
    print(n)
    n + 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")