"""
Sys module used to intract with interpreter.Below are some operation where we use sys module.

- Interacting with the Python interpreter: You can access things like the version of Python running,

- Handling command-line arguments: When you run a Python script from the terminal, you can pass extra arguments

- Managing system-level operations: ou can do things like exit the program early or handle errors gracefully

"""

import sys

#chekck the verison of python 
print(sys.version)

# sys.platform is a string that tells you which operating system (OS) Python is running on.
print(sys.platform)


# directory path where Python looks for modules when you try to import something
print(sys.path)


"""
when ever we excute a command in terminal, there is general formate ,first is command then space and then first arguemnt then second argument and so on .

like : pip install ensible
- pip is command 
- install is first argument
- ensible is second argument.

so this is where sys.argv comes in place.argv is list of python which contains arguments in a command

-in our example argv[0] is pip
- argv[1] is install
- argv[2] ensible
"""
# run current python file and it will print arguments of that command.
print("All arguments:", sys.argv)
print("First argument (script name):", sys.argv[0])