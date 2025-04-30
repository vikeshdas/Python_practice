# By default, an object is  true. if a class defines  a __bool__() method that returns False 
# or a __len__() method that returns zero in these two case object will be Fasle otherwise By default it will 
# be True.

class MyClass:
    def __bool__(self):
        return False

class MyList:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

dic={'name':"vikesh"}
if dic:
    print('True')
else:
    print('False')

obj2 = MyList()
if obj2:
    print("True")
else:
    print("False")

obj1 = MyClass()
if obj1:
    print("True")
else:
    print("False")


print('********************************for None and Fasle*****************************************************')
# None and Falase is allways false
val=None
if val:
    print('True')
else:   
    print('False')

val=False
if val:
    print('True')
else:
    print('False')
print('*********************************for zero value of any type*********************************************')
# zero value of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1) it will allwasy return false
val=0
if val:
    print('True')
else:
    print('False')

val=0.j
if val:
    print('True')
else:
    print('False')

print('*************************************empty sequence and collection **************************************')
str=''
lst=[]
dic={}
st=set()
rang=range(0)

if str:
    print('True')
else:
    print('False')

if lst:
    print('True')
else:
    print('False')

if dic:
    print('True')
else:
    print('False')

if st:
    print('True')
else:
    print('False')

if rang:
    print('True')
else:
    print('False')

print('*************************************boolean operation and,or **************************************')

# if x is true then print x else y
x=0
y=5
print(x or y) #output 5

x=0
y=0
print(x or y)#output 0

x=0.0 #False zerp os allwasy False
y=0.1
print(x and y)

# not x:- if x is false, then True, else False
x=[]
if not x:
    print('True')
else:
    print('Flase')

a=5
b=4
print(not a==b)
# or 
print(not (a==b))

# syntax error
# print(a== not b)

print('*******************************************Comparisons *******************************************************')

x=50
y=10
z=4
print(x>y and y<z) #output: False
#     or
print(x>y<z) 

# If you compare objects that belong to different data types, they will always be considered unequal
# string and integer does not belongs to same numeric type.strings belong to the "sequence" type
str='21'
integ=21
print(str==integ)

# it will give us True becuase integer and float belongs to same numeric type .so here type cast is being performed internally

x=1
y=1.0
print(x==y)

# below code will give error TypeError: '<' not supported between instances of 'int' and 'complex'
# print(3 < 5 + 2j)
# so <=,>=,== etc are used for used for certain object


# is comparator:is used to compare the memory address of two object if both has same memory address return true
# else return false
lst_1=[1,2]
lst_2=[1,2]
print(lst_1==lst_2) #Trues
print(lst_1 is lst_2) #False
print(lst_1 is not lst_2) #apposit method of is

print('*******************************************custome equal *************************************************')

# if you create two instances of a class in Python, if you use == operator ot compare both instace it
# will give us Fallse even if they contains same attributes and data.when we use == operator with user 
# define class it compares memory address of the objects not values.if you want instances of your class
#  to compare as equal based on some criteria you define, you can override this default behavior by 
# defining the __eq__() method within your class.

class MyClass:
    def __init__(self, value):
        self.value = value

obj1 = MyClass(10)
obj2 = MyClass(10)

# without __eq__() method, instances are not equal
print(obj1 == obj2)  # Output: False

# defined __eq__() method for custom equality comparison
class MyClassWithEq:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return isinstance(other, MyClassWithEq) and self.value == other.value

obj3 = MyClassWithEq(10)
obj4 = MyClassWithEq(10)

print(obj3 == obj4)  # Output: True

print('*******************************************custome methods *************************************************')
# By default, instances of a class in Python cannot be ordered with respect to other instances of the same
# class or other types of objects. This means you cannot directly compare instances of the class using
# comparison operators like <, <=, >, or >=.you can define ordering methods within the class to specify 
# how instances should be ordered with respect to each other using below custome methods 
# __lt__(), __le__(), __gt__(), and __ge__() (in general, __lt__() and __eq__()

# The behavior of the is and is not operators cannot be customized; also they can be applied to any two objects 
# and never raise an exception

class CustomeMethods:
    def __init__(self,value):
        self.value=value

    def __lt__(self,other):
        return self.value<other.value
    
    def __le__(self,other):
        return self.value<=other.value
    
    def __gt__(self,other):
        return self.value>other.value

x=CustomeMethods(10)
y=CustomeMethods(20)
print(x<y)
print(x<=y)
print(x>y)

print('*******************************************is(comparator) with integer *************************************************')
x=5
y=5
print(x is y) # is also work with other type with user define class.

print('*******************************************in and not method *************************************************')
# in and not works only with that are iterable.like list ,tuple,set,dictionary or whichimplement the __contains__() method
# in is used to check that if a value is exist in a colleciton or not if value ixist it return true else false

lst=[1,2,3,4]
str="my name is vikesh"
print(3 in lst)
print('vikesh' in str)
print('is vikesh' in str)
print('x' in str)

# not in is appositve of in 
print('x' not in str)


# by default (ns) does not work with user defined class .if you want to use (in) in user defined class you have to 
# write __contains__() method

print("***************************************************************Numeric Types*****************************************************************************")
# There are three distinct numeric types: integers, floating point numbers, and complex numbers
# In addition, Booleans are a subtype of integers
# Integers have unlimited precision.
# Complex numbers have a real and imaginary part, which are each a floating point number.To extract these parts from a complex number z, use z.real and z.imag

# below Operations works on all numeric type except complex

# sum 
int_num_1=5
int_num_2=3

float_num_1=2.6
float_num_2=4.3

res=int_num_1+int_num_2
print(res)

res=float_num_1+float_num_2
print(res)

# subtract
int_num_1=5
int_num_2=3

float_num_1=2.6
float_num_2=4.3

res=int_num_1-int_num_2
print(res)

res=float_num_1-float_num_2
print(res)

# product
int_num_1=5
int_num_2=3

float_num_1=2.6
float_num_2=4.3

res=int_num_1*int_num_2
print(res)

res=float_num_1*float_num_2
print(res)

# quotient
int_num_1=6
int_num_2=3

float_num_1=2.6
float_num_2=4.3

div_res=int_num_1/int_num_2
print(div_res)

res=float_num_1/float_num_2
print(res)


# floored
int_num_1=6
int_num_2=3

float_num_1=2.6
float_num_2=4.3

div_res=int_num_1//int_num_2
print(div_res)

res=float_num_1//float_num_2
print(res)

# remainder
int_num_1=6
int_num_2=3

float_num_1=2.6
float_num_2=4.3

div_res=int_num_1%int_num_2
print(div_res)

res=float_num_1%float_num_2
print(res)

# x converted to integer
print(int(2.3))

#converted to floating point
print(float(5))

# generate imaginary number
img=complex()
print(img)

img=complex(2.3,5.j)
print(img)


#  The complex conjugate of a complex number a+bi  is given by a-bi where a and b are real numbers and 
# i is the imaginary unit

c = 3 + 4j  # Define a complex number
conj_c = c.conjugate()  # Compute its complex conjugate

print(conj_c)

# The divmod(x, y) function in Python returns a tuple containing the quotient and remainder of dividing x by y
# touple contains (x // y, x % y)
result = divmod(10, 3)
print(result)

# power of x,y
print("power",pow(2,3))
# or
print("power",2 ** 3)

# In division
# If both operands are of type int, the result of integer division will be of type int.
# If one or both operands are of type float, the result of integer division will be promoted to type float.
# above case does not match with complex number 
c1 = 3 + 4j
c2 = 2 - 1j
# Convert complex numbers to floats using abs() and perform division-like operation
result = c1 / c2
print("result",result)

# float also accepts the strings “nan” and “inf” with an optional prefix “+” or “-” for Not a Number (NaN) and positive or negative infinity
float_number="vikesh"
try:
    print(float(float_number))#it will give error because you are trying to convert string to float which is not possible
except ValueError as e:
    print(e)
# But in python there are few string which are able to convert into flaot like "NaN","inf","+","-".
nan_float = float("nan")        #Not a number
print(nan_float)
inf_float = float("inf")        #infinity
print(inf_float)
neg_inf_float = float("-inf")   #negetive infinity
print(neg_inf_float)
pos_nan_float = float("+nan")   #positive not a numer
print(pos_nan_float)
neg_nan_float = float("-nan")   #negetive not a number
print(neg_nan_float)

# Python defines pow(0, 0) and 0 ** 0 to be 1, as is common for programming languages
# The numeric literals accepted include the digits 0 to 9 or any Unicode equivalent (code points with the Nd property).

# float also accepts the strings “nan” and “inf” with an optional prefix “+” or “-” for Not a Number (NaN)
# and positive or negative infinit


# both integers (int) and floating-point numbers (float) support certain operations in common, as they 
# are both considered subtypes of the numbers.Real abstract base class in Python.below are common method for 
# int and float
import math
# trucate jut remove the decimal part
print(math.trunc(-4.92)) # -4

# returns the largest integer less than or equal to x
print(math.floor(-4.92)) #-5

# roudof a integer till 3 decimla place
print(round(4.92514789325,3)) # 4.925

print("**********************************************Bitwise Operations on Integer Types********************************************")
# Bitwise operations only make sense for integers.he priorities of the binary bitwise operations are all lower than the numeric 
# operations and higher than the comparisons; the unary operation ~ has the same priority as the other unary numeric operations (+ and -)

x=3
n=4
print(x << n) # ->x shifted left by n bits
print(x >> n) #x shifted right by n bits

# Negative shift counts are illegal and cause a ValueError to be raised
# for exmaple print(x >> -3)

# A left shift by n bits is equivalent to multiplication by pow(2, n)
# A right shift by n bits is equivalent to floor division by pow(2, n)

print('---------------------------------------------------  int.bit_length() ------------------------------------------------------------')
# Return the number of bits necessary to represent an integer in binary, excluding the sign and leading zeros:
x=-37
print(bin(x))
print(x.bit_length())
# if x is nonzero, then x.bit_length() is the unique positive integer k  such that 2**(k-1) <= abs(x) < 2**k

print('-------------------------------------------------------- int.bit_count() ----------------------------------------------------------')
# Return the number of ones in the binary representation of the absolute value of the integer. This is also known as the population count. Example
# n=19

# print(bin(n))
# print(n.bit_count())

print('-------------------------------------------------------- is_integer() ----------------------------------------------------------')
# is_integer chekc if a value with decimal is a integer or no like 5.0 is integer so it will print True,8.2 is float is it will print False
num=5.0 
print(num.is_integer()) #this method does not work with integer value it only work with float value,if num=5 then it will not work

num=8.2
print(num.is_integer())

print("******************************************************__iter__()**********************************************************************")
# it returns the iterator object.this method allow both iterator and container to use for and in statement .
# The .__iter__() method of an iterator typically returns self, which holds a reference to the current object: the iterator itself.
# if we define below method in any custom class and then we call this function then it will return object of that class.
def __iter__(self):
    return self
print('***********************************************__next__()*******************************************************************************')
# returns the next item from the iterator if there are not further item it will rainse StopIteration exception
print("************************************************** generator ******************************************************************************")
# In Python, an iterator is an object that allows you to iterate over collections of data, such as lists, tuples, dictionaries, and sets.
# Python iterators must implement a well-established internal structure known as the iterator protocol
    # A Python object is known as an iterator when it implements two special methods (__iter__() and __next__()) known as the iterator protocol
    # These two methods make Python iterators work   
    # So, if you want to create custom iterator classes, then you must implement the thse two method in your class.
    # Generator functions are special types of functions that allow you to create iterators using a functional style

# Generator Function: A generator function is a special type of function in Python that generates a sequence of values lazily,
# on-the-fly. It uses the yield keyword to yield values one at a time, rather than returning them all at once like a regular
# function. When a generator function is called, it returns a generator object.Iterator Protocol: The iterator protocol is a
# Python protocol that defines how objects can support iteration. It requires objects to implement two methods: __iter__() 
# and __next__(). Objects that implement these methods are considered iterable and can be iterated over using a for loop or
# by calling the iter() and next() functions.The paragraph states that when you create a generator function in Python,
# it automatically returns an iterator that follows the iterator protocol. In other words, the generator object returned
# by the generator function supports iteration because it implements the __iter__() and __next__() methods required by the
# iterator protocol. This means you can iterate over the values generated by the generator using a for loop or by calling 
# the next() function on the generator object


def sequence_generator(sequence):
    for item in sequence:
        yield item

print(sequence_generator([1, 2, 3, 4]))             #<generator object sequence_generator at 0x108cb6260>

for number in sequence_generator([1, 2, 3, 4]): 
    print(number)                                   # output 1 2 3 4

# In below exmaple as you can see i have yield only 10 (one item) but still it become iterlabel object ,if you try to apply for loop 
# on integer object it will give you error that iteger is not a iterable object
def sequence_generator():
        yield 10

temp=sequence_generator()
for item in temp:
    print(item)

# With iterators and generators, you don’t need to store all the data in your compter’s memory at the same time.

print('************************************************************* Sequence data Types ************************************************************')
# There are three basic sequence types: lists, tuples, and range objects
# The below functions are supported by most sequence types, both mutable and immutable

s=[1,2,3,4,8]

print(3 in s) #check if 3 is in s  
print(-2 not in s) #check if -2 is is not in s

print('_________________________________________________Concatination___________________________________________________________________________')
s=[1,2,3,4,5]
t=[1,2,3,4,5]
print(s+t)

# equivalent to adding s to itself 3 times
print(s*3)

# smallest element of s
print("smallest element",min(s))

# s.index(x[, i[, j]]) ->index of the first occurrence of x in s (at or after index i and before index j)
print("index",s.index(2,0,5))

# total number of occurrences of x in s
s=s*3
print("s->",s)
print("count",s.count(1))

# if we comparing two sequence then both should be of the same type with same length,for example we compare list with dictionary there is no means
s=[1,2,3,4]
t=[1,2]
print("s==t",s==t)


# While the in and not in operations are used only for simple containment testing in the general case, some specialised
# sequences (such as str, bytes and bytearray) also use them for subsequence testing:

print("in for string","gg" in "eggs")

#  s[i:j].index(x), find x in a list wihtin the range ,it does not copy the list 
print("index",s[0:3].index(2))

print('**********************************************************funcitons for Mutable Sequence ******************************************************')
# following functions are defined on mutable sequence types

print('_________________________________________________________________________List__________________________________________________________________')
# delete an element from sequence
s=[1,2,3,4,5]
del s[1:2]
print(s)

# delete an item using a key
dic={1:'a',2:'b'}
del dic[1]
print(dic)

# remove all elements
s.clear()
print("after clear s-",s)

# extend method is used to combine two list ,difference betwee extend() and + operator is that extend() make changes in original list 
# it will not create new list ,+ operator create new list

s=[1,2,3,4]
t=[5,6,7]
print(s.extend(t))
print("s",s)
print("t",t)
# + operator 
print(s+t)
print("s",s)
print("t",t)

# s.insert(i, x) insert x in s at index i
s[3]=100
print("s",s)

# s.pop() or s.pop(i) retrieves the item at i and also removes it from s
print(s.pop()) #remove item from last
print("s",s)
print(s.pop(3))
print("s",s)

# s.remove(x) remove the first item from s where s[i] is equal to x
s.remove(1)
print("s",s)

# s.reverse()
s.reverse()
print("s",s)

# Lists are mutable sequences, typically used to store collections of homogeneous items

# sorted() and sort() are both used for sorting lists in Python
# sorted()  does not modify the original list; instead, it returns a new sorted list
# You can use sorted() with any iterable, not just lists

# The sort() method is a list method that sorts the elements of a list in place, modifying the original list
# It sorts the list in ascending order by default, but you can specify a custom sorting order using the reverse parameter.
# sort only works with list

print("_______________________________________________________________touple_____________________________________________________________________")


print('_______________________________________________________________Range_______________________________________________________________________________')

# The range type represents an immutable sequence of numbers and is commonly used for looping a specific number of times in for loops


#1 is start point and  100 is end point and 5 is step ,if start is empty is is set bydefualt 0 ,if step is mepty then default is 1,step can not accept 0
for item in range(1,100,5): 
    print("item",item)

# The advantage of the range type over a regular list or tuple is that a range object will always take the same (small) amount
# of memory, no matter the size of the range it represents (as it only stores the start, stop and step values, calculating
# individual items and subranges as needed

r = range(0, 20, 2)
print("r",type(r))

print('************************************************************** string ********************************************************************************')
# string in python is immutable datatype once a string is created can not be chnaged at rung time.

# When you write two string literals (text enclosed in quotes) next to each other with only whitespace
# (spaces, tabs, or newlines) between them, Python combines them into a single string literal

str="spam " "eggs" #it becomes in python "spam eggs"
print(str)

# 
normal_string = "This is a normal string with a newline: \nThis is the second line"
raw_string = r"This is a raw string with a newline: \nThis is not a second line"

print("noram_string=>",normal_string)
print("row_string=>",raw_string)

print('\n')
# In Python, strings are sequences of characters. Each character in a string is itself a string of length 1.
# So, when you index a string, like s[0], you're getting back a substring containing a single character, 
# not just the character itself. Similarly, when you slice a string, like s[0:1], you're also getting a substring of length 1.

str="vikesh"
sub_str=str[0]
print("is it string ",type(sub_str),'\n')

name=str.join('das')
print('vikesh',name,'\n')
print('str',str)

# Methods of the string 

# str.capitalize()->return copy ,it makes first charactor capital letter rest remain same.
text="my name is vikesh"

print("text after capitalize: ",text.capitalize())

# str.casefold()

# lower() method converts a string to lowercase, it may not handle all cases of case folding,
# especially for characters in languages other than English
# casefold() is more aggressive in this regard. It not only converts characters to lowercase
# but also handles special cases, such as the German letter 'ß' (Eszett), which is equivalent
# to "ss" in uppercase. Since 'ß' has no uppercase equivalent, lower() would leave it unchanged,
# whereas casefold() converts it to "ss"
# For example, in Turkish, the uppercase equivalent of 'i' is 'İ', and the lowercase equivalent
# of 'I' is 'ı'. While lower() would not handle this correctly, casefold() does, as it is intended
# to remove all case distinctions in a string
txt='ß'#latin latter
print('casefold: ',txt.lower())
print('casefold: ',txt.casefold())

# str.center()
# center method put your string in center add padding both sides left and right of the string 
name="vikesh"
print(name.center(8,'*')) #it will put 'vikesh' in center it will give 2 padding 1 left and 1 right,why only two becuase we mention 8,2 padding and 6 character in 'vikesh'
#ouput =*vikesh*


# str.count(sub[, start[, end]])
# above method is used to find the number of occurence of a subsring in a string ,substring should not be overlaping.
text="my name is vikesh"
print("count->",text.count('is'))
print("count->",text.count(''))#if you searching for mepyt string it will return number of character+space+1=18


# str.encode(encoding='utf-8', errors='strict')
# convert string to bytes,default encoding='utf-8'
text = "Hello, world!"

encoded_bytes = text.encode(encoding='utf-8')
print(encoded_bytes)


# # str.endswith(suffix[, start[, end]])
# Return True if the string ends with the specified suffix, otherwise return False. suffix can also be a tuple of suffixes to look for.
# With optional start, test beginning at that position. With optional end, stop comparing at that position.

filename = "document.txt"

result = filename.endswith(".txt")
print(result)  # Output: True


def placeAtCorrectPosition(start,end,items):
    value=items[start]
    start_pointer=start
    end_pointer=end
    while(start_pointer<=end_pointer):
        if items[start_pointer]<value:
            start_pointer+=1
        if item[end_pointer]>value:
            end_pointer-=1
        if items[start_pointer]>value and items[end_pointer]<value:
            items[start_pointer],items[end_pointer]=items[end_pointer],items[start_pointer]
    
    
    items[currect_position],items[end]=items[end],items[currect_position]
    print("currect_position",currect_position)
    print("items",items)
    return currect_position

def performOperation(start,end,items):
    if start>=end:
        return
    item_place=placeAtCorrectPosition(start,end,items)
    performOperation(item_place+1,end,items)
    performOperation(start,item_place-1,items)

items=[3, 6, 8, 10, 1, 2, 1]
n=len(items)
performOperation(0,n-1,items)
print(items)