print("*************************************************************")
# print  0 and one in binary of n and its length
n=-37
print(bin(n))
print(n.bit_length())
print("*************************************************************")
# if x is nonzero, then x.bit_length() is the unique positive integer
# k such that 2**(k-1) <= abs(x) < 2**k.
x=37
k=x.bit_length()
print(k)
print(2**k-1)
print(abs(x))
print(2**k)

print("*************************************************************")
# If x is zero, then x.bit_length() returns 0
y=0
l=y.bit_length()
print(l)

print("***********************************************************")
n=18
number_of_ones=n.bit_count()
print(bin(n))
print(number_of_ones)

print("***********************************************************")
# iether n is integer or not ,below method only work with float not with integer
n=0.20
print(n.as_integer_ratio())
print(n.is_integer())

print("***********************************************************")
# i have initialize lists with 0 of lenght 3 all three index will have value 0 of same reference
lists = [[0]] * 3
print(lists)

print("\n*****below function work with all mutable datatatype*****")
s = [1, 2, 3]
t = [4, 5, 6]
# it will append all element of t to x
s.extend(t)
print(s)

# remove element from s
poped_element=s.pop()
print(poped_element)
# pop element from a particular index
poped_element=s.pop(2)
print(poped_element)
# remvoe first occurence of x
lst=[1,2,3,4,5,6,7,8,9,10,11,12]
lst.remove(2)
print("s",lst)
print("***********************************************************")


# Lists are mutable sequences, typically used to store collections of homogeneous items 
lst=list([1,2])
print(lst)

# difference between sort() and sorted()->sort modify original list but sorted return new list with sort of original list.
lst=[8,2,6,2]
print(sorted(lst))
print(lst)

# Tuples are immutable sequences, typically used to store collections of heterogeneous data .tuples are immutable sequences, which means once they are created, their content cannot be changed.
# Creating a tuple to store information about a person
person = ("John", 30, "New York")
print(person[0])
for item in person:
    print(item)
    
# range() is a built-in function used to generate a sequence of numbers. It's commonly used in loops and when creating lists containing arithmetic progressions of integers. The range() function can take one, two, or three arguments:

#  range object will always take the same (small) amount of memory, no matter the size of the range it represents
list(range(10))
# op-[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(1, 11))
# op- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(range(0, 30, 5))
# op- [0, 5, 10, 15, 20, 25]
list(range(0, 10, 3))
# op- [0, 3, 6, 9]
list(range(0, -10, -1))
#op- [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
list(range(0))
# []
list(range(1, 0))
# []



print('************set and firozen set**********************')
#   Sets are mutable, meaning you can add or remove elements from them after they are created.Frozensets, on the other hand, are immutable. Once created, you cannot add or remove elements from them, nor can you modify the elements already present in the frozenset.

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements to a set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Removing an element from a set
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}

# Checking membership in a set
print(4 in my_set)  # Output: True

# Length of a set
print(len(my_set))  # Output: 5

# Iterating over elements in a set
for element in my_set:
    print(element)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

# Difference
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

print("**************firozen st*********************************")
# Creating frozensets
frozenset1 = frozenset({1, 2, 3, 4})
frozenset2 = frozenset({3, 4, 5, 6})

# copy(): Returns a shallow copy of the frozenset
copy_frozenset = frozenset1.copy()
print("Copied frozenset:", copy_frozenset)

# difference(): Returns the difference of two or more sets as a new frozenset
difference = frozenset1.difference(frozenset2)
print("Difference:", difference)

# intersection(): Returns the intersection of two or more sets as a new frozenset
intersection = frozenset1.intersection(frozenset2)
print("Intersection:", intersection)

# isdisjoint(): Returns True if the frozenset has no elements in common with another set
disjoint = frozenset1.isdisjoint(frozenset2)
print("Disjoint:", disjoint)

# issubset(): Returns True if the frozenset is a subset of another set
subset = frozenset({1, 2}).issubset(frozenset1)
print("Subset:", subset)

# issuperset(): Returns True if the frozenset is a superset of another set
superset = frozenset1.issuperset({1, 2})
print("Superset:", superset)

# symmetric_difference(): Returns the symmetric difference of two sets as a new frozenset
symmetric_difference = frozenset1.symmetric_difference(frozenset2)
print("Symmetric Difference:", symmetric_difference)

# union(): Returns the union of sets as a new frozenset
union = frozenset1.union(frozenset2)
print("Union:", union)

# __contains__(): Returns True if a specific element is present in the frozenset
contains = 3 in frozenset1
print("Contains 3:", contains)

# __iter__(): Returns an iterator object for the frozenset
print("Iterating over frozenset1:")
for element in frozenset1:
    print(element)


print("****************Dictionary and its methods************")
# clear(): Removes all key-value pairs from the dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.clear()

# copy(): Returns a shallow copy of the dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
copy_dict = my_dict.copy()
print(copy_dict) 

#   fromkeys(): Creates a new dictionary with keys from a sequence and values set to a default value.
keys = ['a', 'b', 'c']
default_value = 0
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)

#   get(): Returns the value associated with a key, or a default value if the key is not present
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.get('b')
print(value)  # Op- {'a': 0, 'b': 0, 'c': 0}

#   items(): Returns a view object that displays a list of key-value pairs
my_dict = {'a': 1, 'b': 2, 'c': 3}
items = my_dict.items()
print(items)  # Output- 2

# keys(): Returns a view object that displays a list of keys.
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()
print(keys)  # Op- (['a', 'b', 'c'])

#   pop(): Removes and returns the value associated with a specified key
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.pop('b')
print(value)  # Op- 2


# popitem(): Removes and returns the last inserted key-value pair
my_dict = {'a': 1, 'b': 2, 'c': 3}
key, value = my_dict.popitem()
print(key, value)  # Op- 'c', 3

# setdefault(): Returns the value of a key, or sets it to a default value if the key is not present
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.setdefault('d', 4)
print(value)  # Op- 4


# update(): Updates the dictionary with key-value pairs from another dictionary or iterable
my_dict = {'a': 1, 'b': 2}
other_dict = {'b': 3, 'c': 4}
my_dict.update(other_dict)
print(my_dict)  # Op- {'a': 1, 'b': 3, 'c': 4}

# values(): Returns a view object that displays a list of values
my_dict = {'a': 1, 'b': 2, 'c': 3}
values = my_dict.values()
print(values)  # Op- dict_values([1, 2, 3])
