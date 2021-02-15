from decimal import Decimal
from fractions import Fraction

# Categories of Comparison Operators
# binary operators
# evaluate to a <bool> value

# - Identity Operations: is, is not     --> compares memory address - any tpe
# - Value Comparisons: ==, !=           --> compares values - different types OK, but must be compatible
# - Ordering Comparisons: < <= > >=     --> doesn't work for all types
# - Membership Operations: in, not in   --> used with iterable types

# Numeric Types

# Value comparisons will work with all numeric types
# Mixed types (except complex) in value and ordering comparisons is supported
# Note: Value equality operators work between floats and Decimals, but using value equality with floats has some issues!

print(10.0 == Decimal('10.0'), 0.1 == Decimal('0.1'))
print(Decimal('0.125') == Fraction(1, 8))
print(4 == 4 + 0j)

# Ordering comparisons
# Again, these work across all numeric types, except for complex numbers

print(1 < 3.14)
# print(1 + 1j < 3 + 4j)

# Chained Comparisons
# a == b == c   -->    a == b and b == c
# a < b < c     -->    a < b and b < c

print(1 < 2 < 3)
print(5 < 6 > 2)
print(1 < 2 < 3 < 4)

print('-----------------')

print([1, 2] is [1, 2])
print('a' in 'abc')
print('key' in {'key': 1})
