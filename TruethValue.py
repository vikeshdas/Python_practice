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
float_number="NaN"
print(type(float(float_number)))

print(float(float_number))