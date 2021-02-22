# Extended Unpacking
# Using the * and ** operators

# The use case for *
# We don't always want to unpack every single item in an iterable
# We may, for example, want to unpack the first value, and then unpack the remaining values into another variable
# The * operator can only be used ONCE in the LHS an unpacking assignment for obvious reason
l = [1, 2, 3, 4, 5, 6]

a, b = l[0], l[1:]
print(a, b)

# Apart from cleaner syntax, it also works with any iterable, not just sequence types!
a, *b = l
print(a, b)

t = (1, 2, 3, 4, 5, 6)
a, b, *c = t
print(a, b, c)

a, b, *c, d = t
print(a, b, c, d)

a, *b, c, d = 'python'
print(a, b, c, d)

# We can use * in RHS assignment
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l = [*l1, *l2]
print(l)

# Usage with unordered types
# The * operator will work, since it works with any iterable
s = {10, -99, 3, 'd'}
a, *b, c = s
print(a, b, c)

# It is useful though in a situation where you might want to create single collection containing all the items
# of multiple sets, or all the keys of multiple dictionaries
d1 = {'p': 1, 'y': 2}
d2 = {'t': 3, 'h': 4}  # <--
d3 = {'h': 5, 'o': 6, 'n': 7}  # <-- h is in both d2 and d3
l = [*d1, *d2, *d3]
s = {*d1, *d2, *d3}
print(l, s)

print('-----------------------------')

# The ** unpacking operator
# When working with dictionaries we saw that * essentially iterated the <keys>
# Using **

d = {**d1, **d2, **d3}  # Note that the value of h in d3 "overwrote" the first value of h found in d2
print(d)

d1 = {'a': 1, 'b': 2}
print({'a': 10, 'c': 4, **d1})
print({**d1, 'a': 10, 'c': 4})

print('-----------------------------')

# Nested Unpacking
l = [1, 2, [3, 4]]
a, b, (c, d) = l
print(a, b, c, d)

a, *b, (c, d, e) = [1, 2, 3, 'XYZ']
print(a, b, c, d, e)

a, *b, (c, *d) = [1, 2, 3, 'python']
print(a, b, c, d)
