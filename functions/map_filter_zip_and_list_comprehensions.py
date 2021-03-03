# Higher order functions
# A function that takes a function as a parameter and/or returns a function as its return value
# Example: sorted

# The map function - returns an iterator that calculates the function applied to each element of the iterables
# The iterator stops as soon as one of iterables has been exhausted so, unequal length iterables can be used
l = [2, 3, 4]

print(list(map(lambda x: x**2, l)))

l1 = [1, 2, 3]
l2 = [10, 20, 30, 40]

print(list(map(lambda x, y: x + y, l1, l2)))
print('---------------------')

# The filter function - returns an iterator that contains all the elements of the iterable for which the function
# called on it is Truthy. If function is None, return the items that are true.
l = [0, 1, 2, 3, 4]

print(list(filter(None, l)))
print(list(filter(lambda n: n % 2 == 0, l)))
print('---------------------')

# The zip function
l1 = [1, 2, 3, 4]
l2 = [10, 20, 30, 40]

print(list(zip(l1, l2)))

l1 = [1, 2, 3]
l2 = [10, 20, 30]
l3 = ['a', 'b', 'c']

print(list(zip(l1, l2, l3)))

l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30]

print(list(zip(l1, l2)))

l1 = [1, 2, 3]
l2 = [10, 20, 30, 40]
l3 = 'python'
print(list(zip(l1, l2, l3)))
print('---------------------')


# List Comprehension Alternative to map
# [<expression> for <varname> in <iterable>]
l = [2, 3, 4]
print([x**2 for x in l])

l1 = [1, 2, 3]
l2 = [10, 20, 30]
print([x + y for x, y in zip(l1, l2)])

# List Comprehension Alternative to filter
# [<expression1> for <varname> in <iterable> if <expression2>]
l = [1, 2, 3, 4]
print([x for x in l if x % 2 == 0])
print('---------------------')

# Combining map and filter
l = range(10)
print(list(filter(lambda y: y < 25, map(lambda x: x**2, l))))
print([x**2 for x in range(10) if x**2 < 25])
