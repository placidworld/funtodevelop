# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 09:38:10 2020

@author: heart
"""

### Approach 1
### Define function to demonstrate printing pattern
def pyparttern(n):
    
    # outer loop to handle number of rows
    # n in this case
    for i in range (0, n):
        
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
            
            # printing stars
            print("*", end="")
        
        # ending line after each row
        print("\r")
        
        # driver code
        n = 5
        pyparttern(n)
        

### Approach 2
def pypart(n):
    myList = []
    
    for i in range(1, n+1):
        myList.append("*"*i)
    print("\n".join(myList))
    
# Driver Code
n = 5
pypart(n)