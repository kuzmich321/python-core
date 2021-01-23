# Throughout this course we'll encounter many data types
# Integers (int)
# Booleans (bool)
# Floats (float)
# String (str)
# Lists (list)
# Tuples (tuple)
# Sets (set)
# Dictionaries (dict)
# None (NoneType)

# We'll also see other constructs
# Operators (+, -, ==, is, ...)
# Functions
# Classes
# Types

# But the one thing in common with all these things, is that they are all objects (instances of classes)
# Functions (function)
# Classes (class) [not just instances, but the class itself]
# Types (type)

# This means they all have a memory address!

# As a consequence: Any object can be assigned to a variable... including functions...
# Any object can be passed to a function... including functions...
# Any object can be returned from a function... including functions...

a = 10
print(type(a))

b = int(10)
print(type(b))

# help(int.imag)


def square(a):
    return a ** 2


print(square, type(square))

f = square

print(hex(id(square)), hex(id(f)))

print(square(2), f(2))


def cube(a):
    return a ** 3


def select_function(fn_id):
    if fn_id == 1:
        return square
    else:
        return cube


f = select_function(1)
print(f is square)

f = select_function(2)
print(f is cube)

print(select_function(2)(3))


def exec_function(fn, n):
    return fn(n)


print(exec_function(cube, 3))
print(exec_function(square, 3))
