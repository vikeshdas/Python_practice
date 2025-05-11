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

"""
when we import math module first it will be check in sys.module.
"""

"""
imported module in sys.module namesapce
"""
import sys
for key in sorted(sys.modules.keys()):
    print(key)


"""
check if cmath is in sys.module
"""
print('cmath' in sys.modules) #False

from cmath import exp
# now check cmath is in global namespace
print('cmath' in globals()) # False

print('exp' in globals()) #True

# we can manually add cmath module in sys.module
sys.modules['cmath']
cmath = sys.modules['cmath']
print(globals()) #now you will be able to find cmath in global namespacae

"""
which one take more time importing import math and then sqrt funciton of math, or importing direcltry from math import sqrt
"""
from collections import namedtuple

Timings = namedtuple('Timings', 'timing_1 timing_2 abs_diff rel_diff_perc')
def compare_timings(timing1, timing2):
    rel_diff = (timing2 - timing1)/timing1 * 100
    
    timings = Timings(round(timing1, 1),
                     round(timing2, 1),
                     round(timing2 - timing1, 2),
                     round(rel_diff, 2))
    return timings


import math
from time import perf_counter


test_repeats = 10_000_000


start = perf_counter()
for _ in range(test_repeats):
    math.sqrt(2)
end = perf_counter()
elapsed_fully_qualified = end - start
print(f'Time: {elapsed_fully_qualified}')


from math import sqrt


start = perf_counter()
for _ in range(test_repeats):
    sqrt(2)
end = perf_counter()
elapsed_direct_symbol = end - start
print(f'Elapsed: {elapsed_direct_symbol}')

print(compare_timings(elapsed_fully_qualified, elapsed_direct_symbol))