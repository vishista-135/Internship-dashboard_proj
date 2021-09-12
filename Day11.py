"""

list1 = [1,2,3,4,5]

#[1,4,9,16,25]

list2 = []
for item in list1:
   list2.append(item*item)

print (list2)

#shortcut
#list comprehension
[item**3 for item in list1]
print ([item*item for item in list1])

list1 = ['Amar','Akbar','Anthony']
#length of  each world in a list
#[4,5,7]


print ([len(name) for name in list1])



list1 = [10,20,30,40]

#[100,400,900,1600]
def squarevalue(x):
  return (x*x)

#print (list(map(squarevalue,list1)))




list1 = [1,2,3,4,5]

def iseven(x):
  return (x % 2 == 0)

print  (list(map(iseven, list1)))

print  (list(map(lambda x:x % 2 == 0, list1)))


print  (list(filter(lambda x:x % 2 == 0, list1)))





list1 = [1,2,3,4,5]

def fadd(x,y):
  return (x*y)

import functools

print (functools.reduce(fadd, [1,2,3,4,5]))

print (functools.reduce(lambda x,y: x+y, [1,2,3,4,5]))

"""

#dictionary


"""
name: Bharat
chem: 67
phy: 78
math: 87
"""
dict1 = {
  'name':'Bharat',
  'chem': {'midterm': {'mt1': 40, 'mt2':37}, 'final': 50},
  'phy':78,
  'math':87
}



#unpacking
x, y = divmod(32,5)

t1 = (1,2,3,4,5)

#tuples are read only

