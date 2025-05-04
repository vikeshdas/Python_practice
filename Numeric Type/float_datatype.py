
num=float(10)
print(num)

# string to float
print(float('10.5'))


# num_1 should be equla to num2 but it is printing False
num_1=0.1+0.1+0.1
num_2=0.3
print(num_1==num_2)

print(f"num_1: {format(num_1,'.25f')}, nume_2: {format(num_2,'.25f')}")
"""
output: num_1: 0.3000000000000000444089210, nume_2: 0.2999999999999999888977698
as you can see it is not equal

- to solve above problem we can use math.isclose()
"""
import math
print(math.isclose(num_1,num_2))

# Even in isclose functoin for below s,y it is giving False to solve problem allway pass relative tolrance and absolute tolrance in is close function
x=0.0000000001
y=0.0000000002
print(math.isclose(x,y,rel_tol=0.01,abs_tol=0.01))


"""
floor and ceiling
"""
print(math.floor(10.6))
print(math.ceil(10.4))

"""
trunc removes the numbers after decimal and return integer number
"""
print(math.trunc(10.1))
print(math.trunc(10.6))