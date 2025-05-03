"""
When we define a variable like (name="vikesh") a memory block will be occupied for the string "vikesh" and variable name will refference to the memory address where string "vikesh" is stored.
"""
# example of refernce address of a variable
name="vikesh"

# id will return base 10 number you can convert it inot hex number
print(id(name))
print(hex(id(name)))
print("-----------------------")

"""
Refrence count

"""

"""
circular reference 

lets say we have 
    [Object A]------------>[Object B]
"""


"""
Python is dynamic type means we do not define type of variable unlike other languge for exmaple in c++ we define a varibale like (int var). But in python we do not need to define type of variable 

in python we define ,below var store integer type
var=40
and letter we can change type to string 
var="vikesh"

how it works behind the scene
step1: var ----------->[in memory(40)]

when we change var 40 to "vikesh" it creates new object in memory 
step2: var -------------> [in memory(vikesh)] 
and instead of point  [in memory(40)] it will start pointing 

"""

var=40
print(type(var))

var="vikesh"
print(type(var))
print("-----------------------")


"""
- mutable and immutale 

How object in memory exist:
in memory block an object contains two things type of varaibel and state(called data)

this is memory block ----> [type and data(state)] 0x125544

-In mutable when internal state of variable change it is called mutable .examples are (list,sets,dictionary,User define class)

-In immutable when internal state of variabel can not be changed.(int,float,bool,string,tuple,frozen sets,User define class are immutable)
"""

"""
tupel are immutable elements can not be inserted,updated or deleted
"""
t=(1,2,3)

"""
In below exmaple tuple is immutable but element inside tuple is lsit which is mutable which can be change,so in below case tuple became mutable.
"""
a=[4,5]
b=[5,2]
tup=(a,b)
print(id(tup)) #memory address is same 2058178132032 as below
a.append(8)
print(id(tup)) #memory address did not change 2058178132032

