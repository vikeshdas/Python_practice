
a=complex(1,2)
print(a)

b=1+2j
print(a==b)


# real part:1.0 and type:'float', 
# imageinary part 2.0 and type 'float'
print(f"real part:{a.real} and type:{type(a.real)}, imageinary part {a.imag} and type:{type(a.imag)}")  


# 1+2j
print(a.conjugate)