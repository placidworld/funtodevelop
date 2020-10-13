# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 15:59:26 2020

@author: heart
"""
### 1
x = '10' - '20'
print(x)

"""
Type Error raised when an operator or function is applied to an object of an inappropriate type.
Here the operator - is applied to the object string of an inappropriate type.
"""

### 2
def LetterWord(*inp):
       print(type(inp))
LetterWord('P','y','t','h','o','n')

"""
If you do not know about the Non-Keyword Arguments Click Here.
https://www.programiz.com/python-programming/args-and-kwargs
After going through the above article you will be able to understand the above code.
"""

### 3
List = [1,2,4,5,6,7,8]
for i in range(0,len(List)):
    if(List[i]%5==0):
        List.append(9)
    if((len(List)-1)==i):    
        print(List[i] + List[2])


def f(a):
    print(a)
    return a
l = [1,2,4,5,6,7,8]
for i in f(range(0,len(l))):
      l.append("&")
      print(l)

"""
In the above code range(0, 7) is printed only once, because the range object is created only once.
As the range object is created only therefore irrespective of the change in the length of the list 
in each iteration the number of iteration remains the same. 

In this for i in range(0,len(List)) line of the code the range function will return the range object only once.
As the range() object is created only once, therefore, the number of iterations also remained the same 
instead of increasing the length of the list.

"""
            

### 3
List = [1,2,4,5,6,7,8]
for i in List:
    if(i%5==0):
      List.append(9)
         
    if((List[len(List)-1])==i):    
        print(i + List[2])

"""
As here the whole list is accessed again and again at each iteration by the in operator, 
therefore the changes made in the List using append also affect the number of iteration.
"""    
    
### 5
class BioData:                                       #line1
   def __init__(self,x,y):                           #line2
        self.name = x ; print("Name: ",self.name)    #line3
        self.age = y  print("Age: ",self.age)        #line4
                                                     #line5
BioData('Emma',23)                                   #line6

"""
The semicolon must be used if more than one statement is used in a single line.

The semicolon must be placed between these multiple statements in a single line.
"""


### 6
class Circle:
  def __init__(self,x):
      self.__radius = x 
 
class Sphere(Circle):
  def volume(self):
      r = self.__radius
      print((4/3)*3.14*r*r*r)
 
Sphere(5).volume()

# Private variables are not allowed to be accessed inside the Child class.

class Circle:
  def __init__(self,x):
      self.radius = x 
 
class Sphere(Circle):
  def volume(self):
      r = self.radius
      print((4/3)*3.14*r*r*r)
 
Sphere(5).volume()


### 7
num = 65
for i in range(0, 5): 
     for j in range(0, i+1): 
          ch = chr(num) 
          print(ch, end=" ") 
     num = num + 1
     print(" ")
     
    
### 8
file = open('sys.txt', 'wb') 
file.write(bytearray("JAVA",'ASCII')) 
file.close()

"""
Q: Why bytearray("JAVA",'ASCII')  is used.
Ans. Because the file is opened in a wb mode, therefore,
 the write function will take byte array object or byte object

wb mode Opens a file for writing only. Overwrites the existing file if the file exists. 
If the file does not exist, creates a new file for reading and writing.
"""
file = open('sys.txt', 'wb') 
file.write(b'JAVA')
file.close()


### 9
print(__name__)
print(type(__name__))

"""
If the source file is executed as the main program, the interpreter sets the __name__ variable 
to have a value “__main__”. If this file is being imported from another module,
 __name__ will be set to the module’s name.

As in the above case, the test.py file is executed as the main program, therefore,
the __name__ inside test.py file is assigned the string value “__main__”.
"""


### 10
D = {1:"First",2:"Second",3:"Third",4:"Four"}
if(D[4]!=None) :
    del D[4]
for i in D:
    print(i,end = " ")

"""
This for i in D: way of iterating through dictionary D is used to access keys in a dictionary.
del is used to remove a key from a dictionary.
"""



### 11
D = {1:"First",2:"Second",3:"Third",4:"Four"}
if(D[4]!=None) :
    del D[4]
for i in D.items():
    print(i,end = " ")

"""
The items() method returns a dict_items object. The dict_items object contains 
the key-value pairs of the dictionary, as tuples in a list.
"""
D = {1:"First",2:"Second",3:"Third",4:"Four"}
print(D.items())
  
    
### 12
#Consider that the below code is written inside test1.py file.

print("print of test1: ",__name__)

#Consider that the below code is written inside test2.py file.

import test1
print("print of test2: ",__name__)
#Choose the correct output when the test2.py file is executed.

"""
If the source file is executed as the main program, the interpreter sets the __name__ variable 
to have a value “__main__”. 
If this file is being imported from another module, __name__ will be set to the module’s name.

As in the above case, the test2.py file is executed as the main program, therefore, 
   the __name__ inside test2.py file is assigned the string value “__main__”.

And as test1.py is imported to test2.py file, therefore the print function of test1.py file also gets imported to test2.py file  now as the print("print of test1: ",__name__) is imported from another module therefore __name__ of print("print of test1: ",__name__)  is assigned the name of that module that is "test1".
"""  



### 13
import math
print(math.factorial('4'))

"""
TypeError is raised when an operator or a function is applied to an object of an inappropriate type.
Here function factorial is passed with the object string which is of an inappropriate type.
"""

### 14
def SUM(*x):
    result = 0
    for i in range(len(x)):
        result = result + int(x[i])
    print(result) 
SUM(5,4,1,2,3)



### 15
# If the file sys.txt already contain the text "JAVA" then what will be printed in the console 
# after the execution of the following code:-

file = open('sys.txt', 'rb') 
print(file.read()) 
file.close()

"""
As the file is opened in the binary mode rb  therefore 
the read function will return a byte object of the JAVA string.
"""

file = open('sys.txt', 'rb') 
print(type(file.read())) 
file.close()


### 16
print("SpaceX: %1s"  %("Tesla")) 
print("SpaceX: %4s"  %("Tesla"))  
print("SpaceX: %10s" %("Tesla"))

# Go through the output of the below code you will be able to understand the use of "sd"%
print("1 :","SpaceX: %1s" %("Tesla"))
print("2 :","SpaceX: %2s" %("Tesla"))
print("3 :","SpaceX: %3s" %("Tesla"))
print("4 :","SpaceX: %4s" %("Tesla"))
print("5 :","SpaceX: %5s" %("Tesla"))
print("6 :","SpaceX: %6s" %("Tesla"))
print("7 :","SpaceX: %7s" %("Tesla"))
print("8 :","SpaceX: %8s" %("Tesla"))
print("9 :","SpaceX: %9s" %("Tesla"))
print("10:","SpaceX: %10s" %("Tesla"))

# s is used for string and d is used for integer value inside ()
print("SpaceX: %10d" %(100))
print("SpaceX: %10d" %("Tesla"))

### 17
print(~10)
print(~~10)

"""
~Y is represented as -(Y+1)

~10 -> -(10+1) -> -11
~~10 -> -(~10 + 1) -> -(-11 +1) -> 10
"""

### 18
# Constructor
"""
So according to the definition, None is frequently used to represent the absence of a value or in other words, 
None is used to represent No value.

As according to the above explanation all the below statements are correct:-
1. A class constructor cannot return a value
2. A class constructor can return the None value
3. A class constructor can return a no value
-------------------------------------------------
"""

# A class constructor cannot return a value

class A:
    def __init__(self):
        return 456
A()

#A class constructor can return the None value

class A:
    def __init__(self):
        return None
A()


# A class constructor can return a no value

class A:
    def __init__(self):
        return 
A()



### 19
a = "Tesla"
b = "electric"
c = "makes"
d = "cars"
str = '{0} {2} {1} {3}'.format(a, b, c, d) 
print(str)


#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)


#Use "<" to left-align the value:

txt = "We have {:<8} chickens."
print(txt.format(49))


txt = "We have {:>8} chickens."
print(txt.format(49))

#Use "^" to center-align the value:

txt = "We have {:^8} chickens."
print(txt.format(49))

#Use "=" to place the plus/minus sign at the left most position:

txt = "The temperature is {:=8} degrees celsius."

print(txt.format(-5))



### 20
a = input("Enter first number")
b = input("Enter second number")
print(a+b)


### 21
x = 'Python Java'
for i in x:
     if(i==" ") : print()
     else : print(i,end = "")
     
     
"""
print()  is same as print(end = "\n")  that is the default  value of end is "\n", 
therefore when print() is called cursor moves to the next line.

At most one statement can be placed in front of a colon : without using a semicolon ;
"""


### 22
for i in range(0, 5): 
    for j in range(0, i+1): 
        print("* ",end="") 
    print(" ") 
    
    
### 23
x = Orange
print(x)

"""
NameError comes when Python tried to use a variable or a function name 
and the variable or the function is not defined in the program.
"""

### 24
x = (9,5,1) 
x.append( (7,5,3) ) 
length = len(x)
print(length)


"""
An Error is raised because the tuple does not have the append method.

Q. Why the tuple does not have the append method.

Ans. Because a tuple is immutable.
"""


### 25
try:
      print(1/0)
except ZeroDivisionError:
      print("Zero Division Error")
except:
      print("Error is raised ")
else:
      print("No Error is raised")
      
"""
except:- The except block will execute if there is some error raised inside the try block.

else:- The else block will execute if there is no error raised inside the try block.

finally:- The finally block will execute irrespective of the error raised inside the try block.

As dividing one by zero raise the ZeroDivisionError, therefore, 
the except block catching ZeroDevisionError was executed.
"""


### 26
class Employee :
     company_name = 'Google'
     def __init__(self):
         self.name = 'Emma' 
print(hasattr(Employee(),'company_name'))
print(hasattr(Employee,'company_name'))
print(hasattr(Employee(),'name'))
print(hasattr(Employee,'name'))
print(hasattr(Employee,'salary'))
         
 
"""
Syntax:-
   hasattr(x, y)

1. x: x is the name of a class or the object of a class.
2. y: y is the name of an attribute.

hasattr function returns true if y can be accessed using x.
hasattr function returns false if y can not be accessed using x.

Q. Why print(hasattr(Employee(),'company_name')) and print(hasattr(Employee,'company_name'))  prints true.
Ans. Because the static variable compay_name can be accessed using both the class name and the object of a class.

Q. Why print(hasattr(Employee(),'name')) prints true and print(hasattr(Employee,'name')) prints false.
Ans Because the instance variables like 'name' can be accessed using the object of a class only.

Q. Why print(hasattr(Employee,'salary')) prints false.
Ans. Because the variable name salary is not defined in the Employee class.
"""

### 27
def calculate(x):
  z = lambda x : return x**2
print(z(x))
calculate(4)

# The Error is raised because the return keyword can not be used inside a lambda function.


### 28
#Below is the wrong way to make a tuple with a single element
T = (1)
print(T," : ",type(T))

#Below is the correct way to make a tuple with a single element
T = (1,)
print(T," : ",type(T))


T1 = (1,)
T2 = (2,)
T3 = (3,)
print(T1+T2+T3)


### 29
"""
3Version  can not be used as a variable name Because a variable name 
can start with a digit.
"""

Πύθων  = "Java1"            #Πύθων are greek letters and greek letters are allowed to make variable
Python = "Java2"
_Python = "Java3"
print(Πύθων,Python,_Python)


### 30
class Student :
     def __init__(self):
         self.name = 'Olivia'
         
     def set_rollNo(self):
         self.rollNo = 45786
print(hasattr(Student(),'rollNo'))

         
"""
Syntax:-
   hasattr(x, y)

1. x: x is the name of a class or the object of a class.
2. y: y is the name of an attribute.

hasattr function returns true if y can be accessed using x.
hasattr function returns false if y can not be accessed using x.

Q. Why print(hasattr(Student(),'rollNo')) prints false.
Ans. Because variable rollNo can only be called using the object of the class 
after the call of the setrollNo function.

Only after the call of the set_rollNo() method, the rollNo variable 
gets defined for the object of the class.
"""
class Student :
     
     def __init__(self):
         self.name = 'Olivia'
         
     def set_rollNo(self):
         self.rollNo = 45786
         
a = Student()
a.set_rollNo()
print(hasattr(a,'rollNo'))

b = Student()
print(hasattr(b,'rollNo'))


"""
Q. Why print(hasattr(Student(),'name')) and print(hasattr(Student(),'set_rollNo'))  prints true.
Ans. Because the variables name and set_rollNo are accessible using the object of the class Student only.
"""

### 31
"""
issubclass(x,y)

1.x:-  it is a class
2.y:- Is a class or a data type name like list, int, or a tuple containing more than 
one class or a tuple containing more than one data type name or 
a tuple can contain both class and data type.

->Point 1:-  issubclass(x,y) return true if x is a subclass of y, for vice-versa function will return false.
->Point 2:- issubclass(x,y) return true if x is a subclass of any of the class present in the tuple y.
->Point 3:- issubclass(x,y) return true if both the x and y are the same class.
"""

class A() : pass
class B(A) : pass
class C(B) : pass

print(issubclass(C,A))         #refer to point 1
print(issubclass(B,A))         #refer to point 1
print(issubclass(A,C))         #refer to point 1
print(issubclass(A,B))         #refer to point 1
print(issubclass(C,(A,B)))     #refer to point 2
print(issubclass(B,(C,A)))     #refer to point 2
print(issubclass(B,(A,A)))     #refer to point 2,point 3 
print(issubclass(A,A))         #refer to point point 3


### 32
"""
Syntax:-
     isinstance(x,y)

x:- Is an object of a class or elements of data types like 2, 3.45 or [1,2,3]
y:- Is a class or a data type name like list, int, or a tuple containing more than one class 
or a tuple containing more than one data type name or a tuple can contain both class and data type.

-> Point 1:- isinstance function returns true if x is an object of y or 
at least one of the class present in the tuple y.
-> Point 2:- isinstance function returns true if x is an element of y or 
at least one of the data types present in the tuple y.

"""

#+ operator takes boolean value True as 1
x = True + True    
print(isinstance(x,bool))

class A : pass
class B(A) : pass
obj = B()
print(isinstance(obj,A))

class A : pass
class B(A) : pass
obj = A()
print(isinstance(obj,B))

obj = {1,2,3,4}
print(isinstance(obj,(set,list)))


### 33
try :
  a = 0
  print(a = 4)
except:
  print("Error is raised in try")
  
# Using the assignment operator inside the print function will raise a type error.

print(a = 4)


### 34
# If the file sys.txt already contain the text "Welcome" then what will be the text present 
# in the file after the execution of the following code:-

file = open('sys.txt', 'w') 
file.write("To Programming ") 
file.close()

"""
w in the open function represents the writing mode.

In the writing mode, the text does not get adds up or you can say append, 
rather the old text present("Welcome") gots deleted up and the new text(To Programming) 
got written into the file.
"""


### 35
"""
If the sys.txt file contains the 3 lines,
1st line (Welcome),
2nd line (To Python),
3rd line(Programming)

Fill in the blank, So that the below code will print text as it is written in the file.
"""

file = open('sys.txt', 'r') 
print(___________________) 
file.close()

"""
read(n) here n is the number of characters which we want to print.

If the value of n is smaller than zero or no value is passed then the read function returns 
all the characters present in the file.

==================================

Assume that the sys.txt file contains the below text.

Python 
Welcome 
"""
file = open('sys.txt', 'r') 
print(file.read(5)) 
file.close()
  
file = open('sys.txt', 'r') 
print(file.read(10)) 
file.close()

file = open('sys.txt', 'r') 
print(file.read(100000)) 
file.close()

file = open('sys.txt', 'r') 
print(file.read()) 
file.close()

file = open('sys.txt', 'r') 
print(file.read(-10)) 
file.close()


### 36
class Class_A():
  def info(self):
     print("Class_A")
 
class Class_B(Class_A):
    pass
 
obj = Class_B()
obj.info()

"""
Due to the inheritance info method got inherited to Class_B from Class_A therefore info method 
is accessible using Class_B object.
"""


### 37
class A():
    pass
try :
    raise A()
except ____________ :
    print("Please Rate This Course")
except :    
    print("Write Review for this Course")
    
    
"""
In the below code the statement raise A() does not raise an exception of the class A type 
rather the TypeError is raised by the interpreter when it tries to raise the exception of class A-type.

Q. Why an exception of class A type can not be raised using the raise keyword.
Ans. Because to raise an exception of a user-defined class. The user-defined class 
must inherit the BaseException class or the child class of the BaseException class.

Click here to get the Exception hierarchy in python 3.
"""

class A():
    pass
try :
    raise A()
except BaseException as e :
    print(e.__class__)


#The Exception class is the child class of the BaseException class.

class A(Exception):
    pass
try :
    raise A()
except BaseException as e :
    print(e.__class__)

"""
In the below code the statement except A raise the TypeError due to which the code got terminated.

On executing the statement except A the TypeError is raised because a class not inherited 
from the BaseException class or its child class can not be used by the except block to catch an exception.
"""

class A():
    pass
try :
    raise A()
except A :
    print("Please Rate This Course")
except :    
    print("Write Review for this Course")

"""
In the below code the statement except A is able to catch the exception because class A 
is inheriting the BaseException class.
"""

class A(BaseException):
    pass
try :
    raise A()
except A :
    print("Please Rate This Course")
except :    
    print("Write Review for this Course")

"""
except Exception and except BaseException are able to catch the TypeError 
because the Exception and the BaseException class are the parent class of the TypeError class.
except OSError is not able to catch the TypeError 
because the OSError class is not the parent class of the TypeError class.
"""

class A():
    pass
try :
    raise A()
except BaseException :
    print("Please Rate This Course")
except :    
    print("Write Review for this Course")
    
     
class A():
    pass
try :
    raise A()
except Exception :
    print("Please Rate This Course")
except :    
    print("Write Review for this Course")
    
    
class A():
    pass
try :
    raise A()
except OSError :
    print("Please Rate This Course")
except :    
    print("Write Review for this Course")

    
### 38
class Student:
    def __init__(self,m):
         self.__marks = m
         grace(self)
         print(self.__marks)
         
    def grace(self):
        self.__marks = self.__marks + 10
        
Student(23)

class Student:
    def __init__(self,m):
         self.__marks = m
         Student.grace(self)
         print(self.__marks)
         
    def grace(self):
        self.__marks = self.__marks + 10
        
Student(23)class Student:
    def __init__(self,m):
         self.__marks = m
         self.grace()
         print(self.__marks)
         
    def grace(self):
        self.__marks = self.__marks + 10
        
Student(23)


### 39
tp = (1, 2)
print(2 * tp)


### 40
set1 = {1, 2}
set2 = {1, 2}
print(set1 + set2)

# The plus operator cannot be used when sets are its operands.





  