str1 = "Forsk Coding School"

type(str1)

print (len(str1))

str1[0]

str1[-1]

#indexing, slicing
str1[0:10]

str1[5:15]

str1[10:]

str1[:10]

str1 = "Forsk Coding School"

#string operations
#convert the str1 text to all uppercase

#str

print (dir(str))

help(str.upper)


str2 = str1.upper()


str1[0] = 'f'
#strings are read only
#immutable


#math library

#include <math.h>

import math

dir(math)

help(math.sqrt)

x = input("Enter the number: ")


x = int(x)

print (math.sqrt(x))


#version 01
while (True):
    x = input("Enter the number: ")
    
    #check if x is blank
    
    if (not x):
        print ('Invalid input..leaving app')
        break #terminates the loop
    
    x = int(x)
    
    print (math.sqrt(x))   
    
#version 02
while (True):
    x = input("Enter the number: ")
    
    #check if x is blank
    
    if (not x):
        print ('Invalid input..try next')
        break
    
    
    if( x.isdigit()):
        
        x = int(x)
        
        print ("the square root is", math.sqrt(x)) 
    else:
        print ("the length is", len(x))


#version 03

datastore = []
while (True):
    x = input("Enter the number: ")
    
    #check if x is blank
    
    if (not x):
        print ('Invalid input..try next')
        break
    
    
    if( x.isdigit()):
        
        x = int(x)
        
        datastore.append(math.sqrt(x))
    else:
        datastore.append(len(x))



print (datastore)

