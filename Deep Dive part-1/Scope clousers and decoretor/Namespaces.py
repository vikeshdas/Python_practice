"""
Namespace
Namespace in python is mapping of variable name and object it holds.It is basically a dictionary where key is variable name and value is object it holds.

Namespaces help avoid naming conflicts in different scope.There are different scopes like built-in scope, global scope, local scope.

Building namespace contains python built-in objects(names) like int,float,len , print() etc.

The global namespace contains variables defined at module labels.

Local namespace contains variables defined inside function or parameter of function.

The namespace of the local variable of a function is created when a function is called, not when it is defined.For every function call it creates a new Namespace. 

"""

# global variable because defined at module level
x = 0

def func():
    # assigning here to x, so it will create x as a local variable
    x = 8
    print(x)

def func1():
    # not assigning to x here, so it will use the global variable
    if x <= 0:
        print(x)

def func2():
    global x
    # this will update the global variable
    x = 20

func()
func1()
print(x)
func2()
print(x)


# global variable because defined at module level
x = 0

def func():
    print(x)  # This line causes the error
    x = 8     # This assignment makes x local to the function

func()

"""
Enclosing scope
"""
def func():
    x = 100
    # this is inner function and what ever variable is defined inside nested function will be mapped in enclising scope
    def inner_func():
        x = 200
    
    inner_func()
    print(x) #100

func()

"""
When ever python is told that variable is nonlocal it will find variable in the enclosing scope chain until it first encounter the specific variable.It will look only in local scope not in global scope
As you can see in below code in white block x is nonlocal it means it will use variable defined in upper function(yellow bloc) it is not there then it will look in red block and it find and it will make x=20

"""
def func():
    x = 100
    # to access local variable instead of enclose variable we define
    # nonlocal just like global to access module level variable
    def inner_func():
        nonlocal x  # This allows modifying the x from the enclosing function
        x = 200
    
    inner_func()
    print(x)  # 200

func()