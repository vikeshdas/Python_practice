
"""
name tuple is subclass of tuple,ussulay we can access data from tuple using index.But name tupel allow us to access data of tuple using name(key).This makes code more readable.Named tuple is defined in colleciton module.

-name tuple can be access by index too.

-namedtuple() returns a new class called 'Person'
Person = namedtuple('Person', ['name', 'age', 'job'])

-field name can not be start with underscor(_x)
Point = namedtuple('Point', ['_x', '_y'])

"""

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p = Point(10, 20)
print(p.x)  # 10
print(p.y)  # 20

# list key(field)
print(f"fields: {p._fields}") 

# create a new instance with some fields replaced
p2 = p._replace(y=99)
print(f"p2:{p2}")
print(f"p:{p}")

print("id of p:",id(p))
print("id of 2:",id(p2))


# unpacking named tupel
Point = namedtuple('Point', ['name', 'age','city','gender'])
p=Point("vikehs",27,"new delhi","Male")

name,age,city,gender=p
print(f"name: {name},age: {age},city: {city}, gender: {gender}")


"""
Modifying and extending named tuple,tuple is immutable means if we try to mdify it will create new instance.just like string.
"""
Point2D=namedtuple('Point2D','x y')
pt=Point2D(10,20)
print(f"{pt.x},{pt.y}")
print(id(pt))

# updating pt with new namedtuple ,its actually changed the id 
pt=Point2D(100,pt.x)
print(f"{pt.x},{pt.y}")
print(id(pt))

"""
'symbol year month day open high low close': each space treated as comas(,)
"""
Stock=namedtuple('Stock','symbol year month day open high low close')

#output: ('symbol', 'year', 'month', 'day', 'open', 'high', 'low', 'close')
print(Stock._fields) 

"""
unpacking namedtupel to update values of named tuple  
"""
res=Stock("DJIA",2025,1,25,26,313,26,458)

*values, _=res
print(values) #['DJIA', 2025, 1, 25, 26, 313, 26]

values.append(26_393)
print("values",values)

new_res=Stock(*values)
print(f"new_res: {new_res}")


"""
we can also use slicing with named tuple 
"""
print(new_res[:7])

"""
In above some exmples we are trying to modify namedtupel values and are able to do it.But if we want to updated value in middle in named tuple ,it will become complex if we use above approach ,There is build in mathod to do that which is _replace mathod
"""
new_res=new_res._replace(year=2026)
print(new_res)


"""
extend fields in namedtuple
"""
Point2D=namedtuple('Point2D','x y')
print(Point2D._fields)
print(Point2D._fields+('z',))



