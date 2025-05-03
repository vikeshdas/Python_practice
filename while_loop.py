
"""
if condition with shile ,in below example if condition inside breaks the loops.
if 'if' condition never excute then else condition whill excute which is outside of while loop.if 'if' conidtion excutes inside the while loop then else condition whill not excute whcih is outside of while loop
"""

lst=[5,8,69,3]
val=15
idx=0
while idx<len(lst):
    if val==lst[idx]:
        print("inside if")
        break
    idx+=1

else:
    print("inside else")
    lst.append(val)

print(lst)