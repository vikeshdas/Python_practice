
"""
Operation with integer

                output type
- int + int  :  int
- int - int  :  int
- int * int  :  int
- int / int  :  float 
- int ** int :  int 
"""

print(int("534"))

"""
Integer cunstructor and base
- Integer is a class in python and it has two cunstructor 
  1. int(x=0)
  2. int(x,base=0)

-Above both custructor you can see by print(help(int)): it will show you class representation.

-in int(x=0) cunstructor: you can pass any type of value in x and it will return int type of value of x .By default x is zero.By default it convert x into base 10
- In int(x,base=0): takes a value x and base ,it converts x into integer in base pased by user, by default base is zero
"""

# it will call int(x) cunstructor because we are not passing base
print(int("55")) # ouput will be 55(integer)

# convert float to integer
print(int(10.5)) #ouput: 10


# convert boolean to integer
print(int(True)) # ouput :1
print(int(False)) #ouput: 0


# convert integer to base 2,it allway takes string,can't convert non-string with explicit bas
print(int("101",base=2))


"""
Rational Number
-Rational numbers are fraction of integer number.A number which has finite number of number after decimal point and before the decimla point.
ex: 1/2, -22/7
in above example both numerator and denominator are integer
- 0.5 is also a rational number because it can be represented as 1/2

-Rational number can be represent in python using the Fraction class in fraction model
"""
from fractions import Fraction

x=Fraction(3,4)
print(x)
