# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 11:36:53 2020

@author: heart
"""
class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print("Hello, my name is", self.name)
p = Person("Kunal")
p.sayHi()
