import sys

print('===================================')

print(f'Running main.py - module name: {__name__}')

import module1

print(module1)

module1.pprint_dict('main.globals', globals())

print(sys.path)

print(sys.modules['module1'])

print('IMPORTING MODULE1 AGAIN')
import module1

print('===================================')
