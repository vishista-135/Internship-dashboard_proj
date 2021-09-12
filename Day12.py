# How the memory is allocated in C Language 
# Use of & addressof operator to find the address
# int a = 6 ;
# &a

# How the memory is allocated in Python Language 
a = 6
print(id(a))


# Introduce the concept of Reference Count
b = 6
print(id(b)) 
print(id(a))


# Everything in Python is class
a = 6
#a = 10.7
#a = "Forsk"
#a = True
#a = None

print(type(a))
print(a.__class__)

# If primary data types are class then we can create objects
b = int()
print(b)
print(type(b))


c = int(7)
print(c)
print(type(c))

# Summary
# datatype = you create a variable of it
# Class    = you create a object of it 
# Difference between Reference Variable and Object

# OOPS is Object Oriented Programming System
# OOD  is Object Oriented Design


# History of Software Development 
"""
1950 - First OS ( Assembly Language )
1960 - Fortran, Algol, Cobol, Basic
1964 - OS/360 Mainframe
1967 - Simula (OOP)
1970 - C / Unix
1991 - Linux 

Procedural - Routines / Sub routines / Function and variables
Procedural ( Data and Function as seperate entities)

Why was OOP Invented ?

Slow
Expensive
Time Consuming

Maintainability
Extensibility
Reusability
DRY ( Do not repeat yourself)

OOPS is a philosophy and not a language 
It Logically group data and function 
Easy to reuse and build upon complex softwares
"""


# Introducing the keywords of Object Oriented Programming
"""
Class
Object/Instance
Data Hiding   
    Abstraction     - Something only existing as an idea
    Encapsulation   - Restricts access 
    Inheritance     - Create a new from existing
    Polymorphism    - Object that have more than 1 form 
Overriding 
Overloading
"""

# Algorithm to convert any real world abject into class

"""
# Steps for converting a REAL LIFE OBJECT into a CLASS
# 1. Visualise the REAL LIFE OBJECT in your memory 
# 2. List down the characteristics/state of the object
# 3. List down the Functionality/Behaviour of the object 



# Introduce the concept of Radio Blueprint 
"""
Characteristics    |   Functionality
---------------------------------------
color              |
brand              |
ACPower            |
headphone          |
                   |
power_led          | power_switch  ( ON / OFF)
mode_led           | mode_switch   ( AM / FM )
frequency          | band_tuner    ( 88 - 108 )
volume             | volume_tuner  ( 1 - 10 )
---------------------------------------
Characteristics are mapped into data/variables
Functionality are mapped into methods/functions
Class is a blueprint for creating instances (objects)


"""     
Represent Employee in Python 
Individual employee will have specific attributes and methods
Name
email address
Pay

Each individual employee would be the instance of the class 
"""

class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()


print ( emp_1)     # 0x115b68b00
print ( id(emp_1)) # 4659251968

print ( emp_2)
print ( id(emp_2))

