from collections import namedtuple

# Default Docs for Named Tuples
# When we create a named tuple class, default docstrings are created
Point2D = namedtuple('Point2D', 'x y')
print(Point2D.__doc__)
# help(Point2D)

# Overriding DocStrings
# this is not unique to named tuples!
Point2D.__doc__ = 'Represents a 2D coordinate.'
Point2D.x.__doc__ = 'x coordinate'
print(Point2D.__doc__)
print(Point2D.x.__doc__)

# Default Values
# The namedtuple function does not provide us a way to define default values for each field
# Two approaches to this:

# - Using a Prototype
# Create an instance of the named tuple with default values - the prototype
# Create any additional instances of the named tuple using the prototype._replace method
# You will need to supply a default for every field (can be None)

# - Using the __defaults__ property
# Directly set the defaults of the named tuple constructor (the __new__ method)
# You do not need to specify a default for every field

# Using a Prototype
Vector2D = namedtuple('Vector2D', 'x1 y1 x2 y2 origin_x origin_y')
vector_zero = Vector2D(0, 0, 0, 0, 0, 0)
v1 = vector_zero._replace(x1=10, y1=10, x2=20, y2=20)
print(v1)

# Using __defaults__
# We need to provide defaults to the constructor of our named tuple class __new__
Vector2D.__new__.__defaults__ = (0, 0)
v2 = Vector2D(10, 10, 20, 20)
print(v2)
print('---------------------------')


def func(a, b=10, c=20):
	print(a, b, c)


func(1)
print(func.__defaults__)
func.__defaults__ = (100, 200, 300)
func()
