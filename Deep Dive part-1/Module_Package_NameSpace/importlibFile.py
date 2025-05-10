import sys
sys.exec_prefix

import importlib
importlib.__file__

print(importlib)

importlib.import_module('fractions')


fractions = importlib.import_module('fractions')

f = fractions.Fraction(2, 3)

print(f)

import math

print(math)


print(fractions.__spec__)

print(sys.meta_path)
importlib.util.find_spec('math')
importlib.util.find_spec('fractions')

with open('module1.py', 'w') as code_file:
    code_file.write("print('running module1.py...')\n")
    code_file.write('a = 100\n')

importlib.util.find_spec('module1')

import module1

module1.a



import os

# you can use this for Mac/Linux:
# ext_module_path = os.environ['HOME']

# you can use this in Windows 10
#ext_module_path = os.environ['HOMEPATH']

# or you can just hard code some path
# ext_module_path = 'c:\\temp' 

ext_module_path = os.environ.get('HOME', os.environ['HOMEPATH'])

print(ext_module_path)
file_abs_path = os.path.join(ext_module_path, 'module2.py')
with open(file_abs_path, 'w') as code_file:
    code_file.write("print('running module2.py...')\n")
    code_file.write("x = 'python'\n")
