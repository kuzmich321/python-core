from functools import reduce


# Reducing Functions
# These are functions that recombine an iterable recursively, ending up with a single return value
# Also called accumulators, aggregators, or folding functions.
l = [5, 8, 6, 10, 9]
print(reduce(lambda a, b: a if a > b else b, l))
print(reduce(lambda a, b: a if a < b else b, l))
print(reduce(lambda a, b: a + b, l))
print(reduce(lambda a, b: a if a < b else b, {10, 5, 2, 4}))
print(reduce(lambda a, b: a if a < b else b, 'python'))
print(reduce(lambda a, b: a + ' ' + b, ('python', 'is', 'awesome!')))

# Built-in Reducing Functions
print(max(l))
print(min(l))
print(sum(l))
print(any(l))
print(any([0, 1, 2]))
print(all(l))
print(all([0, 1, 2]))

print(reduce(lambda a, b: bool(a) or bool(b), l))
print(reduce(lambda a, b: a * b, l))

# The reduce initializer
# The reduce function has a third (optional) parameter: initializer (defaults to None)
# If specified, it's like adding it to the front of the iterable
# It's often used to provide some kind of default in case the iterable is empty
l = []
print(reduce(lambda x, y: x + y, l, 1))

l = [1, 2, 3]
print(reduce(lambda x, y: x + y, l, 1))
print(reduce(lambda x, y: x + y, l, 100))
print(reduce(lambda x, y: x + y, l, 0))
