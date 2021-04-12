from collections import namedtuple
from pprint import pprint
import math
import fractions
import sys
import types

# What is a Module? --> objects of the type  ModuleType
print(math)
print(fractions)
print('------------------')

mod_math = globals()['math']
print(mod_math.sqrt(2))
print('------------------')

print(id(math))
import math
print(id(math))
print(id(sys.modules['math']))
print('------------------')


print(type(math))
print(type(fractions))
print(type(sys.modules))
print('------------------')


print(math.__name__)
print(math.__dict__)
f = math.__dict__['sqrt']
print(f(2))
print('------------------')


print(sys.modules['fractions'])
print(dir(fractions))
# pprint(fractions.__dict__)
print('------------------')


print(isinstance(fractions, types.ModuleType))
print(isinstance(math, types.ModuleType))

mod = types.ModuleType('Test', 'This is a test module')
print(isinstance(mod, types.ModuleType))
print(mod.__dict__)
mod.pi = 3.14
mod.hello = lambda: 'Hello!'
print(mod.__dict__)
hello = mod.hello
print('hello' in globals(), 'mod' in globals())

mod.Point = namedtuple('Point', 'x y')
p1 = mod.Point(0, 0)
p2 = mod.Point(1, 1)
print(dir(mod))

PT = getattr(mod, 'Point')
PT(20, 20)

PT = mod.__dict__['Point']
PT(20, 20)
