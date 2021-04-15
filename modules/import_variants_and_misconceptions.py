from collections import namedtuple
from pprint import pprint
from time import perf_counter
import math
import sys

# Case 1
# is math in sys.modules?
# if not, load it and insert ref
# add symbol math to module's global namespace referencing the same object
# if math symbol already exists in our module's namespace, replace reference
print('math' in globals())

# Case 2
import math as r_math
# is math in sys.modules?
# if not, load it and insert ref
# add symbol r_math to module's global namespace referencing the same object
# r_math symbol in namespace
# math symbol NOT in namespace
# if r_math symbol already exists in our module's namespace, replace reference
print('r_math' in globals())

# Case 3
from math import sqrt
# is math in sys.modules?
# if not, load it and insert ref
# add symbol sqrt to module's global namespace referencing math.sqrt
# math symbol not in namespace
# if sqrt symbol already exists in our module's namespace, replace reference
print('sqrt' in globals())

# Case 4
from math import sqrt as r_sqrt
# is math in sys.modules?
# if not, load it and insert ref
# add symbol r_sqrt to module's global namespace referencing math.sqrt
# math symbol not in namespace
# if r_sqrt symbol already exists in our module's namespace, replace reference
print('r_sqrt' in globals())

# Case 5
from math import *
# is math in sys.modules?
# if not, load it and insert ref
# add "all" symbols defined in math to module's global namespace
# math symbol not in namespace
# if any symbols already exists in our module's namespace, replace reference
pprint(globals())
print('---------------------')

# In EVERY case the <math> module was loaded into memory and referenced in sys.modules
# Running <from math import sqrt>
# did not "partially" load math
# it only affected WHAT symbols were placed in module's namespace!
# (i.e it loaded full math but we only have a reference to sqrt)

# Things may be different with packages, but for simple modules this is the behavior
# Why <from math import *> can lead to bugs
from cmath import *
pprint(globals()['sqrt'])
from math import *
pprint(globals()['sqrt'])

# Efficiency
# What's more efficient?
# import math OR from math import sqrt
# importing => the same amount of work
# calling => math.sqrt(2) | sqrt(2)
print('---------------------')


print('cmath' in sys.modules)
cmath = sys.modules['cmath']
print('cmath' in globals())
print(cmath.pi)

Timings = namedtuple('Timings', 'timing_1 timing_2 abs_diff rel_diff_perc')


def compare_timings(timing1, timing2):
	rel_diff = (timing2 - timing1)/timing1 * 100

	timings = Timings(round(timing1, 1), round(timing2, 1), round(timing2 - timing1, 1), round(rel_diff, 2))
	return timings


print(compare_timings(1, 2))

test_repeats = 10_000_000

import math

start = perf_counter()
for _ in range(test_repeats):
	math.sqrt(2)
end = perf_counter()
elapsed_fully_qualified = end - start


from math import sqrt

start = perf_counter()
for _ in range(test_repeats):
	sqrt(2)
end = perf_counter()
elapsed_direct_symbol = end - start

print(compare_timings(elapsed_fully_qualified, elapsed_direct_symbol))
