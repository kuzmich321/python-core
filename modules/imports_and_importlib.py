import os
import sys
import importlib


mod_name = 'math'
math = importlib.import_module(mod_name)

print('math' in sys.modules)
print('factions' in sys.modules)
print('---------------------')

print(id(math))
print(id(sys.modules['math']))
print('---------------------')

fractions = importlib.import_module('fractions')
print(fractions)


# finders
# loaders
# finder + loader == importer

print(fractions.__spec__)
print(math.__spec__)

# contains the finder objects
print(sys.meta_path)


print(importlib.util.find_spec('decimal'))
print('---------------------')

ext_module_path = os.environ['HOME']
print(ext_module_path)

file_abs_path = os.path.join(ext_module_path, 'module2.py')
with open(file_abs_path, 'w') as code_file:
	code_file.write("print('running module2.py...')\n")
	code_file.write("x='python'")


print(importlib.util.find_spec('module2'))
print(sys.path)
sys.path.append(ext_module_path)
print(importlib.util.find_spec('module2'))
import module2