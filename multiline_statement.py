
a=[
    4   #item one 
   ,8   #item two
   ,89
   ,9
   ,6
   ,3]

print(f"a={a}")

tpl=(2#first element
     ,4 #second element
     ,7 #third element
     )
print(f"tuple: {tpl}")

dict_1={"key_1":1
        ,"key_2":2
        ,"key_3":3}

print(dict_1)


def func(param_1 #param one 
         ,parame2 #param2
         ,param3 #param 3
         ):
    return param_1,parame2,param3

result=func(
      5
     ,2
     ,7)
print(result)


"""
multiline statement with if condition we use tab to break line in if condition
"""
a,b,c=44,85,627
if a>5\
and b>7\
and c>80:
    print("yes")
