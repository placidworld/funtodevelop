# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 17:04:31 2020

@author: heart
"""

import os

### Remove the file "test.txt"
os.remove('test.txt')

# Check if File exist
import os

if os.path.exists("test.txt"):
    os.remove("test.txt")
else:
    print("The file does not exist")
    
### Delete folder
### You can only remove empty folders
import os
os.rmdir("myfolder")
