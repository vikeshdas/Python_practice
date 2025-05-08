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
tup[0].append(8)
print(id(tup)) #memory address did not change 2058178132032


"""
When we say "immutable objects are  safe from unintended side effects," it means that modifying a mutable object (like lists, dictionaries, or sets) in one part of your code can unexpectedly affect other parts that reference the same object.

In below code var which is out side of the process and s which is inside process function are pointing to same memory address because in python function call is pass by refrence.

when interpreter reach to process and variable s is modified, since it is immutable type now it will point to new memory address.Now s and var pointing to two different memory address.
"""

def process(s):
    s=s+"world"
    return s

var="hello"
process(var)

"""
"mutable objects are not safe from unintended side effects," it means that modifying a mutable object (like lists, dictionaries, or sets) in one part of your code can unexpectedly affect other parts that reference the same object.
"""


print("---------------------------------------------------------------")
"""
-What is Interning
lets say we create variable a=10 and assigned value 10 then created onother variable b=10 it is also assigned 10 , in this case a and b will have same reference in memory,means a and b will point to same object in memory
"""
a=10
b=10
print(f"a: {id(a)} and b: {id(b)}")
print(a==b)# True
print(a is b)#True

"""
But if we assigned a=500 and b=500 in this case a and b will point to different memory address, both will not share same memeory.

-we can compare memory address of two varable using (== or is)if value is between [-5,256] then reference will be share otherwise a new object will be created for both a and b.

-So interning is python optmization it is memory or speed optmization because it is not creating two different object it is reusing object.It saves memory and time.
"""
x=6000
y=6000
print(x==y)

print("-------------------------------------------------------------------")
"""
Not all string are inter by python,but we can inforce a string to be interning by using the sys.intern() method.
"""
s1="vikesh"
s2="vikesh"
print(s1==s2) #True == compare two string character by chacrater
print(s1 is s2) # is : compare memory address


str1="hello world"
str2="hello world"
print(id(str1),id(str2))

# enforce string to be interning
import sys
str1=sys.intern("the quick brown fox")
str2=sys.intern("the quick brown fox")
print(str1==str2)