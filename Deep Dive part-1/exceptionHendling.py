"""
- exception vs error
Error is an unexpected event that cannot be handled at runtime. Errors can terminate your program. Most of the time, programs cannot recover from an error. Errors cannot be caught or handled
Some examples of error: 
- syntax error
- System-related issues (out of memory, stack overflow)

Exceptions are runtime errors that can be handled using try-except blocks.
Some examples of exception are:
-Divisible by zero.
-File not found
-Invalid input

"""

x=int(input("enter a number"))
y=int(input("enter second number"))
try:
    res=x/y
except Exception as e:
    print("zero division error")
else:
    print("else will excute with try not with except")
finally:
    print("finally block excute with both try and catch")


# example of FileNotFoundError: exception

with open("demo.text",'r') as f:
    try:
        content=f.read(5)
    except FileNotFoundError as e:
        print("File not exist")
    else:
        print("else will excute with try not with except")

# keyError
dic={'a':1}
print(dic['b'])