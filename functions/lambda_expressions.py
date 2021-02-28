# What are Lambda Expressions?
# Lambda expressions are simply another way to create functions --> anonymous functions
# The syntax:
# lambda [parameter list]: expression
# returns a function object that evaluates and returns the expression when it's called
# it can be assigned to a variable
# it can be passed as an arguments to another function

# Examples
# Note that these expressions are function objects, but are not "named" --> anonymous functions
# Lambdas, or anonymous functions, are NOT equivalent to closures
lambda x: x**2
lambda x, y: x + y
lambda: 'hello'
lambda s: s[::-1].upper()

print(type(lambda x: x**2))


# Assigning a Lambda to a Variable name
my_func = lambda x: x**2
print(type(my_func))
print(my_func(3))


# Passing as an Argument to another Function
def apply_func(x, fn):
	return fn(x)


print(apply_func(3, lambda x: x + 5))

# Limitations
# The "body" of a lambda is limited to a single expression
# no assignments
# no annotations
# single <logical> line of code --> line-continuation is OK, but still just one expression


# Default Values
g = lambda x, y=10: x + y
print(g(10))

# args and kwargs can be used
f = lambda x, *args, y, **kwargs: (x, *args, y, kwargs)
print(f(1, 2, 3, y='y', a=10, b=20))

print('--------------------------')


# Lambdas and Sorting
l = [1, 5, 4, 10, 9, 6]
print(sorted(l))

l = ['c', 'B', 'D', 'a']
print(sorted(l))
print(ord('a'))
print(ord('A'))
print(sorted(l, key=lambda s: s.upper()))

d = {'def': 300, 'abc': 200, 'ghi': 100}
print(sorted(d))
print(sorted(d, key=lambda e: d[e]))


def dist_sq(x):
	return (x.real)**2 + (x.imag)**2


print(dist_sq(1+1j))

l = [3+3j, 1-1j, 0, 3+0j]
print(sorted(l, key=dist_sq))
print(sorted(l, key=lambda x: (x.real)**2 + (x.imag)**2))

l = ['Cleese', 'Idle', 'Chapman', 'Gilliam', 'Jones']
print(sorted(l))
print(sorted(l, key=lambda s: s[-1]))

l = ['Idle', 'Cleese', 'Chapman', 'Gilliam', 'Jones']
print(sorted(l, key=lambda s: s[-1]))


print('--------------------------')


# Randomize an Iterable using Sorted
from random import random
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sorted(l, key=lambda x: random()))
