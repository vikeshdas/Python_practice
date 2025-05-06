"""
There were lots of problem with floatin point number like 

-float 0.1 :  it may have infinite binary expression like (0.0000011100000...)

-In backing application we can not use float for represent amout as 0.1 will represnt infinite expression and it is not acceptable in banking applicaiton.

-but decimal number 0.1 have finite binary expression 0.1

-why do we not use fraction 1/10,well fraction is slower when it comes to arithmetic operation,compare to float its much slower

-Above problem solved by decimla getcontext()
The getcontext() function is a crucial part of Python's decimal module, which provides decimal floating-point arithmetic with user-definable precision. This function allows you to access and modify the current decimal arithmetic context

-getcontext() returns the current context for decimal operations, which is a set of parameters that govern:
1. Precision (number of significant digits)
2. Rounding rules
3. Exponent limits
4. Flags for exceptional conditions
-precision: Controls number of significant digits (default is 28),user can modify it by getcontext().prec = 6 limits calculations to 6 significant digits
-Rounding: determines rounding behavior (default is ROUND_HALF_EVEN),Other options: ROUND_UP, ROUND_DOWN, ROUND_CEILING, etc.
-traps: Controls which conditions raise exceptions,example:Controls which conditions raise exceptions
"""

from decimal import Decimal, getcontext, ROUND_DOWN, ROUND_UP

getcontext().prec = 4
result = Decimal(1) / Decimal(7)  # 0.1429

# changing rounding module
getcontext().rounding = ROUND_DOWN
result = Decimal(1) / Decimal(3)  # 0.3333 (instead of rounding up)

"""
where precision exactly affect ,It does not affect in creation of decimal ,it affect in arithmetic operation 
"""
import decimal
with decimal.localcontext() as ctx:
    ctx.prec = 2
    a=Decimal(0.12345)
    b=Decimal(0.12345)
    print(f"a: {a} and b:{b}")

"""
Arithmetic operation with decimal
"""
print(Decimal(-135//4))


"""
0.1 inside Decimla treating as a float.
"""
d = Decimal(0.1)
print(d) #0.1000000000000000055511151231257827021181583404541015625

# cunstructing from string
d = Decimal('0.1')   #ouput 0.1
print(d)

"""
decimal takes more memory then floats and its slower then float
"""
import sys

a=3.1425
b=Decimal('3.1525')

print(f"size of float: {sys.getsizeof(a)}, size of decimal:{sys.getsizeof(b)}")