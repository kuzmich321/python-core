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
print('-----------------------')

print(isinstance(andrey, tuple))

andrey2 = Person('Andrey', '23', 'asd')
print(andrey is andrey2, andrey == andrey2)

print(max(pt))


def dot_product_3d(a, b):
	return a.x * b.x + a.y * b.y + a.z * b.z


a = (1, 2)
b = (1, 1)
print(list(zip(a, b)))
print(sum(e[0] * e[1] for e in zip(a, b)))


def dot_product(a, b):
	return sum(e[0] * e[1] for e in zip(a, b))


pt1 = Point2D(1, 2)
pt2 = Point2D(1, 1)
print(dot_product(pt1, pt2))
print('-----------------------')

Vector3D = namedtuple('Vector3D', 'x y z')
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(1, 1, 1)

print(dot_product(v1, v2))
print(tuple(v1), v1[0], v1[0:2])

Circle = namedtuple('Circle', 'center_x center_y radius')
c = Circle(0, 0, 10)
print(c.radius)
print('-----------------------')

Stock = namedtuple('Stock', 'symbol year month day open high low close')
stock = Stock('DJIA', 2021, 1, 25, 26_313, 26_322, 26_410, 26_393)
print(stock)
for item in stock:
	print(item)

symbol, year, month, day, *_, close = stock
print(symbol, year, month, day, close)
