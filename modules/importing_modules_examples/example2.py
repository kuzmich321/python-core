import sys


sys.modules['test'] = lambda: 'Testing module caching'
import test

print(test())
