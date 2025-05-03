"""
what is pack value?
any iterable is consider a packed value.like string,list,tuple,set map etc.


what is unpacking ?

Unpacking is act of spliting packed value into individual value contained in a list or tuple etc.
"""

# unpacking list
a,b,c=[1,2,3]
print(a,b,c)

# unpacking tupel
a,b,c=(2,3,5)
print(a,b,c)

# unpacking string
a,b,c="vik"
print(a,b,c)

# unpacking dictionary
"""
when we unpacking dictionary it will unpack keys of dictionary not values
-dictionary and sets are unorder type so we don't know which key will be stored in x,y,z
"""

d={'a':1,'b':2,'c':3}
x,y,z=d
print(x,y,z)

# upacking dictionary values
x,y,z=d.values()
print(x,y,z)

# unpacking keys and vlues both
x,y,z=d.items()
print(x,y,z)
a,b=10,20

"""
 how swaping works in python.we have b,a at right hand side of assigment operator.first of all python will create tupel of memory address of b,a which is on right hand side.

 for exmaple
 a,b(148522488,152471125)
now a will have b's memory address and b will have a's memory address.
 """

a=id(b)
print(a)

# extended unpacking
lst=[1,5,1,4,8,6,3]
# put first element of lst in a and rest in b
a,*b=lst
print(f'a:{a} and b={b}')

# unpacking tuple
a,*b=(5,3,5,3,5)
print(f'a:{a} and b={b}')

# put firsst element in a ,secnod element in b and rest in c
"""
when you do slicing instead of unpacking in string you get string but in unpacking you get list as you can see c is list in ouput
"""
a, b, *c="python"
print(f"a={a}, b={b} and c={c}")


"""
we can not combine two set using + opertor set1+set2, but we can achive same thing using unpacking,{*set1,*set2}, or we can do union of two set we will get same result
"""
set1={5,8,9,3}
set2={8,2,1,6}
resutl={*set1,*set2}
print(f"result set={resutl}")


"""
combine two dictionary using unpacking
"""

d1={'a':1,'c':2,'c':3}
d2={'a':8,'d':4,'e':5,'f':6}
resutl={**d1,**d2}
print(f"result: {resutl}")
