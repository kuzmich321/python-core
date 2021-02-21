# A Side Note on Tuples
# What defines a tuple in Python, is not () but ,
# 1, 2, 3 -> is also a tuple -> (1, 2, 3)   --> The () are used to make the tuple clearer
# To create a tuple with a single element:
# (1) - will not work as intended --> int
# 1, or (1, ) -> tuple
# The only exception is when creating an empty tuple: () or tuple()

# Packed Values
# Packed values refers to values that are bundled together in some way
# Tuples and Lists are obvious
# Even a string considered to be a packed value
# Sets and Dictionaries are also packed values
# In fact, any iterable can be considered a packed value

# Unpacking Packed Values
# Unpacking is the act of splitting packed values into individual variables contained in a list or tuple
# a, b, c = [1, 2, 3]
# The unpacking into individual variables is based on the relative positions of each element
# Does this remind you of how positional arguments were assigned to parameters in function?

# Unpacking other iterables
# a, b, c = 10, 20, 'hello'
# a, b, c = 'XYZ'

# Simple Application of Unpacking
# swapping values of two variables
# a, b = b, a
# this works because in Python, the entire RHS is evaluated first and completely
# then assignments are made to the LHS

# Unpacking Sets and Dictionaries
# Dictionaries (and Sets) are unordered types!!!
# They can be iterated, but there is no guarantee the order of the results will match
# In practice, we rarely unpack sets and dictionaries in precisely this way

t1 = (1, 2, 3)
t2 = 1, 2, 3
t3 = (1)
t4 = (1,)
t5 = ()
print(type(t1), type(t2), type(t3), type(t4), type(t5))

a, b, c = [1, 'a', 3.14]
print(a, b, c)

a, b = (1, 2)
print(a, b)

a, b = 10, 20
a, b = b, a
print(a, b)

a, b, c = 'XYZ'
print(a, b, c)

s = {'p', 'y', 't', 'h', 'o', 'n'}
a, b, c, d, e, f = s
print(a, b, c, d, e, f)

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
a, b, c, d = d
print(a, b, c, d)

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d, a, b, c = d.items()
print(d, a, b, c)
