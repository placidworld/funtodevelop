# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 22:44:29 2020

@author: heart
"""



import re

string1 = " I love python"
p = re.compile(r'python')
p.findall(string1)



string1 = " I love Python and python so much"
p = re.compile(r'python', re.IGNORECASE)
p.findall(string1)


string1 = " I love Python and python so much"
p = re.compile(r'python', re.I)
p.findall(string1)


p = re.compile(r'[abc]')
m = p.match('abc and xyx')
print(m)



p = re.compile(r'[a-c]')
m = p.match('abs')
print(m)


p = re.compile(r'[a-c]')
m = p.match('cba')
print(m)


pattern = re.compile(r'[amt?]')
m = pattern.match('?1234')
print(m)


pattern = re.compile(r'[amt?]?')
m = pattern.match('aaabbbccc?')
print(m)


pattern = re.compile(r'[amt?]+')
m = pattern.match('aaabbbccc?')
print(m)


pattern = re.compile(r'[a-zA-Z\s]+')
m = pattern.match("There are many things that 123456 we want to know about RegEx")
print(m)

print(m.group())

print(m.start())

print(m.span())


p = re.compile('[a-z]+')
m = p.search("%^&^%$ 123456789 Hey ^&*#^*&^62738r45")
print(m)


p = re.compile('[a-z]+', re.I)
m = p.search("%^&^%$ 123456789 Hey ^&*#^*&^62738r45")
print(m)


p = re.compile('[a-z\s]+', re.I)
m = p.search("%^&^%$123456789Hey There ^&*#^*&^62738r45 Hi People")
if m:
    print("'", m.group(), "'", ":", "Is Your Match")
else:
    print("No Match")
    


p = re.compile(r'\bpizza\b')
print(p.search('I want a pizzapie'))


print(p.search('I want a pizza'))


p = re.compile(r'\Bpizza\B')
print(p.search('I want a pizzapie'))


print(p.search('I want a pizza'))


print(p.search("Do you think Pinnaplepizzapies taste good?"))


p = re.compile('(ca)*')
print(p.match('cacacacaca').span())


print(p.match('cacac').span())


print(p.match('cacad').span())


print(p.match('cacad').group())



p = re.compile(r'(c(a)t)s')
m = p.match('cats')
m.group(0)


m.group(1)


m.group(2)


p = re.compile(r'(c(a)t)s')
m = p.finditer('I lvoe cats. Many many many cats. Not rats, but cats')
for match in m:
    print(match.span(), match.group())


string1 = "Hello, how, are, you?"

p = re.compile(r',\s(\w+)')
string1 = "Hello, how, are, you?"
f = p.finditer(string1)
for match in f:
    print("Position:{0:3} - String: {1:8}".format(match.start(), match.group(1)))

import re

string1 = "Hello, how, are, you, doing, right, now?"

p = re.compile(r'((\w+),\s(\w+))')
f = p.finditer(string1)
for match in f:
#    print(match.group(1))
#    print(match.group(2))
    print(match.group(3))


import re

string1 = "123 Windows Server 2016 R2; 1234 Windows server 2012 R3; 7225 Windows Server 2008 R3; 27863 Linux Blahblah v3; 345"
p3 = re.compile(r'(^\d+)|[\s+\w+](;\s+(\d+))')
f3 = p3.findall(string1)

for match in f3:
    print("{0:>0.3}{1:<10}".format(match[0],match[2]))

p3 = re.compile(r'(^\d+)|[\s+\w+](;\s+(\d+))')


string1 = "Hello People 2020"
p3 = re.compile(r'(?P<FirstWord>\b\w+\b)\s(?P<SecondWord>\b\w+\b)\s(?P<Year>\d+)')
matches = re.search(p3, string1)

print(matches.group("FirstWord"))
print(matches.group("SecondWord"))
print(matches.group("Year"))


p = re.compile(r'\b(?P<word>\w+)\s+(?P=word)\b')
string1 = "Hello how are are you? Are you you doing ok? Tell me me how you are doing?"
f = p.finditer(string1)
for match in f:
    print("Position:{0:5} - String: {1:8}".format(match.start(), match.group()))
    
### Read in name of all files in a text file
import re

pattern = re.compile(r'\w+\.\w+')

with open("file_names") as in_file:
    for line in in_file:
        output = pattern.findall(line)
        for match in output:
            print(match)
            
 
### Exclude any files that end in .txt from our search
import re

pattern = re.compile(r'\b\w+\.(?!txt)\w+')

with open("file_names") as in_file:
    for line in in_file:
        output = pattern.findall(line)
        for match in output:
            print(match)


### Extract only the phone numbers
import re

pattern = re.compile(r'\d{3}-\d{3}-\d{4}')

with open("phone.txt") as in_file:
    for line in in_file:
        output = pattern.findall(line)
        for match in output:
            print(match)
            
            
p = re.compile(r'\d{3}-?\d{3}-?\d{4}')


### Extract SSN
import re

pattern = re.compile('r\d{3}\s\d{2}\s\d{4}')

with open("ssn.txt", 'r', endcoding='utf-8') as f:
    contents = f.read()
    matches = pattern.findall(contents)
    for match in matches:
        print(match)        


### Grab specific chunks of text
import re

pattern3 = re.compile(r'(\.\s+)(.*snoopy\s*\w*\.)', re.I)

string = "While I was sitting around I saw woodchuck. " + \
         "I love that woodchuck and snoopy too. Big time " + \
         "friends snoopy they are. Hey Snoopy. The peanuts make me laugh snoopy."+ \
         " Snoopy makes me laugh. Charlie Brown loves snoopy."
         
f3 = pattern3.findall(string)

for match in f3:
    print("{0}".format(match[1]))
    

### Complicated pattern
import re

pattern3 = re.compile(r'(.+\.)(\s+.*\.\s+)(.*snoopy\s+\w+.)(\s+[\w\s]+\.)', re.I)  

string = "Here is my first sentence. SENT2 while I was sitting around I saw woodchuck.    "+ \
        "I love that woodchuck and snoopy too Yes I love him. Yese he rocks! " + \
        "If I loved him anymore it would be too much!!! Charlie Brown help!"
        
f3 = pattern3.findall(string)
for match in f3:
    print("Sentence Before: ", match[1])
    print("Snoopy sentence: ", match[2])
    print("Sentence After: ", match[3])
    
    
### Using re.finditer to find the positions of each time
### either word from a list is used in a string
import re

list1 = ['snoopy', 'woodchuck']

string1 = "While I was sitting around I saw woodchuck. " + \
         "I love that woodchuck and snoopy too. Big time " + \
         "friends snoopy they are. Hey Snoopy. The peanuts make me laugh snoopy."+ \
         " Snoopy makes me laugh. Charlie Brown loves snoopy."
         
for match in re.finditer('|'.join(list1), string1):
    print(match)
    

### Splitting strings
import re

p = re.compile(r'\W+')

search1 = p.split('THIS-IS-WHAT-I-WANT-TO-SPLIT.')
search2 = p.split('THIS IS WHAT I WANT TO SPLIT.')
search3 = p.split('THIS-IS-WHAT-I-WANT-TO-SPLIT.', maxsplit=2)

print("From search 1: ", search1)
print("From search 2: ", search2)
print("From search 3: ", search3)

p2 = re.compile(r'(\W+)')
search4 = p2.split('This..IS_something----Special&&.')
print("Also prints delimiter: ", search4)


### Search & Replace
import re

p1 = re.compile('(dogs|cats|fish)')
replace = p1.sub('animals', 'dogs are furry, cats are tricky and fish are pets too!')
print(replace)

p2 = re.compile('(dogs|cats|fish)')
replace = p1.sub('animals', 'dogs are furry, cats are tricky and fish are pets too!', count=2)
print(replace)

p3 = re.compile('(dogs|cats|fish)')
replace = p1.sub('animals', 'dogs are furry, cats are tricky and fish are pets too!', count=1)
print(replace)


text1 = "Animals{Dogs} Animals{Cats} Animals{Fish} Animals{Birds} Animals{Hampster}"

p5 = re.compile("Animals{([^}]*)}', re.VERBOSE)
replace5 = p5.sub(r'Animals{\1}', text1)
print(replace5)

    
Regular_Expression.txt
Displaying Regular_Expression.txt.