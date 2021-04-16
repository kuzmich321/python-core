import os
import sys


def create_module_file(module_name, **kwargs):
	"""Create a module file named <module_name>.py
	Module has a single function (print_values) that will print
	out the supplied (stringified) kwargs
	"""

	module_file_name = f'{module_name}.py'
	module_rel_file_path = module_file_name
	module_abs_file_path  = os.path.abspath(module_rel_file_path)

	with open(module_abs_file_path, 'w') as f:
		f.write(f'# {module_name}.py\n\n')
		f.write(f"print('running {module_file_name}...')\n\n\n")
		f.write(f'def print_values():\n')
		for key, value in kwargs.items():
			f.write(f"\tprint('{str(key)}', '{str(value)}')\n")


create_module_file('test', k1=10, k2='python')


import test
print(test)
test.print_values()


create_module_file('test', k1=10, k2='python', k3='cheese')

import test
test.print_values()
print(id(test))

print('test' in sys.modules)
del sys.modules['test']


import test
print(id(test))
test.print_values()


create_module_file('test', k1=10, k2='python', k3='cheese', k4='parrots')

import importlib
importlib.reload(test)
print(id(test))
test.print_values()
