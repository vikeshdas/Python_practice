
d={'a':1,'b':2,'c':3,'d':4}

dic_ouput={k*2:k for k,v in d.items()}

print(dic_ouput) #{'aa': 'a', 'bb': 'b', 'cc': 'c', 'dd': 'd'}


dic_ouput={k.upper():k*2 for k,v in d.items() if v%3==0}
print(dic_ouput)