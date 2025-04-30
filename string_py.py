# string is immutable data type we can not update a character in string at a index

st="my name is vikesh"

#it will give : TypeError: 'str' object does not support item assignment
try:
    st[1]='5'
except TypeError:
    print(TypeError)
print(st)
print(id(st))

# it woul be abel to modify st but it will create new object ,dose not modify existing one.
st="XYZ"
print(st)
print(id(st))


# some methods of string

name="VIKESH"

# lower()
print(name.lower())
#upper()
print(name.upper())

# capitalize(): it make first character capital rest in small.
print(name.capitalize())

# split(): convert string to list and splite at a point defined by programer
question="what is your name"
# by default split() method split at space
print(question.split())

# split at 'a'
print(question.split('a')) 

