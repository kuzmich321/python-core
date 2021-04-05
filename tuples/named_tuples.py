from collections import namedtuple

# There's a lot to like using tuples to represent simple data structures
# The read drawback is that we have to know that the positions mean, and remember this in our code
# If we ever need to change the structure of our tuple in our code (like inserting a value that we forgot)
# most likely out code will break!

# So what if we could somehow combine these two approaches, essentially creating tuples where se can, in addition,
# give meaningful names to the positions?
# That's what <namedtuples> essentially do
# They subclass tuple, and add a layer to assign property names to the position elements

# namedtuple is a <function> which generates a new class -> class factory
# that new class inherits from tuple
# but also provides named properties to access elements of the tuple


Point2D = namedtuple('Point2D', ['x', 'y'])
# Point2D = namedtuple('Point2D', ('x', 'y'))
# Point2D = namedtuple('Point2D', 'x y')
pt = Point2D(10, 20)
print(pt.x)
print(pt[0])

x, y = pt
print(x, y)

# The rename keyword-only argument
# field names cannot start with an underscore
# Person = namedtuple('Person', 'name age _ssn')  This would now work
# <rename> argument will automatically rename any invalid field name
# uses convention: _{position in list of field names}

Person = namedtuple('Person', 'name age _ssn', rename=True)
andrey = Person('Andrey', '23', 'asd')
print(Person._fields)

# Extracting Named Tuples Values to a Dictionary
# _asdict()

print(andrey._asdict())
