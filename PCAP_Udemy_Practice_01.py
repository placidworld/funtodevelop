# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 17:39:12 2020

@author: heart
"""


### 2

list1=[("abc", "bca"),24.56,23.64,[1,2,3]]
list2 = list(list1)
list2[1]="abc"
list1[3]="bca"
print(list1)
print(list2)


### 3
s = '0123456789'
obj = range(0,len(s),0)
l = []
for i in obj:
     l.append(int(s[i]))
     
add = 0
for i in obj:
    add = add + l[i]
   
print(add)

### 4
i = ""
while i in "         ":
    print("Python", end=i)
    
### 5
print(not('False'))
print(not(0))
print(not(''))
print(not(' '))
print(not(["Python"]))
print(not([]))


### 6
print(2<<1)

print(2^2)

print(2**2)

print(2*2)

### 8
class Class_A:
  def __init__(self , var):
         return var
 
obj = Class_A(20)
print(obj)


### 9
try :
    open('sys.txt','r')
except __________ :
    print("File not found")
except :
    print("File not opened")
    

### 10
file = open('D:\\New\sys.txt', 'r')
for each in file:
    print(each)
    
file = open('D:\\New\sys.txt', 'r')
for each in file:
    print(each)
file.close()

### 13
i = 0
while i < 4: 
  print(i , end = "-") 
  i += 1.5
  if((i < 4) == False):
       break
else: 
  print(0 , end = " ")
  
  
### 14
class Calculate:
  var1=20
  def __init__(self,var1):
      self.var1 = var1
      self.var1 = self.var1 + 7
      Calculate.var1 = Calculate.var1 + 7
      
  def Print(self):
       print(Calculate.var1)
       print(self.var1)
  
Calculate(10).Print()
Calculate(15).Print()
  

### 15
print(tuple[3])
print(tuple(3))


### 16
x = 45
y = 25
 
def Sum(x):
  global x
  print("Sum inside Sum() :",x+y)
  
Sum(25) 
print("Sum outside Sum() :",x+y)

### 18
result1 = '{0}, {2} and {1}'.format('a', 'b', 'c') 
result2 = '{}, {} and {}'.format('a', 'b', 'c')
print(result1)
print(result2)

### 19
a = '😄'
b = '😉'
c = '😊' 
d = '🥰'
print(a+b+c+d)


### 20
print(1**2**2.)


### 21
print("%.2o"% (25))   
print("%.5o"% (25))

print("%.1o"% (25))   
print("%.2o"% (25))
print("%.3o"% (25))
print("%.4o"% (25))
print("%.5o"% (25))


### 22
print("% 10E"% (85792229130))

print("% 10E"% (85792229130))
print("% 20E"% (85792229130))
print("% 30E"% (85792229130))
print("% 40E"% (85792229130))
print("% 50E"% (85792229130))

print("1 : ","% E"% (1))
print("11 : ","% E"% (11))
print("111 : ","% E"% (111))
print("1111 : ","% E"% (1111))
print("11111 : ","% E"% (11111))
print("111111 : ","% E"% (111111))
print("1111111 : ","% E"% (1111111))
print("1111116 : ","% E"% (1111116))
print("11111111 : ","% E"% (11111111))
#rounding of takes place if the digit at 8th place is greater than 4
print("11111114 : ","% E"% (11111114)) 
print("11111115 : ","% E"% (11111115))   
print("11111116 : ","% E"% (11111116))        
print("111111111 : ","% E"% (111111111))
print("111111116 : ","% E"% (111111116))


### 23
### unary operators: + - ~ not

a = 20
print(+a)
print(-a)
print(~a)
print(not a)

### binary operators: += &
a = 20
b = 10
b += a 
print(b)
print(a&b)



### 24
D = {5 : 5, 15 : '15', '5' : 5, '15' : 25} 
D[str(15)] = 100
L = list(D)
L.append("Python")
print(L)



### 25
print(0x3 | 0x9)


### 26
try:
  print(30/0)
except ZeroDivisionError:
  print("Zero Division Error") 
else:
  print("Nothing went wrong") 
except:                           
  print("Something went wrong ")


### 28
i = ""
for i in "    ":
    print("Java", end=i)
    
### 30
class Class:                      #line1
  def __init__(self , var):       #line2
      self.var1 = var             #line3
      self._var1 = var            #line4
      self.__var1 = var           #line5
                                  #line6
obj=Class(20)                     #line7
print(obj.__var1)                 #line8
print(obj._var1)                  #line9
print(obj.var1)                   #line10


### 31
class A:
    def __init__(self):
        self.num1 = 10
    def show_num1(self):
        print(self.num1)
        
class B(A):
    def __init__(self):
        self.num2 = 20
    def show_num2(self):
        print(self.num2)
        
obj = B()
obj.show_num1()
obj.show_num2()   


### 32
class Parent:
  def __init__(self,age):
       self.age=age
  def get_Parent_age(self):
       return self.age
  
class Child(Parent):
   def __init__(self,age1,age2):
       self.age=age1
       super().__init__(age2)
   def get_Child_age(self):
        return self.age
  
  
son=Child(20,40)
print("Parent age :",son.get_Parent_age())
print("Child age :",son.get_Child_age())  


### 33
try:
  print("Pytho"n")
except:
  print("Error is raised")
finally:
  print("Code End")
  

### 34
str =  " , ".join(["Java" , "Python" , "Ruby"])
l = (str, " are" , " Programming" , "languages")
print(l[-5])


### 36
var = round(0.5) + round(0.6) + round(0.4) 
print(var) 

print("0.0 : ",round(0.0))
print("0.1 : ",round(0.1))
print("0.2 : ",round(0.2))
print("0.3 : ",round(0.3))
print("0.4 : ",round(0.4))
print("0.5 : ",round(0.5))
print("0.6 : ",round(0.6))
print("0.7 : ",round(0.7))
print("0.8 : ",round(0.8))
print("0.9 : ",round(0.9))


### 37
a = {2+3}*5+2**2
print(a)


### 38
class Calculate:
    A = 20
    B = 20
    def __init__(self , a ,b):
        A = a
        B= b
        print(self.A + self.B / 2  + 1)
 
Calculate(4,10) 


### 40
import math
print(math.factorial(0.6))








    




