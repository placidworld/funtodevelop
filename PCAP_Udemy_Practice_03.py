# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 17:20:22 2020

@author: heart
"""
### 1
"""
In the below code the __str__() method is not called because the call to the __str__() method 
is independent of the constructor call. Similarly, the call to the parent class constructor
 A using super().__init__() does not affect the __str__ method.
"""

class A:
  num = 0  
  def __str__(self):
      A.num = A.num + 1
      return str(A.num)
  
class B(A):
  def __init__(self):
      super().__init__()
  
obj = A()    
print('A(): ',obj)
print('A(): ',obj)
print('B(): ',B())

####
"""
__str__() method will be executed only when the reference of an object is accessed inside 
the print() function.
"""
class C:
    def __str__(self):
        print('Welcome')
        return 'Welcome'     
C()

####
class D:
    def __str__(self):
        print('Welcome')
        return 'Welcome'
        
print(D())

####
"""
The number of times the __str__method executes depends on the number of times 
the reference of an object is passed to the print() function.
"""
class A:
    num = 0
    def __str__(self):
        A.num = A.num + 1
        print(A.num)
        return 'Welcome'

obj = A()        
print(obj)
print(obj)
print(obj)


### 2
### Below code will present how this "-%0d"% works
print("-%0d"%555.55)
print("-%01d"%555.55)
print("-%02d"%555.55)
print("-%03d"%555.55)
print("-%04d"%555.55)
print("-%05d"%555.55)
print("-%06d"%555.55)
print("-%07d"%555.55)
print("-%08d"%555.55)
print("-%09d"%555.55)
print("-%010d"%555.55)
print("-%011d"%555.55)

print("-%0d"%555.55)
print("-%1d"%555.55)
print("-%2d"%555.55)
print("-%3d"%555.55)
print("-%4d"%555.55)
print("-%5d"%555.55)
print("-%6d"%555.55)
print("-%7d"%555.55)
print("-%8d"%555.55)
print("-%9d"%555.55)
print("-%10d"%555.55)
print("-%11d"%555.55)


### 3
print(10 // 2 * 3 + 9)
print(10.0 // 2 * 3 + 9)
print(10 // 2.0 * 3 + 9)
print(10 / 2 * 3 + 9)


### 4
class Car:
    def __init__(self):
        self.price = 2000
        self.__No_Seats = 4
    def details(self):
        print(self.price)
        print(self.__No_Seats)
    class a : pass
        
obj = Car()
obj.details

"""
1. When the function with parentheses like this display() is called, the function gets execute 
and returns the result to the callable.
2. When the function without parentheses like this display is called, a function reference 
is sent to the callable rather than executing the function itself.
"""

class Car:
    def __init__(self):
        self.price = 2000
        self.__No_Seats = 4
    def details(self):
        print(self.price)
        print(self.__No_Seats)
    class a : pass
        
obj = Car()
print(obj.details)
print(obj.a)    

#################
class Car:
    def __init__(self):
        self.price = 2000
        self.__No_Seats = 4
    def details(self):
        print(self.price)
        print(self.__No_Seats)
            
obj = Car()
obj.details

#####################
class Car:
    def __init__(self):
        self.price = 2000
        self.__No_Seats = 4
    def details(self):
        print(self.price)
        print(self.__No_Seats)
            
obj = Car()
obj.details()


### 5
# readline() function will return an empty string after the last character in a file.

file = open('sys.txt', 'r')
file.readline()
file.readline() 
file.readline()
print(file.readline()) 
file.close()

#######
file = open('sys.txt', 'r')
a = file.readline()
print(a,type(a)) 
a = file.readline()
print(a,type(a)) 
a = file.readline()
print(a,type(a)) 
a = file.readline()
print(a,type(a)) 
a = file.readline()
print(a,type(a)) 
file.close()


### 6
"""
print(_B)  and print(__C) will raise an error because the private variable __C and the protected variable _B
 can not be accessed in another file.
"""

### 7
a = str(30) + "Oranges"
print(a)


### 8
print("Java")
print('Java')
print(`Java`) # . Because grave accent `  can not be used to create a string.


### 9
small = "java"
big = "" 
for i in small: 
  big += chr (ord(i) -32) 
print(big)

"""
UNICODE Code points:- 
j -> 106
a -> 97
v -> 118
a -> 97
J -> 74
A -> 65
V -> 86
A -> 65
"""
"""
ord() is used to convert a character to a code point.
chr() is used to convert a code point to a character.
As you might have noticed after reading the Code points given in the question that the difference between 
the capital caps letters and the small caps letters encoding is of -32. So if you want to convert a 
small caps letter to a capital caps you need to subtract 32 from the code point of the small caps letter.
"""


### 10
text = "Certified Associate in Python Programming"
x = text.split('i') 
for c in x: 
     print(c, end=' ')
     
     
### 11
### test1
class List :
    _name = "List"
    def __init__(self):
        self._l = [1,2,3,4,5,6,7,8,9,10]
        for i in range(0,len(self._l)):
            if self._l[i]%2 == 0 :
               self._l[i] = self._l[i]/2 
               
### test2
import test1
class List1(test1.List):
    def __init__(self):
        super().__init__()
        print("One: ",self._l)      
        print("Two: ",test1.List._name)             
 
List1()

"""
It is true that protected variables can not be accessed in another file or module.

But if the above statement is correct then why we are able to access protected variables _l and _name in another file. 
This happens because the protected variables are not directly accessed in the test2.py file from the test1.py. 
As the List class is public therefore it got inherited to test2.py file and with that, the protected variable to got inherited.
"""


### 12
import math
print(math.floor(5.45))
print(math.floor(-5.45))

# floor(x) function will return the largest integer not greater than x.
import math
print("5.0: ",math.floor(5.0))
print("5.1: ",math.floor(5.1))
print("5.2: ",math.floor(5.2))
print("5.3: ",math.floor(5.3))
print("5.4: ",math.floor(5.4))
print("5.5: ",math.floor(5.5))
print("5.6: ",math.floor(5.6))
print("5.7: ",math.floor(5.7))
print("5.8: ",math.floor(5.8))
print("5.9: ",math.floor(5.9))
print("6:   ",math.floor(6))
print("6.1: ",math.floor(6.1))

import math
print("-5.0: ",math.floor(-5.0))
print("-5.1: ",math.floor(-5.1))
print("-5.2: ",math.floor(-5.2))
print("-5.3: ",math.floor(-5.3))
print("-5.4: ",math.floor(-5.4))
print("-5.5: ",math.floor(-5.5))
print("-5.6: ",math.floor(-5.6))
print("-5.7: ",math.floor(-5.7))
print("-5.8: ",math.floor(-5.8))
print("-5.9: ",math.floor(-5.9))
print("-6:   ",math.floor(-6))
print("-6.1: ",math.floor(-6.1))


### 13
try:
   print("Hello")
except:
   print("Error in Code")
else:
   print("No Error in Code ")
finally:
   print("finally")
   
"""
except:- The except block will execute if there is some error raised inside the try block.

else:- The else block will execute if there is no error raised inside the try block.

finally:- The finally block will execute irrespective of the error raised inside the try block.
"""

try:
   print(Hello)
except:
   print("Error in Code")
else:
   print("No Error in Code ")
finally:
   print("finally")


### 14
A = [[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]
 
print(A)


### 15
# .If the file sys.txt already contain the text "Welcome" 
# then what will be the text present in the file after the execution of the following code:-
file = open('sys.txt', 'a') 
file.write("To Programming ") 
file.close()

"""
In the append mode the new text(To Programming ) got added up to the old text ( Welcome ), 
Therefore finally the file will contain the text "WelcomeTo Programming"
"""


### 16
not(10!=10) and bool(10!=10) 


"""
    y = not(x)

1.  The value of y will be True for the value of x to be a boolean Flase, a Zero, an empty String, 
or for empty data types like an empty list [].

2. The value of y will be False for the value of x to be a boolean True. a non - zero value, a non-empty string  
or for non-empty data types like [1,2,3].

------------------------------------------------

bool() function work opposite to that of not function.
"""

print(not(False))
print(not(True))
print(bool(False))
print(bool(True))

print(not(1))
print(not(0))
print(bool(1))
print(bool(0))

print(not("Hi"))
print(not(""))
print(bool("Hi"))
print(bool(""))


### 17
# Which among the following are the correct ways to delete the length attribute from the Box class

class Box:
     def __init__(self):
         self.length = 3
         self.height = 9
         self.breadth = 5
 
obj = Box()

"""
In delattr() function del means delete and attr means an attribute or a variable.   

     delattr(x ,y)

x:- Name of a class or the reference an object.
y:- Is the name of a variable as a String value

Point 1:- if x is the class name then delattr function is used to delete the static variable y form the class.
Point 2:- if x is the reference of an object then delattr function is used to delete the variable y from the class, 
here the variable y can be static or an instance variable.

Q. Why in the Point2 the variable y can be both static and instance But in the Point1 the variable y can only be static?

Ans. Because a static variable can be accessed using both the object reference and the Name of a class, 
But an instance variable can only be accessed using the reference of the object only.
"""

class Box:
     def __init__(self):
         self.length = 3
         self.height = 9
         self.breadth = 5

obj = Box()
delattr(obj , 'length') 


class Box:
     def __init__(self):
         self.length = 3
         self.height = 9
         self.breadth = 5

obj = Box()
delattr(Box , 'length') 


class Box:
     def __init__(self):
         self.length = 3
         self.height = 9
         self.breadth = 5

obj = Box()
del obj.length 


### 18
small = "small"
print(small)
big = "big"
print(big)
Error = "Error"
print(Error)

in = "in"
print(in)


### 19
class Car:
  speed = 10
  def BoostSpeed():
      result=10*Car.speed
      return result
print(Car.BoostSpeed())

"""
Q.Why the options 1 and 3 are wrong?
Ans.Because both the static method BoostSpeed() and the static variable speed can be called using the class name Car.
"""


### 20
sets = {0,0,1,4,6}
print(sets)

# Duplicate values are not allowed in the Set, therefore the option 2 is correct as it does not contains duplicate zeroes.


### 21
T1 = (1) 
T2 = (3, 4) 
T3 = T1 + T2
print(T3)

"""
#Below is not the correct way to make a tuple using single element
T1 = (1) 
print(T1,type(T1))
#Below is the correct way to make a tuple using single element
T1 = (1,) 
print(T1,type(T1))
"""


### 22
# Fill in the blank, So that the below code prints
# Language is:  Python

class language :
    def __init__(self):
        self.name =  "Java"
    
    def call_me(self):
        print("Language is: ",self.name)
        
obj = language()
obj.name = "Python"
# or setattr(obj, 'name', "Python")
obj.call_me()

"""
   setattr(x,y,z)

x:- variable x contains the reference of an object or it can be the name of a class.
y:- y is the name of a variable to which we want to assign the value z, y must be a string value.
"""

# If x is a class name then y must be a static variable, if the variable y does not exist 
# the python will create one inside the class and assign the value z to it.

class language :
    def __init__(self):
        self.name =  "Java"
    
    def call_me(self):
        print("Language is: ",self.name)
        
obj = language()
setattr(language,'name',"Python")
print(language.name)
obj.call_me()


class language :
    def __init__(self):
        self.name =  "Java"
    
    def call_me(self):
        print("Language is: ",self.name)
        
obj = language()
obj.name = "Python" 
obj.call_me()


### 23
try:
     print("Hello")
finally:
     print("End of Code")
     
"""
1.try and finally block can be used without an except block too.

2.finally block will execute irrespective of an error raised inside the try block.
"""


### 24
x = 50
def Calculate():
  global x 
  x=20
  print("Calculation inside a function:",x*2+5-9)
 
Calculate()
print("Calculation outside a function:",x*2+5-9)

"""
If we try to access a global variable inside a function using the global keyword and try to assign a value to the global variable
the new value will be assigned to the variable that is declared outside of the class.
"""


### 25
i = 6
while True:
  if i%0O14 == 0:
     break
  i += 1
print(i)

"""
0O14 is an octal number and its decimal conversion is 12
"""


### 27
class Parent:
  def __init__(self,age):
       self.age=age
  def get_parent_age(self):
      return self.age
 
class Child(Parent):
  def __init__(self):
      super().__init__(55)
      self.age = super().get_parent_age() - 25
  def get_child_age(self):
        return self.age
 
obj = Child()
print("Child age is:  ",obj.get_child_age())
print("Parent age is: ",obj.get_parent_age())


"""
get_parent_age() method can be called using child the class object reference because it got inherited 
from the parent class to the child class.
--------------------------------------------
get_parent_age() method can be called using super() because here the super() passes the reference of the child class object.
"""

"""
Q.Why the age of both the parent and child is the same.
Ans. because the self variable in the parent and the child class contains the same reference.
"""
class A:
    def __init__(self):
        print(self)
class B(A):
    def __init__(self):
        super().__init__()
        print(self)
B()


### 28
class A:
    def __init__(self):
        print(type(self))
class B(A):
    def __init__(self):
        super().__init__()
        print(type(self))
B()

"""
super() returns the reference of the superclass object, 
But it passes the child class object reference to the parent class constructor.

class A:
    def __init__(self):
        print(type(self))
class B(A):
    def __init__(self):
        super().__init__()
        print(type(self))
        print(type(super()))
B()
"""


### 29
a = '62'+'14'
print(a ,type(a))

"""
#when both the operands of the + operator are string then concatination takes place
a = '62'+'14'
print(a ,type(a))

#when both the operands of the + operator are int then addition takes place
a = 62+14
print(a ,type(a))
"""


### 30
class language :
    def __init__(self):
        self.name =  "Java"
        print(self.name)
        
        
class language :
    def __init__(self):
        self.name =  "Java"
        print(self.name)
language().__init__()   


class language :
    def __init__(self):
        self.name =  "Java"
        print(self.name)
language.__init__(language()) 



### 31
class A:     pass
class B(A) : pass
class C(B,A) : pass
 
print(A.__bases__)
print(B.__bases__)
print(C.__bases__)

"""
This built-in class attribute   __bases__  when called on a class returns the tuple of base classes for the class on which it is called.

Q. Why for class A __bases__ returns (<class 'object'>,).
Ans. Because Object class is the base of all the classes.

Q. If Object class is the base class of all  the classes then why for class B and class C __bases__ does not 
return <class 'object'> inside tuple.
Ans. Because __bases__ return the name of only those parent or base classes that are directly inherited to the class.
"""

class A:
    a = 'a'
class B(A) :
    b = 'b'
class C(B) :
    c = 'c'

print(C.a,C.b,C.c)
print(C.__bases__)

"""
In the above code, you have noticed that although the class C inherits the feature of class A but then also 
the __base__  attribute does not return the name class A because the class A is not directly inherited to class C.
"""


### 32
# Single inheritance, multiple inheritance, hybrid inheritance, hierarchical inheritance


### 33
top_speed = {"audi_r8" : 320, "audi_a4" : 120,"audi_q5" : 147 }
for (key, values) in top_speed .items():
    print(key, values, end = " ")

"""
Dictionaries are unordered till python version 3.6.
But from Python version 3.7 dictionaries are ordered.
An unordered dictionary means the insertion order of key-value pairs is not preserved.
But in an ordered dictionary the insertion order of key-value pairs is preserved.
"""


### 34
speed = {320 , 120 , 200 , 100}
print(speed)

"""
A set is an unordered collection with no duplicate elements.
Unordered means that the order of elements inserted into a set is not preserved.
"""


### 35
# Fill in the blank so that the below code will print 2 3
class Parent:
  def __init__(self):
       self.a = 2
 
class Child(Parent):
  def __init__(self):
       super().__init__()
       self.b = 3
 
obj = Child()
print(obj.a , obj.b)


class Parent:
  def __init__(self):
       self.a = 2
 
class Child(Parent):
  def __init__(self):
       Parent.__init__(self)
       self.b = 3
 
obj = Child()
print(obj.a , obj.b)

"""
Here while calling the parent class constructor, the first argument passed is the reference of the parent class object 
and the second argument passed is the reference of the child class object.
"""
# Below is error
class Parent:
  def __init__(self):
       self.a = 2
 
class Child(Parent):
  def __init__(self):
       Parent().__init__(self)
       self.b = 3
 
obj = Child()
print(obj.a , obj.b)

"""
While calling the parent class constructor as the reference of the parent class object is passed therefore 
the variable a is defined for the parent class object.
"""

class Parent:
  def __init__(self):
       self.a = 2
 
class Child(Parent):
  def __init__(self):
       Parent().__init__()
       self.b = 3
 
obj = Child()
print(obj.a , obj.b)



### 36
import math
print("Output : ",math.ceil(5.45))

# math.ceil(x) return the smallest integer not less than x.
import math 
print("5.0: ",math.ceil(5.0))
print("5.1: ",math.ceil(5.1))
print("5.2: ",math.ceil(5.2))
print("5.3: ",math.ceil(5.3))
print("5.4: ",math.ceil(5.4))
print("5.5: ",math.ceil(5.5))
print("5.6: ",math.ceil(5.6))
print("5.7: ",math.ceil(5.7))
print("5.8: ",math.ceil(5.8))
print("5.9: ",math.ceil(5.9))
print("6.0: ",math.ceil(6.0))
print("6.1: ",math.ceil(6.1))

import math 
print("-5.0: ",math.ceil(-5.0))
print("-5.1: ",math.ceil(-5.1))
print("-5.2: ",math.ceil(-5.2))
print("-5.3: ",math.ceil(-5.3))
print("-5.4: ",math.ceil(-5.4))
print("-5.5: ",math.ceil(-5.5))
print("-5.6: ",math.ceil(-5.6))
print("-5.7: ",math.ceil(-5.7))
print("-5.8: ",math.ceil(-5.8))
print("-5.9: ",math.ceil(-5.9))
print("-6.0: ",math.ceil(-6.0))
print("-6.1: ",math.ceil(-6.1))



### 37
import math
print(math.factorial(4.5)) 

"""
ValueError is raised when an operation or a function receives an argument that has the right type 
but an inappropriate range of value.

Here the factorial() function can take the float value but the float value must be like this 1.0, 4.0, 5.0.
"""

import math
print(math.factorial(4.0)) 



### 38
class Add:
    def __init__(self ,x,y):
        self.num1 = x
        self.num2 = y
        
    def __str__(self):
        return self.num1 + self.num1
        
obj = Add(3,4)
print(obj)

# __str__ function must return an only string value.

class Add:
    def __init__(self ,x,y):
        self.num1 = x
        self.num2 = y
        
    def __str__(self):
        return str(self.num1 + self.num1)
        
obj = Add(3,4)
print(obj)

"""
__str__() method will be executed only when the reference of an object is accessed inside the print() function.
In the below code the __str__() method is not called because the call to the __str__() method is independent of the constructor call.
"""

class A:
    def __str__(self):
        print('Welcome')
        return 'Welcome'     
A()


class A:
    def __str__(self):
        print('Welcome')
        return 'Welcome'
        
print(A())

"""
The number of times the __str__method executes depends on the number of times the reference of an object is passed to the print() function.
"""

class A:
    num = 0
    def __str__(self):
        A.num = A.num + 1
        print(A.num)
        return 'Welcome'
obj = A()        
print(obj)
print(obj)
print(obj)


### 39
"""
The default except block can only be one But the user-defined except block can be as many as we want.
"""
try :
  print("Hello")

except :            #Default except block
    pass

except :
    pass

#
try :
  print("Hello")

except NameError :   # user-defined except block
    pass

except NameError :
    pass


### 40
class Student :
    Class = 0
    def __init__(self,x,y,z):
        self.name = x
        self.roll_name = y
        Student.Class = z
        
obj = Student("Mia",4578,10)
print(obj.__dict__)      

"""
When __dict__ is called on an object reference it will return a dictionary containing the name of a variable as a key of a dictionary 
along with the values stored in a variable as a dictionary value.
"""


class Dog:
    kind = 'canine'         # class variable shared by all instances
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')
print(d)
print(e)
d.kind                  # shared by all dogs'
print(d.kind)
e.kind                  # shared by all dogs
print(e.kind)
d.name                  # unique to d
print(d.name)
e.name                  # unique to e
print(e.name)








