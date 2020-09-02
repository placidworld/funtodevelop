# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:32:54 2020

@author: heart
"""

# Sending email
#smtplib.SMTP([host[,port]])

import smtplib

# Use your own to and from email address
fromaddr = 'xxxx@gmail.com'
toaddrs = 'xxx@gmail.com'

msg = "This is an message sent out through Pythong programming"

# credentials
# Use your own Google Mail credentials while running the program
username = 'xxx@gmail.com'
password = 'xxxx'

# The actual email send
server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()
server.login(username, password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()