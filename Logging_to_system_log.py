# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 15:55:12 2020

@author: heart
"""


import syslog

syslog.syslog('mygeekapp: started logging')

for a in ['a', 'b', 'c']:
    b = 'mygeekapp: I found letter '+a 
    syslog.syslog(b)
    
syslog.syslog('mygeekapp: the script goes to sleep now, bye bye!')
