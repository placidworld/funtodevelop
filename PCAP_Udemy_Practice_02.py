# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 17:39:12 2020

@author: heart
"""
### 1
class Car:
    def __init__(self,x,y):
        self.name = x
        self.price = y
        
obj1 = Car('Audi',2000)
obj2 = Car('Audi',2000)
print(obj1 == obj2)



### 2
var1 = '5555'
var2 = '56'
print(var2>var1)
 
var1 = '5555'
var2 = '55'
print(var2>var1)
 
var1 = '5555'
var2 = '54'
print(var2>var1)

v0 = ord('0')
v1 = ord('1')
v2 = ord('2')
v3 = ord('3')
v4 = ord('4')
v5 = ord('5')
v6 = ord('6')
v7 = ord('7')
v8 = ord('8')
v9 = ord('9')

print(v0, v1, v2, v3, v4, v5, v6, v7, v8, v9)



### 3
for i in range(5):
     pass
print(i)


### 4
L = [1.5 ,'Python',False] 
T = (1.2, 'Java', 'True') 
for i in range(len(L)): 
  if L[i]: 
     L[i] = L[i] + T[i] 
  else: 
     T[i] = L[i] + T[i] 
 
print(L) 


    
### 5


### 6
print(None + None)


### 7
class Animal:
  price=500
  def __init__(self, x):
       self.breed = x
  def name_me(self,y):
       self.name = y
             

### 8
print(float('25.65'))
print(int('25.65'))


### 9
import copy
L = ['A', 'B', 'C']
list1 = [10, 20, 30, L]
list2 = list1.copy()
list2 = [10, 20, 30, L]
list3 = copy.deepcopy(list1)

L[1] = 0000
print(list1)

list1[1] = 0000
print(list1)

print(list1) 
print(list2)
print(list3)

    

### 10
i = 0
for i in range(0,4):
  print(i , end = " ")
  i = i + 1
else:
  print("Python")


### 11
class Vehicle :
  def __init__(self):
          print('Brand:','Ford')
Vehicle()



### 12
class Pet :
     def call_me(name):
         print("Bella")
         
obj.call_me()
Pet.call_me("Bella")



### 13
try:
  print(Hello) 
except NameError:
  print("Something went wrong")
except NameError:
  print("Everything went wrong")
finally:
  print("End of Code")

  
  
### 14
### Dictionary & set cannot be concanatenated.
print({1,2,3,4}+{2,3,4,4}) 
  

### 15
L = [lambda x: x +8  ,lambda y: y + 9,lambda z: z + 3]
for i in range(0,len(L)):
       print(L[i])


### 16
print({a+1 for a in range(4)})
print([a+1 for a in range(4),1 , 2 ,3 ,4 ,6 , 8])

"""
rb+:- Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.

wb+:-Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

wb:- Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

b:- mode does not exist
"""

### 17
print(None == None)
print(None != None)
print(None >= None)
print(None > None)

### 18



### 19
result = dict()
result[(1,2,3)] = 34
result[(2,3,1)] = 40
result[(3,1,2)] = 13

print(result)

l = [(1,2,3),(2,3,1),(3,1,2)]
summ = 0
for i in l:
    summ = summ + result[i]
 
print(summ)



### 20
tuple1 = (4, 3, 7, 9) 
tuple2 = (4, 3, 3, 10) 
print(tuple1 > tuple2)


### 21
l = list('abcdef')
a , b , c , l[0],l[1],l[2] =  l[0],l[1],l[2] , l[-1],l[-2],l[-3]
print(l)

l[3],l[4],l[5] = c , b, a 
print(l)



### 22
def say(p ,q=42,r=5 , s=28):
  print(' p :',p,' q :',q,' r :',r,' s :',s)
say(48,(45,39),s=30)


### 23
def show(x):
    print(x)
    return 0
print(show(1)&show(2)+show(3)*show(4)**show(5))



### 24
print({1.00,1.0,1,3,3.0,3.00})



### 25
if((0.1+0.2)==(0.3)):
  print("if")
elif((0.3 + 0.4) == (0.7)):
  print("elif")
else:
  print("else")

print((0.3+0.4)==0.7)

### 26
"""
ord() is used to convert a character to a UNICODE Code point.

chr() is used to convert a UNICODE Code point to a character.
"""
T = ('a','b','c','d')
L = range(0,5)
for i in L:
    print(_______,end=" ")
    if i >= 3:
        break
    
    
### 27
set1=(1 , 2 , 4)
set2={2 , 4 , 5}
set3=set()
for i in set1:
  for j in set2:
     i=i+1
     set3.add(i)
     set3.add(j)
 
for i in range(0,len(set3)) :   
       print(set3[i] , end = "")




### 28
s = 'pyhtonPYTOHN'
s.capitalize()
print(s)
print(s[0])
print(s.lower())
print(s.upper())

for i in range(0,len(s)):
    if(i%2.0 == 0 ):
        s[i].lower()
        print(s)
    else :
        s[i].upper()
        print(s)
print(s)

    
### 30
class A :
    def x(self,a):
        print("In A")
        
class B(A) :
    def __init__(self):
        self.x(2)
    def __________:
        print("In B")
B()


### 31
class Bike:
    def __init__(self):
        self.__Company_name = "BMW"
        self.price = 2000
    def details(self):
        print('Name : ',self.__Company_name,'Price : ',self.price)
 
class Car(Bike):
    def __init__(self):
        super().__init__()
        self.__Company_name = "Audi"
        self.price = 4000

obj = Car()
obj.details()



### 32
details = {['Audi','BMW'] : ['Price : 2000' , 'Year : 1958']}
details = dict()
details[{'Audi','BMW'}] = {'Price : 2000' , 'Year : 1958'}
details = dict()
details[{'Audi':1,'BMW':2}] = {'Price' : 2000 , 'Year' : 1958}

### 33
list1=[24, 27, 34, 89,48]
list2 = list1
list2[1]= "LIST_2"
list1[3]= "list_1"
print(list1)
print(list2)
  

### 34
s = {1,1,2,4,5,7,8}
var = list(x//1.0 for x in s if x in s and x%2==0) 
print(var)


### 35
my_str = "pythonprogramming"
my_str.sort()
print(my_str.index('p'))


### 36
def Reverse(x):
    x.reverse()
    return x
 
def check_sorted(x):
    return x.sorted()
 
l = list('9876543210')
print("Status : ",check_sorted(Reverse(l)))




### 37


### 38

### 40
import math
print(math.factorial(0.6))



import math  
print(math.factorial('5'))




    




