import operator
from functools import reduce


# Functional Equivalents to Operators
# This module is a convenience module
# You can always use your own functions and lambda expressions instead

print(operator.add(2, 3))
print(operator.mul(2, 3))
print(operator.pow(2, 3))
print(operator.mod(2, 3))
print(operator.floordiv(2, 3))
print(operator.neg(2))
print(operator.lt(2, 3))
print(operator.le(3, 3))
print(operator.gt(2, 3))
print(operator.ge(3, 3))
print(operator.eq(3, 3))
print(operator.ne(2, 3))
print(operator.is_(2, 3))
print(operator.is_not(2, 3))
print(operator.and_(2, 3))
print(operator.or_(0, 3))
print(operator.not_(0))
print(operator.concat('py', 'python'))
print(operator.contains('py', 'python'))
print(operator.countOf('py', 'python'))
print(operator.truth([]))

l = [1, 2, 3, 4, 5, 6]
s = 'python'
print(operator.getitem(l, 2))

f = operator.itemgetter(2, 4, 5)
print(f(l))
print(f(s))

# Attribute Getters
# It also returns a callable, that takes the object as an argument
my_obj = 10
print(operator.attrgetter('numerator')(my_obj))

# Calling another Callable
print(s.upper())
f = operator.attrgetter('upper')
print(f(s)())
print(operator.methodcaller('upper')(s))

print('----------------------')

print(reduce(lambda x, y: x * y, l))
print(reduce(operator.mul, l))

l = [5-10j, 3+3j, 2-100j]
print(sorted(l, key=lambda x: x.real))
print(sorted(l, key=operator.attrgetter('real')))
