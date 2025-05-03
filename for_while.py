"""
A for loop in Python allows you to iterate over any iterable object, which includes.
as you can see below we have set  which is iterable and we are using for loop to iterate over it 
"""

st={5,8,6,3,2}
for item in st:
    print(f"itme: {item}")


"""
can we do same thing with while loop yes we can but code will become comples,we need to manualy convert set into iterator and call next() and StopIteration method of iterator .so we can say while loop is not made for iterate over iterator.

-The for loop in Python has built-in handling of iter()/next() and StopIteration
"""
iterator = iter(st)  

while True:
    try:
        item = next(iterator)  
        print(item)
    except StopIteration:  
        break

