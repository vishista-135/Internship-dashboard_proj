"""
Code Challenge 1
  Filename:
      radio.py
      Create a Radio class with characteristics and functionality discussed in class
      Create the object of the Radio class and start the radio and play a song

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

I should be able to 
Go to the market and buy a new Radio
Switch ON the radio
Set the mode to FM
Set the frequency to 102.2
Set the volume to 8
Listen to your song
Switch OFF the radio
Destroy the Radio
"""


"""
             Instance
              /    \
             /      \
            /        \
     variables      methods


              class
              /    \
             /      \
            /        \
     variables      methods

"""


# Instance variable has data which is unique to each instance 
# Why should you set the instance variable manually everytime
# It should have been set when we create the instance (object)
# Use __init__ method to create the instance variables ( constructor )
# create init method within the class 
# self syntax is how Python tells a method “make use of all
# the previously defined attributes and methods in this instance.”
# However, you never type self when you call the method.
# The init method. is called whenever you create an instance of the class


class Employee:
    def __init__(self, first, last, pay):
        print("Init is called")
        self.first = first
        self.last = last
        self.pay = pay 
        self.email=first.lower() + "." + last.lower() + "@gmail.com"
        # declaring simple variables within this method will have limited scope

emp_1 = Employee("Sylvester","Fernandes",50000)
emp_2 = Employee("Yogendra","Singh",60000)

print(id(emp_1))
print(id(emp_2))

print(emp_1.email)
print(emp_2.email)


# Adding Action (Methods) to the class using functions 
# Display Full Name of the employee 
# create method in the class

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.email=first.lower() + "." + last.lower() + "@gmail.com"

    def fullname(self):
        return "{} {}".format(self.first,self.last) 

emp_1 = Employee("Sylvester","Fernandes",50000)
emp_2 = Employee("Yogendra","Singh",60000)


print ( emp_1.fullname() )
print ( emp_2.fullname() )

# calling the methods from the class name, 
# but we need to pass the instance
# thats why the self object is passed

print (Employee.fullname(emp_1))
print (Employee.fullname(emp_2))




# Class Variables
# Variables which are shared among all the instance of the class 
# Class variable should be the same for all the instances of the class
# Which are the data which can be shared among all the employees

class Employee:
    # declare this in the class level 
        num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.email=first.lower() + "." + last.lower() + "@gmail.com"
        # we need to increase the value in the init method
        Employee.num_of_emps += 1
    
    def fullname(self):
        return "{} {}".format(self.first,self.last) 


emp_1 = Employee("Sylvester","Fernandes",50000)
emp_2 = Employee("Yogendra","Singh",60000)

# How can we access the class variables using the self object 
print (Employee.num_of_emps )
print (emp_1.num_of_emps )
print (emp_2.num_of_emps )



# Inheritance - Creating Subclasses
# Super Class or Parent Class or Base Class
# Sub Class or Child Class or Derived Class    



class Developer( Employee ) :
    pass

print(issubclass(Developer,Employee))

dev_1 = Employee ("Sylvester", "Fernandes",50000)
dev_2 = Employee ("Yogendra", "Singh",60000)

print (dev_1.email)
print (dev_2.email)


print(isinstance(dev_1,Developer))
print(isinstance(dev_1,Employee))


dev_1 = Developer ("Sylvester", "Fernandes",50000)
dev_2 = Developer ("Yogendra", "Singh",60000)

print ( dev_1.email )
print ( dev_2.email )

print(isinstance(dev_1,Developer))
print(isinstance(dev_1,Employee))


# This gives a clear picture of the inheritance and the variables 
# Method resolution order
print ( help( Developer ) ) 



# Overriding variables in subclass 
# Similarly methods can also be overided 


class Developer( Employee ) :
    raise_amount = 1.10
    # this will only affect the instances of the Developer class and not Employee class 

dev_1 = Employee ("Sylvester", "Fernandes",50000)

print (dev_1.pay)
dev_1.apply_raise()
print (dev_1.pay) 

dev_2 = Developer ("Sylvester", "Fernandes",50000)
print (dev_2.pay)
dev_2.apply_raise()
print(dev_2.raise_amount)
print (dev_2.pay) 




# Creating the initialize 

class Developer( Employee ) :
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang ):
        super().__init__(first, last,pay)
        self.prog_lang = prog_lang  



# this will only affect the instances of the Developer class and not Employee class 

dev_1 = Developer ("Sylvester", "Fernandes",50000,"Python")
dev_2 = Developer ("Yogendra", "Singh",60000,"Java")


print ( dev_1.email )
print ( dev_1.prog_lang )



# Multiple Inheritance in Python is possible

# Multilevel Inheritance in Python is possible

# Python does not have access modifiers. ( Private Public Protected )
# All members in a Python class are public by default.
# If you want to access an instance (or class) variable from outside the instance or class, 
# you are always allowed to do so. 
# The single underscore prefix for a member variable or 
# method is a commonly used convention to denote a protected method.
# The double underscore prefix for a member variable or 
# method is a commonly used convention to denote a private method.



# Multiple Inheritance

class A:
    pass

class B:
    pass

class C ( A, B):
    pass


# Multi Level Inheritance

class D:
    pass

class E(D):
    pass

class F(E):
    pass


# Python does not have access modifiers. ( Private Public Protected )
# All members in a Python class are public by default.
# If you want to access an instance (or class) variable from outside the instance or class, 
# you are always allowed to do so. 
# The single underscore prefix for a member variable or 
# method is a commonly used convention to denote a protected method.
# The double underscore prefix for a member variable or 
# method is a commonly used convention to denote a private method.


# Python does not have access modifiers. 
# There is no concept of modes in python (private, protcted, public )
# All members in a Python class are public by default.

"""
variable        public 
_variable_      protected concept
__variable__    private     
"""


