"""
open return oject which contains methods and attributes which can be used to manipulate the file whicha has open.

open takes two argument filet path and access mode like 'r'(read only),'w'(write) etc.we have used rt whcih means opren the file in in text mode and read only.it it is 'rb' it means open the file in binary mode.
"""
f=open("test.text",'rt')
content=f.read()    #it reads entire file 
print(content)

result=f.read(15) #read only firsts 5 charactor of the file
print(result)


#check the curson in the file after reading some charactor
print(f.tell())

# move the cursor from starting point 
f.seek(2)
print(f.read(3))
print(f.tell())

f.close()


"""if we open file sung with statement we don't need to manualy close the file.it close automaticaly"""

with open('test.text','rt') as file:
    content=file.read()
    print(content)


"""splitlines will create list of content and each item in list will be a single ine from text file.
"""
with open('test.text','rt') as file:
    content=file.read().splitlines()
    print(content)


"""
readlines: it creates list of each line and append \n wiht item in list.
"""
with open('test.text','rt') as file:
    content=file.readlines()
    print(content)

"""
read line print a line and move cursor to the next line.
"""
with open('test.text','rt') as file:
    content=file.readline()
    print(content) #print first line 
    print(content) # print second line


#print line by line using for loop
with open('test.text','rt') as file:
    for line in file:
        print(line,end="")




print("**************************write***************************************")

"""
writing to text file,it will create new test.text file if it does not exist elase it will edit in existing file.
"""
with open("test.text","w") as file:
    """
    if you do not add \n in below line second line will replace all the text in that file.
    """
    file.write("added first line at the last \n")
    file.write("added second line at the last ")


"""
if we use 'a'(append mode) instead of 'w' it would not replace whose text in text file with new added line.instead it will append new line at the end of the file.
"""
with open("test.text","a") as file:
    file.write("added fourth line at the last")
    file.write("added fifth line at the last ")